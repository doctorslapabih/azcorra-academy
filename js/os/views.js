// Life-OS views: Dashboard, pages, databases (table, board, calendar) and row pages.
import { esc, toast } from "../ui.js";
import * as api from "./api.js";
import { render, bindTodos, buildToc, registerLinks } from "./notion.js";
import { DBS, FORMULAS, TEMPLATES } from "./schemas.js";

// Notion URLs from the original pages → routes in this app.
registerLinks({
  "https://app.notion.com/p/4078e8d1a09281cba799f1726f7b71a0": "#/p/trading-plan",
  "https://app.notion.com/p/4078e8d1a0928160b81dde44a29448a9": "#/p/training",
  "https://app.notion.com/p/4078e8d1a092818d9f28e8c94154e8fd": "#/p/fuel-plan",
  "https://app.notion.com/p/4078e8d1a092817cbb62f3b745ddf372": "#/p/decision-filter",
  "https://app.notion.com/p/4078e8d1a092814482efd6eb95532720": "#/p/how-to-use",
  "https://app.notion.com/p/4088e8d1a092819d9acdd25d818b8df4": "#/p/chapter-i",
  "https://app.notion.com/p/4088e8d1a0928146b417d4008a29ed87": "#/p/chapter-ii",
  "https://app.notion.com/p/4088e8d1a092817cab08f37ae6486b42": "#/p/chapter-iii",
  "https://app.notion.com/p/4088e8d1a092815cb7c9c8f1d7fd623b": "#/p/chapter-iv",
  "https://app.notion.com/p/4088e8d1a09281ca9761fec4c92feea1": "#/p/chapter-v"
}, {
  "collection://175a86b2-46e7-46a1-9e6a-d35ab9f48533": "tasks",
  "collection://52ef0f48-015b-4cd3-83dd-2f13513618b5": "daily_log",
  "collection://ac38c200-bd00-43e7-ac84-369089e1e2b2": "reading_list",
  "collection://454e5dda-fb35-4396-b4f4-38543fcafb4a": "weekly_review",
  "collection://04d1fd9b-4964-40b5-a8ca-03b201384c34": "decisions",
  "collection://6834fc6f-0793-4b2a-b0e6-c7852aa49415": "trading_calendar",
  "collection://7b900f7a-f586-493c-8831-3f181ecfd18a": "notebook"
});

const LOCKED = `<div class="empty"><b>Sign in to see your dashboard.</b> Your private data loads only on your own Cloudflare address, after you sign in.</div>`;

function pageShell(root, { cover, icon, title, full }) {
  root.innerHTML = `
  <article class="notion${full ? " full" : ""}">
    ${cover ? `<div class="n-cover" style="background-image:url('${esc(cover)}')"></div>` : ""}
    <div class="n-head${cover ? "" : " no-cover"}">${icon ? `<div class="n-page-icon">${esc(icon)}</div>` : ""}<h1 class="n-title">${esc(title)}</h1></div>
    <div class="n-body" data-body></div>
  </article>`;
  return root.querySelector("[data-body]");
}

let saveTimers = {};
function debounce(key, fn, ms = 500) { clearTimeout(saveTimers[key]); saveTimers[key] = setTimeout(fn, ms); }

async function fillInlineDbs(root) {
  for (const el of root.querySelectorAll("[data-db]")) {
    const coll = el.dataset.db;
    const schema = DBS[coll];
    if (!schema) continue;
    let rows = await api.list(coll).catch(() => []);
    const f = el.dataset.filter;
    if (f) { const [k, v] = f.split("="); rows = rows.filter(r => (r.data.props || {})[k] === v); }
    el.innerHTML = `<div class="n-db-head"><a href="#/db/${coll}">${esc(el.dataset.title || schema.title)}</a></div>${schema.view === "calendar" ? calendar(coll, rows, el) : table(coll, rows)}`;
    if (schema.view === "calendar") wireCalendar(el, coll, rows);
  }
}

/* ---------------- Dashboard ---------------- */
export async function dashboard(root) {
  if (!(await api.online())) { root.innerHTML = LOCKED; return; }
  const doc = await api.get("dashboard", "main");
  if (!doc) { root.innerHTML = `<div class="empty">The dashboard hasn't been set up yet.</div>`; return; }
  const d = doc.data;
  const day = api.today();
  const checksDoc = await api.get("checks", "dashboard-" + day);
  const checks = checksDoc ? checksDoc.data.state || {} : {};
  const body = pageShell(root, d);
  body.innerHTML = render(d.body, { checks });
  bindTodos(body, checks, state => debounce("dash", () => api.put("checks", "dashboard-" + day, { date: day, state }).catch(() => toast("Couldn't save. Check your connection."))));
  buildToc(body);
  fillInlineDbs(body);
}

