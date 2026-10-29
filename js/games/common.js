// Shared pieces for IQ Lab games: header, results screen, level logic.
import { esc, pct } from "../ui.js";
import * as store from "../store.js";

export const clamp = (v, a = 0, b = 100) => Math.max(a, Math.min(b, v));

export function levelNorm(level, maxLevel, accuracy) {
  return Math.round(clamp(((level - 1) / (maxLevel - 1)) * 50 + accuracy / 2));
}

export function nextLevel(level, accuracy, maxLevel, up = 80, down = 50) {
  if (accuracy >= up) return Math.min(maxLevel, level + 1);
  if (accuracy < down) return Math.max(1, level - 1);
  return level;
}

export function pips(total, results, current) {
  let h = '<div class="pips" aria-hidden="true">';
  for (let i = 0; i < total; i++) {
    const r = results[i];
    h += `<i class="${r === true ? "ok" : r === false ? "no" : i === current ? "cur" : ""}"></i>`;
  }
  return h + "</div>";
}

export function topLine(meta, left, right) {
  return `<div class="stage-top"><span><b>${esc(meta.title)}</b> · ${esc(left)}</span>${right || ""}</div>`;
}

/**
 * Records the session and renders the results screen.
 * r: { score, max, norm, level, newLevel, metric, summary, review:[{q, your, right, why}] }
 */
export function finish(root, meta, r, replay) {
  const rec = store.addSession({
    kind: "iq", game: meta.id, title: meta.title, ability: meta.ability,
    score: r.score, max: r.max, norm: r.norm, level: r.level, metric: r.metric || "",
    notes: (r.review || []).slice(0, 8).map(x => `${x.q} → answer ${x.right}${x.your != null ? " (you: " + x.your + ")" : ""}`),
    logged: false
  });
  const lvlMsg = r.newLevel > r.level ? `Level up: next time you start at level ${r.newLevel}.`
    : r.newLevel < r.level ? `Dropping to level ${r.newLevel} next time to rebuild accuracy.`
    : r.level ? `You'll stay at level ${r.level} next time.` : "";
  const big = r.big != null ? r.big : `${r.score}/${r.max}`;
  root.innerHTML = `
  <div class="stage">
    ${topLine(meta, "Results")}
    <div class="result">
      <div class="seal"><div><b>${esc(big)}</b><span>${esc(r.bigLabel || (r.max ? pct(r.score, r.max) + "%" : ""))}</span></div></div>
      <div class="stack">
        <h2 class="h2">${esc(r.headline || headline(r.max ? pct(r.score, r.max) : r.norm))}</h2>
        <p class="lede" style="font-size:17px">${esc(r.summary || "")}</p>
        <p class="sub">Practice index <span class="mono">${r.norm}</span>/100 · ${esc(lvlMsg)}</p>
      </div>
    </div>
    ${r.review && r.review.length ? `<div class="review"><span class="eyebrow">Review</span>${r.review.map(x => `
      <div class="item"><span>${esc(x.q)}</span><span class="a">${x.your != null ? "You said " + esc(x.your) + " · " : ""}Answer <b>${esc(x.right)}</b></span>${x.why ? `<span class="a">${esc(x.why)}</span>` : ""}</div>`).join("")}</div>` : ""}
    <div class="actions">
      <a class="btn ghost" href="#/lab">Back to the Lab</a>
      <button class="btn" data-replay>Go again</button>
    </div>
  </div>`;
  root.querySelector("[data-replay]").addEventListener("click", replay);
  return rec;
}

function headline(p) {
  if (p >= 95) return "Flawless.";
  if (p >= 80) return "Sharp work.";
  if (p >= 60) return "Solid. Study the misses.";
  return "Good reps. This is where you grow.";
}

export function intro(root, meta, body, start) {
  root.innerHTML = `
  <div class="stage">
    ${topLine(meta, meta.abilityName)}
    <div class="stack" style="max-width:62ch">
      <span class="eyebrow">${esc(meta.abilityName)}</span>
      <h2 class="title" style="font-size:clamp(32px,5vw,46px)">${esc(meta.title)}</h2>
      <div class="prose" style="font-size:17px">${body}</div>
    </div>
    <div class="actions"><a class="btn ghost" href="#/lab">Back</a><button class="btn" data-start>Begin</button></div>
  </div>`;
  const b = root.querySelector("[data-start]");
  b.addEventListener("click", start);
  b.focus();
}

// Keyboard helper scoped to the current game; removed automatically on route change.
export function keys(handler) {
  const fn = e => { if (e.metaKey || e.ctrlKey || e.altKey) return; if (e.target && /INPUT|TEXTAREA/.test(e.target.tagName) && e.key !== "Enter") return; handler(e); };
  document.addEventListener("keydown", fn);
  const off = () => document.removeEventListener("keydown", fn);
  window.addEventListener("hashchange", off, { once: true });
  return off;
}

// Shared multiple-choice runner for banked items (analogies, logic).
export function runChoiceSession(root, meta, items, opts = {}) {
  const results = [], review = [];
  let i = 0, off = null;
  const L = "ABCD";
  const show = () => {
    const it = items[i];
    const order = it._order || (it._order = it.options.map((_, k) => k).sort(() => Math.random() - 0.5));
    let picked = null;
    const render = () => {
      const done = picked != null, good = picked === it.answer;
      root.innerHTML = `
      <div class="stage">
        ${topLine(meta, `Question ${i + 1} of ${items.length}`, pips(items.length, results, i))}
        <div class="prompt">${esc(it.q)}</div>
        <div class="choices">${order.map((k, pos) => `<button class="choice ${done ? (k === it.answer ? "right" : k === picked ? "wrong" : "dim") : ""}" data-k="${k}" ${done ? "disabled" : ""}><span class="k">${L[pos]}</span><span>${esc(it.options[k])}</span></button>`).join("")}</div>
        ${done ? `<div class="feedback ${good ? "good" : "bad"}" role="status"><span class="verdict">${good ? "Correct." : "Not quite."}</span><p>${esc(it.why)}</p>${it.trick ? `<p class="why"><b>Method</b>${esc(it.trick)}</p>` : ""}</div>` : ""}
        <div class="actions"><span class="hint">${done ? "Enter to continue" : "Choose, or press A–D"}</span><button class="btn" data-next ${done ? "" : "disabled"}>${i === items.length - 1 ? "See results" : "Next"}</button></div>
      </div>`;
      root.querySelectorAll("[data-k]").forEach(b => b.addEventListener("click", () => choose(Number(b.dataset.k))));
      root.querySelector("[data-next]").addEventListener("click", next);
      if (done) root.querySelector("[data-next]").focus();
    };
    const choose = k => {
      if (picked != null) return;
      picked = k;
      const good = k === it.answer;
      results[i] = good;
      if (!good) review.push({ q: it.q, your: it.options[k], right: it.options[it.answer], why: it.trick || it.why });
      render();
    };
    const next = () => {
      if (picked == null) return;
      if (i < items.length - 1) { i++; show(); } else done();
    };
    if (off) off();
    off = keys(e => {
      const idx = "abcd".indexOf(e.key.toLowerCase());
      if (idx >= 0 && picked == null && idx < order.length) choose(order[idx]);
      else if (e.key === "Enter" && picked != null) { e.preventDefault(); next(); }
    });
    render();
  };
  const done = () => {
    if (off) off();
    const score = results.filter(Boolean).length;
    opts.onDone(score, review);
  };
  show();
}
