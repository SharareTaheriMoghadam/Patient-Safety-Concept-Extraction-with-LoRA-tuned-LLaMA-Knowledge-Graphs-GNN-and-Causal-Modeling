import argparse,csv
from pathlib import Path
from metrics import load_jsonl,key
def main():
 p=argparse.ArgumentParser(); p.add_argument("--gold",required=True); p.add_argument("--pred",required=True); p.add_argument("--output",default="results/error_audit.csv"); a=p.parse_args()
 g,q=load_jsonl(a.gold),load_jsonl(a.pred)
 if set(g)!=set(q): raise ValueError("Gold/pred doc IDs differ")
 rows=[]
 for doc in g:
  x={key(e):e for e in g[doc]["entities"]}; y={key(e):e for e in q[doc]["entities"]}
  for k in set(y)-set(x):
   e=y[k]; rows.append({"doc_id":doc,"patient_id":g[doc]["patient_id"],"error_type":"false_positive","start":e["start"],"end":e["end"],"label":e["label"],"text":e.get("text","")})
  for k in set(x)-set(y):
   e=x[k]; rows.append({"doc_id":doc,"patient_id":g[doc]["patient_id"],"error_type":"false_negative","start":e["start"],"end":e["end"],"label":e["label"],"text":e.get("text","")})
 o=Path(a.output); o.parent.mkdir(parents=True,exist_ok=True); fields=["doc_id","patient_id","error_type","start","end","label","text"]
 with o.open("w",newline="",encoding="utf-8") as f: w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
 print(f"Exported {len(rows)} error records to {o}. Clinical severity requires human review.")
if __name__=="__main__": main()
