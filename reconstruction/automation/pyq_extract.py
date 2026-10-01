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

def to_int(v):
    try: return int(v)
    except (TypeError,ValueError): return None

def load_json(p):
    try:
        with p.open(encoding="utf-8") as f: return json.load(f)
    except Exception: return None

# Build source-derived indexes from Cerebellum qBank.
subject_id_to_subject=defaultdict(set)
subject_id_counts_by_subject=defaultdict(Counter)
qbank_id_to_subject=defaultdict(set)
qbank_unique_key_to_subject=defaultdict(set)
qbank_map_id_to_subject=defaultdict(set)
qbank_choice_id_to_subject=defaultdict(set)
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
            n=to_int(sid)
            if n is not None: sids.append(n)
        for sid in sids:
            subject_id_to_subject[sid].add(subject)
            subject_id_counts_by_subject[subject][sid]+=1

        rid=to_int(row.get("id"))
        if rid is not None: qbank_id_to_subject[rid].add(subject)
        uk=row.get("unique_key")
        if uk: qbank_unique_key_to_subject[str(uk)].add(subject)
        mid=to_int(row.get("map_id"))
        if mid is not None: qbank_map_id_to_subject[mid].add(subject)
        for choice in row.get("choices") or []:
            if isinstance(choice,dict):
                cid=to_int(choice.get("id"))
                if cid is not None: qbank_choice_id_to_subject[cid].add(subject)

        q=row.get("question") or row.get("question_text") or row.get("text")
        k=norm(q)
        if k and len(k)>=20: exact[k].add(subject)

# A canonical subject ID is accepted only when a folder has a unique ID
# accounting for >=80% of its tagged rows and that ID belongs to one folder.
canonical_id_to_subject=defaultdict(list)
for subject, counts in subject_id_counts_by_subject.items():
    total=sum(counts.values())
    if not total: continue
    top=counts.most_common()
    sid,n=top[0]
    if (len(top)==1 or n>top[1][1]) and n/total >= 0.80:
        canonical_id_to_subject[sid].append(subject)
canonical_id_to_subject={sid:subs for sid,subs in canonical_id_to_subject.items() if len(subs)==1}
canonical_subject_by_id={sid:subs[0] for sid,subs in canonical_id_to_subject.items()}

