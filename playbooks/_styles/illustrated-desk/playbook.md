# Illustrated Desk Style Playbook (template v1)

**Purpose.** You (Claude) receive {{BV-01.name|the creator}}'s talking-head take, plus any screenshots, screen recordings, logos, photos and B-roll they drop in, plus the script. This playbook makes you edit a calm, bright "illustrated lecture": every thing the creator names gets one small, polished, literal visual (a tool drop, a screen window, a recreated UI, a list row, a book, a calendar), placed in a top band above the head or on a full-screen cutaway, under a soft white caption pill whose words darken as they are spoken. Input (SW-01 `talking_head`): one presenter at a desk; F-C adds the creator's own B-roll.

**How to read it.** Every section is written for the editor. Numbers are px on the final 1080×1920 frame and frames at 30 fps. IDs (H-, N-, W-, L-, G-, P-, T-, Z-, SH-, FB-, CS-) are stable: cite them in the beat sheet and at the checkpoint. `[DNA]` = the style; `[TUNE]` = change inside the stated range; `[VAR]` = the buyer's choice; `[NICHE]` = rewritten per reel for the buyer's topic.

### Style DNA `[DNA]`
A friendly, well-lit desk talker explains something useful, and **every noun they say turns into a neat, real-looking object** within a second: the app's tile and name drop in above the head, a glowing-rimmed screenshot slides into the top band while the face moves down to make room, a list of goals stacks up on a deep navy cutaway, a chat thread scrolls on a pastel gradient. A rounded off-white pill near the bottom carries 2–5 words at a time, each word turning from grey to near-black as it is spoken. A few hand-drawn red circles and scribbles sit on top of the clean UI. Nothing shakes, nothing flashes, nothing shouts: one yellow glow headline per reel at most. It reads as tidy, generous and premium.