/* ---------------- Pages ---------------- */
export async function page(root, slug) {
  if (!(await api.online())) { root.innerHTML = LOCKED; return; }
  const doc = await api.get("pages", slug);
  if (!doc) { root.innerHTML = `<div class="empty">Page not found.</div>`; return; }
  const d = doc.data;
  const body = pageShell(root, d);
  const back = d.parent ? `<a class="n-crumb" href="${esc(d.parent.href)}">← ${esc(d.parent.title)}</a>` : `<a class="n-crumb" href="#/">← Dashboard</a>`;
  root.insertAdjacentHTML("afterbegin", `<div class="n-toolbar">${back}<span data-tools></span></div>`);
  body.innerHTML = render(d.body, { checks: d.checks || {} });
  bindTodos(body, d.checks || {}, state => { d.checks = state; debounce("page-" + slug, () => api.put("pages", slug, d).catch(() => toast("Couldn't save."))); });
  if (body.querySelector("input[data-todo]")) {
    root.querySelector("[data-tools]").innerHTML = '<button class="btn ghost" data-uncheck style="font-size:13px;padding:4px 10px">Uncheck all</button>';
    root.querySelector("[data-uncheck]").addEventListener("click", () => { d.checks = {}; api.put("pages", slug, d).then(() => page(root, slug)).catch(() => toast("Couldn't save.")); });
  }
  buildToc(body);
  fillInlineDbs(body);
}

/* ---------------- Values ---------------- */
const optColor = (p, v) => ((p.options || []).find(o => o.name === v) || {}).color || "default";
function valueHtml(p, props) {
  const v = props[p.name];
  if (p.type === "formula") return esc(FORMULAS[p.formula](props));
  if (v == null || v === "" || (Array.isArray(v) && !v.length)) return "";
  switch (p.type) {
    case "checkbox": return v ? '<span class="n-check on">✓</span>' : '<span class="n-check"></span>';
    case "dollar": return `<span class="${v < 0 ? "n-red" : ""}">${v < 0 ? "−" : ""}$${Math.abs(v).toLocaleString()}</span>`;
    case "number": return esc(String(v));
    case "date": return esc(new Date(v + "T12:00:00").toLocaleDateString(undefined, { month: "short", day: "numeric", year: "numeric" }));
    case "select": case "status": return `<span class="n-tag n-tag-${optColor(p, v)}">${esc(v)}</span>`;
    case "multi": return v.map(x => `<span class="n-tag n-tag-${optColor(p, x)}">${esc(x)}</span>`).join(" ");
    default: return esc(String(v)).slice(0, 220);
  }
}

function sorted(coll, rows) {
  const s = DBS[coll].sort;
  if (!s) return rows;
  return rows.slice().sort((a, b) => {
    const x = (a.data.props || {})[s[0]] || "", y = (b.data.props || {})[s[0]] || "";
    return (x < y ? -1 : x > y ? 1 : 0) * (s[1] === "desc" ? -1 : 1);
  });
}

function table(coll, rows) {
  const schema = DBS[coll];
  if (!rows.length) return `<div class="n-empty">No entries yet.</div>`;
  const cols = schema.props;
  return `<div class="n-table-wrap"><table class="n-table n-dbtable"><thead><tr>${cols.map(p => `<th>${esc(p.name)}</th>`).join("")}</tr></thead><tbody>${sorted(coll, rows).map(r => {
    const props = r.data.props || {};
    return `<tr>${cols.map(p => p.type === "title" ? `<td class="n-titlecell"><a href="#/db/${coll}/${esc(r.id)}">${esc(props[p.name] || "Untitled")}</a></td>` : `<td>${valueHtml(p, props)}</td>`).join("")}</tr>`;
  }).join("")}</tbody></table></div>`;
}

