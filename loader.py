from pathlib import Path
import json

SUPPORTED = {".txt",".log",".md",".json",".csv"}

def read_document(path: Path):
    if path.suffix.lower() == ".json":
        obj = json.loads(path.read_text(encoding="utf-8", errors="ignore"))
        return json.dumps(obj, indent=2)
    return path.read_text(encoding="utf-8", errors="ignore")

def load_source(source):
    p = Path(source)
    if not p.exists():
        raise FileNotFoundError(source)
    if p.is_file():
        return [(p.name, read_document(p))]
    docs=[]
    for f in sorted(p.rglob("*")):
        if f.is_file() and f.suffix.lower() in SUPPORTED:
            docs.append((str(f.relative_to(p)), read_document(f)))
    return docs
