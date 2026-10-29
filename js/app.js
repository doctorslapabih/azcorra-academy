// Azcorra Academy — router and pages.
import { esc, fmtDate, pct, spark, toast, copyText, renderMath } from "./ui.js";
import * as store from "./store.js";
import { GAMES, ABILITIES, find } from "./games/index.js";
import { renderLesson, loadCatalog, loadCourse } from "./course.js";

const app = document.getElementById("app");

function setNav(key) {
  document.querySelectorAll("[data-nav]").forEach(a => { if (a.dataset.nav === key) a.setAttribute("aria-current", "page"); else a.removeAttribute("aria-current"); });
}

function greeting() {
  const h = new Date().getHours();
  return h < 12 ? "Good morning" : h < 18 ? "Good afternoon" : "Good evening";
}

function profile() {
  const S = store.all().sessions;
  return ABILITIES.map(a => {
    const recent = S.filter(s => s.kind === "iq" && s.ability === a.id).slice(0, 3);
    const v = recent.length ? Math.round(recent.reduce((t, s) => t + (s.norm || 0), 0) / recent.length) : null;
    return Object.assign({ v, n: S.filter(s => s.ability === a.id).length }, a);
  });
}

function profileHtml() {
  return `<div class="profile" aria-label="Ability profile">
    ${profile().map(a => `<div class="ability" title="${esc(a.desc)}"><span>${esc(a.name)}</span><div class="track"><div class="fill" style="width:${a.v || 0}%"></div></div><span class="v">${a.v == null ? "—" : a.v}</span></div>`).join("")}
    <p class="sub">Practice index from your last three sessions in each area, 0–100. It tracks your progress in this Lab. It is not an IQ score.</p>
  </div>`;
}

function todaysSet() {
  const day = Math.floor(Date.now() / 86400000);
  const rotating = ["series", "logic", "analogies", "rotation", "speed"];
  return [find("matrix"), find(day % 2 ? "span" : "nback"), find(rotating[day % rotating.length])];
}

