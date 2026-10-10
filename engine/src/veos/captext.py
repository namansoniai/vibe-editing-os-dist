"""Caption text handling (E-05): word classes, case, profanity mask, glossary spelling, Devanagari -> Latin
transliteration, and the two script transforms of `captions.transform`:

- transliterate: the script's romanised words are aligned to the transcript words (sequence alignment on a phonetic
  skeleton), so each word keeps its own timing and shows the script's spelling ("घंटा" -> "ghanta");
- translate: the script's sentences (in the caption language) are aligned to the spoken sentences, and each target word
  gets a time inside its sentence (proportional to its length, snapped to the spoken word onsets).

Everything here is pure (no project IO) so it can be unit-tested.
"""
from __future__ import annotations

import re
import unicodedata

DEVANAGARI = re.compile(r"[ऀ-ॿ]")
SENT_END = re.compile(r"[.?!।॥]+[\"'”’)]*$")
SOFT_PUNCT = re.compile(r"[,;:—–-]+[\"'”’)]*$")
_EDGE = re.compile(r"^([^\wऀ-ॿ$₹€£%#@]*)(.*?)([^\wऀ-ॿ%]*)$", re.S)

# function words: never emphasised, good chunk-break neighbours (English + romanised Hindi/Hinglish)
STOP_EN = set("""a an the and or but so nor yet for of to in on at by from with without into onto over under about above
below up down out off as than then that this these those there here it its it's i i'm i've me my mine we us our you you're
your yours he him his she her they them their is am are was were be been being do does did doing done have has had having
will would can could should shall may might must not no yes just only very really also too even still again ever never
what which who whom whose when where why how if because while though although until unless since all any some each every
both either neither such same other another more most much many few less least own s t don't can't won't isn't aren't
didn't doesn't wasn't weren't let's like get got gets go goes going went come came make makes made say says said see
know think want way thing things one ones lot lots kind sort bit""".split())
STOP_HI = set("""hai hain ho hoga hogi honge hona tha thi the tho toh to ka ki ke ko se me mein mai main mera meri mere tera
teri tere tum tumhe tumhara tumhari tumhare aap aapka aapki aapke hum hamara hamari humne maine tumne usne unhone ye yeh
wo woh vo is us iss uss in un inn unn aur ya par pe bhi hi nahi nahin na mat kya kyun kyon kaise kab kaun kahan jab tab
agar lekin magar kyunki ki ek do bas sab kuch koi bahut bohot zyada kam wala wali wale waala waali raha rahe rahi kar kare
karo karna karke karta karti karte kiya kiye ki gaya gayi gaye diya diye dena de deta deti dete lena le leta liya liye
hua hui hue jaata jaati jaate jata jati jate sakta sakti sakte sake chahiye abhi ab yaar bhai matlab achha accha
jo jis jise jisme jisse jiska jiski jiske jinka jinki jinke uska uski uske unka unki unke iska iski iske apna apni apne
phir fir wahi yahi waha yaha wahan yahan""".split())
STOPWORDS = STOP_EN | STOP_HI
# common romanised Hindi / Hinglish content words (STOP_HI holds the function words). A caption word that reads as
# romanised Hindi or a regional language is never a "misspelling" of a glossary term ("saal" is not "SaaS").
ROMAN_INDIC = set("""saal saalon baat baatein kaam kaamon naam paisa paise paison log logon din dino raat subah shaam
ghar duniya zindagi dil dimaag sach jhooth galat sahi theek thik accha acha achha bura bada badi bade chhota chhoti
chhote naya nayi naye purana purani puraane pura poora puri poori aaj kal parso hamesha kabhi pehle pahle baad
saath sath bina andar bahar upar neeche niche aage peeche piche paas door jaldi dheere sirf bilkul shayad zaroor
zarur pakka sabse jitna utna kitna kitne kitni itna itne itni uthna baithna dekho dekh dekha dekhna suno suna
socho socha samjho samjha samajh samajhna bolo bola bolna likho likha likhna padho padha padhna chalo chala chalna
banao banaya banana bana bani bane lagta lagti lagte laga lagi lage milta milti milte mila mili mile chahta chahti
chahte dhyan tarah tareeka tarika cheez cheezein jagah waqt samay saal mahina mahine hafta ghanta minute rupaye
rupees lakh lakhs crore crores hazaar hazar sau dus bees pachaas sath pachas aadmi aurat ladka ladki bachcha bacche
dost dosto doston bhaiyo behno log sabko sabki sabke khud apna apni apne pyaar pyar mazaa maza mast badhiya
bekaar bakwaas pagal kamaal kamal dhamaal zabardast""".split())
_INDIC_SHAPE = re.compile(r"aa|ii|uu|^(?:bh|dh|kh|jh|chh)[aeiou]")