function board(coll, rows) {
  const schema = DBS[coll];
  const group = schema.props.find(p => p.name === schema.groupBy);
  const titleProp = schema.props.find(p => p.type === "title").name;
  const shown = schema.props.filter(p => p.type !== "title" && p.name !== schema.groupBy).slice(0, 3);
  return `<div class="n-board">${group.options.map(o => {
    const cards = sorted(coll, rows).filter(r => ((r.data.props || {})[group.name] || group.default) === o.name);
    return `<div class="n-lane"><div class="n-lane-head"><span class="n-tag n-tag-${o.color}">${esc(o.name)}</span><span class="n-count">${cards.length}</span></div>
      ${cards.map(r => { const props = r.data.props || {}; return `<a class="n-card" href="#/db/${coll}/${esc(r.id)}"><b>${esc(props[titleProp] || "Untitled")}</b>${shown.map(p => { const h = valueHtml(p, props); return h ? `<div>${h}</div>` : ""; }).join("")}</a>`; }).join("")}
      <button class="n-add" data-new="${esc(o.name)}">+ New</button></div>`;
  }).join("")}</div>`;
}

let calMonth = null;
function calendar(coll, rows, host) {
  const schema = DBS[coll];
  const now = calMonth || new Date();
  const y = now.getFullYear(), m = now.getMonth();
  const first = new Date(y, m, 1), startDay = first.getDay();
  const days = new Date(y, m + 1, 0).getDate();
  const byDate = {};
  rows.forEach(r => { const d = (r.data.props || {})[schema.dateProp]; if (d) (byDate[d] = byDate[d] || []).push(r); });
  const cells = [];
  for (let k = 0; k < startDay; k++) cells.push('<div class="n-cal-cell muted"></div>');
  const todayStr = api.today();
  for (let d = 1; d <= days; d++) {
    const ds = `${y}-${String(m + 1).padStart(2, "0")}-${String(d).padStart(2, "0")}`;
    const items = byDate[ds] || [];
    cells.push(`<div class="n-cal-cell${ds === todayStr ? " today" : ""}" data-date="${ds}"><span class="n-cal-num">${d}</span>${items.map(r => {
      const p = r.data.props || {};
      const pnl = p["P&L"];
      return `<a class="n-cal-item" href="#/db/${coll}/${esc(r.id)}">📓 ${esc(p.Day || "Untitled")}${pnl != null && pnl !== "" ? `<span class="${pnl < 0 ? "n-red" : "n-green"}">${pnl < 0 ? "−" : "+"}$${Math.abs(pnl).toLocaleString()}</span>` : ""}${p["Best Grade"] ? `<span class="n-tag n-tag-${optColor(schema.props.find(x => x.name === "Best Grade"), p["Best Grade"])}">${esc(p["Best Grade"])}</span>` : ""}</a>`;
    }).join("")}</div>`);
  }
  const label = first.toLocaleDateString(undefined, { month: "long", year: "numeric" });
  return `<div class="n-cal"><div class="n-cal-bar"><b>${esc(label)}</b><span><button data-cal="-1" aria-label="Previous month">‹</button><button data-cal="0">Today</button><button data-cal="1" aria-label="Next month">›</button></span></div>
    <div class="n-cal-grid">${["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"].map(w => `<div class="n-cal-wd">${w}</div>`).join("")}${cells.join("")}</div></div>`;
}

function wireCalendar(host, coll, rows) {
  host.querySelectorAll("[data-cal]").forEach(b => b.addEventListener("click", () => {
    const step = Number(b.dataset.cal);
    const base = calMonth || new Date();
    calMonth = step === 0 ? new Date() : new Date(base.getFullYear(), base.getMonth() + step, 1);
    const wrap = host.querySelector(".n-cal");
    wrap.outerHTML = calendar(coll, rows, host);
    wireCalendar(host, coll, rows);
  }));
  host.querySelectorAll(".n-cal-cell[data-date]").forEach(c => c.addEventListener("dblclick", () => createRow(coll, { date: c.dataset.date })));
}

async function createRow(coll, { group, date } = {}) {
  const schema = DBS[coll];
  const id = api.newId();
  let data = { props: {}, body: "", checks: {} };
  if (schema.template) data = Object.assign(data, TEMPLATES[schema.template](date || api.today()));
  else {
    const dateProp = schema.props.find(p => p.type === "date");
    if (dateProp && date) data.props[dateProp.name] = date;
    else if (dateProp && ["Date", "Week Of"].includes(dateProp.name)) data.props[dateProp.name] = api.today();
  }
  schema.props.forEach(p => { if (p.default && data.props[p.name] == null) data.props[p.name] = p.default; });
  if (group && schema.groupBy) data.props[schema.groupBy] = group;
  await api.put(coll, id, data);
  location.hash = `#/db/${coll}/${id}`;
}

