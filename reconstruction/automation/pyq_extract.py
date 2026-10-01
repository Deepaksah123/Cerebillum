#!/usr/bin/env python3
import json, os, re, hashlib, subprocess
from pathlib import Path
from collections import defaultdict

SRC=Path("source_repo/frontend/quizx/Brain/Cerebellum")
PYQ=SRC/"PYQs"
QB=SRC/"qBank"
OUT=Path("reconstruction/generated/pyq")
OUT.mkdir(parents=True,exist_ok=True)

def norm(s):
    s=re.sub(r"<[^>]+>"," ",str(s or ""))
    s=re.sub(r"[^a-z0-9]+"," ",s.lower())
    return re.sub(r"\s+"," ",s).strip()

def load_json(p):
    try:
        with p.open(encoding="utf-8") as f: return json.load(f)
    except Exception: return None

# Build a conservative subject index from qBank content. Exact normalized question
# matches are accepted; fuzzy matches are reported separately and never auto-assigned.
exact={}
for p in QB.rglob("*.json"):
    data=load_json(p)
    if data is None: continue
    rows=data if isinstance(data,list) else data.get("questions",data.get("data",[]))
    if not isinstance(rows,list): continue
    subject=p.relative_to(QB).parts[0] if p.relative_to(QB).parts else p.parent.name
    for row in rows:
        if not isinstance(row,dict): continue
        q=row.get("question") or row.get("question_text") or row.get("text")
        k=norm(q)
        if k and len(k)>=20:
            exact.setdefault(k,set()).add(subject)

summary=defaultdict(lambda:{"files":0,"questions":0,"subject_mapped":0,"unresolved":0,"ambiguous":0})
records=[]
for p in sorted(PYQ.rglob("*.json")):
    data=load_json(p)
    if data is None: continue
    rows=data.get("questions",[]) if isinstance(data,dict) else data
    if not isinstance(rows,list): rows=[]
    rel=p.relative_to(PYQ)
    year=rel.parts[0] if rel.parts else "Unknown"
    key=f"{year}/{p.stem}"
    summary[year]["files"]+=1
    summary[year]["questions"]+=len(rows)
    for i,row in enumerate(rows):
        if not isinstance(row,dict): continue
        q=row.get("question") or row.get("question_text") or row.get("text") or ""
        subjects=sorted(exact.get(norm(q),set()))
        status="MAPPED_EXACT" if len(subjects)==1 else ("AMBIGUOUS_EXACT" if len(subjects)>1 else "UNRESOLVED")
        if status=="MAPPED_EXACT": summary[year]["subject_mapped"]+=1
        elif status=="AMBIGUOUS_EXACT": summary[year]["ambiguous"]+=1
        else: summary[year]["unresolved"]+=1
        records.append({
            "source_file":str(rel).replace(os.sep,"/"),
            "source_index":i,
            "source_id":row.get("id") or row.get("question_id"),
            "year":year,
            "subject_candidates":subjects,
            "classification_status":status,
            "question_hash":hashlib.sha256(norm(q).encode()).hexdigest(),
            "source_record":row
        })

(Path(OUT/"pyq_records.json")).write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding="utf-8")
(Path(OUT/"pyq_year_summary.json")).write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding="utf-8")
(Path(OUT/"pyq_audit.json")).write_text(json.dumps({
    "source_files":sum(v["files"] for v in summary.values()),
    "questions":sum(v["questions"] for v in summary.values()),
    "mapped_exact":sum(v["subject_mapped"] for v in summary.values()),
    "ambiguous_exact":sum(v["ambiguous"] for v in summary.values()),
    "unresolved":sum(v["unresolved"] for v in summary.values()),
    "policy":"Only unique exact question-text matches can auto-map subjects. Ambiguous/unresolved records remain source-preserved and are not guessed."
},ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps({
    "files":sum(v["files"] for v in summary.values()),
    "questions":sum(v["questions"] for v in summary.values()),
    "mapped_exact":sum(v["subject_mapped"] for v in summary.values()),
    "ambiguous_exact":sum(v["ambiguous"] for v in summary.values()),
    "unresolved":sum(v["unresolved"] for v in summary.values())
},indent=2))
