# 🛡️ SENTINEL-X

## AI-Powered Threat Intelligence & SOC Investigation Platform

<p align="center">

**Transforming raw threat reports and security logs into actionable cyber threat intelligence.**

<br/>

`Python` · `NLP` · `Transformers` · `spaCy` · `MITRE ATT&CK` · `Streamlit` · `SQLite` · `Plotly`

</p>

---

## 🚨 What is SENTINEL-X?

**SENTINEL-X** is an AI-assisted Cyber Threat Intelligence and Security Operations Center platform designed to analyze threat reports, incident logs, and security evidence.

Instead of manually searching hundreds of lines of logs for suspicious indicators, SENTINEL-X automatically:

> **Ingests → Extracts → Normalizes → Enriches → Scores → Maps → Correlates → Visualizes → Reports**

It converts unstructured security information into an analyst-friendly investigation workspace.

### Example

A raw report containing:

```text
2026-10-01 08:52 C2 callback detected from 203.0.113.77.
PowerShell downloaded a payload from
https://cdn-example.test/update/payload.exe.
The activity was associated with phishing and ransomware.
```

can become:

```text
┌─────────────────────────────────────────────┐
│ 🚨 THREAT DETECTED                          │
├─────────────────────────────────────────────┤
│ IOC: 203.0.113.77                            │
│ Type: IPv4                                   │
│ Risk: 91/100                                 │
│ Severity: CRITICAL                           │
│ Tactic: Command & Control                    │
│ MITRE: T1071.001                             │
└─────────────────────────────────────────────┘
```

---

# ✨ Core Capabilities

## 🔎 Intelligent IOC Extraction

Automatically identifies security indicators including:

| IOC           | Description                   |
| ------------- | ----------------------------- |
| 🌐 IPv4       | Suspicious IP addresses       |
| 🌍 Domains    | Potential malicious domains   |
| 🔗 URLs       | Suspicious web resources      |
| 📧 Emails     | Phishing/suspicious addresses |
| 🔐 MD5        | File hashes                   |
| 🔐 SHA1       | File hashes                   |
| 🔐 SHA256     | File hashes                   |
| 🐛 CVE        | Vulnerability identifiers     |
| 🪟 Registry   | Windows registry indicators   |
| 📁 File Paths | Suspicious Windows paths      |

---

# 🧠 AI & NLP Intelligence

SENTINEL-X uses a **hybrid intelligence architecture**.

### Deterministic Security Intelligence

High-confidence security extraction is handled using:

* Regular expressions
* Context windows
* IOC normalization
* Deduplication
* Rule-based behavior detection

### NLP Intelligence

The platform can use:

* **spaCy** for entity extraction
* **Hugging Face Transformers** for text classification
* Context-aware threat analysis

This hybrid approach is intentional.

Security-critical indicators should remain explainable instead of relying entirely on a black-box model.

---

# 🎯 Risk Intelligence Engine

Every IOC receives a calculated risk score.

```text
IOC
 │
 ├── Indicator Type
 │
 ├── Threat Context
 │
 ├── Suspicious Keywords
 │
 ├── Behavioral Context
 │
 └── MITRE Mapping
       │
       ▼
   Risk Engine
       │
       ▼
  0 ─────────────── 100
```

### Severity Model

|      Score | Severity    |
| ---------: | ----------- |
| `85 - 100` | 🔴 CRITICAL |
|  `65 - 84` | 🟠 HIGH     |
|  `35 - 64` | 🟡 MEDIUM   |
|   `0 - 34` | 🟢 LOW      |

The system also calculates an IOC confidence value.

---

# 🎯 MITRE ATT&CK Mapping

SENTINEL-X maps observed behaviors to **MITRE ATT&CK techniques**.

Examples:

```text
PowerShell
     ↓
T1059.001
     ↓
PowerShell
     ↓
Execution
```

```text
Phishing
     ↓
T1566
     ↓
Initial Access
```

```text
C2 Callback
     ↓
T1071.001
     ↓
Command & Control
```

```text
Ransomware
     ↓
T1486
     ↓
Impact
```

The dashboard provides visibility into observed tactics and techniques.

---

# 🧬 Attack Chain Reconstruction

SENTINEL-X attempts to reconstruct the progression of an incident.

Example:

