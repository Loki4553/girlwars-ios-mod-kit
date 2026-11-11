import os, shutil
from kit_common import RefConverter, find_mods, load_in_app, KIT, REF
OUT = os.path.join(KIT, "iPhone Ready")
os.system("")
GREEN, BLUE, END = "\x1b[92m", "\x1b[94m", "\x1b[0m"
in_app, src = load_in_app()
if in_app is None or not os.path.isfile(REF):
    print("STOP: run 'Make Modded IPA.bat' first.")
    print()
    print("Drag your decrypted Girl Wars .ipa onto 'Make Modded IPA.bat'. It reads the iPhone")
    print("data this step needs from YOUR IPA (which files are built in, iOS shaders) and saves it.")
    print("(Do it again whenever you use a new game version.)")
    raise SystemExit(1)
conv = RefConverter()
print("Built-in file list:", src, "\n", flush=True)
if os.path.isdir(OUT):
    shutil.rmtree(OUT)
ok = failed = 0
also_app = []
for full, rel in find_mods(conv.prefix.keys() | in_app):
    try:
        data, note = conv.convert(open(full, "rb").read(), rel)
    except Exception as e:
        failed += 1
        print("FAILED", rel, "-", e)
        continue
    dst = os.path.join(OUT, "download", *rel.split("/"))
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    open(dst, "wb").write(data)
    ok += 1
    if rel in in_app:
        also_app.append(rel)
        print(f"{GREEN}OK {rel} ({note}){END}  {BLUE}INSIDE THE IPA{END}", flush=True)
    else:
        print(f"{GREEN}OK {rel} ({note}){END}", flush=True)
print(f"\nDONE: {ok} converted, {failed} failed.")
if ok:
    print("Now copy the files from the 'iPhone Ready\\download' folder into the SAME subfolder of")
    print("Girl Wars > Documents > download on your iPhone (one subfolder at a time, choose Replace).")
    print("NEVER replace the whole 'download' folder - that deletes the game's files.")
if also_app:
    print()
    print(f"{len(also_app)} mod(s) are for files {BLUE}INSIDE THE IPA{END}:")
    for r in also_app:
        print("   -", r)
    print("-> They go into the game with 'Make Modded IPA' (then install that IPA with Sideloadly).")
    print("   If they were in 'Put mods here' when you made your MODDED.ipa, they are already in it.")
    print("-> Copy them to the phone too ONLY if the phone asks to Replace that file.")
