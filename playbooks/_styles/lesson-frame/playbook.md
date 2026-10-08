# Lesson Frame Style Playbook (template v1)

**Purpose:** you (Claude) receive {{BV-01.name|the creator}}'s talking-head take (webcam or phone, seated, short sentences) plus, for walkthroughs, their screen recordings or screenshots. Use this playbook to plan and build every frame of a short **lesson reel**: a permanent two-line title, one rounded 4:3 card whose content swaps between the face, term cards, settings screenshots and screen recordings, tracked ALL-CAPS captions directly under the card, a small credit chip, and an empty bottom band. Input is `talking_head` (SW-01); screen material is the buyer's own.

**Style DNA** `[DNA]`. A Lesson Frame reel looks like **a lesson printed on a page**. A near-black dot-grid page (or a pale grid page for software walkthroughs) carries a two-line title lockup that never moves: a bold grotesk line, then a serif-italic line, underlined by a glowing orange hairline. Under it sits one rounded 4:3 card at the same rect from the first frame to the last. The card is the only thing that changes: the presenter talking in short jump-cut sentences, then, the instant they name a term, a white card with that term in huge condensed caps and the presenter shrunk into the corner, then the settings panel with an orange box on the exact field they are naming. A single line of wide-tracked ALL-CAPS Hinglish captions ticks over under the card every ~0.6 s. Nothing decorates the page. Nothing slides or whooshes: every change is a hard cut inside a frame that never moves; the only smooth moves are a rare push-in or pull-out on the face card in the back half of a reel.

**Copy these 5 things** (each points to where it is built):
1. **The persistent title lockup:** line 1 Inter Tight 800 86 px + line 2 EB Garamond italic 72 px + an orange hairline at y 518; it builds in 0.08–0.8 s and then never moves (§5.2, §16, P-01).
2. **One 936 × 720 card, radius 40, at x 72–1008, y 568–1288,** holding the face, a term card, a dialog card or a screen recording; the rect never changes (§3.2, §16, P-03).
3. **Tracked ALL-CAPS Hinglish captions,** Space Grotesk 500, 44 px, tracking +0.10 em and wide word gaps, 2–4 words, one line, centre y 1345, a hard swap about every 0.6 s, English terms verbatim (§5.3, CS-1).
4. **Term cards and a highlight box instead of B-roll:** the named term in condensed caps 150–190 px on a white card with the presenter tile in the corner, and a 4 px orange box that slides to the field being named (§8.3 P-06…P-21, §22).
5. **The credit chip and the empty bottom band:** a hand-drawn arrow + script line + small coloured chip at y 1396–1532, shown in two windows; nothing at all below y 1536 (§16, §25, P-04).

