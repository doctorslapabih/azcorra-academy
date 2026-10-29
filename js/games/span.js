// Digit Span — forward then backward, adaptive length. Measures working memory span.
import { esc, rand, sleep } from "../ui.js";
import { intro, finish, topLine, keys, clamp } from "./common.js";

export const meta = {
  id: "span", title: "Digit Span", ability: "gwm", abilityName: "Working memory",
  blurb: "Hold a string of digits in your head, then repeat it forward and backward.", minutes: 5
};

export function mount(root) {
  intro(root, meta, `
    <p>Digits flash one at a time. When they stop, type them back.</p>
    <p><strong>Round 1, forward:</strong> type them in the same order. <strong>Round 2, backward:</strong> type them in reverse order. Each correct answer adds a digit. Two misses at the same length ends the round.</p>
    <p>Method: <strong>chunk</strong> the digits into groups of two or three, like a phone number. 7-4-1-9-2-8 becomes "74, 19, 28." For backward, picture the digits on a line and read it from the right.</p>
    <p class="sub">For reference, most adults hold about 6 to 7 digits forward and 4 to 5 backward.</p>`, () => run(root));
}

function digits(n) {
  const out = [];
  while (out.length < n) { const d = rand(0, 9); if (d !== out[out.length - 1]) out.push(d); }
  return out;
}

async function run(root) {
  const fwd = await round(root, "forward", 3);
  if (fwd == null) return;
  const bwd = await round(root, "backward", 2);
  if (bwd == null) return;
  const norm = Math.round(clamp(((fwd - 3) / 6) * 50 + ((bwd - 2) / 6) * 50));
  finish(root, meta, {
    score: fwd + bwd, max: 0, big: `${fwd} · ${bwd}`, bigLabel: "fwd · back", level: 0, newLevel: 0, norm,
    metric: `forward ${fwd}, backward ${bwd}`, headline: `Forward ${fwd}. Backward ${bwd}.`,
    summary: `Your longest correct strings: ${fwd} digits forward and ${bwd} backward. Backward is the harder one because you have to hold the digits and rearrange them at the same time.`,
    review: []
  }, () => run(root));
}

function round(root, mode, startLen) {
  return new Promise(resolve => {
    let len = startLen, misses = 0, best = 0, trial = 0, alive = true;
    const onLeave = () => { alive = false; resolve(null); };
    window.addEventListener("hashchange", onLeave, { once: true });

    const step = async () => {
      if (!alive) return;
      trial++;
      const seq = digits(len);
      root.innerHTML = `
        <div class="stage">
          ${topLine(meta, `${mode === "forward" ? "Forward" : "Backward"} · ${len} digits`, `<span class="mono">best ${best}</span>`)}
          <div class="digit" aria-live="off" data-d>&nbsp;</div>
          <p class="hint" style="text-align:center">Watch…</p>
        </div>`;
      const d = root.querySelector("[data-d]");
      await sleep(700);
      for (const n of seq) {
        if (!alive) return;
        d.textContent = n; await sleep(800);
        d.innerHTML = "&nbsp;"; await sleep(220);
      }
      if (!alive) return;
      root.innerHTML = `
        <div class="stage">
          ${topLine(meta, `${mode === "forward" ? "Forward" : "Backward"} · ${len} digits`, `<span class="mono">best ${best}</span>`)}
          <form class="stack" data-form autocomplete="off" style="align-items:center">
            <label class="prompt" for="ans">${mode === "forward" ? "Type the digits in order." : "Type the digits in <em>reverse</em> order."}</label>
            <input id="ans" class="input" inputmode="numeric" style="width:min(100%,320px);text-align:center;letter-spacing:.3em" aria-label="Digits">
            <button class="btn" type="submit">Check</button>
          </form>
        </div>`;
      const inp = root.querySelector("#ans");
      inp.focus();
      root.querySelector("[data-form]").addEventListener("submit", e => {
        e.preventDefault();
        const typed = inp.value.replace(/\D/g, "");
        const target = (mode === "forward" ? seq : seq.slice().reverse()).join("");
        const good = typed === target;
        if (good) { best = Math.max(best, len); len++; misses = 0; }
        else misses++;
        const over = misses >= 2 || len > 12;
        root.innerHTML = `
          <div class="stage">
            ${topLine(meta, `${mode === "forward" ? "Forward" : "Backward"}`, `<span class="mono">best ${best}</span>`)}
            <div class="feedback ${good ? "good" : "bad"}" role="status">
              <span class="verdict">${good ? "Correct." : "Missed it."}</span>
              <p>Shown: <span class="mono">${seq.join(" ")}</span>${mode === "backward" ? ` · Backward: <span class="mono">${seq.slice().reverse().join(" ")}</span>` : ""}</p>
              ${good ? "" : `<p>You typed: <span class="mono">${esc(typed.split("").join(" ")) || "nothing"}</span></p>`}
            </div>
            <div class="actions"><span class="hint">${over ? "Round over." : good ? `Next: ${len} digits.` : misses === 1 ? "One more try at this length." : ""}</span>
            <button class="btn" data-next>${over ? (mode === "forward" ? "Start backward round" : "See results") : "Next"}</button></div>
          </div>`;
        const b = root.querySelector("[data-next]");
        b.focus();
        b.addEventListener("click", () => {
          if (over) { alive = false; window.removeEventListener("hashchange", onLeave); resolve(best); }
          else step();
        });
      });
    };
    step();
  });
}
