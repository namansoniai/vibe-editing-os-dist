/* Vibe Editing OS renderer: the created-substitute toolkit for third-party moments (E-10, structure §12.5 / §19).
   Classic script, loaded by player.html after fx.js. Claude never fetches anyone else's media: when the creator has no
   clip or screenshot for a moment, these factories build a clean visual from the script's own words.

     VEOS.fx.quoteCard     a post / quote read aloud: generic, unbranded post card (no platform logo), verbatim quote,
                           words reveal, optional highlight wipe
     VEOS.fx.headlineCard  a news headline: outlet name SET IN TYPE (never a fetched masthead), date, the exact headline,
                           Dhruv-style highlight bars wiping word by word, decorative body lines
     VEOS.fx.appUI         a recreated, generic app screen: terminal (typed lines), list (rows + checks), chat, settings
                           (toggles), browser, video (player frame for another creator's clip)
     VEOS.fx.logoPlate     a product / company / event: the name set in type on a neutral plate with a monogram tile
                           (never a fetched logo)
     VEOS.fx.silhouette    a person: a generic silhouette in a portrait disc + name / role plate
     VEOS.fx.citationStrip evidence card: SOURCE strip (masthead · date) over the creator's own screenshot (asset) with
                           highlight boxes, or over a created headline; optional credit line
     VEOS.fx.shot          the creator's own screenshot / clip framed as a premium card (window chrome optional, slow
                           push, highlight boxes, optional credit line); origin creator
     VEOS.fx.creditLine    a standalone credit line ("• SOURCE: …", TC-legal) for a span (optional; nothing requires a credit)

   Every factory registers a normal VEOS.scene and fills its metadata honestly for the validator: box, text,
   text_content, text_px, text_class, events, and the insert fields V-INSERTS / V-CITE read:
     insert (the plan/inserts.json id), recipe, origin (created | creator), label (only when you pass one), synthetic,
     quote_text (the verbatim words shown), credit, asset, source {masthead, date, headline, highlight_spans}.
   Text never comes from anywhere but the options you pass: quote only the script / transcript, verbatim (NC-13).
   Made-up cards carry no label by default and nothing needs a credit line (Naman, 8 Oct 2026); `label` / `credit`
   draw one only when you pass it.
   Pure functions of the frame; colours are playbook roles (or neutral hex); fonts are playbook slots. */
(function () {
"use strict";
const VEOS = window.VEOS;
if (!VEOS) return;
const fx = VEOS.fx = VEOS.fx || {};
const FPS = 30;
const cl = (x, a = 0, b = 1) => (x < a ? a : x > b ? b : x);
const lerp = (a, b, p) => a + (b - a) * p;
const r2 = v => Math.round(v * 100) / 100;
const esc = s => String(s == null ? "" : s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
const eOut = p => 1 - Math.pow(1 - cl(p), 3);
const eIO = p => { p = cl(p); return p < 0.5 ? 4 * p * p * p : 1 - Math.pow(-2 * p + 2, 3) / 2; };
const back = (p, s = 1.5) => { p = cl(p); const c = s + 1, q = p - 1; return 1 + c * q * q * q + s * q * q; };
const RECON = new Set(["quote_card", "headline_card", "recreated_ui", "silhouette", "citation_strip"]);

/* ------------------------------------------------------------------ colour */
const C = (ctx, v, d) => { const x = v == null ? d : v; return (ctx.tokens.colours && ctx.tokens.colours[x]) || x; };
function rgb(h) { h = String(h).replace("#", ""); if (h.length === 3) h = h.split("").map(c => c + c).join(""); return [0, 2, 4].map(i => parseInt(h.slice(i, i + 2), 16) || 0); }
const hex = a => "#" + a.map(v => Math.max(0, Math.min(255, Math.round(v))).toString(16).padStart(2, "0")).join("");
const mixH = (a, b, p) => { const x = rgb(a), y = rgb(b); return hex(x.map((v, i) => lerp(v, y[i], p))); };
function lum(h) { return rgb(h).map(v => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); }).reduce((s, v, i) => s + v * [0.2126, 0.7152, 0.0722][i], 0); }
const contrast = (a, b) => { const x = lum(a), y = lum(b); return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05); };
/* a highlight bar colour from a role and the text colour on it, darkened until the pair reads at >= 4.6:1 */
function barPair(ctx, role) {
  let bar = /^#/.test(C(ctx, role)) ? C(ctx, role) : "#E0201F";
  for (let k = 0; k < 12; k++) {
    const w = contrast(bar, "#ffffff"), b = contrast(bar, "#0b0b0b");
    if (w >= 4.6) return [bar, "#ffffff"];
    if (b >= 7 && k === 0) return [bar, "#0b0b0b"];
    bar = mixH(bar, "#000000", 0.1);
  }
  return [bar, "#ffffff"];
}
const RGBA = (h, a) => { const q = rgb(h); return `rgba(${q[0]},${q[1]},${q[2]},${a})`; };

