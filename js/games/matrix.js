// Matrix Reasoning — procedurally generated 3×3 matrices in the style of Raven's Progressive Matrices.
import { esc, pick, shuffle } from "../ui.js";
import { intro, finish, topLine, pips, keys, levelNorm, nextLevel } from "./common.js";
import * as store from "../store.js";

const MAX = 6, TOTAL = 10;
const SHAPES = ["circle", "square", "triangle", "diamond", "pentagon", "star"];
const FILLS = ["outline", "striped", "solid"];
const SIZES = ["small", "medium", "large"];
const DOMAIN = { shape: [0, 1, 2, 3, 4, 5], count: [1, 2, 3], fill: [0, 1, 2], size: [0, 1, 2] };
const ATTRS = ["shape", "count", "fill", "size"];
const ORDERED = { count: true, fill: true, size: true };
const NOUN = { shape: "shapes", count: "counts", fill: "fills", size: "sizes" };

let uid = 0;

function grid(attr, rule, level) {
  const g = [[], [], []];
  const dom = DOMAIN[attr];
  if (rule === "fixed") { const v = pick(dom); for (let r = 0; r < 3; r++) for (let c = 0; c < 3; c++) g[r][c] = v; }
  else if (rule === "const") { const vals = shuffle(dom).slice(0, 3); for (let r = 0; r < 3; r++) for (let c = 0; c < 3; c++) g[r][c] = vals[r]; }
  else if (rule === "prog") {
    const desc = level >= 5 && Math.random() < 0.5;
    const seq = desc ? dom.slice().reverse() : dom.slice();
    for (let r = 0; r < 3; r++) for (let c = 0; c < 3; c++) g[r][c] = seq[c];
    g.desc = desc;
  } else { // dist: Latin square
    const vals = shuffle(dom).slice(0, 3), shift = pick([1, 2]);
    for (let r = 0; r < 3; r++) for (let c = 0; c < 3; c++) g[r][c] = vals[(c + r * shift) % 3];
  }
  return g;
}

function makeItem(level) {
  const varying = Math.min(4, level <= 1 ? 1 : level === 2 ? 2 : level <= 4 ? 3 : 4);
  const chosen = shuffle(ATTRS).slice(0, varying);
  const rules = {}, grids = {};
  ATTRS.forEach(a => {
    if (!chosen.includes(a)) rules[a] = "fixed";
    else {
      const opts = ["dist"];
      if (ORDERED[a]) opts.push("prog");
      if (level >= 4) opts.push("const");
      rules[a] = pick(opts);
    }
  });
  // keep the puzzle readable: a progression on count with large size gets crowded, so let size vary freely but cap density visually.
  ATTRS.forEach(a => { grids[a] = grid(a, rules[a], level); });
  const cell = (r, c) => ({ shape: grids.shape[r][c], count: grids.count[r][c], fill: grids.fill[r][c], size: grids.size[r][c] });
  const cells = [];
  for (let r = 0; r < 3; r++) for (let c = 0; c < 3; c++) cells.push(cell(r, c));
  const answer = cells[8];
  const key = o => `${o.shape}-${o.count}-${o.fill}-${o.size}`;
  const seen = new Set([key(answer)]);
  const options = [answer];
  const add = o => { const k = key(o); if (!seen.has(k)) { seen.add(k); options.push(o); } };
  if (level >= 3) { add(cells[7]); add(cells[5]); }
  let guard = 0;
  while (options.length < 8 && guard++ < 400) {
    const o = Object.assign({}, answer);
    const n = level >= 4 ? 1 : pick([1, 1, 2]);
    shuffle(ATTRS).slice(0, n).forEach(a => {
      const choices = DOMAIN[a].filter(v => v !== o[a]);
      // prefer values that appear somewhere in the matrix so distractors look plausible
      const inMatrix = choices.filter(v => cells.some(cc => cc[a] === v));
      o[a] = pick(inMatrix.length && Math.random() < 0.75 ? inMatrix : choices);
    });
    add(o);
  }
  return { cells, answer, options: shuffle(options), rules, grids };
}