```text
┌──────────────┐
│ Initial      │
│ Access       │
│ Phishing     │
└──────┬───────┘
       ↓
┌──────────────┐
│ Execution    │
│ PowerShell   │
└──────┬───────┘
       ↓
┌──────────────┐
│ Persistence  │
│ Registry     │
└──────┬───────┘
       ↓
┌──────────────┐
│ Command &    │
│ Control      │
└──────┬───────┘
       ↓
┌──────────────┐
│ Impact       │
│ Ransomware   │
└──────────────┘
```

This provides analysts with a higher-level understanding of the incident instead of showing isolated indicators.

---

# 🕸️ IOC Relationship Graph

SENTINEL-X can visualize relationships between indicators.

```text
                    ┌─────────────┐
                    │  Phishing   │
                    └──────┬──────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ malicious email │
                  └────────┬────────┘
                           │
             ┌─────────────┴─────────────┐
             ▼                           ▼
      ┌─────────────┐             ┌──────────────┐
      │ Malicious   │             │ PowerShell   │
      │ URL         │             │ Execution    │
      └──────┬──────┘             └──────┬───────┘
             │                           │
             └────────────┬──────────────┘
                          ▼
                   ┌─────────────┐
                   │ C2 Server   │
                   └─────────────┘
```

The dashboard provides an interactive graph for investigating relationships between indicators.

---

# 📊 SOC Dashboard

SENTINEL-X includes a Streamlit-based investigation dashboard.

### Dashboard capabilities

* 🚨 Critical IOC counter
* ⚠️ High-risk counter
* 🔎 Total indicator count
* 🛡️ Security posture score
* 📊 Severity distribution
* 🥧 IOC composition
* 🎯 MITRE coverage
* 🧬 Attack-chain visualization
* 🕸️ IOC relationship graph
* 🔍 IOC filtering
* 📄 Evidence viewer
* 📥 Report downloads

---

# 🖥️ Application Architecture

```text
                    ┌───────────────────────┐
                    │ Threat Reports / Logs │
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │     INGESTION LAYER   │
                    │ TXT / LOG / MD / JSON │
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │     IOC EXTRACTION    │
                    │ IP / URL / HASH / CVE │
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │ NORMALIZATION ENGINE  │
                    │ Deduplication         │
                    └───────────┬───────────┘
                                │
                   ┌────────────┴────────────┐
                   ▼                         ▼
          ┌─────────────────┐      ┌─────────────────┐
          │   NLP ENGINE    │      │   RISK ENGINE   │
          │ spaCy / HF      │      │ Score / Severity│
          └────────┬────────┘      └────────┬────────┘
                   │                        │
                   └────────────┬───────────┘
                                ▼
                    ┌───────────────────────┐
                    │   MITRE ATT&CK MAP    │
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │ CORRELATION & ANALYSIS│
                    │ Attack Chain / Graph  │
                    └───────────┬───────────┘
                                │
              ┌─────────────────┼─────────────────┐
              ▼                 ▼                 ▼
        ┌───────────┐    ┌────────────┐    ┌─────────────┐
        │ Dashboard │    │  Database  │    │  Reports    │
        │ Streamlit │    │  SQLite    │    │ JSON/CSV/MD │
        └───────────┘    └────────────┘    └─────────────┘
```

---

# 📁 Project Structure

```text
SENTINEL_X/
│
├── 📄 README.md
├── 📄 LICENSE
├── 📄 requirements.txt
├── 📄 requirements-minimal.txt
├── 📄 .gitignore
├── 📄 .env.example
├── 📄 main.py
├── 📄 app.py
├── 📄 run.bat
├── 📄 run.sh
│
├── ⚙️ config/
│   ├── settings.yaml
│   └── mitre.yaml
│
├── 📊 data/
│   ├── demo/
│   │   ├── incident_report.txt
│   │   └── security.log
│   │
│   └── output/
│
├── 🧠 src/
│   │
│   ├── models.py
│   ├── config.py
│   ├── pipeline.py
│   │
│   ├── ingest/
│   │   └── loader.py
│   │
│   ├── extraction/
│   │   ├── patterns.py
│   │   └── extractor.py
│   │
│   ├── nlp/
│   │   ├── spacy_engine.py
│   │   └── transformer.py
│   │
│   ├── enrichment/
│   │   ├── normalizer.py
│   │   ├── risk.py
│   │   ├── mitre.py
│   │   └── timeline.py
│   │
│   ├── analysis/
│   │   ├── findings.py
│   │   ├── attack_chain.py
│   │   └── graph.py
│   │
│   ├── storage/
│   │   └── database.py
│   │
│   └── reporting/
│       ├── export.py
│       └── html.py
│
└── 🧪 tests/
    └── test_core.py
```

