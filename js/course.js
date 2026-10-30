// Course catalog loading and the lesson reader (readings, worked examples, practice, personal notes).
import { esc, md, pct, renderMath, toast, shuffle } from "./ui.js";
import * as store from "./store.js";

let catalogCache = null;
export async function loadCatalog() {
  if (catalogCache) return catalogCache;
  const res = await fetch("data/courses/index.json");
  if (!res.ok) throw new Error("catalog");
  catalogCache = await res.json();
  return catalogCache;
}
export async function loadCourse(id) {
  const cat = await loadCatalog();
  const c = cat.find(x => x.id === id);
  if (!c) throw new Error("course");
  return c;
}

/* ---------- figures ---------- */
const FIGURES = {
  bell() {
    const W = 620, H = 230, L = 30, R = 590, B = 190, T = 20;
    const x = iq => L + ((iq - 40) / 120) * (R - L);
    const y = iq => { const z = (iq - 100) / 15; return B - Math.exp(-z * z / 2) * (B - T); };
    let d = "";
    for (let iq = 40; iq <= 160; iq += 1) d += (iq === 40 ? "M" : "L") + x(iq).toFixed(1) + " " + y(iq).toFixed(1) + " ";
    let band = `M${x(85)} ${B} `;
    for (let iq = 85; iq <= 115; iq++) band += `L${x(iq).toFixed(1)} ${y(iq).toFixed(1)} `;
    band += `L${x(115)} ${B} Z`;
    let band2 = `M${x(70)} ${B} `;
    for (let iq = 70; iq <= 130; iq++) band2 += `L${x(iq).toFixed(1)} ${y(iq).toFixed(1)} `;
    band2 += `L${x(130)} ${B} Z`;
    const ticks = [55, 70, 85, 100, 115, 130, 145].map(v => `<line class="axis" x1="${x(v)}" y1="${B}" x2="${x(v)}" y2="${B + 5}"/><text x="${x(v)}" y="${B + 18}" text-anchor="middle">${v}</text>`).join("");
    return `<svg class="bell" viewBox="0 0 ${W} ${H + 10}" role="img" aria-label="Bell curve of IQ scores: mean 100, standard deviation 15">
      <path class="band" d="${band2}" style="opacity:.06"/><path class="band" d="${band}"/>
      <path class="curve" d="${d}"/><line class="axis" x1="${L}" y1="${B}" x2="${R}" y2="${B}"/>${ticks}
      <text x="${x(100)}" y="${y(100) + 40}" text-anchor="middle">68% score 85–115</text>
      <text x="${x(100)}" y="${B - 12}" text-anchor="middle">95% score 70–130</text>
      <text x="${x(140)}" y="${y(140) - 10}" text-anchor="middle">130+ ≈ top 2%</text>
    </svg>`;
  }
};

/* ---------- sections ---------- */
function section(s, i) {
  const id = "s" + i;
  switch (s.type) {
    case "note": return `<div class="note-box" id="${id}"><span class="lbl">${esc(s.label || "Note")}</span>${md(s.md)}</div>`;
    case "example": return `<div class="example" id="${id}"><span class="lbl">Worked example${s.title ? " · " + esc(s.title) : ""}</span>${md(s.problem)}<ol>${(s.steps || []).map(x => "<li>" + md(x).replace(/^<p>|<\/p>$/g, "") + "</li>").join("")}</ol>${s.answer ? `<div class="ans">${md(s.answer).replace(/^<p>|<\/p>$/g, "")}</div>` : ""}</div>`;
    case "figure": return `<figure id="${id}" style="margin:0" class="stack">${FIGURES[s.key] ? FIGURES[s.key]() : s.svg || ""}${s.caption ? `<figcaption class="sub">${esc(s.caption)}</figcaption>` : ""}</figure>`;
    case "terms": return `<div class="note-box" id="${id}"><span class="lbl">${esc(s.label || "Key terms")}</span><dl style="margin:0;display:flex;flex-direction:column;gap:6px">${s.terms.map(t => `<div><dt style="font-weight:600;display:inline">${esc(t.term)}</dt> <dd style="display:inline;margin:0">— ${ins(t.def)}</dd></div>`).join("")}</dl></div>`;
    case "check": return `<div class="example check" id="${id}" data-checkbox="${i}"><span class="lbl">Check yourself</span><div class="prompt" style="font-size:19px">${ins(s.q)}</div><div class="choices">${s.options.map((o, k) => `<button class="choice" data-check="${i}" data-k="${k}"><span class="k">${"ABCDEF"[k]}</span><span>${ins(o)}</span></button>`).join("")}</div><div class="feedback" data-checkfb hidden></div></div>`;
    default: return `<div class="prose-block" id="${id}">${md(s.md)}</div>`;
  }
}