def looks_roman_indic(word: str) -> bool:
    """True when a Latin-script word reads as romanised Hindi or another Indian language (a known word, a Hindi function
    word, or a shape English words rarely have: a doubled a / i / u, or a leading bh / dh / kh / jh / chh)."""
    w = norm(word)
    return w in STOP_HI or w in ROMAN_INDIC or w in _HINGLISH_ROMAN or bool(_INDIC_SHAPE.search(w))
COMMON_VERBS = set("""use uses used using try tries tried build builds built start starts started need needs needed take
takes took give gives gave look looks looked work works worked tell tells told feel feels felt keep keeps kept put puts
call calls called find finds found show shows showed help helps helped run runs ran turn turns turned""".split())
CONNECTORS_START = set("""and but so because or then that which who to of in for with when if while though aur lekin
magar toh kyunki ki ke jo jab agar""".split())
DANGLING_END = set("""a an the to of in on at by for with from into my your our their his her its this that these those
and or but is are was were be ka ki ke ko se me mein ek""".split())
NUM_WORDS = set("""zero one two three four five six seven eight nine ten eleven twelve thirteen fifteen twenty thirty
forty fifty sixty seventy eighty ninety hundred thousand million billion trillion lakh lakhs crore crores half double
triple dozen ek teen char chaar paanch panch chhe che saat aath nau das bees pachaas sau hazaar hazar""".split())
UNITS = set("""% percent per cent x times k m b bn mn kb mb gb tb kbps mbps fps px km m cm mm kg g mg lb lbs ml l
hours hour hrs hr minutes minute mins min seconds second secs sec s days day weeks week months month years year yrs
mahine mahina saal din ghante ghanta rupees rupee rs inr usd dollars dollar euros euro lakh lakhs crore crores cr l""".split())
CURRENCY = set("$ ₹ € £ rs rs. inr usd".split())
NUMBER_RE = re.compile(r"^[$₹€£]?[-+]?\d[\d,]*(\.\d+)?(k|m|b|bn|cr|l|x|%|st|nd|rd|th|s)?$", re.I)

PROFANITY = set("""shit shitty bullshit fuck fucking fucked fucker fuckin motherfucker bitch bitches dick dicks asshole
bastard crap damn goddamn piss pissed cunt chutiya chutiye bhenchod behenchod madarchod gandu gaandu bsdk""".split())
# profane roots found inside longer words (bullshit, motherfucker, fucking): the inner mask stars the root only
PROFANE_ROOTS = ("fuck", "shit", "bitch", "cunt", "dick", "piss", "crap", "damn")
INNER_STARS = (2, 3)  # the inner mask stars 2-3 letters and keeps the first and last letters


# ------------------------------------------------------------------------------------------------ tokens
def split_edges(w: str) -> tuple[str, str, str]:
    """('"', 'word', '",') for a token: leading punctuation, core, trailing punctuation."""
    m = _EDGE.match(w or "")
    return (m.group(1), m.group(2), m.group(3)) if m else ("", w or "", "")


def core(w: str) -> str:
    return split_edges(w)[1]


def norm(w: str) -> str:
    return core(w).lower().replace("’", "'")


def is_devanagari(w: str) -> bool:
    return bool(DEVANAGARI.search(w or ""))


def is_number(w: str) -> bool:
    c = norm(w)
    return bool(c) and (bool(NUMBER_RE.match(c.replace(" ", ""))) or c in NUM_WORDS or bool(re.match(r"^[०-९]+$", c)))


def is_unit(w: str) -> bool:
    return norm(w) in UNITS


def is_currency(w: str) -> bool:
    return norm(w) in CURRENCY or core(w) in ("$", "₹", "€", "£")


def is_stop(w: str) -> bool:
    return norm(w) in STOPWORDS


