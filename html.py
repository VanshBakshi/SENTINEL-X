from pathlib import Path
from jinja2 import Template

HTML = """<!doctype html><html><head><meta charset="utf-8">
<title>SENTINEL-X Report</title>
<style>
body{margin:0;background:#07111f;color:#dbeafe;font:15px Arial}
header{padding:35px;background:linear-gradient(135deg,#0b2447,#111827)}
h1{font-size:34px}.wrap{padding:28px}.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.card{background:#0f1d31;border:1px solid #203653;border-radius:16px;padding:20px;margin-bottom:18px}
.metric{font-size:30px;font-weight:bold}.muted{color:#8ca3bd}
table{width:100%;border-collapse:collapse}td,th{padding:10px;border-bottom:1px solid #223550;text-align:left}
</style></head><body>
<header><h1>🛡️ SENTINEL-X</h1><div class="muted">AI Threat Intelligence & SOC Investigation Report</div></header>
<div class="wrap"><div class="grid">
<div class="card"><div class="metric">{{total}}</div><div class="muted">IOCs</div></div>
<div class="card"><div class="metric">{{critical}}</div><div class="muted">Critical</div></div>
<div class="card"><div class="metric">{{high}}</div><div class="muted">High</div></div>
<div class="card"><div class="metric">{{avg}}</div><div class="muted">Average Risk</div></div>
</div>
<div class="card"><h2>Attack Chain</h2>{% for a,b in chain %}<p><b>{{a}}</b> → {{b}}</p>{% endfor %}</div>
<div class="card"><h2>Findings</h2>{% for f in findings %}<p><b>{{f.severity}}</b> — {{f.title}}<br><span class="muted">{{f.description}}</span></p>{% endfor %}</div>
<div class="card"><h2>IOC Inventory</h2><table><tr><th>IOC</th><th>Type</th><th>Risk</th><th>Severity</th><th>MITRE</th></tr>
{% for i in iocs %}<tr><td>{{i.value}}</td><td>{{i.ioc_type}}</td><td>{{i.risk}}</td><td>{{i.severity}}</td><td>{{i.technique}}</td></tr>{% endfor %}
</table></div></div></body></html>"""

def html_export(iocs,findings,chain,path):
    html=Template(HTML).render(
        iocs=iocs,findings=findings,chain=chain,total=len(iocs),
        critical=sum(x.severity=="Critical" for x in iocs),
        high=sum(x.severity=="High" for x in iocs),
        avg=round(sum(x.risk for x in iocs)/len(iocs),1) if iocs else 0)
    Path(path).write_text(html,encoding="utf-8")
