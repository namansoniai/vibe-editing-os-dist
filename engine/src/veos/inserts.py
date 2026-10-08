"""`veos inserts scan|check`: the ask-then-create flow for third-party material (E-10, structure §12.5, NC-7, NC-13).

The engine never fetches anyone else's media. Third-party material (a post read aloud, a news headline, another
creator's clip, a product, an app screen, a chart from somewhere, an event, a person) appears only when the creator
hands it over; everything else is a visual the planner creates from the script's own words.

scan   transcript (work/words.edit.json, edit time) + the script (project.json `script`, `--script`, or
       plan/script.md) -> plan/inserts.scan.json: the moments that call for third-party material, each with
       {id, kind, t0, t1, spoken, script_text, name, cues, also, suggest {recipe, quote_text?}, ask}, plus the
       one plain-language question the `reel-inputs` skill asks the creator. Deterministic heuristic (no model):
       keyword and pattern cues per category, scored per sentence, deduplicated per (kind, name). Also `pointers`:
       the moments where the speaker points with words ("this, this and this", "from this to this", "ye dekho"), from
       veos.pointers; the same question round asks what each should show (with a suggested picture).
check  plan/inserts.json against the record schema, the creator's assets (`veos asset add --origin creator`) and the
       verbatim rule (a created card quotes only script / transcript / creator-typed text). Same checks V-INSERTS runs.
       Made-up cards carry no label and nothing needs a credit line (Naman, 8 Oct 2026).

plan/inserts.json (written by the planner after the one question):
  {"version": 1,
   "asked": {"question": str, "moments": [scan ids], "answer": str},
   "creator_texts": [str],              # text the creator typed in reply (a headline, a post) - quotable verbatim
   "inserts": [{"id", "moment", "t0", "t1", "kind", "origin": "creator" | "created",
                "file"?        (origin creator: the asset name from `veos asset add --origin creator`),
                "recipe"?      (origin created: quote_card | headline_card | recreated_ui | diagram | logo_plate |
                                silhouette | citation_strip),
                "substitute_of"? (origin created: what third-party material it stands in for),
                "quote_text"?  (verbatim words shown as someone's words or as a headline),
                "source"?      ({masthead, date, url?, headline, highlight_spans[]} for citation cards),
                "scene"?       (scene id or ids that show it; scenes may instead declare `insert: <id>`)}],
   "dismissed": [{"moment": scan id, "why": str}],
   "pointers": [{"id": scan pointer id, "t0", "show": str (what the viewer sees there),
                 "by": "creator" | "inferred" (the creator's answer, or the planner's own reading when they had none)}]}
"""
from __future__ import annotations

import difflib
import re
import unicodedata
from pathlib import Path

from .core import VeosError, need_project, read_json, write_json
from .pointers import find_pointers, pointer_question

KINDS = ("post", "headline", "clip", "chart", "event", "person", "product", "app_ui")
RECIPES = ("quote_card", "headline_card", "recreated_ui", "diagram", "logo_plate", "silhouette", "citation_strip")
# created substitutes that imitate a real thing (a post, an article, an app screen, a person)
RECONSTRUCTIONS = {"quote_card", "headline_card", "recreated_ui", "silhouette", "citation_strip"}
QUOTE_RECIPES = {"quote_card", "headline_card"}
KIND_RECIPE = {"post": "quote_card", "headline": "headline_card", "clip": "recreated_ui", "chart": "diagram",
               "event": "logo_plate", "person": "silhouette", "product": "logo_plate", "app_ui": "recreated_ui"}
PLAIN = {"post": "the post you read out", "headline": "the news headline", "clip": "the clip you mention",
         "chart": "the chart or data", "event": "the event", "person": "a photo of {name}",
         "product": "{name} (logo or product shot)", "app_ui": "{name} on screen"}
PLAIN_UNNAMED = {"person": "the person you mention", "app_ui": "the screen you describe", "product": "the product you mention"}
DEFAULT_LABEL = ""   # made-up cards carry no label (kept for callers that pass a label explicitly)
# record problems that are facts (validate blocks on them): someone's words not verbatim, media of unknown origin
FACT_MARKERS = ("(NC-13)", "(NC-7)", "is not quoted from the script", "--origin creator", "is not in plan/assets")


def fact_problem(msg: str) -> bool:
    """True for a record problem that blocks the reel (truth / creator-owned media); the rest is advice."""
    return any(m in msg for m in FACT_MARKERS)
# beat patterns that by definition show third-party material (evidence: Dhruv, Vaibhav, Cleo, peter.visuals)
THIRD_PARTY_PATTERNS = ("P-CITE-CARD", "P-TWEET-CLIP-HOOK", "P-REF-CARD", "P-EXAMPLE-CLIP", "P-THUMBNAIL-WALL")
PRIORITY = {k: i for i, k in enumerate(("post", "headline", "clip", "chart", "person", "event", "app_ui", "product"))}
MIN_SCORE = 2

