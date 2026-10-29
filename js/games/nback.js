// Position N-Back — press Match when the lit square is in the same place as N steps ago.
import { sleep, shuffle } from "../ui.js";
import { intro, finish, topLine, keys, levelNorm, nextLevel } from "./common.js";
import * as store from "../store.js";

const MAX = 4, TRIALS = 20;

export const meta = {
  id: "nback", title: "N-Back", ability: "gwm", abilityName: "Working memory",
  blurb: "Track where a square lit up N steps back while new ones keep coming.", minutes: 4
};

export function mount(root) {
  const n = store.level("nback");
  intro(root, meta, `
    <p>A square lights up on a 3×3 grid, one every 2.5 seconds. Press <strong>Match</strong> (or the <strong>space bar</strong>) when it's in the same spot as it was <strong>${n} step${n > 1 ? "s" : ""} ago</strong>. If it isn't, do nothing.</p>
    <p>Method: say the positions in your head as a rolling list ("top-left, middle, top-left…") and drop the oldest one each step.</p>
    <p class="sub">Straight talk: research finds n-back training makes you better at n-back and similar memory tasks, but it hasn't been shown to raise IQ scores by itself. Treat it as working-memory reps, not a shortcut.</p>
    <p>Current level: <strong>${n}-back</strong> (of ${MAX}).</p>`, () => play(root));
}

function sequence(n) {
  const total = TRIALS + n;
  const seq = [];
  const targets = new Set(shuffle(Array.from({ length: TRIALS }, (_, i) => i + n)).slice(0, 6));
  for (let i = 0; i < total; i++) {
    if (targets.has(i)) seq.push(seq[i - n]);
    else {
      let p;
      do { p = Math.floor(Math.random() * 9); } while (i >= n && p === seq[i - n]);
      seq.push(p);
    }
  }
  return seq;
}

async function play(root) {
  const n = store.level("nback");
  const seq = sequence(n);
  let alive = true;
  window.addEventListener("hashchange", () => { alive = false; }, { once: true });
  let hits = 0, misses = 0, fa = 0, cr = 0, pressed = false, idx = -1;

  root.innerHTML = `
    <div class="stage">
      ${topLine(meta, `${n}-back`, '<span class="mono" data-count></span>')}
      <div class="nb-grid" data-grid>${"<i></i>".repeat(9)}</div>
      <div class="actions" style="justify-content:center"><button class="btn" data-match style="min-width:200px">Match (space)</button></div>
      <p class="hint" style="text-align:center" data-msg>Get ready…</p>
    </div>`;
  const cells = root.querySelectorAll("[data-grid] i");
  const btn = root.querySelector("[data-match]");
  const count = root.querySelector("[data-count]");
  const msg = root.querySelector("[data-msg]");
  const grid = root.querySelector("[data-grid]");

  const press = () => {
    if (pressed || idx < n) return;
    pressed = true;
    const isTarget = seq[idx] === seq[idx - n];
    grid.classList.add(isTarget ? "flash-good" : "flash-bad");
    setTimeout(() => grid.classList.remove("flash-good", "flash-bad"), 250);
  };
  btn.addEventListener("click", press);
  const off = keys(e => { if (e.key === " " || e.key === "m" || e.key === "M") { e.preventDefault(); press(); } });

  await sleep(1200);
  for (idx = 0; idx < seq.length; idx++) {
    if (!alive) { off(); return; }
    pressed = false;
    count.textContent = `${Math.max(0, idx - n + 1)}/${TRIALS}`;
    msg.textContent = idx < n ? `Memorize. Matching starts after ${n} square${n > 1 ? "s" : ""}.` : "";
    cells.forEach((c, k) => c.classList.toggle("on", k === seq[idx]));
    await sleep(700);
    cells.forEach(c => c.classList.remove("on"));
    await sleep(1800);
    if (idx >= n) {
      const isTarget = seq[idx] === seq[idx - n];
      if (isTarget && pressed) hits++;
      else if (isTarget) misses++;
      else if (pressed) fa++;
      else cr++;
    }
  }
  off();
  if (!alive) return;
  const correct = hits + cr;
  const acc = Math.round((correct / TRIALS) * 100);
  const nl = nextLevel(n, acc, MAX, 85, 60);
  store.level("nback", nl);
  finish(root, meta, {
    score: correct, max: TRIALS, level: n, newLevel: nl, norm: levelNorm(n, MAX, acc),
    metric: `${n}-back, hits ${hits}, missed ${misses}, false alarms ${fa}`,
    summary: `${n}-back. Caught ${hits} of ${hits + misses} matches, ${fa} false alarm${fa === 1 ? "" : "s"}. False alarms mean you're pressing on a feeling. Misses mean the list slipped. Fix whichever is bigger.`,
    review: []
  }, () => play(root));
}
