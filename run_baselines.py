"""Launch commands configured in a JSON manifest. Commands must be real project commands."""
import argparse,json,subprocess,sys
from pathlib import Path
def main():
 p=argparse.ArgumentParser(); p.add_argument("--manifest",required=True); p.add_argument("--dry-run",action="store_true"); p.add_argument("--continue-on-error",action="store_true"); a=p.parse_args()
 items=json.loads(Path(a.manifest).read_text(encoding="utf-8"))
 if not isinstance(items,list): raise ValueError("Manifest must be a JSON list")
 failed=[]
 for item in items:
  name=item.get("name","unnamed"); cmd=item.get("command")
  if not isinstance(cmd,list) or not cmd or not all(isinstance(z,str) for z in cmd): raise ValueError(f"{name}: command must be a list of strings")
  if any("REPLACE_WITH" in z or z in {"ARGS","EXISTING_INFERENCE_SCRIPT"} for z in cmd): raise ValueError(f"{name}: replace command placeholders first")
  print("\n",name,":"," ".join(cmd))
  if a.dry_run: continue
  r=subprocess.run(cmd,check=False)
  if r.returncode: failed.append({"name":name,"returncode":r.returncode}); print("FAILED",name,file=sys.stderr)
  if r.returncode and not a.continue_on_error: break
 if failed: print(json.dumps(failed,indent=2),file=sys.stderr); raise SystemExit(1)
if __name__=="__main__": main()
