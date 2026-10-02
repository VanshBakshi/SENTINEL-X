from src.config import OUTPUT,SETTINGS
from src.ingest.loader import load_source
from src.extraction.extractor import extract
from src.nlp.spacy_engine import SpacyEngine
from src.nlp.transformer import TransformerEngine
from src.analysis.findings import build_findings
from src.analysis.attack_chain import reconstruct
from src.analysis.graph import build_graph
from src.reporting.export import json_export,csv_export,markdown_export
from src.reporting.html import html_export
from src.storage.database import Database

class SentinelPipeline:
    def __init__(self):
        self.spacy=SpacyEngine(SETTINGS["nlp"]["spacy_model"])
        self.transformer=TransformerEngine(
            SETTINGS["nlp"]["transformer_model"],
            SETTINGS["nlp"]["enabled"])

    def run(self,source):
        docs=load_source(source)
        all_iocs=[]
        full_text=""
        nlp=[]
        for name,text in docs:
            full_text += "\n" + text
            all_iocs.extend(extract(text,name))
            nlp.append({"source":name,"entities":self.spacy.analyze(text),
                        "transformer":self.transformer.classify(text)})

        unique={}
        for i in all_iocs:
            unique[(i.ioc_type,i.normalized)]=i
        iocs=list(unique.values())

        findings=build_findings(iocs,full_text)
        chain=reconstruct(full_text,iocs)
        graph=build_graph(iocs)

        json_export(iocs,OUTPUT/"iocs.json")
        csv_export(iocs,OUTPUT/"iocs.csv")
        markdown_export(iocs,findings,chain,OUTPUT/"threat_report.md")
        html_export(iocs,findings,chain,OUTPUT/"threat_report.html")

        db=Database()
        db.save(iocs)
        db.close()

        return {
            "iocs":iocs,"findings":findings,"chain":chain,
            "graph":graph,"nlp":nlp,"documents":docs
        }
