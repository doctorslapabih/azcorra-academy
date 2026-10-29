// Local progress store. Everything lives in this browser's localStorage.
const KEY = "azcorra.academy.v1";

function blank() {
  return { sessions: [], levels: {}, best: {}, lessons: {}, created: new Date().toISOString() };
}

function load() {
  try {
    const raw = localStorage.getItem(KEY);
    if (!raw) return blank();
    return Object.assign(blank(), JSON.parse(raw));
  } catch (e) {
    return blank();
  }
}

let state = load();

let remote = null;          // { put(data) } once the private API is reachable
let pushTimer = null;
const listeners = [];

export function save() {
  try { localStorage.setItem(KEY, JSON.stringify(state)); } catch (e) { /* storage full or blocked */ }
  if (remote) { clearTimeout(pushTimer); pushTimer = setTimeout(() => remote.put(state).catch(() => {}), 800); }
}

export function onSession(fn) { listeners.push(fn); }

// Merge with the copy saved in the private database, then keep it in sync.
export async function connect(api) {
  let saved = null;
  try { saved = await api.get("app", "progress"); } catch (e) { return false; }
  if (saved && saved.data) {
    const other = Object.assign(blank(), saved.data);
    const ids = new Set(state.sessions.map(x => x.id));
    state.sessions = state.sessions.concat(other.sessions.filter(x => !ids.has(x.id))).sort((a, b) => (a.at < b.at ? 1 : -1));
    for (const k of Object.keys(other.levels)) state.levels[k] = Math.max(state.levels[k] || 1, other.levels[k] || 1);
    for (const k of Object.keys(other.best)) if (!state.best[k] || (other.best[k].norm || 0) > (state.best[k].norm || 0)) state.best[k] = other.best[k];
    for (const k of Object.keys(other.lessons)) {
      const a = state.lessons[k] || {}, b = other.lessons[k] || {};
      state.lessons[k] = Object.assign({}, b, a, { best: Math.max(a.best || 0, b.best || 0), complete: !!(a.complete || b.complete), myNotes: a.myNotes || b.myNotes });
    }
  }
  remote = { put: data => api.put("app", "progress", data) };
  save();
  return true;
}

export function all() { return state; }

export function addSession(s) {
  const rec = Object.assign({ id: Date.now().toString(36) + Math.random().toString(36).slice(2, 6), at: new Date().toISOString() }, s);
  state.sessions.unshift(rec);
  if (s.game) {
    const b = state.best[s.game];
    if (!b || (s.norm || 0) > (b.norm || 0)) state.best[s.game] = { norm: s.norm, score: s.score, max: s.max, at: rec.at };
  }
  save();
  listeners.forEach(fn => { try { fn(rec); } catch (e) { /* ignore */ } });
  return rec;
}

export function level(game, v) {
  if (v !== undefined) { state.levels[game] = v; save(); }
  return state.levels[game] || 1;
}

export function lesson(id, data) {
  if (data) { state.lessons[id] = Object.assign({}, state.lessons[id], data); save(); }
  return state.lessons[id] || null;
}

export function sessionsFor(game) { return state.sessions.filter(s => s.game === game); }

export function exportJSON() { return JSON.stringify(state); }

export function importJSON(text) {
  const obj = JSON.parse(text);
  if (!obj || !Array.isArray(obj.sessions)) throw new Error("That doesn't look like an Azcorra backup.");
  state = Object.assign(blank(), obj);
  save();
}

export function markLogged(ids) {
  const set = new Set(ids);
  state.sessions.forEach(s => { if (set.has(s.id)) s.logged = true; });
  save();
}

export function localDay(when) {
  const x = new Date(when);
  return x.getFullYear() + "-" + String(x.getMonth() + 1).padStart(2, "0") + "-" + String(x.getDate()).padStart(2, "0");
}

export function streak() {
  const days = new Set(state.sessions.map(s => localDay(s.at)));
  const d = new Date();
  if (!days.has(localDay(d))) d.setDate(d.getDate() - 1);
  let n = 0;
  while (days.has(localDay(d))) { n++; d.setDate(d.getDate() - 1); }
  return n;
}
