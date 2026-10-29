// Private API for Azcorra Academy (Cloudflare Pages Function, D1 binding "DB").
// Every request must come through Cloudflare Access as ALLOWED_EMAIL,
// except /api/widget, which needs the WIDGET_KEY header instead.
//
// Routes:
//   GET    /api/me                      → { email }
//   GET    /api/docs/:collection        → [{ id, data, updated }]
//   GET    /api/docs/:collection/:id    → { id, data, updated } | 404
//   PUT    /api/docs/:collection/:id    → body is the document JSON
//   DELETE /api/docs/:collection/:id
//   GET    /api/widget                  → today's summary for the iPhone widget

const json = (obj, status = 200) => new Response(JSON.stringify(obj), {
  status, headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store" }
});

const SAFE = /^[A-Za-z0-9_.:-]{1,120}$/;

function localDay(tz) {
  const parts = new Intl.DateTimeFormat("en-CA", { timeZone: tz || "America/New_York", year: "numeric", month: "2-digit", day: "2-digit" }).format(new Date());
  return parts; // YYYY-MM-DD
}

async function widget(env) {
  const today = localDay(env.TIMEZONE);
  const dash = await env.DB.prepare("SELECT data FROM docs WHERE collection='dashboard' AND id='main'").first();
  const checks = await env.DB.prepare("SELECT data FROM docs WHERE collection='checks' AND id=?").bind("dashboard-" + today).first();
  const prog = await env.DB.prepare("SELECT data FROM docs WHERE collection='app' AND id='progress'").first();
  let total = 0, done = 0, next = null;
  if (dash) {
    const body = JSON.parse(dash.data).body || "";
    const state = checks ? JSON.parse(checks.data).state || {} : {};
    const todos = [...body.matchAll(/^(?:- \[( |x)\] (.*)|<todo checked="(true|false)"[^>]*>\s*$)/gm)];
    total = todos.length;
    todos.forEach((m, i) => { const on = state[i] != null ? state[i] : false; if (on) done++; });
    const lines = body.split("\n");
    let idx = -1;
    for (let k = 0; k < lines.length && !next; k++) {
      const l = lines[k];
      const plain = /^- \[( |x)\] (.*)$/.exec(l);
      const tag = /^<todo checked="(true|false)"/.exec(l);
      if (plain || tag) {
        idx++;
        if (!state[idx]) next = (plain ? plain[2] : (lines[k + 1] || "")).replace(/<[^>]+>/g, "").replace(/\\/g, "").trim();
      }
    }
  }
  let streak = 0, sessions = 0;
  if (prog) {
    const p = JSON.parse(prog.data);
    sessions = (p.sessions || []).length;
    const days = new Set((p.sessions || []).map(s => new Intl.DateTimeFormat("en-CA", { timeZone: env.TIMEZONE || "America/New_York" }).format(new Date(s.at))));
    const d = new Date();
    const fmt = x => new Intl.DateTimeFormat("en-CA", { timeZone: env.TIMEZONE || "America/New_York" }).format(x);
    if (!days.has(fmt(d))) d.setDate(d.getDate() - 1);
    while (days.has(fmt(d))) { streak++; d.setDate(d.getDate() - 1); }
  }
  return json({ date: today, blueprint: { done, total, next }, streak, sessions });
}

export async function onRequest({ request, env, params }) {
  const url = new URL(request.url);
  const path = (params.path || []).map(decodeURIComponent);

  if (path[0] === "widget") {
    const key = request.headers.get("x-widget-key") || "";
    if (!env.WIDGET_KEY || key !== env.WIDGET_KEY) return json({ error: "Not allowed." }, 401);
    return widget(env);
  }

  const email = (request.headers.get("cf-access-authenticated-user-email") || "").toLowerCase();
  const allowed = (env.ALLOWED_EMAIL || "").toLowerCase();
  if (!allowed || email !== allowed) return json({ error: "Sign in required." }, 401);
  if (!env.DB) return json({ error: "Database not connected." }, 500);

  if (path[0] === "me") return json({ email });

  if (path[0] !== "docs" || !path[1] || !SAFE.test(path[1]) || (path[2] && !SAFE.test(path[2]))) return json({ error: "Not found." }, 404);
  const collection = path[1], id = path[2];

  if (request.method === "GET" && !id) {
    const { results } = await env.DB.prepare("SELECT id, data, updated FROM docs WHERE collection=? ORDER BY id").bind(collection).all();
    return json(results.map(r => ({ id: r.id, data: JSON.parse(r.data), updated: r.updated })));
  }
  if (request.method === "GET") {
    const row = await env.DB.prepare("SELECT id, data, updated FROM docs WHERE collection=? AND id=?").bind(collection, id).first();
    return row ? json({ id: row.id, data: JSON.parse(row.data), updated: row.updated }) : json({ error: "Not found." }, 404);
  }
  if (request.method === "PUT" && id) {
    let body;
    try { body = await request.json(); } catch (e) { return json({ error: "Body must be JSON." }, 400); }
    if (!body || typeof body !== "object" || Array.isArray(body)) return json({ error: "Body must be a JSON object." }, 400);
    const text = JSON.stringify(body);
    if (text.length > 900000) return json({ error: "Document too large." }, 413);
    const updated = new Date().toISOString();
    await env.DB.prepare("INSERT INTO docs (collection, id, data, updated) VALUES (?, ?, ?, ?) ON CONFLICT(collection, id) DO UPDATE SET data=excluded.data, updated=excluded.updated")
      .bind(collection, id, text, updated).run();
    return json({ ok: true, updated });
  }
  if (request.method === "DELETE" && id) {
    await env.DB.prepare("DELETE FROM docs WHERE collection=? AND id=?").bind(collection, id).run();
    return json({ ok: true });
  }
  return json({ error: "Method not allowed." }, 405);
}
