#!/usr/bin/env python3
import json, os, shutil, subprocess, tempfile, zipfile, re
from pathlib import Path

ROOT=Path(".")
ZIPS=[ROOT/x for x in ["01_core_dex.zip","02_dex_3_4.zip","03_dex5_lib_assets.zip","04_remaining_resources.zip"]]
EXPECTED="com.cerebellummobileapp"
WORK=Path(tempfile.mkdtemp(prefix="cerebellum-archive-probe-"))
MERGED=WORK/"merged"
APK=WORK/"candidate.apk"
DECODED=WORK/"decoded"
JADX=WORK/"jadx"
MERGED.mkdir()

inventory={}
for zp in ZIPS:
    with zipfile.ZipFile(zp) as z:
        names=z.namelist()
        inventory[zp.name]={"members":len(names),"bytes":zp.stat().st_size}
        for n in names:
            if not n or n.endswith("/"): continue
            dest=MERGED/n
            dest.parent.mkdir(parents=True,exist_ok=True)
            with z.open(n) as src, open(dest,"wb") as dst:
                shutil.copyfileobj(src,dst)

key_paths={}
for pattern in ["AndroidManifest.xml","resources.arsc","classes.dex","classes*.dex","assets/index.android.bundle"]:
    key_paths[pattern]=[str(p.relative_to(MERGED)) for p in MERGED.rglob("*") if p.is_file() and (p.name==pattern or (pattern.endswith("*.dex") and re.fullmatch(r"classes\d*\.dex",p.name)) or (pattern=="assets/index.android.bundle" and str(p.relative_to(MERGED)).endswith(pattern)))][:50]

# Build an APK-shaped zip only if core members exist.
manifest=next((MERGED/p for p in key_paths["AndroidManifest.xml"] if (MERGED/p).exists()),None)
dex=list(MERGED.rglob("classes*.dex"))+([MERGED/"classes.dex"] if (MERGED/"classes.dex").exists() else [])
if manifest and dex:
    subprocess.run(["zip","-qr",str(APK),"."],cwd=MERGED,check=True)
else:
    APK=None

package=None
apktool_status="NOT_RUN"
jadx_status="NOT_RUN"
main_sources=[]
if APK:
    subprocess.run(["apktool","d","--force",str(APK),"-o",str(DECODED)],check=False,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    dm=DECODED/"AndroidManifest.xml"
    if dm.exists():
        txt=dm.read_text(errors="replace")
        m=re.search(r'package="([^"]+)"',txt)
        package=m.group(1) if m else None
        apktool_status="DECODED"
    else:
        apktool_status="DECODE_FAILED"

if package==EXPECTED:
    subprocess.run(["jadx","-d",str(JADX),str(APK)],check=False,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    for p in JADX.rglob("MainActivity.java"):
        if "com/cerebellummobileapp" in str(p): main_sources.append(str(p))
    for p in JADX.rglob("MainApplication.java"):
        if "com/cerebellummobileapp" in str(p): main_sources.append(str(p))
    jadx_status="RUN"

report={
 "status":"PASS_CEREBELLUM_PACKAGE" if package==EXPECTED else "BLOCKED_PACKAGE_MISMATCH_OR_DECODE_FAILURE",
 "expected_package":EXPECTED,
 "decoded_package":package,
 "inventory":inventory,
 "key_paths":key_paths,
 "apk_assembled":APK is not None,
 "apktool_status":apktool_status,
 "jadx_status":jadx_status,
 "verified_main_sources":main_sources,
 "marrow_block":"reconstruction/apk_root is excluded entirely"
}
out=ROOT/"reconstruction/analysis/cerebellum_archive_identity_probe.json"
out.write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
if package!=EXPECTED: raise SystemExit(3)
