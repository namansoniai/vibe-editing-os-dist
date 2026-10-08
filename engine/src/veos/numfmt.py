"""Number formatting and parsing for on-screen figures (E-08; structure SW-08, §5.5, §18).

`fmt_num(value, spec, base)` is mirrored exactly by `renderer/numbers.js` (`VEOS_NUM.fmt`, which is `ctx.fmtNum` in a
scene): same rounding (half away from zero on the decimal digits, with a 1e-9 nudge so 2.675 -> 2.68 in both), same
grouping, same words. A parity test (tests/test_data.py) runs both over a shared case list.

Spec keys (a format dict; the profile's `numbers` block is the base, a figure's `format` and the call's spec override):
  grouping  indian (1,23,45,678) | international (12,345,678) | none
  currency  "" | "₹" | "$" | "€" | "£" | "Rs" | "INR" ... (alphabetic codes get a space: "Rs 500")
  compact   lakh_crore (L / Cr, lakh / crore) | k_m_b (K / M / B, thousand / million / billion) | none
  style     full (grouped digits) | short (₹12.5 L, $3.2M) | long (₹12.5 lakh, $3.2 million)
  decimals  decimals of a full number (default 0); compact_decimals (2) for short / long forms; percent_decimals (1)
  trim      drop trailing zeros (default: true for short / long / percent, false for full)
  unit      "%" (the value is already in percent), a convertible unit (km, mi, kg, lb, l, gal, c, f, ...), or any label
            (a value with a unit is never written with the currency)
  units     metric | imperial | dual: a convertible unit is converted to the profile's system, or shown with the other
            system in brackets ("12 km (7.5 mi)", dual_decimals 1)
  lang      en | hinglish | hi (long words: lakh / crore; hi: लाख / करोड़); plural: true -> "lakhs" / "crores" (en only)
  sign      true -> "+12%"; space (between the number and L / Cr / K: default true for lakh_crore, false for k_m_b);
  min_compact  below this the short / long style falls back to full (default 1,00,000 for lakh_crore, 1,000 for k_m_b)
  prefix / suffix  literal text
A string spec is a style shorthand: "full" | "short" | "long" | "percent" (or "%").

`parse_numbers(text)` finds the numbers written in a text (for V-NUMFMT / V-DATA): value, the half-unit of its written
precision, currency, compact word, grouping class, decimals, percent and unit.
`spoken_numbers(words)` finds numbers in transcript words (digits, "2.5 lakhs", "fifty one thousand", Hinglish "dhai
lakh"), with the time of their first word.
"""
from __future__ import annotations

import math
import re

DASH = "–"
STYLES = ("full", "short", "long")
DEFAULT = {"grouping": "international", "currency": "", "compact": "none", "style": "full", "decimals": 0,
           "compact_decimals": 2, "percent_decimals": 1, "trim": None, "unit": "", "units": "metric", "dual_decimals": 1, "lang": "en",
           "plural": False, "sign": False, "space": None, "min_compact": None, "prefix": "", "suffix": ""}

# compact tables: (threshold, short symbol, long word en/hinglish, long word hi), largest first
COMPACT = {
    "lakh_crore": [(1e7, "Cr", "crore", "करोड़"), (1e5, "L", "lakh", "लाख")],
    "k_m_b": [(1e9, "B", "billion", "बिलियन"), (1e6, "M", "million", "मिलियन"), (1e3, "K", "thousand", "हज़ार")],
}
MIN_COMPACT = {"lakh_crore": 1e5, "k_m_b": 1e3}