def sentence_end(w: str) -> bool:
    return bool(SENT_END.search((w or "").strip()))


def soft_break(w: str) -> bool:
    return bool(SOFT_PUNCT.search((w or "").strip())) and not sentence_end(w)


# ------------------------------------------------------------------------------------------------ case + mask
def apply_case(text: str, case: str, *, sentence_start: bool = False) -> str:
    """lower | upper | title | sentence | as_spoken (None). Devanagari is unaffected by case."""
    if not text or case in (None, "", "as_spoken", "none"):
        return text
    if case == "lower":
        return text.lower()
    if case == "upper":
        return text.upper()
    if case == "title":
        return " ".join(t[:1].upper() + t[1:] if t and not is_devanagari(t) else t for t in text.split(" "))
    if case == "sentence":
        if sentence_start:
            lead, c, trail = split_edges(text)
            if c:
                return lead + c[:1].upper() + c[1:] + trail
        return text
    return text


def _inner(c: str) -> str:
    """Star 2-3 letters in the middle of a word, keeping its first and last letters ('chutiya' -> 'ch***ya')."""
    if len(c) <= 2:
        return c[0] + "*" * (len(c) - 1)
    n = max(1, min(INNER_STARS[1], len(c) - 2))
    if len(c) - 2 >= INNER_STARS[0]:
        n = max(INNER_STARS[0], n)
    a = 1 + (len(c) - 2 - n) // 2
    return c[:a] + "*" * n + c[a + n:]


def _inner_mask(c: str) -> str:
    """The default mask: the profane root's inner letters become stars, the rest of the word stays
    ('SHIT' -> 'S**T', 'fuck' -> 'f**k', 'bullshit' -> 'bulls**t', 'fucking' -> 'f**king', 'bitch' -> 'b***h')."""
    lc = c.lower()
    for root in PROFANE_ROOTS:
        i = lc.find(root)
        if i >= 0:
            j = i + len(root)
            return c[:i] + _inner(c[i:j]) + c[j:]
    return _inner(c)


def is_profane(w: str, extra: set | None = None) -> bool:
    lc = split_edges(w)[1].lower()
    return bool(lc) and (lc in (PROFANITY | (extra or set())) or any(r in lc for r in ("fuck", "shit", "bitch")))


def mask_word(w: str, mode="inner", extra: set | None = None) -> str:
    """Mask a profanity. inner (the default): 2-3 stars inside the profane root, first and last letters kept
    ('SHIT' -> 'S**T', 'bullshit' -> 'bulls**t'); vowel: 'shit' -> 'sh*t'; full: '****'. Case is kept."""
    lead, c, trail = split_edges(w)
    if not c or not is_profane(c, extra):
        return w
    if mode == "full":
        m = "*" * len(c)
    elif mode in ("inner", True, None, ""):
        m = _inner_mask(c)
    else:  # vowel: the first vowel after the first letter
        m = c
        for k in range(1, len(c)):
            if c[k].lower() in "aeiou":
                m = c[:k] + "*" + c[k + 1:]
                break
        else:
            m = c[0] + "*" + c[2:] if len(c) > 2 else c
    return lead + m + trail


# ------------------------------------------------------------------------------------------------ glossary
def edit_distance(a: str, b: str, cap: int = 99) -> int:
    if a == b:
        return 0
    if abs(len(a) - len(b)) > cap:
        return cap + 1
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i] + [0] * len(b)
        for j, cb in enumerate(b, 1):
            cur[j] = min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb))
        prev = cur
    return prev[-1]


