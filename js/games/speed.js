// Symbol Search — 60 seconds. Is either target symbol in the search group? Score = correct − wrong.
import { pick, shuffle } from "../ui.js";
import { intro, finish, topLine, keys, clamp } from "./common.js";

const SYMBOLS = ["⊕", "⊗", "⊘", "△", "▽", "◇", "◆", "□", "■", "○", "●", "∩", "∪", "⊂", "⊃", "≡", "≈", "∆", "∇", "∞", "§", "¶", "‡", "†", "Ω", "Ψ", "λ", "Σ", "Φ", "#"];
const SECONDS = 60;

export const meta = {
  id: "speed", title: "Symbol Search", ability: "gs", abilityName: "Processing speed",
  blurb: "60 seconds. Spot whether a target symbol appears in a row. Speed and accuracy both count.", minutes: 2
};

export function mount(root) {
  intro(root, meta, `
    <p>On the left are two <strong>target</strong> symbols. On the right is a group of five. Does <em>either</em> target appear in the group?</p>
    <p>Press <strong>→ or J</strong> for <strong>Yes</strong>, <strong>← or F</strong> for <strong>No</strong>. You have ${SECONDS} seconds. Your score is correct answers minus wrong ones, so guessing doesn't pay.</p>
    <p>Method: memorize both targets as a pair, then sweep the group once left to right. Don't double-check: trust the first sweep.</p>`, () => play(root));
}

function item() {
  const pool = shuffle(SYMBOLS);
  const targets = pool.slice(0, 2);
  const yes = Math.random() < 0.5;
  const group = pool.slice(2, yes ? 6 : 7);
  if (yes) group.splice(Math.floor(Math.random() * 5), 0, pick(targets));
  return { targets, group, yes };
}

function play(root) {
  let correct = 0, wrong = 0, cur = item(), left = SECONDS, alive = true, started = performance.now();
  root.innerHTML = `
    <div class="stage">
      ${topLine(meta, "Is a target in the group?", '<span class="timer" data-t></span>')}
      <div class="sym-row" data-row></div>
      <div class="actions" style="justify-content:center;gap:14px">
        <button class="btn ghost" data-ans="no" style="min-width:140px">← No</button>
        <button class="btn" data-ans="yes" style="min-width:140px">Yes →</button>
      </div>
      <p class="hint" style="text-align:center"><span class="mono" data-score>0</span> correct · <span class="mono" data-wrong>0</span> wrong</p>
    </div>`;
  const row = root.querySelector("[data-row]");
  const tEl = root.querySelector("[data-t]");
  const sEl = root.querySelector("[data-score]");
  const wEl = root.querySelector("[data-wrong]");
  const draw = () => {
    row.innerHTML = `<div class="sym-box target" aria-label="Targets">${cur.targets.map(s => `<span>${s}</span>`).join("")}</div><div class="sym-box" aria-label="Group">${cur.group.map(s => `<span>${s}</span>`).join("")}</div>`;
  };
  const answer = yes => {
    if (!alive) return;
    if (yes === cur.yes) correct++; else wrong++;
    sEl.textContent = correct; wEl.textContent = wrong;
    cur = item(); draw();
  };
  root.querySelectorAll("[data-ans]").forEach(b => b.addEventListener("click", () => answer(b.dataset.ans === "yes")));
  const off = keys(e => {
    if (e.key === "ArrowRight" || e.key === "j" || e.key === "J") { e.preventDefault(); answer(true); }
    else if (e.key === "ArrowLeft" || e.key === "f" || e.key === "F") { e.preventDefault(); answer(false); }
  });
  draw();
  const tick = () => {
    if (!alive) return;
    left = Math.max(0, SECONDS - Math.floor((performance.now() - started) / 1000));
    tEl.textContent = `0:${String(left).padStart(2, "0")}`;
    if (left <= 0) return end();
    setTimeout(tick, 200);
  };
  window.addEventListener("hashchange", () => { alive = false; off(); }, { once: true });
  tick();

  function end() {
    alive = false; off();
    const net = correct - wrong;
    const acc = correct + wrong ? Math.round((correct / (correct + wrong)) * 100) : 0;
    finish(root, meta, {
      score: Math.max(0, net), max: 0, big: String(net), bigLabel: "net score", level: 0, newLevel: 0,
      norm: Math.round(clamp((net / 45) * 100)),
      metric: `${correct} right, ${wrong} wrong, ${acc}% accurate`, headline: `${net} net in ${SECONDS} seconds.`,
      summary: `${correct} right, ${wrong} wrong (${acc}% accurate). Speed builds with reps. If accuracy dips under 90%, slow down a notch.`,
      review: []
    }, () => play(root));
  }
}