# convertible units: id -> (dimension, factor to the SI base, system, label); temperatures are affine (c / f)
UNITS = {
    "mm": ("length", 0.001, "metric", "mm"), "cm": ("length", 0.01, "metric", "cm"), "m": ("length", 1.0, "metric", "m"),
    "km": ("length", 1000.0, "metric", "km"), "in": ("length", 0.0254, "imperial", "in"),
    "ft": ("length", 0.3048, "imperial", "ft"), "yd": ("length", 0.9144, "imperial", "yd"),
    "mi": ("length", 1609.344, "imperial", "mi"),
    "g": ("mass", 0.001, "metric", "g"), "kg": ("mass", 1.0, "metric", "kg"), "t": ("mass", 1000.0, "metric", "t"),
    "oz": ("mass", 0.028349523125, "imperial", "oz"), "lb": ("mass", 0.45359237, "imperial", "lb"),
    "ml": ("volume", 0.001, "metric", "ml"), "l": ("volume", 1.0, "metric", "L"),
    "floz": ("volume", 0.0295735295625, "imperial", "fl oz"), "gal": ("volume", 3.785411784, "imperial", "gal"),
    "kmh": ("speed", 1 / 3.6, "metric", "km/h"), "mph": ("speed", 0.44704, "imperial", "mph"),
    "sqm": ("area", 1.0, "metric", "m²"), "sqft": ("area", 0.09290304, "imperial", "sq ft"),
    "ha": ("area", 10000.0, "metric", "ha"), "acre": ("area", 4046.8564224, "imperial", "acres"),
    "c": ("temp", 1.0, "metric", "°C"), "f": ("temp", 1.0, "imperial", "°F"),
}
PAIR = {"km": "mi", "mi": "km", "m": "ft", "ft": "m", "cm": "in", "in": "cm", "mm": "in", "yd": "m", "kg": "lb", "lb": "kg",
        "g": "oz", "oz": "g", "l": "gal", "gal": "l", "ml": "floz", "floz": "ml", "kmh": "mph", "mph": "kmh",
        "sqm": "sqft", "sqft": "sqm", "ha": "acre", "acre": "ha", "c": "f", "f": "c", "t": "lb"}
NOSPACE_UNITS = {"x", "c", "f", "%"}


def convert(value: float, frm: str, to: str) -> float:
    """Unit conversion through the SI base (temperatures affine). Raises KeyError / ValueError on unknown or mixed units."""
    a, b = UNITS[frm], UNITS[to]
    if a[0] != b[0]:
        raise ValueError(f"cannot convert {frm} ({a[0]}) to {to} ({b[0]})")
    if a[0] == "temp":
        if frm == to:
            return value
        return value * 9 / 5 + 32 if frm == "c" else (value - 32) * 5 / 9
    return value * a[1] / b[1]


def resolve_spec(spec=None, base: dict | None = None) -> dict:
    """DEFAULT < base (profile numbers) < spec (dict, or a style shorthand string)."""
    out = dict(DEFAULT)
    for layer in (base, spec):
        if layer is None:
            continue
        if isinstance(layer, str):
            s = layer.strip().lower()
            if s in ("percent", "%"):
                out["unit"] = "%"
            elif s in STYLES:
                out["style"] = s
            continue
        if isinstance(layer, dict):
            for k, v in layer.items():
                if v is not None:
                    out[k] = v
    return out


# ------------------------------------------------------------------ the formatter (mirrored in renderer/numbers.js)
def _digits(a: float, d: int) -> tuple[int, str]:
    """a >= 0 rounded half away from zero to d decimals -> (integer part, fraction digits)."""
    p = 10 ** d
    n = math.floor(a * p + 0.5 + 1e-9)
    ip, fp = divmod(n, p)
    return int(ip), (str(int(fp)).zfill(d) if d > 0 else "")


def group(ip: int, grouping: str) -> str:
    s = str(ip)
    if grouping == "none" or len(s) <= 3:
        return s
    if grouping == "indian":
        head, tail = s[:-3], s[-3:]
        parts = []
        while len(head) > 2:
            parts.insert(0, head[-2:])
            head = head[:-2]
        if head:
            parts.insert(0, head)
        return ",".join(parts + [tail])
    parts = []
    while len(s) > 3:
        parts.insert(0, s[-3:])
        s = s[:-3]
    return ",".join([s] + parts)


def _num(a: float, d: int, grouping: str, trim: bool) -> tuple[str, bool]:
    ip, fp = _digits(a, d)
    if trim:
        fp = fp.rstrip("0")
    return group(ip, grouping) + ("." + fp if fp else ""), (ip == 0 and not fp.strip("0"))


def _cur(c: str) -> str:
    if not c:
        return ""
    return c + " " if re.fullmatch(r"[A-Za-z]{2,}\.?", c) else c


def _int(v, d):
    try:
        return int(v)
    except (TypeError, ValueError):
        return d


