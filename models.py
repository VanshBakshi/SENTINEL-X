from dataclasses import dataclass, asdict
from typing import Dict, Any

@dataclass
class IOC:
    value: str
    ioc_type: str
    normalized: str
    source: str
    context: str
    risk: int
    severity: str
    confidence: float
    technique: str = ""
    tactic: str = ""
    first_seen: str = ""
    metadata: Dict[str, Any] = None

    def to_dict(self):
        return asdict(self)

@dataclass
class Finding:
    title: str
    category: str
    severity: str
    description: str
    evidence: str
    score: int
