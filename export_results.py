import argparse,csv,json
from pathlib import Path
def main():
 p=argparse.ArgumentParser(); p.add_argument("--inputs",nargs="+",required=True); p.add_argument("--output",default="results/model_comparison.csv"); a=p.parse_args(); rows=[]
 for name in a.inputs:
  d=json.loads(Path(name).read_text(encoding="utf-8")); m=d.get("micro",{})
  rows.append({"run":d.get("experiment_name",Path(name).stem),"n_documents":d.get("n_documents"),"n_patients":d.get("n_patients"),"n_gold_entities":d.get("n_gold_entities"),"micro_precision":m.get("precision"),"micro_recall":m.get("recall"),"micro_f1":m.get("f1"),"macro_f1":d.get("macro_f1"),"matching":d.get("matching")})
 o=Path(a.output); o.parent.mkdir(parents=True,exist_ok=True)
 with o.open("w",newline="",encoding="utf-8") as f: w=csv.DictWriter(f,fieldnames=list(rows[0]) if rows else ["run"]); w.writeheader(); w.writerows(rows)
 print("Saved",o)
if __name__=="__main__": main()
