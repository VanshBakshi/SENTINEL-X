PHASES = [
    ("Initial Access","Phishing"),
    ("Execution","PowerShell"),
    ("Persistence","Registry"),
    ("Command and Control","C2"),
    ("Impact","Ransomware")
]

def reconstruct(text, iocs):
    low=text.lower()
    chain=[]
    for tactic,label in PHASES:
        if tactic=="Initial Access" and any(x in low for x in ["phishing","attachment"]):
            chain.append((tactic,label))
        elif tactic=="Execution" and any(x in low for x in ["powershell","cmd.exe","script"]):
            chain.append((tactic,label))
        elif tactic=="Persistence" and any(x in low for x in ["registry","startup","run key"]):
            chain.append((tactic,label))
        elif tactic=="Command and Control" and any(i.tactic=="Command and Control" for i in iocs):
            chain.append((tactic,label))
        elif tactic=="Impact" and any(x in low for x in ["ransomware","encrypted"]):
            chain.append((tactic,label))
    return chain
