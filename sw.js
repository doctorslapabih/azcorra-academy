// Offline support: app shell is cached on install; everything else is cached as it's fetched.
const VERSION = "azcorra-v1";
const SHELL = [
  "./", "index.html", "css/app.css", "manifest.webmanifest", "icons/favicon.svg", "icons/icon-192.png",
  "js/app.js", "js/ui.js", "js/store.js", "js/course.js",
  "js/games/index.js", "js/games/common.js", "js/games/banks.js", "js/games/matrix.js", "js/games/series.js",
  "js/games/span.js", "js/games/nback.js", "js/games/speed.js", "js/games/rotation.js", "js/games/analogies.js", "js/games/logic.js",
  "data/courses/index.json", "data/iq/understanding-iq.json"
];
self.addEventListener("install", e => { e.waitUntil(caches.open(VERSION).then(c => c.addAll(SHELL)).then(() => self.skipWaiting())); });
self.addEventListener("activate", e => {
  e.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k !== VERSION).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
// Network first (so new lessons show up), falling back to cache when offline.
self.addEventListener("fetch", e => {
  if (e.request.method !== "GET") return;
  e.respondWith(
    fetch(e.request).then(res => {
      if (res && (res.ok || res.type === "opaque")) { const copy = res.clone(); caches.open(VERSION).then(c => c.put(e.request, copy)); }
      return res;
    }).catch(() => caches.match(e.request).then(r => r || caches.match("index.html")))
  );
});
