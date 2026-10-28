import argparse
from pathlib import Path
import pandas as pd
def main():
 p=argparse.ArgumentParser(); p.add_argument("--input",required=True); p.add_argument("--label-column",default="label"); p.add_argument("--output",default="results/final_label_counts.csv"); p.add_argument("--expected-total",type=int); a=p.parse_args()
 d=pd.read_csv(a.input)
 if a.label_column not in d: raise ValueError(f"Missing {a.label_column!r}; columns={list(d.columns)}")
 c=d[a.label_column].dropna().astype(str).value_counts().rename_axis("label").reset_index(name="count")
 total=int(c["count"].sum()); print("Rows:",len(d),"missing labels:",int(d[a.label_column].isna().sum()),"sum of label rows:",total); print(c.to_string(index=False))
 if a.expected_total is not None and total!=a.expected_total: print(f"WARNING: difference from expected total = {total-a.expected_total:+,}")
 o=Path(a.output); o.parent.mkdir(parents=True,exist_ok=True); c.to_csv(o,index=False); print("Saved",o)
if __name__=="__main__": main()
