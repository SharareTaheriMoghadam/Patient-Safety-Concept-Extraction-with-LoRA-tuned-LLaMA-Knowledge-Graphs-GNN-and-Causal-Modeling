import argparse,json
from pathlib import Path
import pandas as pd
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
def main():
 p=argparse.ArgumentParser(); p.add_argument("--input",required=True); p.add_argument("--weak-column",default="weak_label"); p.add_argument("--reviewed-column",default="reviewed_label"); p.add_argument("--output",default="results/weak_label_audit.json"); a=p.parse_args()
 d=pd.read_csv(a.input)
 for c in [a.weak_column,a.reviewed_column]:
  if c not in d: raise ValueError(f"Missing column {c}")
 d=d[[a.weak_column,a.reviewed_column]].dropna()
 if d.empty: raise ValueError("No paired weak/reviewed labels")
 y=d[a.reviewed_column].astype(str); pred=d[a.weak_column].astype(str); labels=sorted(set(y)|set(pred))
 result={"n_reviewed_pairs":len(d),"accuracy":accuracy_score(y,pred),"labels":labels,"classification_report":classification_report(y,pred,labels=labels,output_dict=True,zero_division=0),"confusion_matrix":confusion_matrix(y,pred,labels=labels).tolist(),"warning":"Valid only if reviewed labels were independently assigned."}
 o=Path(a.output); o.parent.mkdir(parents=True,exist_ok=True); o.write_text(json.dumps(result,indent=2),encoding="utf-8"); print(json.dumps(result,indent=2))
if __name__=="__main__": main()
