// Renders Notion-flavored Markdown (as exported from Notion) to HTML, keeping Notion's layout:
// callouts, columns, toggles, colored text and backgrounds, to-dos, tables, code, embeds,
// page links and database blocks.
import { esc } from "../ui.js";

const PAGE_LINKS = {};      // notion page url → app route
const DB_LINKS = {};        // notion data-source/database url → collection id
export function registerLinks(pages, dbs) { Object.assign(PAGE_LINKS, pages); Object.assign(DB_LINKS, dbs); }

/* ---------- inline ---------- */
export function inline(src) {
  const keep = [];
  let s = String(src || "").replace(/\\([\\`*_{}\[\]()#+\-.!$~|<>])/g, (_, c) => { keep.push(c); return "\u0000" + (keep.length - 1) + "\u0000"; });
  s = esc(s);
  // allowed Notion inline tags
  s = s.replace(/&lt;(\/?)(b|i|s|u|code|strong|em)&gt;/g, "<$1$2>");
  s = s.replace(/&lt;span color=&quot;([a-z_]+)&quot;&gt;/g, '<span class="n-$1">').replace(/&lt;\/span&gt;/g, "</span>");
  s = s.replace(/&lt;br\s*\/?&gt;/g, "<br>");
  s = s.replace(/&lt;mention[^&]*&gt;(.*?)&lt;\/mention&gt;/g, "$1");
  // markdown inline
  s = s.replace(/`([^`]+)`/g, "<code>$1</code>");
  s = s.replace(/\*\*([^*]+)\*\*/g, "<b>$1</b>");
  s = s.replace(/(^|[^*])\*([^*\s][^*]*)\*/g, "$1<i>$2</i>");
  s = s.replace(/~~([^~]+)~~/g, "<s>$1</s>");
  s = s.replace(/\[([^\]]+)\]\(([^)\s]+)\)/g, (m, t, u) => {
    const url = u.replace(/&amp;/g, "&");
    if (PAGE_LINKS[url]) return `<a href="${PAGE_LINKS[url]}">${t}</a>`;
    if (/^(https?:|#|mailto:)/.test(url)) return `<a href="${esc(url)}"${/^https?:/.test(url) ? ' target="_blank" rel="noopener"' : ""}>${t}</a>`;
    return t;
  });
  s = s.replace(/\u0000(\d+)\u0000/g, (_, n) => esc(keep[Number(n)]));
  return s;
}

const attr = (tag, name) => { const m = new RegExp(name + '="([^"]*)"').exec(tag); return m ? m[1] : null; };

function iconHtml(icon) {
  if (!icon) return "";
  if (icon.startsWith("/icons/")) return `<img class="n-icon" src="https://www.notion.so${esc(icon)}" alt="" onerror="this.style.display='none'">`;
  if (/^https?:/.test(icon)) return `<img class="n-icon" src="${esc(icon)}" alt="">`;
  return `<span class="n-emoji">${esc(icon)}</span>`;
}

/* ---------- block parser ---------- */
const BLOCK_TAGS = ["callout", "columns", "column", "toggle", "quote", "p", "todo", "table", "details", "synced-block"];

function findClose(lines, start, tag) {
  let depth = 0;
  const open = new RegExp(`^\\s*<${tag}(\\s[^>]*)?>\\s*$`), close = new RegExp(`^\\s*</${tag}>\\s*$`);
  for (let j = start; j < lines.length; j++) {
    if (open.test(lines[j])) depth++;
    if (close.test(lines[j])) { depth--; if (depth === 0) return j; }
  }
  return lines.length - 1;
}

export function render(md, ctx = {}) {
  ctx.todo = ctx.todo || { n: 0 };
  return blocks(String(md || "").replace(/\r/g, "").split("\n"), ctx);
}

function blocks(lines, ctx) {
  const out = [];
  let i = 0;
  while (i < lines.length) {
    const line = lines[i];
    const t = line.trim();
    if (!t) { i++; continue; }

    // self-closing / single-line tags
    if (/^<p\s*\/>$/.test(t)) { out.push('<div class="n-spacer"></div>'); i++; continue; }
    if (/^<embed\s/.test(t)) { out.push(embed(attr(t, "source"))); i++; continue; }
    if (/^<table-of-contents/.test(t)) { out.push('<div class="n-toc" data-toc></div>'); i++; continue; }
    if (/^<(image|bookmark|video|file|pdf)\s/.test(t)) {
      const src = attr(t, "source"); const tagName = t.match(/^<(\w+)/)[1];
      out.push(tagName === "image" ? `<img class="n-img" src="${esc(src)}" alt="">` : `<a class="n-bookmark" href="${esc(src)}" target="_blank" rel="noopener">${esc(src)}</a>`);
      i++; continue;
    }

    // page link
    if (/^<page\s/.test(t)) {
      const end = t.includes("</page>") ? i : lines.findIndex((l, k) => k > i && l.trim() === "</page>");
      const block = lines.slice(i, end + 1).join("\n");
      const url = attr(t, "url");
      const title = block.replace(/<page[^>]*>/, "").replace("</page>", "").trim();
      const href = PAGE_LINKS[url] || null;
      out.push(href ? `<a class="n-page" href="${href}">${inline(title)}</a>` : `<span class="n-page">${inline(title)}</span>`);
      i = end + 1; continue;
    }
    // database
    if (/^<database\s/.test(t)) {
      const end = t.includes("</database>") ? i : lines.findIndex((l, k) => k > i && l.trim() === "</database>");
      const block = lines.slice(i, end + 1).join("\n");
      const title = block.replace(/<database[^>]*>/, "").replace("</database>", "").trim();
      const coll = attr(t, "collection") || DB_LINKS[attr(t, "data-source-url")] || DB_LINKS[attr(t, "url")];
      const isInline = attr(t, "inline") === "true";
      const filter = attr(t, "filter");
      if (coll && isInline) out.push(`<div class="n-db-inline" data-db="${esc(coll)}"${filter ? ` data-filter="${esc(filter)}"` : ""} data-title="${esc(title)}"></div>`);
      else if (coll) out.push(`<a class="n-page n-dblink" href="#/db/${esc(coll)}">${inline(title)}</a>`);
      else out.push(`<span class="n-page">${inline(title)}</span>`);
      i = end + 1; continue;
    }

    // container tags
    const open = /^<([a-z-]+)(\s[^>]*)?>(.*)$/.exec(t);
    if (open && BLOCK_TAGS.includes(open[1]) && !t.endsWith("/>")) {
      const tag = open[1], tagLine = t;
      // single-line form <p color="x">text</p>
      if (new RegExp(`</${tag}>$`).test(t) && !(open[3] === "")) {
        const innerText = t.replace(/^<[^>]+>/, "").replace(new RegExp(`</${tag}>$`), "");
        out.push(container(tag, tagLine, [innerText], ctx));
        i++; continue;
      }
      const end = findClose(lines, i, tag);
      out.push(container(tag, tagLine, lines.slice(i + 1, end), ctx));
      i = end + 1; continue;
    }

    // code fence
    const fence = /^(`{3,})(\w*)/.exec(t);
    if (fence) {
      const buf = []; i++;
      while (i < lines.length && lines[i].trim() !== fence[1]) { buf.push(lines[i]); i++; }
      i++;
      out.push(`<pre class="n-code"><code>${esc(buf.join("\n"))}</code></pre>`);
      continue;
    }
    // headings
    const h = /^(#{1,4})\s+(.*)$/.exec(t);
    if (h) { const lvl = Math.min(4, h[1].length + 1); out.push(`<h${lvl} class="n-h">${inline(h[2])}</h${lvl}>`); i++; continue; }
    if (/^(---|\*\*\*)$/.test(t)) { out.push('<hr class="n-hr">'); i++; continue; }
    // pipe tables
    if (/^\|/.test(t)) {
      const rows = [];
      while (i < lines.length && /^\|/.test(lines[i].trim())) { rows.push(lines[i].trim()); i++; }
      const cells = r => r.replace(/^\||\|$/g, "").split(/(?<!\\)\|/).map(c => c.trim());
      const body = rows.filter(r => !/^\|[\s:|-]+\|$/.test(r));
      out.push(`<div class="n-table-wrap"><table class="n-table"><thead><tr>${cells(body[0]).map(c => `<th>${inline(c)}</th>`).join("")}</tr></thead><tbody>${body.slice(1).map(r => `<tr>${cells(r).map(c => `<td>${inline(c)}</td>`).join("")}</tr>`).join("")}</tbody></table></div>`);
      continue;
    }
    // lists (bulleted, numbered, to-do)
    if (/^(- \[( |x)\] |- |\* |\d+\. )/.test(t)) {
      const items = [];
      let kind = null;
      while (i < lines.length) {
        const l = lines[i].trim();
        const todo = /^- \[( |x)\] (.*)$/.exec(l);
        const num = /^\d+\. (.*)$/.exec(l);
        const bul = /^[-*] (.*)$/.exec(l);
        const k = todo ? "todo" : num ? "ol" : bul ? "ul" : null;
        if (!k || (kind && k !== kind)) break;
        kind = k;
        if (todo) items.push(todoHtml(ctx, todo[1] === "x", inline(todo[2]), null));
        else items.push(`<li>${inline((num || bul)[1])}</li>`);
        i++;
      }
      out.push(kind === "todo" ? `<div class="n-todos">${items.join("")}</div>` : kind === "ol" ? `<ol class="n-list">${items.join("")}</ol>` : `<ul class="n-list">${items.join("")}</ul>`);
      continue;
    }
    // paragraph
    const buf = [];
    while (i < lines.length && lines[i].trim() && !/^(<|#{1,4}\s|```|- |\* |\d+\. |\||---$)/.test(lines[i].trim())) { buf.push(lines[i].trim()); i++; }
    if (!buf.length) { buf.push(lines[i].trim()); i++; }
    out.push(`<p class="n-p">${buf.map(inline).join("<br>")}</p>`);
  }
  return out.join("\n");
}

function todoHtml(ctx, checkedDefault, labelHtml, color) {
  const n = ctx.todo.n++;
  const state = ctx.checks && ctx.checks[n] != null ? ctx.checks[n] : checkedDefault;
  return `<label class="n-todo${state ? " done" : ""}${color ? " n-" + color : ""}"><input type="checkbox" data-todo="${n}"${state ? " checked" : ""}${ctx.readonly ? " disabled" : ""}><span>${labelHtml}</span></label>`;
}

function container(tag, tagLine, inner, ctx) {
  const color = attr(tagLine, "color");
  const cls = color ? ` n-${color}` : "";
  switch (tag) {
    case "callout": return `<div class="n-callout${cls}">${iconHtml(attr(tagLine, "icon"))}<div class="n-callout-body">${blocks(inner, ctx)}</div></div>`;
    case "columns": return `<div class="n-cols">${blocks(inner, ctx)}</div>`;
    case "column": { const r = attr(tagLine, "ratio"); return `<div class="n-col"${r ? ` style="flex:${parseFloat(r)} 1 0"` : ""}>${blocks(inner, ctx)}</div>`; }
    case "quote": return `<blockquote class="n-quote${cls}">${blocks(inner, ctx)}</blockquote>`;
    case "p": return `<p class="n-p${cls}">${inner.map(l => inline(l.trim())).filter(Boolean).join("<br>")}</p>`;
    case "todo": {
      const checked = attr(tagLine, "checked") === "true";
      const label = inner.map(l => l.trim()).filter(Boolean).map(inline).join(" ");
      return `<div class="n-todos">${todoHtml(ctx, checked, label, color)}</div>`;
    }
    case "toggle": case "details": {
      const heading = attr(tagLine, "heading");
      let k = 0; while (k < inner.length && !inner[k].trim()) k++;
      const summary = inline((inner[k] || "").trim());
      const body = blocks(inner.slice(k + 1), ctx);
      const hcls = heading ? ` n-toggle-${heading}` : "";
      return `<details class="n-toggle${cls}${hcls}"><summary>${summary}</summary><div class="n-toggle-body">${body}</div></details>`;
    }
    case "table": {
      const text = inner.join("\n");
      const headerRow = attr(tagLine, "header-row") === "true", headerCol = attr(tagLine, "header-column") === "true";
      const rows = [...text.matchAll(/<tr([^>]*)>([\s\S]*?)<\/tr>/g)];
      const html = rows.map((r, ri) => {
        const rc = attr(r[1], "color");
        const tds = [...r[2].matchAll(/<td([^>]*)>([\s\S]*?)<\/td>|<td([^>]*)><\/td>/g)];
        return `<tr${rc ? ` class="n-${rc}"` : ""}>${tds.map((c, ci) => {
          const content = (c[2] || "").split("\n").map(x => x.trim()).filter(Boolean).map(inline).join("<br>");
          const cc = attr(c[1] || c[3] || "", "color");
          const isHead = (headerRow && ri === 0) || (headerCol && ci === 0);
          const el = isHead ? "th" : "td";
          return `<${el}${cc ? ` class="n-${cc}"` : ""}>${content}</${el}>`;
        }).join("")}</tr>`;
      }).join("");
      return `<div class="n-table-wrap"><table class="n-table n-table-styled">${html}</table></div>`;
    }
    default: return blocks(inner, ctx);
  }
}

function embed(src) {
  if (!src) return "";
  const h = /clock/.test(src) ? 150 : /quote/.test(src) ? 210 : /pomodoro/.test(src) ? 330 : 360;
  return `<div class="n-embed"><iframe src="${esc(src)}" height="${h}" loading="lazy" title="Widget" referrerpolicy="no-referrer"></iframe></div>`;
}

/* Wires up to-do checkboxes inside a rendered root. onChange(stateMap) is called on every toggle. */
export function bindTodos(root, initial, onChange) {
  const state = Object.assign({}, initial || {});
  root.querySelectorAll("input[data-todo]").forEach(cb => {
    cb.addEventListener("change", () => {
      state[cb.dataset.todo] = cb.checked;
      cb.closest(".n-todo").classList.toggle("done", cb.checked);
      onChange(state);
    });
  });
  return state;
}

/* Builds the table of contents for a rendered page. */
export function buildToc(root) {
  const toc = root.querySelector("[data-toc]");
  if (!toc) return;
  const hs = [...root.querySelectorAll(".n-h")];
  toc.innerHTML = hs.map((h, k) => { h.id = h.id || "h" + k; return `<a href="#" data-jump="${h.id}" class="lvl-${h.tagName.toLowerCase()}">${h.textContent}</a>`; }).join("");
  toc.querySelectorAll("[data-jump]").forEach(a => a.addEventListener("click", e => { e.preventDefault(); document.getElementById(a.dataset.jump).scrollIntoView({ behavior: "smooth" }); }));
}
