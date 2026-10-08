# Two-Tier Hero Style Playbook (template v1)

**Purpose.** You (Claude) receive {{BV-01.name|the creator}}'s talking-head footage shot at a desk, plus the script. This playbook makes you cut it into a fast, word-led reel where **the words are the graphics**: word-by-word two-tier captions at chest height, one giant hero word or number standing *behind* the presenter's head, whip-cut jump rhythm, and short stylised inserts landing on the exact noun.

**Input it expects (SW-01 `talking_head`):** one presenter at a desk (setup A, §12.1), optionally 1–2 props for the hook, the creator's own B-roll, screen recordings, and a QR image or keyword for the CTA. Everything missing has a fallback (§12.3).

**Inspired by:** Tharun Speaks (evidence: `vibe-editing-os-research/analysis/short/tharun-speaks.md`, five reels v01–v05). Evidence map: App. B and `evidence.md`.

### Style DNA `[DNA]`
A warm, low-key desk shot chopped every 1–2 s, where almost every cut changes the crop (wide / mid / tight) and about once per 10 s the camera itself punches in with a motion-blurred zoom, where every spoken phrase appears word by word on the presenter's chest in **two tiers**: small white connector words (56 px) stacked around **one oversized keyword** (136 px). On the big moments a **hero word or neon number** (200–560 px condensed caps) slams in *behind the head*, so the hair and shoulders occlude it like a magazine cover. Numbers are **performed** (odometer rolls, year rulers, step counts), never just shown. Hooks hold a real **prop** that carries the result (a red glass vs a green glass, a photo, a handwritten card). Inserts are 1–2 s, full-bleed and stylised (halftone, invert, B&W, warm tint) or dark glass explainer cards. One **neon accent per reel** (lime, mint or yellow) and white; red and green only for a result pair.

**Copy these 5 things (they make it read as this style):**
1. **Two-tier word-by-word chest captions**: connector 56 px + keyword 136 px (ratio ≥ 1.7), split stack, one keyword per chunk at most. → §5.3 CS-1
2. **Hero behind the head**: a grit-white word or a neon number, 200–560 px, landed by 1.7 s in the hook and on every item's key noun (E1). → §5.2, P-01…P-06
3. **Punch-cut rhythm (dynamic zoom)**: a cut every 1.0–2.1 s (median), and 9 of 10 face-to-face cuts change the crop (wide 1.00 · mid 1.15–1.22 · tight 1.30–1.45); on top, an animated blur-punch, settle or zoom-blur cut about once every 10 s and 1-frame white flashes into inserts. Never two identical crops in a row. → §9, §10.2
4. **A prop (or its engine twin) carries the hook's result**, tagged with a counter or a hand label. → §6.2, P-09…P-12
5. **Short stylised inserts on the noun**: 0.8–2.2 s creator B-roll with a rotating treatment, or a dark glass card, then straight back to the face. → P-24, P-31

### Directives `[DNA]`
| # | Directive | Where it lives |
|---|---|---|
| D1 | **The words are the graphic.** Every spoken word appears on screen, word by word, in two tiers. Graphics never replace the captions; they sit around them | §5.3, H12 |
| D2 | **A hero behind the head by 1.7 s.** The first hero word or number lands behind the presenter before 1.7 s and stays ≥ 1.5 s | §6.2, H1, H3 |
| D3 | **Numbers are performed.** Every spoken amount, count, duration or year rolls, steps or slides into place on its word | §8.3 B-3, §18 |
| D4 | **Never static.** A cut, punch, flash, hero, insert or caption swap at least every 1.2 s; nothing sits still for 2.0 s | §7.6, H2 |
| D5 | **Concrete before abstract.** A prop, a product, a person or a card shows the thing named, on its noun (lead 2 f) | §8.4, H5 |
| D6 | **One neon per reel.** White + the reel's neon accent; red/green only as a result pair; never a third bright hue | §4, H14 |
| D7 | **Short, stylised inserts.** Full-frame inserts last 0.8–2.2 s each; a graphic run never exceeds 5.0 s without the face | §3.6, H8 |
| D8 | **Money is Indian.** Rupee amounts use ₹ and Indian grouping (₹1,20,000; ₹2.5 Cr) unless the buyer's language moves them to international | §5.5, H11 |

Buyer directives `BD1…` `[VAR]` go here; they may only make the style stricter or more specific.

### Quick index
| § | What | Status |
|---|---|---|
| §0 | Style profile (switches) | ON |
| §1 | Procedure P1–P15 | ON |
| §2 | Hard rules, exceptions E1/E5/E6, H1–H18, N1–N14 | ON |
| §3 | Worlds W-, layouts L-, stage moves G-, safe zones, presenter | ON |
| §4 | Colour, rotating neon packs TH-, grades and clip treatments | ON |
| §5 | Type, hero recipes, caption profiles CS-1…CS-4 | ON |
| §6 | Hook system: HA-08 default, HA-01/HA-07/HA-05 alternates, CTA | ON |
| §7 | Structure, markers SM-1…SM-4, ritual, re-hook, cadence | ON |
| §8 | Visual system: families B-1…B-7, patterns P-01…P-44 | ON |
| §9 | Transitions T-01…T-12 | ON (§9.3 OFF) |
| §10 | Motion, camera Z-1…Z-7, layers, finishing | ON |
| §11 | Sound contract | ON (minimal) |
| §12 | Footage, shots SH-, fallbacks FB-, props, inserts | ON |
| §13 | Output contract | ON |
| §14 | Worked examples (3) | ON |
| §15 | QA | ON |
| §16 | Frame template | OFF |
| §17 | Anchored graphics (running state OFF) | ON (anchors) |
| §18 | Data contract | ON |
| §19 | Citations | OFF |
| §20 | Dialogue | OFF |
| §21 | Canvas camera | OFF |
| §22 | Ink layer (hand tags, arrows, branches) | ON |
| §23 | Continuity (hub spine) | ON |
| §24 | Series | OFF |
| §25 | End cards (QR card, end lockup) | ON |
| C–F | Exceptions & core, personalisation, deviations, IDs | ON |
| App. A / B | Hero & hook bank / evidence map | ON |

Formats: **F-A "Two-tier hero talking head"** (the only format). Themes: **TH-lime, TH-mint, TH-yellow** (rotate per reel).

---

## §0 Style profile `[REQ]`

```yaml
profile:                         # mirrored in tokens.json → profile
  source_type: talking_head
  presenter: {presence: host, share: [60, 80], max_absence_s: 5.0}
  spine: talking_head
  captions: {mode: full, role: primary, mute_policy: mute_safe}
  graphics: support
  duration: {class: standard, target_s: [55, 90]}
  language: {speech: en, captions: {lang: en, script: Latn, transform: verbatim}, on_screen: en, post_title: en,
             supported: [[en, en, Latn], [hinglish, hinglish, Latn], [hi, hi, Deva]]}
  numbers: {grouping: international, currency: "$", compact: k_m_b, units: metric, decimals: 0, style: full}
  tone: {energy: hype, comedy: off, comedy_max: light}
  themes: {policy: per_reel, packs: [TH-lime, TH-mint, TH-yellow], default: TH-lime}
  formats: {list: [F-A], default: F-A}
  footage_dependency: medium
  cta: {devices: [qr, comment_keyword, link_bio, end_card], placement: mid+end, chosen: null}
  modules: {chrome: false, running_state: false, anchors: true, data_figures: true, citations: false,
            dialogue: false, canvas_camera: false, ink: true, continuity: true, series: false, brand: false}
```

Why each value:
- **source_type: talking_head**: all five reels are one presenter at a desk; B-roll and props are inserted around the take (v01–v05).
- **presenter: host 60–80, max absence 5.0 s**: face visible ≈ 60–75% of runtime (v05 ≈ 60%, v01/v03/v04 ≈ 70–75%). Full-screen runs are mostly 1–4 s; the two longer runs seen (v01 @0:31–0:40 glow flow, v05 @0:40–0:47 offer) are capped here at 5.0 s and continued in L-stack so the face stays one glance away.
- **spine: talking_head**: the A-roll take is the timeline; every insert is cut on a spoken noun.
- **captions: full / primary / mute_safe**: captions run ≈ 90–95% of runtime and are the strongest element after the hero (v05 @0:02 "rupees / per month"); the reel reads with sound off.
- **graphics: support**: graphics fill 25–45% of runtime (B-roll and cards), the rest is captions on the face.
- **duration: standard 55–90 s**: measured 58–89 s. One mid-reel re-hook (§7.4).
- **language: default en → en verbatim** `(unverified)`: on-screen captions are English in all five reels and read like verbatim speech ("you can make up to … rupees per month", v05 @0:00–0:02); the speech itself was not transcribed. The buyer chooses (BV-05) between the three language options (English, Hinglish, Hindi).
- **numbers: Indian ₹ in the evidence** (the template default is English, so `$`; Numbers follow the language (BV-06): English → international `$` and K/M/B (unless the buyer picks ₹); Hinglish / Hindi → ₹ with Indian grouping and lakh / crore.): "1,20,000" (v05 @0:01), "₹60/DAY" (v05 @0:15), "3 lakhs" (v01 @1:11), "₹1.82L" (v01 @0:56). v01's international "₹500,000" is treated as an inconsistency and not copied (Part E).
- **tone: hype, comedy off (max light)**: fast cuts, slams and glows, no meme gags in the evidence.
- **themes: per_reel rotation**: the neon accent changes per reel (lime v01/v02, yellow v04, mint v05).
- **formats: F-A only**: one visual system across all five reels.
- **footage_dependency: medium**: props, handwritten cards and team B-roll lift it; every one has a fallback.
- **cta: qr / comment_keyword / link_bio / end_card, mid+end**: QR cards on white in v01, v02, v03, v04, v05; "in bio" in v02 @0:47; end lockups in v03 @0:59 and v05 @1:00; v02 and v04 show the QR twice (mid and end).
- **modules**: anchors (prop tags and arrows sit on objects), data_figures (every performed number is a figure), ink (hand-drawn arrows and branches: v02 @0:01.5, v02 @0:26, v04 @0:27, v04 @0:50), continuity (the hub spine returns per item: v03 @0:06, @0:16, @0:31, @0:50). running_state is OFF (Part E).

---

## §1 Procedure (follow in order) `[REQ] [DNA]`