class Glossary:
    """Brand / term spellings. `canon(token)` maps an exact (case-insensitive) term or alias to the term's spelling;
    `near_miss(token)` finds a misspelling of a term ("elevanlabs" -> "ElevenLabs")."""

    def __init__(self, terms: list | None = None):
        self.terms: dict[str, str] = {}
        self.aliases: dict[str, str] = {}
        self.multi: list[tuple[list[str], str]] = []
        for t in terms or []:
            if isinstance(t, str):
                t = {"term": t}
            term = str(t.get("term") or "").strip()
            if not term:
                continue
            key = self._k(term)
            self.terms[key] = term
            for a in t.get("aliases") or []:
                self.aliases[self._k(a)] = term
            if " " in term:
                self.multi.append(([self._k(x) for x in term.split()], term))

    @staticmethod
    def _k(s: str) -> str:
        return re.sub(r"[^\wऀ-ॿ.+#]", "", str(s).lower())

    def canon(self, token: str) -> str | None:
        k = self._k(core(token))
        return self.terms.get(k) or self.aliases.get(k)

    def near_miss(self, token: str) -> str | None:
        """The glossary term this Latin-script word misspells, or None. Words that read as romanised Hindi or a regional
        language are never flagged (looks_roman_indic: "saal" is not "SaaS")."""
        c = core(token)
        k = self._k(c)
        if len(k) < 4 or k in self.terms or k in self.aliases or norm(c) in STOPWORDS or looks_roman_indic(c):
            return None
        best, bd = None, 99
        for tk, term in self.terms.items():
            if " " in term or abs(len(tk) - len(k)) > 2 or tk[:1] != k[:1]:
                continue
            d = edit_distance(k, tk, 3)
            lim = 1 if len(tk) < 7 else 2
            if 0 < d <= lim and d < bd:
                best, bd = term, d
        return best

    def __bool__(self):
        return bool(self.terms)


# ------------------------------------------------------------------------------------------------ Devanagari -> Latin
_V = {"अ": "a", "आ": "aa", "इ": "i", "ई": "ee", "उ": "u", "ऊ": "oo", "ऋ": "ri", "ए": "e", "ऐ": "ai", "ओ": "o", "औ": "au",
      "ऑ": "o", "ऍ": "e"}
_M = {"ा": "aa", "ि": "i", "ी": "ee", "ु": "u", "ू": "oo", "ृ": "ri", "े": "e", "ै": "ai", "ो": "o", "ौ": "au", "ॉ": "o",
      "ॅ": "e"}
_C = {"क": "k", "ख": "kh", "ग": "g", "घ": "gh", "ङ": "n", "च": "ch", "छ": "chh", "ज": "j", "झ": "jh", "ञ": "n", "ट": "t",
      "ठ": "th", "ड": "d", "ढ": "dh", "ण": "n", "त": "t", "थ": "th", "द": "d", "ध": "dh", "न": "n", "प": "p", "फ": "ph",
      "ब": "b", "भ": "bh", "म": "m", "य": "y", "र": "r", "ल": "l", "व": "v", "श": "sh", "ष": "sh", "स": "s", "ह": "h",
      "क़": "q", "ख़": "kh", "ग़": "gh", "ज़": "z", "ड़": "d", "ढ़": "rh", "फ़": "f", "य़": "y"}
_NUKTA = {"क": "क़", "ख": "ख़", "ग": "ग़", "ज": "ज़", "ड": "ड़", "ढ": "ढ़", "फ": "फ़", "य": "य़"}
_DIG = {chr(0x0966 + i): str(i) for i in range(10)}


# how Hinglish writers type the most common words (beats rule-based output), and English loanwords Whisper writes in
# Devanagari
HINGLISH = {"का": "ka", "की": "ki", "के": "ke", "कि": "ki", "में": "mein", "मैं": "main", "है": "hai", "हैं": "hain",
            "तो": "toh", "भी": "bhi", "ही": "hi", "लिए": "liye", "लिये": "liye", "या": "ya", "यह": "yeh", "वह": "woh",
            "ये": "ye", "वो": "wo", "नहीं": "nahi", "नही": "nahi", "हूँ": "hoon", "हूं": "hoon", "क्या": "kya", "से": "se",
            "को": "ko", "ने": "ne", "पे": "pe", "पर": "par", "ना": "na", "था": "tha", "थी": "thi", "थे": "the",
            "वाला": "wala", "वाली": "wali", "वाले": "wale", "और": "aur", "एक": "ek", "सब": "sab", "कुछ": "kuch",
            "बहुत": "bahut", "अब": "ab", "फिर": "phir", "जो": "jo", "तुम": "tum", "तुम्हें": "tumhe", "तुम्हारा": "tumhara",
            "तुम्हारी": "tumhari", "तुम्हारे": "tumhare", "आप": "aap", "हम": "hum", "मेरा": "mera", "मेरी": "meri",
            "मेरे": "mere", "करो": "karo", "कर": "kar", "करना": "karna", "करके": "karke", "हो": "ho", "हुआ": "hua",
            "दो": "do", "दे": "de", "लो": "lo", "जाओ": "jao", "जाए": "jaaye", "पहले": "pehle", "पहला": "pehla",
            "दूसरा": "doosra", "तीसरा": "teesra", "चौथा": "chautha", "बस": "bas", "यार": "yaar", "भाई": "bhai",
            "क्यों": "kyun", "कैसे": "kaise", "कब": "kab", "कहाँ": "kahan", "अगर": "agar", "लेकिन": "lekin",
            "मतलब": "matlab", "अच्छा": "accha", "सही": "sahi", "पूरा": "poora", "पूरे": "poore", "पूरी": "poori"}
