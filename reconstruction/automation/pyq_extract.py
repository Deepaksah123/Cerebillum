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
        sids=[n for sid in (row.get("subjects_id") or []) if (n:=to_int(sid)) is not None]
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
        k=norm(row.get("question") or row.get("question_text") or row.get("text"))
        if k and len(k)>=20: exact[k].add(subject)

canonical_id_to_subject=defaultdict(list)
for subject, counts in subject_id_counts_by_subject.items():
    total=sum(counts.values())
    if not total: continue
    top=counts.most_common()
    sid,n=top[0]
    if (len(top)==1 or n>top[1][1]) and n/total>=0.80:
        canonical_id_to_subject[sid].append(subject)
canonical_id_to_subject={sid:subs for sid,subs in canonical_id_to_subject.items() if len(subs)==1}
canonical_subject_by_id={sid:subs[0] for sid,subs in canonical_id_to_subject.items()}

# Guarded cross-source metadata: only non-PYQ/non-qBank records with explicit
# canonical subjects_id are eligible. Exact unique_key or exact normalized text
# is required. Mere repetition in another test/module is never sufficient.
cross_unique_key=defaultdict(set)
cross_text=defaultdict(set)
cross_evidence=defaultdict(list)
for p in SRC.rglob("*.json"):
    if PYQ in p.parents or QB in p.parents: continue
    data=load_json(p)
    if data is None: continue
    rows=data if isinstance(data,list) else data.get("questions",data.get("data",[]))
    if not isinstance(rows,list): continue
    rel=str(p.relative_to(SRC)).replace(os.sep,"/")
    for row in rows:
        if not isinstance(row,dict): continue
        sids=[n for sid in (row.get("subjects_id") or []) if (n:=to_int(sid)) is not None]
        if not sids or not all(sid in canonical_subject_by_id for sid in sids): continue
        candidates={canonical_subject_by_id[sid] for sid in sids}
        if len(candidates)!=1: continue
        subject=next(iter(candidates))
        uk=row.get("unique_key")
        if uk:
            key=str(uk)
            cross_unique_key[key].add(subject)
            cross_evidence[("uk",key)].append({"subject":subject,"file":rel})
        nk=norm(row.get("question") or row.get("question_text") or row.get("text"))
        if nk and len(nk)>=20:
            cross_text[nk].add(subject)
            cross_evidence[("text",nk)].append({"subject":subject,"file":rel})

PYQ_FOLDER_ALIASES={
    "biochemistry":"Biochemistry","physiology":"Physiology","anatomy":"Anatomy",
    "pharmacology":"Pharmacology","pathology":"Pathology","microbiology":"Microbiology",
    "psm":"Preventive & Social Medicine","preventive & social medicine":"Preventive & Social Medicine",
    "ophthalmology":"Ophthalmology","ent":"ENT","forensic medicine":"Forensic Medicine",
    "medicine":"Medicine","surgery":"Surgery","pediatrics":"Pediatrics","paediatrics":"Pediatrics",
    "ob g":"Obstetrics & Gynecology","obg":"Obstetrics & Gynecology","obstetrics & gynecology":"Obstetrics & Gynecology",
    "orthopedics":"Orthopedics","orthopaedics":"Orthopedics","psychiatry":"Psychiatry",
    "radiology":"Radiology","dermatology":"Dermatology","anesthesia":"Anesthesia","anaesthesia":"Anesthesia"
}
def folder_subject(path):
    parts=[x.strip().lower() for x in Path(path).parts]
    try:
        i=parts.index("pyq")
        if i+1 < len(parts): return PYQ_FOLDER_ALIASES.get(parts[i+1])
    except ValueError: pass
    return None

folder_unique_key=defaultdict(set)
folder_text=defaultdict(set)
for p in SRC.rglob("*.json"):
    rel=str(p.relative_to(SRC)).replace(os.sep,"/")
    subject=folder_subject(rel)
    if not subject or "/PYQ/" not in ("/"+rel+"/").upper(): continue
    data=load_json(p)
    if data is None: continue
    rows=data if isinstance(data,list) else data.get("questions",data.get("data",[]))
    if not isinstance(rows,list): continue
    for row in rows:
        if not isinstance(row,dict): continue
        uk=row.get("unique_key")
        if uk: folder_unique_key[str(uk)].add(subject)
        nk=norm(row.get("question") or row.get("question_text") or row.get("text"))
        if nk and len(nk)>=20: folder_text[nk].add(subject)

