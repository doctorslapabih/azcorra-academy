// Number Series — generated sequences across five difficulty levels. Type the next term.
import { esc, rand, pick } from "../ui.js";
import { intro, finish, topLine, pips, keys, levelNorm, nextLevel } from "./common.js";
import * as store from "../store.js";

const MAX = 5, TOTAL = 10;
const PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47];

// Each generator returns { seq: [...shown terms], next, why, trick }
const GEN = {
  1: [
    () => { const a = rand(1, 20), d = rand(2, 9); const s = Array.from({ length: 6 }, (_, i) => a + i * d); return { seq: s.slice(0, 5), next: s[5], why: `Add ${d} each time.`, trick: "Check the gaps first." }; },
    () => { const a = rand(60, 120), d = rand(3, 9); const s = Array.from({ length: 6 }, (_, i) => a - i * d); return { seq: s.slice(0, 5), next: s[5], why: `Subtract ${d} each time.`, trick: "Gaps can be negative." }; },
    () => { const a = rand(1, 4), r = pick([2, 3]); const s = Array.from({ length: 6 }, (_, i) => a * r ** i); return { seq: s.slice(0, 5), next: s[5], why: `Multiply by ${r} each time.`, trick: "Gaps growing fast? Check the ratio." }; }
  ],
  2: [
    () => { const o = rand(1, 4); const s = Array.from({ length: 6 }, (_, i) => (i + o) ** 2); return { seq: s.slice(0, 5), next: s[5], why: `Square numbers: ${o}², ${o + 1}², ${o + 2}²…`, trick: "Know your squares up to 20²." }; },
    () => { const a = rand(2, 9), up = rand(4, 9), down = rand(1, up - 1); const s = [a]; for (let i = 1; i < 7; i++) s.push(s[i - 1] + (i % 2 ? up : -down)); return { seq: s.slice(0, 6), next: s[6], why: `Alternates: +${up}, −${down}, +${up}, −${down}…`, trick: "If gaps zig-zag, there are two rules taking turns." }; },
    () => { const a = rand(1, 10), d0 = rand(1, 3), dd = rand(1, 3); const s = [a]; for (let i = 0; i < 5; i++) s.push(s[i] + d0 + i * dd); return { seq: s.slice(0, 5), next: s[5], why: `The gaps grow by ${dd}: +${d0}, +${d0 + dd}, +${d0 + 2 * dd}…`, trick: "Gaps of the gaps (second differences)." }; },
    () => { const s = [1, 3, 6, 10, 15, 21, 28, 36]; const o = rand(0, 2); return { seq: s.slice(o, o + 5), next: s[o + 5], why: "Triangular numbers: add 2, then 3, then 4…", trick: "Gaps that count up by one." }; }
  ],
  3: [
    () => { const m = pick([2, 3]), c = pick([-1, 1, 2]), a = rand(2, 5); const s = [a]; for (let i = 0; i < 5; i++) s.push(s[i] * m + c); return { seq: s.slice(0, 5), next: s[5], why: `Each term is the last ×${m} ${c < 0 ? "− " + -c : "+ " + c}.`, trick: "If ratios are almost constant, try ×k ± c." }; },
    () => { const a = rand(1, 5), b = rand(1, 5); const s = [a, b]; for (let i = 2; i < 8; i++) s.push(s[i - 1] + s[i - 2]); return { seq: s.slice(0, 6), next: s[6], why: "Each term is the sum of the two before it.", trick: "Fibonacci-style: look back two terms." }; },
    () => { const a = rand(1, 9), d = rand(2, 6), b = rand(20, 40), e = rand(2, 5); const s = []; for (let i = 0; i < 4; i++) { s.push(a + i * d); s.push(b - i * e); } return { seq: s.slice(0, 7), next: s[7], why: `Two sequences interleaved: ${a}, ${a + d}, ${a + 2 * d}… and ${b}, ${b - e}, ${b - 2 * e}…`, trick: "Read every other term." }; },
    () => { const a = rand(1, 3); const s = [a]; for (let i = 0; i < 5; i++) s.push(s[i] * (i + 2)); return { seq: s.slice(0, 5), next: s[5], why: "Multiply by 2, then 3, then 4, then 5…", trick: "Ratios that count up." }; }
  ],
  4: [
    () => { const o = rand(1, 3); const s = Array.from({ length: 6 }, (_, i) => (i + o) ** 3); return { seq: s.slice(0, 5), next: s[5], why: "Cube numbers: n × n × n.", trick: "Know cubes: 1, 8, 27, 64, 125, 216, 343." }; },
    () => { const o = rand(0, 4), k = pick([1, 2, 3]); const s = PRIMES.slice(o, o + 6).map(p => p * k); return { seq: s.slice(0, 5), next: s[5], why: k === 1 ? "Prime numbers." : `Prime numbers times ${k}.`, trick: "Random-looking gaps? Divide out a common factor and look for primes." }; },
    () => { const o = rand(1, 4), c = pick([1, -1, 2]); const s = Array.from({ length: 6 }, (_, i) => (i + o) ** 2 + c); return { seq: s.slice(0, 5), next: s[5], why: `Squares ${c > 0 ? "plus " + c : "minus " + -c}: ${o}²${c > 0 ? "+" : "−"}${Math.abs(c)}, ${o + 1}²${c > 0 ? "+" : "−"}${Math.abs(c)}…`, trick: "Near-squares: compare each term to the nearest square." }; },
    () => { const s = [1, 4, 27, 256, 3125]; return { seq: s.slice(0, 4), next: s[4], why: "n to the power n: 1¹, 2², 3³, 4⁴, 5⁵.", trick: "Explosive growth means powers." }; }
  ],
  5: [
    () => { const a = rand(2, 5), m = pick([2, 3]), p = rand(2, 6); const s = [a]; for (let i = 1; i < 7; i++) s.push(i % 2 ? s[i - 1] * m : s[i - 1] + p); return { seq: s.slice(0, 6), next: s[6], why: `Alternates ×${m} and +${p}.`, trick: "Two operations taking turns." }; },
    () => { const a = rand(1, 10); const s = [a]; for (let i = 1; i < 7; i++) s.push(s[i - 1] + i * i); return { seq: s.slice(0, 6), next: s[6], why: "The gaps are square numbers: +1, +4, +9, +16…", trick: "Look at the gaps, then name what the gaps are." }; },
    () => { const a = rand(2, 4), b = rand(2, 4); const s = [a, b]; for (let i = 2; i < 7; i++) s.push(s[i - 1] * s[i - 2]); if (s[5] > 99999) return GEN[5][0](); return { seq: s.slice(0, 5), next: s[5], why: "Each term is the product of the two before it.", trick: "Fibonacci, but multiplying." }; },
    () => { const a = rand(4, 9); const s = [a]; for (let i = 1; i < 7; i++) s.push(i % 2 ? s[i - 1] * 2 : s[i - 1] - 3); return { seq: s.slice(0, 6), next: s[6], why: "Alternates ×2 and −3.", trick: "Two operations taking turns." }; },
    () => { const s = [2, 3, 5, 9, 17, 33, 65, 129]; const o = rand(0, 2); return { seq: s.slice(o, o + 5), next: s[o + 5], why: "Double the last term, minus 1 (or: gaps double: +1, +2, +4, +8…).", trick: "Two ways to see one rule. Either works." }; }
  ]
};

