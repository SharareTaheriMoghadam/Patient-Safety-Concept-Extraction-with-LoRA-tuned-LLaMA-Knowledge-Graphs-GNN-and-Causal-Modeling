import argparse, json
from pathlib import Path
from collections import Counter

def load_jsonl(path):
    out = {}
    with open(path, encoding="utf-8") as f:
        for n, line in enumerate(f, 1):
            if not line.strip(): continue
            r = json.loads(line); doc = str(r["doc_id"])
            if doc in out: raise ValueError(f"{path}:{n}: duplicate doc_id {doc}")
            ents = []
            for e in r.get("entities", []):
                s, t, lab = int(e["start"]), int(e["end"]), str(e["label"])
                if s < 0 or t <= s: raise ValueError(f"{path}:{n}: invalid span")
                ents.append({"start":s,"end":t,"label":lab,"text":e.get("text","")})
            out[doc] = {"patient_id":str(r.get("patient_id",doc)), "entities":ents}
    return out

def key(e): return (int(e["start"]), int(e["end"]), str(e["label"]))

def score(gold, pred):
    if set(gold) != set(pred):
        raise ValueError(f"Gold/pred doc IDs differ: missing={len(set(gold)-set(pred))}, extra={len(set(pred)-set(gold))}")
    cats = sorted({e["label"] for r in gold.values() for e in r["entities"]} |
                  {e["label"] for r in pred.values() for e in r["entities"]})
    c = {x:Counter(tp=0,fp=0,fn=0,support=0) for x in cats}
    allc = Counter(tp=0,fp=0,fn=0)
    patients = {}
    for doc in gold:
        pid = gold[doc]["patient_id"]
        gc, pc = Counter(map(key,gold[doc]["entities"])), Counter(map(key,pred[doc]["entities"]))
        local = Counter(tp=0,fp=0,fn=0)
        for s,e,lab in set(gc)|set(pc):
            tp=min(gc[(s,e,lab)],pc[(s,e,lab)])
            fp=max(pc[(s,e,lab)]-gc[(s,e,lab)],0)
            fn=max(gc[(s,e,lab)]-pc[(s,e,lab)],0)
            c[lab]["tp"]+=tp; c[lab]["fp"]+=fp; c[lab]["fn"]+=fn; c[lab]["support"]+=gc[(s,e,lab)]
            allc["tp"]+=tp; allc["fp"]+=fp; allc["fn"]+=fn
            local["tp"]+=tp; local["fp"]+=fp; local["fn"]+=fn
        patients.setdefault(pid,Counter(tp=0,fp=0,fn=0)).update(local)
    def m(x):
        tp,fp,fn=x["tp"],x["fp"],x["fn"]
        p=tp/(tp+fp) if tp+fp else 0.; r=tp/(tp+fn) if tp+fn else 0.
        return {"tp":int(tp),"fp":int(fp),"fn":int(fn),"precision":p,"recall":r,"f1":2*p*r/(p+r) if p+r else 0.}
    per={}
    for lab,x in c.items(): per[lab]={**m(x),"support":int(x["support"])}
    return {"matching":"strict_exact_span_and_label","n_documents":len(gold),
      "n_patients":len({x["patient_id"] for x in gold.values()}),
      "n_gold_entities":sum(x["support"] for x in per.values()),
      "n_predicted_entities":sum(len(x["entities"]) for x in pred.values()),
      "micro":m(allc),"macro_f1":sum(x["f1"] for x in per.values())/len(per) if per else 0.,
      "per_category":per,"_patient_counts":{k:dict(v) for k,v in patients.items()}}

def main():
    p=argparse.ArgumentParser(); p.add_argument("--gold",required=True); p.add_argument("--pred",required=True); p.add_argument("--output",default="results/metrics.json"); a=p.parse_args()
    r=score(load_jsonl(a.gold),load_jsonl(a.pred)); r.pop("_patient_counts",None)
    out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(r,indent=2),encoding="utf-8")
    print(json.dumps(r,indent=2)); print("Saved",out)
if __name__=="__main__": main()