1. **P1 Inventory.** ffprobe every input (resolution, fps, duration, audio). Conform to 30 fps CFR. Identify setup A / B (§12.1). Register every asset with its origin (`creator` or `created`). List the props seen in the hook take (PR-1…PR-5).
2. **P2 Matte (required).** Generate the person matte for the whole A-roll (RVM). QA hair at 200% on the frames where a hero will sit (E1). No matte → no behind hero: the hero moves above the head (P-05 lockup, clear of the face by 40 px) and the checkpoint says so.
3. **P3 Transcribe** with word timestamps. Apply `language.captions.transform` (default verbatim). Apply the glossary and the profanity mask (`inner`: f**king; v04 @0:39). Brand names exact.
4. **P4 Segment** into HOOK (0–4.5 s), PROMISE/LOOP, ITEM-1…N, REHOOK (one, at 40–60%), PAYOFF, CTA. Mark jump-cut points on word boundaries (±1 f) wherever a breath, retake or pause ≥ 150 ms sits.
5. **P5 Classify** every sentence with a line type (§8.4) and mark its **trigger word**.
6. **P6 Tone-tag** every sentence: `hype` · `explain` · `warn` · `win` · `cta`.
7. **P7 Keyword-tier assignment (this style's craft).** Walk the caption chunks (1–4 words) and mark **at most one keyword per chunk** (tier 2, 136 px), by this priority: (1) a number with its unit word ("₹60", "3 skills"), (2) a proper noun or brand ("Germany", "Instagram"), (3) the topic noun ("degree", "portfolio"), (4) a contrast verb or adjective ("seriously", "acquired", "messy"). Never a pronoun, article, preposition or auxiliary. Target **35–50% of chunks with a keyword**, never more than 3 keyword chunks in a row, ≤ 1 keyword per second. Words that a hero shows at the same moment are **dropped from the caption** (`captions.overrides {i, text: ""}`) so the number or word appears once. Force or block a keyword with `captions.overrides {i, emph: true | false}`.
8. **P8 Hero plan.** Pick the hook hero (§6.2) and one hero per item: a grit word (P-01/P-02/P-05) for names and claims, a neon number (P-03/P-04/P-06) for every amount, count, duration or year. 3–7 heroes per minute. Write each hero's placement against the face box (§5.2 "placement").
9. **P9 Hook plan.** Pick the archetype (default HA-08), write **3 hook variants** with their hero and prop/fallback, run the stopper tests (§6.1).
10. **P10 Visual plan.** A pattern per line (§8.4); the figure plan for every number (§18, `plan/figures.json`); the clip-treatment rotation for every creator clip (§4.4); the **anchor pass** for prop tags, hand arrows and desk chips (§17): read sampled frames and write the static anchor point of each target.
11. **P11 Beat sheet** (§13): one beat per trigger, meeting the cadence targets (§7.6).
12. **P12 Sound + transitions.** The SFX ledger from the bundled pack (§11) and the transition map (§9).
13. **P13 Assets and inserts.** Ask once for third-party moments (§12.5), build or collect assets, resolve fallbacks (§12.3) and list the ones used.
14. **P14 Checkpoint** (§13.5), then **wait for approval.**
15. **P15 Build:** act by act → `veos validate` → preview and QA (§15, max 3 passes) → render.

---

## §2 Hard rules `[REQ] [DNA]`

### 2.1 Editing rules (every style)
The nine editing rules in `playbooks/_global/GLOBAL-RULES.md` apply. They are directions, not limits: smooth, seamless motion; nothing overlaps by accident; keep the face clear (behind the speaker is fair game, text included); readable at a glance; one idea at a time; show what's being said; never fake facts; pace like the style, not like a timer; the style decides the look.
- **Facts the engine checks:** accidental overlaps, jumps, the face covered, unreadable text, numbers and quotes that don't match what was said, the promised count. Every count, timing and budget this playbook gives is direction for the edit, not a limit.
- **Retired (8 Oct 2026), whatever this playbook says below:** no REPRESENTATIONAL or example labels on made-up cards, no credit lines, no flash limit (flash as often as this style calls for; any "NC-11" cap below no longer applies), and text may sit behind the speaker without an exception.

### 2.2 Declared exceptions
| E-id | Use in this style | This style's limits (never looser than the registry) | DNA reason | Evidence |
|---|---|---|---|---|
| **E1** behind-subject type | Hero words and hero numbers stand behind the presenter's head and shoulders | `behind: true`; TC-display only; visible glyph area **≥ 65%** for the whole hold; the first and last letters ≥ 50% visible; **≤ 1** behind hero at a time; hold **≥ 0.6 s** (style default 1.5–3.0 s); matte edge checked at 200% on hair | The magazine-cover depth is the style's signature | "3 SKILLS" v03 @0:00.17; "18 YO" v02 @0:01; "1,20,000" v05 @0:01; "5 YEARS" v04 @0:01.3; "15 DAYS" v04 @0:32 |
| **E5** edge bleed | Hero words and statements may run to 24 px from the frame edges | TC-display ≥ 180 px only; margin ≥ 24 px; glyphs never cropped; never inside the NC-5 bands (y < 110, y > 1540, or x > 970 between y 900 and 1540); ≤ 1 at a time | Edge-to-edge condensed type | "IT DOESN'T MATTER HOW CAPABLE YOU ARE" v03 @0:08–0:10; "FOCUS" v03 @0:41; "1,20,000" v05 @0:01.5 |
| **E6** hard swap | Odometer digits and step counts change inside a fixed slot | The digit slot rect constant ±4 px; only the digits change; the slot's entry and exit stay eased | Numbers are performed in place | "₹150,263 → ₹500,000" v01 @0:02.17–0:02.83; "1 → 4 YEARS → 5 YEARS" v04 @0:01.0–0:01.33 |

### 2.3 Style MUST rules
- **H1. Frame 0** shows the presenter (L-full) with live camera motion starting at f0: a Z-6 settle-out (1.22 → 1.00 over 12 f; from 1.5 with a T-06 defocus when the take opens on a hair flick or a hand to the lens) or a Z-4 settle-push (1.00 → 1.18 over 8 f), the prop already in frame when the hook uses one, and the first caption word on screen by f3. check: V-F0
- **H2. Cadence:** weighted state changes 10–28 per 10 s in the body, ≥ 8 in 0–3 s; no gap > 1.2 s (0.8 s in the hook) between weight-1 changes; nothing static (no change and no continuous motion) for 2.0 s. check: V-CADENCE
- **H3. Payoff by 1.7 s:** the hook hero (grit word or neon number) is fully landed behind the head by 1.7 s and holds ≥ 1.5 s. check: V-F0
- **H4. Hero limits:** ≤ 3 words (or one number + one unit word), ≤ 2 lines, readable at 25% scale (cap height ≥ 160 px), one hero at a time, 3–7 heroes per minute. check: review
- **H5. On the word:** every hero, insert, card, tag and counter starts 2 f before its trigger word's onset and is fully landed within ±5 f; counters land on the number word ±5 f. check: V-ONWORD
- **H6. Face rule:** nothing is drawn in front of the face box; front-layer text keeps 40 px from it; only E1 heroes pass behind the head. check: V-FACE
- **H7. Behind-head occlusion:** every behind hero meets E1 (≥ 65% visible, first and last letters visible) on every frame of its hold; if the presenter moves into it, shorten the hold or move the hero, never accept the occlusion. check: V-EXC
- **H8. Presenter presence:** face visible 60–80% of runtime; no full-screen run without the face longer than 5.0 s (continue in L-stack instead). check: V-PRESENCE
- **H9. Promise integrity:** the hook's count equals the items shown; every "till the end / last secret" is paid on screen; the CTA keyword, URL or QR is on screen ≥ 1.5 s. check: V-PROMISE
- **H10. Truth:** every displayed number traces to the script or a declared input in `plan/figures.json`; results and earnings are the creator's own or script-stated; illustrative counters carry the "example" tag. check: V-DATA
- **H11. Number format:** the format follows BV-05/BV-06: English → `$`, international grouping, K/M/B; Hinglish / Hindi → ₹ glyph (never Rs/INR), Indian grouping (₹1,20,000), lakh/crore compacts (₹2.5 L, ₹1.2 Cr). check: V-NUMFMT
- **H12. Captions:** every spoken word is captioned (except words a hero shows at that moment); 1–4 words per chunk; shown ≤ 0.15 s before the word; at most one keyword per chunk; glossary spellings exact. check: V-CAPTION
- **H13. Tier ratio:** keyword px ÷ connector px ≥ 1.7 on every chunk with a keyword (default 136 / 56 = 2.43; measured 1.75–2.6). check: V-CAPTION
- **H14. Hues:** ≤ 2 bright hues per frame: the reel's neon + one of bad/good, or bad + good in a result pair (then no neon). White, black and greys are not bright hues. check: V-HUES
- **H15. Dead air:** at most 1 gap ≥ 150 ms per 15 s, except a deliberate ≤ 0.3 s beat before a twist line. Cuts on word boundaries ±1 f. check: review
- **H16. Safe zones:** meaning text inside x 64–1016, y 110–1500, except E5 heroes (24 px margin) and the NC-5 bands, which nothing crosses. check: V-SAFE
- **H17. Inserts:** every full-frame insert is 0.8–2.2 s (a T-12 flicker montage counts as one insert, ≤ 1.5 s, clips 5 f each); consecutive creator clips never share a treatment. check: review (V-GRADE when the engine has it)
- **H18. Audio:** −14 LUFS integrated, true peak ≤ −1.5 dBTP, bed ≥ 18 dB under the voice, hard end ≤ 6 f after the last word (NC-8). check: review (mix gate)

### 2.4 NEVER
- **N1.** A hero in front of the face, or a hero that the head covers beyond E1 (a word you can't read is not a hero).
- **N2.** Two heroes at once, or a hero and a full-frame statement at once.
- **N3.** Coloured caption words. Captions are white on footage and dark worlds, ink on light worlds; emphasis is size only.
- **N4.** A third bright hue; red used as decoration; the neon used for a loss.
- **N5.** Static full-screen slides longer than 2.2 s without an internal event; text-heavy cards (more than 6 rows, or body text under 40 px carrying the point).
- **N6.** Stock clichés: handshake stock, piles of cash, generic "success" sunsets, lightbulbs, rockets, matrix code.
- **N7.** Fake earnings screenshots, fake testimonials, dashboards with invented numbers presented as real (NC-6). Generic dashboards carry no unsourced number.
- **N8.** A drawn QR code. The QR card uses the buyer's own QR image only (FB-7 otherwise).
- **N9.** Transitions outside T-01…T-12; zooms outside Z-1…Z-7; a zoom that returns to its start inside the shot (the creator never bounces back; a punch holds until the next cut); the same transition 3× in a row (the T-01/T-03 alternation excepted); the same Z twice in a row.
- **N10.** Hero words that repeat the caption at the same moment (drop the caption word, H12).
- **N11.** Lowercase heroes. Heroes are uppercase grit words or numerals; captions are as spoken.
- **N12.** Handwriting fonts for anything but hand tags and branch labels (P-11, P-23, P-27, P-39).
- **N13.** Light leaks, film burns, RGB-split packs, lens-flare PNGs.
- **N14.** Third-party media the creator did not hand over (NC-7): another creator's clip, a news screenshot, a celebrity photo. Build the created substitute (§12.5).

Buyer additions `BN1…` `[VAR]` go here.

---

## §3 Worlds, layouts, stage moves, safe zones `[REQ] [DNA; coordinates TUNE ±5%]`

### 3.1 Worlds
| ID | Kind | Look | Carries | Enter / exit |
|---|---|---|---|---|
| **W-room** | footage | The creator's own desk room, low-key and warm (measured `#2A1C14`–`#4A3220` midtones), lamp bokeh, the desk surface in the bottom 15–25% | Everything spoken to camera, heroes, prop hooks | Hard cut, whip (T-02), punch |
| **W-glass** | stage | Navy `#0E1A44` → `#050713` (gradient `glass-navy`), a soft `accent` glow (16%, r 520 at x 540, y 820, slow drift), noise 0.03, vignette 0.25 | Glass app cards (P-24), spotlight stack (P-18), slider (P-14), recap (P-22), token carousel (P-19, with a violet `violet-stage` radial painted by the scene) | Hard cut on the noun (G-4) |
| **W-space** | void | `#040406` with faint white star dots (pitch 96, 10%), a drifting smoke glow; scenes add 2–3 slow nebula streaks | The constellation hub spine (SM-1, P-17), B&W statements | Smoke dissolve T-05 in; hard cut out |
| **W-fog** | stage | Radial grey `#ABABAB` (centre x 540, y 760) → `#4A4A4A`, noise 0.04 | Glowing outline flows (P-25): white lines, frosted nodes, metric tiles | Hard cut |
| **W-paper** | paper | Warm paper `#EEEDE9`, grain 0.05, vignette 0.08 | Face cut-out reveals (P-34), disintegrating words (P-37) | Hard cut |
| **W-grid** | canvas | `#EEF0F5` with 2 px `#D7DAE2` grid lines every 96 px | Product circles (P-33), branch maps (P-23), call frames (P-39) | Hard cut |
| **W-white** | canvas | Pure `#FFFFFF` | QR card (P-40), neon chip words on screenshots (P-28) | Hard cut or white flash T-04 |
| **W-black** | void | `#000000`, faint neon glow (8%) behind the centre | Statements (P-35), offer card (P-42), end lockup (P-41) | Hard cut |

Rules: a world switch lands on a spoken noun or ordinal; at most 1 world switch per 1.5 s; the light worlds (W-paper, W-grid, W-white) flip captions to ink (colour_by_bg).

### 3.2 Layout library
| ID | Engine | Presenter rect | Graphic rect | Caption band | Treatment | Share of runtime |
|---|---|---|---|---|---|---|
| **L-full** | `full` | 0, 0, 1080 × 1920 (Z-1/Z-2 crops on top) | — (heroes behind the head, tags around the props) | CS-1 chest: top = face bottom + 200 px (typically y 1000–1320) | none | 50–82% |
| **L-stack** | `stack`, seam_y 960, top `graphic`, bottom `footage` | 0, 960, 1080 × 960 (face centred in the band, head top y 1040–1160) | 0, 0, 1080 × 960 | CS-3 on the seam (y ≈ 960) | none | 0–20% |
| **L-graphic** | `hidden` | — | full frame | CS-4 fixed y 1420 (CS-2 top band y 300 over people B-roll) | none | 12–40% |

**Layout schedule rule:** L-graphic runs last 0.8–5.0 s; L-stack runs 2.0–8.0 s; every switch lands within ±0.25 s of a word (a number, a claim word, a sentence start). A graphic explanation that needs more than 5.0 s continues in L-stack (H8).

### 3.3 Stage moves
| ID | Move | Recipe (30 fps) | Use |
|---|---|---|---|
| **G-1** | Hard cut | `via: cut`, 0 f, on a word boundary ±1 f | Default between any two layouts and between takes |
| **G-2** | Zoom-blur cut | T-02 (§9.1): the outgoing shot pushes in and defocuses for 3 f, the incoming one arrives defocused and slightly zoomed and clears in 3 f | Into a graphic world, a new take or a hero moment; with Z-3 8–16 per minute |
| **G-3** | Split cut | `via: cut` into L-stack; the top graphic is already settled on the cut frame (its own entrance plays inside the band over 8 f) | Tables, documents, flows that need > 5 s, resource folders |
| **G-4** | Graphic cut | Stage → L-graphic and `world` set on the same frame | Glass cards, B-roll, QR |
| **G-5** | Smoke dissolve | T-05: `via: fade-through` 6 f + a smoke scene (z11, 12 f) into W-space | Entering the hub spine the first time |
| **G-6** | Return punch | Hard cut back to L-full with Z-1 (tight) on the first returning word; the next cut goes wide (Z-2) | Every return to the face after an insert |

### 3.4 Layout diagrams
```
L-full (talking head + hero behind head)        L-stack (graphic over face)         L-graphic (insert / world)
┌─────────────────────────┐ 0                   ┌─────────────────────────┐ 0         ┌─────────────────────────┐ 0
│ (IG top UI, keep clear) │ ← 0–110             │ (IG top UI)             │           │ (IG top UI)             │
│ connector "spend"       │ ← 120–230           │  title / table / doc    │ ← 140–900 │  top band: CS-2 y 300   │
│ ███ HERO 30 MINS ███    │ ← hero top 160–480  │  card x 64–1016         │           │  graphic zone           │
│ ███  ( head )   ███     │   hero bottom ≤ 900 ├──── seam y 960 ─────────┤ ← CS-3    │  x 64–1016, y 200–1300  │
│        (face)           │ ← face ~560–1000    │       ( head )          │           │                         │
│   connector "you're"    │                     │        (face)           │           │                         │
│   KEYWORD "seriously"   │ ← CS-1 1000–1320    │                         │           │  CS-4 caption y 1420    │
│   connector "missing"   │                     │                         │           │                         │
│  desk + props           │ ← props 1250–1700   │                         │           │                         │
│ (IG bottom UI)          │ ← 1540–1920         │ (IG bottom UI)          │           │ (IG bottom UI)          │
└─────────────────────────┘ 1920                └─────────────────────────┘ 1920      └─────────────────────────┘ 1920
```

### 3.5 Safe zones and bands
- Meaning-text box: x 64–1016, y 110–1500 (NC-5 holds: nothing in y < 110, y > 1540, or x > 970 between y 900 and 1540).
- **Hero band:** top y 160–480, x 24–1056 (E5), bottom edge ≤ 900. Connector line above the hero at y 120–230; trailer line below-right of the hero.
- **Caption band:** CS-1 chest y 1000–1320 (top = face bottom + 200 px); CS-2 top band centre y 300; CS-3 seam y 960; CS-4 y 1420. Caption max width 860 px (x 110–970).
- **Prop band:** y 1250–1700 (desk). Prop tags sit 40 px above the prop rim and never below y 1500 (text).
- **Graphic zone** in L-graphic: x 64–1016, y 200–1300.

### 3.6 Presenter rules
- Share 60–80%; the longest absence 5.0 s; return by G-1 or G-6.
- **Crops:** L-full wide = the frame as shot (head top y 300–560); Z-1 tight = 1.30× (mid 1.15–1.22) around the face (head top y 120–300); L-stack: face centred in the bottom band.
- **Behind the head (E1):** only heroes (TC-display). Never cards, labels or captions behind the head.
- Props stay in the desk band; the presenter's hands may cross captions (footage is not an element).

---

## §4 Colour, themes, grades `[REQ] [roles' meanings DNA; brandable hex VAR; theme hues TUNE]`

### 4.1 Role palette
| Role | Hex | One job | Text on it | Contrast | Lock |
|---|---|---|---|---|---|
| `primary` | `{{BV-02.primary|#C6FF1A}}` (TH-lime; mint `#4DFFC4`, yellow `#FFF01F`) | The reel's neon: hero numbers, gains, the active node, keyword chips, the current year, glow | `ink` | 16.6:1 (lime), 15.4:1 (mint), 16.6:1 (yellow) | brandable (VAR) |
| `accent` | `{{BV-02.accent|#4363F2}}` | Glass-world glow: card rims, spotlight stage, token halo, hub halo | `paper` | 4.9:1 | brandable (VAR) |
| `bad` | `#FF2A1A` | Zero, loss, the wrong path, the alert grade | `ink` | 5.2:1 | fixed |
| `good` | `#2BFF6E` | The reached result in a result pair, ✓ | `ink` | 14.7:1 | fixed |
| `ink` | `#0B0B0B` | Text on light worlds and on neon chips | — | 19.7:1 on white | TUNE |
| `paper` | `#FFFFFF` | Captions, grit heroes, card text on dark worlds | — | 20.1:1 on night | TUNE |
| `canvas` / `grid` | `#EEEDE9` / `#D7DAE2` | Paper and grid worlds | ink 16.8:1 | | TUNE |
| `night` | `#050713` | Glass and space worlds | paper 20.1:1 | | TUNE |

### 4.2 Meanings
- **White = the words.** Captions, grit heroes, statements.
- **Neon (`primary`) = the number that matters to the viewer**: income, time, count, the active step. One neon per reel.
- **Red / green = a result pair only**: red the zero or the wrong path, green the reached result. When red and green are on screen, the neon is not.
- **Accent = the glass worlds' light.** Never on text.
- Brand colours appear only on the creator's own product and logo.

### 4.3 Theme packs (per-reel rotation)
| ID | `primary` | When |
|---|---|---|
| **TH-lime** | `#C6FF1A` | Rotation slot 1 (the creator's reels 1, 4, 7 …). Default |
| **TH-mint** | `#4DFFC4` | Rotation slot 2 (reels 2, 5, 8 …) |
| **TH-yellow** | `#FFF01F` | Rotation slot 3 (reels 3, 6, 9 …) |

Rule: the reel header declares `theme`; pick the pack that follows the previous reel's pack in the creator's folder (lime → mint → yellow → lime). Never two consecutive reels on one pack. If the buyer set a brand colour (BV-02), all three packs take it and the rotation stops (their choice; "keep default" keeps the rotation).

### 4.4 Grades and clip treatments
- **Footage grade:** none. The creator's room is not regraded; match only exposure and white balance between takes.
- **Grade event GR-alert** (`warn` beats, ≤ 2 per reel, 0.8–1.6 s): the A-roll turns red monochrome (`grayscale(1) sepia(1) saturate(7) hue-rotate(-38deg) brightness(.9) contrast(1.15)`) with a ⚠ icon and a grit statement ("PROBLEM", v03 @0:29). It **strobes**: in the evidence the red grade, ⚠ and "PROBLEM" flick on and off every 1–2 f for 0.75 s (v03 @0:28.85–0:29.6; strip-f03). The recipe follows it: on and off every 1–2 f for 0.75 s, then hold on for the rest of the line; ⚠ and "PROBLEM" show only on the red frames. Built today as a z11 overlay scene (`mix-blend-mode: color` in `bad` at 85% over the footage) until E-16 ships.
- **Clip treatments** on creator B-roll (one per clip, never the same twice in a row, `clean` allowed between):

| ID | Recipe (CSS on the clip frame) | Use for |
|---|---|---|
| `halftone` | `grayscale(1) contrast(1.6)` + a dot overlay (`radial-gradient` 5 px dots, pitch 9 px, multiply) | Money, notes, objects (v05 @0:07) |
| `invert` | `invert(1) grayscale(.6) contrast(1.2)` for ≤ 0.6 s | A shock or "wait" beat (v05 @0:10) |
| `bw_vignette` | `grayscale(1) contrast(1.25)` + a 30% radial vignette | People, the past, "before" (v05 @0:33–0:35) |
| `warm_tint` | `sepia(.45) saturate(1.4) hue-rotate(-8deg) brightness(1.05)` | Team, life, office warmth (v05 @0:19–0:24) |
| `neon_mono` | `grayscale(1) contrast(1.15) brightness(1.08)` + a `primary` wash at 18% (`mix-blend-mode: color`) | People and objects in theme-tinted mono, montages (v05 @0:06.5 banknotes, @0:33.3 student, strip-p05, strip-m05) |
| `clean` | none | Products and screens that must read exactly |

B-roll motion (measured): an entry punch 1.00 → 1.13–1.15 over 6–10 f ease-out (v05 @0:33.36, @0:34.12, @0:35.04), or a slow pull-out 1.08 → 1.00 over 25–30 f on people B-roll (v04 @0:13.7, @0:14.7, @0:16.8). One per clip, alternating.

### 4.5 Rules
- ≤ 2 bright hues per frame (`max_bright_per_frame: 2`).
- Coloured text on light worlds sits on a chip (P-28) or has a 4 px ink stroke; neon text on dark grounds carries its glow.
- Glow only on neon numbers, the active node, tokens and the offer code; grit heroes have no glow (a soft 0 4 24 rgba(0,0,0,.35) shadow only).
- The neon never marks a loss; red never marks a gain.

**Must match `tokens.json`.**

---

## §5 Type & caption system `[REQ]`

### 5.1 Font map `[slots DNA; families TUNE within the class]`
| Slot | Family | Weights | Class (TUNE boundary) | Used for |
|---|---|---|---|---|
| `body` | **Inter Tight** | 700 (connector, plain), 800 (keyword) | neutral grotesk 600–800, tight tracking | Two-tier captions, hero connectors and trailers |
| `ui` | **Inter Tight** | 500–700 | neutral grotesk 400–700 | Glass cards, tables, tiles |
| `display` | **Anton** | 400 | condensed heavy caps | Grit hero words, statements, end lockups |
| `numeric` | **Barlow Condensed** | 600–700 | condensed sans 600–700 | Neon hero numbers, odometers, rulers, node labels, chips |
| `marker` | **Permanent Marker** | 400 | marker / handwritten caps | Hand tags, branch labels |

Devanagari captions fall back to Noto Sans Devanagari 700/800 (no italics; tiers keep their sizes). The ₹ glyph, ✓, ✕ and ⚠ are pre-painted.

### 5.2 Headline element: `none`; the hero carries the headline job `[DNA recipe; NICHE text]`
There is no banner. The **hero** is the headline: the first thing read, readable at 25% scale. Three recipes:

| Recipe | HERO-W grit word (P-01, P-02) | HERO-N neon number (P-03, P-04, P-06) | HERO-L lockup (P-05) |
|---|---|---|---|
| Font | Anton 400, uppercase, tracking −0.5%, line height 0.86 (statements: v03 @ 0:09 "IT DOESN'T MATTER HOW / CAPABLE / YOU ARE" is condensed, a 3-line size ladder). The hook hero can be a **wide** heavy display instead (v03 "3 SKILLS": 835 px wide for 7 glyphs, cap 173 px): use Archivo Black or Unbounded 900 for a 1–2 word hook hero | Barlow Condensed 700, tabular figures, tracking −1% | connector Inter Tight 700 52 px + HERO-W/N + trailer Inter Tight 700 52 px |
| Size | font 200–560 px; fit the word to 760–1032 px wide; cap height ≥ 160 px | font 240–520 px; `size = min(520, 1000 / (0.46 × characters))` (₹1,20,000 = 9 characters → 241 px) | hero as its recipe; connector above-left, trailer below-right of the hero box |
| Fill | off-white `#E0E0E0`–`#F0F0F0` (measured; not pure white) with a **distressed** grit mask: clumpy erosion patches 2–8 px plus thin scratches, ≈ 15–20 % of the glyph eaten (v03 @ 0:00.5 "3 SKILLS", @ 0:09 "CAPABLE"). Built today with layered `repeating-radial-gradient` mask holes (1.2 px dots, pitch 3.1 px and 4.7 px, offsets 17%/31% and 63%/12%) plus a third, coarser layer (3 px dots, pitch 9 px); a soft grey smoke haze (radial, 20–30 % white) sits behind the hook hero; shadow 0 4 24 rgba(0,0,0,.35) | lands in `paper`, then turns `primary` with glow `0 0 28px primary, 0 0 64px primary@50%` over 4 f | connector and trailer `paper`, no glow |
| Position | top y 160–480; bottom ≤ 900; centred on the frame or split around the head (P-02) | top y 220–420, centred | the hero box as its recipe; the connector 12 px above its top-left corner |
| Placement vs head | **behind the head** (E1). Single word: its baseline sits ≤ 0.45 × cap height below the head top, and the word is ≥ 2.6× the head width, so ≤ 35% of the glyph area can be covered. Two words: split around the head (gap = head width + 48 px) | behind the head, same rule; the first and last digits stay outside the head's x-span | the connector is never behind the head; the hero is |
| Entry | slam from the right: x +140 → 0 in 5 f with a 3-ghost horizontal smear (copies at −40/−80/−120 px, 35/20/10% opacity), crackle (mask offset ±2 px) f3–f8, settle 1.03 → 1.00 f5–f9 | tick roll (§10.1): the value updates every frame 10–24 f, fill ramps `paper` → `primary`, lands on the number word ±5 f, glow flickers 4 f then holds (or slot roll 14–22 f) | connector rises 24 px + fades in 6 f, 4–15 f before the hero; trailer pops on its own word |
| Life | pinned to the room: it rides every crop change and camera move with the footage (`follow_footage: true`; v04 @0:32.7, v05 @0:02.96); one optional pulse 1.00 → 1.04 → 1.00 in 6 f on a re-spoken word | same; the glow breathes ±8% over 1.2 s | — |
| Lifetime | 1.5–3.0 s (≥ 0.6 s E1 minimum); the hook hero may hold up to 6 s across cuts on the same take (v05 "1,20,000" 1.0–6.5 s); ends on a world change | same | same |
| Exit | gone with the shot on a cut (preferred), or blur-out 5 f | same | same |
| Text class | TC-display | TC-display | connector/trailer TC-display (48–60 px) |

Head box: from `ctx.face()` (eyebrows to chin); head top = face.y − 0.55 × face.h (hair), head width = 1.25 × face.w. **Hero limits:** ≤ 3 words (one number + one unit word counts as 2), ≤ 2 lines, one hero on screen, 3–7 per minute (H4). Captions keep running while a hero is up (they are in different bands).

### 5.3 Caption system profiles `[DNA mechanics; fonts TUNE; language VAR]`
Four profiles share one skin; only the position changes. All extend the library profile `lib:tharun`.

| Field | CS-1 **Chest two-tier** (default, L-full) | CS-2 **Top band** (people / product B-roll) | CS-3 **Seam** (L-stack) | CS-4 **Graphic band** (L-graphic) |
|---|---|---|---|---|
| Mode | full · primary · mute_safe | same | same | same |
| Chunking | `group`, 1–4 words, ≤ 18 characters per line, ≤ 3 lines (connector / keyword / connector); never split a name, number or unit; new chunk on punctuation and on pauses ≥ 0.25 s (always at 0.6 s) | same | ≤ 2 lines | same as CS-1 |
| Timing | lead 1 f; words **appear one by one on their onsets in their final place** (`reveal: word`); chunk swap **hard** (0 f, measured: no pop or fade, v05 @0:00–0:00.6, v04 @0:07.8); captions blur with the picture through T-02; ≥ 0.25 s per word; tail 0.1 s; no pause hold | same | same | same |
| Skin | Inter Tight 700, **plain 72 px**, as-spoken case, tracking −3%, line height 0.92, `paper`, shadow 0 3 14 rgba(0,0,0,.5), no container | shadow 0 3 16 rgba(0,0,0,.6) | plain 64 px, shadow .65 | shadow 0 2 10 rgba(0,0,0,.35) |
| Two-tier variant | **connector 56 px (700) + keyword 136 px (800)** by default; measured keywords run 84–185 px ("Websites" cap 61 px ≈ 84 px; "rupees" x-height 101 px ≈ 185 px), sized so the keyword line spans ≈ 450–600 px; ratio 2.43 (min **1.7**: real chunks go as low as 1.75, "Websites / and / Apps"), stack `split`: connectors before the keyword above it, after it below it; a chunk without a keyword is plain 72 px | same | connector 56 + keyword 124 | same as CS-1 |
| Position | `chest`: top = face bottom + 200 px, kept inside y 110–1500; centre x 540, max width 860; avoids the face (moves below the chin) | `fixed_y` centre y 300, **left-aligned** at the safe left edge (real: x ≈ 95, small 48–56 px, v02 @ 0:00.5 "the story of", v04 @ 0:20 "here's a", v03 @ 0:11 "spend") | `seam` (y ≈ 960, dy −6) | `fixed_y` centre y 1420 |
| Colour by ground | light ground → `ink`, dark → `paper` | same | paper | same |
| Emphasis | `size_tier` only: the keyword (P7 priority: number → name/brand → topic noun → contrast word); ≤ 1 per chunk, ≤ 1.0 per second, min score 1.3, never stop-words | same | same | same |
| Hide | under z8 scenes (statements, big lockups), during stage morphs, during E2 (not used) | same | same | same |
| Language | Latin; keep English terms verbatim; don't normalise spelling; profanity mask `inner` (f**king); glossary from the reel | same | same | same |
| Text class | TC-subtitle (floor 54: connector 56 ✓) | same | same | same |

**Profile switching:** CS-1 is the default; L-stack switches to CS-3 and L-graphic to CS-4 automatically (`captions.by_layout`); write `captions.overrides {t: [a, b], profile: "CS-2"}` for every full-frame B-roll span whose subject's face or product sits in the centre (v04 @0:14–0:20 "here's a / MacStudio").

**Tier examples (from the evidence; reproduce exactly this shape):**
```
v05 @0:02       v05 @0:03        v02 @0:20          v04 @0:48
   rupees        without a         you're             afford
 per   month      degree         seriously          a MacBook
                                 missing out.        rightnow
(kw + below)   (above + kw)    (above + kw + below) (above + kw + below)
```

### 5.4 Other text systems
| System | Class | Recipe | Hold |
|---|---|---|---|
| **Hand tag** (P-11, P-23, P-27, P-39) | TC-label | Permanent Marker 44–60 px uppercase, `paper` on dark / `ink` on light, rotated −6…+4°; arrow 6 px stroke drawn shaft 7 f then head 3 f, curving from the tag to the target | ≥ 1.0 s |
| **Condensed label** (node labels, "PROJECT 2", ruler years) | TC-label | Barlow Condensed 600, 44–64 px, uppercase, tracking +1% | ≥ 10 f after built |
| **Neon chip word** (P-28) | TC-display | Barlow Condensed 700, 80–120 px, uppercase, `primary` fill, `ink` text, radius 4, padding 4/18 | ≥ 0.6 s |
| **Card title / body** (P-22, P-24, P-26) | TC-label | Inter Tight 700 56–72 px / 500 40–46 px | ≥ 0.25 s per word |
| **Metric value** (P-16) | TC-display | Inter Tight 700 64–96 px, `ink` on white tiles | ≥ 0.8 s after landing |
| **Statement** (P-07, P-35, P-36) | TC-display | Anton 180–300 px, uppercase, grit, line height 0.88; lines appear per phrase 4 f | ≥ 0.25 s per word |
| **Legal / example tag** | TC-legal | Inter Tight 500 24 px, 70% opacity, bottom-left of its card ("example") | the card's hold |

### 5.5 Language and number rules
- Captions as spoken (default English verbatim, `{{BV-05.speech|en}}` speech → `{{BV-05.captions|en}}` captions; BV-05 may switch to Hinglish (romanised captions) or Hindi (Devanagari)). Keep English terms verbatim in Hinglish.
- Brand and tool names exact (glossary). Product names keep their case ("MacBook", "Instagram").
- Numbers: `ctx.fmtNum` with `profile.numbers` (examples for Hinglish / Hindi; English writes `$`, 1.2M): ₹ glyph, Indian grouping (₹1,20,000), compacts ₹2.5 L / ₹1.2 Cr on chips and tags, full form on heroes up to 9 characters (₹1,20,000), short form beyond (₹12.5 L). Years and counts plain ("2026", "3 SKILLS"). Units after numbers in the hero ("30 MINS", "5 YEARS", "₹60/DAY").
- Devanagari: no uppercase or italic; heroes in Devanagari use Noto Sans Devanagari 800 at the same sizes, no grit mask.

---

## §6 Hook system `[REQ]`

### 6.1 Stopper tests
| Test | This style's number |
|---|---|
| **ST-1 Thumbnail** | Frame 1.7 s at 25% scale: the hero reads (cap height ≥ 160 px → ≥ 40 px at 25%) and the presenter's face is visible |
| **ST-2 Mute** | With sound off, 0–3 s tell the topic: captions run from f3 and the hero states the number or the claim |
| **ST-3 Motion at f0** | A Z-6 settle-out or Z-4 settle-push starts at f0 on live footage (the frame is already moving) |
| **ST-4 Read time** | The hero reads in ≤ 1.2 s (≤ 3 words) |
| **ST-5 Change count** | ≥ 8 weighted state changes in 0–3 s (caption swaps count 1.0) |
| **ST-6 Payoff-by** | The hero is fully landed by 1.7 s (HA-08); the result by 2.0 s (HA-01); the number by 1.0 s (HA-07); the lockup by 0.7 s (HA-05) |

### 6.2 Default archetype: HA-08 **Prop + hero** `[DNA]`
The presenter holds or points at a prop, one hero lands behind the head, and a two-tier caption names the payoff. Spoken shape: "*[connector] [HERO] [payoff clause]*" ("the story of this **18 YO** student will blow your mind", v02; "you can make up to **1,20,000** rupees per month", v05).

| t | Beat | Visual | Caption (CS-1) | Layout / camera | SFX moment |
|---|---|---|---|---|---|
| **f0** | Moving start | Live take, prop already in hand or on the desk; the frame starts mid-motion: Z-6 settle-out 1.22 → 1.00 over 12 f (v05 @0:00), or 1.5 → 1.00 over 13 f behind a 6 f T-06 defocus (v04 @0:00), or Z-4 settle-push 1.00 → 1.18 over 8 f (v03 @0:00); 50% of the move happens in the first 2 f, no return | First word appears by f3 (word reveal; v05 shows "you" on f0) | L-full | hook hit on f0 |
| 0.0–0.5 | Setup words | If the hero has a connector ("the story of this", "Don't ignore these", "spend"), it rises in above the hero band (y 120–230) by 0.5 s | Words build one by one: "you" → "you can" → "you can make" (plain 72 px) | L-full | — |
| 0.2–1.0 | Hero lands (word) | P-01/P-02 grit word slams in from the right behind the head (5 f smear, crackle) on its word (v03: hero enters at 0.20 s, sharp at 0.32 s) | The hero's word is dropped from the caption; the caption holds its connector | Z-1 tight crop (1.30×) on the next cut | hero impact |
| 0.8–1.5 | Hero lands (number) | P-03 odometer rolls 14–22 f behind the head, lands on the number word ±5 f | Caption keyword chunk waits for the unit ("rupees") | hold | counter roll |
| 1.5–1.8 | Hero ignites | Neon glow ignites on the number (4 f), or the grit word settles; **payoff by 1.7 s** | Next chunk: keyword tier ("rupees / per month") | — | — |
| 1.8–2.5 | Prop tag | P-11 hand tag + arrow to the prop ("STUDENT", 10 f), or P-20 three icon tiles pop at chest-bottom (3 f stagger), or P-12 card held to camera | Two-tier chunk with a keyword | Z-2 back to wide on a cut, or a Z-3 blur-punch mid-shot (v05 @0:02.96: 1.0 → 1.3 in 5 f, the hero rides it) | tag pop |
| 2.5–3.0 | Promise | Hero still up (hold ≥ 1.5 s total) | "will / blow / your mind" | — | — |
| 3.0–4.5 | Exit to the promise | Hero ends on the cut; T-02 zoom-blur cut, T-04 flash or G-4 cut into the first insert (a glass card, the headline card, a B-roll clip) on the noun | — | — | whoosh on the whip |

State changes in 0–3 s for this table: 4–5 caption swaps + hero enter + glow event + 2 camera moves + 1–2 cuts + tag enter = 10–12 (≥ 8 ✓).

**Never skip the hero.** If the script's first line has no number and no name, use the line's claim word as a grit hero ("FREELANCER", "PROBLEM") or the topic count ("3 SKILLS").

### 6.3 Allowed alternates `[DNA list; VAR choice per reel]`

**HA-01 Result pair (red → green)**, v01: "Here's how you can go from making ₹0 to ₹5 lakh a month". Needs PR-1 (two glasses) or FB-2.

| t | Visual | Caption | Camera |
|---|---|---|---|
| f0 | Both props on the desk (red left, green right), the presenter gesturing; Z-6 settle-out | "Here's how" | L-full wide |
| 0.5–1.1 | — | "you" → "you can" → "you can go" | — |
| 1.1–1.3 | T-02 zoom-blur cut | "making" | — |
| 1.3–2.0 | Punch tight on the **red** prop; P-08 red tag "₹0" pops 40 px above its rim (6 f): **result by 2.0 s** | "₹0" dropped from the caption | Z-1 tight on the prop |
| 2.0–2.2 | Whip-pan to the **green** prop, filmed in camera (6 f, motion blur; the counter keeps ticking through it, v01 @0:02.0; no prop take → T-02) | — | — |
| 2.2–2.9 | P-09 counter rolls ₹0 → ₹5,00,000 above the green rim in `good` (20 f, 5 visible values), lands on "5 lakh" ±5 f, glow | "to" | hold |
| 2.9–4.5 | Pull out: both tags visible (red ₹0, green ₹5,00,000); then a grit hero ("FREELANCER") behind the head with the connector "as a" | "as a" → hero | Z-2 wide |

Example per niche: [NICHE: example] careers "₹0 → ₹1,00,000 a month as a video editor" (two glasses); fitness "92 KG → 76 KG" (red tag on an old photo prop, green tag on the presenter).

**HA-07 Live number / ruler open**, v04: "5 years since I started running a creative agency".

| t | Visual | Caption | Camera |
|---|---|---|---|
| f0 | Focus-pull entry (v04 @0:00): T-06 defocus clears over 6 f while Z-6 settles 1.5 → 1.00 over 13 f, on a hair flick | — | L-full |
| 0.17–0.5 | P-13 year ruler slides in from the right across the chest (y 1100, 12 f) | — (CS-1 offset drops to 120 px while the ruler is up, so captions sit above it) | — |
| 0.67 | The current year turns `primary` on the ruler | — | — |
| 1.0–1.33 | P-04 count steps "1" → "4 YEARS" → "5 YEARS" behind the head (4 f per step), neon glow: **number by 1.0 s** | — | Z-1 tight at 1.17 |
| 2.0–2.9 | P-05 lockup: connector "since I" + grit hero "STARTED / RUNNING", then "a" + "CREATIVE / AGENCY" | connectors only | Z-2 wide |

Example per niche: [NICHE: example] careers "3 YEARS since I quit my 9-to-5"; small business "5 YEARS since we opened the café".

**HA-05 Claim lockup / promise chip**, v03: "Don't ignore these 3 skills if you're 16–20 years old".

| t | Visual | Caption | Camera |
|---|---|---|---|
| f0 | Connector "Don't Ignore These" fades in at y 120–230 (48 px) | — | L-full |
| 0.17 | Grit hero "3 SKILLS" slams in from the right behind the head, crackle: **lockup by 0.7 s** | — | Z-4 settle-push from f0 (1.00 → 1.18, 8 f) |
| 0.8–2.0 | Hero holds | "16-20" → "16-20 years" → "16-20 years old" (plain) | — |
| 2.3–2.8 | P-20 three icon tiles pop at chest-bottom (3 f stagger) and drift up 40 px | "these are the" | — |
| 3.0 | Caption "3 skills"; T-05 smoke dissolve into the hub spine (SM-1) on "skills" | "3 skills" | — |

Example per niche: [NICHE: example] careers "Don't ignore these 3 SKILLS before 2027"; fitness "Stop doing these 3 EXERCISES".

### 6.4 Hook pairs by topic `[NICHE]`
Pair type for HA-08 and HA-05: **subject → reveal** (the prop or claim → the hero); for HA-01: **bad → good result**; for HA-07: **subject → reveal by 1.0 s**.

| Topic [NICHE: example] | Archetype | First subject (prop / line) | Hero (reveal by 1.7 s) | How each is shown |
|---|---|---|---|---|
| Freelancing income (careers) | HA-01 | Red glass: "₹0" | Green glass: ₹1,00,000 a month | PR-1 glasses + P-08 / P-09; fallback P-10 vessels |
| Skills to learn (careers) | HA-05 | "Don't ignore these" | **3 SKILLS** | P-05 lockup + P-20 tiles |
| A student's story (careers) | HA-08 | Printed photo of the subject (creator-owned) | **19 YO** + "STUDENT" tag | PR-2 photo + P-11 hand tag; third-party photo → P-34 silhouette |
| Salary without a degree (careers) | HA-08 | Handwritten card "DEGREE" | **₹1,20,000** per month | P-12 card + P-03 odometer |
| Years of experience (careers / business) | HA-07 | Year ruler | **5 YEARS** | P-13 + P-04 |
| Weight-loss result (fitness) | HA-01 | Old jeans or a photo (red tag "92 KG") | Green tag **76 KG** | Props + P-09; fallback P-10 with kg tags |
| Habits / routine (fitness) | HA-05 | "Stop doing these" | **3 HABITS** | P-05 + P-20 |
| Protein / diet (fitness) | HA-08 | The food in hand (eggs, a bowl) | **120 G** protein | Prop + P-03 neon number |
| Time to result (fitness) | HA-07 | Day ruler (days 1…90) | **90 DAYS** | P-13 (days) + P-04 |

### 6.5 Hero writing `[DNA formula; NICHE examples]`
**Formula:** `[connector, 1–4 lowercase words, optional] + HERO (≤ 3 words, caps, or a number + unit) + [trailer, optional]`. The hero is the one word the viewer must remember.

| Template | Example [NICHE: example] |
|---|---|
| Number + unit | "you can make up to **₹1,20,000** per month" |
| Count + noun | "Don't ignore these **3 SKILLS**" |
| Age / identity | "the story of this **18 YO** student" |
| Time | "**5 YEARS** since I started" · "spend **30 MINS** everyday" |
| Role / claim | "as a **FREELANCER**" · "**DEADLY · COMBO**" |
| Problem word | "**PROBLEM**" (warn, GR-alert) |

- Uppercase heroes, as-spoken captions. English heroes unless the buyer captions in Hinglish or Hindi.
- **Write 3 hooks and pick by the stopper tests.** The others go to trial variants.
- **Banned:** heroes longer than 3 words, vague hype ("GAME CHANGER"), numbers the script doesn't state, ₹ written as Rs.

### 6.6 Hook sound
See §11: the hook carries cues (a hit on f0, the hero impact, the counter roll, the zoom-blur whoosh); the music bed enters after the hook (on the first item marker).

### 6.7 CTA `[DNA device set; VAR values]`
Device chosen by BV-08 (`{{BV-08.device|qr}}`); placement `mid+end`: a first CTA flash at 55–75% of runtime (1.5–2.0 s), the full CTA at the end.

| Device | Spoken pattern | On-screen element | Hold | Where |
|---|---|---|---|---|
| `qr` | "scan this QR code for the entire guide" | **P-40 QR card** on W-white: the buyer's QR image 560 × 560 centred (top y 520); CS-4 caption in ink: "scan this / QR Code" above (centre y 380), "for the / entire guide" below (centre y 1220); a 2 f white flash in (T-04) | ≥ 1.5 s (2–4 s at the end) | mid + end |
| `comment_keyword` | "comment {{BV-08.keyword|KEYWORD}} and I'll send it" | **P-43 keyword hero**: the keyword as a neon grit hero behind the head (kind `cta-keyword`), connector "comment" above; the caption keeps "and I'll send it" | ≥ 1.5 s | mid + end |
| `link_bio` | "link in bio" | Two-tier caption "link / in bio" + a hand arrow (P-11 style) pointing down-left toward the profile (stays above y 1500) | ≥ 1.5 s | end |
| `end_card` | the closing line | **P-41 end lockup** on W-black ("one last push / 90 DAYS / before 2026 ends") or **P-42 offer card** for the creator's own product | 1.5–4.0 s | end |

Silence: no SFX in the 1.0 s before the first CTA word. The reel hard-ends ≤ 6 f after the last word (T-09). End cards are specified in §25.

---

## §7 Structure & cadence `[REQ] [DNA]`

### 7.1 Structure type
**`list`** (promise → items with an identical ritual → payoff → CTA), numbered ascending. When the items are skills or pillars of one idea, the list is drawn as a **framework hub** (SM-1); when they are sequential steps, as a **spotlight stack** (SM-2). Story reels ("the story of this 18 YO…") run the same ritual with beats instead of items: setup → twist → numbers → lesson.

### 7.2 Markers (one per reel, at every item)
| ID | Marker | Recipe | Use for |
|---|---|---|---|
| **SM-1** | **Constellation hub** (P-17) | W-space; the hub sphere + spokes; on the ordinal word the in-scene view flies to the item's node, the node grows 1.0 → 1.25 and glows `primary`, its label types 1 letter/f (Barlow Condensed 600, 56 px); 1.2–2.0 s; the overview returns at the recap ("LEARN THESE / 3 SKILLS") | 3–5 parallel items (skills, habits, pillars) |
| **SM-2** | **Spotlight stack** (P-18) | W-glass; a warm light cone from the top; the step's paper sheet ("STEP 2 / SOLID PORTFOLIO") floats down into the light over 14 f; earlier sheets lie on the desk below; 1.2–2.0 s | Sequential steps, roadmaps (3–6 steps) |
| **SM-3** | **Token carousel** (P-19) | Violet stage; two glowing outline hands hold the item's token (label inside), the queued tokens numbered in a row below; the token flips 6 f per item | 5+ items, ranked lists |
| **SM-4** | **Spoken only** | No marker graphic; the ordinal is the caption keyword ("first", "second") with a Z-1 punch, and the item's hero carries the name | Short lists (2–3) inside story reels |

Numbering ascending. **Recap: on** (P-22 glass recap or the SM-1 overview before the CTA). Teaser chips: off.

### 7.3 Unit ritual (identical for every item)
| Time (from the ordinal word onset) | Step |
|---|---|
| −2 f | Cut (G-4) or smoke dissolve (G-5, first time only) into the marker world; the marker scene enters |
| 0 → +36…60 f | The marker plays (node fly-to / sheet float / token flip); the CS-4 caption carries the ordinal + the item name as keyword |
| on the name word ±1 f | Back to L-full by G-6 (Z-1 tight); the **item hero** lands behind the head (P-01 grit name or P-03/P-04 number), hold 1.5–3.0 s |
| every 1.2–2.5 s after | 2–4 evidence beats, one per noun: P-24 glass card, P-31 stylised clip, P-12 card, P-16 tiles, P-21 icons, P-27 site card; alternate L-full and L-graphic; ≥ 0.8 s of face between two inserts (except a 2-clip montage) |
| the takeaway line | Z-2 wide, a two-tier caption with the takeaway keyword, no graphic (breathing beat, 1.0–2.0 s) |

Item length 6–15 s. The **last item escalates**: its hero is a neon number (P-03) or a statement bleed (P-07), and it gets the reel's only GR-alert or its largest insert.

### 7.4 Open loops and re-hooks
- **Loops used:** the count loop (the hook's "3 skills" is paid by 3 markers), the deliverable loop ("scan / comment for the entire guide"), the "last one" loop ("the last secret", v03 @0:51).
- **Payoff rule:** every promise is paid on screen (H9).
- **Re-hook (standard class: one, at 40–60% of runtime; `rehook_every_s: 35`):** a twist line ("the surprising part?" v02 @0:11, "weird part?" v05 @0:08, "Watch till the end" v03 @0:26) shown as a two-tier caption with the twist word as keyword + a ≤ 0.3 s beat of silence before it + **either** a GR-alert event with a "PROBLEM" statement (warn) **or** a grit hero behind the head ("LAST SECRET") + Z-5 dutch roll.
- **Intro cap:** hook + promise ≤ 15% of runtime (≤ 9 s in a 60 s reel); the first marker by 9 s.

### 7.5 Rhythm and energy curve
- **Every 1.0–2.1 s** (median shot) a cut with a crop change; **about every 10 s** an animated camera move (Z-3/Z-4/Z-6); **every 4–8 s** an insert or card on a noun; **every 8–15 s** a hero.
- Energy: hook (max: prop + hero + punches) → items (steady: ritual) → re-hook (spike) → last item (escalate) → CTA (clean: white QR card or keyword hero, no whips during the CTA words).
- Information beats carry the voice; there are no entertainment-only beats (comedy off).

### 7.6 Cadence (state changes)
| Token | Value | Why |
|---|---|---|
| `sc_per_10s` | **[10, 28]** | Primary captions (weight 1.0) swap ~1.0–1.6×/s; plus 4–6 cuts and 1–3 enters per 10 s (v05 densest: 55.9 cuts/min) |
| `hook_sc_3s` | **8** | 10–12 measured in the evidence hooks (v01, v05) |
| `max_gap_s` | **1.2** (hook **0.8**) | Something new at least every 1.2 s (D4) |
| `max_static_s` | **2.0** | Live footage always moves; graphics need an internal event every ≤ 2.0 s |
| `caption_weight` | **1.0** | Captions are primary |
| `cuts_per_min` / `median_shot_s` | **[24, 50]** / **[1.0, 2.1]** | Measured per frame: v01 26, v02 25, v03 25, v04 29, v05 48 cuts/min; median shot 1.94 / 1.98 / 2.08 / 1.20 / 0.96 s, p90 2.9–4.4 s. The longest single shots (5–9 s) are graphic worlds with in-scene motion; the longest A-roll shot is 3.9 s and carries a blur-punch inside (v01 @0:06.5–0:10.4) |

---

## §8 Visual system `[REQ]`

### 8.1 Graphics role and budget
`graphics: support`: 25–45% of runtime carries a graphic or insert beyond captions and heroes. **44 patterns** (P-01…P-44). Families per 60 s: ≥ 4. Every spoken number becomes a performed number (D3).

### 8.2 Families
| ID | Family | Source class | The buyer supplies |
|---|---|---|---|
| **B-1** | Hero type (grit words, neon numbers, lockups, statements) | engine | nothing |
| **B-2** | Props and result pairs | buyer-owned (props in the A-roll) / engine (fallbacks) | PR-1…PR-5 (optional) |
| **B-3** | Performed numbers (odometers, rulers, sliders, tiles) | engine | the numbers in the script |
| **B-4** | Markers and structure (hub, spotlight, tokens, icon tiles, recap, branch map) | engine | nothing |
| **B-5** | Explainer cards (glass cards, glow flows, tables, site cards, chips, folders, headline cards) | engine / buyer-owned screenshots / created substitutes | SH-5 screenshots (optional) |
| **B-6** | Stylised inserts (B-roll with treatments, people topline, product circle, cut-out reveal, mono statements, alert grade, disintegrate, chat mock, call frames) | buyer-owned / created substitutes | SH-4 clips, SH-6 second angle (optional) |
| **B-7** | CTA and end (QR card, end lockup, offer card, keyword hero) | engine + the buyer's QR / offer | SH-7 QR or keyword |

### 8.3 Pattern specs
All motion at 30 fps. "Engine" names the building block. Every text scene sets `text_class`; every behind hero sets `behind: true, exception: "E1"`.

**B-1 Hero type**
| ID | Name | Type | On screen | Motion (30 fps) | Use when | Class · needs | Engine |
|---|---|---|---|---|---|---|---|
| **P-01** | HERO-GRIT-BEHIND | overlay | One 1–3 word grit-white Anton caps word behind the head, 760–1032 px wide, top y 160–480 | Slam from the right x +140 → 0 in 5 f with 3 smear ghosts; crackle f3–f8; settle 1.03 → 1.00 f5–f9; hold 1.5–3.0 s; ends on the cut | Hook hero, item names, claims ("3 SKILLS", "FOCUS", "FREELANCER") | TC-display · E1 (+E5 when margin < 64) · matte | `VEOS.scene({behind: true, kind: "hero_text", exception: "E1", z: 3})` |
| **P-02** | HERO-HEAD-GAP | overlay | Two words split around the head: word 1 left of it, word 2 right; gap = head width + 48 px (visible ≥ 85%) | Word 1 slides from the left, word 2 from the right 3 f later, each 5 f with smear | Two-word heroes ("18 YO", "15 DAYS", "DEADLY · COMBO") | TC-display · E1 · face box | scene, x from `ctx.face()` |
| **P-03** | HERO-ODOMETER | figure | A neon number behind the head, digits in fixed tabular slots | Default **tick**: the value updates every frame (ease-out, 10–24 f; v01 @0:02.0 ₹1,50,263 → ₹3,80,853 one value per frame, @0:06.6 0 → 77.5% in 9 f), the fill ramps `paper` → `primary` during the roll, glow flickers on alternate frames for 4 f on landing; or **slot** (v05 @0:01): each slot rolls 14–22 f with vertical blur 12 → 0 px. Lands on the number word ±5 f; glow breathes ±8% / 1.2 s | Every money amount, big count, followers, salary | TC-display · E1 + E6 slot · figure | `VEOS.data.counter({font: "numeric", glow: "primary"})` with `behind: true, kind: "hero_number"`, or bespoke with `ctx.figAt` |
| **P-04** | HERO-COUNT-STEPS | figure | A number that steps through 2–4 spoken values; the unit word joins at the last step ("1" → "4 YEARS" → "5 YEARS") | 4 f per step, scale 0.92 → 1.00 per step, glow on the final | Durations, ages, growth over time | TC-display · E1 + E6 · figure (steps) | `VEOS.data.counter` with `steps` |
| **P-05** | HERO-LOCKUP | overlay | Connector (52 px) above-left + hero + trailer (52 px) below-right ("spend / 30 MINS / everyday", "the story of this / 18 YO / student") | Connector rise 24 px + fade 6 f before the hero; hero as P-01/P-03; trailer pops 6 f on its word | Heroes that need context; HA-05 hooks | TC-display · E1 (hero only) | one scene, connector not behind (a second scene `z: 5`) |
| **P-06** | HERO-TICKER | figure | Numbers appear left → right one per spoken word ("18 19 20"), unit row under them ("Years … old") | Each number pops 4 f (scale 0.8 → 1.0) on its word; the newest is `primary` | Counting ages, years, attempts aloud | TC-display · E1 · figure | scene with `events` per word |
| **P-07** | STATEMENT-BLEED | overlay | 2–4 lines of grit caps filling the width (E5), behind the presenter on A-roll, in front of a B-roll clip (clear of the subject's face) | Lines appear per phrase, 4 f each (rise 20 px); hold ≥ 0.25 s/word; captions hide (z8 on B-roll) | A principle or quote the reel turns on ("IT DOESN'T MATTER HOW CAPABLE YOU ARE / IF YOU CAN'T EXPLAIN IT CLEARLY") | TC-display · E1 on A-roll / E5 | scene `z: 8` (B-roll) or `behind` (A-roll) |
| **P-08** | HERO-RED-ZERO | figure | The bad-state value in red glow over the bad prop or card ("₹0", "0 CLIENTS", "92 KG") | Pop 6 f (scale 0.6 → 1.05 → 1.0); red glow 0 0 24px bad | The "before" side of a result pair | TC-display · anchor · figure | scene + anchor point |

**B-2 Props and result pairs**
| ID | Name | Type | On screen | Motion | Use when | Class · needs | Engine |
|---|---|---|---|---|---|---|---|
| **P-09** | PROP-PAIR-TAGS | figure | Two real props (red / green); a red tag on the bad one, a `good` counter on the good one, 40 px above each rim | Red tag pops 6 f on its word; whip-pan T-02 to the good prop; the counter rolls 20 f with 5 visible values and lands on the number word ±5 f | HA-01 hooks with PR-1 | TC-display · anchors (static, from the anchor pass) · figure | counter scene placed at the anchor |
| **P-10** | RESULT-PAIR-VESSELS | figure | FB-2: two drawn glass jars (SVG, 300 × 420 each) on W-glass or in the L-stack top band; liquid red at 8% vs `good` at 85% | Jars rise 10 f, 3 f stagger; the good liquid fills 0 → 85% over 18 f on the number word, with a meniscus wobble; tags as P-09 | HA-01 without props | TC-display · figure | bespoke scene (canvas) |
| **P-11** | PROP-HAND-TAG | annotation | One prop + a hand tag ("STUDENT") + a curved arrow to it | Arrow shaft 7 f + head 3 f, then the tag writes on L → R 10 f | Naming what the prop is (a photo, a device, a person) | TC-label · ink · anchor | scene with an SVG path (`stroke-dashoffset`) |
| **P-12** | PAPER-CARD-PROP | overlay | A handwritten card held to camera (real) or FB-3: a white card 360 × 200, rotated −6°, marker word 72 px `ink`, beside the presenter at chest (x 120–480 or 600–960) | Real: the card flickers to an inverted neon outline for 1–2 f twice while held (v05 @0:03.3; a z5 scene masked to the card's anchor box). Drawn: pop 6 f with a 2° wobble for 10 f | A keyword the viewer must remember ("DEGREE", "₹60/DAY") | TC-label / display | scene (drawn) |
| **P-44** | DESK-COUNTDOWN-TAGS | annotation | Numerals above 3–5 desk chips ("5 4 3 2 1"), Barlow Condensed 600 64 px; the active one `primary` | Each numeral pops 4 f as counted; the active one scales 1.15 | List reels with PR-4 chips (SM-3 physical) | TC-label · anchors | scene, one anchor per chip |

**B-3 Performed numbers**
| ID | Name | Type | On screen | Motion | Use when | Class · needs | Engine |
|---|---|---|---|---|---|---|---|
| **P-13** | TIMELINE-RULER | figure | A ruler across the chest (y 1080–1120): 4 px ticks every 18 px, a major tick per year/day, labels Inter Tight 600 40 px every 210 px; the current one `primary` | Slides in from the right 12 f so the current mark lands at x 540; the current label turns `primary` on its word; drifts 20 px left during the hold | "since 2022", "two years ago", "day 1 → day 90" | TC-label · figure (axis) | `VEOS.data.slider` styled as a ruler, or bespoke |
| **P-14** | STAT-SLIDER | figure | W-glass or W-black: an 800 px track at y 820, marks 0 / 5 / 10+, a glowing handle; zone chips below ("✕ Low credibility" bad, "✓ High credibility" good) 40 px | Track draws 10 f; the handle glides to the value 14 f on its word; the zone chip pops | A threshold or sweet spot ("5–6 great projects") | TC-label · figure | `VEOS.data.slider` |
| **P-15** | PIN-ON-LINE | figure | A `good` line grows L → R to a pin; a white rounded tag under the pin with the value ("₹3 lakh", 64 px ink) | Line 14 f, pin drop 4 f, tag pop 6 f | One milestone value | TC-label · figure | bespoke |
| **P-16** | METRIC-TILES | figure | 2 × 2 white glass tiles 380 × 260 (W-fog or W-glass): label 40 px + value 72 px + a sparkline | Tiles rise with 3 f stagger; values count 12 f; sparklines draw 10 f | Funnel or result metrics the script states ("512 delivered, 148 opened") | TC-label / display · figures | 4 × `VEOS.data.counter` in one scene |

**B-4 Markers and structure**
| ID | Name | Type | On screen | Motion | Use when | Class · needs | Engine |
|---|---|---|---|---|---|---|---|
| **P-17** | CONSTELLATION-HUB | state | W-space: a white marbled sphere Ø 180 with 6–9 thin spokes to white node dots; item nodes Ø 44 labelled in condensed caps 56 px; the active node `primary` glow | Overview: spokes draw 12 f. Per item: the whole diagram translates/scales in-scene so the active node lands at (620, 760) over 18 f (ease in-out), the node grows 1.0 → 1.25, its label types 1 letter/f | SM-1 | TC-label · continuity motif M-hub | `VEOS.fx.diagram` (nodes circle, edges line) inside one transformed scene |
| **P-18** | SPOTLIGHT-STACK | state | W-glass: a warm cone (rgba(255,236,190,.32), a neutral light, not a role) from the top centre; a paper sheet 420 × 560 with "STEP n" (40 px) + title (Barlow 600 56 px) floats into the light; earlier sheets lie on the desk below | Entered by T-02 (v01 @0:17.8); sheet descends 60 px + rotates −6° → −2° over 14 f, glows; earlier sheets slide left 40 px; the whole stage pushes in 1.00 → 1.3–1.6 over the beat, accelerating (in-scene scale, v01 @0:10.6, @0:18.2, @0:52.9) | SM-2 | TC-label | bespoke scene |
| **P-19** | TOKEN-CAROUSEL | state | Violet radial stage (`violet-stage`, z1); two glowing `accent` outline hands hold a Ø 300 token with the item label (Inter Tight 700 44 px); queued tokens Ø 110 numbered below at y 1300–1420 | Token flips on Y 6 f per item; the next numbered token travels up 12 f | SM-3 | TC-label | bespoke scene (SVG hands) |
| **P-20** | ICON-TILE-ROW | overlay | 3 white glass tiles 150 × 150 radius 32 with line icons, at chest-bottom (centre y 1240), x 240 / 540 / 840 | Pop 6 f with 3 f stagger, then drift up 40 px over 1.0 s; exit fade 5 f | Announcing a count ("3 skills", "3 tools") | no text (icons) | `VEOS.fx.card` × 3 or bespoke with `fx.icon` |
| **P-21** | ICON-LABEL-PAIR | overlay | White icon circles Ø 100 + condensed labels 44 px, one each side above the head (y 160–420), appearing one per spoken item ("ONE SKILL TO SELL" + "GREAT COMMUNICATION") | Pop 6 f on each item word; hold to the end of the pair | Combining two ideas ("deadly combo") | TC-label | bespoke |
| **P-22** | RECAP-GLASS-LIST | state | W-glass: a frosted glass card 760 × 620 radius 36, ghost header "CONCLUSION" 40 px, rows typed as spoken (title 56 px, sub-bullets 42 px) | Rows appear on their words 4 f each; the card drifts up 30 px; exits blurring back 8 f | The recap before the CTA | TC-label | `VEOS.fx.card` (glass) with body |
| **P-23** | BRANCH-MAP | annotation | W-grid: a polaroid of the presenter (a still from the A-roll, 14 px white border, rotated 2°) top-centre; hand branches curve down to 2–3 icon tiles with marker labels ("BUILDING STUFF", "CREATIVE FIELDS") | Polaroid drops 8 f; each branch draws 10 f and its label writes 10 f on the spoken option | "Either X or Y" choices | TC-label · ink | bespoke |

**B-5 Explainer cards**
| ID | Name | Type | On screen | Motion | Use when | Class · needs | Engine |
|---|---|---|---|---|---|---|---|
| **P-24** | GLASS-APP-CARD | overlay | W-glass: a window card 520 × 360 radius 28, white 10% fill, 2 px `accent` rim at 40%, inner glow, three window dots, an icon on top (fx.icon 72 px), title Inter Tight 700 60 px; a ghost of the previous card above, blurred 12 px | Card rises 60 px + de-blurs over 10 f; the next card pushes it up and out (T-10: 6 f out, 8 f in) | Naming a skill, tool or category ("Building", "Video Editing", "AI Automation") | TC-label | `VEOS.fx.card({theme: "glass"})` |
| **P-25** | GLASS-FLOW | state | W-fog: white glowing outline nodes (Ø 260 circles with icons) and frosted cards connected by 4 px glowing lines; node titles 64 px (`ink` in the light centre, `paper` at the edges) | The view travels node to node in-scene (18 f each, ease in-out); each line draws 10 f; icons pulse 6 f on their word | A mechanism or pipeline ("scrapes data → filters jobs → writes the email") | TC-label | `VEOS.fx.diagram` with in-scene translate |
| **P-26** | STEP-TABLE | figure | L-stack top band: a dark card with a grit title ("5 SIMPLE STEPS", Anton 96 px) and up to 5 rows (number 44 px + two columns, Inter Tight 500 40 px) | Rows appear on their spoken step, 4 f each; the active row brightens, others 60% | A routine or plan the presenter walks through (> 5 s) | TC-label | bespoke in the stack's graphic rect |
| **P-27** | SITE-CARD-TAG | overlay | A site/app card 460 × 640 (the creator's screenshot SH-5, or a recreated generic UI) top-left of the frame clear of the face by 40 px + a condensed tag ("PROJECT 2", 52 px) top-right with a hand arrow to the card | Card rises 10 f; arrow 10 f; the tag pops 6 f | Showing examples one by one ("project 2, project 3, project 5??") | TC-label · ink · insert (if third-party) | `VEOS.fx.shot` / `fx.appUI` + arrow scene |
| **P-28** | NEON-CHIP-WORD | overlay | W-white: a screenshot or card (creator or recreated) with a condensed keyword on a `primary` chip stamped at its lower-left edge ("TWEAKING,", "HOSTING") | Chip pops 6 f (scale 1.2 → 1.0); the card pushes in 1.00 → 1.04 over the beat | A feature or step name on a product view | TC-display | `VEOS.fx.shot` + chip scene (`overlaps` the card) |
| **P-29** | DOC-FOLDER | overlay | L-stack top band or W-space: a folder icon 180 px (drawn) + label "Detailed Document" 44 px; a cursor glides in 12 f and clicks (folder scale 0.94 → 1.0) | As stated | The deliverable / resources ("I've attached a detailed document") | TC-label | bespoke (`fx.icon` folder + cursor) |
| **P-30** | PAPER-HEADLINE-CARD | overlay | A newspaper-style created headline card (masthead set in type, date, the exact headline from the script, `primary` highlight bars on the spoken phrase), in the L-stack top band | Card rises 10 f; highlight bars wipe word by word from the phrase's word | A story or news fact the script states | TC-label · insert (created) | `VEOS.fx.headlineCard({theme: "paper"})` |

**B-6 Stylised inserts**
| ID | Name | Type | On screen | Motion | Use when | Class · needs | Engine |
|---|---|---|---|---|---|---|---|
| **P-31** | STYLISED-CLIP | footage-treatment | A creator B-roll clip full-bleed (L-graphic), 0.8–2.2 s, with one treatment (§4.4); CS-4 caption (CS-2 when a face or product sits centre) | In on the noun by a T-04 1 f flash or a hard cut; an entry punch 1.00 → 1.14 over 8 f ease-out, or a slow pull-out 1.08 → 1.00 over the clip (§4.4); never the same treatment twice in a row. **Variant P-31b** (FB-4/FB-6): a Z-1 punch of the A-roll with GR-bw for ≤ 1.2 s. **Variant P-31c** flicker montage (T-12): 5–8 clips × 5 f, one treatment, one caption |  Any concrete noun the creator has footage of (office, team, city, money, a laptop) | footage | `VEOS.fx.clip({kenburns: [1, 1.04]})` + CSS filter |
| **P-32** | PEOPLE-TOPLINE | footage-treatment | Team/people B-roll with the two-tier caption in the top band naming the object ("here's a / MacStudio") | As P-31; the topline caption appears with the cut | Showing who uses what, team members, clients | footage | `fx.clip` + `captions.overrides` CS-2 |
| **P-33** | PRODUCT-CIRCLE | overlay | W-grid: a big `accent` circle Ø 760 (centre y 1000) with 2–4 product cut-outs (creator photos) or `fx.logoPlate` tiles; the two-tier caption across it ("uses an / apple device") | Circle scales 0.6 → 1.0 in 10 f; products pop 4 f stagger; a slow 2° rotation | A category of products or tools | TC-label (plates) · insert if third-party | bespoke + `fx.logoPlate` |
| **P-34** | FACE-CUTOUT-REVEAL | overlay | W-paper: a grit statement in `ink` (Anton 200 px, "HIMSELF / REVEALED") with the person's cut-out (creator-owned photo) or `fx.silhouette` in front of its middle; or tool icons orbiting the cut-out | Statement lines slam 4 f each; the cut-out pops 6 f; orbit 1 rev / 4 s | Introducing a person the story is about | TC-display · insert (person) | bespoke / `fx.silhouette` |
| **P-35** | MONO-STATEMENT | overlay | W-black: a B&W illustration or creator photo (GR-bw) with a grit statement above and a second line below that appends ("MOST PEOPLE GET DISTRACTED" / "ONCE" → "ONCE EVERY 2 MINS") | Image push 1.00 → 1.05; line 2 grows on its words (4 f per word) | A sharp fact about people or habits | TC-display · figure if a number | bespoke |
| **P-36** | ALERT-GRADE | footage-treatment | A-roll under GR-alert (red monochrome) + a ⚠ icon (160 px, paper with ink glyph) + a grit statement "PROBLEM" (paper 220 px) at chest | Grade strobes on the word (every 1–2 f for 0.75 s; §4.4), then holds and releases on a cut; ⚠ and statement appear only on the red frames, statement slams 5 f on the first | `warn` lines; the re-hook (≤ 2 per reel) | TC-display · grade event | z11 overlay (`mix-blend-mode: color`) + scene |
| **P-37** | WORD-DISINTEGRATE | overlay | W-paper: a grit word in `ink` ("CRUSH YOU") with a small chip above ("AI"); it breaks into 40–60 seeded particles that drift right | Hold 0.6 s, then particles over 12 f (`ctx.rngStable`) | "replace", "destroy", "crush" lines | TC-display | bespoke canvas scene |
| **P-38** | DM-SHARE-MOCK | overlay | A recreated generic chat screen (dark, no platform logo): the creator's video thumbnail as a sent message + a typed bubble with the spoken share line ("bro, let's do this together?") | Bubble types 1 word per 3 f; send 4 f | The share CTA ("share this video with…") | TC-label · insert (created) | `VEOS.fx.appUI({kind: "chat"})` |
| **P-39** | CALL-FRAMES | overlay | W-grid: two framed stills (the creator's call screenshots, 10 px white border, soft shadow) stacked; a neon hand tag with an arrow names the person (only the name the script says) | Frames drop 8 f, 4 f stagger; arrow 10 f; tag 6 f | "I hired him over a call", testimonials the creator owns | TC-label · ink · insert (creator) | `VEOS.fx.shot` × 2 + arrow scene |

**B-7 CTA and end**
| ID | Name | Type | On screen | Motion | Use when | Class · needs | Engine |
|---|---|---|---|---|---|---|---|
| **P-40** | QR-CARD | overlay | W-white: the buyer's QR image 560 × 560 centred (top y 520), CS-4 captions in ink above and below (§6.7) | 2 f white flash in (T-04); QR scales 0.96 → 1.00 in 8 f; stays still for the scan | CTA `qr`; also the mid-reel flash | asset | `VEOS.fx.shot({asset: "qr", chrome: false})` |
| **P-41** | END-LOCKUP | overlay | W-black: three-tier lockup centred: connector (Inter Tight 700 48 px) above-left, grit hero (Anton 260–320 px), trailer (48 px) below-right ("one last push / 90 DAYS / before 2026 ends") | Connector 6 f, hero slam 5 f, trailer 6 f; hold 1.5–3.0 s; hard end | `end_card` close | TC-display | bespoke, `kind: "end-card"` |
| **P-42** | OFFER-CARD | overlay | W-black: lockup ("NOT JUST A / VIDEO EDITING / COHORT 14": connector 44 px caps, neon Barlow 700 200 px, trailer 44 px), a scarcity line from the script ("100 seats left", 44 px), a glowing code line in `primary` ("USE CODE …", 52 px), the URL 40 px | Lines appear per spoken phrase 4 f; the code glow breathes | Promoting the creator's own product (numbers only from the script) | TC-display/label | bespoke, `kind: "end-card"` |
| **P-43** | KEYWORD-HERO | overlay | A-roll: the CTA keyword as a neon grit hero behind the head, connector "comment" above (§6.7) | As P-01; the keyword glow breathes ±8% | CTA `comment_keyword` | TC-display · E1 | scene `kind: "cta-keyword"`, `behind: true` |

### 8.4 Line → pattern lookup `[NICHE]`
Classify every sentence with this table (P5). [NICHE: example] rows cover the two example niches: **careers & money** (students, freelancers, job seekers) and **fitness & nutrition** (coaches). New line types are appended per reel (Part D.6).

| Line type | Primary | Alternates |
|---|---|---|
| A money amount ("₹1,20,000 a month", "₹60 a day") | P-03 neon odometer behind the head | P-15 pin-on-line, P-12 card |
| A count of items ("3 skills", "5 habits") | P-01/P-05 grit hero + P-20 tiles | P-21 icon pair |
| A duration or year ("5 years since", "90 days") | P-13 ruler + P-04 count steps | P-06 ticker |
| Zero → result ("from ₹0 to …", "92 kg to 76 kg") | P-09 prop pair tags | P-10 vessels (no props), P-14 slider |
| A threshold / sweet spot ("5–6 projects", "35–40 minutes") | P-14 stat slider | P-15 |
| Naming a skill, tool or category | P-24 glass card | P-01 grit hero, P-33 product circle |
| A mechanism / pipeline ("it scrapes, filters, writes") | P-25 glass flow (L-graphic ≤ 5 s, then L-stack) | P-26 table |
| A routine or step list longer than 5 s | P-26 step table in L-stack | P-22 recap |
| A person's story ("this 18-year-old built…") | P-02 hero + P-11 tag on the photo prop, then P-30 headline card | P-34 cut-out reveal (silhouette if no owned photo) |
| A news or public fact | P-30 created headline card (exact words) | — |
| The creator's own team, office, clients | P-32 people topline / P-31 clip | P-39 call frames |
| A product or device | P-33 product circle / P-31 clean clip | P-11 tag on the real device |
| Examples of work ("project 2, 3, 5") | P-27 site cards with tags | P-28 chip words |
| A warning / problem / mistake | P-36 alert grade + "PROBLEM" | P-07 statement |
| A principle or quote to remember | P-07 statement bleed | P-35 mono statement |
| "Replace / crush / destroy" | P-37 disintegrate | P-07 |
| Either/or choice | P-23 branch map | P-21 icon pair |
| Funnel or result metrics stated | P-16 metric tiles | P-03 for the single biggest one |
| [NICHE: example] careers: "without a degree / college" | P-12 card "DEGREE" (real or drawn) | P-01 grit "NO DEGREE" |
| [NICHE: example] careers: "send cold emails / outreach" | P-25 glass flow | P-38 chat mock |
| [NICHE: example] careers: "build a portfolio" | P-18 spotlight sheet (if a step) / P-27 site cards | P-24 |
| [NICHE: example] fitness: "eat 120 g protein" | P-03 neon number + P-31 clean food clip | P-12 card |
| [NICHE: example] fitness: "walk 8,000 steps" | P-13 ruler (steps axis) or P-15 pin | P-03 |
| [NICHE: example] fitness: "most people quit in week 2" | P-35 mono statement + P-06 ticker | P-07 |
| Deliverable ("I've attached a document / guide") | P-29 doc folder | P-40 QR flash |
| Share line ("send this to a friend") | P-38 DM mock | caption only |
| Comment / scan / link CTA | P-43 / P-40 / caption "link / in bio" | P-41 |

### 8.5 Data and truth rules
- Every displayed number is a figure in `plan/figures.json` (§18) written by `ctx.fmtNum`; counters land on the spoken word ±5 f.
- **Countable where possible:** "3 skills" = three tiles; "5 projects" = five cards; "₹0 → ₹1,00,000" = two glasses.
- **Same axes:** a result pair uses two identical vessels or tags at the same size; sliders keep one scale per reel.
- **Real or script-stated numbers only**; illustrative counters (a roll that only suggests growth) carry the TC-legal "example" tag and no number not in the script.

### 8.6 Comedy layer
OFF (`tone.comedy: off`). The evidence has no gags. A buyer may switch to `light` (≤ comedy_max): then ≤ 3 stickers per reel (emoji or 1–2 word chips, 6 f pop), never on the face, never during a hero, no meme SFX.

### 8.7 Asset rules
- **Real first:** the creator's own props, B-roll, screenshots and QR image.
- **Allowed mocks:** generic, unbranded UIs (`fx.appUI`, `fx.device`); never a look-alike of a real brand; never invented numbers inside them.
- **No stock clichés** (N6). No fetched logos: a product is a creator photo or an `fx.logoPlate` with the name set in type.
- **Third-party moments:** ask once, then create (§12.5).

### 8.8 Density and variety
- An insert or card every 4–8 s; a hero every 8–15 s; ≥ 8 distinct patterns per 60 s; ≥ 4 families per 60 s.
- The same pattern at most 2 beats in a row (the item ritual's marker is the exception).
- One hero, one insert, one caption and one tag at most at once (G2: ≤ 3 text blocks).

---

## §9 Transitions & shot grammar `[REQ] [DNA]`

### 9.1 Library (measured at full frame rate, converted 25 → 30 fps)
| ID | Transition | Frames | Recipe | SFX role |
|---|---|---|---|---|
| **T-01** | Jump cut + crop change | 0 | Hard cut on a word boundary ±1 f; the crop changes on the cut (Z-1 / Z-2; 49 of 56 measured face-to-face cuts change crop, median ×1.32). ≈ 60–70% of all boundaries | none |
| **T-02** | **Zoom-blur cut** (replaces the old "whip smear"; no streak bars appear in the evidence) | 3 + 3 | Built in: `{"t": <cut>, "type": "zoom-blur", "frames": 6, "pre": 3, "punch": 0.12, "amount": 0.18, "at": "face", "layers": "all"}`: the outgoing shot pushes 1.00 → 1.12 into the cut with a blur ramp, the incoming one arrives ≈ 1.10 and blurred and clears in 3 f; `layers: "all"` so captions and heroes blur with the picture (v01 @0:06.46, @0:17.79; strip-c01, strip-k01). No camera events and no z11 defocus scene | whoosh |
| **T-03** | Punch cut | 0 | = T-01 into the tight or mid level (Z-1 with `crop: "tight"` or `"mid"`) or back to wide (Z-2); never the same level twice in a row | none (soft tap on a hero) |
| **T-04** | White flash | 1 (2) | One full-white frame on the cut: `{"t", "type": "flash", "frames": 1, "pre": 0, "peak": 1}` (pure white, or `colour` = white tinted 8% toward `primary`, v05 @0:33.33). Major (2 f) into a new take or the re-hook (v03 @0:28.57): two 1 f flashes on consecutive frames, `peak: 0.7` on the frame before the cut, then `peak: 1` on the cut. Captions stay on top (`layers` default). Measured 3–14 per minute (v05 14, v01 7, v04 6), ≤ 1 per 2 s (; V-FLASH counts every flash) | camera / shine |
| **T-05** | Smoke dissolve | 12 | `fade-through` 6 f + a smoke overlay scene (blurred white clouds, 0 → 40% → 0) over 12 f into W-space | riser end |
| **T-06** | Focus pull in | 6 | The incoming shot starts defocused, built in on the footage: `"blur": [{"t": <cut>, "kind": "defocus", "px": 20, "frames": 6, "shape": "decay"}]`, always with a Z-6 settle-out under it (v04 @0:00: `p.land: 1.5`, 13 f) | none |
| **T-07** | Split cut | 0 | Hard cut into L-stack; the top graphic is already settled on the cut frame (v03 @0:12.87) | pop |
| **T-08** | Disintegrate out | 12 | P-37 particles leave, then a hard cut | swish |
| **T-09** | Hard end | 0 | Last frame ≤ 6 f after the last word; no fade, no black tail | none |
| **T-10** | Card push | 12 | The current glass card rises 60–80 px, defocuses to 10 px and dims to 50% (it stays as a ghost above); the next card rises from 300 px below, scaling 0.5 → 1.0 with blur 12 → 0 over 12 f; its title types on at 1 letter/f (v01 @0:12.9; strip-s01) | swish (soft) |
| **T-11** | Panel push | 13 | Horizontal push, built in: `{"t", "type": "push", "dir": "left", "frames": 13}`: the outgoing world (footage window and world together) slides out left while the incoming shot slides in from the right, ease in-out, peak ≈ 130 px/f (v04 @0:53.8; strip-w04). Graphic → face returns only, ≤ 2 per reel | swish |
| **T-12** | Flicker montage | 5 per clip | 5–8 creator clips of 5 f each (0.16 s at 25 fps) under one caption, one shared treatment (`neon_mono`), entered by a 2 f overexposed T-04 (v05 @0:06.52–0:07.56; strip-m05). ≤ 1 per reel, total ≤ 1.5 s | riser end / hit |

### 9.2 Grammar
| Boundary | Use | Never |
|---|---|---|
| Frame 0 | Z-6 settle-out (or T-06 + Z-6 from 1.5) or Z-4 settle-push on live footage | A static frame, a fade from black |
| Into the hook hero | Hero slam on its word (no cut needed) | A hero that appears without motion |
| Hook → first insert | T-04 1 f flash or T-02 zoom-blur cut on the noun | A crossfade |
| A-roll ↔ A-roll | T-01 / T-03 with a crop change (wide → tight → mid → wide …) | Two identical crops in a row |
| Inside a long A-roll shot (> 1.5 s) | One animated move: Z-3 blur-punch on the claim word, Z-4 settle-push, or Z-6 settle-out on a new take | A zoom that bounces back inside the shot |
| Into B-roll / a new take | T-04 flash (1 f) or T-02 | A slow dissolve |
| New item | G-4 cut into the marker world (T-05 smoke the first time into W-space; T-02 otherwise) | A slow dissolve |
| Back to the face | G-6 return punch (Z-1 tight first), or T-11 from a graphic world | A world fade |
| Card → card | T-10 card push | A still jump |
| Number lands | Glow ignite on the number (no camera shake: none in the evidence) | Shake |
| CTA | T-04 white flash into W-white (QR) or a T-01 cut to the keyword hero | A zoom-blur during the CTA words |
| Last word | T-09 | A black tail |

### 9.3 Shot grammar
OFF (spine `talking_head`, single presenter).

### 9.4 Budget (per 60 s; measured on v01–v05)
- Cuts 25–48 per minute (median shot 1.0–2.1 s, p90 2.9–4.4 s).
- T-02 zoom-blur cuts + Z-3 blur-punches together **8–16** (blurred transition clusters measured 8.5–18 per minute); T-04 flashes **4–8** (3–14 measured; never 2 within 2 s); T-05 ≤ 1 per reel; T-08 ≤ 1; T-11 ≤ 2; T-12 ≤ 1; GR-alert ≤ 2 per reel.
- The same transition never 3× in a row except T-01/T-03, which is the rhythm itself.

---

## §10 Motion, camera, layers, finishing `[REQ] [DNA; motion tokens TUNE ±15%]`

### 10.1 Motion tokens (30 fps)
| Token | Value |
|---|---|
| Lead | Visuals 2 f before the onset; caption words 1 f |
| Entries | `cubic-bezier(0.22, 1, 0.36, 1)` (expo-out), 6–10 f |
| Exits | `cubic-bezier(0.64, 0, 0.78, 0)`, 4–5 f (or on a cut) |
| Hero slam | x +140 → 0 in 5 f, 3 smear ghosts, crackle f3–f8, settle 1.03 → 1.00 f5–f9 (measured 4 f at 25 fps, v03 @0:00.20–0:00.32) |
| Number roll | **tick** (default, measured v01 @0:02.0, @0:06.6): the value updates every frame with ease-out, 10–24 f; the fill ramps `paper` → `primary` across the roll; on landing the glow flickers on alternate frames for 4 f, then breathes. **slot** (v05 @0:01): digits roll in fixed slots 14–22 f, vertical blur 12 → 0 px |
| Count step | 4 f per step, scale 0.92 → 1.00 |
| Caption swap | **hard** (0 f): words and chunks appear and swap on their onsets with no animation (v05 @0:00–0:00.6, v04 @0:07.8); on CS-2 toplines the keyword may slide in from the left with motion blur, 6 f (v04 @0:22.06) |
| Pop (tags, tiles, chips) | 6 f, overshoot `cubic-bezier(0.34, 1.56, 0.64, 1)` |
| Tile stagger | 3 f |
| Hand arrow | shaft 7 f + head 3 f; tag writes 10 f |
| Ruler slide | 12 f, then a 20 px drift over the hold |
| Defocus | 20 px max on the footage (`timeline.blur` defocus, T-06 6 f in); T-02 is the built-in `zoom-blur` (3 f out + 3 f in) |
| Hold | Titles ≥ 10 f after built; text ≥ 0.25 s per word; heroes ≥ 1.5 s (E1 ≥ 0.6 s) |

### 10.2 Footage camera (`zoom_policy: presets`): measured with ORB affine tracking on every frame of v01–v05
Crop levels (face width vs the reel's widest A-roll crop): **wide 1.00 · mid 1.15–1.22 · tight 1.30–1.45** (median crop change on a cut ×1.32; v04 reaches ×2 on 4K-class sources; our 1080p cap is 1.35). Animated moves on the A-roll: **0.3–1.1 per 10 s** (median 0.8) on top of the cut crops. Every move **holds until the next cut**: no zoom ever returns to its start inside a shot.

| ID | Preset | Measured (evidence) | Recipe (30 fps) | Use |
|---|---|---|---|---|
| **Z-1** | `snap-punch` "tight on the cut" | crop jumps ×1.21–1.39 on the cut frame, then creeps +2–4% over 6 f (v01 @0:25.16 ×1.38, @0:49.56 ×1.29; v02 @1:14.88 ×1.28; v03 @0:48.52 ×1.21) | On the cut: `{"t", "preset": "snap-punch", "crop": "tight"}` (1 f, 1.325 = the preset's `levels.tight` midpoint) or `"crop": "mid"` (1.185), held to the next cut; crops are about the face | The tight / mid half of the alternation (hype, explain, warn, win) |
| **Z-2** | `pull-out` "wide on the cut" | — | `{"t", "preset": "pull-out"}`: → 1.00 (the wide level) in 1 f on the cut | The wide half, takeaways, CTA |
| **Z-3** | `crash-zoom` "blur-punch" | 1.00 → 1.26–1.44 over 8–13 f, peak speed +8–10%/f at f3–f5 with motion blur (v04 @0:07.72 ×1.26, @0:32.72 ×1.44; v05 @0:02.96 ×1.30; strip-x04, strip-z04, strip-c05) | 1.00 → 1.30 over 12 f, `ease: "inOut"` (built in: peak speed mid-move, as measured), engine motion blur; behind heroes ride it (`follow_footage: true`). On a mid / tight crop write `p.from: "inherit"` with `p.scale` ≤ 1.35 so it pushes on from the crop on screen instead of snapping back to 1.00 | On the claim / number word mid-shot; hero moments |
| **Z-4** | `settle-push` | 1.00 → 1.10–1.19 over 7–16 f, ease-out (v01 @0:00.24, @0:05.0, @1:27.4; v02 @0:00.08, @0:32.64; v03 @0:00, @0:32.96) | 1.00 → 1.12 over 14 f (1.18 / 8 f at f0) | f0, explanations, the recap, the last line |
| **Z-5** | `rotation-snap` "dutch roll" | ≈ 1°/f for 5–6 f → 5–6° with a 1.05 push (v05 @0:25.7, @0:31.7) | 0 → 5° with scale 1.16 over 7 f, reset at the next cut | The re-hook, a warning, a "wait" beat; ≤ 3 per reel |
| **Z-6** | `settle-out` | starts zoomed and eases out: 1.22 → 1.00 / 12 f (v05 @0:00), 1.53 → 1.00 / 13 f under a defocus (v04 @0:00), 1.15 → 1.00 / 15–23 f on new takes (v03 @0:29.92, v05 @0:18.36, v01 @0:30.28, @1:15.04) | `land: 1.22` → 1.00 over 12 f, ease out (`p.land` up to 1.5 with T-06, `p.frames` 13) | f0, the first frame of a new take, after a T-02 |
| **Z-7** | `zoom-through` "crash-in" | accelerating 1.00 → 1.56 over 18 f, ends on a cut (v01 @0:08.56) | 1.00 → 1.5 over 20 f (`ease: "in"` in the preset), cut on the last frame | Into a graphic world on its noun; ≤ 2 per reel |

Rules: never the same crop level twice in a row (Z-1 tight → Z-1 mid / Z-2 wide); never two camera moves within 0.4 s; never an animated move during the CTA words; a 1080p source allows ≤ 1.35× total (crop × move), 4K is needed beyond; zooms never push the face out of the frame. A behind hero rides every camera move (`follow_footage: true`) as in the evidence (v04 @0:32.7 "15 DAYS" grows with the punch); cap Z-3 at 1.15 while a hero is up so it stays ≥ 90% inside the frame and within E1. Captions never move with the camera.

### 10.3 Canvas camera
OFF (§21). Hub and flow travel is done inside one scene by translating and scaling the diagram (eased, ≥ 18 f per move).

### 10.4 Layer order (back to front)
1. World background (z1) / footage
2. **Behind heroes (`behind: true`, z3): grit words, neon numbers, keyword hero**
3. Presenter cut-out (matte) — the head and shoulders occlude the hero
4. Cards, clips, data (z3–4)
5. Hand tags, labels, prop tags (z5)
6. Markers (z6)
7. Captions (z7, CS-1…CS-4)
8. Statements and end lockups (z8; captions hide)
9. — (comedy off)
10. —
11. Smoke and grade overlay scenes (z11, momentary). Flashes, the zoom-blur cut, the panel push and the footage defocus are drawn by core (`timeline.transitions` / `timeline.blur`), not as scenes

### 10.5 Finishing
- No film grain on footage, no vignette on footage (the room is shot dark already). Vignette lives only inside worlds (§3.1) and the `bw_vignette` treatment.
- Grit texture only on Anton heroes and statements; glow only on neon numbers, the active node, tokens and the offer code.
- Cards: radius 28–36, soft shadows (0 20 60 rgba(0,0,0,.45)); no hard offset shadows anywhere.

---

## §11 Sound contract (minimal) `[REQ] [VAR]`
| Line | Decision |
|---|---|
| **Cue moments** | `hook` (f0 hit, hero impact, counter roll), `transitions` (T-02 zoom-blur cuts, T-04 flashes, T-05 smoke, T-11 pushes), `reveals` (heroes, counters landing, cards, tiles), `list_cue` (one file for every item marker), `cta` (QR flash or keyword hero) |
| **Meme cues** | Off (comedy off) |
| **Music bed** | On; enters on the first item marker (after the hook) |
| **Ducking** | The bed sits ≥ 18 dB under the voice while the voice speaks |
| **Loudness** | −14 LUFS integrated, true peak ≤ −1.5 dBTP; hard end ≤ 6 f after the last word (NC-8) |

The sounds themselves come from the bundled SFX pack and its rules S1–S6 (≤ 2 uses per file, one list-cue file, no consecutive repeats, every cue on a picture event).

---

## §12 Footage requirements, shot list, fallbacks, inserts `[REQ]`

### 12.1 Setups `[DNA what the style assumes; VAR the buyer's actual setups]`
| Setup | Spec |
|---|---|
| **A: desk, front-on** (all A-roll) | Seated at a desk, camera at eye level 70–90 cm away, vertical 1080 × 1920 or 4K; low-key warm practicals behind (lamp bokeh, a shelf); a dark or earth-tone plain tee/hoodie (no big logos: captions sit on the chest); the desk surface visible in the bottom 15–25% for props. **Framing:** head top y 300–560, eyes y 620–820, chin y 800–1050, face x 330–750 (the hero needs 160–480 px of room above the head) |
| **B: side angle** (optional) | The presenter working at the same desk from three-quarter or profile, 3–6 s per clip, for statement bleeds and focus beats |
| Frame rate / audio | 25–60 fps (conformed to 30 CFR); a lavalier or shotgun mic out of frame |

### 12.2 Shot list `[DNA]`
| ID | Shot | Spec | Per 60 s | Must / optional | Fallback |
|---|---|---|---|---|---|
| **SH-1** | A-roll | The whole script at the desk (setup A); retakes welcome (they become jump cuts) | the whole reel | **must** | — |
| **SH-2** | Hook prop take | The first 3–4 s performed with 1–2 props in hand or on the desk at chest-to-desk height (PR-1…PR-5) | 1 | optional | FB-2 |
| **SH-3** | Handwritten cards | White card or paper, black marker, 1–2 words or a number ("₹60/DAY"), shown to the lens on the word | 0–3 | optional | FB-3 |
| **SH-4** | Own B-roll | 1–3 s clips: team, office, clients, the product, the city, life moments the creator owns | 4–12 | optional | FB-4 |
| **SH-5** | Screens | Screen recordings or screenshots of the named tools, sites, documents (creator-owned) | 0–6 | optional | FB-5 |
| **SH-6** | Side angle | Setup B, 3–6 s | 0–2 | optional | FB-6 |
| **SH-7** | CTA target | The QR image (PNG, ≥ 600 px), or the URL, or the keyword | 1 | optional | FB-7 |
| **SH-8** | Desk list | 3–5 chips/tokens/cards in a row on the desk for list reels | 0–1 | optional | FB-8 |

### 12.3 Fallbacks
| ID | For | What the engine does instead | Fidelity cost | Result |
|---|---|---|---|---|
| **FB-2** | SH-2 | P-10 result-pair vessels or a drawn P-12 card/photo, in the L-stack top band or on W-glass, with the same tags and counters | No tangible object in the hands; the hook loses its physical surprise | degraded |
| **FB-3** | SH-3 | P-12 drawn card pops beside the presenter at chest height | No in-hand action | holds |
| **FB-4** | SH-4 | An engine visual on the noun: P-24 glass card, P-33 circle with logo plates, a silhouette, or P-31b (an A-roll punch with a treatment) | Fewer real-world cutaways | holds |
| **FB-5** | SH-5 | `fx.appUI` / `fx.device` recreated generic UI, or a P-24 card with the name in type | No real product footage | holds |
| **FB-6** | SH-6 | Z-1 tight punch of the A-roll with GR-bw behind the statement | No second angle | holds |
| **FB-7** | SH-7 | Switch the CTA to `comment_keyword` (P-43) or `link_bio`; never draw a QR | No scan action | holds |
| **FB-8** | SH-8 | P-19 token carousel carries the count | No physical list | holds |

The checkpoint lists every fallback used in the reel.

### 12.4 Props, reaction bank, matte, resolution
- **Props:** PR-1 two clear glasses (red-tinted / green-tinted water) for result pairs; PR-2 a printed photo of the story's subject (creator-owned) or of the creator; PR-3 2–4 handwritten cards; PR-4 3–5 chips or tokens; PR-5 the device or product the reel is about.
- **Reaction bank** (2–3 s each, optional): pointing at the lens; counting fingers 1–5; palms-up shrug; leaning in.
- **Matte:** required (RVM, whole clip; hair checked at 200% where heroes sit).
- **Resolution:** a 1080p source allows punches ≤ 1.35×; 4K allows 2×. Z-1 is 1.30× (works on 1080p).

### 12.5 Third-party inserts: ask, then create `[REQ always]`
1. **Analyse the transcript** (`veos inserts scan`) and list moments that call for third-party material: another person's photo or story, a news headline, a company's product UI, another creator's clip, a brand logo.
2. **Ask {{BV-01.name|the creator}} once:** "For these N moments, do you have a clip or screenshot you own? Drop the files, or say no."
3. **Supplied:** use as given (crop, frame, highlight), never altered to say something it doesn't.
4. **Not supplied, create:**
   - a person's photo → `fx.silhouette` (P-34 variant) with the name from the script;
   - a news story → `fx.headlineCard` (P-30) with the exact headline words;
   - another product's screen → `fx.appUI` generic UI (P-27);
   - a logo → `fx.logoPlate` (name set in type);
   - another creator's clip → `fx.appUI({kind: "video"})` with a caption, or a P-24 card.
5. **Record** every moment in `plan/inserts.json` (`origin: creator | created`). Patterns that show third-party material: P-27, P-30, P-34, P-39.

### 12.6 Frame rate and audio
30 fps CFR output, 1080 × 1920, BT.709. Voice chain: high-pass 80 Hz, de-ess, light compression, −14 LUFS.

---

## §13 Output contract `[REQ] [DNA]`

### 13.1 Core beat fields
`id`, `section` (HOOK · LOOP · ITEM-n · REHOOK · PAYOFF · CTA), `t0`/`t1`, `spoken`, `trigger {word, at}`, `tone` (hype · explain · warn · win · cta), `line_type` (§8.4), `layout` (L-full · L-stack · L-graphic), `visual` (one sentence), `layers` (scene ids), `pattern` (P-…), `sfx`.

### 13.2 Conditional fields used by this style
| Field | Content |
|---|---|
| `caption` | `{profile: CS-1…CS-4, keyword: "<word>" \| null, drop: ["<word a hero shows>"], overrides: [...]}` |
| `hero` | `{pattern: P-01…P-06 \| P-43, text, kind: word \| number \| lockup, placement: centre \| head_gap \| lockup, colour: paper \| primary, exception: "E1", hold_s}` |
| `camera` | `Z-1…Z-7` (Z-1 with `crop: tight | mid` for the crop level) or null (never the same twice in a row) |
| `transition_in` / `transition_out` | `T-01…T-10` |
| `world` | `W-…` when the layout is L-graphic or L-stack |
| `anchor` | `{target: "prop:<label>" \| "object:<label>" \| face, point: {x, y}, follow: none}` (from the anchor pass) |
| `ink` | `[{mark: arrow \| curved_arrow \| branch \| underline, from, to, frames}]` |
| `figure_id` | the `plan/figures.json` id for every displayed number |
| `motif_state` | SM-1 only: `{active_node: "<item>", lit: [...]}` |
| `clip_treatment` | `halftone \| invert \| bw_vignette \| warm_tint \| clean` (creator clips) |
| `grade` | `GR-alert` or null |
| `shot_id`, `fallback_used` | `SH-…`, `FB-…` |
| `insert` | `{id, origin: creator \| created}` for third-party moments |
| `exception` | `E1` / `E5` / `E6` (also on the scene) |

```yaml
- id: 4
  section: HOOK
  t0: 0.84
  t1: 2.10
  spoken: "you can make up to one lakh twenty thousand rupees per month"
  trigger: {word: "twenty", at: 1.12}
  tone: hype
  line_type: money_amount
  layout: L-full
  visual: "Neon ₹1,20,000 rolls behind the head and ignites lime; caption 'rupees / per month' on the chest"
  layers: [hero-salary]
  pattern: P-03
  caption: {profile: CS-1, keyword: "rupees", drop: ["one", "lakh", "twenty", "thousand"]}
  hero: {pattern: P-03, text: "₹1,20,000", kind: number, placement: centre, colour: primary, exception: E1, hold_s: 2.2}
  figure_id: salary
  camera: Z-1
  transition_in: T-01
  sfx: [{id: "<counter-roll id from the pack>", on: "hero-salary@0", why: "odometer roll"}]
```

### 13.3 Reel header
`format: F-A`, `theme: TH-lime | TH-mint | TH-yellow` (the rotation slot), `hook_archetype`, `structure: list`, `marker: SM-…`, `count`, `cta {device, keyword | url | qr_asset}`, `figures` (ids), `props` (PR-… used), `fallbacks` (FB-… used).

### 13.4 Hook proposals (3)
```yaml
- name: "Prop + hero: salary without a degree"
  archetype: HA-08
  hero: "₹1,20,000"            # P-03, behind the head, lands by 1.4 s
  pair: {subject: "handwritten card DEGREE (PR-3)", reveal: "₹1,20,000 per month"}
  stoppers: [ST-1, ST-2, ST-3, ST-4, ST-5, ST-6]
  captions: ["you can make up to", "rupees / per month", "without a / degree"]
  storyboard: "f0 settle-out | 0.2 words build | 0.9 odometer rolls | 1.4 lands + lime glow | 2.0 caption keyword | 2.6 card to lens"
  sound: [f0 hit, counter roll, glow shine, whoosh into the first insert]
  stopper_test: {thumbnail: pass, mute: pass, read_s: 0.9, changes_3s: 11, payoff_s: 1.4}
```

### 13.5 Checkpoint
Send, then **wait for approval**:
1. 3 hook proposals with stopper-test results; the recommended one first.
2. The beat sheet with tones, heroes (text, placement, hold) and caption keyword choices.
3. The transition map and camera plan (Z alternation shown).
4. The SFX ledger.
5. `plan/figures.json` with every displayed number and its source.
6. The inserts record (creator-supplied vs created) and the fallbacks used (FB-…).
7. Style stills: f0, the hero at 1.7 s, one item marker, one glass card, one stylised clip, the CTA.

---

## §14 Worked examples `[REQ] [NICHE]`
Times are estimates; replace them with `words.edit.json` onsets. The personaliser rewrites these for the buyer's niche after their first approved reel.

### 14.1 [NICHE: example] Careers & money: "₹0 to ₹1 lakh a month editing videos as a student" (HA-01, SM-2, TH-lime, CTA qr)
Props: PR-1 two glasses (red, lime-green). 72 s.

| t (s) | Spoken | Tone | Visual | Caption (CS-1) | Camera / transition |
|---|---|---|---|---|---|
| f0 | — | hype | Desk, red glass left, green glass right; the presenter mid-gesture; Z-6 settle-out | — | Z-6 |
| 0.17 | "Here's how" | hype | — | "Here's how" | — |
| 0.5 | "you can go" | hype | — | "you" → "you can" → "you can go" | — |
| 1.1 | "from making" | hype | T-02 zoom-blur cut | "from making" | T-02 |
| 1.4 | "zero" | warn | Tight on the red glass; P-08 "₹0" red tag 40 px above its rim | (dropped) | Z-1 |
| 2.0 | "to" | hype | In-camera whip-pan to the green glass | "to" | T-02 |
| 2.2 | "one lakh a month" | win | P-09 counter ₹0 → ₹1,00,000 in `good` over 20 f, lands on "lakh" | "a / month" (keyword "month") | hold |
| 3.0 | "as a" | hype | Pull out: both tags; connector "as a" | "as a" | Z-2 |
| 3.4 | "video editor" | hype | P-01 grit "VIDEO EDITOR" behind the head | (dropped) | — |
| 5.0 | "even if you're a student" | hype | P-12 drawn card "STUDENT" pops at chest right | "even if / you're a / student" | Z-1 |
| 6.5 | "in 4 steps" | hype | P-20 four icon tiles pop at chest-bottom | "in / 4 steps" | Z-2 |

| Section | Spoken (gist) | Tone | Layout / world | Patterns | Hero |
|---|---|---|---|---|---|
| Loop 7–9 s | "99% of students fail at this" | warn | L-full | Z-5 dutch roll | P-03 "99%" neon (figure) |
| Step 1 9–22 s | "Pick one outlier skill" | explain | G-4 → W-glass SM-2 sheet "STEP 1 / OUTLIER SKILL"; back to L-full; P-24 glass cards "Building", "Video Editing", "AI Automation" (T-10 pushes) | P-18, P-24, P-31 (own desk clip, `warm_tint`) | P-01 "ONE SKILL" |
| Step 2 22–35 s | "Build 5–6 great projects" | explain | SM-2 sheet "STEP 2 / SOLID PORTFOLIO"; P-14 slider 0 → 5–6 → 10+ (✕ low credibility / ✓ high credibility) | P-18, P-14, P-27 site cards "PROJECT 2" | P-02 "5-6 PROJECTS" (head gap) |
| Re-hook 35–38 s | "But here's the problem" | warn | P-36 GR-alert + "PROBLEM" | P-36 | — (statement) |
| Step 3 38–52 s | "Set up an outreach system" | explain | SM-2 sheet "STEP 3"; W-fog P-25 glass flow (scrapes → filters → writes) 4.5 s, then L-stack with P-16 tiles (512 / 148 / 37 / 16 if the script states them) | P-25, P-16 | P-03 "216+" gigs (figure) |
| Step 4 52–62 s | "Close clients on a call" | win | SM-2 sheet "STEP 4 / CLOSE CLIENTS"; P-39 call frames (creator screenshots) | P-18, P-39 | P-01 "CLOSE" |
| Recap 62–66 s | "So: one skill, 8–10 hours a day, a system" | explain | W-glass P-22 recap rows | P-22 | — |
| CTA 66–72 s | "Scan this QR code for the entire guide" | cta | T-04 flash → W-white P-40 QR (creator's QR) 3 s; hard end | P-40 | — |

Figures: `zero` (0, script "zero"), `target` (1,00,000, script "one lakh"), `pct_fail` (99, script), `projects` (5–6 range, script), `gigs` (216, script). Mid-CTA QR flash at 44 s (61%).

### 14.2 [NICHE: example] Fitness & nutrition: "Stop doing these 3 exercises if your back hurts" (HA-05, SM-1, TH-mint, CTA comment_keyword "BACK")
No props. 58 s.

| t (s) | Spoken | Tone | Visual | Caption | Camera |
|---|---|---|---|---|---|
| f0 | — | hype | Connector "Stop doing these" fades in at y 140–220; Z-4 settle-push | — | Z-4 |
| 0.17 | "these" | hype | P-01 grit "3 EXERCISES" slams in behind the head (lockup by 0.7 s) | — | — |
| 0.8 | "if your back hurts" | warn | Hero holds | "if your / back / hurts" (keyword "back") | Z-1 |
| 2.2 | "every morning" | warn | P-20 three icon tiles (back, dumbbell, clock) pop at chest-bottom | "every / morning" | Z-2 |
| 3.0 | "number one" | explain | T-05 smoke dissolve into W-space; P-17 hub overview, node 1 lights | "number / one" | — |

| Section | Spoken (gist) | Tone | Layout / world | Patterns | Hero |
|---|---|---|---|---|---|
| Item 1 3–15 s | "Toe touches with straight legs" | warn → explain | SM-1 node 1 "TOE TOUCH"; L-full; own clip of the wrong form (`bw_vignette`), then the right form (`clean`) | P-17, P-31 ×2 | P-01 "TOE TOUCH" |
| Item 2 15–27 s | "Sit-ups load the spine" | explain | SM-1 node 2; P-07 statement bleed "YOUR SPINE / ISN'T A HINGE" behind the presenter; P-12 drawn card "PLANK" | P-17, P-07, P-12 | — (statement is the hero beat) |
| Re-hook 27–30 s | "The third one surprises everyone" | hype | Z-5 dutch roll; P-01 "LAST ONE" behind the head | — | P-01 |
| Item 3 30–44 s | "Heavy deadlifts in week one" | warn | SM-1 node 3; P-36 GR-alert + "PROBLEM"; P-13 day ruler "WEEK 1 → WEEK 6" | P-17, P-36, P-13 | P-04 "6 WEEKS" (figure) |
| Recap 44–50 s | "So skip these three" | explain | SM-1 overview returns: "SKIP THESE / 3" + all nodes lit | P-17 | — |
| CTA 50–58 s | "Comment BACK and I'll send you my 10-minute routine" | cta | P-43 keyword hero "BACK" (mint glow) behind the head, connector "comment"; caption "and I'll send / my 10-minute / routine" | P-43 | P-43 |

Figures: `weeks` (6, script), `routine_min` (10, script).

### 14.3 [NICHE: example] Careers & money, story reel: "This 19-year-old makes ₹1,20,000 a month without a degree" (HA-08 default, SM-4, TH-yellow, CTA end_card + link_bio)
Props: PR-2 a printed photo of the creator's own student (consent given; creator-owned), PR-3 card "DEGREE". 64 s.

| t (s) | Spoken | Tone | Visual | Caption | Camera |
|---|---|---|---|---|---|
| f0 | — | hype | The presenter holds the photo to the lens, mid-motion; Z-6 settle-out; T-04 1 f white flash on the photo at 0.5 (v02 polaroid flash) | — | Z-6 |
| 0.0 | "the story of this" | hype | Connector "the story of this" top-left above the hero band (P-05) | (dropped: the connector shows it) | — |
| 0.8 | "nineteen year old" | hype | P-02 grit "19 YO" split around the head (head gap), white | (dropped) | — |
| 1.5 | "student" | hype | P-11 hand tag "STUDENT" + curved arrow to the photo | "student" | Z-1 |
| 2.3 | "will blow your mind" | hype | Hero holds | "will / blow / your mind." | Z-2 |
| 3.4 | "he makes" | hype | T-04 1 f flash; P-31 creator clip of the student at work (`warm_tint`) with CS-2 top band | "he makes" | T-04 |
| 4.6 | "one lakh twenty thousand a month" | win | Back to L-full; P-03 neon ₹1,20,000 rolls and ignites yellow | "a / month" | Z-1 |
| 6.2 | "without a degree" | hype | P-12 real card "DEGREE" to the lens | "without a / degree" | — |

| Section | Spoken (gist) | Tone | Layout / world | Patterns | Hero |
|---|---|---|---|---|---|
| Setup 8–20 s | "He used to distribute newspapers for ₹60 a day" | explain | P-31 creator clip (`halftone`), P-12 card "₹60/DAY" | P-31, P-12 | — (the card carries "₹60/DAY") |
| Twist 20–26 s (re-hook) | "The weird part? He never went to college" | hype | Z-5 dutch roll; P-01 "NO COLLEGE" behind the head | — | P-01 |
| Numbers 26–40 s | "Two years ago he joined our first batch" | explain | P-13 year ruler "2024 → 2026", the current year yellow; L-stack P-30 created headline card only if the script quotes a real article (else none) | P-13 | P-04 "2 YEARS" |
| Lesson 40–54 s | "Skills beat degrees when you show proof" | win | P-07 statement "SKILLS / BEAT / DEGREES" on a creator clip; P-27 his portfolio site card (creator-owned) + tag "HIS SITE" | P-07, P-27 | — |
| CTA 54–64 s | "If you want the same roadmap, link in bio" | cta | Caption "link / in bio" + arrow; then P-41 end lockup "one last push / 90 DAYS / before 2026 ends" 2.5 s; hard end | P-41 | — |

Figures: `age` (19), `salary` (1,20,000), `daily` (60), `years` (2). Inserts: I1 the student's photo (creator), I2 clips (creator). No third-party media.

---

## §15 QA checklist `[REQ] [DNA]`

**1. Profile conformance**
- [ ] Format F-A; the theme is the next rotation slot (lime → mint → yellow) (review)
- [ ] Face visible 60–80%; no faceless run > 5.0 s (V-PRESENCE)
- [ ] Runtime 55–90 s (review)

**2. Hook**
- [ ] f0: live footage already moving (Z-6 settle-out or Z-4 settle-push from f0); the prop in frame when used; the first caption word by f3 (V-F0)
- [ ] The hero is landed by 1.7 s (HA-08) / result by 2.0 s / number by 1.0 s / lockup by 0.7 s, and holds ≥ 1.5 s (V-F0)
- [ ] ≥ 8 weighted changes in 0–3 s; the hero reads at 25% scale; the mute test passes (V-CADENCE, review)

**3. Body and cadence**
- [ ] 10–28 SC per 10 s; no gap > 1.2 s; nothing static ≥ 2.0 s (V-CADENCE)
- [ ] 24–50 cuts per minute; every face-to-face cut changes the crop level (wide / mid / tight), never the same level twice; ≈ 1 animated move (Z-3/Z-4/Z-6) per 10 s that holds to the next cut, never bounces back; 4–8 one-frame flashes and 8–16 zoom-blur cuts / blur-punches per minute (V-CAMERA, review)
- [ ] Every item follows the ritual (§7.3) with one marker style; the re-hook sits at 40–60% (review)
- [ ] Inserts 0.8–2.2 s; treatments never repeat back to back (review)

**4. Captions**
- [ ] Every word captioned (except hero-dropped words), 1–4 words per chunk, ≤ 0.15 s lead, words appear on their onsets (V-CAPTION)
- [ ] One keyword max per chunk; 35–50% of chunks carry one; keyword 136 / connector 56 / plain 72 px (ratio ≥ 1.7) (V-CAPTION, V-TYPE)
- [ ] CS-2 used over centred people/product B-roll; ink on light worlds (review)
- [ ] Glossary spellings exact; profanity masked (V-CAPTION)

**5. Modules**
- [ ] **Hero / E1:** ≤ 1 behind hero; ≥ 65% visible; first and last letters visible; hold ≥ 0.6 s (V-EXC)
- [ ] **E5:** ≥ 180 px, ≥ 24 px margin, never in NC-5 bands (V-EXC, V-SAFE)
- [ ] **Anchors / ink:** tags within 40 px of their prop's anchor point; arrows end on their target; ≤ 2 marks on screen; never on the face (V-FACE, review)
- [ ] **Data:** every number on screen is a figure, formatted ₹ + Indian grouping; counters land ±5 f (V-DATA, V-NUMFMT)
- [ ] **Continuity (SM-1):** the hub returns at every item with the active node lit (review; V-CONTINUITY when available)
- [ ] **End cards:** ≤ 4 s; keyword/URL/QR readable ≥ 1.5 s (V-PROMISE)

**6. Truth and inserts**
- [ ] Every third-party moment is creator-supplied or a created substitute, recorded in `plan/inserts.json` (V-INSERTS)
- [ ] No invented results, earnings or testimonials; illustrative counters tagged "example" (V-DATA)

**7. Sound contract**
- [ ] Cues only on hook, transitions, reveals, list cue, CTA; the bed enters at the first marker; nothing in the 1.0 s before the CTA (S1–S6)
- [ ] −14 LUFS, true peak ≤ −1.5 dBTP, bed ≥ 18 dB under the voice (mix gate)

**8. End and export**
- [ ] CTA hold ≥ 1.5 s; hard end ≤ 6 f after the last word; no black tail (V-PROMISE, review)
- [ ] 1080 × 1920, 30 fps CFR (render check)

---

## Conditional modules (§16–§25)

### §16 Frame template
OFF (`profile.modules.chrome = false`): the frame changes every 1–2 s; there are no persistent slots.

### §17 Running state & anchored graphics `[COND: modules.anchors] [DNA mechanics]`
**17.1 Running state:** OFF (`modules.running_state = false`): numbers are performed inside their beat (P-03, P-04, P-09); a value shown again later is the same figure re-rendered, not a persistent display.

**17.2 Anchors (ON):**
- **Targets:** `prop:<label>` (the red glass, the green glass, the photo, a desk chip), `object:<label>` (a laptop, a card), `face` (the hero placement and the caption chest anchor use the engine's face boxes).
- **Mode:** `static`. In P10 (the anchor pass) read sampled frames of the hook take and write one anchor point per target per shot (x, y of the prop's rim centre). Tags sit 40 px above that point; arrows end 12 px short of it.
- **Fallback:** `static_near_target`: if the prop moves more than 60 px during the tag's hold, end the tag at the next cut instead of following it (keyframes wait for E-15).
- **Rules:** an anchored element never covers the face (40 px clearance); a tag's text never sits below y 1500.

### §18 Data contract `[COND: modules.data_figures] [DNA rules]`
- Every displayed number is a figure in `plan/figures.json`: kinds `hero_number` (P-03), `counter` (P-04, P-06, P-09, P-16), `slider` (P-13, P-14), `line` (P-15).
- **Inputs** come from the script with the spoken words (`from: script, said: "one lakh twenty thousand"`), or `spoken@t`. Formulas from the safe set (`sum`, `diff`, `ratio`, `percent_change`, `per_period`, `compound`, `cagr`, `unit_convert`); most heroes are stated values (`none`).
- **Format** from `profile.numbers`: `₹1,20,000` (full) on heroes ≤ 9 characters, `₹12.5 L` (short) beyond; percentages `99%`; durations as integers with the unit word.
- **Illustrative** rolls (a counter suggesting growth without a stated value) carry `illustrative: true` and the TC-legal "example" tag, and show no number.
- Example (§14.3): `{"inputs": {"salary": {"value": 120000, "from": "script", "said": "one lakh twenty thousand"}}, "figures": [{"id": "salary", "kind": "hero_number", "formula": "none", "value": 120000, "steps": [{"value": 120000, "at": 4.95}], "format": {"currency": "₹", "style": "full"}}]}`.
- **V-DATA / V-NUMFMT** run on every reel.

### §19 Evidence & citations
OFF (`modules.citations = false`): no credit lines. A created headline card (P-30) carries the exact headline from the script (§12.5).

### §20 Dialogue
OFF (single presenter).

### §21 Canvas camera
OFF (`graphics: support`; PV-5). Diagram travel happens inside one scene (§10.3).

### §22 Ink & annotation layer `[COND: modules.ink] [DNA look; TUNE colour]`
- **Stroke:** `paper` on dark grounds, `ink` on light ones (TUNE: `paper` or `primary`), 5–7 px, round caps, wobble 1.2 px, drawn over 10 f with an 8° overshoot at the head.
- **Marks:** arrow (straight), curved arrow (P-11, P-27, P-39), branch (P-23), underline (under a card word, 6 f).
- **Labels:** Permanent Marker 44–60 px caps (§5.4).
- **Rules:** ≤ 2 marks on screen; marks finish drawing before the next scene starts; never on the face; an arrow always ends on its target (anchor point).

### §23 Continuity `[COND: modules.continuity] [DNA]`
- **Motif M-hub** (SM-1): the marbled sphere Ø 150–210 with a 36 px glow and its spokes; the same diagram (same node positions) returns at every item; the active node is lit (`primary`) and earlier nodes stay white; the overview returns at the recap.
- With SM-2 the recurring element is the sheet stack (it grows one sheet per step); with SM-3 the token row (one token moves up per item).
- **Morph chain:** not required (hard cuts are the style). **Bookend:** off.

### §24 Series furniture
OFF (`modules.series = false`). A buyer may switch it on (VAR); the series tag then sits top-left at y 120–170 as a condensed label.

### §25 End cards `[COND: cta ∋ end_card] [DNA look; VAR assets]`
- **QR card (P-40):** W-white, the buyer's QR 560 × 560, two-tier ink captions above and below, 2–4 s at the end, 1.5–2.0 s mid-reel.
- **End lockup (P-41):** W-black three-tier lockup, 1.5–3.0 s.
- **Offer card (P-42):** the creator's own product only; every number (seats, price, discount) from the script; a code line glowing in `primary`.
- **Rules:** end cards ≤ 4.0 s; the keyword, URL or QR readable ≥ 1.5 s; black tail ≤ 0.2 s.
- **Sponsors:** none by default; if a reel carries one, NC-12 applies: "Paid partnership" (TC-legal 24 px) top-left for ≥ 2 s, spoken too.

---

## Part C. Declared exceptions and the non-overridable core

### C.1 Non-overridable core (applies unchanged)
| ID | Rule (short) |
|---|---|
| NC-1 | Nothing in front of the face box; behind-subject heroes are not "in front" |
| NC-2 | Meaning text never overlaps meaning text |
| NC-3 | Smooth motion; no teleports; camera moves ≥ 0.4 s apart |
| NC-4 | Absolute floors (display 40, subtitle 36, label 28, legal 22), contrast ≥ 4.5:1 (3:1 display ≥ 96 px) |
| NC-5 | No meaning text at y < 110, y > 1540, or x > 970 between y 900 and 1540 |
| NC-6 | No invented facts, numbers, testimonials or UIs presented as real |
| NC-7 | Creator-owned media only; created substitutes otherwise |
| NC-8 | −14 LUFS, true peak ≤ −1.5 dBTP, bed ≥ 18 dB under the voice |
| NC-9 | Deterministic frames, seeded randomness |
| NC-10 | ≤ 4 bright hues (this style: 2) |
| NC-12 | Sponsors disclosed in speech and on screen |
| NC-13 | Quotes verbatim and attributed |
| NC-14 | Personal identifiers blurred (emails, phone numbers, IDs in screenshots) |

### C.2 Exceptions this template declares
E1 (behind-subject type), E5 (edge bleed), E6 (hard swap), with the limits in §2.2 and `tokens.json → exceptions`. Each scene that relies on one sets `exception: "E1" | "E5" | "E6"` (one id per scene). A buyer may switch any of them off (stricter, VAR); switching E1 off moves every hero above the head as a P-05 lockup clear of the face (the style loses its signature; Part D warns).

---

## Part D. Personalisation

### D.1 Branding questions (one round, each with "keep the template default")
| ID | Question | Default | Lands on |
|---|---|---|---|
| BV-01 | Your name and handle | {{BV-01.name|the creator}} · {{BV-01.handle|@yourhandle}} | `creator.name/handle` |
| BV-02 | One or two brand colours | keep the neon rotation (lime → mint → yellow) and the blue glass glow | `roles.primary`, `roles.accent` (contrast-nudged); a brand colour replaces the rotation |
| BV-05 | The language you speak, and your captions | English ({{BV-05.speech|en}} → {{BV-05.captions|en}}) | `profile.language`, always asked: **English** → English captions (default) · **Hinglish** → romanised Hinglish captions · **Hindi** → Devanagari captions; numbers follow (BV-06) |
| BV-08 | Your call to action | QR card (needs your QR image), or comment keyword, or link in bio | `profile.cta.chosen`, `creator.cta` |

### D.2 Lock summary (full map in `tokens.json → locks`)
| Area | Lock |
|---|---|
| Talking head, host presence, support graphics, primary captions, medium footage | DNA |
| Two-tier mechanics (word reveal, split stack, ratio ≥ 1.7, one keyword per chunk), hero behind the head, whip/punch camera presets, per-reel rotation policy, transitions | DNA |
| Caption sizes (connector 54–66, keyword 120–160, plain 60–84), chest offset 140–280, hero sizes, cadence ±15%, motion ±15%, world tints, font families inside their class | TUNE |
| Neon and glass colours, language, numbers, CTA device and values, marker style per reel, props, setups, sound cue moments, bed | VAR |
| §6.4 hook pairs, §8.4 lookup rows, §14 examples, App. A bank | NICHE |

### D.3 NICHE slots (filled per reel)
Hook pairs (§6.4) and lookup rows (§8.4) are appended at P9/P5 of each reel; §14 becomes the buyer's first approved reel; approved heroes join App. A; confirmed brand names join the glossary.

---

## Part E. Deviations from the coverage table and the analysis (with evidence)
| Decision | Coverage / analysis said | This template | Why |
|---|---|---|---|
| Split layout | "no split screens" (analysis §2) | **L-stack added** (0–20%) | v03 @0:13–0:14 (5 SIMPLE STEPS table over the presenter), @0:22–0:25, @0:39–0:40, @0:44–0:47 are top-graphic / bottom-face splits |
| running_state | on (odometer, ticker) | **off** | Numbers are performed inside their beat; no display persists across cuts. Data figures carry them (V-DATA, V-NUMFMT are live; V-STATE is not built) |
| Cadence | 5–8 SC/10 s | **10–28** | With primary captions weighted 1.0, chunk swaps alone give 10–16 per 10 s; 5–8 would fail every correct reel |
| E6 | E1, E5 | **E1, E5, E6** | Odometer digits and count steps swap inside a fixed slot (v01 @0:02, v04 @0:01) |
| E1 occlusion | evidence frames sometimes hide ~45% of a numeral (v05 "1,20,000") | **≥ 65% visible** (registry) + placement rules (§5.2) | The registry limit is approved and non-negotiable; the head-gap and baseline rules reproduce the look within it |
| Money grouping | Indian ₹ | **Indian ₹ everywhere** | v01's counter used international grouping on ₹ ("₹500,000"); inconsistent with v05 and the coverage decision |
| CTA set | qr / comment_keyword | **+ link_bio, end_card; placement mid+end** | "in bio" v02 @0:47; end lockups v03 @0:59, v05 @1:00; QR shown twice in v02 and v04 |
| Default speech | ? (unverified) | **en → en verbatim** | Captions read as verbatim English in all five reels; the buyer chooses at setup |
| Hero colour | white grit and neon | **grit words white, numbers neon, red only for zero** | v03/v02/v04 words are white; v04/v05 numbers are neon; v01 "₹0" is red |
| Strobe alert, flash count | red strobe every 1–2 f for 0.75 s; up to 14 flashes per minute | **as the evidence: every 1–2 f for 0.75 s, then hold** | no flash limit (8 Oct 2026) |
| Camera shake (old Z-6) | in the earlier analysis | **removed** | Not found in any of the five reels at full frame rate; Z-6 is now the measured settle-out |

---

## Part F. IDs used in this playbook
| Prefix | IDs |
|---|---|
| D | D1–D8 |
| H / N | H1–H18 / N1–N14 |
| E | E1, E5, E6 |
| W | W-room, W-glass, W-space, W-fog, W-paper, W-grid, W-white, W-black |
| L | L-full, L-stack, L-graphic |
| G | G-1–G-6 |
| TH / GR | TH-lime, TH-mint, TH-yellow / GR-alert, GR-bw |
| CS | CS-1–CS-4 |
| HA / ST | HA-08 (default), HA-01, HA-07, HA-05 / ST-1–ST-6 |
| SM | SM-1–SM-4 |
| B / P | B-1–B-7 / P-01–P-44 |
| T / Z | T-01–T-12 / Z-1–Z-7 |
| SH / FB / PR | SH-1–SH-8 / FB-2–FB-8 / PR-1–PR-5 |
| F | F-A |
| BV | BV-01, BV-02, BV-05, BV-08 (asked); BV-03, BV-04, BV-06, BV-07, BV-09–BV-17 (defaulted) |

---

## App. A Hero & hook bank `[NICHE]`
Ten ready heroes for the example niches, each with its archetype. Swap the bracketed slots for the buyer's topic.

| # | Archetype | Connector | HERO | Trailer / caption line | Niche |
|---|---|---|---|---|---|
| 1 | HA-08 | "you can make up to" | **₹1,20,000** | "per month / without a degree" | careers |
| 2 | HA-05 | "Don't ignore these" | **3 SKILLS** | "if you're / 16–20" | careers |
| 3 | HA-01 | "from" | **₹0 → ₹1 LAKH** (two tags) | "as a / [ROLE]" | careers |
| 4 | HA-07 | — | **5 YEARS** | "since I / STARTED / [THING]" | careers / business |
| 5 | HA-08 | "the story of this" | **19 YO** | "student / will blow your mind" | careers |
| 6 | HA-05 | "Stop doing these" | **3 EXERCISES** | "if your / back / hurts" | fitness |
| 7 | HA-01 | — | **92 KG → 76 KG** (two tags) | "in / 90 days" | fitness |
| 8 | HA-08 | "eat" | **120 G** | "protein / every day" | fitness |
| 9 | HA-07 | "day 1 to" | **90 DAYS** | "of [HABIT]" | fitness |
| 10 | HA-05 | "the only" | **[N] [THINGS]** | "you need for / [GOAL]" | any |

---

## App. B Evidence map
Full source map, measurements and the `(unverified)` list: `evidence.md` (this folder). Summary:
| DNA element | Evidence |
|---|---|
| Two-tier chest captions | v05 @0:02, @0:03, @0:06, @0:22; v02 @0:20, @1:14; v04 @0:40–0:48; v01 @1:16–1:17 |
| Hero behind the head | v03 @0:00.17–0:03; v02 @0:00.83–0:02; v05 @0:01–0:06; v04 @0:01–0:03, @0:32–0:33; v01 @0:07 |
| Punch-cut rhythm and dynamic zoom (measured per frame) | crop change on 49 of 56 face cuts; Z-3 v04 @0:07.72, @0:32.72, v05 @0:02.96; Z-6 v04 @0:00, v05 @0:00; T-02 v01 @0:06.46, @0:17.79; T-04 v03 @0:28.57, v05 @0:33.33 (`docs/audit/two-tier-hero/completeness.md`) |
| Prop hooks | v01 beakers @0:00–0:04; v02 polaroid @0:00–0:03; v05 cards @0:03–0:04, @0:14–0:15; v02 chips @0:25–1:15 |
| Stylised inserts | v05 @0:07 halftone, @0:10 invert, @0:33–0:35 B&W; v01 @0:12–0:14 glass cards |
| Rotating neon | lime v01/v02, yellow v04, mint v05 |
| QR CTA | v01 @1:26; v02 @0:50, @1:22; v03 @0:46; v04 @0:44, @0:56; v05 @0:56 |

Unverified: the speech language and caption transform (no transcripts), sound (not observable), exact hero land times against audio.