LOANWORDS = {"यूज": "use", "यूज़": "use", "योज़": "use", "टाइप": "type", "रिलीस": "release", "रिलीज़": "release",
             "रिलीज": "release", "हैक": "hack", "प्रॉम्ट": "prompt", "प्रॉम्प्ट": "prompt", "प्रोम्प्ट": "prompt",
             "ऐप": "app", "एप": "app", "ऐप्स": "apps", "कोड": "code", "वेबसाइट": "website", "वीडियो": "video",
             "रील": "reel", "रील्स": "reels", "डिज़ाइन": "design", "डिजाइन": "design", "फाइल": "file", "फ़ाइल": "file",
             "प्लान": "plan", "मोड": "mode", "बट": "but", "ओके": "okay", "सेट": "set", "टूल": "tool", "टूल्स": "tools",
             "कमांड": "command", "कमांड्स": "commands", "फीचर": "feature", "फीचर्स": "features", "स्क्रीन": "screen",
             "लिंक": "link", "बायो": "bio", "कमेंट": "comment", "पेज": "page", "डेटा": "data", "एआई": "AI"}


_HINGLISH_ROMAN = set(HINGLISH.values())


def hinglish(word: str) -> str:
    """Devanagari word -> the usual Hinglish spelling (dictionary first, then rule-based transliteration)."""
    lead, c, trail = split_edges(word)
    c = c.replace("़", "") if c not in HINGLISH and c not in LOANWORDS else c
    for d in (LOANWORDS, HINGLISH):
        if c in d:
            return lead + d[c] + trail
    t = translit(c)
    t = re.sub(r"ee$", "i", t)
    t = re.sub(r"oo$", "u", t)
    return lead + t + trail.replace("।", ".")


def translit(word: str) -> str:
    """Devanagari -> Hinglish-style Latin (schwa deletion, long vowels shortened as people type them: करता -> karta,
    मैं -> main, हूँ -> hoon). Non-Devanagari characters pass through."""
    s = unicodedata.normalize("NFC", word or "")
    out: list[list] = []  # syllables: [consonant, vowel, explicit_vowel]
    i = 0
    while i < len(s):
        ch = s[i]
        nxt = s[i + 1] if i + 1 < len(s) else ""
        if nxt == "़" and ch in _NUKTA:  # nukta
            ch = _NUKTA[ch]
            i += 1
            nxt = s[i + 1] if i + 1 < len(s) else ""
        if ch in _C:
            out.append([_C[ch], "a", False])
        elif ch in _M and out:
            out[-1][1], out[-1][2] = _M[ch], True
        elif ch == "्" and out:  # virama
            out[-1][1], out[-1][2] = "", True
        elif ch in ("ं", "ँ"):  # anusvara / chandrabindu
            if out:
                out[-1][1] = (out[-1][1] or "") + "n"
                out[-1][2] = True
            else:
                out.append(["", "n", True])
        elif ch == "ः":
            out.append(["", "h", True])
        elif ch in _V:
            out.append(["", _V[ch], True])
        elif ch in _DIG:
            out.append([_DIG[ch], "", True])
        elif ch == "़":
            pass
        else:
            out.append([ch, "", True])
        i += 1
    n = len(out)
    cons = set(_C.values())
    # schwa deletion: the word-final inherent a, then medial inherent a's in V C[a] C V (right to left)
    if n > 1 and not out[-1][2] and out[-1][0] in cons:
        out[-1][1] = ""
    deleted = set()
    for k in range(n - 2, 0, -1):
        c, v, explicit = out[k]
        if explicit or c not in cons or (k - 1) in deleted:
            continue
        if out[k - 1][1] and out[k + 1][1] and out[k + 1][0] in cons:
            out[k][1] = ""
            deleted.add(k)
    # typed Hinglish shortens long vowels after the first syllable: karta, banane, nahin
    for k in range(1, n):
        out[k][1] = out[k][1].replace("aa", "a").replace("ee", "i")
    return "".join(c + v for c, v, _ in out)