---

# ⚙️ Technology Stack

### Programming

* Python 3.10+
* Object-Oriented Programming
* Modular architecture

### AI / NLP

* spaCy
* Hugging Face Transformers
* PyTorch

### Data Processing

* Pandas
* NumPy
* Regular Expressions

### Visualization

* Streamlit
* Plotly
* NetworkX

### Storage

* SQLite

### Configuration

* YAML
* Environment variables

### Testing

* PyTest

---

# 🚀 Installation

## 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd SENTINEL_X
```

---

## 2. Create a virtual environment

### Windows

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

For a lightweight installation:

```bash
pip install -r requirements-minimal.txt
```

---

# 🧠 Optional spaCy Model

Install the English model:

```bash
python -m spacy download en_core_web_sm
```

If the model is unavailable, SENTINEL-X continues operating using its deterministic extraction layer.

---

# ▶️ Run the CLI

Run the included demo incident:

```bash
python main.py --input data/demo
```

Example:

```text
╔══════════════════════════════════════════╗
║       🛡️  SENTINEL-X SOC ENGINE         ║
╚══════════════════════════════════════════╝

✓ Analysis complete

IOCs: 8
Findings: 4
Attack-chain phases: 5
```

---

# 🌐 Launch the SOC Dashboard

```bash
streamlit run app.py
```

Then open the local Streamlit address displayed in your terminal.

---

# 📄 Analyze Your Own Threat Report

Place your file inside the project or provide its path:

```bash
python main.py --input path/to/report.txt
```

You can analyze:

```text
.txt
.log
.md
.json
.csv
```

---

# 📤 Generated Intelligence

After analysis, SENTINEL-X generates:

```text
data/output/

├── iocs.json
├── iocs.csv
├── threat_report.md
├── threat_report.html
└── sentinel.db
```

### JSON

Machine-readable IOC intelligence.

### CSV

Useful for:

* Excel
* Power BI
* SIEM ingestion
* Data analysis

### HTML

Analyst-friendly investigation report.

### Markdown

Easy to publish in GitHub documentation or incident reports.

### SQLite

Persistent local investigation storage.

---

# 🔬 Example IOC Output

```json
{
    "value": "203.0.113.77",
    "ioc_type": "ipv4",
    "normalized": "203.0.113.77",
    "source": "incident_report.txt",
    "risk": 91,
    "severity": "Critical",
    "confidence": 0.95,
    "technique": "T1071.001 Web Protocols",
    "tactic": "Command and Control"
}
```

---

# 🧪 Testing

Run:

```bash
pytest -q
```

The test suite verifies:

* IOC extraction
* hash detection
* risk scoring
* suspicious-context scoring

---

# 🔐 Security Design

SENTINEL-X follows a **defensive-by-design** architecture.

It analyzes supplied information and does not:

* ❌ exploit vulnerabilities
* ❌ attack external systems
* ❌ execute extracted commands
* ❌ deploy malware
* ❌ steal credentials
* ❌ perform unauthorized scanning

The project is intended for:

* SOC learning
* Threat intelligence
* Incident investigation
* Security analytics
* Cybersecurity education
* Portfolio demonstration

---

# 🧩 Example Investigation

### Input

```text
A phishing email was delivered to a user.

The user opened the malicious attachment.

PowerShell downloaded a payload from:
https://cdn-example.test/update/payload.exe

The malware contacted:
203.0.113.77

The activity simulated ransomware encryption.
```

### SENTINEL-X interpretation

```text
Initial Access
      │
      └── Phishing
            │
            ▼
Execution
      │
      └── PowerShell
            │
            ▼
Command & Control
      │
      └── 203.0.113.77
            │
            ▼
Impact
      │
      └── Ransomware
```

---

# 🏆 Why This Project Is Different

Most beginner cybersecurity projects stop at:

```text
Regex → IOC
```

SENTINEL-X goes further:

```text
Raw Evidence
     ↓