// Inline markdown: renders **bold**, *italic*, `code` and links without wrapping in a paragraph.
function ins(s) { return md(s).replace(/^<p>|<\/p>$/g, ""); }

function wireChecks(root, sections) {
  root.querySelectorAll("[data-check]").forEach(b => b.addEventListener("click", () => {
    const i = Number(b.dataset.check), k = Number(b.dataset.k), s = sections[i];
    const box = root.querySelector(`[data-checkbox="${i}"]`);
    if (!box || box.dataset.done) return;
    box.dataset.done = "1";
    box.querySelectorAll("[data-check]").forEach(c => {
      const ck = Number(c.dataset.k);
      c.disabled = true;
      c.classList.add(ck === s.answer ? "right" : ck === k ? "wrong" : "dim");
    });
    const fb = box.querySelector("[data-checkfb]");
    const good = k === s.answer;
    fb.className = "feedback " + (good ? "good" : "bad");
    fb.innerHTML = `<span class="verdict">${good ? "Right." : "Not quite."}</span>${md(s.why || "")}`;
    fb.hidden = false;
    renderMath(box);
  }));
}

/* ---------- lesson ---------- */
export function renderLesson(root, { course, lesson, back, backLabel }) {
  const key = (course ? course.id : "iq") + "/" + lesson.id;
  const rec = store.lesson(key) || {};
  const heads = [];
  (lesson.sections || []).forEach((s, i) => { const m = /^##\s+(.+)$/m.exec(s.md || ""); if (m) heads.push({ i, t: m[1] }); });
  let unitLabel = "";
  if (course) course.units.forEach((u, ui) => u.lessons.forEach((l, li) => { if (l.id === lesson.id) unitLabel = `Unit ${ui + 1} · ${u.title} · Lesson ${ui + 1}.${li + 1}`; }));

  root.innerHTML = `
  <div class="stack">
    <a class="sub" href="${esc(back)}">← ${esc(backLabel)}</a>
    <span class="eyebrow">${esc(course ? course.code + " · " + unitLabel : lesson.eyebrow || "Reading")}</span>
    <h1 class="title">${esc(lesson.title)}</h1>
    ${lesson.lede ? `<p class="lede">${esc(lesson.lede)}</p>` : ""}
    <p class="sub">${lesson.minutes ? "About " + lesson.minutes + " minutes" : ""}${lesson.band ? " · " + esc(lesson.band) : ""}${rec.complete ? ' · <span class="tag live">Mastered</span>' : ""}</p>
  </div>
  <div class="reader">
    <nav class="toc" aria-label="In this lesson">
      <span class="unit">In this lesson</span>
      ${heads.map(h => `<a href="#" data-jump="s${h.i}">${esc(h.t)}</a>`).join("")}
      ${lesson.practice && lesson.practice.length ? '<a href="#" data-jump="practice">Practice</a>' : ""}
      <a href="#" data-jump="notes">Your notes</a>
    </nav>
    <article class="prose">
      ${(lesson.sections || []).map(section).join("\n")}
      ${lesson.practice && lesson.practice.length ? `<h2 id="practice">Practice</h2><p class="sub">${lesson.practice.some(q => q.level === "challenge") ? "Core questions decide mastery: get 80% or better. Challenge questions are harder and test whether you can use the idea somewhere new." : "Get 80% or better to master this lesson."} Answers are checked one at a time.</p><div class="stack" data-practice></div><div data-summary></div>` : ""}
      <h2 id="notes">Your notes</h2>
      <p class="sub">Write what you'd tell someone else about this lesson. It saves on this device and goes into your journal.</p>
      <textarea id="mynotes" class="paste" style="min-height:140px;font-family:var(--font-read);font-size:16px" placeholder="In my own words…">${esc(rec.myNotes || "")}</textarea>
      ${lesson.practice && lesson.practice.length ? "" : `<div class="row"><button class="btn" data-read>Mark as read</button></div>`}
      ${lesson.sources && lesson.sources.length ? `<div class="sources"><b>Sources</b>${lesson.sources.map(s => `<a href="${esc(s.url)}" target="_blank" rel="noopener">${esc(s.title)}</a>`).join("")}</div>` : ""}
    </article>
  </div>`;

  root.querySelectorAll("[data-jump]").forEach(a => a.addEventListener("click", e => {
    e.preventDefault();
    const el = document.getElementById(a.dataset.jump);
    if (el) window.scrollTo({ top: el.getBoundingClientRect().top + window.scrollY - 80, behavior: "smooth" });
  }));

  const notes = root.querySelector("#mynotes");
  let t;
  notes.addEventListener("input", () => { clearTimeout(t); t = setTimeout(() => store.lesson(key, { myNotes: notes.value }), 400); });

  const meta = { course: course ? course.id : "iq", lesson: lesson.id, title: lesson.title, courseTitle: course ? course.title : "IQ Lab" };
  const readBtn = root.querySelector("[data-read]");
  if (readBtn) readBtn.addEventListener("click", () => {
    store.lesson(key, { complete: true, myNotes: notes.value });
    store.addSession(Object.assign({ kind: "lesson", score: 0, max: 0, myNotes: notes.value.trim() || undefined, notes: [] }, meta));
    toast("Saved to your journal.");
    readBtn.disabled = true; readBtn.textContent = "Read";
  });

  wireChecks(root, lesson.sections || []);
  if (lesson.practice && lesson.practice.length) practice(root, lesson, key, meta, notes);
  renderMath(root);
}

function practice(root, lesson, key, meta, notesEl) {
  const host = root.querySelector("[data-practice]");
  const summary = root.querySelector("[data-summary]");
  const qs = lesson.practice;
  const answers = new Array(qs.length).fill(null);
  const hints = new Array(qs.length).fill(false);
  const L = "ABCDEF";
  const isChal = q => q.level === "challenge";
  // Multiple-choice options are shuffled every attempt, so the answer's position never gives it away.
  let orders = [];
  const shuffleAll = () => { orders = qs.map(q => q.type === "mc" ? shuffle(q.options.map((_, k) => k)) : null); };
  shuffleAll();
  const norm = v => String(v).toLowerCase().replace(/[’']/g, "'").replace(/[^a-z0-9' -]/g, "").replace(/\s+/g, " ").trim();
  const textAnswers = q => (Array.isArray(q.answer) ? q.answer : [q.answer]);
  const answerText = q => q.type === "mc" ? q.options[q.answer] : q.type === "text" ? textAnswers(q)[0] : String(q.answer) + (q.unit ? " " + q.unit : "");
  const coreCount = qs.filter(q => !isChal(q)).length;
  let coreN = 0, chalN = 0;
  const label = q => isChal(q) ? `Challenge ${++chalN}` : `Question ${++coreN} of ${coreCount}`;

  const draw = () => {
    coreN = 0; chalN = 0;
    host.innerHTML = qs.map((q, i) => {
      const a = answers[i], done = a != null;
      const good = done && a.good;
      let body;
      if (q.type === "num" || q.type === "text") {
        body = `<form class="row" data-num="${i}" autocomplete="off"><input class="input" id="pq${i}" ${q.type === "num" ? 'inputmode="decimal"' : 'autocapitalize="off" spellcheck="false"'} ${done ? "disabled" : ""} value="${done ? esc(a.value) : ""}" aria-label="Answer to question ${i + 1}">${q.unit ? `<span class="sub">${esc(q.unit)}</span>` : ""}${done ? "" : '<button class="btn ghost" type="submit">Check</button>'}</form>`;
      } else {
        body = `<div class="choices">${orders[i].map((orig, k) => `<button class="choice ${done ? (orig === q.answer ? "right" : orig === a.value ? "wrong" : "dim") : ""}" data-mc="${i}" data-k="${orig}" ${done ? "disabled" : ""}><span class="k">${L[k]}</span><span>${ins(q.options[orig])}</span></button>`).join("")}</div>`;
      }
      const hint = q.hint && !done ? (hints[i] ? `<div class="hint"><b>Hint</b> ${ins(q.hint)}</div>` : `<div><button class="btn ghost small" data-hint="${i}">Show hint</button></div>`) : "";
      const steps = q.steps && q.steps.length ? `<ol class="steps">${q.steps.map(x => "<li>" + ins(x) + "</li>").join("")}</ol>` : "";
      const fb = done ? `<div class="feedback ${good ? "good" : "bad"}"><span class="verdict">${good ? "Correct." : "Not quite."}</span>${!good && q.type !== "mc" ? `<p>Answer: <strong>${esc(answerText(q))}</strong></p>` : ""}${q.why ? md(q.why) : ""}${steps}</div>` : "";
      return `<div class="example${isChal(q) ? " challenge" : ""}" id="q${i}"><span class="lbl">${label(q)}</span><div class="prompt" style="font-size:19px">${ins(q.q)}</div>${body}${hint}${fb}</div>`;
    }).join("");
    host.querySelectorAll("[data-mc]").forEach(b => b.addEventListener("click", () => {
      const i = Number(b.dataset.mc), k = Number(b.dataset.k);
      if (answers[i]) return;
      answers[i] = { value: k, good: k === qs[i].answer };
      after(i);
    }));
    host.querySelectorAll("[data-hint]").forEach(b => b.addEventListener("click", () => { hints[Number(b.dataset.hint)] = true; draw(); }));
    host.querySelectorAll("[data-num]").forEach(f => f.addEventListener("submit", e => {
      e.preventDefault();
      const i = Number(f.dataset.num), q = qs[i];
      const raw = f.querySelector("input").value.trim();
      if (!raw) return;
      if (q.type === "text") {
        answers[i] = { value: raw, good: textAnswers(q).some(t => norm(t) === norm(raw)) };
      } else {
        const v = Number(raw.replace(/[−–]/g, "-").replace(/[,$%\s]/g, "").replace(/^\((.*)\)$/, "-$1"));
        const tol = q.tol != null ? q.tol : 1e-6;
        answers[i] = { value: raw, good: Number.isFinite(v) && Math.abs(v - Number(q.answer)) <= tol };
      }
      after(i);
    }));
    renderMath(host);
  };

  const after = i => {
    draw();
    const nextQ = document.getElementById("q" + (i + 1));
    if (answers.every(Boolean)) finishPractice();
    else if (nextQ) nextQ.scrollIntoView({ behavior: "smooth", block: "nearest" });
  };

  const finishPractice = () => {
    const idx = qs.map((_, i) => i);
    const core = idx.filter(i => !isChal(qs[i])), chal = idx.filter(i => isChal(qs[i]));
    const coreBase = core.length ? core : idx;
    const coreScore = coreBase.filter(i => answers[i].good).length;
    const chalScore = chal.filter(i => answers[i].good).length;
    const score = answers.filter(a => a.good).length;
    const p = pct(coreScore, coreBase.length);
    const prev = store.lesson(key) || {};
    const complete = p >= 80 || !!prev.complete;
    store.lesson(key, { best: Math.max(prev.best || 0, p), complete, myNotes: notesEl.value, challenge: Math.max(prev.challenge || 0, chalScore) });
    const missed = qs.map((q, i) => ({ q, a: answers[i] })).filter(x => !x.a.good)
      .map(x => `${x.q.q.replace(/\*\*/g, "")} → ${answerText(x.q)} (you: ${x.q.type === "mc" ? x.q.options[x.a.value] : x.a.value})`);
    store.addSession(Object.assign({ kind: "lesson", score, max: qs.length, norm: p, metric: `${p}%${chal.length ? ` · challenge ${chalScore}/${chal.length}` : ""}`, notes: missed, myNotes: notesEl.value.trim() || undefined }, meta));
    const chalLine = chal.length ? `<p>Challenge: <strong>${chalScore}/${chal.length}</strong>${chalScore === chal.length ? " · every one. That's real understanding." : chalScore ? ". Reread the explanations on the ones you missed." : ". These are meant to stretch you. Read each explanation, then retry."}</p>` : "";
    summary.innerHTML = `<div class="note-box"><span class="lbl">Result</span><p style="font-family:var(--font-display);font-size:30px;font-weight:600">${coreScore}/${coreBase.length} · ${p}%</p><p>${p >= 80 ? "Mastered. It's in your journal." : "Below 80%. Reread the parts you missed, then try the practice again."}</p>${chalLine}<div class="row"><button class="btn ghost" data-retry>Retry practice</button></div></div>`;
    summary.querySelector("[data-retry]").addEventListener("click", () => { answers.fill(null); hints.fill(false); shuffleAll(); summary.innerHTML = ""; draw(); document.getElementById("practice").scrollIntoView({ behavior: "smooth" }); });
  };
  draw();
}