/* ---------------- Database page ---------------- */
export async function database(root, coll, viewOverride) {
  if (!(await api.online())) { root.innerHTML = LOCKED; return; }
  const schema = DBS[coll];
  if (!schema) { root.innerHTML = `<div class="empty">Database not found.</div>`; return; }
  const rows = await api.list(coll);
  const views = [schema.view, "table"].filter((v, i, a) => a.indexOf(v) === i);
  let view = viewOverride && views.includes(viewOverride) ? viewOverride : schema.view;
  const draw = () => {
    root.innerHTML = `
    <article class="notion full">
      <div class="n-head no-cover"><a class="n-crumb" href="#/">← Dashboard</a><div class="n-page-icon">${esc(schema.icon)}</div><h1 class="n-title">${esc(schema.title)}</h1></div>
      <div class="n-body">
        <div class="n-db-bar"><div class="n-views">${views.map(v => `<button class="${v === view ? "on" : ""}" data-view="${v}">${v[0].toUpperCase() + v.slice(1)}</button>`).join("")}</div><button class="btn" data-new-row>New</button></div>
        <div data-view-host>${view === "board" ? board(coll, rows) : view === "calendar" ? calendar(coll, rows) : table(coll, rows)}</div>
      </div>
    </article>`;
    root.querySelectorAll("[data-view]").forEach(b => b.addEventListener("click", () => { view = b.dataset.view; draw(); }));
    root.querySelector("[data-new-row]").addEventListener("click", () => createRow(coll));
    root.querySelectorAll("[data-new]").forEach(b => b.addEventListener("click", () => createRow(coll, { group: b.dataset.new })));
    if (view === "calendar") wireCalendar(root.querySelector("[data-view-host]"), coll, rows);
  };
  draw();
}

/* ---------------- Row page ---------------- */
function inputFor(p, v) {
  const id = "f-" + p.name.replace(/\W+/g, "-");
  switch (p.type) {
    case "checkbox": return `<input type="checkbox" id="${id}" data-prop="${esc(p.name)}" ${v ? "checked" : ""}>`;
    case "number": case "dollar": return `<input class="n-input" type="number" step="any" id="${id}" data-prop="${esc(p.name)}" value="${v == null ? "" : esc(v)}">`;
    case "date": return `<input class="n-input" type="date" id="${id}" data-prop="${esc(p.name)}" value="${esc(v || "")}">`;
    case "select": case "status": return `<select class="n-input" id="${id}" data-prop="${esc(p.name)}"><option value="">Empty</option>${p.options.map(o => `<option ${o.name === v ? "selected" : ""}>${esc(o.name)}</option>`).join("")}</select>`;
    case "multi": return `<span class="n-multi" data-prop="${esc(p.name)}" data-multi>${p.options.map(o => `<label class="n-tag n-tag-${o.color}"><input type="checkbox" value="${esc(o.name)}" ${(v || []).includes(o.name) ? "checked" : ""}> ${esc(o.name)}</label>`).join("")}</span>`;
    case "formula": return `<span class="n-formula" data-formula="${esc(p.formula)}"></span>`;
    default: return `<textarea class="n-input n-text" rows="1" id="${id}" data-prop="${esc(p.name)}">${esc(v || "")}</textarea>`;
  }
}