# well-known products / companies / platforms (the default glossary adds more); matched case-insensitively as words
BRANDS = (
    "Claude", "Claude Code", "Claude Design", "Anthropic", "OpenAI", "ChatGPT", "GPT", "Codex", "Gemini", "Google",
    "Chrome", "Chrome DevTools", "Google Flow", "Flow", "Apple", "iPhone", "Microsoft", "Copilot", "Meta", "Llama", "Mistral", "Perplexity",
    "Midjourney", "Runway", "ElevenLabs", "Sora", "Veo", "Kling", "Cursor", "Windsurf", "Lovable", "Bolt", "Replit",
    "Vercel", "Supabase", "Firebase", "Netlify", "Figma", "Framer", "Webflow", "Canva", "Notion", "Slack", "Zapier",
    "Make", "n8n", "GitHub", "Stripe", "Shopify", "WordPress", "Instagram", "YouTube", "WhatsApp", "Facebook",
    "LinkedIn", "Twitter", "TikTok", "Reddit", "Amazon", "AWS", "Netflix", "Tesla", "Nvidia", "NVIDIA", "Y Combinator",
    "shadcn", "Context7", "Superpowers", "gstack", "Hugging Face", "DeepSeek", "Grok", "xAI", "Mubert",
)
OUTLETS = ("Reuters", "Bloomberg", "The Verge", "TechCrunch", "New York Times", "NYT", "BBC", "CNN", "The Hindu",
           "Times of India", "Economic Times", "Mint", "Forbes", "Guardian", "Wired", "Hindustan Times", "NDTV",
           "Indian Express", "Business Insider", "CNBC", "Moneycontrol", "Inc42", "YourStory", "The Information")
PRODUCT_NOUNS = r"(?:tool|tools|app|apps|mcp|skill|plugin|extension|model|library|framework|platform|website|site|software|feature|api|agent)"
ROLE_WORDS = r"(?:ceo|cto|coo|founder|co-founder|cofounder|president|prime minister|pm|minister|scientist|professor|investor|youtuber|influencer|ceo's|chairman|director)"

CUES: dict[str, list[tuple[str, int]]] = {
    "post": [(r"\b(tweet(?:ed|s)?|retweet|thread|x pe|on x|twitter pe|linkedin (?:post|pe)|reddit (?:post|pe)|"
              r"post (?:kiya|kari|kara|dala|daala)|posted|ne likha|likha (?:hai|tha)|wrote|caption mein)\b", 2),
             (r"\b(post|comment|replied|reply|said|says|ne kaha|ne bola|bola ki|kaha ki)\b", 1)],
    "headline": [(r"\b(headline|news|khabar|report(?:ed|s)?|article|according to|ke mutabik|ke according|"
                  r"press release|announced|announcement|akhbaar|newspaper|breaking)\b", 2)],
    "clip": [(r"\b(viral (?:reel|video|clip)|(?:uska|unka|uski|unki|uske|unke) (?:reel|video|clip|podcast|interview)|"
              r"(?:reel|video|clip|podcast|interview|keynote) (?:mein|me|pe|par)|in (?:his|her|their|this) (?:video|reel|podcast|interview))\b", 2),
             (r"\b(reel|video|clip|podcast|interview|youtube video)\b", 1)],
    "chart": [(r"\b(chart|graph|survey|study|benchmark|leaderboard|statistics|stats|data (?:ke|ki|se|shows))\b", 2),
              (r"\b(data|research|percent|ranking|rank)\b|\d%", 1)],
    "event": [(r"\b(wwdc|google i/o|devday|dev day|keynote|conference|summit|hackathon|launch event|ceremony|"
               r"olympics|world cup|election|budget \d{4})\b", 2),
              (r"\b(event|launch(?:ed)?|unveil(?:ed)?)\b", 1)],
    "person": [(r"\b" + ROLE_WORDS + r"\b", 2)],
    "app_ui": [(r"(?:^|\s)/[a-z][\w-]+", 2),
               (r"\b(shift\s?\+?\s?tab|ctrl\s?\+|cmd\s?\+|dashboard|settings|terminal|console|button|menu|tab mein|"
                r"screen pe|screenshot|upload karo|paste karo|click karo|kholo|open karo|dabao|type karo)\b", 2),
               (r"\b(open|click|tap|type|paste|upload|screen|window|page|editor|inbox|chat)\b", 1)],
    "product": [],  # names: brand lexicon / glossary / "<Name> <product noun>"
}
DIRECTION_RE = re.compile(r"\[(SCREEN|B-ROLL|BROLL|TEXT|SFX|CUT|VISUAL)\s*:\s*([^\]]*)\]", re.I)
OWN_RE = re.compile(r"\b(naman'?s|my|mera|meri|mere|own|apna|apni|apne|creator'?s)\b", re.I)
QUOTE_RE = re.compile(r"[\"“”]([^\"“”]{3,240})[\"“”]")
STOP = set("""a an the and or but if to of in on at by for with from is are was were be been this that these those it its
i you he she we they me my your our their mera meri mere tum tumhara tumhari tumhare main mein hum ye wo woh hai hain
ho tha thi the ka ki ke ko se ne bhi aur ya toh to na nahi kya kaise kyun pe par ek do teen jo jab tab ab sab
pehla doosra teesra chautha paanchva chhatha saatwa sabse ek do teen char chaar paanch chhe saat aath nau das
last first next""".split())