VIDEO_SUBJECT_ALIASES={
    "biochemistry":"Biochemistry","physiology":"Physiology","anatomy":"Anatomy",
    "pharmacology":"Pharmacology","pathology":"Pathology","microbiology":"Microbiology",
    "preventive":"Preventive & Social Medicine","psm":"Preventive & Social Medicine",
    "ophthalmology":"Ophthalmology","ophthal":"Ophthalmology","ent":"ENT",
    "forensic":"Forensic Medicine","medicine":"Medicine","surgery":"Surgery",
    "pediatrics":"Pediatrics","paediatrics":"Pediatrics","obg":"Obstetrics & Gynecology",
    "obs":"Obstetrics & Gynecology","gynecology":"Obstetrics & Gynecology",
    "orthopedics":"Orthopedics","orthopaedics":"Orthopedics","psychiatry":"Psychiatry",
    "radiology":"Radiology","dermatology":"Dermatology","anesthesia":"Anesthesia",
    "anaesthesia":"Anesthesia"
}
def video_subject_candidates(row):
    urls=[]
    for key in ("solution_video","explanation_video","question_video"):
        v=row.get(key)
        if isinstance(v,str) and v: urls.append(v.lower())
    found=set()
    for u in urls:
        name=re.sub(r"[^a-z0-9]+"," ",u)
        for alias,subject in VIDEO_SUBJECT_ALIASES.items():
            if re.search(rf"\b{re.escape(alias)}\b",name): found.add(subject)
    return found