### Style directives (non-negotiable) `[DNA]`
| # | Directive | Where it lives |
|---|---|---|
| D1 | **The frame never moves.** Title, card rect, caption slot and credit slot keep their rects (±4 px) for their whole lifetime; only the content inside the card changes. | §3.2, §16, H13 |
| D2 | **The title is a claim, not a topic label.** Line 1 names who or what is at stake, line 2 delivers the twist; it is readable by 0.9 s and stays for the whole reel (F-A). | §5.2, §6.5, H3 |
| D3 | **Name it → show it.** When a term, setting, value or tool is spoken, the card shows it within ±5 f: a term card, a highlight box on the field, or a callout on the face card. | §7.3, §8.4, H6 |
| D4 | **Hard cuts only.** No whips, flashes, slides or zoom transitions. Card content swaps, layout changes, callouts and the credit chip cut on and off. The only camera moves are 0–4 face-card pushes / pull-outs per reel (Z-2 / Z-3). | §9, §10.2, N4 |
| D5 | **One accent.** Orange (`primary`) is the only bright hue on the page, plus the small credit chip; there is no good/bad colour axis. | §4, N6 |
| D6 | **Captions are a metronome.** Every spoken word is captioned in tracked caps under the card, 2–4 words at a time, hard-swapped; captions never carry colour or emphasis. | §5.3, H11 |
| D7 | **Teach in short breaths.** The presenter speaks in 2–4-word bursts; dead air is cut; a jump cut lands every 1–3 s at the same framing (measured: no re-crop). | §7.6, §10.2, H2 |
| D8 | **The bottom band is empty.** Nothing at all below y 1536 (the creator's own reels leave ~340 px empty; this template keeps 384 px for the Instagram UI). | §3.5, H14 |

Buyer directives `BD1…` `[VAR]` are added here by the copy and may only make the style stricter.

### Quick index
| § | What | Status |
|---|---|---|
| §0 | Style profile (switches, formats F-A / F-B, themes TH-dark / TH-light) | ON |
| §1 | Procedure (with the lockup step and the field-map step) | ON |
| §2 | Hard rules, exceptions E3 + E6 | ON |
| §3 | World, layouts L-…, stage moves G-…, safe bands | ON |
| §4 | Colour, theme packs | ON |
| §5 | Type, lockup, caption profiles CS-1 / CS-2 | ON |
| §6 | Hook system (HA-05 default, HA-02, HA-04) | ON |
| §7 | Structure (tutorial), unit ritual, cadence | ON |
| §8 | Visual system: families B-1…B-9, patterns P-01…P-32 | ON |
| §9 | Transitions (hard cuts only) | ON |
| §10 | Motion tokens, camera (jump cuts + rare push / pull), layers, finishing | ON |
| §11 | Sound contract | ON (minimal) |
| §12 | Footage, shot list, fallbacks, inserts | ON |
| §13 | Output contract | ON |
| §14 | Worked examples (3) | ON |
| §15 | QA checklist | ON |
| §16 | Frame template / chrome | **ON** |
| §17 | Running state & anchors | OFF |
| §18 | Data contract | OFF |
| §19 | Evidence & citations | OFF |
| §20 | Dialogue | OFF |
| §21 | Canvas camera | OFF |
| §22 | Ink & annotation (highlight box, chevron, cursor) | **ON** |
| §23 | Continuity | OFF |
| §24 | Series furniture | OFF |
| §25 | Brand: credit chip, CTA chip, sponsor chip | **ON** |
| Parts C–F | Exceptions, personalisation, changes, IDs | — |
| App. A | Lockup bank (10 per format) | NICHE |
| App. B | Evidence map (`evidence.md`) | — |

Formats: **F-A Lesson Frame** (default) and **F-B Screen Walkthrough**.

---

## §0 Style profile `[REQ]`

```yaml
profile:                         # mirrored in tokens.json -> profile
  source_type: talking_head
  presenter: {presence: host, share: [60, 100], max_absence_s: 3.0}      # F-B: share [40, 100]
  spine: talking_head
  captions: {mode: full, role: support, mute_policy: mute_safe}
  graphics: support
  duration: {class: short, target_s: [30, 50]}
  language: {speech: en, captions: {lang: en, script: Latn, transform: verbatim}, on_screen: en, post_title: en,
             supported: [[en, en, Latn], [hinglish, hinglish, Latn], [hi, hi, Deva]]}
  numbers: {grouping: international, currency: "$", compact: none, units: metric, decimals: 0}
  tone: {energy: calm, comedy: off, comedy_max: light}
  themes: {policy: per_topic, packs: [TH-dark, TH-light], default: TH-dark}
  formats: {list: [F-A, F-B], default: F-A}
  footage_dependency: low                                                # F-B: medium
  cta: {devices: [none, follow_save_stack, comment_keyword, link_bio], placement: mid+end}
  modules: {chrome: true, running_state: false, anchors: false, data_figures: false, citations: false,
            dialogue: false, canvas_camera: false, ink: true, continuity: false, series: false, brand: true}
```

Why each value:
- **source_type: talking_head**, because every reel is one presenter's A-roll; screen material is inserted into the card (v01–v04).
- **presence: host, share 60–100 (F-B 40–100)**, because the face is on screen 62–80% in F-A-type reels (v01, v02, v04) and only 15% in v03 when the recording carried the face; this template always draws the presenter tile on term and screen cards, so the measured share runs higher.
- **spine: talking_head**, because the take is cut first and the card follows the words.
- **captions: full / support / mute_safe**, because every word is captioned (98% text-on-screen) but the captions serve the card, never carry emphasis.
- **graphics: support**, because term, dialog and screen cards take 20–90% of runtime and illustrate the words; the face carries the argument.
- **duration: short 30–50 s**, because the evidence runs 32.5–47.2 s (mean 40.1 s).
- **language: English by default; setup always asks** (English, Hinglish → romanised Hinglish ALL CAPS captions as in all four reels, Hindi → Devanagari via CS-2). English titles in every option.
- **numbers: international grouping**, because the reels write "50,000KB/S" and "100,000KB/S"; Numbers follow the language (BV-06): English → international `$` and K/M/B (unless the buyer picks ₹); Hinglish / Hindi → ₹ with Indian grouping and lakh / crore.
- **tone: calm / comedy off (max light)**, because the delivery is steady teaching; the only gag in four reels is one creator-supplied reaction clip (v01 @ 0:26).
- **themes: per_topic**, because the dark dot page carries concept reels (v01, v02, v04) and the pale grid page carries the dark-UI walkthrough (v03).
- **formats: F-A + F-B**, because v02/v04 keep the title for the whole reel while v01/v03 drop it after the hook and live in screen and card-only layouts (see Part E for this deviation from the coverage table).
- **footage_dependency: low (F-B medium)**, because F-A needs only the talking head (term cards are engine-built; screenshots optional), while F-B needs screen recordings.
- **cta: mid+end**, because the only persistent call-out is the credit chip, shown in an early and a closing window; it carries the buyer's handle or CTA.
- **modules:** `chrome` (the whole style is a fixed frame), `ink` (the highlight box), `brand` (the credit chip).

### 0.4 Formats `[DNA set; VAR enable]`
| ID | Name | When | Profile overrides | Layouts | Default hook |
|---|---|---|---|---|---|
| **F-A** | Lesson Frame | One concept, mistake, difference or rule explained to camera (most reels) | — | L-lesson, L-term-pip, L-term-full | HA-05 claim lockup (H-1) |
| **F-B** | Screen Walkthrough | Step-by-step settings, where-to-click, app walkthroughs | `footage_dependency: medium`, `presenter.share: [40, 100]`, `slots.S-title`: rect y 812–1026, lifetime `hook` | L-insert-hook, L-lesson, L-screen, L-term-pip, L-term-full, L-full | HA-02 insert hook (H-3) |

Shared DNA: the same page, the same 4:3 card rect, the same tracked caps captions in the same slot, the same highlight box, the same credit chip and the same empty bottom band. Only the title's lifetime and the card's dominant content change. Pick F-B when ≥ 50% of the script is "click here, set this, then this"; otherwise F-A.

### 0.5 Theme packs `[DNA policy; VAR colours]`
| ID | Page | Lockup / credit script | When (topic → theme) |
|---|---|---|---|
| **TH-dark** (default) | pure `#000000` with a dot grid: dots `#131313`, r 4 px, pitch 27 px (measured: 14 × 7 px rounded dashes `#121212`, pitch 29.5 × 24.7 px; the engine draws round dots); noise 0.02 | `paper` | Concepts, terms, mistakes, differences, opinions: the card mostly shows the face or term cards |
| **TH-light** | `#FBF3F1` with 1 px lines `#EDE1DE`, pitch 180 px | `ink` | Software walkthroughs whose card mostly shows dark app UI (export settings, editors, dashboards): the pale page contrasts the dark screenshots |

One theme per reel. The accent (`primary`) and the chip (`accent`) do not change between packs.

---

## §1 Procedure (follow in order) `[REQ] [DNA]`

1. **P1 Inventory.** `ffprobe` every input. Conform the talking head to 30 fps CFR. Register every screen recording and screenshot with `veos asset add --origin creator` (videos become frame folders; `ctx.videoFrame`). Note each recording's resolution: under 1080 px tall, the field text inside it is decorative only.
2. **P2 Prepare.** No matte (the style has no behind-subject type and no cut-out). Check the face sits in the upper half of the source so the 4:3 card crop keeps the head top at y 610–720.
3. **P3 Transcribe** with word timestamps. Apply `language.captions.transform` (`transliterate`: Devanagari → romanised Hinglish; English terms stay as spoken English). Fill the glossary with every tool, setting and format name spoken (e.g. "H.264", "MP4", "1080 x 1920"): these are spelled exactly.
4. **P4 Segment** into `HOOK` (first 2.5–4.5 s), `TERM-n` / `STEP-n` units (§7.3), `RULE` (the takeaway line), `CTA` (only if the buyer set one). Mark every jump-cut point on a word boundary; cut every pause > 150 ms.
5. **P5 Classify** every sentence with a line type (§8.4) and mark its **trigger word**: the term, the field, the value, the number.
6. **P6 Tone-tag** each sentence: `hype` (the claim), `explain`, `warn` (a mistake, "this is wrong"), `win` (the fixed value, the right setting), `cta`.
7. **P7 Title lockup (this style's craft step 1).** Write **3 lockups** (§6.5), two lines each, ≤ 9 words, English. Pick the one whose line 1 names the stake and whose line 2 is the twist the reel proves. Pick the hook variant H-1…H-4 (§6.2–6.3) and run the stopper tests (§6.1).
8. **P8 Visual plan.**
   - **P8a Term list:** every term the reel teaches → its card (light P-06, dark P-08, marker P-09, question P-11), its variant chips (P-07), its marker number (P-10).
   - **P8b Field map (this style's craft step 2: the screen-recording step).** For every screenshot and recording: read its frames (`veos sheet` on the asset), list each field the presenter names, and write the field's rect **in card coordinates** (and, for recordings, the local time and scroll position at which it is visible). These rects become the highlight-box keyframes (§22). A field you can't locate gets a chevron (P-17) instead of a box, never a guessed box.
   - **P8c Callouts:** every spoken number with a unit and every format or file name → P-12 / P-13 / P-14 on the face card.
   - **P8d Third-party moments** (§12.5): list them, ask once, then use the creator's file or the created substitute.
9. **P9 Beat sheet** (§13): one beat per trigger word; meet the cadence targets (§7.6); fill `slot_content` for S-card and S-credit on every beat.
10. **P10 Cue plan and transition map.** The transition map is a list of hard cuts (§9). Sound cues only on the moments §11 allows.
11. **P11 Assets.** Build the term cards and callouts as scenes; crop screenshots to the panel being discussed; resolve fallbacks FB-2…FB-5 (§12.3) and say which ones you used.
12. **P12 Checkpoint** (§13.5), then **wait for approval.**
13. **P13 Build:** act by act; `veos validate` (global checks + `validator.rules`); preview and QA (§15, at most 3 passes); render.

Module steps folded in above: `chrome` → P9 `slot_content`; `ink` → P8b field map; `brand` → P10 credit-chip windows and text (§25).

---

## §2 Hard rules `[REQ] [DNA]`

### 2.1 Editing rules (every style)
The nine editing rules in `playbooks/_global/GLOBAL-RULES.md` apply. They are directions, not limits: smooth, seamless motion; nothing overlaps by accident; keep the face clear (behind the speaker is fair game, text included); readable at a glance; one idea at a time; show what's being said; never fake facts; pace like the style, not like a timer; the style decides the look.
- **Facts the engine checks:** accidental overlaps, jumps, the face covered, unreadable text, numbers and quotes that don't match what was said, the promised count. Every count, timing and budget this playbook gives is direction for the edit, not a limit.
- **Retired (8 Oct 2026), whatever this playbook says below:** no REPRESENTATIONAL or example labels on made-up cards, no credit lines, no flash limit (flash as often as this style calls for; any "NC-11" cap below no longer applies), and text may sit behind the speaker without an exception.

### 2.2 Declared exceptions
| E-id | This style's limits (≤ registry) | DNA reason | Evidence |
|---|---|---|---|
| **E3 Quiet type** | Captions 44–53 px (default 44; measured cap height 28–31 px), weight ≥ 500, 1 line, ≤ 24 characters, contrast ≥ 7:1 (white on the black box: 21:1). Labels 28–39 px only when `redundant: true`. Display text never below 40 px. | The caption line is deliberately small and wide-tracked; at 54 px a 4-word Hinglish chunk would not fit one line at +0.10 em tracking | v02 @ 0:10 (48 px measured), v04 @ 0:18 |
| **E6 Hard swap** | Caption chunks and S-card content swap with no ease, inside containers constant to ±4 px; the containers' own first entry is at f0 (present) and their final exit is the last frame | The caption metronome and the card swaps are hard cuts by design | v02 @ 0:02.8 (face → CODEC), every caption swap |

No other exception is used: no behind-subject text (E1), no chaos burst (E2), no ambient field (E4), no edge bleed (E5).

### 2.3 Style MUST rules
- **H1. Frame 0** shows the presenter (face card, or the face card under an insert in F-B) and the first caption chunk; the lockup is readable by 0.8 s (line 2 from 0.08 s, line 1 from 0.38 s). check: V-F0
- **H2. Cadence:** 8–15 weighted state changes per 10 s (captions weigh 0.5); ≥ 5 in 0–3 s; no gap between weight-1 changes (cut, camera move, card swap, box move, callout) longer than 3.0 s (2.0 s in the hook; measured longest 3.4 s, v04 @ 0:21.5–0:24.8); nothing static > 2.5 s. check: V-CADENCE
- **H3. Lockup limits:** 2 lines, ≤ 9 words in total (line 1: 2–4 words, line 2: 3–5 words), English, read in ≤ 1.2 s; F-A: present from f0 to the last frame; F-B: present for the hook only and cut away with the hook composition. check: V-TITLE
- **H4. Payoff by 3.0 s:** the first proof in the card (term card, dialog card, screen card or a callout) lands by 3.0 s (H-1/H-2) or the insert plays from f0 (H-3). check: V-F0
- **H5. Dead air:** at most 1 gap ≥ 150 ms per 15 s; jump cuts on word boundaries ±1 f; no pause-holds. check: V-CADENCE + review
- **H6. On-the-word visuals:** term cards, highlight-box moves, callouts and chips start 2 f before their trigger word and are fully on within ±5 f. check: V-ONWORD
- **H7. Face rule:** nothing in front of the face box; callouts on the face card keep 40 px clear of it (they sit on the chest or beside the head). check: V-FACE
- **H8. Presenter presence:** share within the format's range; the presenter is never absent > 3.0 s (dark term cards and asides are ≤ 1.5 s; screen cards always carry the presenter tile). check: V-PRESENCE
- **H9. Promise integrity:** a count in the lockup ("3 settings", "Essential #3") equals the units shown; a question asked in the hook is answered on a card; a CTA keyword is on the chip ≥ 1.5 s. check: V-PROMISE
- **H10. Truth:** every number, value and setting on screen is spoken or visible in the buyer's own capture; recreated UIs are generic. check: V-INSERTS + review
- **H11. Captions:** CS-1 exactly (2–4 words, 1 line, ALL CAPS, tracking +0.10 em, hard swap, no colour, no emphasis); sync ≤ 150 ms lead; brand and tool names spelled per the glossary. check: V-CAPTION
- **H12. One accent:** ≤ 2 bright hues per frame (`primary` + the credit chip `accent`). check: V-HUES
- **H13. Chrome is fixed:** S-title, S-card, S-caption and S-credit rects never move or resize during their lifetime (±4 px). check: V-CHROME (pending engine wave E-07; review until then)
- **H14. Bands:** nothing (no text, no graphic, no presenter) below y 1536 in F-A layouts and in L-lesson / L-term-pip / L-term-full / L-screen / L-full; meaning text inside x 64–1016, y 330–1536 (L-insert-hook: y 140–1536). check: V-SAFE
- **H15. Camera:** jump cuts keep the framing (Z-1); at most 3 Z-2 pushes and 2 Z-3 pull-outs per reel, never in the hook, never twice the same in a row, only in L-lesson; no punch, shake or rotation. check: V-CAMERA
- **H16. Spelling:** romanised Hinglish follows the creator's own spelling and stays consistent inside a reel; English words, tool names, formats and numbers are exact. check: V-CAPTION + review
- **H17. Audio:** −14 LUFS integrated, true peak ≤ −1.5 dBTP, hard end ≤ 6 f after the last word (NC-8). check: QA
- **H18. Determinism:** every frame is a function of its index; no CSS animation in scenes; recordings play through `ctx.videoFrame`. check: NC-9 + review

H-TB text-burden rule: n/a (captions are `full`).

### 2.4 NEVER
- **N1.** No transition effects: whips, flashes, light leaks, glitches, zoom-throughs, slides, morphs between layouts, crossfades.
- **N2.** No punch or shake presets (snap-punch, crash-zoom, shake, rotation-snap, zoom-through), no re-crop alternation on jump cuts. Z-2 / Z-3 only.
- **N3.** No coloured, bold, glowing or enlarged words inside captions; no karaoke; no emoji in captions or in the lockup.
- **N4.** No second title, banner, slab or sticker over the frame. The lockup is the only headline.
- **N5.** No B-roll montages, stock footage, AI scenes or decorative clips. An aside (P-26 / P-27) is ≤ 1.5 s, in the card, and says the line.
- **N6.** No more than one bright hue + the chip; no red/green verdict colours; no gradients beyond the hairline.
- **N7.** No text or graphic in the bottom 384 px (y > 1536), in the top 330 px of F-A frames, or over the face.
- **N8.** No readable code, logs or long paragraphs as the point of a card; a screenshot's small text is decorative and the box + caption carry the meaning.
- **N9.** No fake settings presented as real: a recreated panel is generic, uses only the values the presenter says.
- **N10.** No fetched logos, app icons, film clips, memes or other creators' footage (NC-7). Creator-supplied files or created substitutes only.
- **N11.** No highlight box guessed onto a field you didn't locate in the field map; no two boxes at once.
- **N12.** No card content that changes without a spoken trigger (no "filler" swaps).
- **N13.** No moving, resizing or fading of the card rect itself, and no title animation after 0.83 s.
- **N14.** No black tail > 0.2 s; no outro card.

Buyer NEVER items `BN1…` `[VAR]` are added here by the copy.

---

## §3 World, layouts, stage moves, safe zones `[REQ] [DNA; coordinates TUNE ±5%]`

### 3.1 World
| ID | Kind | Look | Carries | Enter / exit |
|---|---|---|---|---|
| **W-page** | `canvas` | TH-dark: `#000000`, dot grid (`#131313`, r 4, pitch 27; real 14 × 7 px dashes at 29.5 × 24.7), noise 0.02. On pure black the caption's black box is invisible, as in the reference. TH-light: `#FBF3F1`, 1 px grid lines `#EDE1DE`, pitch 180. No vignette, no glow | Everything: the frame is printed on it | Present from f0 to the end; the theme never flips inside a reel |

The page shows wherever the stage doesn't: above and below the card, around the presenter tile, behind L-term-full. In L-full the footage covers it.

### 3.2 Layout library
| ID | Engine | Presenter rect | Graphic rect | Caption | Treatment | Share F-A | Share F-B |
|---|---|---|---|---|---|---|---|
| **L-lesson** | `card` | x 72, y 568, 936 × 720, radius 40, crop 4:3, face 0.30, eye 0.40, shadow 0.25 | — (the card is the presenter) | fixed y 1345 | none | 50–80% | 10–40% |
| **L-term-pip** | `card` | tile x 700, y 948, 288 × 320, radius 28, face 0.42, shadow 0.30 | x 72, y 568, 936 × 720 (the term card scene fills it) | fixed y 1345 | none | 15–45% | 0–30% |
| **L-term-full** | `hidden` | — | x 72, y 568, 936 × 720 (dark term card) | fixed y 1345 | — | 0–12% | 0–10% |
| **L-insert-hook** | `card` | x 72, y 1080, 936 × 720, radius 40, crop 4:3 | insert x 72, y 150, 936 × 610 | hidden | none | — | 0–12% |
| **L-screen** | `card` | tile x 92, y 968, 300 × 300, radius 28, face 0.42 | x 72, y 568, 936 × 720 (the recording) | fixed y 1345 | none | — | 40–85% |
| **L-full** | `full` | full frame | — | fixed y 1210 (S-caption-full) | none | — | 0–35% |

Layout schedule: a F-A reel alternates L-lesson ↔ L-term-pip/L-term-full on term words; a run of L-lesson lasts 1.5–8 s, a term card 1.0–6.5 s. A F-B reel runs L-screen for each step (3–12 s) and returns to L-lesson or L-full for the rule lines (1.5–6 s).

### 3.3 Stage moves (all cuts)
| ID | Move | Recipe | Use |
|---|---|---|---|
| **G-1** | Card content cut | `stage.via: cut` between L-lesson and L-term-pip / L-term-full / L-screen on the trigger word (−2 f). The S-card rect is identical before and after; only its content changes | Every term, field or step |
| **G-2** | Composition cut | F-B only: at the end of H-3, one hard cut from L-insert-hook (insert + lockup + face card) to L-screen or L-lesson; the insert and the lockup end on that frame | Hook → body in F-B |
| **G-3** | Full-bleed cut | F-B only: `via: cut` L-lesson ↔ L-full; the caption moves to S-caption-full, the credit to S-credit-full | A personal aside or a rule line said with energy (v01 pattern) |
| **G-4** | Jump cut | A cutmap jump cut at the same framing (Z-1, §10.2); callouts cut on or off with it | Every 1–3 s inside L-lesson and L-full |
| **G-5** | Tile hold | The presenter tile stays at its rect while term cards and dialog cards swap above it (no tile move between consecutive L-term-pip beats) | Consecutive term / dialog cards |

Never use `panel-drop`, `pop-back`, `shrink-to-card`, `grow-from-card`, `slide-*`, `pip-*`, `morph`, `dim` or `fade-through` (N1).

### 3.4 Layout diagrams
**L-lesson (F-A, the frame for ~65% of the reel)**
```
┌──────────────────────────────┐ 0
│        (empty page)          │ ← y 0-330: nothing (IG top UI + air)
│      95% Creators            │ ← line 1 cy 378, Inter Tight 800 86 px
│  don't know this difference  │ ← line 2 cy 466, EB Garamond italic 72 px
│   ───────═══════───────      │ ← hairline y 518, x 130-950
│ ╭──────────────────────────╮ │ ← S-card y 568
│ │                          │ │
│ │   presenter (4:3 crop)   │ │   x 72-1008, radius 40
│ │   head top y 610-720     │ │
│ ╰──────────────────────────╯ │ ← y 1288
│      KOI BHI SOFTWARE        │ ← S-caption cy 1345 (44 px caps, +0.10 em)
│   ↖ lessons by               │ ← S-credit y 1396-1532 (windows only)
│        [ @yourhandle ]       │
│        (empty band)          │ ← y 1536-1920: nothing
└──────────────────────────────┘ 1920
```
**L-term-pip (term / dialog card with the presenter tile)**
```
│ ╭──────────────────────────╮ │ y 568
│ │  (Essential #2)          │ │ ← pill x 112, y 600 (P-10)
│ │        CODEC             │ │ ← term word cy 720, Anton 170 px, termink + shadow
│ │  H.264   H.265           │ │ ← variant chips row y 880, x from 148
│ │                 ╭──────╮ │ │
│ │                 │ tile │ │ │ ← presenter tile x 700-988, y 948-1268, r 28
│ ╰─────────────────┴──────┴─╯ │ y 1288
│            H.265             │ ← caption cy 1345
```
**L-insert-hook (F-B hook, ≤ 4.5 s)**
```
│ ╭──────────────────────────╮ │ y 150   S-insert: 16:9 clip or phone mock (P-23 / P-24)
│ │        insert            │ │
│ ╰──────────────────────────╯ │ y 760
│   Best Export Settings       │ ← line 1 cy 862
│     for Instagram reels      │ ← line 2 cy 948, hairline y 1000
│ ╭──────────────────────────╮ │ y 1080  face card 936 × 720 (bleeds into the lower band:
│ │        presenter         │ │          presenter only, no text; this layout only)
│ ╰──────────────────────────╯ │ y 1800
```
**L-screen (F-B steps)**
```
│        (empty page, no title)│ y 0-568
│ ╭──────────────────────────╮ │ y 568   the recording, cropped to the panel (P-19 / P-20)
│ │  Format  [ MP4      v ]  │ │ ← orange box on the named field (P-16)
│ │╭──────╮ Codec [H.264  v] │ │
│ ││ tile │                  │ │ ← presenter tile x 92-392, y 968-1268
│ ╰┴──────┴──────────────────╯ │ y 1288
│        FORMAT MP4 RAKHO      │ ← caption cy 1345 (box visible on TH-light)
```
**L-full (F-B asides)**
```
│ full-bleed presenter         │
│                              │
│     [ AB TUM LOG JAB BHI ]   │ ← S-caption-full cy 1210, black box
│   ↖ lessons by [@handle]     │ ← S-credit-full y 1262-1398
│                              │
```

### 3.5 Safe zones and bands
| Band | y | Content |
|---|---|---|
| Top empty | 0–330 | Nothing in F-A (in F-B the insert may start at y 150 during the hook only) |
| Title | 330–544 | S-title (F-A); empty in F-B after the hook |
| Card | 568–1288 | S-card |
| Caption | 1313–1377 | S-caption (centre 1345) |
| Credit | 1396–1532 | S-credit, in its windows; empty otherwise |
| Bottom empty | 1536–1920 | Nothing (NC-5 needs y > 1540 free of meaning text; this style keeps the whole band empty) |

Meaning text stays inside x 64–1016. The right IG button column (x > 970, y 900–1540) only ever holds the card's right edge (x 1008) and the presenter tile, never text.

### 3.6 Presenter rules `[COND: presence ≠ none]`
- Share: F-A 60–100%, F-B 40–100%; longest absence 3.0 s (L-term-full and asides only).
- Return: always by a hard cut back to L-lesson (or L-full in F-B).
- Crops: L-lesson head top at y 610–720, eyes at 40% of the card height (y ≈ 856); L-term-pip / L-screen tile: face height 42% of the tile, head top 10–30 px below the tile top; L-full: head top y 150–330, never under the caption box.
- Nothing ever sits behind the head (no E1); the lockup is above the card, so the face and the title never meet.

---

## §4 Colour, themes `[REQ] [meanings DNA; brandable hex VAR]`

### 4.1 Role palette
| Role | Hex | One job | Text on it | Contrast | Brandable |
|---|---|---|---|---|---|
| `primary` | `#F59E0B` (BV-02 colour 1) | The accent: title hairline, highlight box on dark UI, the warm first line of a dark term card | `ink` | 8.9:1 | **yes** |
| `accent` | `#1E7A3A` (BV-02 colour 2) | Credit chip fill | `paper` | 5.4:1 | **yes** |
| `ink` | `#0F0F0F` | Text on white cards and on the light page | — | — | no |
| `paper` | `#FFFFFF` | Lockup on the dark page, caption text, white term cards | — | — | no |
| `night` | `#000000` | TH-dark page | — | paper 20:1 | no (TUNE) |
| `canvas` | `#FBF3F1` | TH-light page | — | ink 18:1 | no (TUNE) |
| `grid` | `#1C1C1C` (role; the TH-dark dots use `#131313`) / `#EDE1DE` (light lines) | Page texture | — | — | no |
| `charcoal` | `#2A2A2E` | Dark term card fill | `paper` / `primary` | 14:1 / 6.7:1 | no (TUNE) |
| `termink` | `#2B2B2E` | Term word and pill text on white | — | 14:1 on white, 8.2:1 on the pill | no (TUNE) |
| `mute` | `#6B6B70` | Second tone of a variant chip ("Apple **Pro Res**") | — | 5.3:1 on white | no (TUNE) |
| `pill` | `#E4E4E7` | Essential #N marker pill fill | `termink` | 8.2:1 | no (TUNE) |

Gradient: `hairline` only (transparent → `#E08A1E` → `#F5B04A` → `#E08A1E` → transparent, left to right).

### 4.2 Meanings
- **Orange = "this one":** the field being named, the state that matters ("AUTOMATIC"), the line under the claim.
- **The chip colour = the creator's mark:** handle, keyword or tool credit; nothing else uses it.
- **White card = definition; charcoal card = verdict or announcement** ("THIS IS WRONG", "FORMAT").
- There is no bad/good axis and no colour for comparisons: comparisons are made by sequence and position (P-30), never by red vs green.
- Brand colours of tools appear only inside the creator's own screenshots and recordings.

### 4.3 Theme packs `[COND: themes ≠ single]`
As §0.5. Topic → theme rule: **TH-light when the card shows dark app UI for ≥ 40% of the reel (F-B walkthroughs of editors, exporters, dashboards); TH-dark otherwise.** Both packs keep `primary` and `accent`. The highlight box is `primary` (orange) on TH-dark and `paper` (white) on TH-light, always over dark UI (v02 orange, v03 white); over a light UI (a white settings sheet) it is `ink` in both packs. On TH-light the caption box (black) becomes visible as a box, which is intended (v03).

### 4.4 Grades: OFF (the footage is not graded; match only exposure and white balance between takes).

### 4.5 Rules
- `max_bright_per_frame: 2` (`primary` + `accent`).
- Coloured text exists only as the first line of a dark term card (orange on charcoal, 6.7:1) and the chip label; both pass 4.5:1.
- Footage is not regraded. Screenshots are not recoloured.
- **Must match `tokens.json`.**

---

## §5 Type & caption system `[REQ]`

### 5.1 Font map `[slots DNA; families TUNE within the class]`
| Slot | Family | Weight / style | Font class (TUNE boundary) | Used for |
|---|---|---|---|---|
| `display` | **Inter Tight** | 800, tracking −0.02 em | neo-grotesk sans 700–900, tight | Lockup line 1 |
| `serif` | **EB Garamond** | 500 italic | book serif with a true italic | Lockup line 2 |
| `body` | **Space Grotesk** | 500, ALL CAPS, +0.10 em | geometric / tech sans 400–600 | Captions |
| `numeric` | **Anton** | 400 | condensed heavy caps | Term words, number and keyword callouts, dark term cards |
| `ui` | **Inter Tight** | 500–700 | neutral sans | Variant chips, question cards, Essential pill, credit chip |
| `marker` | **Permanent Marker** | 400 | hand-drawn marker | Brush term word (P-09), credit script line |
| `deva` | **Noto Sans Devanagari** | 600 | Devanagari sans | Captions when BV-05 picks Devanagari (CS-2) |

All bundled (`assets/fonts`). The creator's evidence used Inter + a Newsreader-like italic + Space Grotesk + Bebas-like condensed + a thin handwriting; the closest bundled faces are listed above. The handwriting credit line uses **Caveat** (slot `script`); Permanent Marker stays for the brush term word.

### 5.2 Headline element: the title lockup `[DNA recipe; NICHE text]`
| Property | Spec |
|---|---|
| Kind / lifetime | `lockup`; F-A lifetime `video` (f0 → last frame); F-B lifetime `hook` (ends with G-2) |
| Line 1 | Inter Tight 800, **86 px** (TUNE 78–94), tracking −0.02 em, centred, cy **378**; `paper` on TH-dark, `ink` on TH-light; 2–4 words, Title Case, may start with a number ("95% Editors") |
| Line 2 | EB Garamond italic 500, **72 px** (TUNE 64–80), centred, cy **466**; same colour as line 1; 3–5 words, sentence case |
| Hairline | y **518** (measured 514–521), x 170–900 (measured 175–892), 3 px core + 8 px glow (`hairline` gradient, `primary` 60% glow), fading to transparent at both ends |
| Box | none: no fill, no stroke, no shadow, no rotation |
| F-B position | line 1 cy 862, line 2 cy 948, hairline y 1000 (S-title rect y 812–1026) |
| f0 behaviour | f0: nothing of the lockup yet (the face card and caption are already up). **f2–3 (0.08 s):** line 2 reveals **left to right** as a soft-edged wipe (≈ 60 px feather) with blur 8 → 0 px, over 6 f (expo-out); the hairline draws left to right with it, 6 f (v02 @ 0.12–0.25 s, full-rate strip). **f11–12 (0.38 s):** line 1 reveals left to right **character by character** (≈ 1 f per character), each character blur 8 → 0 and grey → white over 4 f; the first word is legible by f14. **f22–24 (0.75–0.8 s):** settled and fully readable (v02 @ 0.72 s). F-B H-3 may start line 1 at f0 (v03) |
| Life | None. No pulse, no flip, no underline wipe, no colour change after f24 |
| Exit | F-A: none. F-B: hard cut with the hook composition (G-2) |
| Limits | 2 lines exactly, ≤ 9 words, ≤ 26 characters per line, English (`on_screen: en`), no emoji, no chips, no CAPS words except acronyms |
| Text class | `TC-display`; the scene declares `kind: "lockup"`, `text_content` = both lines |

### 5.3 Caption system profiles `[DNA mechanics; fonts TUNE; language VAR]`
**CS-1 (default, Latin script)**, `extends: lib:editing_explained`:

| Group | Value |
|---|---|
| Mode | `full`, `support`, `mute_safe` |
| Chunking | `group`, 2–4 words (mean ≈ 2.8), 1 line, ≤ 24 characters; never split a name, number or unit ("1080 X 1920", "H.264"); a pause ≥ 0.6 s always breaks; sentence ends break |
| Timing | lead 1 f; min hold 0.15 s per word (a chunk lives ≈ 0.4–0.9 s, ≈ 0.6 s typical); swap **hard** (E6); during a pause the last chunk holds ≤ 0.4 s, then hides |
| Skin | Space Grotesk 500, **44 px** (TC-subtitle under E3; TUNE 44–53; measured cap height 28–31 px ≈ 43 px; the real face is a squarer tech sans, Saira/Exo-like, of which Space Grotesk is the closest bundled font; word gaps are visibly wide, about 2 spaces), **ALL CAPS**, tracking **+0.10 em**, `#FFFFFF`, no stroke, no shadow, line height 1.1; container **box**: `#000000` 100%, radius 0, padding 6 / 14 px (invisible on the dark page, a visible black box on TH-light and on L-full footage) |
| Position | `fixed_y` cy **1345** in L-lesson, L-term-pip, L-term-full, L-screen; cy **1210** in L-full; centred, max width 952; `avoid_face` on (only matters in L-full) |
| Emphasis | **none** (DNA): no colour, weight or size change on any word |
| Variants | karaoke / two-tier / duet / stack: none |
| Hide rules | hidden during L-insert-hook (H-3 hook); hidden under a z8 scene (none planned); **not** hidden under a dark term card even when it repeats the words (v04 @ 0:37.0 "THIS IS WRONG" card + the same caption) |
| Language | romanised Hinglish in Latin script, ALL CAPS; English words kept as spoken ("CODEC H.264", "FRAME REORDERING AAPNE"); the creator's romanisation is kept, consistent within the reel; numbers as digits without grouping ("50000 KBPS"); glossary terms exact; profanity masked `inner` (S**T), on by default |

**CS-2 (Devanagari)**, chosen automatically when BV-05 sets `hi / Deva`: identical except Noto Sans Devanagari 600, 50 px, case `as_spoken` (Devanagari has no capitals), tracking 0, line height 1.25. English terms stay in Latin script inside the chunk.

### 5.4 Other text systems
| Element | Class | Recipe | Hold |
|---|---|---|---|
| Term word (white card) | TC-display | Anton 150–190 px (170 default), `termink`, soft shadow 0 10 18 rgba(0,0,0,.28), centred at card x 540, cy 720 (or y 640 when a pill or strip sits under it); 1 word or 1 token (".MOV", "H.264"); ≤ 9 characters at 190 px, ≤ 12 at 150 px | the card's span (≥ 1.0 s) |
| Dark term card text | TC-display | Anton 140–180 px, 1–3 words on ≤ 2 lines, centred at card centre (540, 928); line 1 `primary` when it names the state ("AUTOMATIC"), line 2 `paper` ("HOTA HAI"); or both `paper` ("THIS IS / WRONG"); text shadow 0 6 16 rgba(0,0,0,.5) | 0.8–1.5 s |
| Brush term word | TC-display | Permanent Marker 140–160 px, `ink`, left-aligned at x 112, cy 690 | the card's span |
| Variant chips | TC-label | Inter Tight 500, 56 px, `ink`, plain text (no pill), row at y 880, starting x 148, 48 px gaps; a two-tone chip writes the family in `ink` and the variant in `mute` ("Apple **Pro Res**") | until the card leaves |
| Question card | TC-display | Inter Tight 600, 78 px, line height 1.0, `ink`, 2 lines, centred at x 540, top y 690 | 1.0–2.0 s |
| Essential pill (SM-1) | TC-label | Inter Tight 600 italic, 40 px, `termink` on `pill`, radius 26, padding 6 / 22, at x 112, y 600 | the card's span |
| Number on card | TC-display | Anton 190 px (170–210), `paper`, shadow 0 6 20 rgba(0,0,0,.45), number + unit glued ("50,000KB/S"), centred, baseline y 1252 (36 px above the card bottom) | ≥ 0.8 s, to the end of the phrase |
| Number beside head | TC-label | Anton 64 px number + Anton 44 px note under it ("BHI NI CHAHIYE"), `paper`, right edge 36 px inside the card on the side away from the face | ≥ 0.8 s |
| Keyword on card | TC-display | Anton 110–140 px, `paper`, shadow as above, baseline y 1252 | ≥ 0.8 s |
| Credit script | TC-legal | Permanent Marker 34 px, `paper` (TH-dark) / `ink` (TH-light), baseline y 1468, x 452 | its window |
| Credit chip | TC-legal | Inter Tight 700, 28 px, `paper` on `accent`, radius 6, padding 4 / 14, top-left at x 560, y 1486 | its window |

### 5.5 Language and number rules
- Captions: romanised Hinglish, ALL CAPS, the creator's spelling (from `script.md` when given; else the transliteration), consistent inside the reel. English words and brand names exact (glossary).
- Lockup, term cards, chips, question cards: **English** (Title Case line 1; sentence case line 2 and question cards; ALL CAPS term words). A Hinglish term card is allowed only for a spoken verdict ("HOTA HAI", "BHI NI CHAHIYE").
- Numbers: callouts use international grouping and glue the unit ("50,000KB/S", "1080 × 1920", "30 FPS"); captions keep digits ungrouped as spoken ("50000 KBPS"). With BV-06 Indian grouping, rupee amounts become "₹1,20,000".
- Devanagari (CS-2): no ALL CAPS, no tracking; Latin terms stay Latin.
- The ₹, ×, ✓ and ≠ glyphs are pre-painted (warm-up) before use.


---

## §6 Hook system `[REQ]`

### 6.1 Stopper tests (run on f0 and on 0–3 s)
| ID | Test | This style's number |
|---|---|---|
| ST-1 | Thumbnail: the frame at 0.8 s at 25% scale shows the claim | Lockup line 1 = 21.5 px at 25% (readable); the face card visible |
| ST-2 | Mute: the first 3 s tell the story without sound | The lockup states the claim; captions carry the spoken question; the first card proves it by 3.0 s |
| ST-3 | Motion at f0 | Live talking-head footage in the card at f0 (and the insert clip playing in H-3) |
| ST-4 | Read time | Lockup ≤ 9 words, readable in ≤ 1.2 s, complete by 0.8 s |
| ST-5 | Change count | ≥ 5 weighted SCs in 0–3 s (typically 5 caption swaps × 0.5 + lockup line 2 + line 1 + 1 jump cut + the first card swap ≈ 6.5) |
| ST-6 | Payoff-by | Lockup readable by 0.8 s (HA-05); first proof card by 3.0 s |

This style does **not** use a result-first stopper. The stopper is the claim itself, read in a quiet, premium frame while the presenter is already mid-sentence and gesturing. The tests above replace "≥ 10 changes in 3 s".

### 6.2 Default archetype: HA-05 Claim lockup, hook **H-1** (F-A) `[DNA]`
Spoken pattern: a direct address that sets up the claim, mid-sentence from f0 ("Chahe tum koi bhi software use karte ho, tumne hamesha dekha hoga…"). The lockup states the stake; the first term card lands on the first term (v02).

| t | Visual | Caption (CS-1) | Layout / camera | Cue moment (§11) |
|---|---|---|---|---|
| **f0** | Dark page; face card (L-lesson) already playing, presenter mid-word, looking at the lens; no lockup yet | First chunk already on ("CHAHE TUM") | L-lesson, crop 1.00 | — |
| 0.08 (f2–3) | Lockup line 2 wipes in left to right with blur (6 f); the hairline draws with it | (same) | — | — |
| 0.38 (f11–12) | Line 1 reveals character by character (≈ 1 f each) | — | — | — |
| 0.50 | Second chunk; a natural gesture toward the lens (OK sign, point) | "KOI BHI SOFTWARE" | — | — |
| 0.8 (f24) | Lockup settled | — | — | — |
| 1.0–1.6 | Jump cut on the next breath (same framing); the caption swaps 1 f after the cut | "USE KARTE HO" | Z-1 jump cut | — |
| 1.6–2.7 | Presenter points down toward the card / looks down; jump cut | "TUMNE HAMESHA" → "DEKHA HOGA" | Z-1 jump cut | — |
| **2.7–3.0** | **First term card:** hard cut (G-1) to the white term card with the term word ("CODEC"), presenter tile bottom-right | the term alone ("CODEC") | L-term-pip via cut | reveal (the card) |
| 3.0–9.0 | Variant chips pop one per spoken variant (P-07), then the dialog card (P-15) with the highlight box | "H.264" → "H.265" → … | — | reveals (≤ 1 per 2 s) |

### 6.3 Allowed alternates `[DNA list; VAR choice per reel]`
**H-2 Question lockup (HA-05 variant):** the presenter asks the viewer a direct question; the lockup names the mistake; the answer lands as a marker term card (v04).

| t | Visual | Caption | Layout / camera |
|---|---|---|---|
| f0 | Face card, presenter glancing down, mid-word | "MERA EK" | L-lesson 1.00 |
| 0.17–0.67 | Lockup builds (line 2 first) | "QUESTION HAI" → "TUM LOGON SE" | — |
| 1.2 | Jump cut (same framing); index finger points at the lens (the gesture fills the card) | "MUJHE HONEST ANSWER KARNA" | Z-1 jump cut |
| 2.17 | Jump cut | "SEARCH NA KARNA" | Z-1 |
| 2.83 | Last breath of the question | "GOOGLE PE" | — |
| **3.0** | **Answer card:** white card, Essential pill ("Essential #3"), brush term word ("Bit Rate"), a strip of the settings panel with the orange box drawing on the field (P-09) | the next chunk | L-term-pip via cut |

[NICHE: example] Money: "Mera ek question hai… credit card ka bill aata hai toh tum kitna pay karte ho?" → answer card "Essential #1 / Minimum Due". Creator tools: "Ek question… tum video kis bitrate pe export karte ho?" → answer card "Essential #2 / Bit Rate".

**H-3 Insert hook (HA-02 Headline + proof): default for F-B** (v03, v01).

| t | Visual | Caption | Layout / camera |
|---|---|---|---|
| **f0** | L-insert-hook: the insert already playing in S-insert (a 16:9 clip of the creator's result, or a phone mock looping their own reel or app screen, P-23 / P-24); face card below; lockup line 1 starting at mid-frame | hidden | L-insert-hook |
| 0.17–0.67 | Lockup line 2 + hairline in; line 1 complete | hidden | — |
| 0.8–1.0 | The insert swaps to its second clip or screen (hard) | — | — |
| 1.6–1.9 | The insert swaps again (third screen: e.g. the app's export screen) | — | — |
| **2.7–4.3** | **Composition cut (G-2):** the insert and the lockup end; the reel continues in L-screen (the first step) or L-lesson; captions start on this frame | first chunk | L-screen / L-lesson via cut |

[NICHE: example] Creator tools: the phone mock plays the creator's own reel, then their editor's export screen, then the upload screen; lockup "Best Export Settings / for Instagram reels". Money: a 16:9 insert of the creator's own banking-app screen recording (redacted, NC-14) scrolling to the "Statement" tab; lockup "Read Your Statement / like a banker".

**H-4 Term first (HA-04 Topic build):** the term card is in the card at f0, the presenter tile in its corner; used when the term itself is the hook ("HDR", "CIBIL"). Derived from the term-card timing of v02 @ 0:02.8 and v04 @ 0:03, moved to f0.

| t | Visual | Caption | Layout |
|---|---|---|---|
| f0 | White term card with the term word settled, presenter tile talking | first chunk | L-term-pip |
| 0.17–0.67 | Lockup builds | — | — |
| 0.9–1.8 | 1–2 variant chips pop on their words | — | — |
| 1.8–2.4 | Hard cut to the face card (L-lesson) for the claim line | — | L-lesson via cut |
| 2.4–3.0 | Jump cut on the next breath | — | Z-1 |

[NICHE: example] Money: "CIBIL" card at f0, chips "300" and "900" on "300 se 900 tak". Creator tools: "HDR" card at f0, chips "10-bit" and "HLG".

### 6.4 Hook pairs by topic `[NICHE]` (pair type: claim → proof in the card)
| Topic | Claim (lockup) | Proof visual in the card | By |
|---|---|---|---|
| [NICHE: example] Credit-card minimum due | "This Mistake is / costing you interest" | P-09: "Essential #1" + brush "Minimum Due" + a strip of the creator's own bill screenshot with the box on "Minimum Amount Due" | 3.0 s |
| [NICHE: example] SIP vs lump sum | "90% Investors / mix up these two" | P-06 "SIP" with chips "monthly" and "auto-debit", then P-06 "LUMP SUM" | 2.8 s |
| [NICHE: example] UPI Lite | "Your UPI App / has a hidden mode" | P-06 "UPI LITE", chips "no PIN" and "small payments" | 2.8 s |
| [NICHE: example] Export settings for reels | "Best Export Settings / for Instagram reels" | H-3: phone insert of the creator's reel → L-screen with the box on "Resolution" | f0 / 2.7 s |
| [NICHE: example] HDR vs SDR | "95% Creators / don't know this difference" | P-06 "HDR" with chips "10-bit" and "HLG"; later P-06 "SDR" | 2.8 s |
| [NICHE: example] Shooting reels in 4K | "Stop Shooting 4K / for your reels" | P-08 dark card "4K ≠ / BETTER", then the camera-settings screenshot with the box on "1080p · 30" | 2.9 s |

The editor writes this row per reel at P7 and appends it to the buyer's copy (Part D.3).

### 6.5 Lockup writing `[DNA formula; NICHE examples]`
**Formula:** line 1 = **the stake** (who or what, 2–4 words, Title Case: a share "95% Editors", a superlative "Best Render Settings", a gate "Only Pro Editors", "This Mistake is") + line 2 = **the twist** (3–5 words, sentence case: what they don't know or what it does, "don't know this difference", "ruining your video", "use this kind of subtitle", "for social media"). Read together, the two lines are one sentence.

| Template | Line 1 | Line 2 |
|---|---|---|
| Share | "[N]% [People]" | "don't know this difference" |
| Mistake | "This Mistake is" | "ruining your [thing]" |
| Gate | "Only Pro [People]" | "use this kind of [thing]" |
| Best | "Best [Thing] Settings" | "for [platform / use]" |
| Hidden | "Your [Tool]" | "has a hidden [feature]" |
| Stop | "Stop [doing X]" | "for your [goal]" |

- English always (`on_screen: en`), even when the speech and captions are Hinglish.
- No emoji, no chips, no CAPS words (acronyms excepted), no exclamation or question marks.
- A number in line 1 must be true or clearly the creator's own spoken estimate ("95%" only if they say it).
- **Write 3 and pick by ST-1 and ST-4.** Banned: vague hype ("Game changer", "Mind-blowing"), a claim the reel doesn't prove, more than 9 words.

### 6.6 Hook sound
See §11: the hook may carry one cue on the first card reveal (H-1, H-2, H-4) or on the composition cut (H-3). No cue at f0. The bed enters after the hook.

### 6.7 CTA `[DNA device set; VAR values]`
| Device | Spoken pattern | On screen (the W2 credit chip) | Hold | Where |
|---|---|---|---|---|
| `none` (default) | none | script "lessons by" + chip = the handle (BV-01), in both windows | its windows | early + end |
| `follow_save_stack` | "Aise aur lessons ke liye follow kar lo" (last sentence) | script "follow for more" + chip = the handle | ≥ 1.5 s, to the end | end |
| `comment_keyword` | "Comment karo [KEYWORD], main bhej dunga" | script "comment" + chip = the keyword (BV-08) (P-31) | ≥ 1.5 s, to the end | end |
| `link_bio` | "Poori guide link in bio" | script "full guide" + chip "link in bio" | ≥ 1.5 s | end |

This copy's values: handle `{{BV-01.handle|@yourhandle}}`, CTA device `{{BV-08.device|none}}`, keyword `{{BV-08.keyword|KEYWORD}}` (used only with `comment_keyword`). No CTA graphic ever enters the card, and there is no end card (N14). The last 1.0 s before the CTA sentence carries no cue.

---

## §7 Structure & cadence `[REQ] [DNA]`

### 7.1 Structure type: `tutorial` (both formats)
- **F-A:** claim (lockup + hook) → term 1 (name → show where → rule) → term 2 … (1–4 terms) → the rule or verdict → (CTA line).
- **F-B:** insert hook → step 1 … step N (each: name the field → box on it → say the value) → closing rule on the face card → (CTA line).

### 7.2 Markers
- **SM-1 Essential pill:** "Essential #N" (Inter Tight 600 italic 40 px, `termink` on `pill`, radius 26) at the top-left of the term card (x 112, y 600), only when the reel is part of a numbered set of essentials or the lockup promises a count. Numbering ascending. When the reel teaches one idea, markers are `none (spoken only)`.
- F-B steps are not numbered on screen; the caption and the box carry the step.
- No recap card, no teaser chips.

### 7.3 Unit ritual (every term in F-A, every step in F-B)
| Step | Frames | What |
|---|---|---|
| **U-1 Name** | trigger −2 f | Hard cut (G-1) to the term card: white P-06 (definition), marker P-09 (the essential), dark P-08 (verdict or announcement), question P-11 (a turn). The caption shows the term alone when it is spoken alone |
| **U-2 Unpack** | +8 f → card end | Variant chips pop one per spoken variant (P-07), each on its word, ≥ 0.6 s apart; ≤ 4 chips |
| **U-3 Show where** | the field word −2 f (the box: −12 f) | Cut to the dialog card (P-15) or the screen card (P-19); the highlight box traces on the field (14–16 f, from ≈ 12 f before the word) and slides to each next field on its word (7 f) |
| **U-4 Rule** | the rule line | Cut back to the face card (L-lesson); jump cuts every 1–3 s; a late rule or verdict line may carry one Z-2 push or Z-3 pull-out |
| **U-5 Number** | the number word −2 f | A number or keyword callout on the face card (P-12 / P-13 / P-14), cut on with a jump cut (no animation), off on the next cut, holds ≥ 0.8 s |

A unit lasts 4–14 s. U-2, U-3 and U-5 are used only when the speech has variants, a place and a number.

### 7.4 Open loops and re-hooks
- **Question loop (H-2):** a question in the first 3 s is answered by the next card, by 3.0 s.
- **Count loop:** a lockup or spoken count ("3 settings") is paid by that many units; the Essential pill numbers them.
- **Deliverable loop:** only with `comment_keyword`.
- Re-hooks: none (`short` class). The intro (hook ≤ 4.5 s) stays ≤ 15% of runtime.

### 7.5 Rhythm and energy curve
Flat and steady, slightly rising: the hook (claim) → units at an even pace → the verdict on a dark term card or a callout (the only peak) → a calm last line on the face card. No entertainment beats (comedy `off`). With BV-11 = `light`: one P-27 reaction insert ≤ 1.2 s per reel, never in the hook or the last 3 s.

### 7.6 Cadence (state changes)
| Token | Value | Why |
|---|---|---|
| `sc_per_10s` | **[8, 15]** | Caption swaps every ~0.6 s (×0.5) + jump cuts every 1–3 s + card swaps and box moves (v02 @ 0:00–0:18) |
| `hook_sc_3s` | **5** | v02 0–3 s ≈ 6.5 weighted |
| `max_gap_s` | **3.0** (hook **2.0**) | Weight-1 events only (cuts, camera moves, card swaps, box moves, callouts); caption swaps don't fill gaps. Measured longest talking run without one: 3.4 s (v04 @ 0:21.5) |
| `max_static_s` | **2.5** | Live footage and recordings (`kind: "video"`) count as continuous motion |
| `caption_weight` | **0.5** | Support captions |
| `cuts_per_min` | null | Not DNA: the card swaps carry the rhythm |

V-CADENCE computes all of these from the timeline.

---

## §8 Visual system `[REQ]`

### 8.1 Graphics role and budget
`graphics: support`. Term, dialog and screen cards fill 20–45% of an F-A reel and 50–90% of an F-B reel. 32 patterns. ≥ 4 families per 40 s. **Numbers become callouts, not charts:** a spoken value with a unit appears on the face card (P-12) or on its field in a screenshot (P-16); this style never draws bars, counters or crowds.

### 8.2 Families
| ID | Family | Source class | Buyer must supply |
|---|---|---|---|
| B-1 | Frame chrome (lockup, hairline, credit chip) | engine | handle / CTA text (BV-01, BV-08) |
| B-2 | Presenter card and tile | buyer-owned | the talking-head take (SH-1) |
| B-3 | Term cards (light, dark, marker, question, chips, pill) | engine | — |
| B-4 | Callouts on the face card (number, keyword) | engine | — |
| B-5 | Dialog cards (screenshot + box) | buyer-owned screenshots; fallback recreated (FB-3) | screenshots (SH-3) |
| B-6 | Screen cards (recording + box) | buyer-owned recordings; fallback recreated (FB-2) | recordings (SH-2) |
| B-7 | Ink (highlight box, chevron, cursor) | engine | — |
| B-8 | Hook inserts (clip, phone mock, icon row) | buyer-owned; creator-supplied third-party with a created substitute | SH-4 (optional) |
| B-9 | Asides (B-roll, reaction clip) | buyer-owned; creator-supplied third-party with a created substitute | SH-5 (optional) |

### 8.3 Pattern specs (30 fps)
Engine building blocks: `VEOS.scene` (bespoke HTML/canvas), `ctx.videoFrame` (recordings), `VEOS.fx.shot` (screenshots with highlights), `VEOS.fx.appUI` (recreated UI), `VEOS.fx.logoPlate`, `VEOS.fx.clip`, `VEOS.fx.device` (phone frame), the camera presets `push-drift` (Z-2) / `pull-out` (Z-3), and the stage layouts of §3.2.

| ID | Pattern | Type | What's on screen | Motion (frames at 30 fps) | Use | Family / class | Needs |
|---|---|---|---|---|---|---|---|
| **P-01** | Lockup build | overlay | Two-line title + hairline (§5.2) | Line 2 at f2–3: soft L→R wipe + blur 8→0, 6 f expo-out, the hairline drawing with it; line 1 at f11–12, character-by-character L→R blur reveal (≈ 1 f per char, 4 f each); settled at f22–24 | Every reel, f0 | B-1 / TC-display; scene `kind: "lockup"`, z 6, `events: [0.1, 0.4, 0.9]` | — |
| **P-02** | Lockup mid (F-B hook) | overlay | The same lockup at S-title y 812–1026, between the insert and the face card | Same as P-01; line 1 may start at f0; ends on the G-2 cut (`out: "none"`) | H-3 | B-1 / TC-display | — |
| **P-03** | Face card | stage | The presenter in the 936 × 720 card, radius 40, soft shadow (0 24 48 rgba(0,0,0,.25)) | Hard cut in; live footage | Default state | B-2 | L-lesson |
| **P-04** | Credit chip | overlay | A hand-drawn arrow (2.5 px, 70 px long, pointing up-left at the caption) + a script line ("lessons by") + a chip (the handle) | The whole unit (arrow + script + chip) cuts on together with a 6 f flicker: on 3 f, off 1, on 1, off 1, then on (v04 @ 0:05.43); exit: hard off in 1 frame (v04 @ 0:10.2) | Window W1 (starts on a sentence boundary at 4.5–7.0 s, lasts 6–9 s) and W2 (the last 8–12 s) | B-1 / TC-legal; z 6 | S-credit |
| **P-05** | Jump cut | cut | A cut inside the take at the **same framing** (scale 1.00 ± 2 %, measured on 30+ cuts); the presenter's pose changes, the crop doesn't | Hard cut on a word boundary; the caption swaps on the next frame | Every 1–3 s of talking in L-lesson / L-full; 20–35 per minute | B-2 | cutmap |
| **P-06** | Term card, light | stage + overlay | A white card (`paper`, radius 40, filling S-card) with the term word (Anton 170 px, `termink`, shadow) at cy 720; the presenter tile bottom-right | Card and word: hard cut together (G-1, L-term-pip); the word is static from its first frame, no settle (v02 @ 0:02.82) | A term is defined or named ("codec", "minimum due", "HDR") | B-3 / TC-display; scene z 3 (under the tile) | L-term-pip |
| **P-07** | Variant chips | overlay | Plain-text chips in a row under the term (Inter Tight 500 56 px; two-tone allowed) | Each: soft left-to-right character reveal with blur 4→0, 8 f, no rise, starting 2 f before its caption word (v02 @ 0:03.95–4.22); ≥ 18 f apart; never re-flows earlier chips | Spoken variants, types, options, examples ("H.264, H.265, ProRes") | B-3 / TC-label; nested in P-06 (`overlaps`) | P-06 |
| **P-08** | Term card, dark | stage + overlay | A charcoal card filling S-card, 1–3 condensed words on ≤ 2 lines (line 1 `primary` for the state, line 2 `paper`); no presenter | Hard cut in and out (L-term-full); the text is static, no settle; held 0.7–1.5 s (v04 @ 0:36.97–0:37.70) | A verdict ("THIS IS WRONG"), a state ("AUTOMATIC HOTA HAI"), an announced term ("FORMAT"), an announcement gag ("LADIES & GENTLEMEN") | B-3 / TC-display | L-term-full, ≤ 1.5 s |
| **P-09** | Term card, marker | stage + overlay | A white card; the Essential pill (P-10) top-left; the brush term word (Permanent Marker 150 px) at x 112, cy 690; a strip of the settings panel (≤ 160 px tall) at y 800–960 with the highlight box drawing on its field; the presenter tile | Hard cut; the box draws (6 f) on the field word | The answer to a hook question; "the essential setting" | B-3 + B-5 + B-7 | L-term-pip; field map |
| **P-10** | Essential pill (SM-1) | overlay | "Essential #N" pill (§5.4) | Arrives with its card (no motion of its own) | Numbered essentials | B-3 / TC-label | P-06 / P-09 |
| **P-11** | Question card | stage + overlay | A white card, a 2-line sentence-case question (Inter Tight 600 78 px, `ink`), the presenter tile | Hard cut; text fades in over 6 f | The presenter turns the lesson with a question ("Why Automatic is good then?") | B-3 / TC-display | L-term-pip, 1.0–2.0 s |
| **P-12** | Number on card | overlay | A number + unit (Anton 190 px, `paper`, shadow) at the card bottom, over the presenter's chest | Hard on, on the jump cut nearest the number word (≤ 3 f before it); hard off on the next cut (v04 @ 0:18.10 on, 0:33.30 off) | A spoken value that matters ("50,000KB/S", "₹500", "30 FPS") | B-4 / TC-display; `overlaps` the face card; 40 px face clearance | L-lesson |
| **P-13** | Number beside the head | overlay | A number (64 px) + a 2–3-word note (44 px), stacked, in the empty side of the card | Hard on / off with cuts, as P-12 | A secondary value said in passing ("10,000KB/S bhi ni chahiye") | B-4 / TC-label | L-lesson; face box |
| **P-14** | Keyword on card | overlay | A format, file or product name (Anton 110–140 px, `paper`) at the card bottom | As P-12 | A name the viewer must remember (".MOV", "APPLE PRORES 4444") | B-4 / TC-display | L-lesson |
| **P-15** | Dialog card | stage + overlay | A white card; the creator's screenshot (dark UI) inset at x 92–868, y 588–1168, radius 22, cropped to the panel; the presenter tile bottom-right, overlapping its corner | Hard cut; the screenshot settles 1.02 → 1.00 over 7 f (expo-out), then drifts in ≈ +0.1 % per frame for the card's span (v02 @ 0:09.02) | Where a setting lives in an app | B-5 (`fx.shot`, `chrome: false`) | L-term-pip; field map |
| **P-16** | Highlight box | annotation | A 4 px rectangle (`primary` on TH-dark, `paper` on TH-light, `ink` on a light UI), radius 6, 8 px padding around the field | First: the stroke traces from the **top-right corner leftwards, then down** (counter-clockwise), 14–16 f, starting ≈ 12 f before the field word (`t_in` = word − 0.4 s) and closing on it (v02 @ 0:09.15–0:09.55; a lead ≤ 15 f is a valid on-word start). Next field: position and size slide over 7 f (inOut) on the field word −2 f. Exits with the card | Every named field, value or button (one box at a time) | B-7 / §22 | field-map keyframes |
| **P-17** | Chevron pointer | annotation | A white double chevron (« or ⌄), 96 px, 24 px outside the target, pointing at it | Pops 0.8→1 in 6 f; bobs 6 px toward the target on an 18 f sine cycle | A target under 40 px tall, a dropdown arrow, or a field the box can't frame cleanly | B-7 | field map |
| **P-18** | Cursor glide | annotation | A white arrow cursor (44 px, 2 px ink outline) gliding to the field; a click ring (r 10→34, 8 f, `paper` 60%→0) | Glide 12 f inOut, landing on the field word −2 f | Screenshots only (recordings show the real cursor) | B-7 | field map |
| **P-19** | Screen card | stage | The creator's recording filling S-card (cover-cropped to the panel), the presenter tile bottom-left (L-screen) | Hard cut; plays at 1× (`kind: "video"`, continuous) | F-B steps | B-6 (`ctx.videoFrame`) | L-screen |
| **P-20** | Screen focus | footage-treatment | The crop window inside the recording moves to the next panel region | Pan / zoom 14 f inOut, scale 1.0–1.6×, only when the next field is outside the current crop; never while a field name is being spoken | Long panels (export dialog sections) | B-6 | field map |
| **P-21** | Value pick | annotation | The box sits on a dropdown; when the recording opens it, the box resizes onto the chosen option on the value word | Resize 7 f | "24 → 32", "Auto → 30" | B-7 | field map |
| **P-22** | Panel strip | overlay | A horizontal crop (≤ 160 px tall) of a screenshot showing one row group, inside a term card | Static; its box draws over 6 f | Inside P-09 / P-11 | B-5 | — |
| **P-23** | Top insert (16:9) | overlay | A 16:9 clip in S-insert (936 × 527, radius 40, centred in y 150–760) | Hard swap to the next clip every 0.8–2.0 s; plays at 1× | H-3: the creator's own result, or a creator-supplied reference clip | B-8; insert record | L-insert-hook |
| **P-24** | Phone insert | overlay | A generic phone frame (300 × 610, radius 44, 10 px bezel) centred in S-insert, looping the creator's reel or app screen | The clip swaps every 0.8–1.0 s, hard | H-3 for app and reel topics | B-8 (`fx.device` phone + `ctx.videoFrame`) | L-insert-hook |
| **P-25** | Icon row | overlay | The tools named, as a row of type-set logo plates (`fx.logoPlate`: names in type, never fetched logos), or the creator's own dock capture | Plates pop over 6 f, 4 f stagger | "Premiere, DaVinci, CapCut, sab mein" | B-8; insert record | S-card or S-insert |
| **P-26** | B-roll in card | stage | The creator's own B-roll (desk, setup) in S-card, ≤ 1.5 s | Hard cut in and out | "Aur ye meri footage hai…" (it shows the line) | B-9 | L-lesson geometry (`fx.clip`) |
| **P-27** | Reaction in card | stage | A creator-supplied reaction clip ≤ 1.2 s in S-card; the created substitute is a P-08 announcement card with the line | Hard cut | Comedy `light` only, ≤ 1 per reel | B-9; insert record | BV-11 = light |
| **P-28** | Full-bleed face | stage | L-full: the presenter full frame, boxed caption at cy 1210, credit under it | Hard cut (G-3); jump cuts continue at the same framing | F-B asides and rule lines, ≤ 6 s per run | B-2 | L-full |
| **P-29** | Card only (no title) | stage | F-B body: the face card with an empty page above it | Hard cut | F-B rule lines between steps | B-2 | L-lesson |
| **P-30** | Term sequence | stage | 2–4 terms compared by sequence: identical card skin and position, each followed by its dialog card | Ritual U-1…U-3 per term | "Difference between X and Y" reels | B-3 | — |
| **P-31** | CTA chip | overlay | The credit chip in W2, carrying the CTA text (§6.7) | As P-04 | The CTA sentence | B-1 / TC-legal | S-credit |
| **P-32** | Recreated panel | stage + overlay | `fx.appUI` kind `settings`: a generic, unbranded settings panel with the field names and values the presenter says, | Rows fade in with a 4 f stagger on first show, then static; box as P-16 | FB-2 / FB-3, when the creator has no capture | B-5 / B-6 substitute | insert record |

### 8.4 Line → pattern lookup `[NICHE]`
| Line type | Primary | Alternates |
|---|---|---|
| The claim or setup ("Chahe tum koi bhi app use karte ho…") | P-03 + P-01 | P-23 / P-24 (F-B) |
| A term is named or defined | P-06 | P-08 (announced), P-09 (the essential) |
| Variants, types or examples of a term | P-07 on the term card | P-25 (tools) |
| "Yahan pe / is setting mein / click karo" (where) | P-15 + P-16 (F-A), P-19 + P-16 (F-B) | P-17, P-18, P-32 |
| A value is chosen ("32 select karo", "MP4 rakho") | P-21 | a P-16 move |
| A spoken number with a unit | P-12 | P-13 (secondary), P-16 on its field |
| A file, format or product name to remember | P-14 | P-06 |
| A verdict ("ye galat hai", "automatic hota hai") | P-08 | P-12 |
| A question that turns the lesson | P-11 | — |
| A personal aside or proof of the creator's work | P-26 | P-28 (F-B) |
| A joke or reaction (comedy light only) | P-27 | P-08 announcement |
| The rule or takeaway | P-03 (late in the reel: + Z-2 push or Z-3 pull-out) | P-28 (F-B) |
| The CTA | P-31 | — |

Niche rows `[NICHE: example]`:
| Niche line | Pattern |
|---|---|
| Money: "credit score 300 se 900 tak hota hai" | P-06 "CIBIL" + P-07 chips "300" and "900" |
| Money: "bill mein Minimum Amount Due likha hota hai" | P-15 with the creator's bill screenshot + P-16 on "Minimum Amount Due" |
| Money: "sirf minimum pay kiya toh 40% tak interest" (only if the script says it) | P-12 "40%" on the face card |
| Money: "auto-debit on karo" | P-19 or P-32 + P-16 on the toggle |
| Creator tools: "codec matlab H.264, H.265" | P-06 "CODEC" + P-07 |
| Creator tools: "resolution 1080 by 1920 rakho" | P-19 + P-21 on the resolution dropdown, then P-12 "1080 × 1920" |
| Creator tools: "4K mein shoot karna zaroori nahi" | P-08 "4K ≠ / BETTER" |
| Creator tools: "CapCut, VN, InShot, sab mein ye option hai" | P-25 (type-set plates) |

### 8.5 Data and truth rules
- No figures module: no computed numbers and no charts. Every number on screen is a spoken value or a value visible in the creator's own capture.
- Callout numbers use the spoken value exactly (V-NUMFMT grouping); captions keep the spoken digits.
- A recreated panel (P-32) shows only spoken field names and values, generic styling.
- An illustrative claim ("95% editors") stays in the lockup only when the creator says it.

### 8.6 Comedy layer: OFF by default (`tone.comedy: off`)
With BV-11 = `light`: P-27 only (one creator-supplied reaction clip ≤ 1.2 s, or its P-08 substitute), never on a teaching beat's trigger word, never with a meme sound (meme cues stay off).

### 8.7 Asset rules
- Real captures first: the creator's own screen recordings and screenshots for every app or setting (SH-2, SH-3).
- Crop screenshots to the panel being discussed; blur personal identifiers (emails, account numbers, file paths with names) for their whole time on screen (NC-14).
- Mocks: only generic, unbranded `fx.appUI` panels with spoken values (P-32), labelled.
- Logos and app icons: never fetched; the creator's own dock capture or type-set plates (P-25).
- Film clips, memes, other creators' reels: ask, then create (§12.5).
- No stock footage, no AI scenes, no decorative B-roll.

### 8.8 Density and variety
- An SC every 0.6–1.5 s counting captions; a weight-1 SC every ≤ 2.5 s.
- ≥ 6 distinct patterns per 40 s (F-A), ≥ 5 (F-B).
- The same card pattern at most 3 times in a row, except the unit ritual (P-30) and consecutive F-B steps (P-19).
- Term cards: on average ≤ 1 per 3 s; each holds ≥ 1.0 s.

---

## §9 Transitions `[REQ] [DNA]`

### 9.1 Library (hard cuts only)
| ID | Transition | Frames | Recipe | Cue role |
|---|---|---|---|---|
| **T-01** | Jump cut | 0 | A cutmap cut inside the talking head on a word boundary ±1 f; pairs with P-05 | none |
| **T-02** | Card content cut (G-1) | 0 | `stage.via: cut` + the card scene's `t_in` on the same frame | `reveals` (≤ 1 per 2 s) |
| **T-03** | Composition cut (G-2) | 0 | F-B hook → body: the insert and lockup scenes end, the stage cuts, captions start | `reveals` |
| **T-04** | Full-bleed cut (G-3) | 0 | L-lesson ↔ L-full | none |
| **T-05** | Lockup build | 25 | The lockup's entry (P-01); not a scene transition | none |
| **T-06** | Credit window in / out | 6 / 0 | P-04 flicker-on and hard off | none |
| **T-07** | Hard end | 0 | The last frame ≤ 6 f after the last word, on the face card | none |

### 9.2 Grammar
| Boundary | Use | Never |
|---|---|---|
| Frame 0 | Already playing (no fade-in) | Fade from black, a title card |
| Hook → body | F-A: T-02 to the first term card; F-B: T-03 | Any animated transition |
| New term or step | T-02 on the trigger word −2 f | A slide, a pop, a crossfade |
| Back to the presenter | T-02 (or T-04 into L-full) | A grow or pop-back |
| Inside a talking run | T-01 with P-05 alternation | Smooth zooms |
| A number or keyword lands | The callout cuts on with the nearest jump cut | Shake, flash, scale-ins |
| Last word | T-07 | An outro card, a black tail |

### 9.3 Shot grammar: OFF (`spine: talking_head`, single speaker).

### 9.4 Budget (per 40 s)
- T-01: 15–30 (every 1–3 s of talking).
- T-02: 6–16.
- T-03: ≤ 1 (F-B). T-04: ≤ 6 (F-B).
- "The same transition never 3× in a row" does not apply: every transition here is a cut.
---

## §10 Motion, camera, layers, finishing `[REQ] [DNA; motion tokens TUNE ±15%]`

### 10.1 Motion tokens (30 fps)
| Token | Value |
|---|---|
| Beat lead | 2 f before the trigger word (caption lead 1 f) |
| Entry ease | `cubic-bezier(0.22, 1, 0.36, 1)` (expo-out) |
| Exit ease | `cubic-bezier(0.64, 0, 0.78, 0)`, 5–6 f, used only by callouts and the credit chip |
| Lockup reveal | line 2: L→R soft wipe + blur 8 → 0, 6 f, at f2–3; line 1: L→R per-character blur reveal at f11–12, ≈ 1 f per character, 4 f each; settled f22–24 |
| Hairline draw | 6 f, left to right, with line 2 |
| Term / dark card text | none: on with the cut, static |
| Variant chip | L→R character reveal + blur 4 → 0, 8 f, no rise; ≥ 18 f between chips |
| Callouts | hard on / off with jump cuts (0 f) |
| Highlight box | stroke trace from the top-right, counter-clockwise, 14–16 f; slide 7 f inOut |
| Screenshot settle | 1.02 → 1.00, 7 f expo-out, then +0.1 %/f drift |
| Chevron | pop 6 f; bob 6 px per 18 f |
| Credit chip | flicker-on 6 f (on 3, off 1, on 1, off 1, on); exit hard (0 f) |
| Holds | titles ≥ 10 f after building; on-screen text ≥ 0.25 s per word (captions under E3: ≥ 0.15 s per word, set by the caption profile) |

### 10.2 Footage camera: zoom policy `presets` `[DNA]`
Measured at full frame rate (background-registered ORB / LK scale between frames): the jump cuts keep the framing (scale 1.00 ± 2 % across 30+ cuts in v01, v02, v04), so the earlier 1.00 / 1.25 re-crop alternation was a 1 fps artefact of the presenter leaning in. The only camera moves are a few smooth pushes and pull-outs on the face card, all in v02's back half (0:31–0:42); v01, v03 and v04 have none.

| ID | Preset | Recipe (30 fps) | Use |
|---|---|---|---|
| **Z-1** | none (cutmap) | Jump cut at the same framing; no camera event | Every 1–3 s of talking (P-05) |
| **Z-2** | `push-drift` | 1.00 → 1.28 over 18 f, accelerating (`ease: "in"` in the preset, built in; measured +0.5 %/f rising to +4 %/f), starting on a jump cut; holds the push until the next card swap or stage cut, which resets to 1.00 (v02 @ 0:41.20–0:41.77). Small variant: 1.00 → 1.08 over 14 f (v02 @ 0:31.8, 0:34.7) | A rule or verdict line said with emphasis, back half only |
| **Z-3** | `pull-out` | 1.15 → 1.00 over 33 f, near-linear (`ease: "linear"` in the preset; −0.4 %/f), starting **mid-shot from the tighter crop** (v02 @ 0:38.77–0:39.8): when the face card is already tighter than 1.00 (a held Z-2), write `{"preset": "pull-out", "p": {"from": "inherit"}}` so it pulls from the crop on screen with no snap. Only from a 1.00 card, start it on a jump cut at the preset's 1.15 | A widening line ("lossless", "the whole picture"), back half only |

Rules:
- 0–4 camera moves per reel (Z-2 max 3, Z-3 max 2), only in L-lesson, never in the hook (0–4.5 s), never the same preset twice in a row (v02: push, push-small, pull, push).
- Never inside L-term-pip, L-screen, L-insert-hook or L-full; the stage resets the camera at every layout cut, so the first face-card shot after a term card is always 1.00.
- No punch, shake, rotation or zoom-through (N2). A Z-2 at 1.28 needs a ≥ 1080 px-wide source.

### 10.3 Canvas camera: OFF (§21).

### 10.4 Layer order (back to front)
1. W-page (z 1).
2. Card scenes that fill S-card or S-insert: term cards, dialog card, screen card, inserts, B-roll (z 3).
3. The stage window: the face card or the presenter tile (z 4).
4. Callouts on the face card, variant chips, the Essential pill, the highlight box, chevron and cursor (z 5).
5. The lockup and the credit chip (z 6).
6. Captions (z 7, auto).
z 8–11 are not used.

### 10.5 Finishing
- The card: radius 40; soft shadow 0 24 48 rgba(0,0,0,.25) (visible on TH-light, invisible on TH-dark); a screenshot inside a white card gets radius 22 and no border.
- Page noise 0.02 on TH-dark; nothing on TH-light.
- Glow: only the hairline (8 px, `primary` at 60%).
- No grain, no vignette, no bloom, no light leaks, no colour grade.

---

## §11 Sound contract (minimal) `[REQ] [VAR]`
| Line | Decision |
|---|---|
| **Cue moments** | `reveals` (a term card, dark card or question card landing; the first highlight-box draw on a new card; a number callout) and `list_cue` (the unit entry when the reel numbers its essentials or F-B steps: one file, once per unit). The hook carries at most one cue, on its first card reveal (H-1, H-2, H-4) or the composition cut (H-3). Jump cuts, re-crops, caption swaps, box slides and the credit chip are silent. ≤ 3 cues per 10 s |
| **Meme cues** | Off (comedy is off; `light` adds no meme sounds) |
| **Music bed** | On: a calm bed from the pack, entering after the hook (on the first unit) |
| **Ducking** | The bed sits ≥ 20 dB under the voice while the voice speaks |
| **Loudness** | −14 LUFS integrated, true peak ≤ −1.5 dBTP; hard end ≤ 6 f after the last word (NC-8) |

Mirrored in `tokens.json → sound`.

---

## §12 Footage requirements, shot list, fallbacks, inserts `[REQ]`

### 12.1 Setups `[DNA assumed; VAR actual]`
| ID | Setup | Spec |
|---|---|---|
| **A** | Talking head | Webcam or phone, seated front-on, chest-up, the lens at eye level or slightly below; a plain lit room with one practical lamp or plant behind; 16:9 or 9:16 source (the card crops 4:3); 30 fps (VFR conformed); clothing plain (no fine stripes: the card downsamples) |
| **B** | Screen capture | Record the app at 100% UI scale on a 1080p+ display, no webcam overlay (the engine draws the presenter tile), cursor visible, slow deliberate moves; one recording per step or one continuous take with clean pauses |

### 12.2 Shot list `[COND: footage_dependency ≥ medium → F-B]`
| ID | Shot | Spec | Count per 40 s | Must / optional | Formats |
|---|---|---|---|---|---|
| SH-1 | Talking head in short breaths | Setup A; 2–4 words per breath; gestures toward the lens (OK sign, point) | the whole reel | must | F-A, F-B |
| SH-2 | Screen recording per step | Setup B; 3–12 s each; the cursor rests on each field as it is named | 3–8 | must (F-B) | F-B |
| SH-3 | Screenshots of named panels | PNG, full resolution, cropped later | 1–4 | optional | F-A |
| SH-4 | Hook proof clip | 2–4 s of the creator's own result or phone screen recording | 1 | optional | F-B |
| SH-5 | Own B-roll | 1–2 s of the creator's desk or setup | 0–2 | optional | F-A, F-B |

### 12.3 Fallbacks
| ID | For | What the engine does instead | Fidelity cost | Result |
|---|---|---|---|---|
| FB-1 | SH-1 | none: the style is the presenter teaching | — | `no_fallback` |
| FB-2 | SH-2 | P-32 recreated settings panel (`fx.appUI` kind `settings`, generic, unbranded) with the spoken field names and values, the box stepping through it | No real UI motion or scroll; viewers can't match it pixel for pixel to their app | `degraded` |
| FB-3 | SH-3 | The same recreated strip inside the dialog card | Generic UI instead of the real panel | `degraded` |
| FB-4 | SH-4 | Use H-1 (claim lockup in frame) instead of the insert hook | No proof clip in the first 2.7 s | `holds` |
| FB-5 | SH-5 | Skip the aside; stay on the face card with a jump cut | One fewer variety beat | `holds` |

Say at the checkpoint which fallbacks were used.

### 12.4 Props, reaction bank, matte, resolution
- Props: none.
- Reaction bank (natural gestures to keep in the cut): an OK sign to camera, an index finger at the lens, a two-hand "frame", a shrug, a hand-wave "no". Keep them; they are the face card's only "graphics".
- Matte: none.
- Resolution: the Z-2 push (1.28) needs a ≥ 1080 px-wide source (a 16:9 1080p webcam gives ample room in the 936 px card). Screenshots under 1600 px wide: crop tighter and treat their small text as decorative.

### 12.5 Third-party inserts: ask, then create `[REQ]`
Claude never fetches anyone else's media. This style's typical third-party moments and their created substitutes:

| Moment | Ask for | Created substitute (if not supplied) |
|---|---|---|
| A film or TV scene that evokes the topic (v01 hook) | "Do you have the clip?" | P-08 dark card with the concept ("SUBTITLES / BURNED IN") or `fx.appUI` kind `video` with a generic frame |
| A celebrity or creator reaction meme (comedy light) | the clip | P-08 announcement card with the line |
| Another creator's reel in the phone mock | the reel file | `fx.appUI` kind `video` in the phone frame, labelled |
| App icons, tool logos (v04 dock) | the creator's own dock capture | P-25 type-set logo plates |
| A product's UI the creator didn't record | a screen recording | P-32 recreated panel |

Flow: `veos inserts scan` → one short question listing the moments → creator files (`veos asset add --origin creator`) or created substitutes → `plan/inserts.json` records every moment (`origin: creator | created`). 

### 12.6 Frame rate and audio
30 fps CFR, 1080 × 1920, BT.709. One voice track: high-pass 80 Hz, de-ess, light compression, −14 LUFS.

---

## §13 Output contract `[REQ] [DNA]`

### 13.1 Core beat fields
`id`, `section` (`HOOK | TERM-n | STEP-n | RULE | CTA`), `t0`, `t1`, `spoken`, `trigger {word, at}`, `tone`, `line_type`, `layout` (L-…), `visual` (one sentence), `layers` (scene ids), `pattern` (P-…), `sfx`.

### 13.2 Conditional fields (this style)
| Field | Content |
|---|---|
| `caption` | `{profile: CS-1, overrides: []}` (never chunk text by hand) |
| `slot_content` | `{S-card: "face" \| "term_light:<WORD>" \| "term_dark:<LINES>" \| "term_marker:<WORD>" \| "question" \| "dialog:<asset>" \| "screen:<asset>" \| "broll:<asset>" \| "reaction:<insert>", S-title: "lockup" \| "none", S-credit: "credit" \| "cta" \| "none", S-insert: "<asset>"}` |
| `ink` | `[{mark: box \| chevron \| cursor, target: "field:<name>", rect: {x, y, w, h} (card coordinates), at, frames}]` from the field map |
| `insert` | `{id, origin: creator \| created}` for third-party moments |
| `exception` | `E3` (captions, inherited) or `E6` (caption and slot swaps) |
| `theme` | `TH-dark` / `TH-light` (reel header only; per_topic) |
| `shot_id`, `fallback_used` | for F-B shots |

### 13.3 Reel header
```yaml
format: F-A                     # F-A Lesson Frame | F-B Screen Walkthrough
theme: TH-dark                  # TH-dark | TH-light (topic rule §4.3)
hook_archetype: HA-05           # HA-05 (H-1 / H-2) | HA-02 (H-3) | HA-04 (H-4)
hook_variant: H-2
structure: tutorial
count: 3                        # units promised (or null)
lockup: ["This Mistake is", "costing you interest"]
credit: {w1: [5.4, 13.0], w2: [27.0, 38.0], script: "lessons by", chip: "@yourhandle"}
cta: {device: comment_keyword, keyword: BILL}
```

### 13.4 Beat example
```yaml
- id: 6
  section: TERM-1
  t0: 3.00
  t1: 5.20
  spoken: "agar tum sirf minimum due pay karte ho"
  trigger: {word: "minimum", at: 3.06}
  tone: warn
  line_type: term_named
  layout: L-term-pip
  pattern: P-09
  visual: "White card: 'Essential #1' pill, brush 'Minimum Due', the creator's bill strip with the orange box drawing on 'Minimum Amount Due'; presenter tile bottom-right"
  layers: [term-min-due, box-min-due]
  slot_content: {S-card: "term_marker:Minimum Due", S-title: lockup, S-credit: none}
  ink: [{mark: box, target: "field:Minimum Amount Due", rect: {x: 132, y: 846, w: 520, h: 64}, at: 3.06, frames: 6}]
  caption: {profile: CS-1, overrides: []}
  insert: null
  sfx: [{t: 3.0, id: "<pack id: soft UI pop>", beat: 6, on: "term-min-due@0", why: "answer card lands"}]
```

### 13.5 Hook proposals (3 required)
Each: name, archetype + variant (H-1…H-4), the lockup (2 lines), the hook pair (§6.4 row), the first proof card and its time, the caption chunks for 0–3 s, a storyboard line, the cue moment, and the stopper-test results (ST-1…ST-6 with numbers).

### 13.6 Checkpoint (before building)
1. 3 hook proposals with lockups and stopper tests.
2. The beat sheet with tones, layouts, patterns and `slot_content`.
3. The field map (every box rect, per asset) and the term list.
4. The transition map (cuts) and the cue list.
5. The credit windows and the CTA chip text.
6. The inserts record (creator vs created) and the fallbacks used.
7. Style stills: f0 + 0.8 s (lockup complete), the first term card, one dialog or screen card with the box, one callout on the face card, the last frame.

**Wait for approval.**

---

## §14 Worked examples `[REQ] [NICHE]`
Times are planning estimates; replace them with `words.edit.json` onsets. Spoken lines are example scripts (every number shown is one the example script states).

### 14.1 F-A Lesson Frame, H-2 question hook. [NICHE: example] Money: "credit card minimum due"
- **Lockup:** "This Mistake is / costing you interest". **Theme:** TH-dark. **Count:** 3 essentials (pill #1–#3). **CTA:** `comment_keyword` "BILL".

**Hook (0–3.0 s)**
| t (s) | Spoken | Visual | Caption chunks | Layout / camera |
|---|---|---|---|---|
| f0 | "Mera ek…" | Face card, presenter glancing down | "MERA EK" | L-lesson 1.00 |
| 0.17–0.67 | "…question hai" | Lockup builds (line 2 + hairline, then line 1) | "QUESTION HAI" | — |
| 1.10 | "honestly batana" | Jump cut; finger at the lens | "HONESTLY BATANA" | Z-1 |
| 1.80 | "credit card ka bill aata hai" | Jump cut | "CREDIT CARD KA" → "BILL AATA HAI" | Z-1 |
| 2.60 | "toh tum kitna pay karte ho?" | — | "TOH TUM KITNA" → "PAY KARTE HO" | — |
| **3.00** | "Agar sirf minimum…" | **P-09:** "Essential #1", brush "Minimum Due", the creator's bill strip (account number blurred), orange box draws on "Minimum Amount Due" | "AGAR SIRF MINIMUM" | L-term-pip (cut) |

**Body**
| Section | t (s) | Spoken (gist) | Tone | Layout | Patterns |
|---|---|---|---|---|---|
| TERM-1 | 3.0–5.2 | "agar tum sirf minimum due pay karte ho" | warn | L-term-pip | P-09, P-10, P-16 |
| | 5.2–7.4 | "toh baaki bill pe interest lagta hai" | warn | L-lesson | P-03, P-05 ×2; **credit W1 5.4–13.0** (P-04) |
| | 7.4–8.6 | "interest lagta hai" (repeated as the verdict) | warn | L-term-full | P-08 "INTEREST" (primary) / "LAGTA HAI" (paper) |
| | 8.6–12.4 | "aur kuch cards pe ye saal ka 40% tak hota hai" | warn | L-lesson | P-05; **P-12 "40%"** on "40%" (10.2), holds to 11.4 |
| TERM-2 | 12.4–14.0 | "Toh sahi tarika kya hai?" | explain | L-term-pip | P-11 "So what's the / right way?" |
| | 14.0–17.4 | "total amount due, poora, due date se pehle" | win | L-term-pip | P-06 "TOTAL DUE" + P-10 "Essential #2" + P-07 chips "full amount" (15.1), "before due date" (16.3) |
| | 17.4–20.4 | "app mein yahan dikhega… aur yahan pay" | explain | L-term-pip | P-15 the creator's card-app screenshot; P-16 on "Total Amount Due" (17.5) → slides to "Pay" (19.6) |
| | 20.4–24.0 | "hamesha total pay karo, minimum nahi" | win | L-lesson | P-03, P-05 ×2 |
| TERM-3 | 24.0–27.0 | "Aur agar ek saath nahi ho raha, toh EMI mein convert karo" | explain | L-term-pip | P-06 "EMI" + P-10 "Essential #3" + P-07 "convert" (25.2), "lower rate" (26.1) |
| | 27.0–29.6 | "is option se" | explain | L-term-pip | P-15 screenshot "Convert to EMI"; P-16 on the option (27.3); **credit W2 27.0–38.0** |
| | 29.6–31.4 | "interest kam lagega" | win | L-lesson | P-03, P-05 |
| RULE | 31.4–32.8 | "minimum due bill paid nahi hai" | warn | L-term-full | P-08 "MINIMUM DUE ≠" (primary) / "BILL PAID" (paper) |
| | 32.8–34.4 | "yaad rakhna" | explain | L-lesson | P-03 |
| CTA | 34.4–38.0 | "Comment karo BILL, main checklist bhej dunga" | cta | L-lesson | **P-31:** the W2 chip switches to "comment" + "BILL" at 34.4 (1.0 s silence before) |

Cue moments: 3.0 (P-09 lands), 7.4 (P-08), 10.2 (P-12), 12.4 / 24.0 (list cue: Essential #2, #3 entries share one file), 31.4 (P-08). Bed from 3.0.

### 14.2 F-B Screen Walkthrough, H-3 insert hook. [NICHE: example] Creator tools: "export settings for reels"
- **Lockup:** "Best Export Settings / for Instagram reels". **Theme:** TH-light (the card shows a dark editor UI). **CTA:** `follow_save_stack`. **Assets:** SH-4 the creator's own reel (phone insert), SH-2 one recording of their editor's export panel (34 s) and one of the upload screen (6 s).

**Hook (0–2.8 s)**
| t (s) | Visual | Caption | Layout |
|---|---|---|---|
| f0 | L-insert-hook: phone insert (P-24) playing the creator's reel; face card below; lockup line 1 starting at mid-frame (P-02) | hidden | L-insert-hook |
| 0.17–0.67 | Line 2 + hairline; lockup complete | hidden | — |
| 0.90 | The phone cuts to the editor's timeline screen | hidden | — |
| 1.80 | The phone cuts to the export screen | hidden | — |
| **2.80** | **G-2 composition cut** to L-screen: the export panel recording, box draws on "Resolution" | "RESOLUTION SABSE PEHLE" | L-screen (cut) |

**Body**
| Section | t (s) | Spoken (gist) | Layout | Patterns |
|---|---|---|---|---|
| STEP-1 | 2.8–6.8 | "resolution 1080 by 1920 rakho" | L-screen | P-19, P-16 on "Resolution" (2.8); **P-21** box onto "1080 × 1920" (4.6); credit W1 5.0–13.0 |
| STEP-2 | 6.8–9.6 | "frame rate 30" | L-screen | P-16 slides to "Frame rate" (6.8); P-21 onto "30" (7.9) |
| aside | 9.6–12.4 | "60 tabhi, jab shoot bhi 60 pe kiya ho" | L-full | P-28 full-bleed, caption cy 1210, credit in S-credit-full; P-05 ×1 |
| STEP-3 | 12.4–16.6 | "bitrate recommended pe rakho" | L-screen | **P-20** focus pans to the quality section (12.4, 14 f); P-16 on "Bitrate" (13.0); P-21 onto "Recommended" (14.2) |
| verdict | 16.6–17.8 | "zyada bitrate se quality nahi badhti" | L-term-full | P-08 "HIGHER ≠" (primary) / "BETTER" (paper) |
| STEP-4 | 17.8–23.0 | "format MP4, codec H.264" | L-screen | P-16 on "Format" (18.0) → "MP4" (19.4) → "Codec" (20.6) → "H.264" (21.6) |
| RULE | 23.0–26.4 | "bas ye chaar settings" | L-lesson | P-29 card only (no title), P-05 ×2; credit W2 from 25.0 |
| STEP-5 | 26.4–31.4 | "aur upload karte waqt high quality on" | L-screen | P-19 upload recording; P-17 chevron at the small toggle (28.3) |
| CTA | 31.4–35.0 | "aise aur settings ke liye follow kar lo" | L-full | P-28; P-31 the chip reads "follow for more" + handle (31.4) |

Cue moments: 2.8 (composition cut), list cue at each STEP entry (6.8, 12.4, 17.8, 26.4: one file), 16.6 (P-08). Bed from 2.8.

### 14.3 F-A Lesson Frame, H-1 claim lockup, term sequence. [NICHE: example] Creator tools: "HDR vs SDR"
- **Lockup:** "95% Creators / don't know this difference". **Theme:** TH-dark. **CTA:** `none` (credit chip: "lessons by" + handle).

| Section | t (s) | Spoken (gist) | Layout | Patterns |
|---|---|---|---|---|
| HOOK | 0–2.8 | "Chahe tum phone se shoot karo ya camera se, tumne settings mein dekha hoga…" | L-lesson | P-01, P-03; jump cuts at 1.1 and 2.0 |
| TERM-1 | 2.8–4.6 | "HDR" | L-term-pip | P-06 "HDR" |
| | 4.6–8.2 | "10-bit, HLG… zyada colours, zyada brightness range" | L-term-pip | P-07 "10-bit" (4.8), "HLG" (5.9); credit W1 5.2–12.0 |
| | 8.2–10.6 | "phone mein yahan milega" | L-term-pip | P-15 the creator's camera-settings screenshot; P-16 on "HDR video" (8.4) |
| TERM-2 | 10.6–12.4 | "aur SDR" | L-term-pip | P-06 "SDR" (P-30: same skin, same position) |
| | 12.4–15.0 | "8-bit, normal range, har phone pe same dikhta hai" | L-term-pip | P-07 "8-bit" (12.6), "every screen" (13.9) |
| RULE | 15.0–19.6 | "Instagram pe HDR kabhi kabhi washed out dikhta hai" | L-lesson | P-03, P-05 ×2, P-14 "WASHED OUT" (17.2) |
| verdict | 19.6–20.8 | "toh HDR hamesha better nahi hai" | L-term-full | P-08 "HDR ≠" / "ALWAYS BETTER" |
| where | 20.8–24.4 | "reels ke liye ye toggle off rakho" | L-term-pip | P-15 the same screenshot; P-17 chevron at the small toggle (21.4) |
| close | 24.4–32.0 | "jab tak tumhara editor HDR export na kare" | L-lesson | P-03, P-05 ×3; credit W2 22.0–32.0 |

Cue moments: 2.8, 10.6 (term entries, one list-cue file), 19.6 (P-08), 8.4 (first box). Bed from 2.8.

---

## §15 QA checklist `[REQ] [DNA]`

**1. Profile conformance**
- [ ] One format (F-A / F-B) and one theme for the whole reel; the theme follows the §4.3 topic rule. (review)
- [ ] Presenter share within the format's range; no absence > 3.0 s. (V-PRESENCE)
- [ ] Duration 30–50 s. (review)

**2. Hook**
- [ ] f0: presenter + first caption (F-A) or insert + face card (F-B); lockup readable by 0.9 s and settled by 1.1 s. (V-F0)
- [ ] Lockup: 2 lines, ≤ 9 words, English, no emoji; F-A to the last frame; F-B ends on the composition cut. (V-TITLE)
- [ ] First proof card by 3.0 s; ≥ 5 weighted SCs in 0–3 s. (V-F0, V-CADENCE)

**3. Body and cadence**
- [ ] 8–15 weighted SCs per 10 s; no weight-1 gap > 2.5 s; nothing static > 2.5 s. (V-CADENCE)
- [ ] Every term, field, value and number lands within ±5 f of its word. (V-ONWORD)
- [ ] Every unit follows U-1…U-5 in order; term cards hold ≥ 1.0 s. (review)
- [ ] Jump cuts keep the framing; ≤ 4 Z-2 / Z-3 moves, back half only, in L-lesson, never twice the same in a row. (V-CAMERA)
- [ ] Hard cuts only; no transition effect anywhere. (review)

**4. Captions**
- [ ] CS-1: ALL CAPS, 44 px (E3), +0.10 em, 1 line, 2–4 words, hard swaps, no emphasis, cy 1345 (1210 in L-full). (V-CAPTION, V-TYPE)
- [ ] Sync ≤ 150 ms lead; English terms and tool names exact; the creator's romanisation consistent. (V-CAPTION)

**5. Modules**
- [ ] §16 Chrome: S-title, S-card, S-caption, S-credit rects constant ±4 px; nothing below y 1536. (V-CHROME pending → review; V-SAFE)
- [ ] §22 Ink: one box at a time, always on the field being named (checked against the field map), drawn 6 f, slides 7 f. (review)
- [ ] §25 Brand: credit chip in W1 (starts 4.5–7.0 s, 6–9 s long) and W2 (last 8–12 s); CTA text ≥ 1.5 s when a CTA is set. (V-PROMISE)

**6. Truth and inserts**
- [ ] Every number on screen is spoken or visible in the creator's capture. (V-NUMFMT, review)
- [ ] Personal identifiers blurred for their whole time on screen. (review, NC-14)
- [ ] Every third-party moment is creator-supplied or a created substitute. (V-INSERTS)

**7. Sound contract**
- [ ] Cues only on reveals and the list cue; ≤ 3 per 10 s; none on cuts, camera moves or the credit chip; 1.0 s silence before the CTA. (S1–S6)
- [ ] The bed enters after the hook, ≥ 20 dB under the voice; −14 LUFS, TP ≤ −1.5 dBTP. (QA)

**8. End and export**
- [ ] Hard end ≤ 6 f after the last word, on the face card; no black tail, no outro card. (review)
- [ ] 1080 × 1920, 30 fps CFR. (QA)

---

## §16 Frame template / persistent chrome `[COND: modules.chrome] [DNA rects; TUNE ±5%]` (ON)

The whole style is this frame. The beat sheet writes only `slot_content`; scenes paint into these rects and nowhere else.

| Slot | Rect (x, y, w, h) | Radius | z | Lifetime | Allowed content | Entry (once) | Content swap |
|---|---|---|---|---|---|---|---|
| **S-title** | F-A: 64, 330, 952, 214. F-B: 64, 812, 952, 214 | 0 | 6 | F-A `video`; F-B `hook` | the lockup | P-01 build (f2–f24) | none (never changes) |
| **S-insert** | 72, 150, 936, 610 | 40 | 3 | `hook` (F-B H-3 only) | 16:9 clip, phone mock, icon row, created scene card | present at f0 | hard, every 0.8–2.0 s |
| **S-card** | 72, 568, 936, 720 | 40 | 3–4 | `video` | face, term_light, term_dark, term_marker, question, dialog, screen, broll, reaction | present at f0 (F-B: from the composition cut) | hard (E6) on the trigger word −2 f |
| **S-caption** | 64, 1313, 952, 64 | 0 | 7 | `video` (hidden during L-insert-hook) | captions (CS-1 / CS-2) | hard | hard (E6), ~0.6 s |
| **S-credit** | 360, 1396, 460, 136 | 0 | 6 | `after:5` (windows W1 and W2) | credit, CTA chip | P-04 (6 f flicker; hard off) | fade 6 f (credit → CTA text) |
| **S-caption-full** | 64, 1178, 952, 64 | 0 | 7 | `section:full` (L-full only) | captions | hard | hard |
| **S-credit-full** | 360, 1262, 460, 136 | 0 | 6 | `section:full`, inside W1 / W2 | credit, CTA chip | cuts with the layout | — |

Rules:
- Slot rects stay constant (±4 px) for their lifetime (V-CHROME, pending engine wave E-07; frame review until then). The presenter tile is part of the S-card content: it sits at the layout's tile rect, never elsewhere.
- Slots never overlap one another; the gaps (24 px card → caption, 19 px caption → credit) are fixed.
- Content swaps inside S-card and S-caption are hard (E6); mark each card scene's container `data-slot` and declare `exception: "E6"`.
- The lockup counts as one text element for the whole reel; with the caption and one card text element, a frame holds 3 text elements (the credit chip is TC-legal and not counted).
- **Credit windows:** W1 starts on the first sentence boundary between 4.5 and 7.0 s and lasts 6–9 s; W2 covers the last 8–12 s. Between them S-credit is empty. Never show the chip during the hook.

## §17 Running state & anchored graphics: OFF (`modules.running_state = false`, `modules.anchors = false`; the highlight box uses field-map keyframes from §22, not tracked anchors).

## §18 Data contract: OFF (`modules.data_figures = false`; numbers are spoken values shown as callouts, never computed).

## §19 Evidence & citations: OFF (`modules.citations = false`; the credit chip is brand furniture (§25), not a source line; third-party inserts follow §12.5).

## §20 Dialogue: OFF (`source_type: talking_head`, one speaker).

## §21 Canvas camera: OFF (`modules.canvas_camera = false`, `graphics: support`).

## §22 Ink & annotation layer `[COND: modules.ink] [DNA look; TUNE colour]` (ON)

| Token | Value |
|---|---|
| Stroke | `primary` on TH-dark, `paper` on TH-light, `ink` over a light UI; width 4 px (3 px on targets under 40 px tall); no wobble (a clean UI rectangle, not a hand-drawn mark) |
| Box | radius 6, padding 8 px around the field's rect; the stroke traces from the top-right corner leftwards then down (counter-clockwise) over 14–16 f, starting ≈ 12 f before the field word and closing on it; slides position and size over 7 f inOut to the next field |
| Chevron | white double chevron, 96 px, 24 px outside the target, bobbing 6 px per 18 f |
| Cursor | white arrow, 44 px, 2 px ink outline; glide 12 f; click ring 8 f |
| On screen | one mark at a time (a box, or a chevron, or a cursor) |

Marks used: **box** (P-16, P-21), **chevron** (P-17), **cursor** (P-18). No circles, scribbles, arrows with heads, underlines or brackets.

Targets come from the **field map** (§1 P8b): for each screenshot and recording, every named field's rect in card coordinates, and for recordings the local time range in which the field is visible at that rect (re-read the frames after any scroll). Rules:
- The box always sits on the field being named (from its word −2 f until the next field's word).
- Marks finish before the card cuts away; they never move onto the presenter tile or the face.
- When a recording scrolls under a static box, cut the box at the scroll start and redraw it on the new rect when the field is still again (6 f).
- No mark on a field that the field map doesn't contain.

## §23 Continuity: OFF (`modules.continuity = false`; hard cuts, no morph chain).

## §24 Series furniture: OFF (`modules.series = false`). The Essential pill (SM-1) is a per-reel marker, not a series tag; BV-13 can turn a series tag on later as a DNA change.

## §25 Brand: credit chip, CTA chip, sponsor chip `[COND: modules.brand] [DNA look; VAR text]` (ON)

| Element | Recipe | Text (VAR) | When |
|---|---|---|---|
| **Credit chip** (P-04) | A hand-drawn arrow (2.5 px, `paper` / `ink`, 70 px, from (440, 1440) up-left to (390, 1404), pointing at the caption) + a script line (Caveat 34 px, baseline y 1468, starting x 452) + a chip (Inter Tight 700 28 px, `paper` on `accent`, radius 6, padding 4 / 14, at x 560, y 1486) | script "lessons by"; chip = the handle (BV-01) | W1 and W2 |
| **CTA chip** (P-31) | The same chip; the script line and chip text change with a 6 f fade on the CTA sentence | §6.7 per device; with `comment_keyword` the chip reads the keyword (BV-08) | W2, from the CTA sentence to the end (≥ 1.5 s) |
| **Sponsor chip** | Only when a reel is sponsored: the chip reads the sponsor's name set in type, the script line reads "in partnership with", and a TC-legal "Paid partnership" line (24 px) sits 12 px under the chip for ≥ 2 s (NC-12) | sponsor name; BV-14 wording | W1 (replaces the credit) |
| **End card** | none (N14) | — | — |

The chip colour (`accent`) appears nowhere else. On TH-light the arrow and script are `ink`.

---

## Part C. Exceptions and the non-overridable core

**Declared:** E3 (quiet type: captions 44–53 px, default 48, weight ≥ 500, 1 line, ≤ 24 characters, contrast ≥ 7:1) and E6 (hard swap: captions and S-card content inside rects constant ±4 px). Limits are in §2.2 and `tokens.json → exceptions`. Buyers may switch either off (VAR): without E3 the captions rise to 54 px and the chunk drops to 2–3 words to keep one line; without E6 every swap gets a 3 f fade (the style loses its snap).

**Not used:** E1, E2, E4, E5.

**NC-1…NC-14 apply unchanged.** The ones this style leans on: NC-1 (callouts keep clear of the face), NC-5 (the empty bottom band is stricter than NC-5), NC-6 (recreated panels labelled), NC-7 (no fetched icons, clips or memes), NC-14 (blur identifiers in screenshots and recordings).

---

## Part D. Personalisation

### D.1 What the buyer is asked (one round, each with "keep the template default")
| ID | Question | Feeds | Default |
|---|---|---|---|
| BV-01 | Your name and handle? | the credit chip, the CTA chip | "the creator", `@yourhandle` |
| BV-02 | One or two brand colours? | `primary` (hairline, highlight box, dark-card state line), then `accent` (credit chip); contrast-nudged against `ink` / `paper` | `#F59E0B`, `#1E7A3A` |
| BV-05 | What language do you speak, and what should captions be in? | `profile.language`, always asked: **English** → English captions (default) · **Hinglish** → romanised Hinglish captions · **Hindi** → Devanagari captions; numbers follow (BV-06) | English ({{BV-05.speech|en}} → {{BV-05.captions|en}}) |
| BV-08 | Call to action: none, follow, comment keyword or link in bio? | §6.7, §25 | none (credit chip shows the handle) |

Defaulted, changeable later: fonts within each class (BV-03), number grouping (BV-06: international; Indian grouping for rupee-heavy niches), formats enabled (BV-09: both), theme colours (BV-10), humour (BV-11: off, max light), duration (BV-17: 30–50 s, TUNE 25–60).

### D.2 Lock summary
- **DNA:** the frame (slots and their order), the lockup recipe and lifetime, caption mechanics (ALL CAPS, box, hard swap, no emphasis), hard cuts only, same-framing jump cuts with rare late pushes, the unit ritual, the term-card skins, the empty bottom band, the one-accent rule.
- **TUNE:** coordinates ±5%; lockup sizes (78–94 / 64–80); caption size 44–54, tracking 0.06–0.14, cy 1325–1365; term-word size ±10%; cadence and motion ±15%; page colours within near-black / warm off-white; credit windows within the ranges above; energy calm ↔ balanced.
- **VAR:** `primary`, `accent`, handle, CTA device and text, language, numbers, theme choice per reel (by the topic rule), comedy off / light, sound contract.
- **NICHE:** §6.4 hook pairs, §8.4 niche rows, §14, App. A.

### D.3 NICHE slots, filled per reel
At P7 the editor appends the reel's hook pair (§6.4) and lockup (App. A); at P5 / P8 new line types are mapped to existing patterns (§8.4); the first approved reel of each format replaces its §14 example in the buyer's copy; confirmed tool and setting names go to the glossary.

---

## Part E. Changes and decisions vs the sources

| Decision | Source said | This template | Why |
|---|---|---|---|
| Two formats | STYLE-COVERAGE: one format with an F-mode variant inside it | F-A Lesson Frame + F-B Screen Walkthrough | v02 / v04 keep the title the whole reel; v01 / v03 drop it after a 2.7–4.3 s insert hook and live in screen / card-only / full-bleed layouts. One format couldn't state when the title persists (D1 vs the evidence) |
| Bottom band | ~340 px empty (y 1580–1920) | 384 px empty (y ≥ 1536) | NC-5 keeps meaning text out of y > 1540; the credit chip moved up 48 px |
| Lockup sizes | analysis: 62 / 54 px | 86 / 72 px | Re-measured on the 1080 × 1920 frames (v02 @ 0:10: line 1 is 442 px wide, cap height ≈ 65 px); the analysis numbers were cap heights |
| Credit chip lifetime | analysis: "appears at 4–6 s and stays" | two windows (W1 early, W2 closing) | Every reel hides it mid-video (v02 0:15–0:34, v04 0:10–0:36, v03 0:15–0:23, v01 0:11–0:23) |
| Presenter on term cards | a matte cut-out of the presenter at the card's bottom-right | a rounded presenter tile (288 × 320, radius 28) | Today's `card` layout shows a rectangular window; a matte cut-out PiP is an engine request (below) |
| Credit script font | thin handwriting | Permanent Marker 34 px | No thin handwriting face is bundled (engine request) |
| Box colour by theme | — | orange on TH-dark, white on TH-light | v02 orange on the dark page; v03 white on the light page |

### Engine requests
1. **Matte cut-out PiP** (`card` / `pip` option `cutout: true`: draw only the person cut-out inside the tile rect, no background, bottom edge flush with the card). Why: the evidence's term and dialog cards show the presenter as a cut-out leaning in at the card's corner (v02 @ 0:03–0:17). Today: the rounded presenter tile (L-term-pip), marked as the fallback.
2. **V-CHROME** (E-07, pending): slot-rect constancy. Today: frame review (§15).
3. ~~A thin handwriting font for the credit script line~~ (done: Caveat is bundled and used, slot `script`).
4. **Slot windows** (`slots.<id>.windows`) so S-credit's W1 / W2 are validated. Today: the scene's `t_in` / `t_out` carry the windows.
5. ~~Camera preset easing~~ (done: `camera_presets.push-drift.ease: "in"`, `pull-out.ease: "linear"`, and `p.from: "inherit"` for the mid-shot pull-out).
6. ~~Early-start on-word marks~~ (done: V-ONWORD accepts a lead-in of up to 15 f, so the box starts ≈ 12 f before its word, as measured).

---

## Part F. IDs used in this playbook

| Prefix | IDs |
|---|---|
| D | D1–D8 |
| H, N | H1–H18, N1–N14 |
| E | E3, E6 |
| W, L, G | W-page; L-lesson, L-term-pip, L-term-full, L-insert-hook, L-screen, L-full; G-1–G-5 |
| TH | TH-dark, TH-light |
| CS | CS-1, CS-2 |
| HA, ST | HA-05 (H-1, H-2), HA-02 (H-3), HA-04 (H-4); ST-1–ST-6 |
| SM | SM-1 Essential pill |
| U | U-1–U-5 (unit ritual) |
| P, B | P-01–P-32; B-1–B-9 |
| T | T-01–T-07 |
| Z | Z-1 jump cut (no preset), Z-2 `push-drift`, Z-3 `pull-out` |
| SH, FB | SH-1–SH-5; FB-1–FB-5 |
| S (slots) | S-title, S-insert, S-card, S-caption, S-credit, S-caption-full, S-credit-full |
| F | F-A, F-B |
| BV | BV-01, BV-02, BV-05, BV-08 asked; BV-03, BV-06, BV-09, BV-10, BV-11, BV-13, BV-14, BV-17 defaulted |
| V | V-F0, V-CADENCE, V-TITLE, V-ONWORD, V-FACE, V-PRESENCE, V-PROMISE, V-CAPTION, V-TYPE, V-EXC, V-HUES, V-LAYOUT, V-CAMERA, V-SAFE, V-INSERTS, V-NUMFMT, V-THEME, V-CHROME (pending) |

---

## App. A Lockup bank `[NICHE]`
Two lines, ≤ 9 words; `[slots]` are filled per reel.

**F-A Lesson Frame**
| # | Line 1 | Line 2 | Hook | Example niche |
|---|---|---|---|---|
| 1 | 95% [People] | don't know this difference | H-1 | "95% Creators / don't know this difference" (HDR vs SDR) |
| 2 | This Mistake is | ruining your [thing] | H-2 | "This Mistake is / ruining your credit score" |
| 3 | This Mistake is | costing you interest | H-2 | credit-card minimum due |
| 4 | Only Pro [People] | use this [setting] | H-1 | "Only Pro Editors / use this kind of subtitle" |
| 5 | Your [Tool] | has a hidden mode | H-4 | "Your UPI App / has a hidden mode" |
| 6 | Stop [doing X] | for your [goal] | H-1 | "Stop Shooting 4K / for your reels" |
| 7 | [N] Settings | every [person] should change | H-1 | "3 Settings / every phone user should change" |
| 8 | [Term] vs [Term] | explained in 30 seconds | H-4 | "SIP vs Lump Sum / explained in 30 seconds" |
| 9 | Nobody Tells You | what [term] means | H-4 | "Nobody Tells You / what CIBIL means" |
| 10 | The [Thing] Rule | most people get wrong | H-2 | "The 50-30-20 Rule / most people get wrong" |

**F-B Screen Walkthrough**
| # | Line 1 | Line 2 | Hook | Example niche |
|---|---|---|---|---|
| 1 | Best Export Settings | for Instagram reels | H-3 | creator tools |
| 2 | Best [Tool] Settings | for [use] | H-3 | "Best Camera Settings / for night shots" |
| 3 | Set Up [Feature] | in under a minute | H-3 | "Set Up Auto-Pay / in under a minute" |
| 4 | Turn This Off | before you [action] | H-3 | "Turn This Off / before you upload" |
| 5 | [N] Settings | your [app] hides from you | H-3 | "5 Settings / your banking app hides" |
| 6 | Read Your [Document] | like a [pro] | H-3 | "Read Your Statement / like a banker" |
| 7 | Fix [Problem] | in [N] clicks | H-3 | "Fix Blurry Uploads / in 3 clicks" |
| 8 | The Right Way | to [action] | H-3 | "The Right Way / to file your ITR" |
| 9 | Where to Find | [hidden setting] | H-3 | "Where to Find / your UPI limit" |
| 10 | [App] Settings | I change first | H-3 | "Camera Settings / I change first" |

## App. B Evidence map
See `evidence.md` (every DNA rule → `vNN @ m:ss`, with the inferred and unverified values listed).