# ------------------------------------------------------------------------------------------------ text helpers
def _nfkc(s: str) -> str:
    s = unicodedata.normalize("NFKC", str(s or ""))
    return s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("–", "-").replace("—", "-")


def norm_tokens(s: str) -> list[str]:
    """Lower-cased word tokens with edge punctuation removed (the unit of the verbatim rule)."""
    out = []
    for t in _nfkc(s).lower().split():
        t = re.sub(r"^[^\w/#@$₹%]+|[^\w%]+$", "", t)
        if t:
            out.append(t)
    return out


def contains_tokens(hay: list[str], needle: list[str]) -> bool:
    if not needle:
        return False
    n, first = len(needle), needle[0]
    for i in range(len(hay) - n + 1):
        if hay[i] == first and hay[i:i + n] == needle:
            return True
    return False


def is_verbatim(text: str, corpus: list[str]) -> bool:
    """True when `text` appears word for word (case and edge punctuation ignored) inside one corpus document."""
    need = norm_tokens(text)
    if not need:
        return False
    return any(contains_tokens(norm_tokens(doc), need) for doc in corpus)


def fmt_t(t: float) -> str:
    return f"{int(t // 60)}:{int(t % 60):02d}"


# ------------------------------------------------------------------------------------------------ script
def parse_script(md: str) -> list[dict]:
    """Spoken paragraphs of a script file: [{text, directions: [(TAG, body)], quotes: [str]}].

    Takes the `## Script` section when there is one (else the whole file). Headings, blockquotes (`>`), tables and
    `---` rules are skipped; a direction line (`**[SCREEN: ...]**`) attaches to the next spoken paragraph."""
    text = _nfkc(md)
    m = re.search(r"^##\s*script\b.*$", text, re.I | re.M)
    if m:
        rest = text[m.end():]
        nxt = re.search(r"^##\s+\S", rest, re.M)
        text = rest[:nxt.start()] if nxt else rest
    paras, pending = [], []
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith(("#", ">", "|", "---", "```")):
            continue
        dirs = DIRECTION_RE.findall(line)
        spoken = DIRECTION_RE.sub("", line).replace("**", "").strip(" *_-")
        if dirs:
            pending.extend((t.upper().replace("BROLL", "B-ROLL"), b.strip()) for t, b in dirs)
        if not spoken or re.fullmatch(r"[\W_]*", spoken):
            continue
        if re.match(r"^[-*]\s", raw.strip()) and not dirs:   # bullet metadata, not speech
            continue
        paras.append({"text": spoken, "directions": pending, "quotes": QUOTE_RE.findall(spoken)})
        pending = []
    return paras


def script_text_of(proj, explicit: str | None = None) -> tuple[str | None, str | None]:
    """(script markdown, path) from --script, project.json `script`, or plan/script.md|txt."""
    cands = []
    if explicit:
        cands.append(Path(explicit).expanduser())
    if proj is not None:
        pj = proj.root / "project.json"
        if pj.exists():
            try:
                sp = (read_json(pj) or {}).get("script")
                if sp:
                    cands.append(Path(sp))
            except ValueError:
                pass
        cands += [proj.root / "plan" / "script.md", proj.root / "plan" / "script.txt"]
    for c in cands:
        if c.is_file():
            return c.read_text(encoding="utf-8", errors="replace"), c.as_posix()
    if explicit:
        raise VeosError("INPUT_MISSING", f"script not found: {explicit}", "Check the --script path.")
    return None, None


# ------------------------------------------------------------------------------------------------ alignment
def sentences(words: list[dict], gap: float = 0.45, max_words: int = 18, min_words: int = 3) -> list[list[int]]:
    """Clause-sized word index groups: break after . ? ! , ; (and the Devanagari danda), on pauses >= gap, or at
    max_words; a fragment shorter than min_words joins the next clause (a name split off by a comma stays with it)."""
    raw, cur = [], []
    for i, w in enumerate(words):
        if cur and (words[i]["s"] - words[cur[-1]]["e"] >= gap or len(cur) >= max_words):
            raw.append(cur)
            cur = []
        cur.append(i)
        if re.search(r"[.?!।,;:]$", str(w.get("w", "")).strip()):
            raw.append(cur)
            cur = []
    if cur:
        raw.append(cur)
    out: list[list[int]] = []
    carry: list[int] = []
    for g in raw:
        g = carry + g
        if len(g) < min_words:
            carry = g
            continue
        out.append(g)
        carry = []
    if carry:
        if out:
            out[-1] += carry
        else:
            out.append(carry)
    return out


