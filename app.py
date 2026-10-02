import json
import tempfile
from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from src.pipeline import SentinelPipeline

st.set_page_config(page_title="SENTINEL-X",page_icon="🛡️",layout="wide")

st.markdown("""
<style>
.stApp{background:#07111f}
.block-container{padding-top:1.5rem}
.hero{padding:28px;border:1px solid #203653;border-radius:20px;
background:linear-gradient(135deg,#0b2447,#101827);margin-bottom:22px}
.hero h1{font-size:42px;margin:0}
.hero p{color:#8ca3bd}
.metric-card{background:#0f1d31;border:1px solid #203653;border-radius:15px;padding:18px}
</style>
""",unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>🛡️ SENTINEL-X</h1>
<p>AI Threat Intelligence & SOC Investigation Platform • v2.0</p>
</div>
""",unsafe_allow_html=True)

with st.sidebar:
    st.header("⚙️ Investigation")
    upload=st.file_uploader("Threat report / log",type=["txt","log","md","json"])
    demo=st.button("🚀 Load Demo Incident",use_container_width=True)
    st.divider()
    st.caption("Defensive analysis only")
    st.caption("IOC extraction • NLP • MITRE • Risk • Attack Chain")

source=None
if upload:
    tmp=Path(tempfile.gettempdir())/upload.name
    tmp.write_bytes(upload.getvalue())
    source=str(tmp)
elif demo:
    source="data/demo"

if not source:
    st.info("Upload a report/log or click **Load Demo Incident**.")
    st.stop()

with st.spinner("Running SENTINEL-X investigation..."):
    result=SentinelPipeline().run(source)

iocs=result["iocs"]
findings=result["findings"]
chain=result["chain"]

df=pd.DataFrame([x.to_dict() for x in iocs]) if iocs else pd.DataFrame()

if df.empty:
    st.warning("No indicators detected.")
    st.stop()

total=len(df); critical=int((df.severity=="Critical").sum())
high=int((df.severity=="High").sum())
medium=int((df.severity=="Medium").sum())
posture=max(0,100-int(df.risk.mean()))

a,b,c,d=st.columns(4)
a.metric("🔎 Indicators",total)
b.metric("🚨 Critical",critical)
c.metric("⚠️ High",high)
d.metric("🛡️ Posture",f"{posture}/100")

tabs=st.tabs(["📊 Overview","🧬 Attack Chain","🕸️ IOC Graph","🎯 MITRE","🔍 IOC Explorer","📄 Reports"])

with tabs[0]:
    left,right=st.columns(2)
    with left:
        vc=df.severity.value_counts().reset_index()
        vc.columns=["severity","count"]
        st.plotly_chart(px.bar(vc,x="severity",y="count",title="Risk Severity Distribution"),use_container_width=True)
    with right:
        tc=df.ioc_type.value_counts().reset_index()
        tc.columns=["type","count"]
        st.plotly_chart(px.pie(tc,values="count",names="type",title="IOC Composition"),use_container_width=True)

    st.subheader("🚨 Analyst Findings")
    for f in findings:
        st.warning(f"**{f.severity} — {f.title}**  \n{f.description}")

with tabs[1]:
    st.subheader("🧬 Reconstructed Attack Chain")
    if chain:
        cols=st.columns(len(chain))
        for col,(phase,label) in zip(cols,chain):
            col.markdown(f"### {label}")
            col.caption(phase)
            col.success("Observed")
    else:
        st.info("No multi-stage attack chain reconstructed.")

with tabs[2]:
    st.subheader("🕸️ Indicator Relationship Graph")
    import networkx as nx
    g=result["graph"]
    pos=nx.spring_layout(g,seed=42)
    edge_x=[];edge_y=[]
    for a,b in g.edges():
        edge_x += [pos[a][0],pos[b][0],None]
        edge_y += [pos[a][1],pos[b][1],None]
    node_x=[pos[n][0] for n in g.nodes()]
    node_y=[pos[n][1] for n in g.nodes()]
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=edge_x,y=edge_y,mode="lines",line=dict(width=1),hoverinfo="none"))
    fig.add_trace(go.Scatter(x=node_x,y=node_y,mode="markers+text",
        text=list(g.nodes()),textposition="top center",
        marker=dict(size=16),hoverinfo="text"))
    fig.update_layout(height=600,showlegend=False,xaxis=dict(visible=False),yaxis=dict(visible=False))
    st.plotly_chart(fig,use_container_width=True)

with tabs[3]:
    st.subheader("🎯 MITRE ATT&CK Coverage")
    mitre=df[df.technique!="Unmapped"]
    if not mitre.empty:
        m=mitre.tactic.value_counts().reset_index()
        m.columns=["tactic","count"]
        st.plotly_chart(px.bar(m,x="tactic",y="count",title="Observed Tactics"),use_container_width=True)
        st.dataframe(mitre[["technique","tactic","risk","severity"]].drop_duplicates(),
                     use_container_width=True,hide_index=True)
    else:
        st.info("No MITRE mappings found.")

with tabs[4]:
    st.subheader("🔍 IOC Explorer")
    col1,col2=st.columns(2)
    types=sorted(df.ioc_type.unique())
    severities=sorted(df.severity.unique())
    with col1:
        selected_types=st.multiselect("IOC type",types,default=types)
    with col2:
        selected_sev=st.multiselect("Severity",severities,default=severities)
    view=df[df.ioc_type.isin(selected_types)&df.severity.isin(selected_sev)]
    st.dataframe(view[["value","ioc_type","risk","severity","confidence","technique","tactic","source"]],
                 use_container_width=True,hide_index=True)
    selected=st.selectbox("Evidence viewer",view.value.tolist() if not view.empty else [""])
    if selected:
        row=view[view.value==selected].iloc[0]
        st.code(row.context)

with tabs[5]:
    st.subheader("📄 Generated Intelligence")
    out=Path("data/output")
    for name,label in [("threat_report.html","HTML analyst report"),
                       ("threat_report.md","Markdown report"),
                       ("iocs.json","JSON IOC feed"),
                       ("iocs.csv","CSV IOC feed")]:
        p=out/name
        if p.exists():
            st.download_button(f"⬇️ {label}",p.read_bytes(),file_name=name)
    st.success("Reports are generated automatically after each investigation.")
