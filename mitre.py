from src.config import MITRE

def map_mitre(text):
    low=text.lower()
    hits=[]
    for tid,data in MITRE.items():
        if any(k.lower() in low for k in data.get("keywords",[])):
            hits.append((tid,data))
    if not hits:
        return "Unmapped",""
    labels=[f"{tid} {d['name']}" for tid,d in hits[:3]]
    tactics=sorted(set(d["tactic"] for _,d in hits))
    return "; ".join(labels), ", ".join(tactics)