/* ---------------- pages ---------------- */
async function home() {
  setNav("home");
  const st = store.all();
  const done = Object.values(st.lessons).filter(l => l.complete).length;
  const last = st.sessions[0];
  let catalog = [];
  try { catalog = await loadCatalog(); } catch (e) { catalog = []; }
  app.innerHTML = `
  <section class="hero">
    <div class="stack">
      <span class="eyebrow">${esc(new Date().toLocaleDateString(undefined, { weekday: "long", month: "long", day: "numeric" }))}</span>
      <h1 class="title">${greeting()}, Isaac.</h1>
      <p class="lede">Your academy: an IQ Lab for sharpening how you think, and full courses for what you know. Pick up where you left off.</p>
      <div class="row">${last ? `<a class="btn" href="${last.kind === "lesson" ? "#/learn/" + esc(last.course) + "/" + esc(last.lesson) : "#/lab/" + esc(last.game)}">Continue: ${esc(last.title)}</a>` : `<a class="btn" href="#/lab/understanding-iq">Start with Understanding IQ</a>`}<a class="btn ghost" href="#/lab">Open the Lab</a></div>
    </div>
    <div class="ledger" aria-label="Your record">
      <div><b>${st.sessions.length}</b><span>Sessions</span></div>
      <div><b>${store.streak()}</b><span>Day streak</span></div>
      <div><b>${done}</b><span>Lessons done</span></div>
    </div>
  </section>

  <section class="stack">
    <div class="section-head"><h2 class="h2">Today's training</h2><span class="sub">About 15 minutes · rotates daily</span></div>
    <div class="grid fit">${todaysSet().map(g => gameCard(g)).join("")}</div>
  </section>

  <section class="stack">
    <div class="section-head"><h2 class="h2">Courses</h2><a class="sub" href="#/courses">All courses →</a></div>
    <div class="grid wide">${catalog.map(courseCard).join("") || '<div class="empty">Courses are loading.</div>'}</div>
  </section>

  <section class="stack">
    <div class="section-head"><h2 class="h2">Ability profile</h2><a class="sub" href="#/lab">IQ Lab →</a></div>
    ${profileHtml()}
  </section>`;
}

function gameCard(g) {
  const m = g.meta;
  const hist = store.sessionsFor(m.id).slice(0, 10).reverse().map(s => s.norm || 0);
  const lvl = store.all().levels[m.id];
  return `<a class="card" href="#/lab/${m.id}">
    <span class="code">${esc(m.abilityName.toUpperCase())}</span>
    <h3>${esc(m.title)}</h3>
    <p>${esc(m.blurb)}</p>
    ${hist.length > 1 ? spark(hist) : ""}
    <div class="foot"><span>~${m.minutes} min</span><span>${lvl ? "Level " + lvl : hist.length ? hist.length + " played" : "New"}</span></div>
  </a>`;
}

function courseCard(c) {
  const st = store.all();
  const total = c.units.reduce((t, u) => t + u.lessons.length, 0);
  const ready = c.units.reduce((t, u) => t + u.lessons.filter(l => l.ready).length, 0);
  const done = c.units.reduce((t, u) => t + u.lessons.filter(l => st.lessons[c.id + "/" + l.id] && st.lessons[c.id + "/" + l.id].complete).length, 0);
  return `<a class="card" href="#/course/${esc(c.id)}">
    <span class="code">${esc(c.code)} · ${esc(c.span)}</span>
    <h3>${esc(c.title)}</h3>
    <p>${esc(c.blurb)}</p>
    <div class="foot"><span>${c.units.length} units · ${total} lessons</span><span>${ready ? `${done}/${ready} done` : '<span class="tag soon">Being written</span>'}</span></div>
  </a>`;
}

function lab() {
  setNav("lab");
  app.innerHTML = `
  <section class="stack">
    <span class="eyebrow">IQ Lab</span>
    <h1 class="title">Train how you think.</h1>
    <p class="lede">Each game targets one of the abilities that IQ tests measure. Levels adapt to you. Start with the reading if you want to know what you're training and why.</p>
    <div class="row"><a class="btn accent" href="#/lab/understanding-iq">Read: Understanding IQ</a></div>
  </section>
  <section class="stack">
    <div class="section-head"><h2 class="h2">Your profile</h2><span class="sub">Updates after every session</span></div>
    ${profileHtml()}
  </section>
  <section class="stack">
    <div class="section-head"><h2 class="h2">The games</h2><span class="sub">${GAMES.length} games · 7 abilities</span></div>
    <div class="grid">${GAMES.map(gameCard).join("")}</div>
  </section>`;
}

async function understanding() {
  setNav("lab");
  try {
    const res = await fetch("data/iq/understanding-iq.json");
    const lesson = await res.json();
    renderLesson(app, { course: null, lesson, back: "#/lab", backLabel: "IQ Lab" });
  } catch (e) {
    app.innerHTML = `<div class="empty">Couldn't load this reading. If you're offline, open it once while online so it's saved.</div>`;
  }
}

function game(id) {
  setNav("lab");
  const g = find(id);
  if (!g) return notFound();
  app.innerHTML = `<div data-stage></div>`;
  g.mount(app.querySelector("[data-stage]"));
}

async function courses() {
  setNav("courses");
  let catalog = [];
  try { catalog = await loadCatalog(); } catch (e) { /* offline */ }
  app.innerHTML = `
  <section class="stack">
    <span class="eyebrow">Courses</span>
    <h1 class="title">From 7th grade to AP.</h1>
    <p class="lede">Each course runs in order: short readings, worked examples, then practice you have to get 80% on to master the lesson. New lessons land here as they're written.</p>
  </section>
  <div class="grid wide">${catalog.map(courseCard).join("") || '<div class="empty">Couldn\'t load the catalog. Check your connection and refresh.</div>'}</div>`;
}