export const meta = {
  id: "series", title: "Number Series", ability: "gq", abilityName: "Quantitative reasoning",
  blurb: "Spot the rule driving a sequence and type the next number.", minutes: 6
};

export function mount(root) {
  intro(root, meta, `
    <p>Type the next number. No multiple choice here: you have to actually find the rule.</p>
    <p>Method, in order: <strong>1.</strong> check the gaps. <strong>2.</strong> if gaps grow fast, check ratios. <strong>3.</strong> check the gaps of the gaps. <strong>4.</strong> try every other term. <strong>5.</strong> compare to squares, cubes and primes.</p>
    <p>Ten sequences, adaptive, currently <strong>level ${store.level("series")} of ${MAX}</strong>.</p>`, () => play(root));
}

function play(root) {
  const level = store.level("series");
  const pool = GEN[level].concat(level > 1 ? GEN[level - 1].slice(0, 1) : []);
  const items = [];
  const used = new Set();
  let tries = 0;
  while (items.length < TOTAL) {
    const it = pick(pool)();
    const k = it.seq.join(",");
    if (!used.has(k) || ++tries > 200) { used.add(k); items.push(it); }
  }
  const results = [], review = [];
  let i = 0, off = null;

  const show = () => {
    const it = items[i];
    let answered = null;
    const render = () => {
      const done = answered != null, good = done && answered === it.next;
      root.innerHTML = `
      <div class="stage">
        ${topLine(meta, `Level ${level} · ${i + 1} of ${TOTAL}`, pips(TOTAL, results, i))}
        <div class="big-seq" aria-label="Sequence">${it.seq.join(", ")}, <span style="color:var(--accent)">?</span></div>
        <form class="row" data-form autocomplete="off">
          <label class="sub" for="ans">Next term</label>
          <input id="ans" class="input" inputmode="numeric" ${done ? "disabled" : ""} value="${done ? esc(answered) : ""}" aria-label="Your answer">
          ${done ? "" : '<button class="btn" type="submit">Check</button>'}
        </form>
        ${done ? `<div class="feedback ${good ? "good" : "bad"}" role="status"><span class="verdict">${good ? "Correct." : "The answer is " + it.next + "."}</span><p>${esc(it.why)}</p><p class="why"><b>Method</b>${esc(it.trick)}</p></div>` : ""}
        <div class="actions"><span class="hint">${done ? "Enter to continue" : "Type a number and press Enter"}</span>${done ? `<button class="btn" data-next>${i === TOTAL - 1 ? "See results" : "Next"}</button>` : ""}</div>
      </div>`;
      const form = root.querySelector("[data-form]");
      form.addEventListener("submit", e => {
        e.preventDefault();
        if (done) return;
        const v = root.querySelector("#ans").value.replace(/[,\s]/g, "");
        if (!/^-?\d+$/.test(v)) { root.querySelector("#ans").focus(); return; }
        answered = Number(v);
        results[i] = answered === it.next;
        if (!results[i]) review.push({ q: it.seq.join(", ") + ", ?", your: String(answered), right: String(it.next), why: it.why });
        render();
      });
      if (done) { const n = root.querySelector("[data-next]"); n.addEventListener("click", next); n.focus(); }
      else root.querySelector("#ans").focus();
    };
    const next = () => { if (i < TOTAL - 1) { i++; show(); } else end(); };
    if (off) off();
    off = keys(e => { if (e.key === "Enter" && answered != null && e.target.tagName !== "INPUT") { e.preventDefault(); next(); } });
    render();
  };

  const end = () => {
    if (off) off();
    const score = results.filter(Boolean).length, acc = Math.round((score / TOTAL) * 100);
    const nl = nextLevel(level, acc, MAX);
    store.level("series", nl);
    finish(root, meta, { score, max: TOTAL, level, newLevel: nl, norm: levelNorm(level, MAX, acc), metric: `level ${level}`, summary: `Level ${level}. Work the method in order every time and it becomes automatic.`, review }, () => play(root));
  };
  show();
}
