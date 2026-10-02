from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
with open(ROOT/"config/settings.yaml", encoding="utf-8") as f:
    SETTINGS = yaml.safe_load(f)
with open(ROOT/"config/mitre.yaml", encoding="utf-8") as f:
    MITRE = yaml.safe_load(f)

OUTPUT = ROOT / SETTINGS["paths"]["output"]
OUTPUT.mkdir(parents=True, exist_ok=True)