async function course(id) {
  setNav("courses");
  let c;
  try { c = await loadCourse(id); } catch (e) { return notFound(); }
  const st = store.all();
  app.innerHTML = `
  <section class="stack">
    <a class="sub" href="#/courses">← Courses</a>
    <span class="eyebrow">${esc(c.code)} · ${esc(c.span)}</span>
    <h1 class="title">${esc(c.title)}</h1>
    <p class="lede">${esc(c.intro || c.blurb)}</p>
  </section>
  ${c.units.map((u, ui) => `
  <section class="stack">
    <div class="section-head"><h2 class="h2"><span class="mono" style="font-size:16px;color:var(--gold);margin-right:10px">UNIT ${ui + 1}</span>${esc(u.title)}</h2><span class="sub">${esc(u.band || "")}</span></div>
    ${u.summary ? `<p class="sub" style="max-width:70ch">${esc(u.summary)}</p>` : ""}
    <div class="entries">${u.lessons.map((l, li) => {
      const rec = st.lessons[c.id + "/" + l.id];
      const status = rec && rec.complete ? '<span class="tag live">Mastered</span>' : rec && rec.best != null ? `<span class="tag">Best ${rec.best}%</span>` : l.ready ? '<span class="tag">Ready</span>' : '<span class="tag soon">Coming</span>';
      const inner = `<span class="d">${ui + 1}.${li + 1}</span><span class="t">${esc(l.title)}${l.desc ? `<small>${esc(l.desc)}</small>` : ""}</span><span>${status}</span>`;
      return l.ready ? `<a class="entry" style="text-decoration:none" href="#/learn/${esc(c.id)}/${esc(l.id)}">${inner}</a>` : `<div class="entry" style="opacity:.6">${inner}</div>`;
    }).join("")}</div>
  </section>`).join("")}`;
}

async function learn(courseId, lessonId) {
  setNav("courses");
  let c, lesson;
  try {
    c = await loadCourse(courseId);
    const res = await fetch(`data/lessons/${courseId}/${lessonId}.json`);
    if (!res.ok) throw new Error("missing");
    lesson = await res.json();
  } catch (e) {
    app.innerHTML = `<div class="stack"><a class="sub" href="#/course/${esc(courseId)}">← Back to course</a><div class="empty">This lesson isn't written yet, or you're offline. Lessons you've opened before work offline.</div></div>`;
    return;
  }
  renderLesson(app, { course: c, lesson, back: "#/course/" + courseId, backLabel: c.title });
}

function journal() {
  setNav("journal");
  const st = store.all();
  const unlogged = st.sessions.filter(s => !s.logged);
  app.innerHTML = `
  <section class="stack">
    <span class="eyebrow">Journal</span>
    <h1 class="title">Everything you've studied.</h1>
    <p class="lede">Every game and lesson lands here. To file it in your Notion notebook, copy the unlogged entries and paste them to Claude with "log these."</p>
    <div class="row">
      <button class="btn" data-copy ${unlogged.length ? "" : "disabled"}>Copy ${unlogged.length} unlogged for Claude</button>
      <button class="btn ghost" data-mark ${unlogged.length ? "" : "disabled"}>Mark as logged</button>
    </div>
  </section>
  ${st.sessions.length ? `<div class="entries">${st.sessions.slice(0, 200).map(s => `
    <div class="entry"><span class="d">${esc(fmtDate(s.at))}</span>
      <span class="t">${esc(s.title)}<small>${esc(s.kind === "lesson" ? "Lesson · " + (s.courseTitle || "") : "IQ Lab" + (s.metric ? " · " + s.metric : ""))}${s.logged ? " · logged" : ""}</small></span>
      <span class="s">${s.max ? `${s.score}/${s.max}` : s.norm != null ? "idx " + s.norm : ""}</span></div>`).join("")}</div>`
    : '<div class="empty">No sessions yet. Play a game in the IQ Lab or finish a lesson and it shows up here.</div>'}
  <section class="stack">
    <div class="section-head"><h2 class="h2">Backup</h2><span class="sub">Progress lives in this browser</span></div>
    <p class="sub" style="max-width:70ch">Your progress is saved on this device. To move it to another computer or phone, copy the backup here and paste it there.</p>
    <div class="row"><button class="btn ghost" data-export>Copy backup</button></div>
    <label class="sub" for="restore">Paste a backup to restore it on this device</label>
    <textarea id="restore" class="paste" placeholder='{"sessions":[…]}'></textarea>
    <div class="row"><button class="btn ghost" data-import>Restore from backup</button></div>
  </section>`;

  app.querySelector("[data-copy]").addEventListener("click", async () => {
    const text = journalText(unlogged);
    const ok = await copyText(text);
    toast(ok ? "Copied. Paste it to Claude with \"log these.\"" : "Couldn't copy. Try again.");
  });
  app.querySelector("[data-mark]").addEventListener("click", () => { store.markLogged(unlogged.map(s => s.id)); toast("Marked as logged."); journal(); });
  app.querySelector("[data-export]").addEventListener("click", async () => { const ok = await copyText(store.exportJSON()); toast(ok ? "Backup copied." : "Couldn't copy."); });
  app.querySelector("[data-import]").addEventListener("click", () => {
    try { store.importJSON(app.querySelector("#restore").value); toast("Restored."); journal(); }
    catch (e) { toast(e.message || "That backup couldn't be read."); }
  });
}