function describe(o) {
  const n = o.count;
  const shape = SHAPES[o.shape] + (n > 1 ? "s" : "");
  return `${n} ${SIZES[o.size]} ${FILLS[o.fill]} ${shape}`;
}

function explain(item) {
  const lines = [];
  ATTRS.forEach(a => {
    const r = item.rules[a];
    if (r === "const") lines.push(`${cap(a)} stays the same across each row, and each row has its own.`);
    if (r === "prog") lines.push(`${cap(a)} ${item.grids[a].desc ? "drops" : "climbs"} one step across every row.`);
    if (r === "dist") lines.push(`Every row uses each of three ${NOUN[a]} exactly once.`);
  });
  const fixed = ATTRS.filter(a => item.rules[a] === "fixed");
  if (fixed.length) lines.push(`${fixed.map(cap).join(", ")} never change${fixed.length === 1 ? "s" : ""}.`);
  return { rule: lines.join(" "), answer: `The missing cell is ${describe(item.answer)}.` };
}
const cap = s => s[0].toUpperCase() + s.slice(1);

function shapeSvg(shape, cx, cy, R, style) {
  const pts = (n, rot, rr = R) => Array.from({ length: n }, (_, i) => { const a = rot + (i * 2 * Math.PI) / n; return `${(cx + rr * Math.cos(a)).toFixed(1)},${(cy + rr * Math.sin(a)).toFixed(1)}`; }).join(" ");
  switch (SHAPES[shape]) {
    case "circle": return `<circle cx="${cx}" cy="${cy}" r="${(R * 0.9).toFixed(1)}" ${style}/>`;
    case "square": { const s = R * 1.5; return `<rect x="${(cx - s / 2).toFixed(1)}" y="${(cy - s / 2).toFixed(1)}" width="${s.toFixed(1)}" height="${s.toFixed(1)}" ${style}/>`; }
    case "triangle": return `<polygon points="${pts(3, -Math.PI / 2)}" ${style}/>`;
    case "diamond": return `<polygon points="${cx},${(cy - R).toFixed(1)} ${(cx + R * 0.72).toFixed(1)},${cy} ${cx},${(cy + R).toFixed(1)} ${(cx - R * 0.72).toFixed(1)},${cy}" ${style}/>`;
    case "pentagon": return `<polygon points="${pts(5, -Math.PI / 2)}" ${style}/>`;
    default: {
      const out = [];
      for (let i = 0; i < 10; i++) { const a = -Math.PI / 2 + (i * Math.PI) / 5, rr = i % 2 ? R * 0.45 : R; out.push(`${(cx + rr * Math.cos(a)).toFixed(1)},${(cy + rr * Math.sin(a)).toFixed(1)}`); }
      return `<polygon points="${out.join(" ")}" ${style}/>`;
    }
  }
}

function glyph(o) {
  const id = "h" + (++uid);
  const pos = { 1: [[50, 50]], 2: [[29, 50], [71, 50]], 3: [[50, 28], [28, 71], [72, 71]] }[o.count];
  const base = { 1: 36, 2: 18, 3: 16 }[o.count] * [0.55, 0.78, 1][o.size];
  const style = o.fill === 0 ? 'class="glyph"' : o.fill === 2 ? 'class="glyph solid"' : `class="glyph" style="fill:url(#${id})"`;
  return `<svg viewBox="0 0 100 100" width="100%" height="100%" aria-hidden="true"><defs><pattern id="${id}" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="5" style="stroke:var(--ink);stroke-width:1.5"/></pattern></defs>${pos.map(p => shapeSvg(o.shape, p[0], p[1], base, style)).join("")}</svg>`;
}

export const meta = {
  id: "matrix", title: "Matrix Reasoning", ability: "gf", abilityName: "Fluid reasoning",
  blurb: "Find the rule hiding in a 3×3 grid and complete it. The core of most IQ tests.", minutes: 8
};

export function mount(root) {
  intro(root, meta, `
    <p>Each grid follows rules across its <strong>rows</strong>. A rule can change the <strong>shape</strong>, <strong>number</strong>, <strong>fill</strong> or <strong>size</strong> of what's in each cell.</p>
    <p>There are three kinds of rule. <strong>Progression:</strong> something climbs or drops one step across the row. <strong>Distribution:</strong> each row uses the same three values in a different order. <strong>Constant:</strong> it stays put across a row.</p>
    <p>Method: check one attribute at a time, reading across rows. Decide what the missing cell needs, <em>then</em> look at the options. Ten puzzles, adaptive level, currently <strong>level ${store.level("matrix")} of ${MAX}</strong>.</p>`, () => play(root));
}