# ------------------------------------------------------------------------------------------------ alignment helpers
def skeleton(w: str) -> str:
    """A rough phonetic key for matching a romanised transcript word with the script's spelling."""
    t = (translit(w) if is_devanagari(w) else w).lower()
    t = re.sub(r"[^a-z0-9]", "", t)
    for a, b in (("ph", "f"), ("w", "v"), ("z", "j"), ("q", "k"), ("sh", "s"), ("chh", "ch"), ("ee", "i"), ("oo", "u"),
                 ("aa", "a"), ("ck", "k"), ("c", "k"), ("y", "i")):
        t = t.replace(a, b)
    t = re.sub(r"(.)\1+", r"\1", t)
    return t


def similarity(a: str, b: str, _sk: dict | None = None) -> float:
    sk = _sk if _sk is not None else {}

    def keys(x):
        if x not in sk:
            k1 = skeleton(x)
            sk[x] = (k1, re.sub(r"[aeiou]", "", k1) or k1)
        return sk[x]
    sa, ca = keys(a)
    sb, cb = keys(b)
    if not sa or not sb:
        return 0.0
    if sa == sb:
        return 1.0
    if abs(len(sa) - len(sb)) > max(len(sa), len(sb)) * 0.6:
        return 0.0
    d1 = edit_distance(sa, sb) / max(len(sa), len(sb))
    d2 = edit_distance(ca, cb) / max(len(ca), len(cb))
    return max(0.0, 1.0 - 0.5 * d1 - 0.5 * d2)


def _lcs(a: str, b: str) -> int:
    prev = [0] * (len(b) + 1)
    for ca in a:
        cur = [0]
        for j, cb in enumerate(b, 1):
            cur.append(prev[j - 1] + 1 if ca == cb else max(prev[j], cur[j - 1]))
        prev = cur
    return prev[-1]


def same_word(spoken: str, written: str) -> bool:
    """The script token spells the spoken word (not a different word in the same slot): consonant skeletons differ by
    at most one inserted/deleted consonant (maine ~ mahine, ep ~ app, aap ~ apps) and never by a substitution
    (karta vs karke, hone vs hoga)."""
    a = re.sub(r"[aeiou]", "", skeleton(spoken))
    b = re.sub(r"[aeiou]", "", skeleton(written))
    if not a or not b:
        return skeleton(spoken)[:1] == skeleton(written)[:1]
    if a[0] != b[0] and not (len(a) == 1 or len(b) == 1):
        return False
    if abs(len(skeleton(spoken)) - len(skeleton(written))) > 2:
        return False
    return len(a) + len(b) - 2 * _lcs(a, b) <= 1


def parse_script(md: str) -> list[str]:
    """Spoken sentences from a reel script.md: skips headings, metadata bullets, bracketed directions [B-ROLL...] and
    block quotes; only the part under a '## Script' heading when there is one."""
    lines = (md or "").splitlines()
    for k, l in enumerate(lines):
        if re.match(r"^#{1,3}\s*script\b", l.strip(), re.I):
            lines = lines[k + 1:]
            break
    out = []
    for l in lines:
        s = l.strip()
        if not s or s.startswith(("#", ">", "-", "*", "|", "---")) or re.match(r"^\*\*\[.*\]\*\*$", s):
            if s.startswith("##"):
                break  # the next section (hook shortlist, notes)
            continue
        s = re.sub(r"\*\*\[[^\]]*\]\*\*", "", s)
        s = re.sub(r"\[[^\]]*\]", "", s).strip()
        if s:
            out += [x.strip() for x in re.split(r"(?<=[.?!।])\s+", s) if x.strip()]
    return out


def script_tokens(sentences: list[str]) -> list[str]:
    return [t for s in sentences for t in s.split() if core(t) or t.strip()]


