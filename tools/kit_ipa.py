import sys, os, zipfile, time, plistlib
from kit_common import g, find_mods, RefConverter, save_in_app, build_reference
SRC = sys.argv[1]
OUT = os.path.splitext(SRC)[0] + " - MODDED.ipa"
APP = "Payload/GirlWars.app/Data/Raw/AssetBundles/download/"
os.system("")
GREEN, END = "\x1b[92m", "\x1b[0m"

class IpaConverter(g.Converter):
    def __init__(self, z, ref):
        super().__init__(z)
        self.map = {g.IOS_ROOT + n[len(APP):]: n for n in z.namelist() if n.startswith(APP)}
        self.names = set(self.map)
        self.ref = ref
        real_read = z.read
        class R:
            def read(_, name): return real_read(self.map[name])
        self.zip = R()

    def ios_shader(self, path_id, first_choice):
    
        if first_choice:
            for ob in self.UnityPy.load(g.split_bundle(first_choice)[1]).objects:
                if ob.type.name == "Shader" and ob.path_id == path_id:
                    return ob.get_raw_data()
        return self.ref.shader_for(self._rel, path_id)

    def convert(self, mod_bytes, rel):
        self._rel = rel
        return super().convert(mod_bytes, rel)

with zipfile.ZipFile(SRC) as zin:
    if "Payload/GirlWars.app/Info.plist" not in zin.namelist():
        sys.exit("ERROR: this is not a Girl Wars IPA.")
    names = set(zin.namelist())
    in_app = {n[len(APP):] for n in names if n.startswith(APP) and n.endswith(".assetbundle")}
    version = plistlib.loads(zin.read("Payload/GirlWars.app/Info.plist")).get("CFBundleShortVersionString", "?")
    build_reference(zin, APP, f"{version}|{os.path.getsize(SRC)}")
    ref = RefConverter()
    save_in_app(in_app, version)
    print(f"Game version {version}: {len(in_app)} files are built into the app (list saved for 'Convert Mods for iPhone').")
    conv = IpaConverter(zin, ref)
    ready = {}
    for full, rel in find_mods(ref.prefix.keys() | in_app):
        if APP + rel in names:
            ready[APP + rel], note = conv.convert(open(full, "rb").read(), rel)
            print(f"{GREEN}OK (into app) {rel} {note}{END}", flush=True)
    print(len(ready), "mods go into the app itself (the rest are copied to the phone with 'Convert Mods for iPhone').")
    INFO = "Payload/GirlWars.app/Info.plist"
    raw = zin.read(INFO)
    fmt = plistlib.FMT_BINARY if raw.startswith(b"bplist") else plistlib.FMT_XML
    pl = plistlib.loads(raw)
    pl["UIFileSharingEnabled"] = True
    pl["LSSupportsOpeningDocumentsInPlace"] = True
    ready[INFO] = plistlib.dumps(pl, fmt=fmt)
    print("File Sharing turned on (game files will show in iMazing / Files app)")
    print("Writing", OUT, "...", flush=True)
    t = time.time()
    with zipfile.ZipFile(OUT + ".part", "w") as zout:
        for info in zin.infolist():
            data = ready.get(info.filename)
            ni = zipfile.ZipInfo(info.filename, info.date_time)
            ni.external_attr = info.external_attr
            ni.create_system = info.create_system
            ni.compress_type = info.compress_type
            zout.writestr(ni, data if data is not None else zin.read(info.filename))
    os.replace(OUT + ".part", OUT)
with zipfile.ZipFile(OUT) as z:
    bad = z.testzip()
    for n, d in ready.items():
        assert z.read(n) == d, n
print("DONE in %.0fs:" % (time.time() - t), OUT, "(zip test", "OK)" if bad is None else f"FAILED {bad})")
print("Install it with Sideloadly.")
