import re

PATTERNS = {
    "ipv4": re.compile(r"\b(?:(?:25[0-5]|2[0-4]\d|1?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|1?\d?\d)\b"),
    "url": re.compile(r"https?://[^\s<>'\"]+", re.I),
    "email": re.compile(r"\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b"),
    "sha256": re.compile(r"\b[a-fA-F0-9]{64}\b"),
    "sha1": re.compile(r"\b[a-fA-F0-9]{40}\b"),
    "md5": re.compile(r"\b[a-fA-F0-9]{32}\b"),
    "cve": re.compile(r"\bCVE-\d{4}-\d{4,7}\b", re.I),
    "domain": re.compile(r"\b(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,63}\b"),
    "registry": re.compile(r"\b(?:HKLM|HKCU|HKCR|HKU|HKCC)\\[^\s,;]+", re.I),
    "windows_path": re.compile(r"\b[A-Za-z]:\\(?:[^\\\r\n]+\\)*[^\\\r\n]+")
}
