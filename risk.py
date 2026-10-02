BASE = {
    "sha256":58,"sha1":52,"md5":48,"ipv4":38,"url":45,
    "domain":40,"email":26,"cve":52,"registry":45,"windows_path":30
}

BOOSTS = {
    "malware":18,"ransomware":22,"phishing":18,"payload":14,
    "command and control":20,"c2":18,"backdoor":20,"credential":14,
    "exploit":20,"powershell":14,"persistence":16,"malicious":15,
    "callback":12,"download":10,"trojan":20,"encrypted":16
}

def calculate_risk(kind,value,context):
    text=context.lower()
    score=BASE.get(kind,25)
    reasons=[]
    for word,points in BOOSTS.items():
        if word in text:
            score+=points
            reasons.append(word)

    if kind in {"url","domain","ipv4"} and any(x in text for x in ["c2","command and control","callback"]):
        score+=15

    score=min(100,score)
    if score>=85: sev="Critical"
    elif score>=65: sev="High"
    elif score>=35: sev="Medium"
    else: sev="Low"

    confidence=min(.99, .55 + score/225)
    return score,sev,round(confidence,2)
