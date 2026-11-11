"""Shared helpers for the Girl Wars iOS Mod Kit."""
import os, sys, zipfile
HERE = os.path.dirname(os.path.abspath(__file__))
KIT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import convert_core as g

MODS = os.path.join(KIT, "Put mods here")
REF = os.path.join(HERE, "ios_ref.zip")  
IN_APP_LIST = os.path.join(HERE, "in_app.txt")


def build_reference(zin, app_dir, stamp):
   
    if os.path.isfile(REF):
        try:
            with zipfile.ZipFile(REF) as z:
                if z.read("STAMP").decode() == stamp:
                    print("iOS reference: already built from this IPA.", flush=True)
                    return
        except Exception:
            pass
    import UnityPy
    names = [n for n in zin.namelist() if n.startswith(app_dir) and n.endswith(".assetbundle")]
    print(f"Building the iOS reference from your IPA ({len(names)} files, a few minutes, only once)...", flush=True)
    prefix, per_file, counts = {}, {}, {}
    for i, n in enumerate(names, 1):
        rel = n[len(app_dir):]
        pre, body = g.split_bundle(zin.read(n))
        prefix[rel] = pre
        try:
            for ob in UnityPy.load(body).objects:
                if ob.type.name == "Shader":
                    raw = ob.get_raw_data()
                    per_file[(rel, ob.path_id)] = raw
                    c = counts.setdefault(ob.path_id, {})
                    c[raw] = c.get(raw, 0) + 1
        except Exception as e:
            print("   (skipped shaders of", rel, "-", e, ")")
        if i % 200 == 0:
            print(f"   {i}/{len(names)}", flush=True)
    common = {pid: max(c, key=c.get) for pid, c in counts.items()}
    with zipfile.ZipFile(REF + ".part", "w", zipfile.ZIP_DEFLATED) as z:
        for rel, pre in prefix.items():
            z.writestr("prefix/" + rel, pre)
        for pid, raw in common.items():
            z.writestr(f"shader/{pid}", raw)
        for (rel, pid), raw in per_file.items():
            if raw != common[pid]:
                z.writestr(f"fshader/{rel}|{pid}", raw)
        z.writestr("STAMP", stamp)
    os.replace(REF + ".part", REF)
    print(f"iOS reference saved: {len(prefix)} files, {len(common)} shaders.", flush=True)


def load_in_app():
   
    if not os.path.isfile(IN_APP_LIST):
        return None, None
    text, src = open(IN_APP_LIST, encoding="utf-8").read(), "your IPA"
    lines = text.splitlines()
    if lines and lines[0].startswith("#"):
        src += f" (game {lines[0][1:].strip()})"
    return {l.strip() for l in lines if l.strip() and not l.startswith("#")}, src


def save_in_app(paths, version):
    with open(IN_APP_LIST, "w", encoding="utf-8") as f:
        f.write(f"# {version}\n" + "\n".join(sorted(paths)) + "\n")


class RefConverter(g.Converter):
  
    def __init__(self, ref_path=REF):
        import UnityPy
        self.UnityPy = UnityPy
        self.names = set()
        self.prefix, self.shaders, self.fshaders = {}, {}, {}
        self._rel = None
        with zipfile.ZipFile(ref_path) as z:
            for n in z.namelist():
                if n.startswith("prefix/"):
                    self.prefix[n[7:]] = z.read(n)
                elif n.startswith("shader/"):
                    self.shaders[int(n[7:])] = z.read(n)
                elif n.startswith("fshader/"):
                    rel, pid = n[8:].rsplit("|", 1)
                    self.fshaders[(rel, int(pid))] = z.read(n)

    def shader_for(self, rel, path_id):

        return self.fshaders.get((rel, path_id), self.shaders.get(path_id))

    def ios_original(self, rel):
        return None

    def ios_shader(self, path_id, first_choice):
        return self.shader_for(self._rel, path_id)

    def convert(self, mod_bytes, rel):
        self._rel = rel
        data, note = super().convert(mod_bytes, rel)
        if note == "already iOS":
            return data, note
        note = note.replace(", NEW file (your iPhone doesn't have this one yet)", "")
        pre = self.prefix.get(rel)
        if pre is None: 
            pre = g.split_bundle(mod_bytes)[0]
        return pre + data, note


_containers = {}


def _container_keys(path):
    if path not in _containers:
        import UnityPy
        try:
            env = UnityPy.load(g.split_bundle(open(path, "rb").read())[1])
            _containers[path] = [k.lower() for k in env.container.keys()]
        except Exception:
            _containers[path] = []
    return _containers[path]


def _bundle_in_folder(path, folder):
   
    want = f"assets/download/{folder}/".lower()
    return any(k.startswith(want) for k in _container_keys(path))


def folder_from_bundle(path, fn):

    stem = fn[: -len(".assetbundle")].lower()
    votes = {}
    for k in _container_keys(path):
        if not k.startswith("assets/download/"):
            continue
        parts = k[len("assets/download/"):].split("/")
        if stem in parts[1:]:
            folder = "/".join(parts[: parts.index(stem, 1)])
            votes[folder] = votes.get(folder, 0) + 1
    return max(votes, key=votes.get) if votes else None


def find_mods(ref_names):

    by_name = {}
    for r in ref_names:
        by_name.setdefault(r.rsplit("/", 1)[-1], []).append(r)
    for dp, _, files in os.walk(MODS):
        for fn in files:
            if not fn.endswith(".assetbundle"):
                continue
            full = os.path.join(dp, fn)
            rel = os.path.relpath(full, MODS).replace(os.sep, "/")
            if "/" in rel:
                yield full, rel
                continue
            folder = folder_from_bundle(full, fn)  
            if folder:
                yield full, f"{folder}/{fn}"
                continue
            hits = by_name.get(fn, [])
            if len(hits) > 1:  
                hits = [h for h in hits if _bundle_in_folder(full, h.rsplit("/", 1)[0])] or hits
            if len(hits) == 1:
                yield full, hits[0]
            elif not hits:
                print(f"?? {fn}: unknown game file. Put it in its folder, e.g. Put mods here\\ui\\uiprefabandres\\{fn}")
            else:
                print(f"?? {fn}: this name exists in several game folders. Move it into the right one:")
                for h in hits:
                    print("      Put mods here\\" + h.replace("/", "\\"))