IOC Extraction
     ↓
Context Analysis
     ↓
Risk Scoring
     ↓
Confidence
     ↓
MITRE ATT&CK
     ↓
Attack Chain
     ↓
Relationship Graph
     ↓
Analyst Findings
     ↓
SOC Dashboard
     ↓
Machine + Human Reports
```

The goal is not simply to find an IP address.

The goal is to answer:

> **What happened, what indicators are involved, how risky are they, what behavior do they represent, and how can an analyst investigate the evidence?**

---

# 🔮 Roadmap

## Phase 1 — Current

* [x] IOC extraction
* [x] IOC normalization
* [x] Risk scoring
* [x] Confidence scoring
* [x] MITRE mapping
* [x] Attack-chain reconstruction
* [x] IOC graph
* [x] NLP integration
* [x] SOC dashboard
* [x] SQLite storage
* [x] Report generation

## Phase 2 — Planned

* [ ] VirusTotal enrichment
* [ ] MISP integration
* [ ] OpenCTI integration
* [ ] STIX 2.1 export
* [ ] YARA integration
* [ ] Sigma rule correlation
* [ ] Elasticsearch/OpenSearch
* [ ] Threat-feed ingestion
* [ ] Scheduled analysis

## Phase 3 — Advanced AI

* [ ] RAG threat-intelligence assistant
* [ ] Vector database
* [ ] Similar incident detection
* [ ] Custom cybersecurity NER model
* [ ] Automatic report summarization
* [ ] Analyst feedback loop
* [ ] Explainable AI recommendations
* [ ] Threat actor clustering
* [ ] Campaign correlation

---

# 💼 Real-World Use Cases

### SOC Analyst

Analyze incoming security alerts and identify high-priority indicators.

### Threat Intelligence Analyst

Extract and organize indicators from intelligence reports.

### Incident Response

Understand the sequence of suspicious activity.

### Security Research

Analyze large collections of public threat reports.

### Cybersecurity Education

Demonstrate practical applications of AI and NLP in security operations.

---

# 📈 Future Production Architecture

```text
                    Internet / Threat Feeds
                              │
                              ▼
                     ┌──────────────────┐
                     │ Collection Layer │
                     └────────┬─────────┘
                              │
              ┌───────────────┼────────────────┐
              ▼               ▼                ▼
          MISP Feed       OpenCTI          Reports
              │               │                │
              └───────────────┼────────────────┘
                              ▼
                    ┌──────────────────┐
                    │ SENTINEL-X Core │
                    └────────┬─────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
          IOC Engine      AI/NLP       Correlation
              │              │              │
              └──────────────┼──────────────┘
                             ▼
                     MITRE ATT&CK
                             │
                             ▼
                     Risk Intelligence
                             │
             ┌───────────────┼────────────────┐
             ▼               ▼                ▼
          SIEM/SOC       Dashboard        Reports
```

---

# 📊 Project Metrics

| Component          | Capability |
| ------------------ | ---------- |
| IOC Types          | 10+        |
| Risk Levels        | 4          |
| NLP Engines        | 2          |
| MITRE Mapping      | Included   |
| Attack Chain       | Included   |
| Relationship Graph | Included   |
| Dashboard          | Included   |
| Database           | SQLite     |
| Export Formats     | 4          |
| Test Framework     | PyTest     |

---

# 👨‍💻 Author

**Your Name**

Cybersecurity • AI • Python • Threat Intelligence

### Areas of Interest

* Artificial Intelligence
* Cybersecurity
* Threat Intelligence
* Security Operations
* Python Development
* NLP
* Data Analytics

---

# ⭐ If You Like This Project

Give the repository a ⭐ and feel free to extend the platform with additional threat-intelligence providers and enterprise integrations.

---

# ⚠️ Disclaimer

SENTINEL-X is an educational and defensive cybersecurity project.

The included incident data is fictional and intended for software demonstration.

Users are responsible for ensuring that any security analysis they perform is authorized and complies with applicable laws, organizational policies, and the terms of the systems and data being analyzed.

---

<div align="center">

## 🛡️ SENTINEL-X

### **From Raw Threat Data → Actionable Security Intelligence**

`Analyze • Correlate • Understand • Defend`

</div>
