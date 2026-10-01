#!/usr/bin/env python3
import json, os, re, hashlib
from pathlib import Path
from collections import defaultdict, Counter

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

# Build both a raw ID index and a strict folder-level canonical ID profile.
subject_id_to_subject=defaultdict(set)
subject_id_counts_by_subject=defaultdict(Counter)
exact=defaultdict(set)

for p in QB.rglob("*.json"):
    data=load_json(p)
    if data is None: continue
    rows=data if isinstance(data,list) else data.get("questions",data.get("data",[]))
    if not isinstance(rows,list): continue
    rel=p.relative_to(QB)
    subject=rel.parts[0] if rel.parts else p.parent.name
    for row in rows:
        if not isinstance(row,dict): continue
        sids=[]
        for sid in row.get("subjects_id") or []:
            try: sids.append(int(sid))
            except (TypeError,ValueError): pass
        for sid in sids:
            subject_id_to_subject[sid].add(subject)
            subject_id_counts_by_subject[subject][sid]+=1
        q=row.get("question") or row.get("question_text") or row.get("text")
        k=norm(q)
        if k and len(k)>=20:
            exact[k].add(subject)

# A canonical ID is accepted only when the subject folder has a unique ID
# accounting for >=80% of its tagged rows, and that ID is canonical for only
# one subject folder. This is source-derived metadata, not a guessed subject.
subject_canonical_id={}
canonical_id_to_subject=defaultdict(list)
for subject, counts in subject_id_counts_by_subject.items():
    total=sum(counts.values())
    if not total: continue
    top=counts.most_common()
    if len(top)==1 or top[0][1] > top[1][1]:
        sid,n=top[0]
        if n/total >= 0.80:
            subject_canonical_id[subject]=sid
            canonical_id_to_subject[sid].append(subject)
canonical_id_to_subject={sid:subs for sid,subs in canonical_id_to_subject.items() if len(subs)==1}
canonical_subject_by_id={sid:subs[0] for sid,subs in canonical_id_to_subject.items()}

summary=defaultdict(lambda:{"files":0,"questions":0,"subject_id_mapped":0,"canonical_subject_id_mapped":0,"exact_mapped":0,"subject_mapped":0,"unresolved":0,"ambiguous":0})
records=[]

for p in sorted(PYQ.rglob("*.json")):
    data=load_json(p)
    if data is None: continue
    rows=data.get("questions",[]) if isinstance(data,dict) else data
    if not isinstance(rows,list): rows=[]
    rel=p.relative_to(PYQ)
    year=rel.parts[0] if rel.parts else "Unknown"
    summary[year]["files"]+=1
    summary[year]["questions"]+=len(rows)

    for i,row in enumerate(rows):
        if not isinstance(row,dict): continue
        q=row.get("question") or row.get("question_text") or row.get("text") or ""

        source_sids=[]
        for sid in row.get("subjects_id") or []:
            try: source_sids.append(int(sid))
            except (TypeError,ValueError): pass

        raw_candidates=set()
        id_evidence={}
        for sid in source_sids:
            candidates=subject_id_to_subject.get(sid,set())
            id_evidence[str(sid)]=sorted(candidates)
            raw_candidates.update(candidates)

        canonical_candidates={canonical_subject_by_id[sid] for sid in source_sids if sid in canonical_subject_by_id}
        if source_sids and len(canonical_candidates)==1 and all(sid in canonical_subject_by_id for sid in source_sids):
            subjects=sorted(canonical_candidates)
            status="MAPPED_SUBJECT_ID_CANONICAL"
            summary[year]["canonical_subject_id_mapped"]+=1
            summary[year]["subject_id_mapped"]+=1
        elif source_sids and len(raw_candidates)==1 and all(len(subject_id_to_subject.get(sid,set()))==1 for sid in source_sids):
            subjects=sorted(raw_candidates)
            status="MAPPED_SUBJECT_ID"
            summary[year]["subject_id_mapped"]+=1
        else:
            subjects=sorted(exact.get(norm(q),set()))
            if len(subjects)==1:
                status="MAPPED_EXACT"
                summary[year]["exact_mapped"]+=1
            elif len(subjects)>1:
                status="AMBIGUOUS_EXACT"
            else:
                status="UNRESOLVED"

        if status in ("MAPPED_SUBJECT_ID_CANONICAL","MAPPED_SUBJECT_ID","MAPPED_EXACT"):
            summary[year]["subject_mapped"]+=1
        elif status=="AMBIGUOUS_EXACT":
            summary[year]["ambiguous"]+=1
        else:
            summary[year]["unresolved"]+=1

        records.append({
            "source_file":str(rel).replace(os.sep,"/"),
            "source_index":i,
            "source_id":row.get("id") or row.get("question_id"),
            "year":year,
            "source_subject_ids":source_sids,
            "subject_id_evidence":id_evidence,
            "subject_candidates":subjects,
            "classification_status":status,
            "question_hash":hashlib.sha256(norm(q).encode()).hexdigest(),
            "source_record":row
        })

audit={
    "source_files":sum(v["files"] for v in summary.values()),
    "questions":sum(v["questions"] for v in summary.values()),
    "mapped_subject_id":sum(v["subject_id_mapped"] for v in summary.values()),
    "mapped_canonical_subject_id":sum(v["canonical_subject_id_mapped"] for v in summary.values()),
    "mapped_exact":sum(v["exact_mapped"] for v in summary.values()),
    "mapped_total":sum(v["subject_mapped"] for v in summary.values()),
    "ambiguous_exact":sum(v["ambiguous"] for v in summary.values()),
    "unresolved":sum(v["unresolved"] for v in summary.values()),
    "subject_id_index_entries":len(subject_id_to_subject),
    "canonical_subject_count":len(canonical_subject_by_id),
    "canonical_subject_by_id":{str(k):v for k,v in sorted(canonical_subject_by_id.items())},
    "policy":"Use source subjects_id directly when uniquely mapped in QBank. For IDs colliding across QBank folders, use only a strict folder-level canonical ID when that folder has a unique ID accounting for >=80% of its tagged rows and that ID is canonical for exactly one folder. Otherwise use unique exact normalized question-text mapping; never guess ambiguous/unresolved records."
}

(Path(OUT/"pyq_records.json")).write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding="utf-8")
(Path(OUT/"pyq_year_summary.json")).write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding="utf-8")
(Path(OUT/"pyq_audit.json")).write_text(json.dumps(audit,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps(audit,indent=2))
