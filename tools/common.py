import json, os
ROOT = os.path.join(os.path.dirname(__file__), "..")
def T(md): return {"type": "text", "md": md}
def N(label, md): return {"type": "note", "label": label, "md": md}
def E(title, problem, steps, answer): return {"type": "example", "title": title, "problem": problem, "steps": steps, "answer": answer}
def TERMS(terms, label=None):
    d = {"type": "terms", "terms": [{"term": a, "def": b} for a, b in terms]}
    if label: d["label"] = label
    return d
def MC(q, options, answer, why): return {"type": "mc", "q": q, "options": options, "answer": answer, "why": why}
def NUM(q, answer, why, tol=0.001, unit=None):
    d = {"type": "num", "q": q, "answer": answer, "why": why, "tol": tol}
    if unit: d["unit"] = unit
    return d
def save(course, lessons):
    out = os.path.join(ROOT, "data", "lessons", course); os.makedirs(out, exist_ok=True)
    for l in lessons:
        for q in l.get("practice", []):
            if q["type"] == "mc": assert 0 <= q["answer"] < len(q["options"]), l["id"]
        json.dump(l, open(os.path.join(out, l["id"] + ".json"), "w"), ensure_ascii=False, indent=1)
    print(course, [l["id"] for l in lessons])
