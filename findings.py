from src.models import Finding

def build_findings(iocs, text):
    findings=[]
    low=text.lower()

    if any(x in low for x in ["ransomware","encrypted files","file encryption"]):
        findings.append(Finding(
            "Potential Ransomware Behavior","Impact","Critical",
            "The evidence contains ransomware or file-encryption terminology.",
            "ransomware / encryption language detected",90))

    if any(x in low for x in ["phishing","credential harvesting","malicious attachment"]):
        findings.append(Finding(
            "Potential Phishing Activity","Initial Access","High",
            "The source contains phishing or credential-harvesting indicators.",
            "phishing-related language detected",75))

    if any(i.tactic=="Command and Control" for i in iocs):
        findings.append(Finding(
            "Command-and-Control Indicators","Command and Control","High",
            "Network indicators were associated with callback or C2 context.",
            "IOC context mapped to C2 behavior",82))

    if any(i.tactic=="Persistence" for i in iocs):
        findings.append(Finding(
            "Persistence Behavior","Persistence","High",
            "Evidence references startup or registry persistence.",
            "persistence-related IOC context",78))

    return findings
