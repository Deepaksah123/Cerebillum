#!/usr/bin/env python3
import json, os, re, shutil, subprocess, zipfile
from pathlib import Path

ROOT=Path(".")
OUT=ROOT/"reconstruction/cerebellum_native_verified"
REPORT=ROOT/"reconstruction/analysis/cerebellum_archive_native_recovery.json"
ZIPS=[ROOT/x for x in ["01_core_dex.zip","02_dex_3_4.zip","03_dex5_lib_assets.zip","04_remaining_resources.zip"]]
EXPECTED="com.cerebellummobileapp"

def strings_bytes(b):
    return set(re.findall(rb"[A-Za-z0-9_.$/-]{6,}", b))

inventory={}
manifest_candidates=[]
source_hits=[]
bundle_hits=[]
for zp in ZIPS:
    if not zp.exists():
        inventory[zp.name]={"exists":False}
        continue
    with zipfile.ZipFile(zp) as z:
        names=z.namelist()
        inventory[zp.name]={"exists":True,"bytes":zp.stat().st_size,"members":len(names)}
        for n in names:
            bn=n.rsplit("/",1)[-1]
            if bn=="AndroidManifest.xml":
                manifest_candidates.append((zp,n))
            if re.search(r"(^|/)sources/com/cerebellummobileapp/(MainActivity|MainApplication)\.java$",n):
                source_hits.append((zp,n))
            if n.endswith("resources/assets/index.android.bundle") or n.endswith("assets/index.android.bundle"):
                bundle_hits.append((zp,n))

manifest_evidence=[]
for zp,n in manifest_candidates:
    with zipfile.ZipFile(zp) as z:
        b=z.read(n)
    ss=strings_bytes(b)
    found=EXPECTED.encode() in b or any(EXPECTED.encode() in x for x in ss)
    manifest_evidence.append({"archive":zp.name,"member":n,"bytes":len(b),"expected_package_found":found})

status="BLOCKED_NO_VERIFIED_ARCHIVE_HOST"
reason="No archive member has yet been proven to contain the Cerebellum package identity."
if any(x["expected_package_found"] for x in manifest_evidence):
    status="CEREBELLUM_ARCHIVE_IDENTITY_VERIFIED"
    reason="Archive manifest evidence contains com.cerebellummobileapp."

if status=="CEREBELLUM_ARCHIVE_IDENTITY_VERIFIED":
    OUT.mkdir(parents=True,exist_ok=True)
    # Extract only exact Cerebellum package/source/bundle paths; never copy generic or Marrow paths.
    for zp,n in source_hits+bundle_hits:
        with zipfile.ZipFile(zp) as z:
            rel=n
            dest=OUT/rel
            dest.parent.mkdir(parents=True,exist_ok=True)
            dest.write_bytes(z.read(n))
    # Extract only the verified manifest candidate.
    for m in manifest_evidence:
        if m["expected_package_found"]:
            zp=ROOT/m["archive"]
            with zipfile.ZipFile(zp) as z:
                dest=OUT/"resources/AndroidManifest.xml"
                dest.parent.mkdir(parents=True,exist_ok=True)
                dest.write_bytes(z.read(m["member"]))
            break

report={
 "status":status,
 "reason":reason,
 "expected_package":EXPECTED,
 "inventory":inventory,
 "manifest_evidence":manifest_evidence,
 "source_hits":[[a.name,n] for a,n in source_hits],
 "bundle_hits":[[a.name,n] for a,n in bundle_hits],
 "output":str(OUT) if OUT.exists() else None,
 "marrow_block":"reconstruction/apk_root is never read or copied by this workflow"
}
REPORT.parent.mkdir(parents=True,exist_ok=True)
REPORT.write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
if status!="CEREBELLUM_ARCHIVE_IDENTITY_VERIFIED":
    raise SystemExit(2)