function play(root) {
  const level = store.level("matrix");
  const items = Array.from({ length: TOTAL }, () => makeItem(level));
  const results = [], review = [];
  let i = 0, off = null, t0 = 0, times = [];
  const L = "ABCDEFGH";

  const show = () => {
    const it = items[i];
    let picked = null;
    t0 = performance.now();
    const render = () => {
      const done = picked != null, good = done && picked === 0 + it.options.indexOf(it.answer);
      const ex = explain(it);
      root.innerHTML = `
      <div class="stage">
        ${topLine(meta, `Level ${level} · Puzzle ${i + 1} of ${TOTAL}`, pips(TOTAL, results, i))}
        <div class="matrix-wrap">
          <div class="matrix" role="img" aria-label="3 by 3 matrix with the last cell missing">
            ${it.cells.map((c, k) => k === 8 ? `<div class="cell q">${done ? glyph(it.answer) : "?"}</div>` : `<div class="cell">${glyph(c)}</div>`).join("")}
          </div>
          <div class="stack">
            <span class="sub">Which option completes the grid?</span>
            <div class="mopts">${it.options.map((o, k) => {
              const cls = done ? (o === it.answer ? "right" : k === picked ? "wrong" : "") : "";
              return `<button class="mopt ${cls}" data-k="${k}" ${done ? "disabled" : ""} aria-label="Option ${L[k]}"><span class="k">${L[k]}</span>${glyph(o)}</button>`;
            }).join("")}</div>
          </div>
        </div>
        ${done ? `<div class="feedback ${good ? "good" : "bad"}" role="status"><span class="verdict">${good ? "Correct." : "Not this time."}</span><p class="why"><b>Rule</b>${esc(ex.rule)}</p><p>${esc(ex.answer)}</p></div>` : ""}
        <div class="actions"><span class="hint">${done ? "Enter to continue" : "Click an option or press A–H"}</span><button class="btn" data-next ${done ? "" : "disabled"}>${i === TOTAL - 1 ? "See results" : "Next puzzle"}</button></div>
      </div>`;
      root.querySelectorAll("[data-k]").forEach(b => b.addEventListener("click", () => choose(Number(b.dataset.k))));
      root.querySelector("[data-next]").addEventListener("click", next);
      if (done) root.querySelector("[data-next]").focus();
    };
    const choose = k => {
      if (picked != null) return;
      picked = k;
      times.push((performance.now() - t0) / 1000);
      const good = it.options[k] === it.answer;
      results[i] = good;
      if (!good) { const ex = explain(it); review.push({ q: `Puzzle ${i + 1}`, your: describe(it.options[k]), right: describe(it.answer), why: ex.rule }); }
      render();
    };
    const next = () => { if (picked == null) return; if (i < TOTAL - 1) { i++; show(); } else end(); };
    if (off) off();
    off = keys(e => {
      const idx = "abcdefgh".indexOf(e.key.toLowerCase());
      if (idx >= 0 && picked == null) choose(idx);
      else if (e.key === "Enter" && picked != null) { e.preventDefault(); next(); }
    });
    render();
  };

  const end = () => {
    if (off) off();
    const score = results.filter(Boolean).length;
    const acc = Math.round((score / TOTAL) * 100);
    const nl = nextLevel(level, acc, MAX);
    store.level("matrix", nl);
    const avg = times.reduce((a, b) => a + b, 0) / times.length;
    finish(root, meta, {
      score, max: TOTAL, level, newLevel: nl, norm: levelNorm(level, MAX, acc), metric: `level ${level}, avg ${avg.toFixed(1)}s`,
      summary: `Level ${level}. Average ${avg.toFixed(1)} seconds per puzzle. Accuracy matters more than speed here: real matrix tests give you time to check every rule.`,
      review
    }, () => play(root));
  };
  show();
}
