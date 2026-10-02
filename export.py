import json,csv
from pathlib import Path

def json_export(iocs,path):
    Path(path).write_text(json.dumps([x.to_dict() for x in iocs],indent=2),encoding="utf-8")

def csv_export(iocs,path):
    fields=["value","ioc_type","normalized","source","risk","severity","confidence","technique","tactic","first_seen","context"]
    with open(path,"w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=fields)
        w.writeheader()
        for x in iocs:
            d=x.to_dict()
            w.writerow({k:d.get(k,"") for k in fields})

def markdown_export(iocs,findings,chain,path):
    lines=["# SENTINEL-X Threat Intelligence Report","","## Executive Summary",
           f"- Total IOCs: {len(iocs)}",
           f"- Critical: {sum(x.severity=='Critical' for x in iocs)}",
           f"- High: {sum(x.severity=='High' for x in iocs)}","",
           "## Attack Chain"]
    for a,b in chain: lines.append(f"- **{a}** → {b}")
    lines += ["","## Findings"]
    for f in findings: lines.append(f"- **{f.severity}: {f.title}** — {f.description}")
    lines += ["","## IOC Inventory",""]
    for x in sorted(iocs,key=lambda z:z.risk,reverse=True):
        lines.append(f"- `{x.value}` | {x.ioc_type} | Risk {x.risk} | {x.severity} | {x.technique}")
    Path(path).write_text("\n".join(lines),encoding="utf-8")
