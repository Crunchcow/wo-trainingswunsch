import yaml, json, os, sys
from datetime import datetime

def load_yaml(path):
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

plan = load_yaml("data/trainingsplan.yaml")
sperren = load_yaml("data/sperren.yaml")

# Merge Sperren in den Plan
plan["sperren"] = {
    "weekly": sperren.get("weekly", []),
    "once":   sperren.get("once",   []),
}

# Minimal-Validierung
plan.setdefault("plaetze", [])
plan.setdefault("tage", [])
plan.setdefault("slots", [])

os.makedirs("site", exist_ok=True)
out_path = "site/trainingsplan.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(plan, f, ensure_ascii=False, indent=2)

print(f"Wrote {out_path} ({len(plan['slots'])} slots, "
      f"{len(plan['sperren']['weekly'])} weekly sperren, "
      f"{len(plan['sperren']['once'])} once)")
