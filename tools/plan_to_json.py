import yaml, json, os, sys

def load_yaml(path):
    if not os.path.exists(path):
        return {}
    try:
        with open(path, encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    except yaml.YAMLError as e:
        print(f"\nYAML parse error in {path}:\n{e}\n")
        # Hinweise auf typische Copy&Paste-Fehler (Backticks/Codefences)
        with open(path, encoding="utf-8") as f2:
            for i, line in enumerate(f2.read().splitlines(), start=1):
                if "`" in line or line.strip().startswith("```"):
                    print(f"Hint: possible markdown fence/backtick on line {i}: {line}")
        sys.exit(1)

plan = load_yaml("data/trainingsplan.yaml")
sperren = load_yaml("data/sperren.yaml")

# Struktur absichern
if not isinstance(plan, dict):
    print("Error: data/trainingsplan.yaml must parse to a mapping (dict).")
    sys.exit(1)
plan.setdefault("plaetze", [])
plan.setdefault("tage", [])
plan.setdefault("slots", [])

# Sperren mergen (falls Datei fehlt/leer)
if not isinstance(sperren, dict):
    sperren = {}
plan["sperren"] = {
    "weekly": sperren.get("weekly") or [],
    "once":   sperren.get("once")   or [],
}

os.makedirs("site", exist_ok=True)
with open("site/trainingsplan.json", "w", encoding="utf-8") as f:
    json.dump(plan, f, ensure_ascii=False, indent=2)

print(
    f"Wrote site/trainingsplan.json "
    f"(slots={len(plan['slots'])}, weekly_sperren={len(plan['sperren']['weekly'])}, once_sperren={len(plan['sperren']['once'])})"
)