export async function row(root, coll, id) {
  if (!(await api.online())) { root.innerHTML = LOCKED; return; }
  const schema = DBS[coll];
  const doc = await api.get(coll, id);
  if (!schema || !doc) { root.innerHTML = `<div class="empty">Entry not found.</div>`; return; }
  const d = doc.data; d.props = d.props || {}; d.checks = d.checks || {};
  const titleProp = schema.props.find(p => p.type === "title").name;
  const save = () => debounce("row-" + id, () => api.put(coll, id, d).then(() => {}).catch(() => toast("Couldn't save.")));
  root.innerHTML = `
  <article class="notion">
    <div class="n-head no-cover"><a class="n-crumb" href="#/db/${coll}">← ${esc(schema.title)}</a>
      <input class="n-title n-title-input" value="${esc(d.props[titleProp] || "")}" placeholder="Untitled" aria-label="Title" data-title>
    </div>
    <div class="n-body">
      <div class="n-props">${schema.props.filter(p => p.type !== "title").map(p => `<label class="n-prop"><span class="n-prop-name">${esc(p.name)}</span><span class="n-prop-val">${inputFor(p, d.props[p.name])}</span></label>`).join("")}</div>
      <hr class="n-hr">
      <div class="n-row-tools"><button class="btn ghost" data-edit>Edit page</button><button class="btn ghost" data-delete>Delete</button></div>
      <div data-content></div>
    </div>
  </article>`;
  const refreshFormulas = () => root.querySelectorAll("[data-formula]").forEach(el => { el.textContent = FORMULAS[el.dataset.formula](d.props); });
  refreshFormulas();
  root.querySelector("[data-title]").addEventListener("input", e => { d.props[titleProp] = e.target.value; save(); });
  root.querySelectorAll("[data-prop]").forEach(el => {
    const name = el.dataset.prop, p = schema.props.find(x => x.name === name);
    if (el.dataset.multi != null) {
      el.addEventListener("change", () => { d.props[name] = [...el.querySelectorAll("input:checked")].map(x => x.value); save(); });
      return;
    }
    const handler = () => {
      if (p.type === "checkbox") d.props[name] = el.checked;
      else if (p.type === "number" || p.type === "dollar") d.props[name] = el.value === "" ? null : Number(el.value);
      else d.props[name] = el.value;
      refreshFormulas(); save();
    };
    el.addEventListener(p.type === "checkbox" || p.type === "select" || p.type === "status" || p.type === "date" ? "change" : "input", handler);
    if (el.tagName === "TEXTAREA") { const fit = () => { el.style.height = "auto"; el.style.height = el.scrollHeight + "px"; }; fit(); el.addEventListener("input", fit); }
  });
  const content = root.querySelector("[data-content]");
  if (!d.body && schema.template) d.body = TEMPLATES[schema.template](d.props[schema.dateProp] || api.today()).body;
  let editing = false;
  const show = () => {
    if (editing) {
      content.innerHTML = `<textarea class="paste n-editor" aria-label="Page content">${esc(d.body || "")}</textarea><p class="sub">Supports the same formatting as Notion exports: headings (##), lists, - [ ] to-dos, callouts, toggles and tables.</p>`;
      const ta = content.querySelector("textarea");
      ta.addEventListener("input", () => { d.body = ta.value; save(); });
      ta.focus();
    } else {
      content.innerHTML = render(d.body || "", { checks: d.checks });
      bindTodos(content, d.checks, s => { d.checks = s; save(); });
      fillInlineDbs(content);
    }
    root.querySelector("[data-edit]").textContent = editing ? "Done editing" : "Edit page";
  };
  root.querySelector("[data-edit]").addEventListener("click", () => { editing = !editing; show(); });
  const delBtn = root.querySelector("[data-delete]");
  delBtn.addEventListener("click", async () => {
    if (delBtn.dataset.armed) { await api.del(coll, id); toast("Deleted."); location.hash = `#/db/${coll}`; }
    else { delBtn.dataset.armed = "1"; delBtn.textContent = "Tap again to delete"; setTimeout(() => { delBtn.dataset.armed = ""; delBtn.textContent = "Delete"; }, 3000); }
  });
  show();
}

/* ---------------- Notebook (Claude IQ) ---------------- */
export async function notebook(root) { return page(root, "claude-iq"); }

/* Files a finished Lab game or lesson into the Notebook. */
export async function fileToNotebook(entry) {
  if (!(await api.online())) return;
  const subjectMap = { iq: "IQ & Reasoning", math: "Mathematics", vocab: "Vocabulary", writing: "Writing", science: "Science" };
  const props = {
    Entry: entry.title, Date: api.today(),
    Subject: subjectMap[entry.course] || (entry.kind === "iq" ? "IQ & Reasoning" : undefined),
    Type: entry.kind === "lesson" ? (entry.max ? "Lesson" : "Reading") : "Game",
    Score: entry.max ? entry.score : null, "Out Of": entry.max || null,
    "Key lesson": (entry.notes || []).slice(0, 3).join(" · "),
    "My notes": entry.myNotes || ""
  };
  await api.put("notebook", entry.id || api.newId(), { props, body: "" }).catch(() => {});
}
