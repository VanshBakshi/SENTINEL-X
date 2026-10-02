import re

def find_date(text):
    m=re.search(r"\b20\d{2}[-/]\d{1,2}[-/]\d{1,2}(?:[T ]\d{2}:\d{2}(?::\d{2})?)?",text)
    return m.group(0) if m else "Unknown"