def align(words: list[dict], paras: list[dict]) -> tuple[list[int | None], list[str], list[int]]:
    """Map every transcript word to a script token: returns (word -> script token index, script tokens (original
    spelling), script token -> paragraph index)."""
    s_orig, s_norm, s_para = [], [], []
    for pi, p in enumerate(paras):
        for t in p["text"].split():
            nt = norm_tokens(t)
            if nt:
                s_orig.append(t)
                s_norm.append(nt[0])
                s_para.append(pi)
    w_norm = [(norm_tokens(w.get("w", "")) or [""])[0] for w in words]
    m: list[int | None] = [None] * len(words)
    sm = difflib.SequenceMatcher(None, w_norm, s_norm, autojunk=False)
    for a, b, size in sm.get_matching_blocks():
        for k in range(size):
            m[a + k] = b + k
    # fill short gaps (spelling differences) by interpolation between matched neighbours
    for i in range(len(m)):
        if m[i] is None:
            lo = next((j for j in range(i - 1, -1, -1) if m[j] is not None), None)
            hi = next((j for j in range(i + 1, len(m)) if m[j] is not None), None)
            if lo is not None and hi is not None and hi - lo <= 6 and m[hi] - m[lo] >= hi - lo:
                m[i] = m[lo] + (i - lo)
    return m, s_orig, s_para


# ------------------------------------------------------------------------------------------------ detection
def _loose(name: str) -> str:
    """Brand pattern that also matches the transcript's spellings: 'Context7' ~ 'context 7', 'Claude Code' ~ 'claude-code'."""
    out = ""
    for i, ch in enumerate(name):
        if ch == " ":
            out += r"[\s-]*"
            continue
        if i and name[i - 1] != " " and (name[i - 1].isalpha() != ch.isalpha()) and (name[i - 1].isalnum() and ch.isalnum()):
            out += r"[\s-]?"
        out += re.escape(ch)
    return out


def _brand_re(names) -> re.Pattern:
    alts = sorted({_loose(n) for n in names if n}, key=len, reverse=True)
    return re.compile(r"(?<![\w/])(" + "|".join(alts) + r")(?![\w])", re.I)


def _canon(found: str, names) -> str:
    low = re.sub(r"[\s-]+", "", found.lower())
    for n in names:
        if re.sub(r"[\s-]+", "", n.lower()) == low:
            return n
    return found


def _person_names(text: str, brands: set[str]) -> list[str]:
    """Capitalised word pairs that look like a person's name (not a brand, not the first word of the sentence)."""
    toks = re.findall(r"[A-Za-z][A-Za-z.'-]*|[,.;:!?]", text)
    out = []
    for i in range(1, len(toks) - 1):
        a, b = toks[i], toks[i + 1]
        if toks[i - 1] in ",.;:!?":
            continue
        if re.fullmatch(r"[A-Z][a-z]{1,15}", a) and re.fullmatch(r"[A-Z][a-z]{1,15}", b):
            pair = f"{a} {b}"
            if pair.lower() in brands or a.lower() in brands or b.lower() in brands or a.lower() in STOP:
                continue
            out.append(pair)
    return out


