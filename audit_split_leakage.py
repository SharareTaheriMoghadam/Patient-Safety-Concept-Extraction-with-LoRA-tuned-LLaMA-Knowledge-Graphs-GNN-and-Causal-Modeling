import argparse, hashlib, json
from pathlib import Path
import pandas as pd
def norm(x): return "" if pd.isna(x) else " ".join(str(x).casefold().split())
def main():
 p=argparse.ArgumentParser(); p.add_argument("--input",required=True); p.add_argument("--split-column",default="split"); p.add_argument("--patient-column",default="patient_id"); p.add_argument("--text-column",default="text"); p.add_argument("--output",default="results/leakage_audit.json"); a=p.parse_args()
 d=pd.read_csv(a.input)
 for col in [a.split_column,a.patient_column,a.text_column]:
  if col not in d: raise ValueError(f"Missing {col!r}; columns={list(d.columns)}")
 d["_split"]=d[a.split_column].astype("string"); d["_patient"]=d[a.patient_column].astype("string")
 d["_hash"]=d[a.text_column].map(lambda x:hashlib.sha256(norm(x).encode()).hexdigest())
 sets={str(s):set(g["_patient"].dropna().astype(str)) for s,g in d.groupby("_split",dropna=False)}
 names=list(sets); overlaps=[]
 for i,x in enumerate(names):
  for y in names[i+1:]:
   v=sorted(sets[x]&sets[y]); overlaps.append({"split_a":x,"split_b":y,"overlap_count":len(v),"example_ids":v[:20]})
 dd=d[d[a.text_column].map(norm)!=""].copy(); dup=dd[dd["_hash"].duplicated(keep=False)]
 groups=[]
 for h,g in dup.groupby("_hash"):
  sp=sorted(g["_split"].dropna().astype(str).unique().tolist()); groups.append({"hash":h,"rows":len(g),"splits":sp,"cross_split":len(sp)>1})
 report={"input_rows":len(d),"split_sizes":{str(k):int(v) for k,v in d["_split"].value_counts(dropna=False).items()},"patient_overlap":overlaps,"exact_duplicate_groups":groups,"warnings":["No identifier overlap does not prove cross-version patient independence.","Verify patient-linkage identifiers for the exact MIMIC versions.","Exact hashes do not detect all near-duplicates."]}
 o=Path(a.output); o.parent.mkdir(parents=True,exist_ok=True); o.write_text(json.dumps(report,indent=2),encoding="utf-8"); print(json.dumps(report,indent=2))
if __name__=="__main__": main()
