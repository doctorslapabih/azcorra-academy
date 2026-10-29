// Client for the private API. Everything degrades gracefully when the API isn't reachable
// (for example on the public GitHub copy of the site): `online()` resolves false.
let status = null; // null = unknown, true/false after the first check

async function call(method, path, body) {
  const res = await fetch("api/" + path, {
    method,
    headers: body ? { "content-type": "application/json" } : {},
    body: body ? JSON.stringify(body) : undefined,
    credentials: "same-origin",
    cache: "no-store"
  });
  if (res.status === 404 && method === "GET") return null;
  const type = res.headers.get("content-type") || "";
  if (!res.ok || !type.includes("application/json")) throw new Error("api " + res.status);
  return res.json();
}

export async function online() {
  if (status !== null) return status;
  try { const me = await call("GET", "me"); status = !!(me && me.email); }
  catch (e) { status = false; }
  return status;
}

export const list = c => call("GET", `docs/${encodeURIComponent(c)}`).then(r => r || []);
export const get = (c, id) => call("GET", `docs/${encodeURIComponent(c)}/${encodeURIComponent(id)}`);
export const put = (c, id, data) => call("PUT", `docs/${encodeURIComponent(c)}/${encodeURIComponent(id)}`, data);
export const del = (c, id) => call("DELETE", `docs/${encodeURIComponent(c)}/${encodeURIComponent(id)}`);

export function newId() {
  return Date.now().toString(36) + Math.random().toString(36).slice(2, 7);
}

export function today() {
  const d = new Date();
  return d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0");
}