summary=defaultdict(lambda:{"files":0,"questions":0,"subject_id_mapped":0,"canonical_subject_id_mapped":0,
                            "qbank_id_mapped":0,"qbank_unique_key_mapped":0,"qbank_map_id_mapped":0,"qbank_choice_id_mapped":0,
                            "video_subject_mapped":0,"cross_source_unique_key_mapped":0,"cross_source_text_mapped":0,
                            "folder_pyq_unique_key_mapped":0,"folder_pyq_text_mapped":0,"exact_mapped":0,"subject_mapped":0,"unresolved":0,"ambiguous":0})
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
        source_sids=[n for sid in (row.get("subjects_id") or []) if (n:=to_int(sid)) is not None]
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
            video_candidates=video_subject_candidates(row)
            if len(video_candidates)==1:
                subjects=sorted(video_candidates)
                status="MAPPED_VIDEO_SUBJECT_METADATA"
                evidence="explicit subject token in source solution/explanation/question video filename"
                summary[year]["video_subject_mapped"]+=1
            else:
                qid_candidates=qbank_id_to_subject.get(source_id_int,set()) if source_id_int is not None else set()
                if len(qid_candidates)==1:
                    subjects=sorted(qid_candidates)
                    status="MAPPED_QBANK_ID"
                    evidence="source.id -> qBank.id exact match"
                    summary[year]["qbank_id_mapped"]+=1
                else:
                    uk=str(row.get("unique_key")) if row.get("unique_key") else None
                    uk_candidates=qbank_unique_key_to_subject.get(uk,set()) if uk else set()
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
                                nk=norm(q)
                                cands=cross_unique_key.get(str(row.get("unique_key")),set()) if row.get("unique_key") else set()
                                text_cands=cross_text.get(nk,set())
                                if len(cands)==1:
                                    subjects=sorted(cands)
                                    status="MAPPED_CROSS_SOURCE_UNIQUE_KEY_METADATA"
                                    evidence="exact unique_key -> non-PYQ/non-qBank source with explicit canonical subjects_id"
                                    summary[year]["cross_source_unique_key_mapped"]+=1
                                elif len(cands)>1:
                                    subjects=[]
                                    status="AMBIGUOUS_CROSS_SOURCE_UNIQUE_KEY"
                                    evidence="exact unique_key matched multiple explicit canonical subjects"
                                elif len(text_cands)==1:
                                    subjects=sorted(text_cands)
                                    status="MAPPED_CROSS_SOURCE_TEXT_METADATA"
                                    evidence="exact normalized question text -> non-PYQ/non-qBank source with explicit canonical subjects_id"
                                    summary[year]["cross_source_text_mapped"]+=1
                                elif len(text_cands)>1:
                                    subjects=[]
                                    status="AMBIGUOUS_CROSS_SOURCE_TEXT"
                                    evidence="exact normalized question text matched multiple explicit canonical subjects"
                                else:
                                    folder_uk_cands=folder_unique_key.get(str(row.get("unique_key")),set()) if row.get("unique_key") else set()
                                    folder_text_cands=folder_text.get(nk,set())
                                    if len(folder_uk_cands)==1:
                                        subjects=sorted(folder_uk_cands)
                                        status="MAPPED_SUBJECT_FOLDER_PYQ_UNIQUE_KEY"
                                        evidence="exact unique_key -> subject-labeled DocTutorial/PYQ folder"
                                        summary[year]["folder_pyq_unique_key_mapped"]+=1
                                    elif len(folder_uk_cands)>1:
                                        subjects=[]
                                        status="AMBIGUOUS_SUBJECT_FOLDER_PYQ_UNIQUE_KEY"
                                        evidence="exact unique_key matched multiple subject-labeled DocTutorial/PYQ folders"
                                    elif len(folder_text_cands)==1:
                                        subjects=sorted(folder_text_cands)
                                        status="MAPPED_SUBJECT_FOLDER_PYQ_TEXT"
                                        evidence="exact normalized question text -> unique subject-labeled DocTutorial/PYQ folder"
                                        summary[year]["folder_pyq_text_mapped"]+=1
                                    elif len(folder_text_cands)>1:
                                        subjects=[]
                                        status="AMBIGUOUS_SUBJECT_FOLDER_PYQ_TEXT"
                                        evidence="exact normalized question text matched multiple subject-labeled DocTutorial/PYQ folders"
                                    else:
                                        subjects=sorted(exact.get(nk,set()))
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
        elif status.startswith("AMBIGUOUS_") or status=="AMBIGUOUS_EXACT":
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
    "mapped_video_subject_metadata":sum(v["video_subject_mapped"] for v in summary.values()),
    "mapped_cross_source_unique_key_metadata":sum(v["cross_source_unique_key_mapped"] for v in summary.values()),
    "mapped_cross_source_text_metadata":sum(v["cross_source_text_mapped"] for v in summary.values()),
    "mapped_subject_folder_pyq_unique_key":sum(v["folder_pyq_unique_key_mapped"] for v in summary.values()),
    "mapped_subject_folder_pyq_text":sum(v["folder_pyq_text_mapped"] for v in summary.values()),
    "mapped_exact":sum(v["exact_mapped"] for v in summary.values()),
    "mapped_total":sum(v["subject_mapped"] for v in summary.values()),
    "ambiguous_exact":sum(v["ambiguous"] for v in summary.values()),
    "unresolved":sum(v["unresolved"] for v in summary.values()),
    "cross_source_unique_key_index_entries":len(cross_unique_key),
    "cross_source_text_index_entries":len(cross_text),
    "subject_folder_pyq_unique_key_index_entries":len(folder_unique_key),
    "subject_folder_pyq_text_index_entries":len(folder_text),
    "canonical_subject_count":len(canonical_subject_by_id),
    "canonical_subject_by_id":{str(k):v for k,v in sorted(canonical_subject_by_id.items())},
    "policy":"Explicit source subjects_id first; exact qBank id/unique_key/map_id/choice-id next; then exact unique_key or exact normalized question text against non-PYQ/non-qBank records carrying explicit canonical subjects_id; then exact unique_key/text against a subject-labeled DocTutorial/PYQ folder; then unique exact qBank text. Never infer subject from content or mere duplication across tests/modules."
}
(Path(OUT/"pyq_records.json")).write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding="utf-8")
(Path(OUT/"pyq_year_summary.json")).write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding="utf-8")
(Path(OUT/"pyq_audit.json")).write_text(json.dumps(audit,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps(audit,indent=2))
