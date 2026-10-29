# Marks lessons as ready when their JSON exists; run after adding lessons.
import json, os
ROOT = os.path.join(os.path.dirname(__file__), "..")
p = os.path.join(ROOT, "data", "courses", "index.json")
cat = json.load(open(p))
for c in cat:
    for u in c["units"]:
        for l in u["lessons"]:
            f = os.path.join(ROOT, "data", "lessons", c["id"], l["id"] + ".json")
            l["ready"] = os.path.exists(f)
            if l["ready"]:
                d = json.load(open(f))
                if d.get("lede"): l["desc"] = d["lede"]
json.dump(cat, open(p, "w"), indent=1, ensure_ascii=False)
print({c["id"]: sum(l["ready"] for u in c["units"] for l in u["lessons"]) for c in cat})
