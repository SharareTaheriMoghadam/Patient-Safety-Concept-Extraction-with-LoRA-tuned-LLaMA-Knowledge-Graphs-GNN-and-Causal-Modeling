import argparse,re
from pathlib import Path
PATTERNS=[r"\bTODO\b",r"\bTBD\b",r"REPLACE WITH",r"Note exact counts",r"planned figure",r"project questionnaire",r"approximately\s+\d",r"0\.89",r"8,742"]
def main():
 p=argparse.ArgumentParser(); p.add_argument("--manuscript",required=True,help="TXT/MD export of manuscript"); a=p.parse_args()
 lines=Path(a.manuscript).read_text(encoding="utf-8",errors="replace").splitlines(); hits=[]
 for n,line in enumerate(lines,1):
  for pat in PATTERNS:
   if re.search(pat,line,re.I): hits.append((n,pat,line.strip()))
 if not hits: print("No configured warning patterns found; this does not validate results.")
 for n,pat,line in hits: print(f"line {n} | {pat} | {line}")
if __name__=="__main__": main()
