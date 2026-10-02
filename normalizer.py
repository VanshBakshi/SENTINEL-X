import re

def normalize(value, kind):
    value=value.strip().strip(".,;:)]}")
    if kind in {"url","domain","email"}:
        value=value.lower()
    if kind=="url":
        value=re.sub(r"^https?://","",value,flags=re.I).rstrip("/")
    if kind=="cve":
        value=value.upper()
    return value
