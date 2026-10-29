// Mental Rotation — is the right shape the same as the left one rotated, or a mirror image?
import { rand, pick } from "../ui.js";
import { intro, finish, topLine, pips, keys, clamp } from "./common.js";

const TOTAL = 16;

export const meta = {
  id: "rotation", title: "Mental Rotation", ability: "gv", abilityName: "Visual-spatial",
  blurb: "Turn shapes in your head. Same shape rotated, or its mirror image?", minutes: 4
};

export function mount(root) {
  intro(root, meta, `
    <p>Two block shapes. The right one has been <strong>rotated</strong>. Sometimes it has also been <strong>flipped</strong> into its mirror image.</p>
    <p>Press <strong>S</strong> for <strong>Same</strong> (just rotated) or <strong>M</strong> for <strong>Mirror</strong>.</p>
    <p>Method: find one distinctive feature, like the "foot" that sticks out, and track it as you turn the shape. Then check which side it ends up on.</p>`, () => play(root));
}

const norm = cells => {
  const minX = Math.min(...cells.map(c => c[0])), minY = Math.min(...cells.map(c => c[1]));
  return cells.map(c => [c[0] - minX, c[1] - minY]).sort((a, b) => a[0] - b[0] || a[1] - b[1]);
};
const key = cells => norm(cells).map(c => c.join(",")).join(";");
const rot = cells => cells.map(([x, y]) => [-y, x]);
const mir = cells => cells.map(([x, y]) => [-x, y]);
const rotations = cells => { const out = [cells]; for (let i = 0; i < 3; i++) out.push(rot(out[out.length - 1])); return out; };

function polyomino(size) {
  for (;;) {
    const cells = [[0, 0]];
    const has = (x, y) => cells.some(c => c[0] === x && c[1] === y);
    while (cells.length < size) {
      const [x, y] = pick(cells);
      const [dx, dy] = pick([[1, 0], [-1, 0], [0, 1], [0, -1]]);
      if (!has(x + dx, y + dy)) cells.push([x + dx, y + dy]);
    }
    const rk = new Set(rotations(cells).map(key));
    const mk = rotations(mir(cells)).map(key);
    if (mk.every(k => !rk.has(k))) return cells; // chiral: mirror is never a rotation
  }
}

function svg(cells) {
  const n = norm(cells);
  const w = Math.max(...n.map(c => c[0])) + 1, h = Math.max(...n.map(c => c[1])) + 1;
  const s = Math.max(w, h);
  const ox = (s - w) / 2, oy = (s - h) / 2;
  return `<svg viewBox="-0.3 -0.3 ${s + 0.6} ${s + 0.6}" width="100%" style="max-width:200px;aspect-ratio:1" aria-hidden="true">${n.map(([x, y]) => `<rect x="${x + ox}" y="${y + oy}" width="1" height="1" style="stroke-width:.06"/>`).join("")}</svg>`;
}

function play(root) {
  const items = Array.from({ length: TOTAL }, (_, i) => {
    const base = polyomino(i < 6 ? 5 : rand(5, 7));
    const mirror = Math.random() < 0.5;
    let shown = mirror ? mir(base) : base;
    const turns = rand(1, 3);
    for (let t = 0; t < turns; t++) shown = rot(shown);
    return { base, shown, mirror, turns };
  });
  const results = [], times = [];
  let i = 0, t0 = 0, off = null, locked = false;

  const show = () => {
    const it = items[i];
    locked = false;
    root.innerHTML = `
      <div class="stage">
        ${topLine(meta, `${i + 1} of ${TOTAL}`, pips(TOTAL, results, i))}
        <div class="rot-pair"><div>${svg(it.base)}</div><div>${svg(it.shown)}</div></div>
        <div class="actions" style="justify-content:center;gap:14px">
          <button class="btn" data-a="same" style="min-width:150px">Same (S)</button>
          <button class="btn ghost" data-a="mirror" style="min-width:150px">Mirror (M)</button>
        </div>
        <p class="hint" style="text-align:center" data-msg>&nbsp;</p>
      </div>`;
    t0 = performance.now();
    root.querySelectorAll("[data-a]").forEach(b => b.addEventListener("click", () => answer(b.dataset.a === "mirror")));
  };
  const answer = saidMirror => {
    if (locked) return;
    locked = true;
    const it = items[i];
    times.push((performance.now() - t0) / 1000);
    results[i] = saidMirror === it.mirror;
    const m = root.querySelector("[data-msg]");
    m.innerHTML = results[i] ? `<span style="color:var(--good)">Correct</span> · rotated ${it.turns * 90}°${it.mirror ? " and mirrored" : ""}` : `<span style="color:var(--bad)">It was ${it.mirror ? "a mirror image" : "the same shape"}</span> · rotated ${it.turns * 90}°`;
    setTimeout(() => { if (i < TOTAL - 1) { i++; show(); } else end(); }, results[i] ? 650 : 1500);
  };
  off = keys(e => { const k = e.key.toLowerCase(); if (k === "s") answer(false); else if (k === "m") answer(true); });
  window.addEventListener("hashchange", () => { locked = true; off(); }, { once: true });
  show();

  function end() {
    off();
    const score = results.filter(Boolean).length;
    const acc = Math.round((score / TOTAL) * 100);
    const avg = times.reduce((a, b) => a + b, 0) / times.length;
    const speed = clamp(((6 - avg) / 5) * 100);
    finish(root, meta, {
      score, max: TOTAL, level: 0, newLevel: 0, norm: Math.round(acc * 0.7 + speed * 0.3),
      metric: `avg ${avg.toFixed(1)}s`, summary: `Average ${avg.toFixed(1)} seconds per shape. Get accurate first, then the speed comes.`, review: []
    }, () => play(root));
  }
}
