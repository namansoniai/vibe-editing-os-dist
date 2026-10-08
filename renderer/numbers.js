/* Vibe Editing OS renderer: the number formatter (E-08). Classic script / UMD, loaded by player.html before core.js.
   VEOS_NUM.fmt(value, spec, base) is ctx.fmtNum in a scene. It mirrors engine/src/veos/numfmt.py fmt_num EXACTLY (same
   rounding: half away from zero with a 1e-9 nudge; same grouping, words and units); tests/test_data.py checks parity.

   spec keys: grouping indian|international|none, currency, compact lakh_crore|k_m_b|none, style full|short|long,
   decimals, compact_decimals (2), percent_decimals (1), trim, unit ("%" or km/mi/kg/lb/l/gal/c/f... or a label),
   units metric|imperial|dual, dual_decimals (1), lang en|hinglish|hi, plural, sign, space, min_compact, prefix, suffix.
   A string spec is a style shorthand: "full" | "short" | "long" | "percent" | "%". */
(function (root, factory) {
  const api = factory();
  if (typeof module === "object" && module.exports) module.exports = api;
  else root.VEOS_NUM = api;
}(typeof self !== "undefined" ? self : this, function () {
"use strict";
const DASH = "–";
const STYLES = ["full", "short", "long"];
const DEFAULT = { grouping: "international", currency: "", compact: "none", style: "full", decimals: 0,
  compact_decimals: 2, percent_decimals: 1, trim: null, unit: "", units: "metric", dual_decimals: 1, lang: "en",
  plural: false, sign: false, space: null, min_compact: null, prefix: "", suffix: "" };
const COMPACT = {
  lakh_crore: [[1e7, "Cr", "crore", "करोड़"], [1e5, "L", "lakh", "लाख"]],
  k_m_b: [[1e9, "B", "billion", "बिलियन"], [1e6, "M", "million", "मिलियन"], [1e3, "K", "thousand", "हज़ार"]],
};
const MIN_COMPACT = { lakh_crore: 1e5, k_m_b: 1e3 };
const UNITS = {
  mm: ["length", 0.001, "metric", "mm"], cm: ["length", 0.01, "metric", "cm"], m: ["length", 1.0, "metric", "m"],
  km: ["length", 1000.0, "metric", "km"], in: ["length", 0.0254, "imperial", "in"],
  ft: ["length", 0.3048, "imperial", "ft"], yd: ["length", 0.9144, "imperial", "yd"],
  mi: ["length", 1609.344, "imperial", "mi"],
  g: ["mass", 0.001, "metric", "g"], kg: ["mass", 1.0, "metric", "kg"], t: ["mass", 1000.0, "metric", "t"],
  oz: ["mass", 0.028349523125, "imperial", "oz"], lb: ["mass", 0.45359237, "imperial", "lb"],
  ml: ["volume", 0.001, "metric", "ml"], l: ["volume", 1.0, "metric", "L"],
  floz: ["volume", 0.0295735295625, "imperial", "fl oz"], gal: ["volume", 3.785411784, "imperial", "gal"],
  kmh: ["speed", 1 / 3.6, "metric", "km/h"], mph: ["speed", 0.44704, "imperial", "mph"],
  sqm: ["area", 1.0, "metric", "m²"], sqft: ["area", 0.09290304, "imperial", "sq ft"],
  ha: ["area", 10000.0, "metric", "ha"], acre: ["area", 4046.8564224, "imperial", "acres"],
  c: ["temp", 1.0, "metric", "°C"], f: ["temp", 1.0, "imperial", "°F"],
};
const PAIR = { km: "mi", mi: "km", m: "ft", ft: "m", cm: "in", in: "cm", mm: "in", yd: "m", kg: "lb", lb: "kg",
  g: "oz", oz: "g", l: "gal", gal: "l", ml: "floz", floz: "ml", kmh: "mph", mph: "kmh",
  sqm: "sqft", sqft: "sqm", ha: "acre", acre: "ha", c: "f", f: "c", t: "lb" };
const NOSPACE = new Set(["x", "c", "f", "%"]);
const has = (o, k) => Object.prototype.hasOwnProperty.call(o, k);

function convert(value, frm, to) {
  const a = UNITS[frm], b = UNITS[to];
  if (!a || !b) throw new Error(`unknown unit ${!a ? frm : to}`);
  if (a[0] !== b[0]) throw new Error(`cannot convert ${frm} (${a[0]}) to ${to} (${b[0]})`);
  if (a[0] === "temp") { if (frm === to) return value; return frm === "c" ? value * 9 / 5 + 32 : (value - 32) * 5 / 9; }
  return value * a[1] / b[1];
}

function resolveSpec(spec, base) {
  const out = Object.assign({}, DEFAULT);
  for (const layer of [base, spec]) {
    if (layer == null) continue;
    if (typeof layer === "string") {
      const s = layer.trim().toLowerCase();
      if (s === "percent" || s === "%") out.unit = "%"; else if (STYLES.includes(s)) out.style = s;
      continue;
    }
    if (typeof layer === "object") for (const k of Object.keys(layer)) if (layer[k] != null) out[k] = layer[k];
  }
  return out;
}

function digits(a, d) { // a >= 0, rounded half away from zero to d decimals -> [integer part, fraction digits]
  const p = Math.pow(10, d), n = Math.floor(a * p + 0.5 + 1e-9);
  const ip = Math.floor(n / p), fp = n - ip * p;
  return [ip, d > 0 ? String(fp).padStart(d, "0") : ""];
}
function group(ip, grouping) {
  let s = String(ip);
  if (grouping === "none" || s.length <= 3) return s;
  if (grouping === "indian") {
    let head = s.slice(0, -3); const tail = s.slice(-3), parts = [];
    while (head.length > 2) { parts.unshift(head.slice(-2)); head = head.slice(0, -2); }
    if (head) parts.unshift(head);
    return parts.concat([tail]).join(",");
  }
  const parts = [];
  while (s.length > 3) { parts.unshift(s.slice(-3)); s = s.slice(0, -3); }
  return [s].concat(parts).join(",");
}
function num(a, d, grouping, trim) {
  let [ip, fp] = digits(a, d);
  if (trim) fp = fp.replace(/0+$/, "");
  return [group(ip, grouping) + (fp ? "." + fp : ""), ip === 0 && !fp.replace(/0/g, "")];
}
const cur = c => (!c ? "" : /^[A-Za-z]{2,}\.?$/.test(c) ? c + " " : c);
const int = (v, d) => { const x = parseInt(v, 10); return isNaN(x) ? d : x; };

function fmt(value, spec, base) {
  const f = resolveSpec(spec, base);
  let v = typeof value === "number" ? value : (value == null || value === "" ? NaN : Number(value));
  if (!isFinite(v)) return DASH;
  const unit = String(f.unit || ""), pct = unit === "%";
  let ukey = unit.toLowerCase(), alt = null;
  if (has(UNITS, ukey) && !pct) {
    const system = UNITS[ukey][2], pref = f.units || "metric";
    if ((pref === "metric" || pref === "imperial") && system !== pref && has(PAIR, ukey)) { v = convert(v, ukey, PAIR[ukey]); ukey = PAIR[ukey]; }
    else if (pref === "dual" && has(PAIR, ukey)) alt = [convert(v, ukey, PAIR[ukey]), PAIR[ukey]];
  }
  const neg = v < 0, a = Math.abs(v);
  const style = STYLES.includes(f.style) ? f.style : "full";
  const compact = has(COMPACT, f.compact) ? f.compact : "none";
  const grouping = f.grouping || "international", trim = f.trim;
  let word = "", n = null, zero = false;
  if (!pct && (style === "short" || style === "long") && compact !== "none") {
    const table = COMPACT[compact];
    const minc = f.min_compact == null ? MIN_COMPACT[compact] : Number(f.min_compact);
    const cd = int(f.compact_decimals, 2);
    let idx = table.findIndex(row => a >= row[0]);
    if (idx >= 0 && a >= minc) {
      const [ip, fp] = digits(a / table[idx][0], cd);
      if (idx > 0 && ip + (fp ? parseInt(fp, 10) : 0) / Math.pow(10, cd) >= table[idx - 1][0] / table[idx][0]) idx -= 1;
      [n, zero] = num(a / table[idx][0], cd, grouping, trim == null ? true : !!trim);
      const row = table[idx];
      if (style === "short") {
        const sp = f.space == null ? compact === "lakh_crore" : !!f.space;
        word = (sp ? " " : "") + row[1];
      } else {
        const lang = f.lang || "en";
        let w = lang === "hi" ? row[3] : row[2];
        if (lang === "en" && f.plural && n !== "1") w += "s";
        word = " " + w;
      }
    }
  }
  if (n === null) {
    const d = pct ? int(f.percent_decimals, 1) : int(f.decimals, 0);
    [n, zero] = num(a, d, grouping, trim == null ? pct : !!trim);
  }
  const sign = neg && !zero ? "-" : (f.sign && !neg && !zero ? "+" : "");
  let out = sign + (pct || unit ? "" : cur(String(f.currency || ""))) + n + word;
  if (pct) out += "%";
  else if (has(UNITS, ukey)) out += (NOSPACE.has(ukey) ? "" : " ") + UNITS[ukey][3];
  else if (unit) out += (NOSPACE.has(unit) ? "" : " ") + unit;
  if (alt) {
    const [an] = num(Math.abs(alt[0]), int(f.dual_decimals, 1), grouping, true);
    out += " (" + (alt[0] < 0 && an.replace(/[0.,]/g, "") ? "-" : "") + an + (NOSPACE.has(alt[1]) ? "" : " ") + UNITS[alt[1]][3] + ")";
  }
  return String(f.prefix || "") + out + String(f.suffix || "");
}

/* the profile's numbers block (tokens.profile.numbers; v1 tokens: derived from creator.language like the engine) */
const INDIAN_LANGS = ["hinglish", "hi", "ta", "te", "mr", "bn", "kn", "ml", "gu", "pa"];
function profileOf(tokens) {
  const p = tokens && tokens.profile && tokens.profile.numbers;
  if (p) return p;
  const lang = String(((tokens && tokens.creator) || {}).language || "en").toLowerCase(), ind = INDIAN_LANGS.includes(lang);
  return { grouping: ind ? "indian" : "international", currency: ind ? "₹" : "$", compact: ind ? "lakh_crore" : "k_m_b", units: "metric", decimals: 0 };
}

return { fmt, resolveSpec, convert, group, digits, profileOf, UNITS, PAIR, COMPACT, DEFAULT };
}));