function journalText(list) {
  const lines = ["AZCORRA ACADEMY — journal entries to log", ""];
  list.slice().reverse().forEach(s => {
    const d = new Date(s.at);
    const head = `${d.toLocaleDateString()} ${d.toLocaleTimeString([], { hour: "numeric", minute: "2-digit" })} · ${s.kind === "lesson" ? "Lesson" : "IQ Lab"} · ${s.title}`;
    lines.push(head);
    if (s.courseTitle) lines.push(`  Course: ${s.courseTitle}`);
    if (s.ability) lines.push(`  Ability: ${(ABILITIES.find(a => a.id === s.ability) || {}).name || s.ability}`);
    lines.push(`  Result: ${s.max ? s.score + "/" + s.max + " (" + pct(s.score, s.max) + "%)" : ""}${s.metric ? " " + s.metric : ""}${s.norm != null ? " · index " + s.norm : ""}`);
    (s.notes || []).forEach(n => lines.push(`  Missed: ${n}`));
    if (s.myNotes) lines.push(`  My notes: ${s.myNotes}`);
    lines.push("");
  });
  return lines.join("\n");
}

function notFound() {
  app.innerHTML = `<div class="stack"><h1 class="title">Not here.</h1><p class="lede">That page doesn't exist.</p><a class="btn" href="#/">Home</a></div>`;
}

/* ---------------- router ---------------- */
async function route() {
  const parts = (location.hash.replace(/^#\/?/, "") || "").split("/").filter(Boolean);
  window.scrollTo(0, 0);
  if (!parts.length) await home();
  else if (parts[0] === "lab" && !parts[1]) lab();
  else if (parts[0] === "lab" && parts[1] === "understanding-iq") await understanding();
  else if (parts[0] === "lab") game(parts[1]);
  else if (parts[0] === "courses") await courses();
  else if (parts[0] === "course" && parts[1]) await course(parts[1]);
  else if (parts[0] === "learn" && parts[1] && parts[2]) await learn(parts[1], parts[2]);
  else if (parts[0] === "journal") journal();
  else notFound();
  renderMath(app);
}
window.addEventListener("hashchange", route);
route();

/* ---------------- install + offline ---------------- */
if ("serviceWorker" in navigator) {
  window.addEventListener("load", () => { navigator.serviceWorker.register("sw.js").catch(() => {}); });
}
let deferred = null;
window.addEventListener("beforeinstallprompt", e => {
  e.preventDefault(); deferred = e;
  const slot = document.getElementById("install-slot");
  slot.innerHTML = '<button class="btn ghost" style="padding:5px 12px;font-size:13px" data-install>Install app</button>';
  slot.querySelector("[data-install]").addEventListener("click", async () => {
    if (!deferred) { toast("Use Chrome's ⋮ menu → Cast, save and share → Install page as app."); return; }
    try {
      toast("Look for the install box at the top of your browser window.");
      await deferred.prompt();
      const choice = await deferred.userChoice;
      toast(choice.outcome === "accepted" ? "Installed. Find Azcorra Academy in your app launcher." : "Install canceled.");
    } catch (err) {
      toast("Use Chrome's ⋮ menu → Cast, save and share → Install page as app.");
    }
    deferred = null; slot.innerHTML = "";
  });
});

window.addEventListener("appinstalled", () => { const slot = document.getElementById("install-slot"); if (slot) slot.innerHTML = ""; toast("Installed. Find Azcorra Academy in your app launcher."); });
