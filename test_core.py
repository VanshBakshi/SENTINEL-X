from src.extraction.extractor import extract
from src.enrichment.risk import calculate_risk

def test_ip_and_hash():
    text="malware C2 callback 203.0.113.9 hash aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    items=extract(text,"x.txt")
    assert any(x.ioc_type=="ipv4" for x in items)
    assert any(x.ioc_type=="sha256" for x in items)

def test_risk():
    a=calculate_risk("domain","example.test","normal documentation")
    b=calculate_risk("domain","evil.test","malware command and control callback")
    assert b[0]>a[0]
