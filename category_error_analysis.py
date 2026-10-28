import argparse,csv
from pathlib import Path
from metrics import load_jsonl,key
def main():
 p=argparse.ArgumentParser(); p.add_argument("--gold",required=True); p.add_argument("--pred",required=True); p.add_argument("--output",default="results/category_metrics.csv"); a=p.parse_args()
 g,q=load_jsonl(a.gold),load_jsonl(a.pred)
 if set(g)!=set(q): raise ValueError("Gold/pred doc IDs differ")
 labels=sorted({e["label"] for r in g.values() for e in r["entities"]}|{e["label"] for r in q.values() for e in r["entities"]})
 c={l:{"tp":0,"fp":0,"fn":0,"support":0} for l in labels}
 for doc in g:
  x={}; y={}
  for e in g[doc]["entities"]: x[key(e)]=x.get(key(e),0)+1
  for e in q[doc]["entities"]: y[key(e)]=y.get(key(e),0)+1
  for s,t,l in set(x)|set(y):
   z=c[l]; z["tp"]+=min(x.get((s,t,l),0),y.get((s,t,l),0)); z["fp"]+=max(y.get((s,t,l),0)-x.get((s,t,l),0),0); z["fn"]+=max(x.get((s,t,l),0)-y.get((s,t,l),0),0); z["support"]+=x.get((s,t,l),0)
 rows=[]
 for l,z in c.items():
  pr=z["tp"]/(z["tp"]+z["fp"]) if z["tp"]+z["fp"] else 0; re=z["tp"]/(z["tp"]+z["fn"]) if z["tp"]+z["fn"] else 0
  rows.append({"label":l,**z,"precision":pr,"recall":re,"f1":2*pr*re/(pr+re) if pr+re else 0})
 o=Path(a.output); o.parent.mkdir(parents=True,exist_ok=True)
 with o.open("w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=["label","support","tp","fp","fn","precision","recall","f1"]); w.writeheader(); w.writerows(rows)
 print("Saved",o)
if __name__=="__main__": main()
