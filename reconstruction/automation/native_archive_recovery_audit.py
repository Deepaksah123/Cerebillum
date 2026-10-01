#!/usr/bin/env python3
import json, pathlib, subprocess, re, os
root=pathlib.Path(".")
zips=["01_core_dex.zip","02_dex_3_4.zip","03_dex5_lib_assets.zip","04_remaining_resources.zip"]
patterns=re.compile(r"(?:^|/)(?:build\.gradle(?:\.kts)?|settings\.gradle(?:\.kts)?|gradlew|gradle\.properties|AndroidManifest\.xml|apktool\.yml|.*\.smali|.*\.java|.*\.kt|.*\.aidl|.*\.xml)$",re.I)
all_hits=[]
summ={}
for z in zips:
    p=root/z
    if not p.exists():
        summ[z]={"exists":False}
        continue
    out=subprocess.check_output(["unzip","-Z1",str(p)],text=True,errors="replace")
    members=[x.strip() for x in out.splitlines() if x.strip()]
    hits=[x for x in members if patterns.search(x)]
    summ[z]={"exists":True,"bytes":p.stat().st_size,"members":len(members),"source_like_hits":len(hits)}
    all_hits.extend((z,x) for x in hits)
# Also inspect the already-extracted APK root.
apk=pathlib.Path("reconstruction/apk_root")
apk_paths=[]
if apk.exists():
    for p in apk.rglob("*"):
        if p.is_file():
            s=str(p)
            if re.search(r"\\.(?:java|kt|smali|gradle|kts)$",s,re.I) or p.name in {"build.gradle","settings.gradle","apktool.yml"}:
                apk_paths.append(s)
result={
 "archive_inventory":summ,
 "source_like_members":all_hits[:2000],
 "source_like_member_count":len(all_hits),
 "extracted_apk_source_files":apk_paths[:500],
 "extracted_apk_source_file_count":len(apk_paths),
 "rebuildable_android_source_found":bool(all_hits or apk_paths),
 "note":"Archive membership is evidence only; source-like filenames must still be inspected for actual rebuildability."
}
pathlib.Path("reconstruction/analysis/native_archive_recovery_audit.json").write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
