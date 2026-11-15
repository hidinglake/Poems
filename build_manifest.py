"""Keep poems/files.json in step with the .txt files in poems/.

Files already listed keep their order and titles; new .txt files are added
at the end; files that no longer exist are dropped.
"""
import json
from pathlib import Path

poems = Path(__file__).resolve().parent.parent / "poems"
manifest = poems / "files.json"

try:
    entries = json.loads(manifest.read_text(encoding="utf-8"))
except (FileNotFoundError, json.JSONDecodeError):
    entries = []
entries = [{"file": e} if isinstance(e, str) else e for e in entries]

present = sorted(p.name for p in poems.glob("*.txt"))
kept = [e for e in entries if e.get("file") in present]
listed = {e["file"] for e in kept}
kept += [{"file": name} for name in present if name not in listed]

manifest.write_text(json.dumps(kept, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"{len(kept)} file(s) in poems/files.json")
