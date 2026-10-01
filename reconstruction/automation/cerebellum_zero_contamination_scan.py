#!/usr/bin/env python3
import json, re
from pathlib import Path

ROOT=Path(".")
FORBIDDEN=[
    "com.marrow","com.marrow2","Marrow2","Marrow","marrow_content",
]
EXCLUDED_PREFIXES=(
    "reconstruction/analysis/",
    "reconstruction/forensics/",
    "reconstruction/apk_root/",
    ".git/",
)
EXCLUDED_FILES={
    "01_core_dex.zip","02_dex_3_4.zip","03_dex5_lib_assets.zip","04_remaining_resources.zip"
}
CANDIDATE_PREFIXES=("app/","android/","src/","native/","reconstruction/native/","reconstruction/build/")
TEXT_EXT={".kt",".java",".xml",".gradle",".kts",".properties",".json",".js",".jsx",".ts",".tsx",".smali",".txt",".md"}

hits=[]
scanned=[]
quarantined_apk_root_exists=Path("reconstruction/apk_root").exists()
for p in ROOT.rglob("*"):
    if not p.is_file() or p.name in EXCLUDED_FILES: continue
    s=p.as_posix()
    if s.startswith(EXCLUDED_PREFIXES): continue
    if not (s.startswith(CANDIDATE_PREFIXES) or p.name in {"AndroidManifest.xml","settings.gradle","build.gradle","build.gradle.kts","gradlew"}):
        continue
    if p.suffix.lower() not in TEXT_EXT and p.name!="AndroidManifest.xml": continue
    try: data=p.read_text(errors="replace")
    except Exception: continue
    scanned.append(s)
    for token in FORBIDDEN:
        if token.lower() in data.lower():
            hits.append({"path":s,"token":token})

report={
    "status":"PASS_ZERO_MARROW_IDENTIFIERS" if not hits else "BLOCKED_MARROW_CONTAMINATION",
    "scanned_files":len(scanned),
    "quarantined_marrow_tree_present":quarantined_apk_root_exists,
    "hits":hits,
    "rule":"No Marrow identifiers may enter promoted Cerebellum native/build candidates.",
    "excluded_evidence":"analysis/forensics and reconstruction/apk_root are quarantined evidence-only trees and are never promoted to Cerebellum implementation candidates."
}
out=ROOT/"reconstruction/analysis/cerebellum_zero_contamination_scan.json"
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
if hits: raise SystemExit(4)