**Copy these 5 things** (each is load-bearing):
1. **The karaoke pill** — Poppins 600, 50 px, 2–5 words, light-grey pill (#E6E4E7, opaque, 96 px tall) at cy 1420 (F-B 1220), spoken words #111111, queued words #666666 (the reels use ≈ #A0A0A0; held darker for the legibility floor) (§5.3 CS-1).
2. **The top-band insert with make-room** — one insert in x 150–930, y 130–560 while the footage lowers 220–340 px (L-topband, G-1; §3.2, §3.3, P-07, P-08).
3. **One named thing, one distinct visual** — each tool, book, person or idea gets its own literal visual within 1 s of its name, each tool name set in its own type voice (§8.3 P-07, H6).
4. **Calm cutaway worlds** — navy #0A1220 for concepts (glow headline, list rows, books), paper for calendars and questions, a pastel yellow→green gradient for chat and file UIs (§3.1).
5. **Ink on clean UI** — red (#D92D3A) hand-drawn circles, scribble underlines, handwritten name tags and gold sparkles that draw on in 9–12 f over otherwise flat, perfect cards (§22).

### Directives `[DNA]`
| # | Directive | Where it lives |
|---|---|---|
| D1 | **Name it, show it.** Every tool, app, book, person, place, number and named idea gets its literal visual 2 f before its word and fully on within ±5 f | H6, §8.4 |
| D2 | **The face stays findable.** F-A never loses the face; F-B leaves it for ≤ 6.5 s; F-C for ≤ 12 s. Inserts sit above the head or replace the frame, never on top of the face | H7, H8, §3.6 |
| D3 | **One insert at a time.** One idea per screen: an insert exits before the next enters; at most 1 insert + 1 ink mark group + the pill | H9, G2 |
| D4 | **Quick and clean, never loud.** Graphics move fast and tidily: inserts push in and out sideways in 8 f with a touch of motion blur, words fade on in 3 f, the pill swaps chunks with a hard cut; no shake, no crash zoom, no whip pan of the footage, no glitch, no flashing colour (measured at full frame rate, §10.1) | H10, §10 |
| D5 | **The pill is the constant.** The pill runs on every spoken word except where a card spells the same words (question card, hero statement) | H11, §5.3 |
| D6 | **Real first, then a clean substitute.** Use the creator's screenshot, recording, logo or B-roll; when there isn't one, build a generic, labelled version from the script's words — never a look-alike of a real brand's UI | H13, §12.5 |
| D7 | **Ink means "look here".** Red marks point at the one thing that matters on a card; they never mean good/bad and never touch the face | §22 |
| D8 | **The CTA lives in the post, not the edit.** No end card, no keyword card by default; the reel ends on the face, and the CTA goes in the post title/caption (§6.7). Option, off by default: `profile.cta.on_screen_keyword: true` shows the comment keyword on screen (see §6.7) | H14, §6.7 |

Buyer directives (BD1…) `[VAR]` may only make the style stricter or more specific.

### Quick index
| § | What | Status |
|---|---|---|
| §0 | Style profile (switches, formats) | REQ |
| §1 | Procedure | REQ |
| §2 | Hard rules, exception E3, NEVER list | REQ |
| §3 | Worlds, layouts, stage moves, safe zones | REQ |
| §4 | Colour | REQ |
| §5 | Type and the karaoke pill | REQ |
| §6 | Hook system | REQ |
| §7 | Structure and cadence | REQ |
| §8 | Visual system: 37 patterns P-01…P-37 | REQ |
| §9 | Transitions and shot grammar | REQ |
| §10 | Motion, camera, layers, finishing | REQ |
| §11 | Sound contract | REQ |
| §12 | Footage, shot list, fallbacks, inserts | REQ |
| §13 | Output contract | REQ |
| §14 | Worked examples (F-A, F-B, F-C) | REQ |
| §15 | QA checklist | REQ |
| §16–§21 | Chrome, running state, data, citations, dialogue, canvas camera | OFF |
| §22 | Ink & annotation layer | **ON** |
| §23–§24 | Continuity, series | OFF |
| §25 | Sponsor, brand & end cards | **ON** (no end cards) |
| Parts C–F | Exceptions, personalisation, changes, IDs | REQ |
| App. A / B | Headline bank / evidence map | REQ |

Formats: **F-A Desk list** (default) · **F-B Concept cutaways** · **F-C Story with B-roll**.

---

## §0 Style profile `[REQ]`

```yaml
profile:                         # mirrored in tokens.json -> profile (base = F-A values where formats differ)
  source_type: talking_head
  presenter: {presence: host, share: [45, 100], max_absence_s: 6.5}   # F-A anchor [90,100] 1.0 s; F-C guest [20,45] 12 s
  spine: talking_head            # F-C: hybrid
  captions: {mode: full, role: support, mute_policy: mute_safe}
  graphics: primary              # F-B: support
  duration: {class: short, target_s: [45, 60]}                       # F-C: standard [60, 90]
  language: {speech: en, captions: {lang: en, script: Latn, transform: clean}, on_screen: en, post_title: en,
             supported: [[en, en, Latn], [hinglish, hinglish, Latn], [hi, hi, Deva]]}
  numbers: {grouping: international, currency: "$", compact: k_m_b, units: metric, decimals: 0}
  tone: {energy: calm, comedy: off, comedy_max: light}
  themes: {policy: single, packs: [], default: null}
  formats: {list: [F-A, F-B, F-C], default: F-A}
  footage_dependency: medium     # F-C: high
  cta: {devices: [post_only, link_bio], placement: end}
  modules: {chrome: false, running_state: false, anchors: false, data_figures: false, citations: false,
            dialogue: false, canvas_camera: false, ink: true, continuity: false, series: false, brand: true}
```

Why each value:
- **source_type talking_head** — all three evidence reels are carried by the creator's own take (v01 one desk take; v02 desk take + cutaways; v03 walk-and-talk + B-roll).
- **presenter host** — face share 100% / 52% / 36% (v01/v02/v03). F-A is an anchor (v01 never loses the face); F-B leaves for cutaways up to 6 s (v02 0:10–0:16); F-C runs VO over B-roll and UI for long stretches (v03 0:08–0:21).
- **spine talking_head** — the take is the timeline and visuals are inserted; F-C is hybrid because B-roll carries whole sentences (v03 0:36–0:56).
- **captions full / support / mute_safe** — the pill is on ~95–97% of runtime in all three reels, but the inserts carry the meaning, so captions are support (weight 0.5).
- **graphics primary** — inserts cover ~70% (v01) and ~55% (v03) of runtime; F-B is support (~46%, v02).
- **duration short** — 51 s and 58 s (v01, v02); F-C standard because the story reel ran 86.5 s (v03).
- **language en** — every caption read is English (no transcript existed; speech is read from the burned-in pill, which is word-accurate). Hinglish and Hindi combinations are supported for buyers; the pill works in Latin and Devanagari.
- **numbers international** — v03 shows "$1,840", "$49.70"; Indian buyers get Indian grouping through BV-05/BV-06.
- **tone calm, comedy off** — no gags, stickers or meme beats in any reel; `light` (emoji sticker tabs) is the buyer's maximum.
- **themes single** — one palette with three cutaway worlds (desk, navy, pastel); colours don't switch per topic.
- **formats** — the three reels are three different visual systems sharing the pill, the literal-noun rule and the ink (§0.4).
- **footage_dependency medium** — the style is strongest with the creator's own screenshots, recordings and logos (v01) and needs B-roll for F-C (v03); everything has a created fallback (§12.3).
- **cta post_only** — no reel shows an on-screen CTA or end card; v02 and v03 put "link in bio/description" in the post title.
- **modules** — `ink` (v03 red circles, underline, name tag; v02 handwritten tag) and `brand` (brand-faithful tool titles, own-product segments) are on; everything else is absent from the evidence.

### 0.4 Formats `[DNA set; VAR enable]`
| ID | Name | When (reel type) | Profile overrides | Layouts | Default hook | Structure |
|---|---|---|---|---|---|---|
| **F-A** | Desk list | "N tools / apps / habits / resources I use", "my setup", any numbered list said in one take | presence anchor [90,100], max absence 1.0 s; graphics primary | L-desk, L-topband, L-frost | HA-04 topic build (count title + tile arc) | list |
| **F-B** | Concept cutaways | One idea, principle or method: "focus on one thing", "why X works", a framework with examples | presence host [45,70], max absence 6.5 s; graphics support; captions cy 1220 | L-desk, L-cutaway, L-frost, L-topband | HA-12 question → glow headline | explainer |
| **F-C** | Story with B-roll | A story or case: "a week with…", "how our team…", "what happened when…" | presence guest [20,45], max absence 12 s; spine hybrid; standard [60,90]; footage high; re-hook every ≤ 45 s | L-desk, L-topband, L-cutaway, L-broll, L-frost | HA-04 topic build (ink bubble) | story |

**Shared DNA (one line):** the karaoke pill, one literal polished visual per named thing within 1 s, soft spring motion with no loud effects, red ink accents on clean UI, and a warm, bright desk talker.

Pick the format at P4 from the script: a spoken count of items → F-A; one concept with 2–5 examples → F-B; a chronological story with people or a product in use → F-C. When the script fits two, choose the one whose footage exists (no B-roll → never F-C).

### 0.5 Theme packs
OFF (themes.policy = single). The three cutaway worlds are part of the single palette, chosen per beat by §3.1, not per reel.

---

## §1 Procedure (follow in order) `[REQ] [DNA]`

The craft step of this style is **P5b, the named-thing inventory**: every noun the creator names becomes a row with its visual, its source (creator file or created) and its placement (top band, cutaway, B-roll card).

1. **P1 Inventory.** `ffprobe` every input. Conform VFR to 30 fps CFR. Identify the setup (§12.1 A desk / B standing). Measure the head-top y on 3 frames of the take (full frame) and write it down: it sets the make-room offset (§3.3 G-1). Register every asset with `veos asset add <file> --origin creator` (screenshots, recordings, logos, photos, B-roll).
2. **P2 Prepare.** No matte by default. Make one only for P-17 (a person cut-out from a clip the creator supplied). F-C: tag every B-roll clip `{id, subject, people, place, mood, duration}` (P1b of the `narrated_footage` branch, used here because F-C is hybrid).
3. **P3 Transcribe** with word timestamps. Captions transform per SW-07 (`clean` for English: remove fillers "um/uh", keep every content word). Apply the glossary (brand and tool names exact, case exact). Profanity mask `inner` (on by default).
4. **P4 Segment** into the structure units (§7.1): F-A `HOOK → ITEM-1…ITEM-n → OUT`; F-B `HOOK → PROBLEM → CONCEPT → EXAMPLES → QUESTION → TACTIC → OUT`; F-C `HOOK → CHAPTER-1…n → TURN → OUT`. Mark jump-cut points on word boundaries. Pick the format (§0.4).
5. **P5 Classify** every sentence with a line type from §8.4 and mark its **trigger word** (the noun or number the visual lands on).
   - **P5b Named-thing inventory (the craft step).** List every tool, app, site, book, person, place, product, document and number the script names, in order, with: `name · first word time · line type · pattern (§8.4) · source (creator file id | created recipe) · placement (top band | cutaway | B-roll card)`. Every row must get a visual (H6). Duplicate mentions reuse the first visual only if they come within 6 s; otherwise they get a smaller echo (a tool tile in the corner of a window, or an ink circle on the existing card).
6. **P6 Tone-tag** every sentence: `explain` · `awe` · `win` · `warn` · `cta`. Most lines are `explain`; the one big idea reveal is `awe`; a chosen/finished thing is `win`; "don't do this" is `warn`; the closing invitation is `cta`.
7. **P7 Hook plan.** Pick the archetype from the format default or §6.3, write **3 hook variants** with their headline (≤ 6 words) and run the stopper tests (§6.1).
8. **P8 Visual plan.** One pattern per line from §8.4; the ink plan (≤ 3 marks per 10 s, each on a named target, §22); the third-party list for §12.5 (every P5b row whose source is not a creator file).
9. **P9 Beat sheet** (§13): one beat per trigger word, meeting the cadence of §7.6 and the layout shares of §3.2.
10. **P10 Sound and transitions.** The transition map (§9) and the SFX cues allowed by §11 (from the bundled pack).
11. **P11 Assets.** Ask the creator once for the missing third-party files (§12.5 step 2). Build the created substitutes. Resolve the §12.3 fallbacks and list which ones were used.
12. **P12 Checkpoint** (§13.5), then **wait for approval.**
13. **P13 Build.** Build act by act; `veos scenes-meta` → `veos measure --every 10` → `veos validate`; preview, QA (§15, at most 3 passes); render.

**Branch (source_type talking_head):** P2 matte only for P-17. P4 also marks jump-cut points on word boundaries (±1 f).

**Module steps:**
| Module | Step |
|---|---|
| `ink` | **Anchor pass** at P8: for each ink mark, write its target rect. Targets on created cards come from the card's own layout (you drew them: exact). Targets on the creator's screenshot come from the image's pixel rect scaled into the window. Targets on footage (a person for a name tag) are read from 3 sampled frames of that span and must be static (± 30 px); a moving target gets no ink (use P-30 beside the person instead, ≥ 40 px from the face box). |
| `brand` | **Sponsor check:** is any segment paid, affiliated or the creator's own product? Paid/affiliate → disclosure (§25); own product → no disclosure needed, but the plate is the creator's logo or type. |

---

## §2 Hard rules `[REQ] [DNA]`

### 2.1 Editing rules (every style)
The nine editing rules in `playbooks/_global/GLOBAL-RULES.md` apply. They are directions, not limits: smooth, seamless motion; nothing overlaps by accident; keep the face clear (behind the speaker is fair game, text included); readable at a glance; one idea at a time; show what's being said; never fake facts; pace like the style, not like a timer; the style decides the look.
- **Facts the engine checks:** accidental overlaps, jumps, the face covered, unreadable text, numbers and quotes that don't match what was said, the promised count. Every count, timing and budget this playbook gives is direction for the edit, not a limit.
- **Retired (8 Oct 2026), whatever this playbook says below:** no REPRESENTATIONAL or example labels on made-up cards, no credit lines, no flash limit (flash as often as this style calls for; any "NC-11" cap below no longer applies), and text may sit behind the speaker without an exception.

### 2.2 Declared exceptions
| ID | Limits in this style (≤ registry) | DNA reason | Evidence |
|---|---|---|---|
| **E3 Quiet type** | Pill captions 48–56 px (default 50) at weight ≥ 600, **1 line**, ≤ 30 characters, on a painted pill with contrast ≥ 4.5:1 for every word state (active #111111 ≈ 17:1, queued #666666 ≈ 4.8:1). UI meta text 28–39 px only when `redundant: true` (the same words are spoken or shown larger). Display text stays ≥ 40 px. | The small, soft pill is the style's caption; a 54 px+ caption reads as a different, louder style | Pill measured 48–52 px in v01 @ 0:00–0:50, v02 @ 0:00–0:57, v03 @ 0:05–1:25 |

No other exception is used: no behind-subject text (E1), no chaos bursts (E2), no ambient fields (E4), no edge bleed (E5), no hard swaps (E6; the pill fades).

### 2.3 Style MUST rules
- **H1 Frame 0.** f0 shows the creator on live footage, already moving (gesture or speech). F-A: the first tile grows in by 0.2 s (f0 itself is the gesture) and the count title (kind `title_card`) is readable by 1.0 s. F-B: the pill is on the first word (≤ 0.2 s) and the glow headline cutaway lands by 1.8 s (tag it `payoff: true`). F-C: the ink bubble label (kind `title_card`) starts at f0 and names the subject by 1.0 s. check: V-F0
- **H2 Cadence.** Weighted state changes 5–10 per 10 s (F-B 5–11), ≥ 6 in 0–3 s, no gap > 1.0 s without a full-weight change in the hook, ≤ 4.0 s in the body (F-B 3.5 s), nothing static > 2.5 s (live footage counts as motion). check: V-CADENCE
- **H3 Payoff by 1.8 s.** The topic is on screen as a title by 1.8 s (F-A count title, F-B glow headline, F-C bubble wordmark). check: V-F0
- **H4 Headline limits.** The `title_card` headline is ≤ 6 words, ≤ 2 lines, 0 emoji, readable in ≤ 1.5 s; its serif subline is a separate scene of ≤ 7 words. check: V-TITLE
- **H5 Dead air.** Talking head: ≤ 1 pause ≥ 150 ms per 15 s, cut on word boundaries ±1 f. F-C B-roll stretches may hold a natural breath ≤ 0.4 s between sentences. check: review
- **H6 On-the-word visuals.** Every P5b row's visual starts 2 f before its trigger word and is fully on within ±5 f; tool drops land within ±2 f of the tool name. check: V-ONWORD
- **H7 Face rule.** No element (z ≥ 5) within 40 px of the face box; top-band inserts end ≥ 24 px above the head top after make-room; ink never on the face. check: V-FACE
- **H8 Presenter presence.** F-A share 90–100%, longest absence 1.0 s; F-B 45–70%, 6.5 s; F-C 20–45%, 12 s. check: V-PRESENCE
- **H9 One insert at a time.** At most one top-band insert or one cutaway card group on screen, plus ≤ 3 ink marks and the pill; the outgoing insert has finished its exit before the next one's entry starts (overlap ≤ 2 f). check: review (G2 also enforces ≤ 4 graphics / ≤ 3 text)
- **H10 Clean motion only.** Only the presets of §10.1 and the camera moves Z-2/Z-3 (Z-1 optional); no shake, no crash zoom, no rotation snap, no whip pan of the footage, no glitch, no white flash frames. check: V-CAMERA + review
- **H11 Pill integrity.** The pill shows every spoken word (transform `clean`) on 2–5-word chunks, 1 line, at the format's cy; it hides only under z8 scenes that spell the same words (P-06 hero statement, P-18 question card). check: V-CAPTION
- **H12 Hue cap.** ≤ 3 bright hues per frame (roles primary, accent, concept, data, violet, marker, good); the muted tab tints `warm`/`rose` are never declared as bright roles; at most one glow headline per reel. check: V-HUES
- **H13 Truth in recreations.** A recreated UI (chat, calendar, prompt box, file card) shows only words and numbers the script says (or the creator supplied); it is generic (no real brand's logo, colours or layout) unless it is the creator's own capture. check: V-INSERTS + review
- **H14 Promise integrity.** A spoken count ("5 apps") equals the items shown, in order; F-A shows exactly one tool drop per item. No on-screen CTA element and no end card. check: V-PROMISE
- **H15 Spelling.** Tool, product, book and person names are spelled and cased exactly as the creator writes them (glossary). check: V-CAPTION
- **H16 Audio.** −14 LUFS integrated, true peak ≤ −1.5 dBTP, bed ≥ 18 dB under the voice, hard end ≤ 6 f after the last word (NC-8). check: review (mix gate)
- **H17 Determinism.** Every animation is a function of the frame index; seeded noise only (NC-9). check: review

### 2.4 NEVER list
- **N1** Stock 3D abstract art, glowing brains, generic "productivity" stock clips. Use the named thing itself.
- **N2** A fetched or redrawn brand logo, or a UI that imitates a real product's look (its colour scheme, logo glyph, layout). Logos only from the creator; otherwise the name set in type (P-07).
- **N3** Two inserts at once, or a top-band insert and a full cutaway together.
- **N4** Shake, crash zoom, rotation snap, whip pans, RGB split, glitch, light leaks, film burns, emoji spam.
- **N5** More than one glow headline per reel, or a glow headline on the desk footage (it lives on W-navy only).
- **N6** The pill overlapping a card, a list row or a window (keep ≥ 40 px clear; the evidence's v02 0:26 overlap is a defect, not DNA).
- **N7** Coloured words inside the pill. The pill is two greys only.
- **N8** White or cream text on W-paper / W-pastel; ink text on W-navy (contrast).
- **N9** Ink marks as decoration: every circle, underline or arrow points at the thing being said.
- **N10** An end card, a keyword card, a subscribe sticker or a follow stack.
- **N11** Readable personal data in a creator screenshot (emails, phone numbers, account IDs): blur it for its whole time on screen (NC-14).
- **N12** A recreated chat or file card that invents a stat, a reply, a name or a time the script doesn't give.

Buyer additions BN1… `[VAR]`.

---

## §3 Worlds, layouts, stage moves, safe zones `[REQ] [DNA; coordinates TUNE ±5%]`

### 3.1 Worlds
| ID | Kind | Look | Carries | Enter / exit |
|---|---|---|---|---|
| **W-desk** | footage | The creator's own room: warm, bright, soft key from camera left, bokeh shelf or a pale wall; not regraded | Every talking line, top-band inserts, opinions | Hard cut (T-01) back from a cutaway |
| **W-navy** | stage | `#0A1220` with a soft radial lift (`#14213A` at x 50%, y 42%), grain 0.05, vignette 0.35 | Concepts: glow headline, list rows, book float, object dome, person card, stat card | Hard cut on the noun (T-01); out by hard cut |
| **W-paper** | paper | `#F2F2F0`, grain 0.03, vignette 0.12 (light world: ink text) | Question card, calendar, checklist | Blur-out + cut from the face (T-02) or hard cut |
| **W-pastel** | canvas | Vertical gradient `#F4E3A0` (top) → `#A9E6A3` (bottom), grain 0.02 (light world) | Recreated chat threads, file cards, hub dots (F-C, also F-A for a long UI moment) | Hard cut; leaves by the T-10 curtain wipe (the B-roll slides down over it, v03 @ 22.0) or a hard cut to the face. The card stack drifts slowly while held (≈ 1–2 px/f) |

One cutaway world per beat; never cross-fade two worlds into each other (they switch by cut).

### 3.2 Layout library
| ID | Engine | Presenter | Graphic | Caption band | Treatment | Share F-A / F-B / F-C |
|---|---|---|---|---|---|---|
| **L-desk** | `full` | full frame, head top y 260–380 | none (inserts not allowed) | pill cy 1420 (F-B 1220) | none | 20–45% / 45–65% / 15–40% |
| **L-topband** | `low` (offset 220–340, inline on the stage entry) | lowered by the offset; head top ≥ 584 | x 150–930, y 130–560 | pill cy 1420 (F-B 1220) | the revealed top is the engine's blurred, darkened copy | 50–80% / 0–15% / 5–25% |
| **L-frost** | `full` + `dim {blur_px 18, luma −0.35}` | full frame, blurred and darkened | card zone x 90–990, y 180–1260 | pill cy 1420 | dim | 0–10% / 0–8% / 0–10% |
| **L-cutaway** | `hidden` | none | full frame on W-navy / W-paper / W-pastel; content inside x 90–990, y 160–1300 | pill cy 1420 (F-B 1220) | none | 0% / 30–50% / 15–35% |
| **L-broll** | `hidden` + a z1 `fx.clip` full-bleed | none (the creator may appear inside B-roll) | top band x 150–930, y 130–600 for P-24 | pill cy 1420 | B-roll may take a 0–35% darken under P-06 | 0% / 0% / 25–50% |

The validator holds each layout to the widest range across formats (tokens `layouts.*.share`); the per-format targets above are checked at QA (§15.1).

**Layout schedule rule (F-A).** L-topband is entered on a named noun (a tool, site, document) and left on the first opinion/aside sentence ("I love it because…", "which is super nice") or after the insert's hold (≤ 5.5 s), whichever comes first. Consecutive items may **chain inside L-topband**: the outgoing window pushes out left while the next tool name pushes in from the right (T-11), with no settle-back between them (v01 @ 9.44–9.84 window → "Claude"). When the face does settle back, L-desk runs ≥ 1.5 s before the next make-room.

### 3.3 Stage moves
| ID | Move | Recipe (30 fps) | Use |
|---|---|---|---|
| **G-1** | **Make-room** | Stage entry `{"layout": "L-topband", "offset": O, "via": "morph", "dur": 13, "ease": "out"}` with **O = clamp(584 − head_top_y, 220, 340)** from P1. Measured (v01 @ 0:00.40–0:00.65): the picture moves down ≈ 245 px **and zooms out ≈ 0.89×** over 12–15 f, fastest in the first half (ease-out). The insert's entry starts on frame 4 of the move | Every top-band insert (P-07…P-12, P-24 on footage, P-36) |
| **G-2** | **Settle-back** | `{"layout": "L-desk", "via": "morph", "dur": 12, "ease": "out"}` starting **on the same frame** as the insert's T-11 push-out (they run together, not one after the other). Measured (v01 @ 26.58–27.0): up ≈ 225 px and zoom in ≈ 1.12× over 12 f, ease-out | After the insert's last beat; on the opinion line |
| **G-3** | **Cut to cutaway** | `{"layout": "L-cutaway"}` (via `cut`) + `world` switch at the same t (W-navy / W-paper / W-pastel) on the trigger noun | F-B concepts, F-C UI sequences |
| **G-4** | **Blur-out, then cut** | The pill hides; the face blurs 0 → 20 px and darkens ≈ 15% over 6 f; **hard cut** to the cutaway on the next frame, where the card grows from a point (P-18) — no cross-dissolve (v02 @ 43.27–43.50). Built-in: one `timeline.grades` event ending past the cut, `{"t": cut − 0.2, "t1": cut + 0.2, "fade": 0.2, "grade": {"brightness": 0.85}, "blur": 20}` (the blur and the darken ride the event's 6 f fade envelope and peak on the last face frame; the cutaway hides the footage after the cut), plus a plain `timeline.transitions` marker `{"t": cut}` (no `type`) as T-02 | Face → question card / calendar; a reflective turn |
| **G-5** | **Frost under card** | `{"layout": "L-frost", "via": "dim", "dur": 8}` | A card that must stay full-frame while the face keeps talking (P-25, P-34) |
| **G-6** | **Cut to B-roll** | `{"layout": "L-broll"}` + a z1 `fx.clip` starting at the same t, `kenburns: [1.0, 1.06]`; by hard cut, or by the T-10 curtain wipe (built-in `curtain` transition, §9.1) when it leaves a pastel UI run | F-C sentences told over the creator's own footage |

### 3.4 Layout diagrams
```
L-topband (F-A workhorse)               L-desk                         L-cutaway (W-navy, F-B)
┌─────────────────────────┐ 0          ┌─────────────────────────┐ 0  ┌─────────────────────────┐ 0
│ (IG top UI, keep clear) │ 0-110      │ (IG top UI)             │    │ (IG top UI)             │ 0-110
│  ┌───────────────────┐  │ 130        │                         │    │   GLOW HEADLINE  Anton  │ 300-560
│  │ ONE INSERT        │  │            │        ( head )         │    │   240 px #EBC20E + glow │
│  │ tool drop/window  │  │            │      head top 260-380   │    │   hand subline 58 px    │ 600-660
│  │ x 150-930         │  │ 560        │                         │    │                         │
│  └───────────────────┘  │            │       face + torso      │    │  objects / list rows    │ 700-1180
│        ( head )         │ ≥ 584      │                         │    │  x 130-950              │
│     face, lowered by O  │            │                         │    │ ╭─ pill (F-B cy 1220) ─╮│ 1214-1266
│        torso            │            │                         │    │  ◜ pale dome (P-15) ◝   │ 1320+
│ ╭─ pill cy 1420 ───────╮│ 1372-1468  │ ╭─ pill cy 1420 ───────╮│    │                         │
│                         │ 1540       │                         │    │                         │ 1540
│ (IG caption/UI band)    │            │ (IG caption/UI band)    │    │ (IG caption/UI band)    │
└─────────────────────────┘ 1920       └─────────────────────────┘    └─────────────────────────┘
```

### 3.5 Safe zones and bands
- Meaning text inside x 64–1016, y 110–1500 (NC-5); nothing meaningful in x > 970 between y 900–1540.
- **Top band:** x 150–930, y 130–560 (one insert; its own content may reach x 120–960 for a 2-plate row).
- **Pill band:** centre y 1420 (F-B 1220), height ≈ 96 px (50 px type + 20 px padding top and bottom; measured y 1386–1482, v01 @0:20, @0:45); keep every other element ≥ 40 px above it (y ≤ 1332 for F-A/F-C; ≤ 1132 for F-B content above, or ≥ 1308 below).
- **Cutaway content box:** x 90–990, y 160–1300 (F-B content ends at 1160 above the pill or starts at 1310 below it).

### 3.6 Presenter rules
- Share and longest absence per format: H8.
- **Return:** from a cutaway by hard cut on a sentence start (T-01) (T-02 blur-out + cut only goes face → cutaway); from L-topband by G-2 settle-back.
- **Crops:** L-desk as shot (head top 260–380; the eyes at y 520–640). If the creator's head top is above 260, punch the whole reel to 1.08 (Z-0 base scale) only when the source is ≥ 1440 px wide.
- Nothing sits behind the head (no E1). Ink and name tags stay ≥ 40 px from the face box.

---

## §4 Colour `[REQ] [roles' meanings DNA; brandable hex VAR; muted tints TUNE]`

### 4.1 Role palette
This copy's brand colours: primary {{BV-02.primary|#EBC20E}}, accent {{BV-02.accent|#3FCFC6}} (contrast-nudged at setup; the table lists the template defaults).

| Role | Hex | Its one job | Text on it (ratio) | Brandable |
|---|---|---|---|---|
| `primary` | #EBC20E (sampled v02 @0:02.5; the buyer's colour 1) | The glow headline on navy; the picked row's edge; the one keyword colour on dark worlds | ink (13.0:1) | yes (BV-02 colour 1) |
| `accent` | #3FCFC6 (the buyer's colour 2) | Glow rim of screen windows, the tool-drop underline bar, dashed links, tile glow | ink (9.8:1) | yes (BV-02 colour 2) |
| `concept` | #F2C14E | Gold serif-italic keyword in a hero statement; sparkles | ink (11.3:1); on navy 11.2:1 | yes (TUNE: warm gold) |
| `data` | #2F6BDB | Focus block in a calendar; mentions and links in chat UIs; third rim tint | paper (4.95:1) | yes (TUNE: saturated blue) |
| `violet` | #9B6CF0 | Second rim tint; the app tile in recreated chat UIs | ink (5.2:1) | yes (TUNE) |
| `marker` | #D92D3A | Ink layer only: circles, underlines, arrows | paper (4.8:1) | no (fixed) |
| `good` | #7ED68A | The picked/finished item; a tick | ink (10.7:1) | no (fixed) |
| `warm` / `rose` | #E8C170 / #E58F8F | Muted category tabs on list rows and calendar blocks; never counted as bright | ink (11.1:1 / 7.8:1) | no (TUNE) |
| `ink` | #111111 | Text on cards and the pill (active words); ink-bubble fill | — | no |
| `paper` | #FFFFFF | Cards, windows, tiles; text on navy and footage | — | no |
| `pill` | #E6E4E7 @ 1.0 (sampled on footage and on the pastel world) | Caption pill fill | ink 17:1, queued 4.8:1 | no (TUNE: light neutral) |
| `queued` | #666666 | Caption words not yet spoken | — | no (TUNE) |
| `cream` | #F6EBDD | Serif-italic subline under the count title | — | no (TUNE) |
| `night` | #0A1220 | W-navy | paper 18.8:1 | no (TUNE: deep navy) |
| `canvas` / `grid` | #F2F2F0 / #D9D9D9 | W-paper; hairlines inside UI recreations | — | no |

Gradients: `G-count` #F2A7C3 → #FBE8C8 (count numeral + caps title; VAR, follows BV-02 when the buyer gives a second colour: primary → paper at 70%); `G-pastel` #F4E3A0 → #A9E6A3 (W-pastel; TUNE).

### 4.2 Meanings
- **Neutral is the base.** White cards, off-white pill, navy and pastel worlds. Colour is rare and always means something.
- **Yellow (primary) = the big idea.** Only on navy: the glow headline, the picked row's edge.
- **Teal (accent) = this is a window onto a tool.** Rims, the underline bar under a tool name, links between tools. Rotate rims accent → violet → data across consecutive windows so each tool feels distinct.
- **Red (marker) = look here.** Only hand-drawn ink. Never "bad".
- **Green (good) = the chosen one / done.**
- **Gold (concept) = the phrase to remember** inside a hero statement.
- **Brand colours** appear only on the creator-supplied logo files themselves; created tool plates never use a brand's colour.

### 4.3 Theme packs
OFF (themes.policy = single).

### 4.4 Grades
OFF (no grade events): footage is never regraded; match exposure and white balance between setups only.

### 4.5 Rules
- ≤ 3 bright hues per frame (`max_bright_per_frame` 3; NC-10). A window rim + an ink circle + the glow headline is the maximum; in practice keep 2.
- Coloured text on a light world sits on a chip or is ≥ 4.5:1 (data blue on white passes; gold never goes on paper).
- The glow headline is the only glowing text; window rims are the only glowing shapes.
- Footage is not regraded.

---

## §5 Type & caption system `[REQ]`

### 5.1 Font map `[slots DNA; families TUNE within the class]`
| Slot | Family | Weights | Font class (TUNE boundary) | Used for |
|---|---|---|---|---|
| `body` | Poppins | 500 / 600 / 700 | geometric sans 500–700 | pill, cards, list rows, UI text, tool names (sans voice) |
| `ui` | Poppins | 500 / 700 | geometric sans 500–700 | recreated UI chrome |
| `display` | Anton | 400 | condensed heavy caps | count title, glow headline |
| `numeric` | Anton | 400 | condensed heavy caps | count numeral, stat card number |
| `serif` | Instrument Serif | 400 regular + italic | high-contrast display serif | subline under the count title (italic), tool names (serif voice), bubble fragments |
| `kinetic` | EB Garamond | 700 italic | old-style serif italic 600–800 | gold keyword in hero statements |
| `hand` | Caveat | 400–700 | light handwriting (the ink) | subline under the glow headline, name tags |
| `airy` | Montserrat | 300, tracked +0.28 em caps | geometric sans light, tracked caps | tool names (airy voice) |
| `round` | Lilita One | 400 | rounded heavy display | tool names (round voice), ink-bubble wordmark |
| `mono` | JetBrains Mono | 400–500 | monospace | code chips inside UI recreations |

Brand wordmarks and logos are never fonts: a creator-supplied logo is an image asset; otherwise the name is set in one of the four **type voices** (P-07).

### 5.2 Headline element: `title_card` `[DNA recipe; NICHE text]`
| Property | F-A Count title (P-02) | F-B Glow headline (P-04) | F-C Ink bubble (P-05) |
|---|---|---|---|
| Fill / colour | `G-count` gradient text (#F2A7C3 → #FBE8C8), shadow `0 3 14 rgba(0,0,0,.45)` | `primary` #EBC20E text, 220–260 px Anton (v02 @0:02.5: cap 226 px, 882 px wide) + same-hue glow 22 px (two text-shadows: 0 0 22 px @ 70%, 0 0 6 px @ 90%) | ink #111111 blob at 92% opacity, organic outline (8-point seeded wobble ±6%), paper outline 3 px offset 10 px drawn on |
| Type | Numeral Anton 150 px + caps title Anton 88 px on one line; tracking 0 | Anton 190 px caps, line height 0.95, tracking −1% | Fragment Instrument Serif 46 px (paper; one word in `good` green allowed) + wordmark Lilita One 96 px paper |
| Rect | Group centred on x 540, y 150–310 | Centred, cy 420 (2 lines: y 230–610) | x 220–860, y 130–400 (top band) |
| Words / lines | ≤ 5 words in 1 line (numeral + ≤ 4 words); subline separate (P-03) | ≤ 3 words, ≤ 2 lines; subline separate (hand, 58 px) | fragment ≤ 3 words + wordmark 1–2 words + second fragment ≤ 3 words |
| f0 behaviour | Numeral snaps on (≤ 2 f fade, no rise) on the count word at ≈ 0.44 s; the caps title snaps on beside it (≤ 2 f) on "productivity" at ≈ 0.72 s (v01 strip-v01-hook) | Hard cut in at ≤ 1.8 s, already lit, the hand subline **already complete** on the cut (v02 @ 1.767) | Blob **already on screen at f0** (no scale-in); fragment words fade in 3 f on their onsets; the wordmark fades in 3 f (no overshoot) and the blob grows to fit it over the same 3 f (v03 @ 0.17–0.77) |
| Life | Holds through the hook; tiles (P-01) static once landed | Holds 2.0–3.0 s with the subline and P-15 objects | Sparkles fade in 3 f with the second word, then twinkle (P-31) |
| Lifetime | `hook` (2.5–4.0 s) | `hook` (2.0–3.0 s) | `hook` (1.8–2.5 s); reused as the F-C chapter re-hook (`section`) |
| Exit | Title + subline rocket up off the top with vertical motion blur (8 f, `out: "rocket"`) on the first item word, while tiles 2…N scatter outward (left tiles left, right tiles right, ±20° spin, 8–10 f) (v01 @ 3.08–3.36) | Leaves with its cutaway (hard cut) | Leaves with the hard cut to B-roll (no scale-out, v03 @ 1.80) |

Count rule: a numeral in the title must equal the number of ITEM sections (H14).

### 5.3 Caption system profile CS-1 (the karaoke pill) `[DNA mechanics; size/y TUNE; language VAR]`
| Group | Value |
|---|---|
| Mode | `full` · role `support` (weight 0.5) · `mute_safe` · `extends: lib:ali` |
| Chunking | `unit: group`, 2–5 words (mean 3.3), ≤ 30 characters, **1 line**; never split a name, number or unit; a sentence end breaks (`punct_break`); a pause ≥ 0.6 s always breaks (`hard_pause_s`) |
| Timing | Lead 2 f before the first word; hold ≥ 0.25 s per word; **swap = hard cut (0 f)**: the old chunk is gone and the new one (all words queued grey) is on in the same frame, the pill resizing instantly to the new width (measured: v01 @ 3.16, 20.24, 27.10; v02 @ 0.10, 0.70) — no fade, no rise; no pause hold (the pill hides in pauses > 0.6 s) |
| Skin | Poppins 600, **50 px** (TUNE 48–56), sentence case, tracking 0, commas and full stops kept; container `pill`: fill #E6E4E7 opaque, radius 16, padding 20 × 40 px (pill 96 px tall; text inset 40–43 px, v01 @0:45, v03 @1:20), shadow `0 4 12 rgba(0,0,0,.18)`; no stroke, no text shadow |
| Karaoke | `cumulative`: a word turns from **queued #666666** to **active #111111** over 2 f starting on its onset (measured 1–3 f, v02 @ 0.10–0.60); spoken words stay dark until the chunk swaps |
| Position | `fixed_y`, **cy 1420** (F-B **1220**; measured 1434 v01, 1415 v03, ≈ 1210–1224 v02), centred on x 540, max width 952; `avoid_face: true` (a pill that would touch the face box moves to the chest); colour never flips (the pill carries its own background) |
| Emphasis | `none` — no bold, colour or size change inside the pill (N7) |
| Hide rules | Hidden under z8 scenes (P-06 hero statement, P-18 question card), during stage morphs, during an E2 burst (none used) |
| Language | Latin by default; Devanagari for `hi` (no italics are involved); keep English terms verbatim in Hinglish; glossary spellings enforced; profanity mask `inner` |

Why these numbers: v01 pill at y ≈ 1417–1435, v03 ≈ 1415, v02 ≈ 1225 (tighter framing); 2–5 words with a mean of 3.3; the swap was read as a fade on 6 fps sheets, but full-frame-rate bursts show a hard swap in every reel. The evidence's queued grey (#9B9B9B) fails 4.5:1 on the pill, so this template darkens it to #666666 (Part E).

### 5.4 Other text systems
| System | Class | Recipe | Hold |
|---|---|---|---|
| **Serif subline** (P-03) | TC-label | Instrument Serif italic 50 px `cream`, shadow `0 2 10 rgba(0,0,0,.5)`, centred under the count title at y 330–390; types letter by letter with a 6 → 0 px blur per letter at 1 letter / f | until the title exits |
| **Tool name** (P-07) | TC-display | 80–96 px paper with shadow `0 3 14 rgba(0,0,0,.45)` in one of four voices: **sans** Poppins 700 −2%; **serif** Instrument Serif 400; **airy** Montserrat 300 caps +28% tracking (60–72 px); **round** Lilita One 400 | 1.5–2.5 s |
| **Hand subline** | TC-label | Caveat 600 58 px paper under the glow headline, on screen complete from the cut (no write-on) | with the headline |
| **Hero statement** (P-06) | TC-display | Plain lines Poppins 400 88 px paper; keyword lines EB Garamond 700 italic 92 px `concept`; left-aligned at x 110, from y 300, line gap 18 px; **each word fades in 3 f on its own onset** (no slide) | per line ≥ 0.25 s/word |
| **Card text** | TC-label | Poppins 600 48–56 px ink on paper | ≥ 0.25 s/word |
| **List row label** | TC-label | Poppins 700 58 px ink + one emoji 56 px (Noto Color Emoji) | until the row group exits |
| **UI text** | TC-label | Poppins 500 40 px ink; names Poppins 700 40 px; times and badges Poppins 500 26 px #8A8A8A (TC-decorative) | ≥ 0.25 s/word for the line being read |
| **Name tag** (P-30) | TC-label | Caveat 600 60 px paper with a 4 px paper flourish | 1.5–3 s |
| **Labels on cards** | TC-label ≥ 40 px; 28–39 px only `data-redundant` (E3) | Poppins 600 | — |
| **Legal** | TC-legal | Poppins 500 24 px, paper at 0.85 on dark / #555 on light: "Paid partnership" | the whole time the card is up |

### 5.5 Language and number rules
- English words and brand names exact (glossary; case as the creator writes it: "Notion", "ChatGPT", "iPhone").
- Numbers: international grouping (12,500), `$` pre-painted, K/M/B compacts ("1.2M"); Indian buyers (BV-05 Hinglish/Hindi) switch to Indian grouping and ₹ with lakh/crore compacts (BV-06).
- Numbers inside recreated UIs are written exactly as spoken; never round or invent.
- Devanagari: no italics exist for the pill (none needed); the serif-italic subline becomes Instrument Serif regular in Latin or Noto Sans Devanagari 500 in Hindi; the hand font has no Devanagari, so the hand subline becomes Noto Sans Devanagari 600.

---

## §6 Hook system `[REQ]`

### 6.1 Stopper tests
| Test | This style's number | How it passes |
|---|---|---|
| ST-2 Mute | first 3 s | The topic is readable without sound: count title + tiles (F-A), glow headline (F-B), ink bubble + hero statement (F-C) |
| ST-3 Motion at f0 | ≥ 1 moving element | Live footage mid-gesture (F-A tile 1 follows by 0.2 s; F-C blob already on screen, its first word by 0.2 s) |
| ST-4 Read time | ≤ 1.5 s | Headline ≤ 6 words (0.25 s per word) |
| ST-5 Change count | ≥ 6 weighted SC in 0–3 s | Tile pops, the make-room move, title, subline, pill swaps (×0.5) |
| ST-6 Payoff-by | topic by 1.8 s | The `title_card` (or F-B's glow headline tagged `payoff: true`) is on screen by 1.8 s |

ST-1 (thumbnail at f0) is not used: f0 of this style is the creator mid-gesture. Choose the post's cover frame from 1.0–2.5 s, where title + tiles (or the glow headline) are fully readable.

### 6.2 Default archetype: HA-04 Topic build (F-A) `[DNA]`
Spoken pattern: "These are [N] [things] that I [use / swear by] [every day]." Times are typical; replace them with the word onsets.

| t (s) | Visual | Pill | Layout / camera | Cue moment (§11) |
|---|---|---|---|---|
| **f0** | Desk take mid-gesture, nothing else (v01: hand wave with motion blur, 0–0.15 s) | — | L-desk | — |
| 0.16–0.40 | **Tile 1** (the first item's monogram tile or the creator's logo) grows from 0.3 → 1.0 while rising ≈ 60 px and turning −20° → −10°, 6 f (expo-out), at x ≈ 200, y ≈ 470 | pill hard-swaps on with the first chunk at ≈ 0.20 ("These are five productivity", all grey, darkening word by word) | L-desk | hook: one soft pop as tile 1 lands |
| 0.40–0.65 | **G-1 make-room** (13 f, ease-out: down ≈ 245 px, zoom-out ≈ 0.89×); the **count numeral** snaps on at its word (≈ 0.44) | — | → L-topband | — |
| 0.48–0.80 | **Tiles 2…N** pop into the arc (P-01): 3 f each, 2–3 f stagger, scale 0 → 1.04 → 1.0, rotations ±8–14° | "five productivity" | L-topband | — |
| 0.72 | **Caps title** snaps on beside the numeral (≤ 2 f): the `title_card` is complete by ≈ 0.8 s | — | — | reveal (soft) |
| 1.10–2.40 | **Serif subline** (P-03) types letter by letter under the title, 1 letter/f with a 6 → 0 px blur | "apps that I use every single day" | — | — |
| 2.40–3.00 | Everything holds; the pill carries the first ordinal | "Firstly," | — | — |
| ≈ 3.0 (item 1's tool name −2 f) | Title + subline rocket off the top (8 f, vertical motion blur); tiles 2…N scatter outward and off-frame with ±20° spin (8–10 f); **tile 1 spins and travels to the top centre** (T-07, 10 f) and becomes item 1's tool drop (P-07) (v01 @ 3.08–3.36) | "we have [Tool]," | stays L-topband | list cue (item 1) |

Never skip: the count numeral equals the number of items (H14), and the first item's tile is the one that travels.

### 6.3 Allowed alternates `[DNA list; VAR choice per reel]`

**HA-12 Question → glow headline (default for F-B).** Spoken pattern: a "what would happen if…" question that names the idea.

| t (s) | Visual | Pill (cy 1220) | Layout / camera | Cue |
|---|---|---|---|---|
| f0 | Desk take, the creator leaning in as they ask (v02's face growth is the lean, not a digital push; Z-1 is optional) | — | L-desk | — |
| 0.10 | — | "What would happen" (hard-swapped on) | — | — |
| 0.5–1.5 | Gestures | "if you committed" / "to one thing" | — | — |
| ≤ 1.8 (the idea's noun) | **Hard cut (G-3) to W-navy**: the glow headline (P-04) and its hand subline are both already complete; objects already moving, sliding left → right across the dome with motion blur (P-15) | "to one thing" | L-cutaway | hook: one soft impact or whoosh on the cut |
| 2.2–3.0 | The hero object travels in from the left onto the dome (≈ 12 f) while the first objects drift on to the right | "for the next" / "90 days?" | — | — |
| 3.0–4.0 | Hard cut back to the face on the next sentence (T-01) | next chunk | L-desk | — |

- Niche A example: "What would happen if you studied one subject first every morning?" → glow headline "ONE SUBJECT" / hand "first thing, every day"; objects: a closed notebook and an alarm clock (line icons or the creator's cut-out photos).
- Niche B example: "What if you trained just one lift for 12 weeks?" → glow headline "ONE LIFT" / hand "for the next 12 weeks"; objects: a kettlebell and a calendar page.

**HA-04 Ink-bubble topic (default for F-C).** Spoken pattern: "When we [did X] last [time]…".

| t (s) | Visual | Pill | Layout | Cue |
|---|---|---|---|---|
| f0 | Walk-and-talk (setup B) or desk; the empty ink blob is **already on screen** in the top band | hidden (the bubble spells the words; z8) | L-desk | — |
| 0.17–0.5 | Fragment words fade in on their onsets (3 f each); two sparkles fade in either side with the second word | hidden | — | — |
| 0.5–0.8 | The keyword ("hired") fades in `good` green; the subject's wordmark fades in (3 f) and the blob grows to fit it; the paper outline draws around the blob (14 f) | hidden | — | soft pop |
| 1.0–1.8 | Second fragment ("last month") fades in under the wordmark | hidden | — | — |
| 1.8 | **Hard cut to B-roll (G-6)**; the bubble leaves with the cut; the hero statement (P-06) builds word by word (3 f fades) over darkened B-roll | hidden (z8) | L-broll | — |
| 2.5–2.8 | Marker underline draws under the keyword line (10 f) | — | — | reveal (soft scribble) |
| 3.0–6.0 | Remaining statement lines; cut into chapter 1 | the pill returns | — | — |

- Niche A example: bubble "When I tried" + "TIMEBLOCKING" + "for a month"; statement "I genuinely / *didn't expect* / how much / I'd get done".
- Niche B example: bubble "When we gave" + "HABIT CARDS" + "to 20 clients"; statement "I honestly / *did not know* / if anyone / would use them".

**HA-02 Headline + proof (allowed in F-A and F-C).** Use when the reel opens on a result the creator owns ("I built this study planner in 20 minutes").

| t (s) | Visual | Pill | Layout |
|---|---|---|---|
| f0 | L-topband already set (the stage at t 0 = L-topband with the offset); the **proof window** (P-08: the creator's own screenshot or recording of the result) at x 240–840, y 240–578, accent rim; the `title_card` headline (≤ 5 words, Anton 72 px G-count) at y 140–220 | first chunk on the first word | L-topband |
| 0.3–1.5 | The window's content scrolls or plays; one ink circle (P-27) draws on the key element at its word | chunks | — |
| ≤ 2.5 | Headline + window exit (6 f); the reel continues as F-A or F-C | — | — |

- Niche A: "MY 1-PAGE EXAM PLAN" + the creator's planner screenshot, circle on "Week 3".
- Niche B: "MY 15-MINUTE PREP BOARD" + the creator's own board photo, circle on "Sunday".

### 6.4 Hook pairs by topic `[NICHE]`
Write the pair for each reel at P7 and append it here. The pair type follows the archetype.

| Archetype (pair type) | Topic | First subject (by 1.0 s) | Reveal / payoff (by 1.8 s) | Patterns | Niche |
|---|---|---|---|---|---|
| HA-04 (subject → reveal) | Study apps I use daily | Tiles of the N apps (monograms or the creator's logos) | "5 STUDY APPS" + "that run my week" | P-01 + P-02 + P-03 | A (example) |
| HA-04 | My note-taking system | Tiles: notebook, cards, app | "3 NOTE HABITS" + "I'll never drop" | P-01 + P-02 | A (example) |
| HA-04 | Home-gym gear | Tiles: band, mat, kettlebell (icon tiles) | "4 HOME-GYM BUYS" + "that I use every day" | P-01 + P-02 + P-03 | B (example) |
| HA-12 (thesis → scene) | Deep work blocks | Face + question pill | "ONE BLOCK" + "before you open email" (navy) | P-04 + P-15 | A (example) |
| HA-12 | Protein at breakfast | Face + question pill | "PROTEIN FIRST" + "for 30 days" | P-04 + P-15 | B (example) |
| HA-04 bubble | A month of timeblocking | Bubble "When I tried / TIMEBLOCKING / for a month" | Hero statement over desk B-roll | P-05 + P-06 | A (example) |
| HA-04 bubble | Clients using habit cards | Bubble "When we gave / HABIT CARDS / to 20 clients" | Hero statement over studio B-roll | P-05 + P-06 | B (example) |
| HA-02 (promise → proof) | A planner I built | Headline "MY 1-PAGE EXAM PLAN" | The creator's screenshot + ink circle | P-02 + P-08 + P-27 | A (example) |

### 6.5 Headline writing `[DNA formula; NICHE examples]`
| Element | Formula | Limits | Examples (niche A / B) |
|---|---|---|---|
| Count title (P-02) | `[N] [THING-PLURAL]` in caps | numeral + ≤ 4 words; N = item count | "5 STUDY APPS" / "4 HOME-GYM BUYS" |
| Serif subline (P-03) | `that I [verb] [frequency/context]` or `[for/to] [outcome]` | ≤ 7 words, sentence case, no full stop | "that run my whole week" / "that I use every single day" |
| Glow headline (P-04) | `[THE IDEA IN 1–3 WORDS]` caps | ≤ 3 words, ≤ 2 lines | "ONE SUBJECT" / "PROTEIN FIRST" |
| Hand subline | `[for / in / before] [time frame or condition]` | ≤ 6 words, lower case | "for the next 90 days" / "before you open email" |
| Ink bubble (P-05) | `[fragment ≤ 3 words]` + `[SUBJECT]` + `[fragment ≤ 3 words]` | wordmark 1–2 words | "When we tried / FOCUS FRIDAYS / last term" |

Rules: numerals not words ("5", not "five"); no emoji in headlines; no hype words ("insane", "secret", "game-changer"); the headline names a thing the reel then shows. **Write 3 and pick by ST-4 and ST-6.**

### 6.6 Hook sound
See §11: the hook may carry ≤ 3 cues (tile landing, title reveal, the cut to the glow headline); the music bed enters after the hook.

### 6.7 CTA `[DNA device set; VAR values]`
| Device | Spoken pattern (optional, last sentence) | On screen | Hold | Where |
|---|---|---|---|---|
| `post_only` (default) | A question to the viewer: "What's one [thing] you use every day? I'd love to know." | Nothing new: L-desk, the pill, the face (P-35). No card, no keyword | Face ≥ 1.5 s from the CTA's first word to the hard end | end |
| `link_bio` | "The [deliverable] is linked in my bio." | Nothing new (P-35) | ≥ 1.5 s | end |

- **This copy's CTA:** {{BV-08.device|link in bio}}.
- **Post title / caption formula:** `[headline restated in sentence case] — [CTA]`, where the CTA is the line above, or "comment {{BV-08.keyword|KEYWORD}}" when the buyer uses a comment keyword. By default the keyword lives only in the post caption, never on screen (do not set `meta.keyword` in the timeline). **On-screen keyword option (off by default):** when the buyer sets `profile.cta.on_screen_keyword: true` with `comment_keyword`, the keyword appears once as the hand subline style (Caveat 600 58 px paper, `COMMENT "{{BV-08.keyword|KEYWORD}}"`) under the face for ≥ 1.5 s from the spoken keyword, scene `kind: "cta-keyword"`; nothing else changes (no end card). Tool names set in their type voices (P-07) are part of the style and stay.
- No SFX in the 1.0 s before the CTA's first word; nothing enters after it; hard end ≤ 6 f after the last word.

---

## §7 Structure & cadence `[REQ] [DNA]`

### 7.1 Structure type per format
| Format | Type | Arc and typical lengths |
|---|---|---|
| F-A | `list` | HOOK 2.5–3.5 s → ITEM-1…ITEM-N (N = 3–7, 6–10 s each; the last item 8–12 s) → OUT 2–5 s |
| F-B | `explainer` | HOOK 3–4 s → PROBLEM 5–10 s (list rows of the many things) → CONCEPT 6–12 s (glow / books / quote) → EXAMPLES 8–15 s (row pick, person, stat) → QUESTION 4–6 s (question card) → TACTIC 6–10 s (calendar or checklist) → OUT 2–4 s |
| F-C | `story` | HOOK 4–6 s (bubble + hero statement) → CHAPTER-1…CHAPTER-K (K = 2–4, 12–25 s each) → TURN 6–12 s (the result: file card / stat with ink) → OUT 3–6 s (face, reflection) |

Beat `section` names are exactly these (`HOOK`, `ITEM-1`, `PROBLEM`, `CHAPTER-2`, `OUT`…): V-PROMISE counts `ITEM-n` sections.

### 7.2 Markers
- **SM-1 Tool drop as marker (F-A).** Numbering is spoken only ("First", "Next up", "Third", "And finally"); no numerals on screen after the hook. Each item opens with its P-07 tool drop on the item's name; that drop is the marker.
- **SM-2 Chapter bubble (F-C).** Each chapter after the first opens with a P-05 ink bubble ("then came / [SUBJECT]", "a week with / [PERSON]"), 1.5–2.5 s, scene `rehook: true`.
- **F-B: `markers: none` (spoken only).** Sections are carried by world changes (face ↔ navy ↔ paper).

### 7.3 Unit ritual (frames at 30 fps; t = the item noun's onset)
**F-A item:**
| When | What |
|---|---|
| t − 12 f | Ordinal word on the pill; face on L-desk |
| t − 6 f | G-1 make-room starts (13 f) unless already in L-topband |
| t − 2 f | **P-07 tool drop**: when the previous insert is still up, the name pushes in from the right (T-11, 8 f) as the old insert pushes out left; otherwise the tile pops (3–4 f). The logo tile lands beside the name 2–4 f after it (v01 @ 9.60–9.84) |
| t + 1.5–2.5 s | On the next noun ("workspace", "dashboard", "inbox") the drop **rockets up off the top** (3–4 f, vertical motion blur) while the **P-08 screen window slides in from the right** (9 f, expo-out) in the same frames (v01 @ 20.28–20.60), or its created substitute P-09 / P-10 / P-21 |
| t + 2.5–7 s | The window holds with 1–2 internal events (scroll, screen swap, an ink circle on the feature named); jump cuts in the take run under it untouched |
| Next item named | T-11 push: the window slides out left, the next tool name slides in from the right — stay in L-topband |
| Opinion line | The window slides out left (8 f, expo-out with a slow tail) **while** G-2 settle-back runs (12 f) → face ≥ 1.5 s on L-desk; a Z-2 reframe on a jump cut is allowed |

**F-B concept beat:** face line on L-desk → on the noun, G-3 hard cut to the cutaway; the pattern builds over 0.3–1.5 s (one row / one book / one object per spoken item) → holds while the sentence runs (2.5–6.5 s, the max absence) → back to the face by T-01 on the next sentence start.

**F-C chapter:** P-05 chapter bubble (1.5–2.5 s, re-hook) → B-roll beats (G-6, 2.5–6 s clips) with one P-24 card over B-roll per ≈ 10 s → a pastel UI run (G-3 on W-pastel: P-21 thread, P-22 file card; 6–12 s) with one ink circle on the key number → a person beat with a P-30 name tag → back to the face (L-desk, or L-topband with one card) for the reflection.

### 7.4 Open loops and re-hooks
- **Count loop (F-A):** the title numeral is paid off item by item; "And finally" introduces the last item with the richest insert (P-10 sequence or P-08 + ink).
- **Question loop (F-B):** the question card (P-18, kind `question-card`, which also counts as a re-hook) is answered by the tactic within 10 s.
- **Story loop (F-C):** the hero statement's doubt ("I didn't know if…") is answered in TURN. Re-hook every ≤ 45 s (`structure.rehook_every_s`): one chapter bubble between 40% and 55% of the runtime, plus a second one when the reel runs past 85 s.
- **Intro cap:** HOOK ≤ 15% of runtime (F-A ≤ 3.5 s in a 45 s reel; F-C ≤ 6 s in a 60 s reel).
- Every promise is paid on screen: a count, a question, a story doubt.

### 7.5 Rhythm and energy curve
Even and warm: information beats every 1–2 s, no comedy beats. The last item or chapter gets the richest visual (a screen sequence, the row pick, the stat with ink), never a louder effect. The end is quiet: the face, the pill, a question or a thought, then a hard end (P-35).

### 7.6 Cadence (weighted state changes)
| Token | F-A | F-B | F-C | Evidence |
|---|---|---|---|---|
| `sc_per_10s` (pill swaps × 0.5 included) | 5–10 | 5–11 | 5–10 | change points measured at full rate (scene score ≥ 0.06 v01 / ≥ 0.2 v02, v03): 2.8 / 2.9 / 1.6 per 10 s, plus insert-internal events and ~8–10 pill swaps per 10 s at 0.5 |
| `hook_sc_3s` | 6 | 6 | 6 | v01 0–3 s: 5 tile pops, numeral, title, subline, 3 pill swaps |
| `hook_max_gap_s` | 1.0 | 1.0 | 1.0 | — |
| `max_gap_s` (weight ≥ 1) | 4.0 | 3.5 | 4.0 | v01 0:26–0:31 face-only 5 s, v03 1:19–1:25 6 s: tightened to 4.0 |
| `max_static_s` | 2.5 | 2.5 | 2.5 | live footage, B-roll and drifting windows count as motion |
| `caption_weight` | 0.5 | 0.5 | 0.5 | support captions |
| `cuts_per_min` | — | — | — | not DNA (detector: 0 / 17.5 / 4.9). Shot / scene length measured: v02 median 2.5 s, p90 5.9 s; v03 median 3.3 s, p90 15.7 s (UI runs); v01 overlay change every 2.5–5.5 s on one take; longest stretch without a scene change: v03 66.9–86.5 s (face + cards) |

How to fill a face-only stretch longer than 4.0 s: a Z-2 reframe on a jump cut, or a small top-band insert for the next noun — never a decorative element.

---

## §8 Visual system `[REQ]`

### 8.1 Graphics role and budget
- **Role:** primary in F-A and F-C, support in F-B (SW-05).
- **Insert share of runtime:** F-A 55–85% (top band), F-B 30–55% (cutaways), F-C 50–80% (B-roll cards + pastel UI).
- **Families per 60 s:** ≥ 4. **Patterns per 60 s:** ≥ 6 distinct.
- **Numbers become pictures** only when the script gives a number: a stat card (P-37) or an ink circle on the number inside the UI that shows it. Never a chart without numbers from the script.

### 8.2 Families
| ID | Family | Source class | What the buyer supplies |
|---|---|---|---|
| B-1 | Tool drop (tile + name) | creator-supplied logo, else engine (name in type) | Optional: a logo PNG/SVG per tool they may show |
| B-2 | Screen window | buyer-owned (screenshot / screen recording), else engine recreated UI | A screenshot or 4–8 s recording per tool/site/document named |
| B-3 | Recreated UI (chat, prompt box, calendar, checklist, file card) | engine | Nothing; optional screenshots of their own tools |
| B-4 | Titles (count title, glow headline, ink bubble, hero statement, question card) | engine | Nothing |
| B-5 | List rows | engine | Nothing |
| B-6 | Objects and covers (object dome, book float) | buyer-owned cut-out photos, else engine (created covers, line icons) | Optional: cover photos, product cut-outs |
| B-7 | Ink layer (circles, underlines, arrows, name tags, sparkles) | engine | Nothing |
| B-8 | People | creator-supplied photo/clip (cut-out), else engine silhouette | Optional: a photo or clip of each person named |
| B-9 | B-roll | buyer-owned | F-C: 6–12 clips per 60 s of their own work/life |
| B-10 | Links and diagrams (dashed link, two-plate compare, hub dots) | engine | Nothing |

### 8.3 Pattern specs
Engine building blocks: `VEOS.scene` (bespoke), `VEOS.fx.logoPlate`, `fx.appUI`, `fx.quoteCard`, `fx.silhouette`, `fx.shot`, `fx.clip`, `fx.card`, `fx.icon`, `fx.typewriter`, `fx.typeStack`, the stage layouts and the camera presets (SCENES-API). Every scene that carries text sets `text_class`; every third-party moment carries `insert` (§12.5).

**Hook and titles (B-4, B-1)**
| ID | Pattern | Type | On screen | Motion (30 fps) | When | Family / class | Engine | Needs |
|---|---|---|---|---|---|---|---|---|
| **P-01** | **Tile arc** | overlay | 3–7 white tiles 128 px (measured 120–135 px, v01 @0:03), radius 26, shadow `0 10 24 rgba(0,0,0,.28)`, each with a monogram (Poppins 800 54 px ink, TC-decorative) or the creator's logo, on an arc centred x 540, y 380–700 (the outer tiles sit lowest, v01 @0:03), rotations alternating ±8–14° | tile 1 grows 0.3 → 1.0 while rising ≈ 60 px, 6 f; the others pop 0 → 1.04 → 1.0 in 3 f, 2–3 f stagger; idle bob ±3 px at 0.5 Hz (seeded phase); exit: scatter outward off-frame with ±20° spin, 8–10 f (tile 1 travels instead, T-07) | F-A hook: the items of the count | B-1 / TC-decorative | bespoke `VEOS.scene`, `kind: "tile"`, z5, one scene for all tiles, `events` per pop | a tile per item |
| **P-02** | **Count title** | overlay | Numeral Anton 150 px + caps title Anton 88 px, G-count gradient text, shadow; centred group, y 150–310 | numeral snaps on (≤ 2 f) on the count word; title snaps on (≤ 2 f) on its word; exit `rocket` off the top (8 f, vertical motion blur) | F-A hook | B-4 / TC-display | bespoke, `kind: "title_card"`, z6 | numeral = item count |
| **P-03** | **Serif subline** | overlay | Instrument Serif italic 50 px `cream`, y 330–390, centred, ≤ 7 words | letters appear 1/f, each blur 6 → 0 px over 5 f; exits with P-02 | Under P-02 | B-4 / TC-label | bespoke or `fx.typewriter`, z6 | — |
| **P-04** | **Glow headline** | overlay | W-navy cutaway: Anton 190 px `primary` with a 22 px same-hue glow, centred cy 420; hand subline Caveat 600 58 px paper at y 600–660 | arrives complete and lit on the cut (headline + subline); static while held (glow breathing optional, ≤ ±4 px over 2 s) | F-B hook (≤ 1 per reel) | B-4 / TC-display | bespoke, `kind: "title_card"`, z6, `payoff: true` | `primary` role |
| **P-05** | **Ink bubble label** | overlay | Black organic blob (ink 92%, w 600–720, h 220–280) in the top band; serif fragment 46 px paper, wordmark Lilita One 96 px paper, second fragment; 2 gold sparkles; paper outline 3 px offset 10 px | blob already on at its start (no scale-in); fragment words fade 3 f on onsets; sparkles fade 3 f; wordmark fades 3 f while the blob grows to fit (3 f); outline draws 14 f; exits with the next hard cut | F-C hook (kind `title_card`), F-C chapter starts (`rehook: true`) | B-4 / TC-display + TC-label | bespoke, z8 (hides the pill) | — |
| **P-06** | **Hero statement** | overlay | 3–5 lines left-aligned at x 110 from y 300: plain lines Poppins 400 88 px paper; keyword lines EB Garamond 700 italic 92 px `concept`; a 0 → 35% black gradient over the left 70% of the B-roll | each word fades in over 3 f on its own onset, in place (no slide; v03 @ 1.97–2.43); marker underline under the main keyword line 10 f after it lands | F-C hook; one strong claim over B-roll | B-4 / TC-display | `fx.typeStack` (sans/serif styles mapped to `body`/`kinetic`) or bespoke, z8 | B-roll or footage under it |

**Top band: tools and screens (B-1, B-2, B-3, B-10)**
| ID | Pattern | Type | On screen | Motion (30 fps) | When | Family / class | Engine | Needs |
|---|---|---|---|---|---|---|---|---|
| **P-07** | **Tool drop** | overlay | Tile 132 px (monogram or the creator's logo) + the name 80–96 px paper in its **type voice** (§5.4), group centred on x 540, cy 266; accent bar 8 px under the name | enters by T-11 push from the right (`in: "slide-r"`, `in_frames: 8`, `smear: true`, expo-out) when it replaces an insert, else the tile pops (3–4 f) or arrives from P-01; the logo tile lands 2–4 f after the name; bar grows 12 f; exit `rocket` up off the top (`out_frames: 4`: 3–4 f of travel, vertical motion blur) as the window slides in, or `slide-l` (`out_frames: 8`, `smear: true`) when the next tool replaces it | Every tool / app / site / product named (the F-A marker) | B-1 / TC-display | bespoke `VEOS.scene` (z5, `insert`), or `fx.logoPlate({theme: "light"})` when a larger plate reads better | insert record (logo_plate) |
| **P-08** | **Screen window** | overlay | The creator's screenshot or recording in a rounded rect r 22 at x 160–920, y 132–560 (16:9), 3 px rim in the rotating rim tint (accent → violet → data) + an outer glow 18 px at 45% | slides in from the right edge (`in: "slide-r"`, `in_frames: 9`, `smear: true`: the preset's blur becomes a horizontal smear along its travel, expo-out) in the same frames as the tool drop leaves; a recording plays at 1.0×; a screenshot pushes 1.00 → 1.05 or scrolls top → bottom over the hold; exit slides out left (`out: "slide-l"`, `out_frames: 8`, `smear: true`, expo-out with a slow 4–6 f tail at the edge) (v01 @ 20.28, 26.66) | The tool's workspace / result / page is described | B-2 / content TC-decorative | `fx.shot({asset, chrome: false, push: [1, 1.05]})` or `fx.clip({asset, x, y, w, h, radius: 22})`, z4 | creator file (else P-09/P-10/P-21) |
| **P-09** | **Prompt box** | overlay | Greeting line Instrument Serif 54 px paper with a small sparkle icon (y 150–220); input box 760 × 170, r 24, 2 px `warm` border on 12% white, the typed question Poppins 500 40 px paper, caret| greeting fades 6 f; box rises 10 f; the question types at 30 characters/s (`fx.typewriter`); caret blinks every 15 f | An AI assistant or search being asked something | B-3 / TC-label | bespoke, or `fx.appUI({kind: "chat"})`, z4, `insert` (recreated_ui) | the question's exact words |
| **P-10** | **Screen sequence** | overlay | P-08's window whose content swaps 2–3 screens (the creator's recording segments or screenshots) | each swap slides 100% left in 10 f (inOut) = one event | A flow described in steps ("pick a habit → set a goal → get a reminder") | B-2 | `fx.shot` per screen inside one bespoke frame scene, z4 | creator files (else 2–3 `fx.appUI` screens) |
| **P-11** | **Dashed link** | overlay | Two tool plates (tile + name, 64 px names) at x 160–480 and x 600–920, cy 250; a dashed arc above them (accent, 5 px, dash 18/14) | plate 2 pops when named (8 f); the arc draws over 12 f, then its dashes flow 2 px/f while held | "X syncs with / connects to / pulls from Y" | B-10 / TC-display | bespoke, z5, `insert` per plate | two insert records |
| **P-12** | **Two-plate compare** | overlay | Two plates side by side (as P-11 without the arc) and a 2 px paper divider; the winner gets a P-27 ink circle or a `good` tick 56 px | plates pop 8 f each on their names; the circle/tick lands on the verdict word | "X vs Y", "I switched from X to Y" | B-10 + B-7 | bespoke, z5 | two insert records |

**Cutaway concepts (B-4, B-5, B-6, B-8)**
| ID | Pattern | Type | On screen | Motion (30 fps) | When | Family / class | Engine | Needs |
|---|---|---|---|---|---|---|---|---|
| **P-13** | **List rows** | overlay | W-navy: ≤ 6 white rows 820 × 136, r 28, x 130–950, pitch 162 from y 190 (F-B ends ≤ 1112, above the pill at 1220); a left tab 120 px in `warm` / `rose`; emoji 56 px + label Poppins 700 58 px ink | each new row **wipes open left → right** (its width grows 0 → 100%, ≈ 12 f, label clipped as it opens) on its spoken item; when the stack must make room it steps up in 2–3 discrete 1-frame jumps (≈ 50 px each; on the jump frame the stack carries `filter:${ctx.blur(8, 90)}`, a vertical smear) rather than a smooth scroll (v02 @ 15.88–16.32). A 50 px one-frame jump is inside G3's 90 px per-frame limit, so no exception or declared event is needed | Listing the many things (goals, tasks, habits, meals) | B-5 / TC-label | bespoke, z4, one scene, `events` per row | — |
| **P-14** | **Row pick** | state | The P-13 stack: the picked row's fill turns `good`, its edge glows `primary` 3 px, scale 1.04; the others fade to 55% with grey tabs | on the decision word: the stack steps up once (1 f), the picked row scales 1.04 and gains a white glow rim, its left fill grows across the row while the other rows' fills retract to thin tabs (≈ 15 f) (v02 @ 27.83–28.17) | "Pick one", "the one that matters" | B-5 | an event of the P-13 scene | — |
| **P-15** | **Object dome** | overlay | W-navy: a pale dome (ellipse #E9ECEF → #C9CED6, centre x 540, y 1900, rx 760, ry 520); 1–3 objects (the creator's cut-out photos, else `fx.icon` 220 px paper line icons) float at y 700–1160 | objects are already moving on the cut, sliding left → right across the dome with tumble and motion blur (≈ 25 px/f); the hero object enters from the left (≈ 12 f) as they drift on (v02 @ 1.77–2.37) | Under P-04 | B-6 | bespoke, z3 | cut-outs optional |
| **P-16** | **Book float** | overlay | W-navy: 1–3 covers 300 × 450, rotateY 18°, rotateZ −8°, shadow `0 30 60 rgba(0,0,0,.5)`; the creator's cover photo, else a created cover: flat `warm` / `rose` / paper fill, title Instrument Serif 52 px ink, author Poppins 600 40 px | each cover drifts in from below (14 f) on its title; idle drift ±10 px | A book, course or paper is named | B-6 / TC-label | bespoke, z4, `insert` | creator photo or created cover |
| **P-17** | **Person card** | overlay | W-navy: the person (a cut-out from the creator's clip/photo, 600–800 px tall, bottom-anchored at y 1160) + a P-30 name tag beside the head; else `fx.silhouette({name, role})` | the cut-out rises 40 px + fades 10 f; the name tag writes on after 6 f | An author, expert or team member is named | B-8 / TC-label | `fx.shot` with a matte asset, or `fx.silhouette`, z4, `insert` | creator photo/clip (else silhouette) |
| **P-18** | **Question card** | overlay | W-paper (or W-navy): a white card 760 wide at x 160, y 640–1180, r 40, shadow; a 96 px emoji sticker tab on its top-left corner tilted −8°; text Poppins 600 54 px ink, centred, ≤ 22 words | the card **grows from a point** anchored at its top-left corner after the G-4 cut, its box expanding in steps to fit the text as it types (≈ 25 f to the first line); letters type 1–2 / f with wide tracking that settles to normal; the tab pops 6 f once the box is full size (v02 @ 43.50–44.38) | A question to the viewer or to oneself | B-4 / TC-label | **Build (any length, ≤ 22 words):** `fx.card({x: 160, y: 640, w: 760, h: 150, theme: "light", radius: 40, titleFont: "body", titleWeight: 600, titleTracking: 0.04, titleSize: 54, title, grow: "fit-text", typeAt: 0, cps: 45, minW: 140, in: "none", z: 8, kind: "question-card"})` (Poppins 600 with the measured open tracking; the box grows from its left edge with the typed title, and a question wider than 760 px wraps by words and the card grows taller line by line, as in v02; 45 cps = the measured 1–2 letters / f) + a z8 tab scene popping 6 f when `typeAt + title.length / 45` is reached. `kind: "question-card"` (counts as a re-hook) | — |
| **P-19** | **Calendar day** | overlay | W-paper: a generic day view 900 × 1300 at x 90, y 180, tilted rotateZ −2°; hour rail Poppins 500 30 px #8A8A8A (TC-decorative); blocks 760 wide: the focus block `data` with a Poppins 600 44 px paper label, others `warm` / grey #E4E4E4 / #3A3340 with labels | blocks drop in (8 f each) on their words; the whole view drifts 1.00 → 1.03 | Scheduling, time-blocking, routines | B-3 / TC-label | bespoke, z4 | label words from the script |
| **P-20** | **Checklist card** | overlay | A white card 820 × (100 + 110 per row) on W-paper or W-navy; rows: a 44 px box + a Poppins 600 52 px label; a `good` tick draws in the box on each completed step | rows fade in 6 f each; ticks draw 8 f on their words | Steps, a routine, a setup list | B-3 / TC-label | bespoke, or `fx.appUI({kind: "list"})`, z4 | — |

**UI story and B-roll (B-3, B-9)**
| ID | Pattern | Type | On screen | Motion (30 fps) | When | Family / class | Engine | Needs |
|---|---|---|---|---|---|---|---|---|
| **P-21** | **Chat thread** | overlay | W-pastel (or over B-roll in the top band): white message cards 900 wide at x 90, r 28, shadow `0 10 30 rgba(0,0,0,.12)`; avatar 72 px (initials, decorative), name Poppins 700 40 px, time 26 px (decorative), body Poppins 500 40 px ink, mentions and links in `data`, an attachment chip (`rose`, 30 px decorative name + a 40 px label when it matters) | each new card slides up 40 px + fades (8 f) on its words; a reply types at 30 characters/s; when the stack passes y 1200 it scrolls up one card (12 f, inOut); ≤ 3 cards visible | Messages, asking someone/something to do a task, a team update | B-3 / TC-label | `fx.appUI({kind: "chat", theme: "light", size: 40})` or bespoke, z4, `insert` (recreated_ui) | the exact words |
| **P-22** | **File card** | overlay | A 620 × 380 card: a header band (`warm` → `rose` gradient, or `violet`) with a title Poppins 700 44 px and a small illustrative bar group (no axis numbers; a % or number only if spoken, Poppins 700 44 px); a file-name chip 26 px (decorative) | rises 10 f; bars grow 14 f | A report, deliverable, summary or document produced | B-3 / TC-label | bespoke or `fx.card`, z4, `insert` | spoken number only |
| **P-23** | **Hub dots** | overlay | A 160 px tile (`violet`, monogram or the creator's logo) at the centre of the band with 12 coloured dots (accent, data, primary, good) gathering from a ring of r 360 to r 200 | dots gather over 24 f (seeded angles); thin lines pulse 0 → 40% at 0.8 Hz | "It connects to all our tools", "everything in one place" | B-10 | bespoke, z4 | — |
| **P-24** | **Card over B-roll** | overlay | One P-21 / P-22 / P-08 card pinned in the top band (y 140–600) while the B-roll plays full-bleed under it | as its pattern; the B-roll continues | F-C: a UI moment while life footage carries the voice | B-3 + B-9 | the card scene z4 over the z1 `fx.clip` | creator B-roll |
| **P-25** | **Frosted pages** | overlay | L-frost (or a z1 B-roll clip with a dim): 2–3 white page cards 480 × 680 sliding in horizontally; page title Poppins 600 40 px + decorative lines | each page slides from x +600 to its slot in 10 f on its noun; the row drifts −40 px over the hold | Documents, slides, posts or pages produced | B-3 | bespoke, z4 | spoken titles only |
| **P-26** | **B-roll beat** | footage-treatment | The creator's own clip full-bleed | `fx.clip({kenburns: [1.0, 1.06]})`, 2.5–6 s per clip; hard cuts on clause boundaries | F-C sentences told over life footage | B-9 | `fx.clip` at z1, `parallax: false` | creator B-roll (SH-4) |

**Ink layer (B-7; §22)**
| ID | Pattern | Type | On screen | Motion (30 fps) | When | Family / class | Engine | Needs |
|---|---|---|---|---|---|---|---|---|
| **P-27** | **Ink circle** | annotation | A hand-drawn ellipse round the target rect + 14–22 px pad, 7 px `marker`, round caps, tilt ±6°, seeded wobble 1.5 px | stroke-dashoffset draw over 9 f from 200°, overshooting the start by 15°; holds until the target exits | A number, a field, a feature or a word on a card is named | B-7 | SVG inside the target's scene, or its own z6 scene with `overlaps: [target]` | target rect (anchor pass) |
| **P-28** | **Scribble underline** | annotation | A 2-wave line (amplitude 6 px) 10 px under the phrase, 7 px `marker` | draws L → R over 10 f | The key phrase of a hero statement, a card line, a book title | B-7 | SVG in the target scene | target rect |
| **P-29** | **Ink arrow** | annotation | A curved shaft (7 px `marker`) + a 2-stroke head pointing at the target from 80–140 px away | shaft 6 f, then head 2 f | "This one", "right here" on a UI element | B-7 | SVG, z6, `overlaps: [target]` | target rect |
| **P-30** | **Name tag** | annotation | The name in Caveat 600 60 px paper (shadow `0 2 8 rgba(0,0,0,.5)`) beside the person's head, ≥ 40 px from the face box, with a 4 px paper curl flourish | the name wipes on L → R in 10 f; the flourish draws in 12 f | A person appears in B-roll or a person card | B-7 / TC-label | bespoke z6 | the person's position (static ± 30 px) |
| **P-31** | **Sparkles** | annotation | 2–4 four-point stars 28–40 px in `concept` | pop 0 → 1.2 → 1 (6 f); twinkle ±10% at 0.8 Hz | Either side of a wordmark (P-05) or a "new" product | B-7 | inside the host scene | — |

**Camera, quotes, ending, brand**
| ID | Pattern | Type | On screen | Motion (30 fps) | When | Family / class | Engine | Needs |
|---|---|---|---|---|---|---|---|---|
| **P-32** | **Hook push** | footage-treatment | The face slowly enlarging | Z-1 push-drift 1.00 → 1.10–1.12 over the first sentence (1.5–2 s) | Optional (not measured in the evidence): a reflective line | — | `camera: push-drift` | ≥ 1080 px source |
| **P-33** | **Reframe on cut** | cut | A tighter (1.12) or wider (1.00) crop of the same take | Z-2 snap-punch over 2 f exactly on a cutmap jump cut; Z-3 pull-out back over 10 f at a later cut | 2–4 per minute on face-only stretches | — | `camera: snap-punch` / `pull-out` | ≥ 1080 px (1.12×) |
| **P-34** | **Quote card** | overlay | A light quote card: the quote verbatim Poppins 600 54 px, the name, one highlighted phrase in `concept` | `fx.quoteCard` reveal word by word | A person's or a book's words are quoted | B-4 / TC-label | `fx.quoteCard({theme: "light", highlight, hlRole: "concept"})`, z4, `insert` (quote_card), on L-frost or W-navy | verbatim quote (NC-13) |
| **P-35** | **Quiet out** | footage-treatment | The face on L-desk, the pill, nothing else | — | The last 1.5–4 s (the CTA or the last thought) | — | stage L-desk | — |
| **P-36** | **Sponsor / product plate** | overlay | A P-07 tool drop with the brand's own logo (creator-supplied) or its name in type, plus "Paid partnership" TC-legal 24 px under it for the whole segment | as P-07; the disclosure fades in with the plate | A paid, affiliate or own-product segment (§25) | B-1 / TC-display + TC-legal | bespoke or `fx.logoPlate`, z5, `insert`, `sponsor` | disclosure if paid |
| **P-37** | **Stat card** | overlay | A white card 520 wide: the spoken number Anton 140 px ink + its label Poppins 600 44 px; a P-27 circle on the number on its word | the card rises 10 f; the circle draws 9 f on the number word | One number the script says (price, hours, %, count) | B-4 / TC-display | bespoke, z4 (top band or cutaway) | the number is spoken |

Pattern count: 37 (P-01…P-37).

### 8.4 Line → pattern lookup `[NICHE]`
Classify every sentence with this table at P5. Niche A = study & productivity tools; niche B = home fitness & nutrition (both `[NICHE: example]`; append the buyer's own rows per reel).

| Line type | Primary | Alternates | Niche A example | Niche B example | Created substitute when no creator file |
|---|---|---|---|---|---|
| Count promise ("These are 5 …") | P-01 + P-02 + P-03 | HA-02 | "5 apps that run my study week" | "4 home-gym buys I use daily" | monogram tiles |
| A tool / app / product named | P-07 | P-36 if paid | a flashcard app | a resistance-band brand | the name in type (logo plate) |
| What the tool looks like / does | P-08 | P-10, P-09, P-21 | the deck view | the timer app's screen | P-09 / P-21 / P-20 recreated UI |
| A flow inside a tool ("you pick… then…") | P-10 | P-20 | "make a deck → review → see stats" | "pick a plan → log a set → see the week" | 2–3 `fx.appUI` screens |
| Two tools connected | P-11 | P-23 | "it pulls my highlights from my reader" | "it syncs with my watch" | plates in type |
| X vs Y / switched from X to Y | P-12 | P-14 | "I moved from paper to an app" | "dumbbells vs a band" | plates in type |
| Asking an AI or a search something | P-09 | P-21 | "I ask it to quiz me" | "I ask it for a 20 g protein breakfast" | P-09 |
| A list of many things (goals, chores, foods) | P-13 | P-20 | "exams, project, club, job, sleep" | "cardio, mobility, strength, diet, sleep" | — |
| Choosing one of them | P-14 | P-27 on a row | "this term: just the project" | "this block: just strength" | — |
| The big idea / principle | P-04 + P-15 (≤ 1 per reel) | P-06 | "one subject first" | "protein first" | icons for objects |
| A book / course / paper | P-16 | P-34 | a study-skills book | a nutrition book | created cover |
| A person (author, coach, teammate) | P-17 + P-30 | P-34 | a professor | a client by first name | silhouette + name tag |
| A quote | P-34 | P-18 | a line from the book | a coach's line | quote card (verbatim) |
| A question to the viewer | P-18 | P-34 | "what's the one subject that would change your term?" | "what's the one habit you'd keep?" | — |
| Scheduling / routine / time blocks | P-19 | P-20 | "9–11 is the one thing" | "6:30 am mobility" | recreated generic calendar |
| Steps / a setup | P-20 | P-10 | "3 steps to set it up" | "warm-up in 3 moves" | — |
| A message / team update / request | P-21 | P-24 | "I messaged my study group" | "my client texted me" | recreated chat |
| A report / document / output | P-22 | P-25 | "it made a revision summary" | "it made a weekly plan PDF" | created file card |
| One number said aloud | P-37 | P-27 on the UI | "I saved 6 hours a week" | "4 kg in 10 weeks" | — |
| "It connects everything" | P-23 | P-11 | "notes, tasks and calendar in one" | "workouts, meals and sleep in one" | — |
| A strong claim / turning point (F-C) | P-06 | P-04 | "I didn't think I'd stick with it" | "I didn't know if clients would use it" | — |
| A story moment with people/places (F-C) | P-26 + P-30 | P-24 | the study group at the library | clients in the studio | FB-4 (no B-roll: F-B worlds) |
| Opinion / aside / "I love it because" | L-desk face (G-2), P-33 | P-32 | — | — | — |
| The last thought / CTA | P-35 | — | — | — | — |

### 8.5 Data and truth rules
- No `data_figures` module: numbers appear only as words the script says (P-37, chat bodies, file cards), written exactly as spoken (§5.5).
- No charts with axes or values unless every value is spoken; a file card's mini bars are illustrative and carry no numbers.
- Recreated UIs are generic (H13); a created card quotes only the script.
- Personal data in a creator screenshot is blurred for its whole time on screen (NC-14).

### 8.6 Comedy layer
OFF (tone.comedy = off). A buyer may raise it to `light` (VAR): then one emoji sticker tab (as on P-18) may sit on a P-07/P-08 corner, ≤ 1 per 15 s, never on the face; no meme sounds.

### 8.7 Asset rules
- **Real captures first:** the creator's screenshots and recordings of the tools they name, their logos (only ones they may show), their B-roll, their photos.
- **Created substitutes are generic:** no real product's logo glyph, colour scheme or layout (a chat UI is white cards with initials avatars, not a look-alike of a known chat app);.
- **No stock:** no stock B-roll, no stock 3D renders; objects are the creator's cut-out photos or `fx.icon` line icons.
- **Logos:** never fetched, never redrawn; the name set in a type voice is the default.
- **Third-party moments:** the ask-then-create flow (§12.5).

### 8.8 Density and variety
- An insert or card event every 1–3 s while inserts are up; a face-only stretch ≤ 4.0 s without a state change (§7.6).
- ≥ 6 distinct patterns per 60 s; the same pattern ≤ 3 times in a row, except the F-A item ritual (P-07 → P-08 per item).
- Type voices (P-07): never the same voice on two consecutive tools when there are ≥ 3 tools.
- Rim tints (P-08): rotate accent → violet → data; never the same tint on consecutive windows.

---

## §9 Transitions & shot grammar `[REQ] [DNA]`

### 9.1 Library
| ID | Transition | Frames | Recipe | Cue role (§11) |
|---|---|---|---|---|
| **T-01** | Hard cut | 0 | On a word boundary ±1 f; face ↔ cutaway, B-roll ↔ B-roll, B-roll ↔ pastel UI | silent, or one soft whoosh on the first cut into a cutaway |
| **T-02** | Blur-out, then cut (G-4) | 6 + 0 | The pill hides; the face blurs 0 → 20 px and darkens ≈ 15% over 6 f; hard cut to the cutaway, whose card grows from a point. Built-in: the `timeline.grades` event of G-4 (`grade: {brightness: 0.85}`, `blur: 20`, `fade: 0.2`, t = cut − 0.2 to cut + 0.2) + a `timeline.transitions` marker on the cut | silent |
| **T-03** | Make-room (G-1) | 10 | `low` morph down by the offset (§3.3); the insert's entry starts on f4 | the insert's landing may carry a soft pop |
| **T-04** | Settle-back (G-2) | 10 | `low` → `full` morph, starting the frame the insert's exit ends | silent |
| **T-05** | Insert out | 3–8 | A tool drop rockets up off the top (vertical motion blur) as the window enters; a window slides out left (8 f + slow tail); for a chat stack, the top card swipes up 120 px (12 f) as the next card rises | silent |
| **T-06** | Stack step | 1 | A card stack or list jumps up ≈ 50 px in a single frame (2–3 jumps per new row), a vertical smear `ctx.blur(8, 90)` on the jump frame (within G3's 90 px / frame) — the "flash pairs" the cut detector logged (v02 @ 15.93/16.07, 27.83) are these steps, not white flashes. No white flash frames in this style | silent |
| **T-07** | Tile hand-off | 10 | The hook's tile 1 spins and travels (x, y, scale 128 → 132 px) from the arc to the tool-drop slot while the title rockets off the top and the other tiles scatter outward | list cue |
| **T-08** | Frost (G-5) | 8 | `dim` treatment in; the card rises over it from f3 | silent |
| **T-09** | Hard end | 0 | ≤ 6 f after the last word; no black tail, no outro card | silent |
| **T-10** | Curtain wipe | 15 | The incoming B-roll slides down from the top as a full-width panel over the pastel UI, its bottom edge travelling y 0 → 1920 with ease-out (half the distance in the first 6 f); the incoming clip is already pushing in (v03 @ 21.9–22.45; same 0.2 s detector signature at 42.3, 47.9, 50.3, 66.9). Built-in: `{"t": cut, "type": "curtain", "dir": "down", "slide": true, "frames": 15}` in `timeline.transitions` (the outgoing pastel UI is held on its last frame underneath), with the B-roll's z1 `fx.clip({kenburns: [1.0, 1.06]})` starting on the cut | soft whoosh (optional) |
| **T-11** | Insert push | 8 | Inside L-topband: the outgoing insert slides out left (`out: "slide-l"`) while the incoming one slides in from the right (`in: "slide-r"`) in the same frames (`in_frames` / `out_frames: 8`), expo-out, `smear: true` for the horizontal motion blur (v01 @ 9.56–9.84). Enter / exit presets are measured at rest, so the ≈ 87 px / frame travel does not trip G3 | silent, or the list cue when it brings in a new item |

### 9.2 Grammar
| Boundary | Use | Never |
|---|---|---|
| Frame 0 | The live take mid-gesture (+ the F-C blob); F-B plain take | A fade-in from black, a title card before the face |
| Hook → item 1 (F-A) | T-07 tile hand-off | A hard pop of the first tool |
| New item (F-A) | from L-desk: T-03 make-room + P-07; from an insert: T-11 push | A cut to a cutaway world |
| Tool drop → its window | drop rockets off the top + window slides in from the right, same frames | Two inserts cross-dissolving; a rise-and-fade |
| Item → opinion line | window slides out left + T-04 settle-back together | Holding the insert over the opinion |
| Face → concept (F-B) | T-01 on the noun (± 1 f) | A blur-out on a noun (too slow) |
| Face → question card / calendar | T-02 | — |
| Cutaway → face | T-01 on the next sentence start (T-02 runs only face → cutaway) | — |
| B-roll → B-roll (F-C) | T-01 on clause ends (R-1); under a pinned card the clips may stutter through a 2-frame clip (v03 @ 38.23–38.30) | Dissolves, whips |
| Pastel UI → B-roll (F-C) | T-10 curtain wipe | A cross-fade between worlds |
| Last word | T-09 | A black tail, an end card |

### 9.3 Shot grammar `[COND: spine hybrid (F-C)]`
- **R-1** Cut B-roll on clause ends (±1 f of the word end); 2.5–6 s per clip.
- **R-2** When a person is named, cut to a clip of that person within ±5 f and add a P-30 name tag.
- **R-3** Alternate wide and detail clips; never two wides in a row.
- **R-4** Return to the creator's face at least once per chapter for ≥ 2 s (a reflection line).
- **R-5** B-roll that shows the creator counts as presence only when the face is ≥ 6% of the frame height; V-PRESENCE reads the main take's face boxes only, so plan presence from the take.

### 9.4 Budget (per 60 s)
- T-01: F-A 0–4 (plus jump cuts in the take), F-B 8–18, F-C 8–16. T-02: ≤ 3. T-06: only inside P-13/P-21 stacks. T-07: once (F-A hook). T-10: F-C 2–5 per reel. T-11: F-A 2–6 per reel.
- The same transition never 3× in a row, except the F-A item ritual (T-03 / T-11 / T-05 / T-04) and R-1 B-roll cuts.

---

## §10 Motion, camera, layers, finishing `[REQ] [DNA; motion tokens TUNE ±15%]`

### 10.1 Motion tokens
| Token | Value |
|---|---|
| Beat lead | 2 f before the trigger word's onset |
| Entry ease | expo-out `cubic-bezier(0.22, 1, 0.36, 1)` |
| Exit ease | `cubic-bezier(0.64, 0, 0.78, 0)`, 6 f |
| Spring / pop | scale 0 → 1.04 → 1.0 over 3–4 f (hook tiles, emoji tab); 6 f for the tab |
| Fade (words, fragments, hero statement) | 3 f on each word's onset |
| Pill swap | 0 f (hard) |
| Horizontal push (inserts in / out, T-11) | 8–9 f, expo-out, ≈ 700 px travel, horizontal motion blur (engine `slide-r` in / `slide-l` out with `in_frames` / `out_frames` 8–9 and `smear: true`) |
| Rocket exit (tool name, count title) | off the top in 3–8 f with vertical motion blur (engine `rocket`) |
| Row wipe-open (P-13) | width 0 → 100% over ≈ 12 f |
| Stack step (T-06) | 1-frame jump ≈ 50 px, 2–3 per new row, `ctx.blur(8, 90)` on the jump frame |
| Letter reveal | 1 letter / f, each de-blurs 6 → 0 px over 5 f (P-03); P-18 types with tracking settling |
| Typing | 30 characters / s (prompt box, chat replies) |
| Make-room / settle-back | 13 f / 12 f, ease-out; translate + zoom (0.89× / 1.12×) |
| Ink draw | circle 9 f, underline 10 f, arrow 6 + 2 f, flourish 12 f |
| Stack scroll | one card height in 12 f inOut |
| Idle life | tile bob ±3 px at 0.5 Hz; window push 1.00 → 1.05 over the hold; object float ±8 px; dashes flow 2 px/f |
| Hold | titles ≥ 10 f after building; text ≥ 0.25 s per word |

### 10.2 Footage camera (`zoom_policy: presets`)
| ID | Preset | Recipe | Use |
|---|---|---|---|
| **Z-1** | `push-drift` | 1.00 → 1.10–1.12 over the beat (linear, no blur). **Optional:** not measured in the evidence (v02's hook growth is the presenter leaning in; ORB on the take shows no steady digital zoom) | A reflective line (≤ 2 per reel) |
| **Z-2** | `snap-punch` (reframe) | 1.00 → 1.12 over 2 f, **only exactly on a cutmap jump cut**, held to the next cut | Face-only stretches: 2–4 per minute |
| **Z-3** | `pull-out` | 1.12 → 1.00 over 10 f at a later cut | Back to the wide crop |

Rules: never the same Z twice in a row; never two moves within 0.4 s; no camera move while a top-band insert is up (the insert is the event, and a stage change resets the camera) — plain jump cuts in the take may run under an insert (v01 @ 9.44); never shake, crash zoom or rotation snap (H10). The biggest camera-like moves in this style are the make-room / settle-back morphs (§3.3), which carry their own zoom.

### 10.3 Canvas camera
OFF (modules.canvas_camera = false).

### 10.4 Layer order (back to front)
1. z1 world (W-navy / W-paper / W-pastel) or the B-roll clip (`fx.clip`)
2. Footage (the take; lowered in L-topband, dimmed in L-frost)
3. z3 objects on the dome (P-15)
4. z4 cards, windows, UI recreations, list rows, covers, person cards
5. z5 tiles, tool drops, plates (P-01, P-07, P-11, P-12, P-36)
6. z6 titles (P-02, P-03, P-04) and the ink layer (P-27…P-30)
7. z7 the pill (auto)
8. z8 hero statement, question card, ink bubble (the pill hides)
9. Core-drawn, no scenes: the T-02 blur-out (a `timeline.grades` event on the footage) and the T-10 `curtain` transition (picture layer: world, footage and z1–6, under the pill)

### 10.5 Finishing
- Window rims: 3 px solid rim + 18 px outer glow at 45% of the rim tint; the only glowing shapes.
- Card shadows soft (`0 10 30 rgba(0,0,0,.12)` on light worlds; `0 18 40 rgba(0,0,0,.35)` on navy); no hard offset shadows anywhere.
- Grain only on W-navy (0.05) and W-paper (0.03); vignette only on W-navy (0.35) and W-paper (0.12).
- Glow only on the glow headline (P-04) and the window rims.
- Footage untouched (no grade, no grain, no vignette).

---

## §11 Sound contract (minimal) `[REQ] [VAR]`
Sound comes from the bundled SFX pack and its global rules S1–S6 (every cue marks a visible event, ≤ 2 uses per file, one list-cue exception, no consecutive repeats, catalogue ids only); the pack's calm defaults follow `tone.energy: calm`.

| Line | Decision |
|---|---|
| **Cue moments** | `hook` (≤ 3 cues: tile 1 landing, the title reveal, the cut into the glow headline), `reveals` (a tool drop landing, a window or card arriving, an ink circle finishing, a row pick), `list_cue` (one soft pop or swish on every F-A tool drop / F-C chapter bubble). Transitions are silent; ≤ 4 cues per 10 s; nothing in the 1.0 s before the CTA |
| **Meme cues** | Off (comedy off) |
| **Music bed** | On, entering after the hook (unverified: no audio was observable in the evidence) |
| **Ducking** | The bed sits 20 dB under the voice while the voice speaks; the creator's B-roll sound is muted under the voice unless the script calls for it |
| **Loudness** | −14 LUFS integrated, true peak ≤ −1.5 dBTP; hard end ≤ 6 f after the last word (NC-8) |

---

## §12 Footage requirements, shot list, fallbacks, inserts `[REQ]`

### 12.1 Setups `[DNA assumed; VAR actual]`
| ID | Setup | Spec |
|---|---|---|
| **A** | Desk talker (F-A, F-B; F-C reflections) | Vertical, 4K preferred (1080 p allows reframes up to 1.12×), 30 fps; seated at a desk, eye level, 35–50 mm equivalent; head top at y 260–380 in the full frame; soft key from camera left, bright and warm; background a bokeh bookshelf or a pale plain wall; a light plain tee; the desk edge visible at the bottom |
| **B** | Walk-and-talk / standing (F-C) | Same camera rules; a workplace or studio; a visible lav mic is fine; a foreground plant or desk edge may frame the shot; head top y 280–420 |

### 12.2 Shot list
| ID | Shot | Spec | Count per 60 s | Must / optional | Formats |
|---|---|---|---|---|---|
| SH-1 | The talking-head take | Setup A (B allowed in F-C), one continuous take or a few takes | 1–3 takes | must | all |
| SH-2 | Screenshots / screen recordings | One per tool, site or document named; recordings 4–8 s, 30 fps, the relevant screen only; personal data hidden or blurred | 3–6 | optional | F-A, F-C |
| SH-3 | Logo files | PNG/SVG of each tool named, only ones the creator may show | 3–6 | optional | all |
| SH-4 | B-roll of the creator's own work/life | 3–6 s clips: the workplace, people (with consent), hands on laptops, the product in use; wides and details | 6–12 | must (F-C) | F-C |
| SH-5 | Object / cover photos | Books, products, gear; cut-out PNG preferred | 0–4 | optional | F-B, F-C |
| SH-6 | People | A photo or a short clip of each person named | 0–3 | optional | F-B, F-C |

### 12.3 Fallbacks
| ID | For | What the engine does instead | Fidelity cost | Result |
|---|---|---|---|---|
| FB-1 | SH-1 | Nothing: the style needs the creator on camera | format unavailable | no_fallback |
| FB-2 | SH-2 | P-09 / P-21 / P-20 / P-22 recreated generic UI built from the script's words | no real product pixels; the window reads as a diagram of the tool | degraded |
| FB-3 | SH-3 | The tool's name in its type voice on a monogram tile (P-07) | no brand mark; the typographic variety carries it | holds |
| FB-4 | SH-4 | Tell the story in F-B worlds: L-desk + W-pastel chat/file UIs + W-navy cards; B-roll beats become P-21 / P-22 / P-37 / P-06 on W-navy | no lived-in footage; the story reads as an explainer (consider switching the reel to F-B) | degraded |
| FB-5 | SH-5 | A created cover or product card (title and author set in type on a flat cover colour, CSS tilt + soft shadow), or `fx.icon` line icons for objects | no real cover art | holds |
| FB-6 | SH-6 | `fx.silhouette` + a P-30 name tag with the name and role from the script | no face of the person | holds |

Say at the checkpoint which fallbacks a reel uses.

### 12.4 Props, reaction bank, matte, resolution
- Props: none required. A real object the creator holds up (a book, a notebook) is its own visual; then skip P-16 for it.
- Reaction bank: none.
- Matte: only for P-17 (a person cut-out from a supplied clip or photo).
- Minimum source: 1080 px wide for Z-2 reframes up to 1.12×; 2160 px for anything tighter. L-topband needs no extra headroom (the engine fills the revealed band with a blurred copy), but the head top must be ≥ 260 px in the full frame or the offset hits its 340 px cap.

### 12.5 Third-party inserts: ask, then create `[REQ]`
Claude never fetches anyone else's media.
1. **Analyse** (`veos inserts scan`, refined by hand): every P5b row that names a product, app, site, book, person, post, article or quote is a third-party moment.
2. **Ask once**, as a list: "For these N moments, do you have a screenshot, screen recording, logo, photo or clip? Drop the files, or say no and I'll build clean, labelled versions." (e.g. "1. [Tool] screen · 2. [Tool] logo · 3. [Book] cover · 4. photo of [Person]").
3. **Supplied:** use as given (P-08 window, P-07 tile with the logo, P-16 cover, P-17 cut-out); crop, frame and circle, never alter what it says; blur personal data.
4. **Not supplied, build from the script's words:**

| Moment | Created substitute | Recipe id | Label |
|---|---|---|---|
| A product / app / site / company | P-07 tool drop (name in type, monogram tile) or `fx.logoPlate` | `logo_plate` | none (it is type) |
| An app's screen, a UI flow, an AI prompt | P-09 / P-21 / P-20 / P-22 (`fx.appUI` or bespoke generic UI) | `recreated_ui` | — |
| A post or quote read aloud | P-34 (`fx.quoteCard`, verbatim) | `quote_card` | — |
| A book / course | P-16 created cover | `diagram` | none (it is type) |
| A person | `fx.silhouette` + P-30 | `silhouette` | — |
| An article or headline | `fx.headlineCard` on W-paper | `headline_card` | — |

5. **Record** every moment in `plan/inserts.json`: `{id, moment, t0, t1, kind, origin: creator | created, file?, recipe?, substitute_of?, quote_text?}`, and put its id on the scene as `insert`.

### 12.6 Frame rate and audio
Output 1080×1920, 30 fps CFR (conform VFR). One voice track: high-pass 80 Hz, de-ess, light compression, −14 LUFS.

---

## §13 Output contract `[REQ] [DNA]`

### 13.1 Core beat fields
`id`, `section`, `t0`, `t1`, `spoken`, `trigger {word, at}`, `tone`, `line_type` (§8.4), `layout` (L-…), `visual` (one sentence), `layers` (scene ids), `pattern` (P-…), `sfx`.

### 13.2 Conditional fields used by this style
| Switch / module | Beat fields |
|---|---|
| captions (full) | `caption {profile: "CS-1", overrides: []}` (no emphasis, no tiers) |
| ink | `anchor {target: "<scene id>#<element>" or region {x, y, w, h}}`, `ink [{mark: circle / underline / arrow / name_tag / sparkle, target, frames}]` |
| brand | `sponsor {id, disclosure}` on paid / affiliate segments |
| footage ≥ medium | `shot_id` (SH-…), `fallback_used` (FB-… or null) |
| third-party moment | `insert {id, origin: creator / created}` |
| E3 | captions inherit E3 from CS-1; a scene with 28–39 px redundant labels sets `exception: "E3"` |
| this style | `make_room_offset` (on L-topband entries), `type_voice` (P-07: sans / serif / airy / round), `rim` (P-08: accent / violet / data), `world` (W-…) |

```yaml
- id: 7
  section: ITEM-2
  t0: 12.10
  t1: 14.60
  spoken: "Next up we have [Notes app], which is my second brain"
  trigger: {word: "[Notes app]", at: 12.62}
  tone: explain
  line_type: tool_named
  layout: L-topband
  make_room_offset: 284
  pattern: P-07
  type_voice: sans
  visual: "Tile with the notes app's monogram pops into the top band; its name writes on in Poppins 700; a teal bar grows under it"
  layers: [drop-notes]
  insert: {id: I3, origin: created}
  caption: {profile: CS-1, overrides: []}
  shot_id: SH-1
  fallback_used: FB-3
  sfx: [{id: "<pack pop id>", on: "drop-notes@0.25", why: "tool drop lands"}]
```

### 13.3 Reel header
```yaml
format: F-A                 # F-A | F-B | F-C
theme: null                 # single palette
hook_archetype: HA-04       # HA-04 | HA-12 | HA-02
structure: list             # list | explainer | story
count: 5                    # F-A items (= the count title numeral)
keyword: null               # never set: the CTA lives in the post caption
cta: {device: post_only, post_caption: "5 study apps that run my week. Link in bio."}
make_room_offset: 284       # from the P1 head-top measurement
inserts: plan/inserts.json
sponsor: null
```

### 13.4 Hook proposals (3)
```yaml
- name: "Topic build: 5 study apps"
  archetype: HA-04
  headline: "5 STUDY APPS"               # title_card, <= 6 words
  subline: "that run my whole week"      # P-03, <= 7 words
  pair: {first_subject: "5 monogram tiles", reveal: "count title by 1.0 s"}
  captions: CS-1 from the first word
  storyboard: "f0 tile 1 in flight | 0.03 make-room | 0.3 tiles 2-5 pop | 0.45 numeral | 0.6-1.0 title | 1.1-2.4 subline | 3.0 tile hand-off"
  sound: [pop on tile 1, soft reveal on title, list cue on item 1]
  stopper_test: {mute: pass, motion_f0: pass, read_s: 0.75, sc_0_3s: 9.5, payoff_s: 1.0}
```

### 13.5 Checkpoint (send, then wait for approval)
1. The format and why; 3 hook proposals with stopper results.
2. The P5b named-thing inventory: every named thing with its pattern and source (creator file / created recipe).
3. The beat sheet with tones and layouts, the transition map, the SFX cues.
4. The ink plan (marks, targets, times) and the inserts record (creator vs created), with the fallbacks used.
5. The make-room offset and the measured head top.
6. Style stills: f0, the title at 1.0 s (or the glow headline), one top-band insert, one cutaway or B-roll card, one ink mark, the last frame.

---

## §14 Worked examples `[REQ] [NICHE]`
Times are planning estimates; replace them with `words.json` onsets. Tool, book and person names in brackets are slots for the buyer's real ones.

### 14.1 F-A Desk list — niche A: "5 study apps that run my week" (≈ 51 s)
**Header:** F-A · HA-04 · list · count 5 · make-room offset 284 (head top 300) · CTA post_only ("Which one would you keep? My setup is linked in bio.").

**Hook (0–3.0 s)** — spoken: "These are five study apps that run my whole week. First, [Flashcard app]…"
| t (s) | Spoken | Visual | Pill | Layout / camera | Cue |
|---|---|---|---|---|---|
| 0.00 | — | Tile 1 "FL" flies in from the left, spinning −90° → −10° | — | L-desk → G-1 at 0.03 | pop |
| 0.12 | "These are five" | Tiles "NO", "TI", "RE", "CA" pop at 0.30 / 0.40 / 0.50 / 0.60 | "These are five study" | L-topband (offset 284) | — |
| 0.45 | "study apps" | Numeral "5" (G-count) | — | — | — |
| 0.62 | "that run my" | Title "STUDY APPS" slides in; complete by 1.0 | "apps that run my" | — | reveal |
| 1.10–2.40 | "whole week." | Serif subline "that run my whole week" types on | "whole week." | — | — |
| 2.62 | "First," | Holds | "First," | — | — |
| 2.95 | "[Flashcard app]" | T-07: tile "FL" travels to the tool slot; everything else exits | "[Flashcard app]," | — | list cue |

**Section plan**
| Section | t (s) | Spoken gist | Patterns, in order | Layout | Ink / camera | Inserts |
|---|---|---|---|---|---|---|
| ITEM-1 | 2.95–11.8 | "…it shows me 40 cards due every morning" | P-07 (round voice) → 5.0 P-08 window: the creator's recording of the review screen, rim accent → 7.3 P-27 circle on "40 due" (spoken "40 cards") → 9.6 T-05 + G-2 | L-topband → L-desk | circle 7.3; Z-2 reframe at the 10.4 jump cut | I1 logo plate (created), I2 recording (creator) |
| ITEM-2 | 11.8–20.2 | "Next up, [Notes app]: lectures, readings and my own notes in one place" | P-07 (sans) → 14.0 P-10 sequence: 3 screenshots (lecture page → reading list → index), rim violet → 19.0 out + G-2 | L-topband → L-desk | — | I3 logo plate, I4 screenshots (creator) |
| ITEM-3 | 20.2–28.0 | "Third, [Timer app]: 25 minutes on, 5 off" | P-07 (airy) → no creator file: 22.4 P-37 stat card "25 min" + label "focus, then 5 off" → 24.8 P-27 circle on "25" → 26.4 out + G-2 | L-topband → L-desk | circle 24.8 | I5 logo plate (created) |
| ITEM-4 | 28.0–36.6 | "Fourth, [Reader app], which sends my highlights straight into my notes" | P-07 (serif) → 30.6 P-11 dashed link: [Reader app] ↔ [Notes app] plates, the arc draws on "straight into" → 35.0 out + G-2 | L-topband → L-desk | Z-2 reframe at the 35.4 cut | I6 logo plate |
| ITEM-5 | 36.6–47.0 | "And finally, [Calendar app]: every Sunday I block the week" | P-07 (sans, ≠ the previous serif) → 39.0 P-08 window: the creator's calendar screenshot, rim data, scrolling → 41.6 P-27 circle on the Sunday block → 44.5 out + G-2 | L-topband → L-desk | circle 41.6 | I7 logo plate, I8 screenshot (creator) |
| OUT | 47.0–51.0 | "Which one would you keep? Tell me." | P-35 quiet out | L-desk | Z-3 pull-out at the 47.0 cut | — |

Checks: 5 ITEM sections = numeral 5; presence 100%; type voices round → sans → airy → serif → sans; rims accent → violet → data; 3 ink marks in 51 s.

### 14.2 F-B Concept cutaways — niche B: "Train one lift for 12 weeks" (≈ 56 s)
**Header:** F-B · HA-12 · explainer · pill cy 1220 · CTA post_only ("Which lift are you picking?").

**Hook (0–3.6 s)** — spoken: "What if you trained just one lift for the next twelve weeks?"
| t (s) | Spoken | Visual | Pill (cy 1220) | Layout / camera | Cue |
|---|---|---|---|---|---|
| 0.00 | — | Desk take | — | L-desk (leaning in) | — |
| 0.15 | "What if you trained" | — | "What if you trained" | — | — |
| 0.95 | "just one lift" | — | "just one lift" | — | — |
| 1.60 | "for the next" | **Hard cut to W-navy**: "ONE LIFT" glow headline (payoff), hand subline "for the next 12 weeks" already on; kettlebell + calendar-page icons slide left → right across the dome | "for the next" | L-cutaway | soft whoosh on the cut |
| 2.30 | "twelve weeks?" | The kettlebell rises into the dome centre | "twelve weeks?" | — | — |
| 3.60 | "Most of us…" | Hard cut back to the face | "Most of us chase" | L-desk | — |

**Section plan**
| Section | t (s) | Spoken gist | Patterns, in order | Layout / world | Ink / camera |
|---|---|---|---|---|---|
| PROBLEM | 3.6–11.0 | "Most of us chase five goals at once: cardio, mobility, strength, diet, sleep" | face → 6.0 T-01 → P-13 rows "🏃 Cardio", "🧘 Mobility", "🏋️ Strength", "🥗 Diet", "😴 Sleep" on their words (6.2–10.4) → 11.0 T-01 back | L-desk → L-cutaway W-navy | — |
| CONCEPT | 11.0–21.0 | "There's a book called [Book] by [Author]… '[verbatim line]'" | face → 14.0 T-01 → P-16 cover (creator photo or created) → 17.0 T-01 to face → 18.5 G-5 → P-34 quote card (verbatim) on L-frost → 21.0 out | L-desk → W-navy → L-desk → L-frost | P-28 underline under the highlighted phrase at 19.8 |
| EXAMPLES | 21.0–34.0 | "So pick one. For me this block it's strength: three sessions a week." | face → 25.0 T-01 → P-13 rows again → 26.4 P-14 pick "Strength" (good) → 30.0 T-01 to face → P-37 stat "3 sessions" + "a week" in the top band (G-1) → 33.2 G-2 | W-navy → L-topband → L-desk | P-27 circle on "3" at 30.6 |
| QUESTION | 34.0–40.0 | "So ask yourself: what's the one lift that would change your training most in 12 weeks?" | 34.0 T-02 → P-18 question card on W-paper (pill hidden) → 40.0 T-01 back | L-cutaway W-paper → L-desk | — |
| TACTIC | 40.0–52.0 | "Then put it in your calendar first: deadlift at 6:30, mobility after, everything else around it" | face → 43.0 T-02 → P-19 calendar: "Deadlift · 6:30" focus block (data) on "first", "Mobility · 10 min" (warm), "Everything else" (grey) → 49.0 T-01 back | W-paper → L-desk | P-27 circle on the focus block at 44.6 |
| OUT | 52.0–56.0 | "Which lift are you picking?" | P-35 | L-desk | — |

Checks: longest absence 6.0 s (QUESTION, TACTIC) ≤ 6.5; presence ≈ 52%; one glow headline; inserts I1 book cover and I2 quote (verbatim), both recorded.

### 14.3 F-C Story with B-roll — niche A: "When I tried timeblocking for a month" (≈ 78 s)
**Header:** F-C · HA-04 (ink bubble) · story · standard class · re-hook at 35.5 s · CTA link_bio ("My template is in my bio.").

**Hook (0–5.5 s)** — spoken: "When I tried timeblocking for a month, I genuinely didn't expect how much I'd actually get done."
| t (s) | Spoken | Visual | Pill | Layout | Cue |
|---|---|---|---|---|---|
| 0.00 | — | Walk-and-talk (setup B); the ink blob scales in at the top band | hidden (z8) | L-desk | pop |
| 0.15 | "When I tried" | Fragment "When I tried" fades in word by word; sparkles pop | hidden | — | — |
| 0.60 | "timeblocking" | Wordmark "TIMEBLOCKING" pops; the paper outline draws | hidden | — | — |
| 1.20 | "for a month," | Second fragment "for a month" | hidden | — | — |
| 1.80 | "I genuinely" | **Hard cut to B-roll** (library desk); hero statement line 1 "I genuinely" | hidden (z8) | L-broll | — |
| 2.40 | "didn't expect" | Line 2 "*didn't expect*" (gold italic); P-28 underline at 2.75 | hidden | — | soft scribble |
| 3.30–5.30 | "how much I'd actually get done." | Lines 3–4 "how much / I'd get done" | hidden | — | — |

**Section plan**
| Section | t (s) | Spoken gist | Patterns, in order | Layout / world | Ink | Face on screen |
|---|---|---|---|---|---|---|
| CHAPTER-1 | 5.5–22.0 | "Week one: I messaged my study group, 'Blocking 9 to 11 for physics, every day.' Riya replied 'I'm in.' So I set it up like this…" | 5.5 B-roll (morning desk) + P-24 chat card in the top band: me "Blocking 9 to 11 for physics, every day", Riya "I'm in" types → 10.0 T-01 face (1.8 s) → 11.8 T-02 → P-19 calendar: physics block 9:00–11:00 (data), "Lab report" (warm), "Gym" (grey) → 16.0 T-01 face: "Honestly, day three was rough." | L-broll → L-desk → W-paper → L-desk | P-27 on the physics block at 13.4 | 10.0–11.8, 16.0–22.0 |
| CHAPTER-2 | 22.0–37.5 | "But Riya kept showing up at nine sharp…" | 22.0 B-roll library with Riya + P-30 name tag "Riya" at 23.0 → 27.0 T-01 W-pastel P-21 thread (Riya "Same time tomorrow?" / me "9 sharp") → 33.0 face → **35.5 P-05 chapter bubble "Then came / EXAM WEEK"** (re-hook, pill hidden) | L-broll → W-pastel → L-desk | name tag 23.0 | 33.0–37.5 |
| CHAPTER-3 | 37.5–58.0 | "Exam week… the plan made a revision summary: twelve topics, one per block" | 37.5 B-roll exam prep (3 clips, R-3) → 43.0 face + G-1 → P-22 file card "Physics revision summary" in the top band ("12 topics" spoken) → 50.0 G-2 → face reflection to 58.0 | L-broll → L-topband → L-desk | P-27 on "12 topics" at 45.2 | 43.0–58.0 |
| TURN | 58.0–66.0 | "By the end of the month I'd logged 38 focused hours." | 58.0 T-01 W-navy P-37 stat "38 hours" + "focused, in one month" → 62.0 B-roll result (hands on the finished paper) | W-navy → L-broll | P-27 on "38" at 59.4 | — |
| OUT | 66.0–78.0 | "If you try it, start with one block. My template is in my bio." | face, P-35; Z-3 pull-out at 66.0 | L-desk | — | 66.0–78.0 |

Checks: longest absence 8.2 s (1.8–10.0) ≤ 12; presence ≈ 41% (20–45); re-hook at 35.5 s (45% of 78) and the gaps 5.5 → 35.5 → 78 are ≤ 45 s; B-roll cut on clause ends; inserts I1 chat (created), I2 calendar (created), I3 file card (created); the creator's real screenshots replace them when supplied.

---

## §15 QA checklist `[REQ] [DNA]`

**1. Profile conformance**
- [ ] The format matches the script (§0.4); the reel header declares it. (review)
- [ ] Presence share and longest absence per format (H8). (V-PRESENCE)
- [ ] Layout shares within the format's targets (§3.2); L-topband entered with the measured offset. (V-LAYOUT + review)
- [ ] Duration inside the class (F-A/F-B 45–60 s, F-C 60–90 s). (review)

**2. Hook**
- [ ] f0: live take moving; tile 1 grows in by 0.2 s (F-A) / blob on screen (F-C). (V-F0)
- [ ] Topic title by 1.8 s; F-B glow headline tagged `payoff: true` by 1.8 s. (V-F0)
- [ ] Headline ≤ 6 words, ≤ 2 lines, 0 emoji; subline ≤ 7 words. (V-TITLE)
- [ ] ≥ 6 weighted SC in 0–3 s; the mute test passes. (V-CADENCE + review)

**3. Body and cadence**
- [ ] 5–10 SC per 10 s (F-B 5–11); body gaps ≤ 4.0 s (F-B 3.5 s); nothing static > 2.5 s. (V-CADENCE)
- [ ] Every P5b named thing has its visual on the word (−2 f, ±5 f). (V-ONWORD)
- [ ] One insert at a time; the next enters only after the previous exit (≤ 2 f overlap). (review, G2)
- [ ] F-A ritual identical per item; type voices and rim tints rotate. (review)
- [ ] F-C re-hook between 40% and 55% of runtime; gaps ≤ 45 s. (V-REHOOK)

**4. Captions**
- [ ] CS-1: 2–5 words, 1 line, 50 px Poppins 600, cy 1420 (F-B 1220); karaoke #666666 → #111111. (V-CAPTION, V-TYPE with E3)
- [ ] The pill never overlaps a card, row or window (≥ 40 px clear). (G1)
- [ ] Hidden only under P-06 / P-18 / P-05. (review)
- [ ] Glossary spellings exact. (V-CAPTION)

**5. Modules**
- [ ] Ink (§22): ≤ 3 marks on screen, each on a named target, drawn on the word, finished before the next scene, ≥ 40 px from the face. (review, V-FACE)
- [ ] Brand (§25): paid / affiliate segments carry the disclosure ≥ 2 s; no end card. (V-PROMISE + review)

**6. Truth and inserts**
- [ ] Every third-party moment recorded (creator / created) and shown by its scene. (V-INSERTS)
- [ ] Recreated UIs generic, quoting only the script. (V-INSERTS + review)
- [ ] Quotes verbatim (NC-13); personal data blurred (NC-14); numbers only as spoken. (V-INSERTS, V-NUMFMT + review)
- [ ] No fetched logos; no brand look-alike UIs. (review)

**7. Sound contract**
- [ ] Cues only on hook, reveals and the list cue (S1–S6); ≤ 4 per 10 s; silence 1.0 s before the CTA. (S1–S6)
- [ ] Bed after the hook, 20 dB under the voice; −14 LUFS; true peak ≤ −1.5 dBTP. (mix gate)

**8. End and export**
- [ ] Ends on the face (P-35), hard end ≤ 6 f after the last word, no black tail. (review)
- [ ] 1080×1920, 30 fps CFR. (review)
- [ ] Hue cap ≤ 3; one glow headline max; no shake / crash / glitch. (V-HUES, V-CAMERA)

---

## Conditional modules (§16–§25)

§16 Frame template / chrome: OFF (profile.modules.chrome = false): nothing persists across the reel except the pill.

§17 Running state & anchored graphics: OFF (modules.running_state = false, modules.anchors = false): ink targets are static rects (§22), no counters persist.

§18 Data contract: OFF (modules.data_figures = false): numbers appear only as spoken words (§8.5).

§19 Evidence & citations: OFF (modules.citations = false): no credit lines; the §12.5 inserts flow still applies.

§20 Dialogue: OFF (modules.dialogue = false): one presenter.

§21 Canvas camera: OFF (modules.canvas_camera = false).

### §22 Ink & annotation layer `[COND: modules.ink — ON] [DNA look; TUNE colour]`
The handmade layer on top of clean UI: it tells the eye where to look.

**Stroke tokens**
| Token | Value |
|---|---|
| Colour | `marker` #D92D3A (TUNE: red to coral, ≥ 4.5:1 with white); name tags and bubble outlines in `paper`; sparkles in `concept` |
| Width | 7 px (TUNE 5–8), round caps and joins |
| Wobble | seeded ±1.5 px perpendicular noise along the path (8–12 control points), fixed per mark (`ctx.rngStable`) |
| Draw-on | circle 9 f (TUNE 7–12), underline 10 f, arrow shaft 6 f + head 2 f, name-tag flourish 12 f, bubble outline 14 f; ease-out |
| Overshoot | circles start at 200° and run 375° (15° past the start), so the end crosses the start like a pen stroke |

**Marks**
| Mark | Pattern | Geometry | Use |
|---|---|---|---|
| Circle | P-27 | ellipse round the target rect + 14–22 px pad, tilt ±6° | a number, a field, a feature, a word on a card |
| Scribble underline | P-28 | 2 waves, amplitude 6 px, 10 px below the baseline, the phrase's width + 8 px | a key phrase (hero statement, card line, title) |
| Arrow | P-29 | curved shaft 80–140 px long ending 16 px from the target, 2-stroke head 26 px | "this one", "right here" |
| Name tag | P-30 | Caveat 600 60 px + a curl flourish, ≥ 40 px from the face box | a person in B-roll or a person card |
| Sparkles | P-31 | 4-point stars 28–40 px | either side of a wordmark |
| Bubble outline | P-05 | the blob outline offset 10 px, 3 px paper | the ink bubble |
| Highlight sweep / box | — | not used in this style | — |

**Targets.** Ink lands on rects you know exactly: the element rect inside a card you built (draw the mark inside that card's own markup so it nests and moves with it), or a pixel rect inside the creator's screenshot (scaled into the window). On footage, only a person beside whom a name tag sits, read in the anchor pass (§1) and static within ± 30 px for the tag's life; otherwise no mark (anchors / tracking are off).

**Rules**
- ≤ 3 marks on screen; 2–6 marks per 60 s (budget `ink_marks_per_60s`).
- A mark starts drawing 2 f before its word and finishes within its draw time; it lives as long as its target and exits with it.
- Marks finish before the next scene; never on the face (≥ 40 px from the face box); never on the pill.
- One circle per card at a time; a second circle on the same card replaces the first (fade 4 f).
- Ink never means good/bad; a "winner" in P-12 gets the circle because it is the one being talked about.

**Recipe (SVG inside the target scene; deterministic):**
```js
function inkCircle(ctx, r, p, seed) {            // r = {x, y, w, h} target rect; p = 0..1 draw progress
  const R = ctx.rngStable(seed), pad = 18, cx = r.x + r.w / 2, cy = r.y + r.h / 2;
  const rx = r.w / 2 + pad, ry = r.h / 2 + pad, tilt = (R() * 12 - 6) * Math.PI / 180, pts = [];
  for (let i = 0; i <= 40; i++) {                 // 200° -> 575° (375° sweep: 15° overshoot)
    const a = (200 + 375 * i / 40) * Math.PI / 180, w = 1 + (R() - 0.5) * 0.03;
    const x = rx * w * Math.cos(a), y = ry * w * Math.sin(a);
    pts.push([cx + x * Math.cos(tilt) - y * Math.sin(tilt), cy + x * Math.sin(tilt) + y * Math.cos(tilt)]);
  }
  const d = "M" + pts.map(q => q[0].toFixed(1) + " " + q[1].toFixed(1)).join(" L"), L = 2 * Math.PI * Math.max(rx, ry) * 1.1;
  return `<svg width="1080" height="1920" style="position:absolute;left:0;top:0;overflow:visible"><path d="${d}" fill="none"
    stroke="${ctx.col("marker")}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"
    stroke-dasharray="${L.toFixed(0)}" stroke-dashoffset="${(L * (1 - ctx.ease.out(ctx.clamp(p)))).toFixed(1)}"/></svg>`;
}
```

§23 Continuity: OFF (modules.continuity = false). The one hand-off (T-07 tile → tool drop) is a transition, not a morph chain.

§24 Series furniture: OFF (modules.series = false; VAR). If a buyer turns it on: a series tag `{name} · part {n}` Poppins 600 40 px paper on a 60% ink chip at x 64, y 130 for the hook only (2.5 s, inside the top band, left of the count title), and the number from the reel brief; it counts toward the intro cap.

### §25 Sponsor, brand & end cards `[COND: modules.brand — ON] [DNA look; VAR assets]`
- **Sponsor / affiliate segment:** P-36 in the top band: the brand's logo only if the creator supplies it (else its name in a type voice), plus the disclosure "Paid partnership" (TC-legal, Poppins 500 24 px, paper at 0.85, centred under the plate) for the whole segment and ≥ 2 s; the creator also says it (NC-12). The plate never sits over the face, the pill or another insert. The sponsor's screens follow P-08 / P-10 like any tool.
- **The creator's own product** (their app, course, book, newsletter): treat it as a tool (P-07 with the creator's logo, P-08 with their own screens; P-05 bubble when it is the story's subject). No disclosure is needed, and no hype stamps.
- **Brand colours** appear only inside the creator-supplied logo file; created plates stay in the template palette.
- **End cards:** none (brand.endcard.max_s = 0; V-PROMISE fails any end card). The reel ends on the face (P-35).

---

## Part C. Declared exceptions and the non-overridable core

### C.1 This style's exceptions
| ID | Limits | Scenes that rely on it |
|---|---|---|
| E3 Quiet type | Pill 48–56 px (default 50), weight ≥ 600, 1 line, ≤ 30 characters, contrast ≥ 4.5:1 on the painted pill (queued #666666 is 4.8:1); labels 28–39 px only with `data-redundant` | Captions (inherited from CS-1); UI scenes with redundant 28–39 px meta labels set `exception: "E3"` |

A buyer may switch E3 off (stricter, VAR): the pill then runs at 54 px and the chunk limit drops to 26 characters.

### C.2 The non-overridable core (applies untouched)
| ID | Rule | Where this style is most at risk |
|---|---|---|
| NC-1 | The face is never covered | Top-band inserts after make-room (H7); name tags |
| NC-2 | Meaning text never overlaps meaning text | The pill vs list rows / cards (N6) |
| NC-3 | Smooth motion; eased camera; ≥ 0.4 s between camera moves | Z-2 reframes only on cuts |
| NC-4 | Legibility floors and contrast | The pill's queued grey; UI text ≥ 40 px |
| NC-5 | IG bands: nothing meaningful in the top 110 px, below y 1540, or in the right 110 px between y 900–1540 | The top band starts at y 130 (the evidence started at 55) |
| NC-6 | Truth: no invented facts, numbers or UIs presented as real | Recreated chats, calendars, file cards (H13) |
| NC-7 | Creator-owned media only; never fetched | Logos, screenshots, covers, people (§12.5) |
| NC-8 | −14 LUFS, true peak ≤ −1.5 dBTP, bed ≥ 18 dB under the voice | §11 |
| NC-9 | Determinism | Seeded wobble, bob and dot positions |
| NC-10 | ≤ 4 bright hues per frame (this style: 3) | Rim + ink + headline |
| NC-12 | Disclosure of paid segments | §25 |
| NC-13 | Quote integrity | P-34, P-18 when quoting |
| NC-14 | Redaction of personal identifiers | Creator screenshots and recordings |

---

## Part D. Personalisation

### D.1 Asked at setup (one round; every question has "keep the template default")
| ID | Question | Default | What it changes |
|---|---|---|---|
| BV-01 | Your name and handle | "the creator" / "@yourhandle" | `creator.name/handle`; the greeting in a P-09 prompt box only when the script says it |
| BV-02 | One or two brand colours | primary #EBC20E, accent #3FCFC6 | `roles.primary` (glow headline, picked-row edge) and `roles.accent` (window rims, tool-drop bar, dashed links); contrast-nudged in OKLCH |
| BV-05 | The language you speak and your caption language | English ({{BV-05.speech|en}} → {{BV-05.captions|en}}) | `profile.language`, always asked: **English** → English captions (default) · **Hinglish** → romanised Hinglish captions · **Hindi** → Devanagari captions; numbers follow (BV-06) |
| BV-08 | Your call to action | post_only ("link in bio" in the post) | `profile.cta.chosen` + `creator.cta`; it goes in the post caption only (§6.7) |

This copy: {{BV-01.name|the creator}} ({{BV-01.handle|@yourhandle}}), speaking {{BV-05.speech|English}} with captions in {{BV-05.captions|English, Latin script}}.

### D.2 Defaulted, changeable later
Fonts within each slot's class (BV-03); niche topics inferred per reel (BV-04); number format from the language (BV-06); formats enabled: all three (BV-09); humour off, max `light` (BV-11); series off (BV-13); sponsor disclosure "Paid partnership" (BV-14); never-on-screen list empty (BV-15); logo files none, names set in type (BV-16); duration within the class (BV-17).

### D.3 Lock map (summary; full map in `tokens.json → locks`)
| Field | Lock | Range |
|---|---|---|
| Karaoke pill mechanics (CS-1 chunking, karaoke, pill container type, hide rules) | DNA | — |
| Pill size / weight / y | TUNE | 48–56 px / 600–700 / y 1220–1440 |
| Pill fill / queued grey / active colour | TUNE | light neutral L ≥ 0.94 / a grey ≥ 4.5:1 on the fill / near-black |
| `primary`, `accent` colours | VAR | any (contrast-nudged) |
| `concept`, `data`, `violet`, `marker`, `warm`, `rose`, `night`, `cream` | TUNE | hue families in tokens |
| `good` | DNA | — |
| Worlds (W-desk, W-navy, W-paper, W-pastel) | DNA set; navy/pastel hex TUNE | deep navy L ≤ 0.2; pastels L ≥ 0.85 |
| Fonts | TUNE inside the class | e.g. body: Poppins / Plus Jakarta Sans / Jost / Montserrat |
| Layouts and stage moves | DNA; make-room offset TUNE | 220–340 px |
| Hooks (archetype set, f0 rules) | DNA | per-reel choice VAR |
| Cadence, motion tokens | TUNE | ±15% |
| Ink look | DNA; width/colour TUNE | 5–8 px; marker or primary |
| Modules ink / brand / series | DNA / VAR / VAR | — |
| Sound contract | VAR | duck −26 to −18 dB |

### D.4 How common tweaks are classified
| Buyer says | Class | What happens |
|---|---|---|
| "Bigger captions" | TUNE | 50 → up to 56 px |
| "Captions in yellow / with coloured keywords" | DNA | warned deviation (N7: the pill is two greys) |
| "Captions higher" | TUNE | cy down to 1220 |
| "Use my brand green" | VAR | `primary` or `accent` |
| "No red circles" | DNA | warned deviation (the ink layer is one of the 5 traits) |
| "Add an end card with my keyword" | DNA | warned deviation (D8, N10) |
| "Faster, more cuts" | TUNE / DNA | ±15% cadence is TUNE; beyond is a deviation |
| "Use my font" | TUNE | accepted when it is in the slot's class and bundled |
| "Show the real logos" | VAR | yes, when the creator supplies the files (SH-3) |

### D.5 NICHE slots (filled per reel)
§6.4 hook pairs, §8.4 lookup rows, §14 (the first approved reel of each format replaces its example) and App. A grow with every reel, dated, from the transcript. The glossary gains every tool and person name the creator confirms.

---

## Part E. What this template changes vs the evidence
| Area | Evidence | Template | Why |
|---|---|---|---|
| Queued caption grey | #9B9B9B (≈ 2.5:1 on the pill) | #666666 (4.8:1) | NC-4 contrast for every word state |
| Pill opacity | ≈ 88% | 97% | Keeps 4.5:1 for the queued grey over dark footage |
| Ink red | #E63946 | #D92D3A | 4.8:1 with white (the evidence red reached 4.2:1) |
| Top band | y ≈ 55–575 (v01 @ 0:06) | y 130–560 | NC-5: nothing meaningful in the top 110 px |
| List rows | 6 rows ran to y ≈ 1674 with the pill inside the stack (v02 @ 0:26) | ≤ 6 rows ending ≤ 1136; the pill 40 px clear | NC-5 and G1 |
| Logos | Real brand logos and brand typefaces (v01) | The creator's own logo files, else the name in one of 4 bundled type voices | NC-7; logos are never fetched or redrawn |
| Slack / calendar UIs | Look-alikes of real products (v03, v02) | Generic chat, calendar and file cards | NC-6, N2 |
| 3D renders (weight plates, bulb, books) | Pre-rendered 3D objects (v02) | The creator's cut-out photos or line icons on a CSS dome; created covers | No 3D pipeline; no stock |
| Face-only gaps | Up to 5–6 s (v01 0:26–0:31, v03 1:19–1:25) | ≤ 4.0 s body gap (F-B 3.5 s) | Keeps the reel alive with a reframe or a small insert |
| F-B hook | Glow headline lands at 1.83 s (v02) | HA-12 with the headline by 1.8 s | The validator's HA-04 requires a topic title by 1.0 s; v02 is a thesis-first hook |
| CTA | In the post title only | Same, made a rule (post_only / link_bio) | Faithful |
| F-C max absence | 13 s of Slack UI (v03 0:08–0:21) | ≤ 12 s | Presence rule with a clear cap |
| Make-room zoom | Pan ≈ 245 px **plus** zoom-out ≈ 0.89× onto real headroom (v01 @ 0:00.40, 26.6) | Pan by the offset over the engine's blurred top copy | Engine `low` has no scale and no real-pixel reveal (completeness audit, engine gaps) |
| Question card growth | The box grows in width **and** height as a multi-line question types (v02 @ 43.50–44.38) | Built-in `fx.card({grow: "fit-text", titleFont: "body", titleWeight: 600, titleTracking: 0.04})` for every question: it widens, then wraps by words and grows taller line by line | Covered (the tracking settle to normal is not drawn: the tracking holds at 0.04 em) |

---

## Part F. ID index (this playbook)
| Prefix | IDs used |
|---|---|
| D | D1–D8 |
| H / N | H1–H17 / N1–N12 |
| E / NC | E3 / NC-1…NC-14 |
| F (formats) | F-A, F-B, F-C |
| W / L / G | W-desk, W-navy, W-paper, W-pastel / L-desk, L-topband, L-frost, L-cutaway, L-broll / G-1…G-6 |
| CS | CS-1 |
| HA / ST | HA-04 (default), HA-12 (F-B default), HA-02 / ST-2…ST-6 |
| SM | SM-1 tool drop, SM-2 chapter bubble |
| B / P | B-1…B-10 / P-01…P-37 |
| T / R | T-01…T-11 / R-1…R-5 |
| Z | Z-1 push-drift, Z-2 reframe, Z-3 pull-out |
| SH / FB | SH-1…SH-6 / FB-1…FB-6 |
| BV | BV-01, BV-02, BV-05, BV-08 asked; BV-03…BV-17 defaulted |

---

## App. A Headline & hook bank `[NICHE]`
Slots in brackets are filled per reel. Niche A = study & productivity; niche B = home fitness & nutrition.

**F-A Desk list (count title + serif subline; HA-04 unless marked)**
| # | Count title | Serif subline | Niche |
|---|---|---|---|
| 1 | "[N] STUDY APPS" | "that run my whole week" | A |
| 2 | "[N] TOOLS I OPEN DAILY" | "before my first lecture" | A |
| 3 | "[N] NOTE HABITS" | "I'll never drop" | A |
| 4 | "[N] FREE AI TOOLS" | "for [subject] revision" | A |
| 5 | "MY 1-PAGE EXAM PLAN" (HA-02) | — (proof window instead) | A |
| 6 | "[N] HOME-GYM BUYS" | "that I use every single day" | B |
| 7 | "[N] KITCHEN TOOLS" | "for 15-minute meal prep" | B |
| 8 | "[N] APPS IN MY TRAINING" | "and the one I deleted" | B |
| 9 | "[N] BREAKFASTS" | "with 30 g of protein" | B |
| 10 | "MY [N]-MINUTE PREP BOARD" (HA-02) | — (proof window instead) | B |

**F-B Concept cutaways (glow headline + hand subline; HA-12)**
| # | Question spoken | Glow headline | Hand subline | Niche |
|---|---|---|---|---|
| 1 | "What if you studied one subject first every morning?" | "ONE SUBJECT" | "first thing, every day" | A |
| 2 | "What if your phone stayed in another room?" | "OTHER ROOM" | "for one study block" | A |
| 3 | "What if you reviewed before you learned?" | "REVIEW FIRST" | "then the new stuff" | A |
| 4 | "What would change if you planned on Sunday?" | "SUNDAY PLAN" | "15 minutes, once a week" | A |
| 5 | "What if you only did the hardest task?" | "HARD THING" | "before 11 am" | A |
| 6 | "What if you trained just one lift for 12 weeks?" | "ONE LIFT" | "for the next 12 weeks" | B |
| 7 | "What if breakfast was mostly protein?" | "PROTEIN FIRST" | "for 30 days" | B |
| 8 | "What if you walked after every meal?" | "10 MINUTES" | "after every meal" | B |
| 9 | "What if you stopped counting calories?" | "COUNT PLATES" | "not calories" | B |
| 10 | "What if rest days were planned like workouts?" | "PLANNED REST" | "in your calendar first" | B |

**F-C Story with B-roll (ink bubble; HA-04)**
| # | Bubble (fragment / WORDMARK / fragment) | Hero statement keyword line | Niche |
|---|---|---|---|
| 1 | "When I tried / TIMEBLOCKING / for a month" | "*didn't expect*" | A |
| 2 | "When our group tried / ONE SHARED PLAN / this term" | "*nobody missed*" | A |
| 3 | "A week with / [AI TOOL] / as my tutor" | "*honestly surprised*" | A |
| 4 | "When I deleted / [APP] / for 30 days" | "*didn't miss it*" | A |
| 5 | "The day I / QUIT CRAMMING / for good" | "*finally slept*" | A |
| 6 | "When we gave / HABIT CARDS / to 20 clients" | "*did not know*" | B |
| 7 | "A month of / 6 AM WORKOUTS / with my team" | "*never thought*" | B |
| 8 | "When I cooked / ONLY AT HOME / for 4 weeks" | "*saved more*" | B |
| 9 | "Our studio's / FIRST CHALLENGE / last spring" | "*fully booked*" | B |
| 10 | "When I trained / WITH MY DAD / for 12 weeks" | "*didn't expect*" | B |

---

## App. B Evidence map (summary; full map and the unverified list in `evidence.md`)
| DNA element | Evidence |
|---|---|
| Karaoke pill: Poppins-like 600, ~50 px, 2–5 words, grey → black, y 64–75% | v01 @ 0:00–0:50 (y ≈ 1417–1435); v02 @ 0:00.17–0:00.5 (fade-in), y ≈ 1225; v03 @ 0:05–1:25 (y ≈ 1415) |
| Top-band insert + make-room | v01 @ 0:04–0:09, 0:10–0:15, 0:20–0:26, 0:31–0:36, 0:41–0:46 (head top 0.15 → 0.29 of frame height) |
| Tile arc + count title + serif subline | v01 @ 0:00.17–0:02.8 |
| Brand-faithful tool titles | v01 @ 0:04 Notion, 0:10 Claude, 0:19 Momentum, 0:31 Readwise, 0:41 Day One |
| Glow headline + hand subline + object dome | v02 @ 0:01.83–0:03.9 |
| List rows + row pick | v02 @ 0:10–0:16, 0:26–0:29 |
| Book float + person cut-out + handwritten name | v02 @ 0:32–0:37 |
| Question card with emoji tab | v02 @ 0:44–0:48 |
| Calendar day | v02 @ 0:51–0:57 |
| Ink bubble label + sparkles + outline | v03 @ 0:00–0:01.8, 0:05–0:07 |
| Hero statement + gold italic + red underline | v03 @ 0:01.8–0:04 |
| Chat thread on pastel gradient + red circles | v03 @ 0:08–0:21 (circles 0:15–0:18) |
| Name tag on B-roll | v03 @ 0:22–0:24 |
| Frosted pages | v03 @ 0:33–0:35 |
| Card over B-roll | v03 @ 0:36–0:47 |
| No on-screen CTA | v01 end 0:50, v02 end 0:57, v03 end 1:25 |
| Motion at full frame rate (hard pill swap, T-11 push, rocket exits, make-room zoom, row wipe-open, stack steps, blur-out + cut, curtain wipe) | `docs/audit/illustrated-desk/completeness.md` + strips (v01 @ 0.0, 2.7, 9.3, 20.2, 26.5; v02 @ 1.6, 15.75, 27.7, 43.2, 43.78; v03 @ 0.0, 1.7, 22.0, 38.1) |