def fmt_num(value, spec=None, base: dict | None = None) -> str:
    """Format a number for the screen. See the module doc for the spec keys."""
    f = resolve_spec(spec, base)
    try:
        v = float(value)
    except (TypeError, ValueError):
        return DASH
    if not math.isfinite(v):
        return DASH
    unit = str(f.get("unit") or "")
    pct = unit == "%"
    ukey = unit.lower()
    alt = None
    if ukey in UNITS and not pct:
        system, pref = UNITS[ukey][2], f.get("units") or "metric"
        if pref in ("metric", "imperial") and system != pref and ukey in PAIR:
            v, ukey = convert(v, ukey, PAIR[ukey]), PAIR[ukey]
        elif pref == "dual" and ukey in PAIR:
            alt = (convert(v, ukey, PAIR[ukey]), PAIR[ukey])
    neg = v < 0
    a = abs(v)
    style = f.get("style") if f.get("style") in STYLES else "full"
    compact = f.get("compact") if f.get("compact") in COMPACT else "none"
    grouping = f.get("grouping") or "international"
    trim = f.get("trim")
    word = ""
    num, zero = None, False
    if not pct and style in ("short", "long") and compact != "none":
        table = COMPACT[compact]
        minc = f.get("min_compact")
        minc = MIN_COMPACT[compact] if minc is None else float(minc)
        cd = _int(f.get("compact_decimals"), 2)
        idx = next((i for i, row in enumerate(table) if a >= row[0]), None)
        if idx is not None and a >= minc:
            ip, fp = _digits(a / table[idx][0], cd)
            if idx > 0 and ip + (int(fp) if fp else 0) / (10 ** cd) >= table[idx - 1][0] / table[idx][0]:
                idx -= 1  # rounding carried into the next unit (99.999 L -> 1 Cr)
            num, zero = _num(a / table[idx][0], cd, grouping, True if trim is None else bool(trim))
            row = table[idx]
            if style == "short":
                sp = f.get("space")
                sp = (compact == "lakh_crore") if sp is None else bool(sp)
                word = (" " if sp else "") + row[1]
            else:
                lang = f.get("lang") or "en"
                w = row[3] if lang == "hi" else row[2]
                if lang == "en" and f.get("plural") and num != "1":
                    w += "s"
                word = " " + w
    if num is None:
        d = _int(f.get("percent_decimals"), 1) if pct else _int(f.get("decimals"), 0)
        num, zero = _num(a, d, grouping, (pct if trim is None else bool(trim)))
    sign = "-" if neg and not zero else ("+" if f.get("sign") and not neg and not zero else "")
    out = sign + ("" if pct or unit else _cur(str(f.get("currency") or ""))) + num + word
    if pct:
        out += "%"
    elif ukey in UNITS:
        lab = UNITS[ukey][3]
        out += ("" if ukey in NOSPACE_UNITS else " ") + lab
    elif unit:
        out += ("" if unit in NOSPACE_UNITS else " ") + unit
    if alt is not None:
        an, _ = _num(abs(alt[0]), _int(f.get("dual_decimals"), 1), grouping, True)
        lab = UNITS[alt[1]][3]
        out += " (" + ("-" if alt[0] < 0 and an.strip("0.,") else "") + an + ("" if alt[1] in NOSPACE_UNITS else " ") + lab + ")"
    return str(f.get("prefix") or "") + out + str(f.get("suffix") or "")


# ------------------------------------------------------------------ parsing written numbers
CUR_RE = r"(?P<cur>₹|\$|€|£|¥|Rs\.?\s?|INR\s?|USD\s?|EUR\s?)?"
NUM_RE = re.compile(
    r"(?<![\w.,])(?P<sign>[-−+])?" + CUR_RE +
    r"(?P<num>\d(?:[\d,]*\d)?(?:\.\d+)?|\.\d+)"
    r"(?P<sp>\s?)(?P<suf>[Cc]rores?|[Ll]akhs?|[Ll]acs?|Cr|L|K|k|M|B|bn|mn|[Mm]illion|[Bb]illion|[Tt]housand|लाख|करोड़|हज़ार|%)?"
    r"(?![\w\d])", re.UNICODE)
SUF_MULT = {"cr": 1e7, "crore": 1e7, "crores": 1e7, "करोड़": 1e7, "l": 1e5, "lakh": 1e5, "lakhs": 1e5, "lac": 1e5,
            "lacs": 1e5, "लाख": 1e5, "k": 1e3, "thousand": 1e3, "हज़ार": 1e3, "m": 1e6, "mn": 1e6, "million": 1e6,
            "b": 1e9, "bn": 1e9, "billion": 1e9}
