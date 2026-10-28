import argparse, json
from pathlib import Path
import numpy as np
from metrics import load_jsonl, key

def counts_by_patient(gold,pred):
 if set(gold)!=set(pred): raise ValueError("Gold and predictions must contain identical document IDs")
 out={}
 for doc in gold:
  pid=gold[doc]["patient_id"]; g={}; p={}
  for x in gold[doc]["entities"]: g[key(x)]=g.get(key(x),0)+1
  for x in pred[doc]["entities"]: p[key(x)]=p.get(key(x),0)+1
  c=out.setdefault(pid,[0,0,0])
  for k in set(g)|set(p):
   c[0]+=min(g.get(k,0),p.get(k,0)); c[1]+=max(p.get(k,0)-g.get(k,0),0); c[2]+=max(g.get(k,0)-p.get(k,0),0)
 return out
def f1(c, sample):
 tp=sum(c[x][0] for x in sample); fp=sum(c[x][1] for x in sample); fn=sum(c[x][2] for x in sample); den=2*tp+fp+fn
 return 2*tp/den if den else 0.
def main():
 a=argparse.ArgumentParser(); a.add_argument("--gold",required=True); a.add_argument("--pred-a",required=True); a.add_argument("--pred-b",required=True); a.add_argument("--n-bootstrap",type=int,default=2000); a.add_argument("--seed",type=int,default=42); a.add_argument("--output",default="results/paired_bootstrap.json"); x=a.parse_args()
 g=load_jsonl(x.gold); ca=counts_by_patient(g,load_jsonl(x.pred_a)); cb=counts_by_patient(g,load_jsonl(x.pred_b))
 if set(ca)!=set(cb): raise ValueError("Patient groups differ")
 ps=np.array(sorted(ca)); rng=np.random.default_rng(x.seed); dif=[]
 for _ in range(x.n_bootstrap):
  s=rng.choice(ps,len(ps),replace=True).tolist(); dif.append(f1(ca,s)-f1(cb,s))
 r={"comparison":"model_a_minus_model_b","metric":"strict_exact_entity_micro_f1","point_difference":f1(ca,ps.tolist())-f1(cb,ps.tolist()),"ci_95_percentile":[float(np.quantile(dif,.025)),float(np.quantile(dif,.975))],"bootstrap_replicates":x.n_bootstrap,"seed":x.seed,"resampling_unit":"patient"}
 o=Path(x.output); o.parent.mkdir(parents=True,exist_ok=True); o.write_text(json.dumps(r,indent=2),encoding="utf-8"); print(json.dumps(r,indent=2))
if __name__=="__main__": main()