summary=defaultdict(lambda:{"files":0,"questions":0,"subject_id_mapped":0,"canonical_subject_id_mapped":0,
                            "qbank_id_mapped":0,"qbank_unique_key_mapped":0,"qbank_map_id_mapped":0,"qbank_choice_id_mapped":0,
                            "exact_mapped":0,"subject_mapped":0,"unresolved":0,"ambiguous":0})
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
        source_id=row.get("id") if row.get("id") is not None else row.get("question_id")
        source_id_int=to_int(source_id)
        source_sids=[]
        for sid in row.get("subjects_id") or []:
            n=to_int(sid)
            if n is not None: source_sids.append(n)

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
            evidence="source.subjects_id -> qBank canonical subject ID"
            summary[year]["canonical_subject_id_mapped"]+=1
            summary[year]["subject_id_mapped"]+=1

        elif source_sids and len(raw_candidates)==1 and all(len(subject_id_to_subject.get(sid,set()))==1 for sid in source_sids):
            subjects=sorted(raw_candidates)
            status="MAPPED_SUBJECT_ID"
            evidence="source.subjects_id -> qBank subject"
            summary[year]["subject_id_mapped"]+=1

        else:
            qid_candidates=qbank_id_to_subject.get(source_id_int,set()) if source_id_int is not None else set()
            if len(qid_candidates)==1:
                subjects=sorted(qid_candidates)
                status="MAPPED_QBANK_ID"
                evidence="source.id -> qBank.id exact match"
                summary[year]["qbank_id_mapped"]+=1
            else:
                uk_candidates=qbank_unique_key_to_subject.get(str(row.get("unique_key")),set()) if row.get("unique_key") else set()
                if len(uk_candidates)==1:
                    subjects=sorted(uk_candidates)
                    status="MAPPED_QBANK_UNIQUE_KEY"
                    evidence="source.unique_key -> qBank.unique_key exact match"
                    summary[year]["qbank_unique_key_mapped"]+=1
                else:
                    mid=to_int(row.get("map_id"))
                    mid_candidates=qbank_map_id_to_subject.get(mid,set()) if mid is not None else set()
                    if len(mid_candidates)==1:
                        subjects=sorted(mid_candidates)
                        status="MAPPED_QBANK_MAP_ID"
                        evidence="source.map_id -> qBank.map_id exact match"
                        summary[year]["qbank_map_id_mapped"]+=1
                    else:
                        choice_subjects=set()
                        for choice in row.get("choices") or []:
                            if isinstance(choice,dict):
                                cid=to_int(choice.get("id"))
                                if cid is not None: choice_subjects.update(qbank_choice_id_to_subject.get(cid,set()))
                        correct_cid=to_int(row.get("correct_choice_id"))
                        correct_subjects=qbank_choice_id_to_subject.get(correct_cid,set()) if correct_cid is not None else set()
                        if len(choice_subjects)==1 and (not correct_subjects or correct_subjects==choice_subjects):
                            subjects=sorted(choice_subjects)
                            status="MAPPED_QBANK_CHOICE_ID"
                            evidence="source.choices[].id -> qBank.choices[].id exact subject linkage"
                            summary[year]["qbank_choice_id_mapped"]+=1
                        else:
                            subjects=sorted(exact.get(norm(q),set()))
                        if len(subjects)==1:
                            status="MAPPED_EXACT"
                            evidence="unique exact normalized question text -> qBank subject"
                            summary[year]["exact_mapped"]+=1
                        elif len(subjects)>1:
                            subjects=[]
                            status="AMBIGUOUS_EXACT"
                            evidence="multiple qBank subjects matched exact text"
                        else:
                            subjects=[]
                            status="UNRESOLVED"
                            evidence="no source-derived unique mapping"

        if status.startswith("MAPPED_"):
            summary[year]["subject_mapped"]+=1
        elif status=="AMBIGUOUS_EXACT":
            summary[year]["ambiguous"]+=1
        else:
            summary[year]["unresolved"]+=1

        records.append({
            "source_file":str(rel).replace(os.sep,"/"),
            "source_index":i,
            "source_id":source_id,
            "year":year,
            "source_subject_ids":source_sids,
            "subject_id_evidence":id_evidence,
            "subject_candidates":subjects,
            "classification_status":status,
            "mapping_evidence":evidence,
            "question_hash":hashlib.sha256(norm(q).encode()).hexdigest(),
            "source_record":row
        })

audit={
    "source_files":sum(v["files"] for v in summary.values()),
    "questions":sum(v["questions"] for v in summary.values()),
    "mapped_subject_id":sum(v["subject_id_mapped"] for v in summary.values()),
    "mapped_canonical_subject_id":sum(v["canonical_subject_id_mapped"] for v in summary.values()),
    "mapped_qbank_id":sum(v["qbank_id_mapped"] for v in summary.values()),
    "mapped_qbank_unique_key":sum(v["qbank_unique_key_mapped"] for v in summary.values()),
    "mapped_qbank_map_id":sum(v["qbank_map_id_mapped"] for v in summary.values()),
    "mapped_qbank_choice_id":sum(v["qbank_choice_id_mapped"] for v in summary.values()),
    "mapped_exact":sum(v["exact_mapped"] for v in summary.values()),
    "mapped_total":sum(v["subject_mapped"] for v in summary.values()),
    "ambiguous_exact":sum(v["ambiguous"] for v in summary.values()),
    "unresolved":sum(v["unresolved"] for v in summary.values()),
    "subject_id_index_entries":len(subject_id_to_subject),
    "qbank_id_index_entries":len(qbank_id_to_subject),
    "qbank_unique_key_index_entries":len(qbank_unique_key_to_subject),
    "qbank_map_id_index_entries":len(qbank_map_id_to_subject),
    "qbank_choice_id_index_entries":len(qbank_choice_id_to_subject),
    "canonical_subject_count":len(canonical_subject_by_id),
    "canonical_subject_by_id":{str(k):v for k,v in sorted(canonical_subject_by_id.items())},
    "policy":"Use explicit source subjects_id first. If absent/unusable, use exact source id/unique_key/map_id/choice-id linkage to qBank records only when the linkage resolves to exactly one qBank subject folder. Then use unique exact normalized question text. Never infer subject from question content."
}

(Path(OUT/"pyq_records.json")).write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding="utf-8")
(Path(OUT/"pyq_year_summary.json")).write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding="utf-8")
(Path(OUT/"pyq_audit.json")).write_text(json.dumps(audit,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps(audit,indent=2))