def align_transliterate(words: list[dict], tokens: list[str], key="w") -> list[str | None]:
    """Needleman-Wunsch alignment of transcript words to script tokens on `similarity`. Returns, per word, the script's
    spelling for it, or None when the word should keep its own text (a Latin-script or number word the speaker said
    differently from the script) or fall back to transliteration (no good match). Script words the speaker skipped are
    dropped: captions show what is spoken."""
    n, m = len(words), len(tokens)
    if not n or not m or n * m > 400000:
        return [None] * n
    GAP_W, GAP_T = -0.35, -0.3
    cache: dict = {}
    src = [str(w.get(key, "")) for w in words]
    sim = [[similarity(src[i], tokens[j], cache) for j in range(m)] for i in range(n)]
    S = [[0.0] * (m + 1) for _ in range(n + 1)]
    P = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        S[i][0], P[i][0] = S[i - 1][0] + GAP_W, 1
    for j in range(1, m + 1):
        S[0][j], P[0][j] = S[0][j - 1] + GAP_T, 2
    for i in range(1, n + 1):
        si, Si, Sp = sim[i - 1], S[i], S[i - 1]
        for j in range(1, m + 1):
            best, bp = Sp[j - 1] + (si[j - 1] * 2 - 0.6), 0
            if Sp[j] + GAP_W > best:
                best, bp = Sp[j] + GAP_W, 1
            if Si[j - 1] + GAP_T > best:
                best, bp = Si[j - 1] + GAP_T, 2
            Si[j], P[i][j] = best, bp
    out: list[str | None] = [None] * n
    i, j = n, m
    while i > 0 and j > 0:
        bp = P[i][j]
        if bp == 0:
            wi, tj = i - 1, j - 1
            v = sim[wi][tj]
            latin = not is_devanagari(src[wi])
            if is_number(src[wi]):
                out[wi] = None                    # digits as spoken/transcribed
            elif latin:
                out[wi] = tokens[tj] if v >= 0.8 else None
            elif core(src[wi]) in LOANWORDS:
                out[wi] = tokens[tj] if norm(tokens[tj]).rstrip("s") == LOANWORDS[core(src[wi])].rstrip("s") else None
            elif core(src[wi]) in HINGLISH:
                out[wi] = tokens[tj] if same_word(HINGLISH[core(src[wi])], tokens[tj]) else None
            elif v >= 0.4 and same_word(src[wi], tokens[tj]):
                out[wi] = tokens[tj]
            i, j = i - 1, j - 1
        elif bp == 1:
            i -= 1
        else:
            j -= 1
    return out


def spoken_sentences(words: list[dict], key="w", pause_s=0.55) -> list[list[int]]:
    """Indices of the transcript grouped in sentences: punctuation, else pauses >= pause_s."""
    out, cur = [], []
    for k, w in enumerate(words):
        cur.append(k)
        txt = str(w.get("caption") if w.get("caption") else w.get(key, ""))
        nxt = words[k + 1] if k + 1 < len(words) else None
        gap = float(nxt["s"]) - float(w["e"]) if nxt else 9
        if sentence_end(txt) or gap >= pause_s or nxt is None:
            out.append(cur)
            cur = []
    return out