/* ------------------------------------------------------------------ shared pieces */
const THEME = {
  light: { card: "#FFFFFF", ink: "#121214", sub: "#4A4A52", line: "rgba(18,18,20,.10)", skel: "rgba(18,18,20,.09)", tag: "#55555E", shadow: "0 30px 80px rgba(0,0,0,.28),0 6px 18px rgba(0,0,0,.12)" },
  paper: { card: "#FBF8F1", ink: "#16130F", sub: "#4D463C", line: "rgba(22,19,15,.14)", skel: "rgba(22,19,15,.10)", tag: "#5A5246", shadow: "0 30px 80px rgba(0,0,0,.30),0 6px 18px rgba(0,0,0,.12)" },
  dark: { card: "#141418", ink: "#F4F4F6", sub: "#B9B9C3", line: "rgba(255,255,255,.12)", skel: "rgba(255,255,255,.10)", tag: "#B4B4BE", shadow: "0 30px 90px rgba(0,0,0,.55),0 0 0 1px rgba(255,255,255,.06)" },
};
const theme = o => Object.assign({}, THEME[o.theme || "light"] || THEME.light, o.colors || {});
/* an optional label (only when a scene passes `label`): TC-legal, letter-spaced, quiet but readable */
const labelHTML = (ctx, text, th, style = "") => `<div data-tc="TC-legal" style="font:700 24px/1 ${ctx.fam("mono")};letter-spacing:.16em;color:${th.tag};white-space:nowrap;${style}">${esc(text)}</div>`;
const creditHTML = (ctx, text, col, dot, style = "") => `<div data-tc="TC-legal" style="display:flex;align-items:center;gap:12px;font:600 24px/1.1 ${ctx.fam("display")};letter-spacing:.06em;text-transform:uppercase;color:${col};white-space:nowrap;${style}"><span style="width:10px;height:10px;border-radius:50%;background:${dot};flex:none"></span>${esc(text)}</div>`;
/* card entrance shared by the factories: rise + de-blur over `f` frames, exit fade over the last 6 */
function enter(lt, dur, f = 10, rise = 46) {
  const k = lt * FPS, p = eOut((k + 0.5) / f), q = cl((dur - lt) * FPS / 6);
  return { op: r2(cl(p * 1.4) * q), ty: r2(rise * (1 - p) - 10 * (1 - q)), sc: r2(lerp(0.965, 1, p)), bl: r2(6 * (1 - p)) };
}
const wrapStyle = (e, x, y, w, extra = "") => `position:absolute;left:${x}px;top:${y}px;width:${w}px;opacity:${e.op};transform:translateY(${e.ty}px) scale(${e.sc});transform-origin:50% 0;${e.bl > 0.3 ? `filter:blur(${e.bl}px);` : ""}${extra}`;
function splitWords(text) { return String(text || "").split(/\s+/).filter(Boolean); }
/* greedy word wrap with the real font; returns [[{w, i}]] (i = word index in the text) */
function wrap(ctx, words, font, maxW) {
  const lines = []; let cur = [], cw = 0; const sp = ctx.measure(" ", font);
  words.forEach((w, i) => { const ww = ctx.measure(w, font); if (cur.length && cw + sp + ww > maxW) { lines.push(cur); cur = []; cw = 0; } cw += (cur.length ? sp : 0) + ww; cur.push({ w, i }); });
  if (cur.length) lines.push(cur);
  return lines;
}
/* word indices covered by highlight spans (each span: a phrase that must occur in the text, or {text}) */
function spanIdx(words, spans) {
  const low = words.map(w => w.toLowerCase().replace(/[^\p{L}\p{N}%₹$#@/-]/gu, "")), out = [];
  (spans || []).forEach((s, k) => {
    const t = splitWords(typeof s === "object" ? s.text : s).map(w => w.toLowerCase().replace(/[^\p{L}\p{N}%₹$#@/-]/gu, ""));
    for (let i = 0; i + t.length <= low.length; i++) if (t.every((x, j) => low[i + j] === x)) { out.push({ k, from: i, to: i + t.length - 1 }); break; }
  });
  return out;
}
/* words of a block with optional reveal (word by word from `revealAt`, `wps` words/s) and highlight bars wiping in
   (span k starts at hlAt + k*hlGap; each word of a span 4 frames after the previous, 6-frame wipe) */
function textBlock(ctx, o) {
  const words = splitWords(o.text), font = `${o.weight || 700} ${o.size}px ${o.fam}`, lines = wrap(ctx, words, font, o.maxW);
  const hl = spanIdx(words, o.spans), inSpan = i => hl.find(s => i >= s.from && i <= s.to);
  const [bar, onBar] = o.hlRole ? barPair(ctx, o.hlRole) : ["", ""];
  const k = o.lt * FPS, revF = o.revealAt != null ? o.revealAt * FPS : null, perW = FPS / (o.wps || 9);
  let html = "";
  for (const ln of lines) {
    html += `<div style="white-space:nowrap">`;
    ln.forEach((wd, j) => {
      const s = inSpan(wd.i);
      const op = revF == null ? 1 : cl((k - revF - wd.i * perW) / 4);
      let p = 0;
      if (s) { const st = (o.hlAt || 0) * FPS + s.k * (o.hlGap || 0.5) * FPS + (wd.i - s.from) * 4; p = eIO((k - st) / 6); }
      const col = s && p > 0.55 ? onBar : o.color;
      const pad = Math.round(o.size * 0.12);
      const barEl = s && p > 0 ? `<span style="position:absolute;left:${-pad}px;right:${-pad - (j < ln.length - 1 && inSpan(ln[j + 1].i) === s ? Math.round(o.size * 0.28) : 0)}px;top:${-Math.round(o.size * 0.08)}px;bottom:${-Math.round(o.size * 0.1)}px;background:${bar};border-radius:${Math.round(o.size * 0.08)}px;transform:scaleX(${r2(p)});transform-origin:0 50%;z-index:-1"></span>` : "";
      html += `<span style="position:relative;display:inline-block;color:${col};opacity:${r2(op)}">${barEl}${esc(wd.w)}</span>${j < ln.length - 1 ? " " : ""}`;
    });
    html += `</div>`;
  }
  return { html: `<div style="position:relative;z-index:0;font:${font};line-height:${o.lh || 1.18};letter-spacing:${o.track || 0}em">${html}</div>`, lines: lines.length };
}
function insMeta(o, recipe, origin, extra) {
  const label = o.label || undefined;
  return Object.assign({ insert: o.insert, recipe, origin, label, synthetic: origin === "created" && RECON.has(recipe) ? true : undefined,
    credit: o.credit || undefined, fx: "insert:" + recipe }, extra || {});
}
function reg(o, d) {
  const s = Object.assign({}, d, o.extra || {});
  for (const k of ["id", "t_in", "t_out", "z", "in", "out", "behind", "follow_footage", "parallax", "may_overlap_face", "overlaps", "cuts", "kind", "roles", "figure", "depicts", "illustrative"]) if (o[k] !== undefined) s[k] = o[k];
  if (o.events) s.events = [...new Set([...(s.events || []), ...o.events])].sort((a, b) => a - b);
  for (const k of Object.keys(s)) if (s[k] === undefined) delete s[k];
  return VEOS.scene(s);
}
const evs = (list, dur) => [...new Set(list.map(v => Math.round(v * 1000) / 1000).filter(v => v > 0.05 && v < dur - 0.05))].sort((a, b) => a - b);
const initials = name => { const w = String(name || "?").replace(/[^\p{L}\p{N}\s]/gu, " ").split(/\s+/).filter(Boolean); if (w.length > 1) return (w[0][0] + w[1][0]).toUpperCase(); const m = (w[0] || "?").match(/^(\p{L})\p{L}*?(\d+)?$/u); return m ? (m[1] + (m[2] || "")).toUpperCase().slice(0, 3) : (w[0] || "?")[0].toUpperCase(); };

/* ================================================================ quote / post card */
/* o: {id, t_in, t_out, insert, quote (verbatim script words), name, handle?, meta? (e.g. "post"), x=90, y, w=900,
       theme light|dark, size=54, reveal=true (word by word), wps=9, highlight:[phrases], hlRole='primary', hlAt (local s),
       label (optional), credit?, z=4} */
fx.quoteCard = function (o) {
  const x = o.x != null ? o.x : 90, y = o.y != null ? o.y : 420, w = o.w || 900, size = o.size || 54, pad = 52, dur = o.t_out - o.t_in;
  const qWords = splitWords(o.quote), estLines = Math.ceil(qWords.join(" ").length * size * 0.5 / (w - 2 * pad)) || 1;
  const h = Math.round(pad * 2 + 104 + 30 + estLines * size * 1.24 + 86);
  const revealAt = o.reveal === false ? null : (o.revealAt != null ? o.revealAt : 0.28);
  const hlAt = o.hlAt != null ? o.hlAt : (revealAt != null ? revealAt + qWords.length / (o.wps || 9) + 0.15 : 0.4);
  const label = o.label || null;
  const txt = [o.name, o.handle, o.quote, label, o.credit].filter(Boolean).join(" / ");
  return reg(o, Object.assign({
    id: o.id, t_in: o.t_in, t_out: o.t_out, z: o.z || 4, in: "none", out: "none", text: true, text_content: txt,
    text_px: 24, text_class: o.text_class || "TC-label", box: { x, y, w, h }, roles: o.roles || (o.highlight ? [o.hlRole || "primary"] : []),
    events: evs([revealAt || 0, hlAt], dur), quote_text: String(o.quote || ""),
  }, insMeta(o, "quote_card", "created", { label: label || undefined }), {
    render(ctx, lt) {
      const th = theme(o), e = enter(lt, dur);
      const av = 104, nm = esc(o.name || ""), hd = o.handle ? esc(o.handle) : "";
      const avatar = `<div style="width:${av}px;height:${av}px;border-radius:50%;flex:none;background:linear-gradient(150deg,${th.sub},${mixH(th.sub, dark(th) ? "#ffffff" : "#000000", 0.25)});display:flex;align-items:center;justify-content:center;font:800 40px/1 ${ctx.fam("display")};color:${th.card}">${esc(initials(o.name))}</div>`;
      const body = textBlock(ctx, { text: o.quote, size, fam: ctx.fam(o.font || "display"), weight: 600, maxW: w - 2 * pad, color: th.ink, lt, revealAt, wps: o.wps,
        spans: o.highlight, hlRole: o.highlight ? (o.hlRole || "primary") : null, hlAt, lh: 1.24, track: -0.01 });
      const glyph = `<svg width="44" height="44" viewBox="0 0 48 48" style="flex:none;opacity:.55"><path d="M6 10 H42 V32 H22 L13 40 V32 H6 Z" fill="none" stroke="${th.ink}" stroke-width="3.4" stroke-linejoin="round"/></svg>`;
      return ctx.html(`<div style="${wrapStyle(e, x, y, w, `box-sizing:border-box;padding:${pad}px;border-radius:40px;background:${th.card};box-shadow:${th.shadow}`)}">
        <div style="display:flex;align-items:center;gap:26px">${avatar}<div style="display:flex;flex-direction:column;gap:8px;min-width:0;flex:1">
          <div style="font:800 46px/1.05 ${ctx.fam("display")};color:${th.ink};white-space:nowrap;overflow:hidden">${nm}</div>
          ${hd ? `<div style="font:500 40px/1.05 ${ctx.fam("display")};color:${th.sub};white-space:nowrap">${hd}</div>` : ""}</div>${glyph}</div>
        <div style="height:30px"></div>${body.html}
        <div style="display:flex;justify-content:space-between;align-items:center;margin-top:34px;padding-top:26px;border-top:2px solid ${th.line}">
          ${label ? labelHTML(ctx, label, th) : "<span></span>"}${o.credit ? creditHTML(ctx, o.credit, th.tag, th.tag) : ""}</div></div>`);
    },
  }));
};

/* ================================================================ headline card (news) */
/* o: {id, t_in, t_out, insert, masthead (outlet name, set in type), date, headline (exact), highlight:[phrases],
       hlRole='bad', hlAt (local s, default 0.45), kicker?, x=70, y, w=940, theme paper|light|dark, size=66,
       body=3 (decorative body lines), label, credit, source_url?} */
fx.headlineCard = function (o) {
  const x = o.x != null ? o.x : 70, y = o.y != null ? o.y : 380, w = o.w || 940, size = o.size || 66, pad = 54, dur = o.t_out - o.t_in;
  const hWords = splitWords(o.headline), estLines = Math.ceil(String(o.headline || "").length * size * 0.52 / (w - 2 * pad)) || 1;
  const nBody = o.body != null ? o.body : 3;
  const h = Math.round(pad * 2 + 70 + 34 + estLines * size * 1.22 + (nBody ? 40 + nBody * 34 : 0) + 76);
  const hlAt = o.hlAt != null ? o.hlAt : 0.45, label = o.label || null;
  const spans = (o.highlight || []).map(s => (typeof s === "object" ? s.text : s));
  const txt = [o.masthead, o.date, o.headline, label, o.credit].filter(Boolean).join(" / ");
  return reg(o, Object.assign({
    id: o.id, t_in: o.t_in, t_out: o.t_out, z: o.z || 4, in: "none", out: "none", text: true, text_content: txt,
    text_px: 24, text_class: o.text_class || "TC-label", box: { x, y, w, h }, roles: o.roles || [o.hlRole || "bad"],
    events: evs([hlAt, ...spans.map((_, k) => hlAt + k * 0.5)], dur), quote_text: String(o.headline || ""),
    source: { masthead: o.masthead, date: o.date, headline: o.headline, url: o.source_url, highlight_spans: spans },
  }, insMeta(o, "headline_card", "created", { label: label || undefined }), {
    render(ctx, lt) {
      const th = theme(Object.assign({ theme: "paper" }, o)), e = enter(lt, dur);
      const head = textBlock(ctx, { text: o.headline, size, fam: ctx.fam(o.font || "serif"), weight: o.weight || 400, maxW: w - 2 * pad, color: th.ink, lt,
        spans: o.highlight, hlRole: o.hlRole || "bad", hlAt, hlGap: 0.5, lh: 1.22, track: -0.01 });
      const bodyLines = Array.from({ length: nBody }, (_, i) => `<div style="height:14px;border-radius:7px;background:${th.skel};width:${[96, 88, 72, 90, 64][i % 5]}%"></div>`).join("");
      return ctx.html(`<div style="${wrapStyle(e, x, y, w, `box-sizing:border-box;padding:${pad}px;border-radius:30px;background:${th.card};box-shadow:${th.shadow}`)}">
        <div style="display:flex;align-items:baseline;justify-content:space-between;gap:24px;padding-bottom:22px;border-bottom:3px solid ${th.ink}">
          <div style="font:700 50px/1 ${ctx.fam("serif")};color:${th.ink};letter-spacing:-.01em;white-space:nowrap">${esc(o.masthead || "")}</div>
          <div style="font:600 40px/1 ${ctx.fam("display")};color:${th.sub};white-space:nowrap">${esc(o.date || "")}</div></div>
        ${o.kicker ? `<div style="margin-top:26px;font:800 40px/1 ${ctx.fam("display")};letter-spacing:.08em;text-transform:uppercase;color:${C(ctx, o.hlRole || "bad")}">${esc(o.kicker)}</div>` : ""}
        <div style="height:30px"></div>${head.html}
        ${nBody ? `<div style="display:flex;flex-direction:column;gap:20px;margin-top:38px">${bodyLines}</div>` : ""}
        <div style="display:flex;justify-content:space-between;align-items:center;margin-top:34px">${label ? labelHTML(ctx, label, th) : "<span></span>"}${o.credit ? creditHTML(ctx, o.credit, th.tag, C(ctx, o.hlRole || "bad")) : ""}</div></div>`);
    },
  }));
};

/* ================================================================ recreated generic app UI */
/* o: {id, t_in, t_out, insert, kind terminal|list|chat|settings|browser|video, title (window title, set in type),
       lines: [str | {text, who: me|them, on, icon}], at: [local s per line] (default staggered), x=90, y, w=900, h,
       accent='primary', theme dark|light, size=40, label, credit, caption? (video: the spoken title)} */
fx.appUI = function (o) {
  const kind = o.kind || "terminal", x = o.x != null ? o.x : 90, y = o.y != null ? o.y : 400, w = o.w || 900, dur = o.t_out - o.t_in;
  const size = Math.max(40, o.size || 42), lines = (o.lines || []).map(l => (typeof l === "object" ? l : { text: String(l) }));
  const step = o.step || (kind === "terminal" ? 0.55 : 0.32), at = lines.map((l, i) => (o.at && o.at[i] != null ? o.at[i] : 0.35 + i * step));
  // rows wrap: estimate each row's line count from its length (mono 0.6 em, sans 0.53 em per character)
  const inner = kind === "list" ? w - 80 - size - 32 : kind === "chat" ? (w - 80) * 0.8 - 56 : w - 80, em = kind === "terminal" ? 0.6 : 0.53;
  const nl = l => Math.max(1, Math.ceil((String(l.text).length + (kind === "terminal" ? 2 : 0)) * size * em / inner));
  const rowH = l => kind === "chat" ? nl(l) * size * 1.28 + 62 : kind === "settings" ? size + 56 : nl(l) * size * 1.5 + (kind === "list" ? 22 : 6);
  const h = o.h || Math.round(78 + 40 + (kind === "video" ? Math.round((w - 64) * 9 / 16) + 150 : lines.reduce((a, l) => a + rowH(l), 0) + 30) + 70);
  const label = o.label || null, dark = (o.theme || (kind === "terminal" || kind === "video" ? "dark" : "light")) === "dark";
  const txt = [o.title, ...lines.map(l => l.text), o.caption, label, o.credit].filter(Boolean).join(" / ");
  return reg(o, Object.assign({
    id: o.id, t_in: o.t_in, t_out: o.t_out, z: o.z || 4, in: "none", out: "none", text: true, text_content: txt,
    text_px: 24, text_class: o.text_class || "TC-label", box: { x, y, w, h }, roles: o.roles || [o.accent || "primary"],
    events: evs([...at, ...(kind === "terminal" ? lines.flatMap((l, i) => { const T = String(l.text).length / (o.cps || 34), out = [];
      for (let q = 0.9; q < T; q += 0.9) out.push(at[i] + q); return out; }) : [])], dur),
  }, insMeta(o, "recreated_ui", "created", { label: label || undefined, ui: kind }), {
    render(ctx, lt) {
      const th = theme({ theme: dark ? "dark" : "light" }), e = enter(lt, dur), acc = C(ctx, o.accent || "primary");
      const accOn = contrast(acc, "#0b0b0b") >= 4.6 ? "#0b0b0b" : "#ffffff";
      const ui = ctx.fam(o.font || "display"), mono = ctx.fam("mono"), k = lt * FPS;
      const pIn = i => eOut((k - at[i] * FPS) / 7);
      const dots = `<div style="display:flex;gap:12px">${["#ff5f57", "#febc2e", "#28c840"].map(c => `<span style="width:18px;height:18px;border-radius:50%;background:${c}"></span>`).join("")}</div>`;
      const bar = `<div style="display:flex;align-items:center;gap:22px;padding:0 26px;height:78px;border-bottom:2px solid ${th.line}">${dots}
        <div style="flex:1;text-align:center;font:600 40px/1 ${kind === "terminal" ? mono : ui};color:${th.sub};white-space:nowrap;overflow:hidden">${esc(o.title || "")}</div><span style="width:78px"></span></div>`;
      let body = "";
      if (kind === "terminal") {
        body = lines.map((l, i) => {
          if (k < at[i] * FPS) return "";
          const n = Math.floor((lt - at[i]) * (o.cps || 34)), t = String(l.text), typing = n < t.length, last = i === lines.length - 1 || k < at[i + 1] * FPS;
          const caret = (typing || (last && Math.floor(k / 15) % 2 === 0)) ? `<span style="display:inline-block;width:.55em;height:1.05em;vertical-align:-.15em;background:${acc};margin-left:4px"></span>` : "";
          const pre = l.out ? "" : `<span style="color:${acc}">&gt;</span> `;
          return `<div style="font:500 ${size}px/1.5 ${mono};color:${l.out ? th.sub : th.ink};white-space:pre-wrap;overflow-wrap:anywhere">${pre}${esc(t.slice(0, Math.max(0, n)))}${caret}</div>`;
        }).join("");
      } else if (kind === "list") {
        body = lines.map((l, i) => { const p = pIn(i); if (p <= 0) return ""; const ok = l.on !== false;
          return `<div style="display:flex;align-items:center;gap:24px;padding:11px 0;opacity:${r2(cl(p * 1.5))};transform:translateX(${r2(30 * (1 - p))}px);border-bottom:2px solid ${th.line}">
            <span style="width:${size + 8}px;height:${size + 8}px;border-radius:12px;flex:none;background:${ok ? acc : "transparent"};border:3px solid ${ok ? acc : th.sub};display:flex;align-items:center;justify-content:center">
            ${ok ? `<svg width="${size - 4}" height="${size - 4}" viewBox="0 0 48 48"><path d="M10 25 L19 34 L38 14" fill="none" stroke="${accOn}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="44" stroke-dashoffset="${r2(44 * (1 - eOut((k - at[i] * FPS - 3) / 6)))}"/></svg>` : ""}</span>
            <span style="font:700 ${size}px/1.2 ${ui};color:${th.ink}">${esc(l.text)}</span></div>`; }).join("");
      } else if (kind === "chat") {
        body = `<div style="display:flex;flex-direction:column;gap:22px">` + lines.map((l, i) => { const p = pIn(i); if (p <= 0) return ""; const me = l.who === "me";
          return `<div style="align-self:${me ? "flex-end" : "flex-start"};max-width:80%;padding:20px 28px;border-radius:34px;${me ? `border-bottom-right-radius:10px;background:${acc};color:${accOn}` : `border-bottom-left-radius:10px;background:${dark ? "#26262c" : "#ececf1"};color:${th.ink}`};font:600 ${size}px/1.28 ${ui};opacity:${r2(cl(p * 1.5))};transform:translateY(${r2(24 * (1 - p))}px) scale(${r2(lerp(0.92, 1, p))});transform-origin:${me ? "100% 100%" : "0 100%"}">${esc(l.text)}</div>`; }).join("") + `</div>`;
      } else if (kind === "settings") {
        body = lines.map((l, i) => { const p = pIn(i), on = l.on !== false, sw = on ? eIO((k - at[i] * FPS - 4) / 6) : 0;
          return `<div style="display:flex;align-items:center;justify-content:space-between;padding:12px 0;border-bottom:2px solid ${th.line};opacity:${r2(cl(0.35 + p))}">
            <span style="font:600 ${size}px/1.2 ${ui};color:${th.ink};white-space:nowrap">${esc(l.text)}</span>
            <span style="position:relative;width:96px;height:54px;border-radius:27px;flex:none;background:${sw > 0.5 ? acc : (dark ? "#3a3a42" : "#d6d6dc")}">
              <span style="position:absolute;top:5px;left:${r2(5 + 42 * sw)}px;width:44px;height:44px;border-radius:50%;background:#fff;box-shadow:0 2px 6px rgba(0,0,0,.25)"></span></span></div>`; }).join("");
      } else if (kind === "browser") {
        body = `<div style="display:flex;flex-direction:column;gap:20px">` + lines.map((l, i) => { const p = pIn(i); if (p <= 0) return "";
          return i === 0 ? `<div style="font:800 ${Math.round(size * 1.35)}px/1.1 ${ui};color:${th.ink};opacity:${r2(cl(p * 1.5))}">${esc(l.text)}</div>`
            : `<div style="font:500 ${size}px/1.3 ${ui};color:${th.sub};opacity:${r2(cl(p * 1.5))}">${esc(l.text)}</div>`; }).join("")
          + `<div style="display:flex;gap:18px;margin-top:10px"><div style="height:66px;width:250px;border-radius:33px;background:${acc}"></div><div style="height:66px;width:200px;border-radius:33px;border:3px solid ${th.line}"></div></div></div>`;
      } else { // video: a generic player frame standing in for someone else's clip (never the clip itself)
        const vw = w - 64, vh = Math.round(vw * 9 / 16), pr = cl(lt / Math.max(dur, 0.1));
        body = `<div style="position:relative;width:${vw}px;height:${vh}px;border-radius:22px;overflow:hidden;background:linear-gradient(135deg,#1d1d24,#0d0d12)">
            <div style="position:absolute;inset:0;background:radial-gradient(circle at ${r2(30 + 40 * pr)}% 40%,${RGBA(acc, 0.22)} 0,rgba(0,0,0,0) 55%)"></div>
            <div style="position:absolute;left:50%;top:50%;width:120px;height:120px;margin:-60px 0 0 -60px;border-radius:50%;background:rgba(255,255,255,.14);display:flex;align-items:center;justify-content:center">
              <svg width="56" height="56" viewBox="0 0 48 48"><path d="M16 10 L38 24 L16 38 Z" fill="#fff"/></svg></div>
            <div style="position:absolute;left:24px;right:24px;bottom:22px;height:8px;border-radius:4px;background:rgba(255,255,255,.22)"><div style="width:${r2(pr * 100)}%;height:100%;border-radius:4px;background:${acc}"></div></div></div>
          ${o.caption ? `<div style="margin-top:26px;font:700 ${size}px/1.25 ${ui};color:${th.ink}">${esc(o.caption)}</div>` : ""}`;
      }
      return ctx.html(`<div style="${wrapStyle(e, x, y, w, `height:${h}px;box-sizing:border-box;border-radius:34px;background:${th.card};box-shadow:${th.shadow};overflow:hidden`)}">${bar}
        <div style="padding:${kind === "video" ? "32px" : "34px 40px"};box-sizing:border-box">${body}</div>
        <div style="position:absolute;left:40px;right:40px;bottom:26px;display:flex;justify-content:space-between;align-items:center">${label ? labelHTML(ctx, label, th) : "<span></span>"}${o.credit ? creditHTML(ctx, o.credit, th.tag, acc) : ""}</div></div>`);
    },
  }));
};

/* ================================================================ product / company / event: name set in type */
/* o: {id, t_in, t_out, insert, name, kicker? ("by Y Combinator", from the script), sub?, x=110, y, w=860, theme dark|light,
       accent='concept', monogram (default initials; decorative), size=96, pulses:[local s] (the tile pulses on a word), credit?} */
fx.logoPlate = function (o) {
  const x = o.x != null ? o.x : 110, y = o.y != null ? o.y : 520, w = o.w || 860, size = o.size || 96, dur = o.t_out - o.t_in;
  const h = Math.round(56 * 2 + 200 + (o.sub ? 70 : 0) + (o.credit ? 56 : 0));
  const txt = [o.kicker, o.name, o.sub, o.credit].filter(Boolean).join(" / ");
  return reg(o, Object.assign({
    id: o.id, t_in: o.t_in, t_out: o.t_out, z: o.z || 4, in: "none", out: "none", text: true, text_content: txt,
    text_px: o.credit ? 24 : 40, text_class: o.text_class || "TC-display", box: { x, y, w, h }, roles: o.roles || [o.accent || "concept"],
    events: evs([0.25, 0.55, ...(o.pulses || [])], dur),
  }, insMeta(o, "logo_plate", "created", { label: undefined, name: o.name }), {
    render(ctx, lt) {
      const th = theme({ theme: o.theme || "dark" }), e = enter(lt, dur, 9, 34), acc = C(ctx, o.accent || "concept"), k = lt * FPS;
      const accOn = contrast(acc, "#ffffff") >= 4.6 ? "#ffffff" : "#0b0b0b";
      const pt = back((k - 7) / 10, 1.6), pn = eOut((k - 9) / 12), pu = eIO((k - 16) / 12);
      const pulse = (o.pulses || []).reduce((a, at) => { const q = (k - at * FPS) / 8; return q >= 0 && q <= 1 ? Math.max(a, Math.sin(Math.PI * q)) : a; }, 0);
      const mono = esc(o.monogram || initials(o.name)), tile = 200;
      const fs = Math.min(size, Math.floor((w - tile - 56 * 2 - 44) / Math.max(1, ctx.measure(String(o.name || ""), `800 ${size}px ${ctx.fam("display")}`) / size)));
      return ctx.html(`<div style="${wrapStyle(e, x, y, w, `height:${h}px;box-sizing:border-box;padding:56px;border-radius:44px;background:${th.card};box-shadow:${th.shadow};display:flex;flex-direction:column;justify-content:center`)}">
        <div style="display:flex;align-items:center;gap:44px">
          <div style="width:${tile}px;height:${tile}px;flex:none;border-radius:50px;background:linear-gradient(145deg,${mixH(acc, "#ffffff", 0.12)},${mixH(acc, "#000000", 0.28)});display:flex;align-items:center;justify-content:center;opacity:${r2(cl(pt * 2))};transform:scale(${r2(lerp(0.6, 1, Math.min(pt, 1.2)) * (1 + 0.07 * pulse))});box-shadow:inset 0 2px 0 rgba(255,255,255,.25),0 18px ${r2(40 + 30 * pulse)}px ${RGBA(acc, r2(0.35 + 0.3 * pulse))}">
            <span data-tc="TC-decorative" style="font:900 ${mono.length > 2 ? 64 : 92}px/1 ${ctx.fam("display")};color:${accOn};letter-spacing:-.04em">${mono}</span></div>
          <div style="display:flex;flex-direction:column;gap:14px;min-width:0;opacity:${r2(cl(pn * 1.3))};transform:translateX(${r2(28 * (1 - pn))}px)">
            ${o.kicker ? `<div style="font:700 40px/1 ${ctx.fam("display")};letter-spacing:.06em;text-transform:uppercase;color:${th.sub};white-space:nowrap">${esc(o.kicker)}</div>` : ""}
            <div style="font:800 ${fs}px/1 ${ctx.fam("display")};letter-spacing:-.03em;color:${th.ink};white-space:nowrap">${esc(o.name)}</div>
            <div style="height:8px;border-radius:4px;background:${acc};width:${r2(pu * 100)}%"></div></div></div>
        ${o.sub ? `<div style="margin-top:30px;font:500 44px/1.2 ${ctx.fam("display")};color:${th.sub};opacity:${r2(pu)}">${esc(o.sub)}</div>` : ""}
        ${o.credit ? creditHTML(ctx, o.credit, th.tag, acc, "margin-top:26px") : ""}</div>`);
    },
  }));
};

/* ================================================================ person placeholder: silhouette */
/* o: {id, t_in, t_out, insert, name, role? (from the script), x=190, y, w=700, theme dark|light, accent='data',
       label (optional), credit?} */
const BUST = "M100 34 C121 34 138 52 138 76 C138 100 121 120 100 120 C79 120 62 100 62 76 C62 52 79 34 100 34 Z M24 206 C26 160 58 134 100 134 C142 134 174 160 176 206 Z";
fx.silhouette = function (o) {
  const x = o.x != null ? o.x : 190, y = o.y != null ? o.y : 380, w = o.w || 700, dur = o.t_out - o.t_in, disc = Math.min(w - 160, 440);
  const h = Math.round(60 + disc + 50 + 96 + (o.role ? 60 : 0) + 80);
  const label = o.label || null;
  const txt = [o.name, o.role, label, o.credit].filter(Boolean).join(" / ");
  return reg(o, Object.assign({
    id: o.id, t_in: o.t_in, t_out: o.t_out, z: o.z || 4, in: "none", out: "none", text: true, text_content: txt,
    text_px: 24, text_class: o.text_class || "TC-label", box: { x, y, w, h }, roles: o.roles || [o.accent || "data"],
    events: evs([0.3, 0.6], dur),
  }, insMeta(o, "silhouette", "created", { label: label || undefined, name: o.name }), {
    render(ctx, lt) {
      const th = theme({ theme: o.theme || "dark" }), e = enter(lt, dur), acc = C(ctx, o.accent || "data"), k = lt * FPS;
      const pr = eIO((k - 4) / 16), ps = eOut((k - 8) / 12), pn = eOut((k - 14) / 10);
      const R = disc / 2, circ = 2 * Math.PI * (R - 6);
      const fig = mixH(th.sub, th.card, dark(th) ? 0.15 : 0.1);
      return ctx.html(`<div style="${wrapStyle(e, x, y, w, `height:${h}px;box-sizing:border-box;padding:60px 60px 0;border-radius:48px;background:${th.card};box-shadow:${th.shadow};display:flex;flex-direction:column;align-items:center`)}">
        <div style="position:relative;width:${disc}px;height:${disc}px;flex:none">
          <div style="position:absolute;inset:12px;border-radius:50%;overflow:hidden;background:radial-gradient(circle at 50% 30%,${RGBA(acc, 0.28)} 0,${mixH(th.card, "#000000", dark(th) ? 0.25 : 0.06)} 70%)">
            <svg viewBox="0 0 200 206" width="${disc - 24}" height="${disc - 24}" style="position:absolute;left:0;top:${r2(30 * (1 - ps) + 8)}px;opacity:${r2(cl(ps * 1.4))}">
              <defs><linearGradient id="sg-${esc(o.id)}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${mixH(fig, "#ffffff", 0.25)}"/><stop offset="1" stop-color="${mixH(fig, "#000000", 0.25)}"/></linearGradient></defs>
              <path d="${BUST}" fill="url(#sg-${esc(o.id)})"/></svg></div>
          <svg width="${disc}" height="${disc}" style="position:absolute;inset:0;transform:rotate(-90deg)"><circle cx="${R}" cy="${R}" r="${R - 6}" fill="none" stroke="${acc}" stroke-width="8" stroke-linecap="round" stroke-dasharray="${r2(circ)}" stroke-dashoffset="${r2(circ * (1 - pr))}"/></svg></div>
        <div style="margin-top:44px;text-align:center;opacity:${r2(cl(pn * 1.4))};transform:translateY(${r2(16 * (1 - pn))}px)">
          <div style="font:800 76px/1.05 ${ctx.fam("display")};letter-spacing:-.02em;color:${th.ink};white-space:nowrap">${esc(o.name || "")}</div>
          ${o.role ? `<div style="margin-top:14px;font:600 44px/1.1 ${ctx.fam("display")};color:${acc === th.card ? th.sub : th.sub};white-space:nowrap">${esc(o.role)}</div>` : ""}</div>
        <div style="position:absolute;left:44px;right:44px;bottom:30px;display:flex;justify-content:space-between;align-items:center">${label ? labelHTML(ctx, label, th) : "<span></span>"}${o.credit ? creditHTML(ctx, o.credit, th.tag, acc) : ""}</div></div>`);
    },
  }));
};
const dark = th => lum(th.card) < 0.2;

/* ================================================================ the creator's own screenshot / clip */
/* o: {id, t_in, t_out, insert, asset (plan/assets name, added with --origin creator), x=70, y, w=940, h (default from
       aspect), aspect (w/h of the image, default 16/10; also used for the cover crop, or imageAspect when they differ), chrome (window bar title or false), radius=30, push=[1, 1.06],
       focus=[fx, fy], highlights:[{x, y, w, h (0..1 of the image), at (local s), role}], credit, offset/speed (video)} */
function shotHTML(ctx, o, lt, dur, x, y, w, h, th) {
  // slow push without growing any painted element (the measured rect stays the card): the image is a cover-sized
  // background whose size and position change; highlight boxes are placed in image space and clamped to the window
  const k = lt * FPS, push = o.push || [1, 1.06], f = o.focus || [0.5, 0.5], s = lerp(push[0], push[1], eIO(lt / Math.max(dur, 0.1)));
  const src = (ctx.videoFrame && ctx.videoFrame(o.asset, (o.offset || 0) + lt * (o.speed || 1))) || ctx.asset(o.asset);
  const chromeH = o.chrome === false ? 0 : 64, ih = h - chromeH, imgA = o.imageAspect || o.aspect || 16 / 10, boxA = w / ih;
  const bw = imgA >= boxA ? ih * s * imgA : w * s, bh = imgA >= boxA ? ih * s : w * s / imgA;
  const bx = f[0] * (w - bw), by = f[1] * (ih - bh);
  let dimP = 0;
  const hls = (o.highlights || []).map(hl => {
    const p = eIO((k - (hl.at != null ? hl.at : 0.5) * FPS) / 7); if (p <= 0) return "";
    dimP = Math.max(dimP, p);
    const [bar] = barPair(ctx, hl.role || "bad");
    const x0 = Math.max(0, bx + hl.x * bw), y0 = Math.max(0, by + hl.y * bh), x1 = Math.min(w, bx + (hl.x + hl.w) * bw), y1 = Math.min(ih, by + (hl.y + hl.h) * bh);
    return `<div style="position:absolute;left:${r2(x0)}px;top:${r2(y0)}px;width:${r2(Math.max(0, x1 - x0))}px;height:${r2(Math.max(0, y1 - y0))}px;border:6px solid ${bar};border-radius:10px;box-sizing:border-box;transform:scaleX(${r2(p)});transform-origin:0 50%"></div>`;
  }).join("");
  const chrome = chromeH ? `<div style="height:${chromeH}px;display:flex;align-items:center;gap:12px;padding:0 24px;background:${th.card};border-bottom:2px solid ${th.line}">${["#ff5f57", "#febc2e", "#28c840"].map(c => `<span style="width:16px;height:16px;border-radius:50%;background:${c}"></span>`).join("")}${o.chrome ? `<span style="flex:1;text-align:center;font:600 24px/1 ${ctx.fam("display")};color:${th.sub}" data-tc="TC-decorative">${esc(o.chrome)}</span><span style="width:72px"></span>` : ""}</div>` : "";
  return `${chrome}<div style="position:relative;width:${w}px;height:${ih}px;overflow:hidden;background:#000">
      <div style="position:absolute;inset:0;background:url('${src}') ${r2(bx)}px ${r2(by)}px/${r2(bw)}px ${r2(bh)}px no-repeat"></div>
      ${hls ? `<div style="position:absolute;inset:0;background:rgba(0,0,0,${r2(0.12 * dimP)})"></div>${hls}` : ""}</div>`;
}
fx.shot = function (o) {
  const x = o.x != null ? o.x : 70, y = o.y != null ? o.y : 300, w = o.w || 940, chromeH = o.chrome === false ? 0 : 64;
  const h = o.h || Math.round(w / (o.aspect || 16 / 10) + chromeH), dur = o.t_out - o.t_in, hasCredit = !!o.credit;
  const evts = (o.highlights || []).map(hl => (hl.at != null ? hl.at : 0.5));
  return reg(o, Object.assign({
    id: o.id, t_in: o.t_in, t_out: o.t_out, z: o.z || 4, in: "none", out: "none", text: hasCredit, text_content: o.credit || undefined,
    text_px: hasCredit ? 24 : undefined, text_class: hasCredit ? "TC-legal" : undefined, box: { x, y, w, h: h + (hasCredit ? 52 : 0) },
    roles: o.roles || ((o.highlights || []).length ? ["bad"] : []), events: evs(evts, dur), asset: o.asset,
  }, insMeta(o, o.recipe || "creator_media", "creator", { label: undefined }), {
    render(ctx, lt) {
      const th = theme({ theme: o.theme || "light" }), e = enter(lt, dur, 10, 40);
      return ctx.html(`<div style="${wrapStyle(e, x, y, w)}"><div style="width:${w}px;height:${h}px;border-radius:${o.radius != null ? o.radius : 30}px;overflow:hidden;box-shadow:${th.shadow};background:${th.card}">${shotHTML(ctx, o, lt, dur, 0, 0, w, h, th)}</div>
        ${hasCredit ? creditHTML(ctx, o.credit, "#ffffff", C(ctx, o.creditDot || "primary"), "margin-top:18px;text-shadow:0 1px 3px rgba(0,0,0,.65)") : ""}</div>`);
    },
  }));
};

/* ================================================================ citation strip (Dhruv-style evidence) */
/* o: {id, t_in, t_out, insert, masthead, date, headline (exact), highlight:[phrases] | highlights (boxes on the asset),
       asset? (creator screenshot: shown instead of the created headline), aspect, x=60, y, w=960, hlRole='bad',
       credit (e.g. "SOURCE: <masthead>"), label (created only)} */
fx.citationStrip = function (o) {
  const x = o.x != null ? o.x : 64, y = o.y != null ? o.y : 330, w = o.w || 952, dur = o.t_out - o.t_in, created = !o.asset;
  const size = o.size || 60, pad = 50, strip = 92;
  const estLines = Math.ceil(String(o.headline || "").length * size * 0.52 / (w - 2 * pad)) || 1;
  const bodyH = created ? Math.round(pad * 2 + estLines * size * 1.14 + 3 * 34 + 40) : Math.round(w / (o.aspect || 16 / 10));
  const h = strip + bodyH + 64;
  const label = created ? (o.label || null) : null;
  const hlAt = o.hlAt != null ? o.hlAt : 0.5, spans = (o.highlight || []).map(s => (typeof s === "object" ? s.text : s));
  const txt = [o.masthead, o.date, created ? o.headline : null, label, o.credit].filter(Boolean).join(" / ");
  return reg(o, Object.assign({
    id: o.id, t_in: o.t_in, t_out: o.t_out, z: o.z || 4, in: "none", out: "none", text: true, text_content: txt,
    text_px: 24, text_class: o.text_class || "TC-label", box: { x, y, w, h }, roles: o.roles || [o.hlRole || "bad"],
    events: evs([hlAt, ...spans.map((_, k) => hlAt + k * 0.5), ...(o.highlights || []).map(hl => (hl.at != null ? hl.at : 0.5))], dur),
    quote_text: created ? String(o.headline || "") : undefined, asset: o.asset,
    source: { masthead: o.masthead, date: o.date, headline: o.headline, url: o.source_url, highlight_spans: spans },
  }, insMeta(o, "citation_strip", created ? "created" : "creator", { label: label || undefined }), {
    render(ctx, lt) {
      const th = theme({ theme: o.theme || "paper" }), e = enter(lt, dur), [bar] = barPair(ctx, o.hlRole || "bad"), k = lt * FPS;
      const ps = eIO((k - 2) / 10);
      const stripHTML = `<div style="height:${strip}px;display:flex;align-items:center;gap:22px;padding:0 34px;background:#0e0e11;position:relative;overflow:hidden">
        <div style="position:absolute;left:0;bottom:0;height:6px;width:${r2(ps * 100)}%;background:${bar}"></div>
        <span style="font:800 40px/1 ${ctx.fam("display")};letter-spacing:.12em;color:#ffffff">SOURCE</span>
        <span style="width:3px;height:40px;background:rgba(255,255,255,.3)"></span>
        <span style="font:700 40px/1 ${ctx.fam("serif")};color:#ffffff;white-space:nowrap;overflow:hidden;flex:1">${esc(o.masthead || "")}</span>
        <span style="font:600 40px/1 ${ctx.fam("display")};color:#d8d8de;white-space:nowrap">${esc(o.date || "")}</span></div>`;
      let body;
      if (created) {
        const head = textBlock(ctx, { text: o.headline, size, fam: ctx.fam(o.font || "serif"), weight: 400, maxW: w - 2 * pad, color: th.ink, lt, spans: o.highlight, hlRole: o.hlRole || "bad", hlAt, hlGap: 0.5, lh: 1.22 });
        body = `<div style="padding:${pad}px;background:${th.card}">${head.html}<div style="display:flex;flex-direction:column;gap:20px;margin-top:36px">${[94, 86, 70].map(p => `<div style="height:14px;border-radius:7px;background:${th.skel};width:${p}%"></div>`).join("")}</div></div>`;
      } else {
        body = shotHTML(ctx, Object.assign({ chrome: false }, o), lt, dur, 0, 0, w, bodyH, th);
      }
      return ctx.html(`<div style="${wrapStyle(e, x, y, w, `border-radius:28px;overflow:hidden;box-shadow:${th.shadow};background:${th.card}`)}">${stripHTML}${body}
        <div style="height:64px;display:flex;align-items:center;justify-content:space-between;padding:0 34px;background:${th.card};border-top:2px solid ${th.line}">${label ? labelHTML(ctx, label, th) : "<span></span>"}${o.credit ? creditHTML(ctx, o.credit, th.tag, bar) : ""}</div></div>`);
    },
  }));
};

/* ================================================================ standalone credit line */
/* o: {id, t_in, t_out, text ("SOURCE: …"), x, y (default tokens.citations.credit_line or 40, 140), size (>= 22), insert?} */
fx.creditLine = function (o) {
  const cfg = o.config || {}, size = Math.max(22, o.size || cfg.size || 24);
  const x = o.x != null ? o.x : (cfg.x != null ? cfg.x : 64), y = o.y != null ? o.y : (cfg.y != null ? cfg.y : 140), dur = o.t_out - o.t_in;
  const text = (o.prefix != null ? o.prefix : "") + (o.text || "");
  return reg(o, {
    id: o.id, t_in: o.t_in, t_out: o.t_out, z: o.z || 6, in: "none", out: "none", kind: "credit", text: true, text_content: text,
    text_px: size, text_class: "TC-legal", box: { x, y, w: Math.min(1016 - x, Math.round(text.length * size * 0.66 + 40)), h: Math.round(size * 1.3) },
    credit: text, insert: o.insert, roles: [],
    render(ctx, lt) {
      const p = cl((lt * FPS - 4) / 6) * cl((dur - lt) * FPS / 6);
      return ctx.html(`<div style="position:absolute;left:${x}px;top:${y}px;opacity:${r2(p * (o.opacity || 0.9))}">${creditHTML(ctx, text, "#ffffff", C(ctx, o.dot || "primary"), `font-size:${size}px;text-shadow:0 1px 4px rgba(0,0,0,.7)`)}</div>`);
    },
  });
};
fx.insertsVersion = 1;
})();
