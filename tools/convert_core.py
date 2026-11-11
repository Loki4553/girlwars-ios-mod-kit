"""Girl Wars iOS Mod Kit - conversion core.

Turns an Android Girl Wars mod file (.assetbundle) into the iOS format:
sets the bundle's platform to iOS, swaps Android shaders for the iOS ones,
and checks the result. The kit's other scripts supply the iOS data.
"""
import struct
import warnings

warnings.filterwarnings("ignore")

IOS_ROOT = "Container/Documents/download/"
PLATFORM_PATTERN = b"2020.2.1f1\x00\x0d\x00\x00\x00"  # Unity version + Android (13)
IOS_PLATFORM = 9


def split_bundle(data):
    j = data.find(b"UnityFS")
    if j < 0:
        raise ValueError("not a Unity asset bundle")
    o = j + 12
    o = data.index(b"\0", o) + 1
    o = data.index(b"\0", o) + 1
    size = struct.unpack(">q", data[o:o + 8])[0]
    return data[:j], data[j:j + size]


def platforms(env):
    return {int(sf.target_platform)
            for f in env.files.values()
            for sf in getattr(f, "files", {}).values()
            if hasattr(sf, "target_platform")}


def object_counts(env):
    counts = {}
    for ob in env.objects:
        counts[ob.type.name] = counts.get(ob.type.name, 0) + 1
    return counts


class Converter:

    def __init__(self, source):
        import UnityPy
        self.UnityPy = UnityPy
        self.zip = source
        self.names = set(source.namelist())

    def ios_original(self, rel):
        name = IOS_ROOT + rel
        return self.zip.read(name) if name in self.names else None

    def ios_shader(self, path_id, first_choice):
        raise NotImplementedError

    def convert(self, mod_bytes, rel):
        """Return (ios_bytes, note)."""
        ios = self.ios_original(rel)
        _, body = split_bundle(mod_bytes)
        prefix = split_bundle(ios)[0] if ios else b""
        env = self.UnityPy.load(body)
        if platforms(env) == {IOS_PLATFORM}:
            return mod_bytes, "already iOS"
        before = object_counts(env)
        swapped = 0
        for ob in env.objects:
            if ob.type.name == "Shader":
                data = self.ios_shader(ob.path_id, ios)
                if data is None:
                    raise RuntimeError("no matching iOS shader found")
                ob.set_raw_data(data)
                swapped += 1
        bundle = list(env.files.values())[0]
        bundle._changed = True
        for f in bundle.files.values():
            f._changed = True
        raw = bytearray(bundle.save(packer="none"))
        hits, i = [], raw.find(PLATFORM_PATTERN)
        while i >= 0:
            hits.append(i)
            i = raw.find(PLATFORM_PATTERN, i + 1)
        if not hits:
            raise RuntimeError("platform field not found (different Unity version?)")
        for h in hits:
            raw[h + len(PLATFORM_PATTERN) - 4] = IOS_PLATFORM
        env2 = self.UnityPy.load(bytes(raw))
        b2 = list(env2.files.values())[0]
        b2._changed = True
        packed = b2.save(packer="lz4")
        check = self.UnityPy.load(packed)
        if platforms(check) != {IOS_PLATFORM}:
            packed = bytes(raw)
            check = self.UnityPy.load(packed)
        if platforms(check) != {IOS_PLATFORM} or object_counts(check) != before:
            raise RuntimeError("verification failed after conversion")
        note = "converted" + (", iOS shader swapped" if swapped else "")
        return prefix + packed, note