LAKH_SUF = {"cr", "crore", "crores", "करोड़", "l", "lakh", "lakhs", "lac", "lacs", "लाख"}
KMB_SUF = {"k", "thousand", "m", "mn", "million", "b", "bn", "billion"}


def grouping_class(intpart: str) -> str:
    """'none' (no commas), 'both' (valid either way: 40,000), 'indian', 'international' or 'invalid'."""
    if "," not in intpart:
        return "none"
    g = intpart.split(",")
    intl = 1 <= len(g[0]) <= 3 and all(len(x) == 3 for x in g[1:])
    ind = len(g[-1]) == 3 and 1 <= len(g[0]) <= 2 and all(len(x) == 2 for x in g[1:-1])
    if intl and ind:
        return "both"
    return "indian" if ind else "international" if intl else "invalid"


def parse_numbers(text: str) -> list[dict]:
    out = []
    for m in NUM_RE.finditer(str(text or "")):
        raw_num = m.group("num")
        if not re.search(r"\d", raw_num):
            continue
        intpart, _, frac = raw_num.partition(".")
        try:
            base = float(raw_num.replace(",", ""))
        except ValueError:
            continue
        suf = m.group("suf") or ""
        sk = suf.lower()
        mult = SUF_MULT.get(sk, 1.0)
        val = base * mult
        if m.group("sign") in ("-", "−"):
            val = -val
        cur = (m.group("cur") or "").strip()
        half = 0.5 * (10 ** -len(frac)) * mult
        if mult > 1:  # "₹2 L" is not an honest way to write 1,63,250: a compact number is good to +-2.5 % at most
            half = min(half, max(0.5, 0.025 * abs(val)))
        out.append({"raw": m.group(0).strip(), "start": m.start(), "end": m.end(), "value": val,
                    "half": half, "currency": cur, "suffix": suf, "compact": sk if sk in SUF_MULT else "",
                    "grouping": grouping_class(intpart), "int_digits": len(intpart.replace(",", "")), "decimals": len(frac),
                    "percent": suf == "%", "space": m.group("sp") or ""})
    return out


# ------------------------------------------------------------------ spoken numbers (transcript words)
EN_UNITS = {w: i for i, w in enumerate("zero one two three four five six seven eight nine ten eleven twelve thirteen "
                                       "fourteen fifteen sixteen seventeen eighteen nineteen".split())}
EN_TENS = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90}
HI_UNITS = {"ek": 1, "do": 2, "teen": 3, "char": 4, "chaar": 4, "paanch": 5, "panch": 5, "chhe": 6, "che": 6, "saat": 7,
            "aath": 8, "nau": 9, "das": 10, "bees": 20, "tees": 30, "chalis": 40, "chaalis": 40, "pachaas": 50,
            "pachas": 50, "sattar": 70, "assi": 80, "nabbe": 90}
HI_FRACT = {"dhai": 2.5, "dedh": 1.5, "paune": -0.25}
SCALES = {"hundred": 100, "sau": 100, "thousand": 1e3, "hazaar": 1e3, "hazar": 1e3, "lakh": 1e5, "lakhs": 1e5,
          "lac": 1e5, "lacs": 1e5, "crore": 1e7, "crores": 1e7, "million": 1e6, "billion": 1e9, "k": 1e3}
SKIP_WORDS = {"and", "rupees", "rupee", "rs", "dollars", "dollar", "percent", "%"}


def _clean(w: str) -> str:
    w = re.sub(r"^[^\w₹$€£.]+|[^\w%]+$", "", str(w or "").lower()).replace("₹", "").replace("$", "")
    m = re.match(r"^(\d[\d,.]*)-\w+$", w)  # "10-year" -> "10"
    return m.group(1) if m else w


