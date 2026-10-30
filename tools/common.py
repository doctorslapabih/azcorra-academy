import json, os
ROOT = os.path.join(os.path.dirname(__file__), "..")
def T(md): return {"type": "text", "md": md}
def N(label, md): return {"type": "note", "label": label, "md": md}
def E(title, problem, steps, answer): return {"type": "example", "title": title, "problem": problem, "steps": steps, "answer": answer}
def TERMS(terms, label=None):
    d = {"type": "terms", "terms": [{"term": a, "def": b} for a, b in terms]}
    if label: d["label"] = label
    return d
def _extra(d, level=None, hint=None, steps=None):
    # level="challenge" marks a harder question; hint is revealable before answering; steps show after answering.
    if level: d["level"] = level
    if hint: d["hint"] = hint
    if steps: d["steps"] = steps
    return d
def MC(q, options, answer, why, **kw): return _extra({"type": "mc", "q": q, "options": options, "answer": answer, "why": why}, **kw)
def NUM(q, answer, why, tol=0.001, unit=None, **kw):
    d = {"type": "num", "q": q, "answer": answer, "why": why, "tol": tol}
    if unit: d["unit"] = unit
    return _extra(d, **kw)
def TXT(q, answers, why, **kw):
    # Typed answer, checked case-insensitively against any of the accepted spellings.
    return _extra({"type": "text", "q": q, "answer": answers if isinstance(answers, list) else [answers], "why": why}, **kw)
def CHECK(q, options, answer, why):
    # An unscored "check yourself" question placed inside the reading.
    return {"type": "check", "q": q, "options": options, "answer": answer, "why": why}
def save(course, lessons):
    out = os.path.join(ROOT, "data", "lessons", course); os.makedirs(out, exist_ok=True)
    for l in lessons:
        for q in l.get("practice", []):
            if q["type"] == "mc":
                assert 0 <= q["answer"] < len(q["options"]), l["id"]
                assert len(set(q["options"])) == len(q["options"]), (l["id"], q["q"])
            if q["type"] == "text": assert q["answer"] and all(isinstance(a, str) for a in q["answer"]), l["id"]
            if q["type"] == "num": float(q["answer"])
            assert q.get("why"), (l["id"], q["q"])
            assert q.get("level") in (None, "challenge"), l["id"]
        for s in l.get("sections", []):
            if s["type"] == "check": assert 0 <= s["answer"] < len(s["options"]), l["id"]
        json.dump(l, open(os.path.join(out, l["id"] + ".json"), "w"), ensure_ascii=False, indent=1)
    print(course, [l["id"] for l in lessons])
