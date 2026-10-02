# 🛡️ SENTINEL-X — AI Threat Intelligence & SOC Platform

**SENTINEL-X** is a portfolio-grade defensive cyber threat intelligence platform built with Python.

It turns raw threat reports and logs into an analyst-ready investigation:

```text
THREAT REPORT / LOG
        ↓
Document Intelligence
        ↓
IOC Extraction
        ↓
Normalization + Deduplication
        ↓
AI/NLP Context Analysis
        ↓
Risk & Confidence Engine
        ↓
MITRE ATT&CK Mapping
        ↓
Attack Chain Reconstruction
        ↓
IOC Relationship Graph
        ↓
SOC Dashboard + Reports
```

## 🔥 Highlights

- IOC extraction for IPs, domains, URLs, emails, hashes and CVEs
- Context-aware risk scoring
- IOC confidence scoring
- MITRE ATT&CK technique mapping
- Attack-chain reconstruction
- Timeline extraction
- Threat-category classification
- Entity extraction with spaCy
- Optional Transformer NLP
- IOC relationship graph
- Executive summary
- Analyst investigation workspace
- Search/filter/sort
- SQLite evidence store
- JSON / CSV / HTML / Markdown exports
- Streamlit SOC dashboard
- Demo incident included
- Unit tests
- No offensive execution or exploitation

## ⚡ Start

### Windows

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

Then:

```powershell
streamlit run app.py
```

### Quick demo

```powershell
python main.py --input data/demo
```

## 📊 Dashboard

The dashboard includes:

- Security posture score
- IOC risk distribution
- Critical/high IOC counter
- MITRE ATT&CK coverage
- attack-chain view
- threat timeline
- IOC graph
- analyst table
- evidence/context viewer
- export controls

## 🧠 AI layer

The project uses a hybrid architecture.

**Deterministic security extraction**
- high precision regex patterns
- normalization
- deduplication
- contextual scoring

**NLP**
- spaCy entities
- optional Hugging Face Transformers classification

**Security intelligence**
- MITRE ATT&CK rule mapping
- behavior detection
- risk scoring
- confidence calculation
- attack-chain reconstruction

The deterministic layer keeps important IOC extraction explainable instead of hiding every decision inside a black-box model.

## 🔐 Defensive scope

SENTINEL-X analyzes supplied defensive reports and logs. It does not exploit systems, deploy malware, steal credentials, scan targets, or execute extracted commands.

## 🚀 Future integrations

- VirusTotal
- MISP
- OpenCTI
- STIX 2.1
- YARA
- Sigma
- Elasticsearch/OpenSearch
- threat-feed APIs
- RAG over internal threat reports
- analyst feedback learning