def detect(text: str, script_text: str, directions: list[tuple[str, str]], brands: list[str]) -> dict:
    """Score every category for one sentence. Returns {kind: {score, cues, name}}."""
    low = _nfkc(text).lower()
    full = _nfkc(script_text or text)
    flow = full.lower()
    hay = low + " \n " + flow
    res: dict[str, dict] = {}

    def add(kind, pts, cue, name=None):
        r = res.setdefault(kind, {"score": 0, "cues": [], "name": None})
        r["score"] += pts
        if cue not in r["cues"]:
            r["cues"].append(cue)
        if name and not r["name"]:
            r["name"] = name

    for kind, cues in CUES.items():
        for rx, pts in cues:
            got = re.search(rx, hay, re.I)
            if got:
                add(kind, pts, got.group(0).strip())
    brand_rx = _brand_re(brands)
    names = [_canon(b, brands) for b in brand_rx.findall(full) + brand_rx.findall(_nfkc(text))]
    for mm in re.finditer(r"\b([A-Z][\w.+-]{1,24}(?:\s[A-Z][\w.+-]{1,24})?)\s+" + PRODUCT_NOUNS + r"\b", full):
        nm = mm.group(1)
        at_start = mm.start() == 0 or re.search(r"[.?!,:;]\s*$", full[:mm.start()])
        if nm.split()[0].lower() not in STOP and not at_start:
            names.append(nm)
    if names:   # a product is one cue however many names the clause holds (score 2)
        uniq = list(dict.fromkeys(names))
        add("product", 2, uniq[0], uniq[0])
        res["product"]["cues"] += [n for n in uniq[1:] if n not in res["product"]["cues"]]
        res["product"]["names"] = uniq
    for oc in OUTLETS:
        if re.search(r"(?<!\w)" + re.escape(oc) + r"(?!\w)", full):
            add("headline", 2, oc, oc)
    bset = {b.lower() for b in brands}
    people = list(dict.fromkeys(_person_names(full, bset) + _person_names(_nfkc(text), bset)))
    if people:
        add("person", 1, people[0], people[0])           # a name alone is a weak cue; with a role word it is a person
        if re.search(re.escape(people[0]) + r"\s+(?:ka|ki|ke|ne|says|said)\b", full + " \n " + _nfkc(text)):
            add("person", 1, people[0] + " (possessive)")
    if "person" in res and not res["person"]["name"]:
        res["person"]["score"] = min(res["person"]["score"], 1)   # a role word with nobody named is not a photo moment
    for tag, body in directions:
        b = body.lower()
        if tag == "SCREEN":
            add("app_ui", 2, f"[SCREEN: {body[:60]}]")
        elif tag in ("B-ROLL", "VISUAL"):
            for kind, cues in CUES.items():
                if any(re.search(rx, b, re.I) for rx, _ in cues):
                    add(kind, 1, f"[{tag}: {body[:60]}]")
    q = QUOTE_RE.findall(full)
    if q and any(k in res for k in ("post", "headline")):
        k = "post" if "post" in res else "headline"
        add(k, 1, f'"{q[0][:40]}"')
    if "app_ui" in res and not res["app_ui"].get("name"):
        prod = res.get("product", {}).get("name")
        slash = re.search(r"(?:^|\s)(/[a-z][\w-]+)", hay)
        things = r"\b(website|site|app|dashboard|terminal|inbox|document|doc|spreadsheet|photo|image|page|file|form)\b"
        thing = re.search(things, low) or next((m for m in (re.search(things, b.lower()) for _, b in directions) if m), None)
        res["app_ui"]["name"] = prod or (slash.group(1) if slash else (f"the {thing.group(1)}" if thing else None))
    return res


