import yaml, json, os
with open("data/trainingsplan.yaml", encoding="utf-8") as f:
    y = yaml.safe_load(f)
os.makedirs("site", exist_ok=True)
with open("site/trainingsplan.json","w",encoding="utf-8") as f:
    json.dump(y, f, ensure_ascii=False, indent=2)
print("Wrote site/trainingsplan.json")