def align_translate(words: list[dict], sentences: list[str], key="w") -> list[dict]:
    """Target-language caption words with times. The script sentences (in the caption language) split the speech into
    consecutive blocks by dynamic programming: each block's share of the spoken text should match its sentence's share
    of the script, and block boundaries prefer speaker changes, sentence punctuation and pauses. Each target word then
    gets a slice of its block's speech time proportional to its length, snapped to the nearest spoken onset within
    0.18 s. Returns synthetic words {w, s, e, src: [word indices]}."""
    tgt = [x for x in sentences if x.strip()]
    n, T = len(words), len(tgt)
    if not n or not T:
        return []
    clen = [len(str(w.get("caption") or w.get(key, ""))) + 1 for w in words]
    pre = [0]
    for c in clen:
        pre.append(pre[-1] + c)
    tl = [len(x) + 1 for x in tgt]
    tpre = [0]
    for c in tl:
        tpre.append(tpre[-1] + c)
    ts, tt = pre[-1], tpre[-1]

    def bscore(i):  # quality of a block boundary after word i-1
        if i >= n:
            return 0.0
        a_, b_ = words[i - 1], words[i]
        txt = str(a_.get("caption") or a_.get(key, ""))
        gap = float(b_["s"]) - float(a_["e"])
        sc = 0.0
        if (a_.get("speaker") or a_.get("role")) != (b_.get("speaker") or b_.get("role")):
            sc += 3.0
        if sentence_end(txt):
            sc += 2.0
        elif soft_break(txt):
            sc += 0.8
        sc += 1.5 if gap >= 0.5 else 0.8 if gap >= 0.25 else 0.3 if gap >= 0.1 else -1.0
        return sc
    bs = [0.0] + [bscore(i) for i in range(1, n + 1)]
    INF = 1e18
    D = [[INF] * (T + 1) for _ in range(n + 1)]
    Bk = [[0] * (T + 1) for _ in range(n + 1)]
    D[0][0] = 0.0
    for t in range(1, T + 1):
        exp_end = tpre[t] / tt * n
        span = max(6, int(n * 0.35))
        lo_i, hi_i = max(t, int(exp_end - span)), min(n - (T - t), int(exp_end + span) + 1)
        for i in range(lo_i, hi_i + 1):
            best, bj = INF, 0
            for j in range(t - 1, i):
                if D[j][t - 1] >= INF:
                    continue
                c = D[j][t - 1] + 10 * abs((pre[i] - pre[j]) / ts - tl[t - 1] / tt) - 2.0 * bs[i]
                if c < best:
                    best, bj = c, j
            D[i][t], Bk[i][t] = best, bj
    if D[n][T] >= INF:
        return []
    blocks, i = [], n
    for t in range(T, 0, -1):
        j = Bk[i][t]
        blocks.append((list(range(j, i)), [t - 1]))
        i = j
    blocks.reverse()
    out = []
    for idx, tsx in blocks:
        s0, s1 = float(words[idx[0]]["s"]), float(words[idx[-1]]["e"])
        onsets = [float(words[k]["s"]) for k in idx]
        toks = [x for ti in tsx for x in tgt[ti].split()]
        if not toks:
            continue
        wts = [len(core(x)) + 2 for x in toks]
        tot = sum(wts)
        cum = [0.0]
        for w_ in wts:
            cum.append(cum[-1] + w_)
        # anchors: the same word in both languages (numbers, English terms in Hinglish speech) pins its time
        pts, j0 = [(0.0, s0)], 0
        for k, x in enumerate(toks):
            cx = norm(x)
            if len(cx) < 2 and not is_number(x):
                continue
            for jj in range(j0, len(idx)):
                sw = words[idx[jj]]
                st = str(sw.get("caption") or sw.get(key, ""))
                if (is_number(x) and is_number(st) and norm(st) == cx) or (len(cx) >= 3 and not is_devanagari(st)
                                                                             and similarity(x, st) >= 0.85):
                    t_ = float(sw["s"])
                    if t_ > pts[-1][1] and cum[k] > pts[-1][0]:
                        pts.append((cum[k], t_))
                        j0 = jj + 1
                    break
        pts.append((tot, s1))

        def at(c):
            for (c0, t0), (c1, t1) in zip(pts, pts[1:]):
                if c <= c1:
                    return t0 + (t1 - t0) * ((c - c0) / (c1 - c0) if c1 > c0 else 0)
            return s1
        prev_s = s0 - 1
        for k, x in enumerate(toks):
            s = at(cum[k])
            e = at(cum[k + 1])
            near = min(onsets, key=lambda o: abs(o - s))
            if abs(near - s) <= 0.18 and near > prev_s + 0.06:
                s = near
            s = max(s, prev_s + 0.06)
            prev_s = s
            src = [kk for kk in idx if float(words[kk]["s"]) < e and float(words[kk]["e"]) > s] or [idx[0]]
            out.append({"w": x, "s": round(s, 3), "e": round(max(e, s + 0.06), 3), "src": src})
    for k in range(len(out) - 1):  # contiguous, non-overlapping
        out[k]["e"] = round(min(out[k]["e"], out[k + 1]["s"]), 3) if out[k + 1]["s"] - out[k]["e"] < 0.12 else out[k]["e"]
        if out[k]["e"] <= out[k]["s"]:
            out[k]["e"] = round(out[k]["s"] + 0.04, 3)
    return out