def scan(words: list[dict], script_md: str | None = None, brands: list[str] | None = None,
         min_score: int = MIN_SCORE, label: str = DEFAULT_LABEL) -> list[dict]:
    """The candidate third-party moments, in time order (pure function: same input, same list)."""
    brands = list(brands or BRANDS)
    words = [w for w in words if isinstance(w, dict) and "s" in w and "e" in w]
    paras = parse_script(script_md) if script_md else []
    wmap, s_orig, s_para = align(words, paras) if paras else ([None] * len(words), [], [])
    groups = sentences(words)
    # directions belong to one sentence of their paragraph: the one sharing most words with the direction text
    dir_of: dict[int, list] = {}
    for pi, p in enumerate(paras):
        if not p["directions"]:
            continue
        cand = [gi for gi, g in enumerate(groups) if any(wmap[i] is not None and s_para[wmap[i]] == pi for i in g)]
        if not cand:
            continue
        for d in p["directions"]:
            dt = set(norm_tokens(d[1])) - STOP
            best = max(cand, key=lambda gi: (len(dt & set(norm_tokens(" ".join(words[i]["w"] for i in groups[gi])))), -gi))
            dir_of.setdefault(best, []).append(d)
    moments, seen, seen_names = [], set(), set()
    for gi, g in enumerate(groups):
        spoken = " ".join(str(words[i].get("w", "")).strip() for i in g).strip()
        idx = sorted(wmap[i] for i in g if wmap[i] is not None)
        if idx:   # keep the aligned tokens near the median (a stray match elsewhere in the script is dropped)
            med = idx[len(idx) // 2]
            idx = [j for j in idx if abs(j - med) <= len(g) + 4]
        script_text = " ".join(s_orig[min(idx):max(idx) + 1]) if idx else ""
        res = detect(spoken, script_text, dir_of.get(gi, []), brands)
        own = any(OWN_RE.search(b) for _, b in dir_of.get(gi, []))
        cands = sorted(((k, r) for k, r in res.items() if r["score"] >= min_score),
                       key=lambda kr: (-kr[1]["score"], PRIORITY[kr[0]]))
        pick = None
        for kind, r in cands:
            if kind == "product":   # each product once per reel ("Claude" after "Claude Code" is the same thing)
                fresh = [n for n in r.get("names") or [r.get("name")] if n and not any(
                    n.lower() in s or s in n.lower() for s in seen_names)]
                if not fresh:
                    continue
                r = dict(r, name=fresh[0])
            key = (kind, (r.get("name") or "").lower() or spoken.lower()[:40])
            if key in seen:
                continue
            pick = (kind, r, key)
            break
        if pick is None:
            continue
        kind, r, key = pick
        if own and kind == "app_ui":
            r = dict(r, own=True)
        seen.add(key)
        if r.get("name"):
            seen_names.add(r["name"].lower())
        for n in (res.get("product") or {}).get("names") or []:
            if kind in ("app_ui", "product") and n.lower() in (r.get("name") or "").lower():
                seen_names.add(n.lower())
        t0, t1 = round(float(words[g[0]]["s"]), 3), round(float(words[g[-1]]["e"]), 3)
        recipe = KIND_RECIPE[kind]
        quotes = QUOTE_RE.findall(script_text)
        sug = {"recipe": recipe}
        if recipe in QUOTE_RECIPES:
            sug["quote_text"] = quotes[0] if quotes else (script_text or spoken)
        if recipe in RECONSTRUCTIONS and label:
            sug["label"] = label
        name = r.get("name")
        plain = PLAIN[kind].format(name=name) if name else PLAIN_UNNAMED.get(kind, PLAIN[kind])
        moments.append({"kind": kind, "t0": t0, "t1": t1, "spoken": spoken, "script_text": script_text, "name": name,
                        "score": r["score"], "cues": r["cues"][:6],
                        "also": [k for k, _ in cands[1:]], "own_footage_hint": bool(r.get("own")),
                        "suggest": sug, "ask": f"{fmt_t(t0)} · {plain}"})
    moments = _merge(moments)
    for k, m in enumerate(moments, 1):
        m["id"] = f"M{k}"
    return [{"id": m.pop("id"), **m} for m in moments]


def _merge(moments: list[dict], gap: float = 1.0) -> list[dict]:
    """One moment per run: consecutive moments of one kind (same thing, or one of them unnamed) <= gap apart merge."""
    out: list[dict] = []
    for m in moments:
        p = out[-1] if out else None
        if p and p["kind"] == m["kind"] and m["t0"] - p["t1"] <= gap and (not p["name"] or not m["name"] or p["name"] == m["name"]):
            p["t1"], p["spoken"] = m["t1"], (p["spoken"] + " " + m["spoken"]).strip()
            p["script_text"] = (p["script_text"] + " " + m["script_text"]).strip() if m["script_text"] not in p["script_text"] else p["script_text"]
            p["cues"] = list(dict.fromkeys(p["cues"] + m["cues"]))[:6]
            p["score"] = max(p["score"], m["score"])
            if not p["name"] and m["name"]:
                p["name"] = m["name"]
                p["ask"] = f"{fmt_t(p['t0'])} · " + PLAIN[p["kind"]].format(name=m["name"])
            continue
        out.append(m)
    return out


def question(moments: list[dict]) -> str:
    n = len(moments)
    if not n:
        return ""
    head = (f"Do you have your own screenshot or clip for these {n} moments? If not, I'll make a clean card for each."
            if n > 1 else "Do you have your own screenshot or clip for this moment? If not, I'll make a clean card for it.")
    return head + "\n" + "\n".join(f"{i}. {m['ask']} (\"{m['spoken'][:70]}\")" for i, m in enumerate(moments, 1))


# ------------------------------------------------------------------------------------------------ records
def asset_origins(proj) -> dict[str, dict]:
    """plan/assets.json `assets` (written by `veos asset add --origin`)."""
    p = proj.root / "plan" / "assets.json" if proj is not None else None
    if p is None or not p.exists():
        return {}
    try:
        return dict((read_json(p) or {}).get("assets") or {})
    except ValueError:
        return {}


def asset_name(file: str) -> str:
    """'plan/assets/cc-shot.png' or 'cc-shot.png' or 'cc-shot' -> 'cc-shot'."""
    f = str(file).replace("\\", "/").rstrip("/")
    base = f.split("/")[-1]
    return base.rsplit(".", 1)[0] if "." in base else base


def corpus(proj, words: dict | list | None = None, data: dict | None = None, script_md: str | None = None) -> list[str]:
    """Quotable text: the script's spoken lines, the transcript, and what the creator typed (inserts.json)."""
    docs = []
    if script_md is None and proj is not None:
        script_md, _ = script_text_of(proj)
    if script_md:
        docs += [p["text"] for p in parse_script(script_md)]
        docs += [p for para in parse_script(script_md) for p in para["quotes"]]
    if words is None and proj is not None and (proj.work / "words.edit.json").exists():
        try:
            words = read_json(proj.work / "words.edit.json")
        except ValueError:
            words = None
    ws = words.get("words") if isinstance(words, dict) else words
    if ws:
        docs.append(" ".join(str(w.get("w", "")) for w in ws if isinstance(w, dict)))
        if any("caption" in w for w in ws if isinstance(w, dict)):
            docs.append(" ".join(str(w.get("caption", w.get("w", ""))) for w in ws if isinstance(w, dict)))
    if data:
        docs += [str(t) for t in data.get("creator_texts") or []]
    return [d for d in docs if d and d.strip()]


def record_problems(data, proj=None, corpus_docs: list[str] | None = None, style: dict | None = None,
                    scan_ids: list[str] | None = None) -> list[tuple[str | None, str, str]]:
    """[(insert id, message, fix)] for plan/inserts.json: schema, creator assets, verbatim quotes (fact_problem()
    tells the blocking ones apart)."""
    out: list[tuple[str | None, str, str]] = []
    if not isinstance(data, dict) or not isinstance(data.get("inserts"), list):
        return [(None, "plan/inserts.json needs an `inserts` list", "Write {\"version\": 1, \"inserts\": [...]} (engine/SPEC.md section 7).")]
    ins_cfg = (style or {}).get("inserts") or {}
    allowed = set(ins_cfg.get("create_fallbacks") or RECIPES) | {"citation_strip"}
    origins = asset_origins(proj) if proj is not None else {}
    adir = proj.root / "plan" / "assets" if proj is not None else None
    ids = set()
    for k, r in enumerate(data["inserts"]):
        if not isinstance(r, dict):
            out.append((None, f"inserts[{k}] is not an object", "Each insert is {id, moment, t0, t1, kind, origin, ...}."))
            continue
        rid = r.get("id")
        tag = rid or f"inserts[{k}]"
        if not rid:
            out.append((None, f"{tag} has no id", "Give every insert an id (I1, I2, ...)."))
        elif rid in ids:
            out.append((rid, f"insert id {rid} is used twice", "Make the ids unique."))
        ids.add(rid)
        for f in ("moment", "kind", "origin"):
            if not r.get(f):
                out.append((rid, f"{tag} has no `{f}`", f"Set `{f}` (see engine/SPEC.md section 7, inserts)."))
        try:
            t0, t1 = float(r.get("t0")), float(r.get("t1"))
            if not t1 > t0 >= 0:
                raise ValueError
        except (TypeError, ValueError):
            out.append((rid, f"{tag} needs t0 < t1 (edit seconds)", "Set t0/t1 to the moment's time range."))
        if r.get("kind") and r["kind"] not in KINDS + ("other",):
            out.append((rid, f"{tag}: unknown kind '{r['kind']}'", f"Use one of {', '.join(KINDS)} or other."))
        origin = r.get("origin")
        if origin and origin not in ("creator", "created"):
            out.append((rid, f"{tag}: origin '{origin}' is not allowed (creator | created). The engine never fetches media (NC-7)",
                        "Use the creator's own file (origin creator) or build a card (origin created)."))
        if origin == "creator":
            f = r.get("file")
            if not f:
                out.append((rid, f"{tag} is origin creator but has no `file`",
                            "Add the creator's file with `veos asset add <file> --origin creator` and set `file` to its name."))
            elif proj is not None:
                nm = asset_name(f)
                rec = origins.get(nm)
                exists = adir is not None and (any(adir.glob(nm + ".*")) or (adir / nm).is_dir())
                if not exists:
                    out.append((rid, f"{tag}: file '{f}' is not in plan/assets",
                                f"Run `veos asset add <the creator's file> --name {nm} --origin creator`."))
                elif not rec or rec.get("origin") != "creator":
                    out.append((rid, f"{tag}: asset '{nm}' was not added with --origin creator",
                                f"Re-add it: `veos asset add <file> --name {nm} --origin creator` (only the creator's own files are shown)."))
        if origin == "created":
            recipe = r.get("recipe")
            if not recipe:
                out.append((rid, f"{tag} is origin created but has no `recipe`", f"Set `recipe` to one of {', '.join(RECIPES)}."))
            elif recipe not in RECIPES:
                out.append((rid, f"{tag}: unknown recipe '{recipe}'", f"Use one of {', '.join(RECIPES)}."))
            elif recipe not in allowed:
                out.append((rid, f"{tag}: recipe '{recipe}' is not one of this style's created fallbacks",
                            f"Use one of {', '.join(sorted(allowed))} (tokens inserts.create_fallbacks)."))
            if not r.get("substitute_of"):
                out.append((rid, f"{tag}: a created insert names what it stands in for (`substitute_of`)",
                            "Set `substitute_of`, e.g. \"the post by X that the script reads out\"."))
            if recipe in QUOTE_RECIPES and not r.get("quote_text"):
                out.append((rid, f"{tag}: a {recipe} needs `quote_text` (the exact words it shows)",
                            "Copy the words from the script or transcript, verbatim."))
        qt = r.get("quote_text")
        if qt and corpus_docs is not None and origin != "creator" and not is_verbatim(qt, corpus_docs):
            out.append((rid, f"{tag}: quote_text \"{str(qt)[:60]}\" is not in the script, the transcript or the creator's own text (NC-13)",
                        "Quote only words that were said or written in the script, verbatim; never paraphrase someone's words."))
        src = r.get("source")
        if isinstance(src, dict) and src.get("headline") and corpus_docs is not None and origin != "creator" \
                and not is_verbatim(src["headline"], corpus_docs):
            out.append((rid, f"{tag}: headline \"{str(src['headline'])[:60]}\" is not quoted from the script or the creator",
                        "Use the exact headline as the script (or the creator) gives it."))
    known = set(scan_ids or [])
    covered = {str(r.get("moment")) for r in data["inserts"] if isinstance(r, dict)}
    dismissed = {str(d.get("moment")) for d in data.get("dismissed") or [] if isinstance(d, dict) and d.get("why")}
    for mid in sorted(known - covered - dismissed, key=lambda s: (len(s), s)):
        out.append((None, f"scanned moment {mid} has no insert record and was not dismissed",
                    f"Add an insert for {mid} (the creator's file or a created card), or list it under `dismissed` with a reason."))
    return out


# ------------------------------------------------------------------------------------------------ command
def add_args(p, cmd):
    p.add_argument("action", choices=["scan", "check"])
    p.add_argument("--script", default=None, help="scan: script file (default: project.json script, else plan/script.md)")
    p.add_argument("--min-score", type=int, default=MIN_SCORE, help="scan: cue score a sentence needs (default 2)")
    p.add_argument("--file", default=None, help="check: the record file (default plan/inserts.json)")


def _style(proj):
    try:
        from .tokens import effective_style, load_playbook, project_playbook
        return effective_style(load_playbook(project_playbook(proj, None, {})), warnings=[], errors=[])
    except Exception:  # noqa: BLE001 - the checks fall back to the defaults without a playbook
        return {}


def _brands(proj) -> list[str]:
    names = list(BRANDS)
    try:
        from .glossary import load_glossary
        gp = proj.root / "plan" / "glossary.json"
        g = load_glossary(gp if gp.exists() else None)
        names += [t["term"] for t in g.get("terms", []) if len(t.get("term", "")) > 2 and not t.get("ambiguous")]
    except Exception:  # noqa: BLE001 - the built-in list is enough
        pass
    return list(dict.fromkeys(names))


def main(args, project) -> dict:
    proj = need_project(project)
    if args.action == "scan":
        wp = proj.work / "words.edit.json"
        if not wp.exists():
            raise VeosError("NO_WORDS", "work/words.edit.json not found", "Run `veos transcribe` and `veos cut` first.")
        words = read_json(wp)
        md, spath = script_text_of(proj, args.script)
        ms = scan(words.get("words") if isinstance(words, dict) else words, md, _brands(proj), args.min_score, "")
        q = question(ms)
        ptrs = find_pointers(words.get("words") if isinstance(words, dict) else words)
        out = {"version": 1, "engine": "veos.inserts/1", "script": spath, "fetch": False, "moments": ms, "question": q,
               "pointers": ptrs}
        write_json(proj.path("plan", "inserts.scan.json"), out)
        return {"moments": len(ms), "by_kind": {k: sum(1 for m in ms if m["kind"] == k) for k in KINDS if any(m["kind"] == k for m in ms)},
                "question": q, "pointers": len(ptrs), "pointing": pointer_question(ptrs), "file": "plan/inserts.scan.json"}
    fp = Path(args.file) if args.file else proj.root / "plan" / "inserts.json"
    if not fp.exists():
        raise VeosError("NO_INSERTS", f"{fp.name} not found", "Write plan/inserts.json after asking the creator (reel-inputs).")
    try:
        data = read_json(fp)
    except ValueError as e:
        raise VeosError("BAD_INSERTS", f"inserts file is not valid JSON: {e}", "Fix the JSON syntax.")
    scan_ids = None
    sp = proj.root / "plan" / "inserts.scan.json"
    if sp.exists():
        scan_ids = [m.get("id") for m in (read_json(sp) or {}).get("moments", [])]
    probs = record_problems(data, proj, corpus(proj, data=data), _style(proj), scan_ids)
    recs = data.get("inserts") or []
    return {"passed": not probs, "problems": [{"insert": i, "msg": m, "fix": f} for i, m, f in probs],
            "inserts": len(recs), "creator": sum(1 for r in recs if isinstance(r, dict) and r.get("origin") == "creator"),
            "created": sum(1 for r in recs if isinstance(r, dict) and r.get("origin") == "created")}
