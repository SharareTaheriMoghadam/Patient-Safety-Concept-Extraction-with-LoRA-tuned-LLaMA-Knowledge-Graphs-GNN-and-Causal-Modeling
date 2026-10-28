"""Create artificial weak-label corruption variants; does not train/evaluate models."""
import argparse,json
from pathlib import Path
import numpy as np
import pandas as pd
def main():
 p=argparse.ArgumentParser(); p.add_argument("--input",required=True); p.add_argument("--label-column",default="label"); p.add_argument("--rates",nargs="+",type=float,default=[.05,.10,.20]); p.add_argument("--seed",type=int,default=42); p.add_argument("--output-dir",default="data/noise_sensitivity"); a=p.parse_args()
 d=pd.read_csv(a.input)
 if a.label_column not in d: raise ValueError(f"Missing {a.label_column}")
 labels=sorted(d[a.label_column].dropna().astype(str).unique())
 if len(labels)<2: raise ValueError("Need at least two labels")
 out=Path(a.output_dir); out.mkdir(parents=True,exist_ok=True); manifest=[]
 for i,rate in enumerate(a.rates):
  if not 0<=rate<=1: raise ValueError("Noise rates must be between 0 and 1")
  x=d.copy(); rng=np.random.default_rng(a.seed+i); eligible=np.flatnonzero(x[a.label_column].notna().to_numpy()); n=round(rate*len(eligible)); chosen=rng.choice(eligible,n,replace=False) if n else []
  for idx in chosen:
   old=str(x.at[idx,a.label_column]); alternatives=[z for z in labels if z!=old]; x.at[idx,a.label_column]=rng.choice(alternatives)
  f=out/f"labels_noise_{rate:.2f}.csv"; x.to_csv(f,index=False); manifest.append({"requested_noise_rate":rate,"rows_corrupted":int(n),"eligible_rows":int(len(eligible)),"seed":a.seed+i,"file":str(f)})
 (out/"manifest.json").write_text(json.dumps(manifest,indent=2),encoding="utf-8"); print(json.dumps(manifest,indent=2)); print("Synthetic corruption is not an estimate of real annotation noise.")
if __name__=="__main__": main()
