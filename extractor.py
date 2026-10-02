from .patterns import PATTERNS
from src.models import IOC
from src.enrichment.normalizer import normalize
from src.enrichment.risk import calculate_risk
from src.enrichment.mitre import map_mitre
from src.enrichment.timeline import find_date

def context(text,a,b,n=180):
    return " ".join(text[max(0,a-n):min(len(text),b+n)].split())

def extract(text, source):
    results=[]
    seen=set()

    for kind, pattern in PATTERNS.items():
        for m in pattern.finditer(text):
            value=m.group(0).rstrip(".,;:)]}")
            norm=normalize(value,kind)
            key=(kind,norm)
            if key in seen:
                continue
            seen.add(key)

            ctx=context(text,m.start(),m.end())
            risk,severity,confidence=calculate_risk(kind,value,ctx)
            technique,tactic=map_mitre(ctx)

            results.append(IOC(
                value=value,
                ioc_type=kind,
                normalized=norm,
                source=source,
                context=ctx,
                risk=risk,
                severity=severity,
                confidence=confidence,
                technique=technique,
                tactic=tactic,
                first_seen=find_date(ctx),
                metadata={"start":m.start(),"end":m.end()}
            ))
    return results
