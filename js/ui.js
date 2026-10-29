// Small shared helpers.
export function esc(s) {
  return String(s == null ? "" : s).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}

export const rand = (a, b) => a + Math.floor(Math.random() * (b - a + 1));
export const pick = arr => arr[Math.floor(Math.random() * arr.length)];
export function shuffle(arr) {
  const a = arr.slice();
  for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; }
  return a;
}
export const sleep = ms => new Promise(r => setTimeout(r, ms));

export function pct(a, b) { return b ? Math.round((a / b) * 100) : 0; }

export function fmtDate(iso) {
  try { return new Date(iso).toLocaleDateString(undefined, { month: "short", day: "numeric" }); } catch (e) { return ""; }
}

let toastTimer;
export function toast(msg) {
  let t = document.querySelector(".toast");
  if (!t) { t = document.createElement("div"); t.className = "toast"; t.setAttribute("role", "status"); document.body.appendChild(t); }
  t.textContent = msg; t.hidden = false;
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => { t.hidden = true; }, 2600);
}

export async function copyText(text) {
  try { await navigator.clipboard.writeText(text); return true; }
  catch (e) {
    const ta = document.createElement("textarea");
    ta.value = text; ta.style.position = "fixed"; ta.style.opacity = "0";
    document.body.appendChild(ta); ta.select();
    let ok = false; try { ok = document.execCommand("copy"); } catch (e2) { ok = false; }
    ta.remove(); return ok;
  }
}

export function spark(values) {
  if (!values.length) return "";
  const w = 200, h = 40, pad = 4;
  const max = 100, min = 0;
  const step = values.length > 1 ? (w - pad * 2) / (values.length - 1) : 0;
  const pts = values.map((v, i) => [pad + i * step, h - pad - ((v - min) / (max - min)) * (h - pad * 2)]);
  const d = pts.map((p, i) => (i ? "L" : "M") + p[0].toFixed(1) + " " + p[1].toFixed(1)).join(" ");
  const last = pts[pts.length - 1];
  return `<svg class="spark" viewBox="0 0 ${w} ${h}" preserveAspectRatio="none" aria-hidden="true"><path d="${d}"/><circle cx="${last[0].toFixed(1)}" cy="${last[1].toFixed(1)}" r="3"/></svg>`;
}

// Minimal markdown: headings (##, ###), paragraphs, lists, blockquote, tables, **bold**, *italic*, `code`, [links](url). Math in $...$ is left for KaTeX.
function inline(s) {
  let out = esc(s);
  out = out.replace(/`([^`]+)`/g, "<code>$1</code>");
  out = out.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
  out = out.replace(/(^|[^*])\*([^*\s][^*]*)\*/g, "$1<em>$2</em>");
  out = out.replace(/\[([^\]]+)\]\((https?:[^)\s]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>');
  return out;
}

export function md(src) {
  const lines = String(src || "").replace(/\r/g, "").split("\n");
  const out = [];
  let i = 0;
  while (i < lines.length) {
    const line = lines[i];
    if (!line.trim()) { i++; continue; }
    if (/^###\s/.test(line)) { out.push("<h3>" + inline(line.slice(4)) + "</h3>"); i++; continue; }
    if (/^##\s/.test(line)) { out.push("<h2>" + inline(line.slice(3)) + "</h2>"); i++; continue; }
    if (/^>\s?/.test(line)) {
      const buf = [];
      while (i < lines.length && /^>\s?/.test(lines[i])) { buf.push(lines[i].replace(/^>\s?/, "")); i++; }
      out.push("<blockquote>" + inline(buf.join(" ")) + "</blockquote>"); continue;
    }
    if (/^\|/.test(line)) {
      const rows = [];
      while (i < lines.length && /^\|/.test(lines[i])) { rows.push(lines[i]); i++; }
      const cells = r => r.replace(/^\||\|$/g, "").split("|").map(c => c.trim());
      const head = cells(rows[0]);
      const body = rows.slice(rows[1] && /^\|[\s:-]+\|/.test(rows[1]) ? 2 : 1);
      out.push('<div class="table-wrap"><table><thead><tr>' + head.map(c => "<th>" + inline(c) + "</th>").join("") + "</tr></thead><tbody>" +
        body.map(r => "<tr>" + cells(r).map(c => "<td>" + inline(c) + "</td>").join("") + "</tr>").join("") + "</tbody></table></div>");
      continue;
    }
    if (/^(-|\d+\.)\s/.test(line)) {
      const ordered = /^\d+\./.test(line);
      const buf = [];
      while (i < lines.length && /^(-|\d+\.)\s/.test(lines[i])) { buf.push(lines[i].replace(/^(-|\d+\.)\s/, "")); i++; }
      out.push((ordered ? "<ol>" : "<ul>") + buf.map(b => "<li>" + inline(b) + "</li>").join("") + (ordered ? "</ol>" : "</ul>"));
      continue;
    }
    const buf = [];
    while (i < lines.length && lines[i].trim() && !/^(#{2,3}\s|>|\||-\s|\d+\.\s)/.test(lines[i])) { buf.push(lines[i]); i++; }
    out.push("<p>" + inline(buf.join(" ")) + "</p>");
  }
  return out.join("\n");
}

export function renderMath(root) {
  const go = () => {
    if (!window.katex) return false;
    root.querySelectorAll(".prose, .example, .prompt, .choice, .feedback, .note-box").forEach(node => {
      const walker = document.createTreeWalker(node, NodeFilter.SHOW_TEXT);
      const texts = [];
      while (walker.nextNode()) { if (walker.currentNode.nodeValue.includes("\\(")) texts.push(walker.currentNode); }
      texts.forEach(t => {
        const parts = t.nodeValue.split(/(\\\([\s\S]+?\\\))/g);
        if (parts.length < 2) return;
        const frag = document.createDocumentFragment();
        parts.forEach(p => {
          if (/^\\\([\s\S]+\\\)$/.test(p)) {
            const span = document.createElement("span");
            try { window.katex.render(p.slice(2, -2), span, { throwOnError: false }); } catch (e) { span.textContent = p; }
            frag.appendChild(span);
          } else frag.appendChild(document.createTextNode(p));
        });
        t.parentNode.replaceChild(frag, t);
      });
    });
    return true;
  };
  if (!go()) window.addEventListener("load", go, { once: true });
}