def _word_value(w: str):
    """('num', value, unit, is_word) | ('frac', value) | ('saadhe',) | ('scale', mult) | None for one cleaned word."""
    if re.fullmatch(r"\d[\d,]*(\.\d+)?%?", w):
        s = w.rstrip("%").replace(",", "")
        frac = s.partition(".")[2]
        return ("num", float(s), 10.0 ** -len(frac), False)
    m = re.fullmatch(r"(\d+(?:\.\d+)?)(k|l|cr|m|b)", w)
    if m:
        mult = {"k": 1e3, "l": 1e5, "cr": 1e7, "m": 1e6, "b": 1e9}[m.group(2)]
        return ("num", float(m.group(1)) * mult, 10.0 ** -len(m.group(1).partition(".")[2]) * mult, False)
    for table in (EN_UNITS, EN_TENS, HI_UNITS):
        if w in table:
            return ("num", float(table[w]), 1.0, True)
    if w in HI_FRACT:
        return ("frac", HI_FRACT[w])
    if w in ("saadhe", "sadhe"):
        return ("saadhe",)
    if w in SCALES:
        return ("scale", SCALES[w])
    return None


def spoken_numbers(words: list[dict]) -> list[dict]:
    """Numbers in transcript words: [{value, half, s, e, i0, i1, text, by_words}] (s = first word start, edit time).

    Digits ("51,880", "2.5", "8%"), digit + scale ("2.5 lakhs", "50K"), English words ("fifty one thousand",
    "one lakh thirty one thousand"), Hinglish ("dhai lakh", "saadhe teen crore", "do sau"). A lone "one" / "ek" / "zero"
    is not reported (too common); `half` is half the unit of the last spoken component (51,880 -> 0.5, 2.5 lakh -> 5,000)."""
    out, i, n = [], 0, len(words)
    raw = [str(w.get("w", "")) for w in words]
    vals = [_word_value(_clean(r)) for r in raw]
    while i < n:
        t0 = vals[i]
        if t0 is None or t0[0] == "scale" or (t0[0] == "saadhe" and not (i + 1 < n and vals[i + 1] and vals[i + 1][0] == "num")):
            i += 1
            continue
        total, cur, unit, saadhe, last, by_words = 0.0, None, 1.0, False, None, True
        j = i
        while j < n:
            t = vals[j]
            if t is None:
                if _clean(raw[j]) == "and" and cur is None and total and j + 1 < n and vals[j + 1] and vals[j + 1][0] == "num":
                    j += 1
                    continue
                break
            k = t[0]
            if k == "num":
                if cur is not None:
                    tens_unit = t[3] and last == "tens" and t[1] < 10
                    after_hundred = t[3] and last == "hundred" and t[1] < 100
                    if not (tens_unit or after_hundred):
                        break
                    cur += t[1]
                    unit = min(unit, t[2])
                else:
                    cur, unit = t[1], (min(unit, t[2]) if saadhe else t[2])
                    by_words = by_words and t[3]
                last = "tens" if (t[3] and t[1] >= 20 and t[1] % 10 == 0) else "num"
            elif k == "frac":
                if cur is not None:
                    break
                cur, unit, last = t[1], 0.1, "num"
            elif k == "saadhe":
                if cur is not None:
                    break
                saadhe, unit = True, 0.1
            else:  # scale
                if cur is None:
                    break
                cur = (cur + (0.5 if saadhe else 0)) * t[1]
                unit *= t[1]
                saadhe = False
                if t[1] >= 1e3:
                    total, cur, last = total + cur, None, "big"
                else:
                    last = "hundred"
            j += 1
            if not re.search(r"\w$", raw[j - 1].strip()) and not raw[j - 1].strip().endswith("%"):
                break  # punctuation ends a number ("51,880. On ...")
        if j == i:
            i += 1
            continue
        val = total + (cur or 0.0)
        if by_words and val <= 1 and j - i == 1:
            i = j
            continue
        half = unit / 2 if unit <= 1 else min(unit / 2, max(0.5, 0.025 * abs(val)))  # "2 lakhs" means 2,00,000 +-2.5 %
        out.append({"value": val, "half": half, "s": float(words[i].get("s", 0)), "e": float(words[j - 1].get("e", 0)),
                    "i0": i, "i1": j - 1, "text": " ".join(raw[i:j]), "by_words": by_words})
        i = j
    return out


def same_number(a: float, b: float, half_a: float = 0.5, extra: float = 0.0) -> bool:
    """b matches a number written / spoken as a with precision +-half_a (+ an extra tolerance)."""
    return abs(a - b) <= half_a + extra + 1e-9 * max(1.0, abs(a))
