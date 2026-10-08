# Ledger Explainer Style Playbook (template v1)

**Purpose:** you (Claude) receive a talking-head take of {{BV-01.name|the creator}} plus its script. Use this playbook to turn every spoken quantity into a **live ledger**: white rounded cards that build row by row on a dark, topic-keyed gradient, values that land on the spoken number, the claimed figure struck and the real figure revealed. The presenter stays calm and framed the whole time; the graphic is the argument.

**Input it expects (SW-01 `talking_head`):** one front-on seated A-roll take (landscape 16:9, 4K preferred), the script, and, for the Case-file format only, 15–25 monochrome stills the creator owns. Everything else (cards, chips, bars, sliders, counters, end card) is built by the engine.

**Inspired by:** Ankur Warikoo (style only; see App. B). Template status: `draft`.

### Style DNA `[DNA]`
A Ledger Explainer reel reads in one glance as **a calm teacher in a framed 16:9 window (or full-width at the bottom), with the explanation drawn underneath as a ledger of white rounded UI cards on a deep teal, maroon or green gradient; small white sentence-case captions sit inside the footage frame; numbers count up, get struck through and are replaced by the truth.** There are no zooms, punch-ins, stickers or meme sounds; the A-roll is only trimmed with same-framing jump cuts at sentence ends. The rhythm comes from in-place state changes: a row enters, a chip fills, a value is struck, a bar grows, a slider steps. It is a finance classroom, not a hype reel, and it works the same for calories, hours or grams.

**Copy these 5 things:**
1. **One fixed, calm presenter asset**, framed and never moved: a 16:9 inset at the top (F-A), a full-width face under the data panel (F-B), or a 16:9 clip under a still band (F-C). §3.2, §3.6.
2. **White rounded ledger cards on a dark two-stop gradient**: radius 12, `ink` Poppins figures, grey micro-labels, rows that enter one by one on the spoken beat. §3.1, §8.3 (B-1, B-2, B-3).
3. **One honest comparison axis: claim vs reality.** The claim is grey and gets struck; the reality is a white tile. Red = costs more / the false belief, green = cheaper / the truth. §4.2, P-15, P-22.
4. **Numbers are the heroes and they are real**: Poppins 800 figures, currency and grouping following the language (₹ Indian grouping for Hinglish / Hindi, $ international for English), values that roll for 10 f and land on the spoken word, every figure recomputed from `plan/figures.json`. §5.5, §18.
5. **Quiet captions inside the footage frame**: Poppins 500, 36 px, white, sentence case, one sentence at a time, no word highlighting. §5.3, E3.

### Directives `[DNA]`
| # | Directive | Where it lives |
|---|---|---|
| D1 | **Teach with the graphic, never decorate.** Every card carries a number, a named quantity or the mechanism being said. No icons for flavour, no stock imagery | §2.3 H8, §8 |
| D2 | **Claim vs reality is the only comparison axis.** The false or assumed value is shown first in grey, then struck; the true value lands in a white tile | §4.2, P-14, P-15 |
| D3 | **Every number is real and recomputable.** It comes from the script, the creator, or a formula over those, and it lands within ±5 f of its spoken word | §18, H6 |
| D4 | **The presenter never moves.** No zooms, no punch-ins, no pop-backs, no splits that change mid-reel. The frame is fixed for the whole body | §3.3, §10.2 |
| D5 | **Calm and trusted:** no flashes (F-C alone allows ≤ 2 white story flashes, T-9), no shakes, no stickers, no meme sound, ≤ 3 bright hues per frame, soft eases | §4.5, §9, §11 |
| D6 | **Small, plain captions inside the footage** (36 px, white, sentence case), never over the cards | §5.3 |
| D7 | **The topic picks the colour.** How-it-works and plans are teal; traps and myths are maroon; story episodes are case green | §4.3 |
| D8 | **Furniture without clutter:** series tags, ledger counters, sponsor and end cards slot into fixed places and never break the layout | §16, §24, §25 |

Buyer directives `BD1…` `[VAR]` go here; they may only make the style stricter or more specific.

### Quick index
| § | What | Status |
|---|---|---|
| §0 | Style profile | ON |
| §1 | Procedure | ON |
| §2 | Hard rules, exceptions E3 + E6 | ON |
| §3 | Worlds, layouts L-inset-top / L-face-bottom / L-cinema-top / L-endcard | ON |
| §4 | Colour roles, theme packs TH-teal / TH-maroon / TH-case | ON |
| §5 | Type, caption profile CS-1 (+ CS-2 scrim fallback) | ON |
| §6 | Hook system (HA-07 default; HA-02, HA-12) | ON |
| §7 | Structure (ledger build, claim list, calculator, case story) and cadence | ON |
| §8 | Visual system: 10 families, 52 patterns P-01…P-52 | ON |
| §9 | Transitions T-1…T-8 | ON |
| §10 | Motion, layers, finishing (zoom policy `none`) | ON |
| §11 | Sound contract | ON |
| §12 | Footage, shot list SH-1…SH-6, fallbacks, inserts | ON |
| §13 | Output contract | ON |
| §14 | Worked examples (F-A, F-B, F-C) | ON |
| §15 | QA | ON |
| §16 | Frame template / chrome | **ON** |
| §17 | Running state | **ON** (anchors OFF) |
| §18 | Data contract | **ON** |
| §19 | Evidence & citations | OFF |
| §20 | Dialogue | OFF |
| §21 | Canvas camera | OFF |
| §22 | Ink & annotation | OFF |
| §23 | Continuity | OFF |
| §24 | Series furniture | **ON** (VAR; F-C uses it always) |
| §25 | Sponsor, brand & end cards | **ON** |
| Part C–F | Exceptions, personalisation, deviations from the source, IDs | — |
| App. A / B | Hook & title bank / evidence map | — |

**Formats:** F-A Ledger inset (default) · F-B Face-bottom calculator · F-C Case file.

---

## §0 Style profile `[REQ]`

```yaml
profile:                         # mirrored in tokens.json → profile
  source_type: talking_head
  presenter: {presence: anchor, share: [88, 100], max_absence_s: 3.5}
  spine: talking_head
  captions: {mode: full, role: support, mute_policy: mute_safe}
  graphics: primary
  duration: {class: short, target_s: [40, 60]}
  language: {speech: en, captions: {lang: en, script: Latn, transform: verbatim}, on_screen: en, post_title: en,
             supported: [[en, en, Latn], [hinglish, hinglish, Latn], [hi, hi, Deva]]}
  numbers: {grouping: international, currency: "$", compact: k_m_b, units: metric, decimals: 0, style: full}
  tone: {energy: calm, comedy: off, comedy_max: off}
  themes: {policy: per_topic, packs: [TH-teal, TH-maroon, TH-case], default: TH-teal}
  formats: {list: [F-A, F-B, F-C], default: F-A}
  footage_dependency: low          # F-C overrides: high
  cta: {devices: [end_card, comment_keyword, link_bio, post_only], placement: end, chosen: end_card}
  modules: {chrome: true, running_state: true, anchors: false, data_figures: true, citations: false,
            dialogue: false, canvas_camera: false, ink: false, continuity: false, series: true, brand: true}
```

Why each value:
- **source_type `talking_head`, spine `talking_head`:** all four source reels are one continuous take of one presenter; the picture never leaves him (v01–v04).
- **presenter `anchor` 88–100%, max absence 3.5 s:** the face is on screen 93–100% of runtime; the only absence is the 3 s end card (v01 @ 0:45–0:48).
- **captions `full / support / mute_safe`:** a sentence caption is on screen ~97% of the time, but it is small and serves the cards (all four).
- **graphics `primary`:** cards occupy 90–95% of runtime in v01–v03 and carry the argument. F-C overrides to `support` (~25% graphics; stills carry the story, v04).
- **duration `short` 40–60 s:** 39.9 / 48.1 / 59.8 / 49.6 s.
- **language:** the burned-in captions and labels are English while three post titles are Hinglish; the speech language is **(unverified)**. Template default: English speech, English captions; setup always asks (English, Hinglish, Hindi; BV-05).
- **numbers `indian ₹ lakh_crore`:** ₹1,31,190 · ₹60,00,000 · ₹75 L · ₹1.25 Cr on screen (v01, v03, v04). Numbers follow the language (BV-06): English → international `$` and K/M/B (unless the buyer picks ₹); Hinglish / Hindi → ₹ with Indian grouping and lakh / crore.
- **tone `calm`, comedy `off` (max `off`):** no stickers, stamps, shakes or meme layer anywhere (all four).
- **themes `per_topic`:** teal for money-mechanics topics (v01, v03), maroon for offers/traps (v02), near-black green for the story series (v04).
- **formats F-A / F-B / F-C:** three of the four reels use three different layouts around one presenter asset; F-A = v01 + v02, F-B = v03, F-C = v04.
- **footage_dependency `low`** (F-A, F-B: only the A-roll); F-C is `high` (≈21 stills in 50 s, v04).
- **cta:** the source uses an end card with the next video's thumbnail (v01) and a sponsor link line (v03). Comment keyword and post-only are added for buyers.
- **modules:** chrome (fixed frame, tabs, case tag, ledger slot), running_state (F-C ledger; the F-B parameter), data_figures (every number), series (F-C "case 01 / 07"), brand (sponsor card, end card). Citations off: the source shows no outlet cards.

### 0.4 Formats `[DNA set; VAR enable]`

| Field | F-A Ledger inset (default) | F-B Face-bottom calculator | F-C Case file |
|---|---|---|---|
| `when` | Build the numbers (2–4 named quantities → total → stress test → moral), or a claim-vs-reality list of 3–7 items | One calculation stepped through a parameter (years, months, servings): two options on one axis → why → transfer to a second case | A documentary story told as one episode of a numbered series, with a running ledger |
| profile overrides | none | none | `footage_dependency: high`, `graphics: support` |
| layouts | `L-inset-top`, `L-endcard` | `L-face-bottom`, `L-endcard` | `L-cinema-top`, `L-endcard` |
| structure | `ledger` (L-BUILD or L-LIST) | `ledger` (L-CALC) | `story` (S-CASE) |
| hook default | HA-07 (opening O-1 row build or O-2 rank skeleton) | HA-07 (opening O-3 dual stat question) | HA-12 title card |
| cadence | SC/10 s 4–7, hook 5, max gap 2.5 s | same | SC/10 s 3–6, hook 4, max gap 3.0 s |
| needs | just you talking | just you talking (a vertical or 4K take is best) | you talking + 15–25 monochrome stills you own |
| theme | TH-teal or TH-maroon by topic | TH-teal or TH-maroon by topic | TH-case only |

**Shared DNA:** the same calm presenter asset in a fixed frame, the same Poppins figures with ₹ grouping, the same claim-vs-reality colour axis, the same quiet in-footage captions. **Format choice rule:** if the script steps one calculation through a changing parameter → F-B; if it tells a story with dates, people and places → F-C; everything else → F-A.

### 0.5 Theme packs `[DNA policy; VAR colours]`
See §4.3. One theme per reel; the reel header declares it.

---

## §1 Procedure (follow in order) `[DNA]`

1. **P1 Inventory.** `ffprobe` every input. Confirm one A-roll setup (§12.1). Conform VFR to 30 fps CFR. Register every asset with its origin (`creator` / `created`, §12.5). For F-C, count the stills: < 15 per 60 s means FB-2 for the missing beats.
2. **P2 Prepare.** No matte: this style never draws behind the presenter. For F-B check the source: a 1080p landscape take allows ≤ 1.35× (FB-6).
3. **P3 Transcribe** with word timestamps, then apply `language.captions.transform` (default: translate Hinglish speech into clean English sentences, keeping English terms and brand names verbatim). Apply the glossary. Spoken numbers stay digits in captions ("₹2.5 lakhs", "51,880").
4. **P4 Segment** into the units of the structure (§7.1): L-BUILD (parameters → build → stress test → moral → question), L-LIST (promise → item 1…N → payoff), L-CALC (question → parameters → steps → why → transfer), S-CASE (title → chapters → turn → open question). Mark jump-cut points on word boundaries only.
5. **P5 Classify** every sentence with a line type (§8.4) and mark its **trigger word**: the number word for value beats, the item word for tiles, the verdict word for strikes.
6. **P6 Tone-tag** every sentence: `explain` · `claim` · `reality` · `warn` · `win` · `story` · `cta`. `claim` = the belief or advertised value (grey treatment); `reality` = the true value (white tile); `warn` = costs more / risk (red tag); `win` = cheaper / fixed (green tag).
7. **P7 Hook plan.** Pick the archetype and opening (§6.2–6.3). Write **3 hook variants**; each states its claim → evidence pair (§6.4). Run the stopper tests (§6.1).
8. **P8 Visual plan — the craft step of this style: "line → ledger move".** For every line: which row, chip, tile, bar or slider step it creates or changes, where on the board grid (§3.4) it lands, and which existing element it replaces. One board scene per section (§8.2 rule B0). Then:
   - **Data check (module `data_figures`):** write `plan/figures.json`: every displayed number as an input with provenance (`script` + `said`, `creator`, `spoken@t`) or a formula over inputs; run `veos figures` and resolve every mismatch with the script before planning further (§18).
   - **State plan (module `running_state`):** F-C ledger states and the F-B parameter steps with their `at` words (§17).
   - **Series metadata (module `series`):** episode number, case index "n / of", chapter name (§24).
   - **Sponsor check (module `brand`):** logo file or wordmark, disclosure wording, the spoken disclosure line, the slot (§25).
9. **P9 Beat sheet** (§13): one beat per trigger, meeting §7.6 cadence. Every value beat names its `figure_id`.
10. **P10 SFX ledger** (§11: cues only on reveals, the list cue and the CTA) and the transition map (§9).
11. **P11 Assets.** Build or collect them; run the third-party ask-then-create flow (§12.5) once; apply fallbacks FB-… and list which were used.
12. **P12 Checkpoint** (§13.5), then **wait for approval.**
13. **P13 Build** section by section → `veos figures` → `veos scenes-meta` → `veos measure` → `veos validate` → preview → QA (§15, ≤ 3 passes) → render.

---

## §2 Hard rules `[DNA]`

### 2.1 Editing rules (every style)
The ten editing rules in `playbooks/_global/GLOBAL-RULES.md` apply. They are directions, not limits: smooth, seamless motion; nothing overlaps by accident; keep the face clear (behind the speaker is fair game, text included); readable at a glance; one idea at a time; show the thing, not the word; say what was said; hook titles hook; pace like the style, not like a timer; the style decides the look.
- **Facts the engine checks:** accidental overlaps, jumps, the face covered, unreadable text, numbers and quotes that don't match what was said, the promised count. Every count, timing and budget this playbook gives is direction for the edit, not a limit.
- **Picture first, in this style's own look:** every key beat shows the thing being said (an object, a screen or app, a diagram, numbers in motion), not just its word; text supports the picture and never replaces it. When the speaker points with words ("this, this and this", "from this to this", "ye dekho"), show what they mean. Illustrations may use made-up but realistic numbers and names ("212 views", "1.2M views"), with no label; a number or quote the speaker says is shown as said. This overrides any rule below that bans made-up numbers or asks for an example tag: those rules now cover claims (the creator's results, prices, benchmarks, testimonials), not illustrations.
- **Hook titles hook:** the on-screen title promises the viewer something (an outcome, a curiosity gap, who it's for) and is true to what the reel delivers; it need not repeat the spoken words. This playbook sets its shape (§5.2, §6.5: lines, sizes, word limits, case), never its voice (§6).
- **Retired (8 Oct 2026), whatever this playbook says below:** no REPRESENTATIONAL or example labels on made-up cards, no credit lines, no flash limit (flash as often as this style calls for; any "NC-11" cap below no longer applies), and text may sit behind the speaker without an exception.

### 2.2 Declared exceptions
| ID | Style limits (never looser than the registry) | DNA reason | Evidence |
|---|---|---|---|
| **E3 Quiet type** | Captions 36–44 px (template 36), weight ≥ 500, ≤ 2 lines, ≤ 44 characters per line, contrast ≥ 7:1 (≥ 4.5:1 on the CS-2 scrim pill). Labels 28–39 px **only** with `redundant: true` (the words are spoken in the same beat or shown larger beside them): micro-labels, unit lines, tabs, parameter chips, status tags, case tag, ledger sub-label. Display text stays ≥ 40 px | The small, plain caption inside the footage and the grey micro-labels under values are what make the ledger look like a calm UI rather than a reel. The source measures 30–34 px captions and ~14–25 px labels; the template raises them to the registry floors | v01–v04 captions 30–34 px; micro-labels v01 @ 0:01 "a year", v02 @ 0:05 "you think" |
| **E6 Hard swap** | Content changes inside a container whose rect stays within ±4 px: counter digits rolling, chip-tab state (grey → white), the ledger counter's sub-label, the panel title text swap. The container's first entry and final exit stay eased | Ledger values change in place; the source never moves a value's box when its content updates | v02 tabs; v03 @ 0:07–0:21 value roll-ups; v04 @ 0:11–0:46 ledger |

Every scene that relies on one sets `exception: "E3"` or `"E6"`. Captions inherit E3 from CS-1.

### 2.3 MUST rules
- **H1 Frame 0 (HA-07):** f0 shows the presenter in the format's frame, the caption carrying the claim sentence, and the first board element already moving (entering on f0). A board with nothing moving at f0 fails (the weak v02 opening is not copied). check: V-F0
- **H2 Payoff by 1.0 s:** the first number or data row is visible by 1.0 s (F-A, F-B); the F-C thesis title is complete by 3.0 s. check: V-F0
- **H3 Cadence:** weighted state changes 4–7 per 10 s (F-C 3–6), ≥ 5 in 0–3 s (F-C ≥ 4), no gap between weight-1 changes longer than 2.5 s (F-C 3.0 s), nothing static > 2.5 s (live footage counts as motion). check: V-CADENCE
- **H4 On the word:** a row, chip, tile or tag starts 2 f before its trigger word and is fully on within ±5 f of it; a value lands on its number word within ±5 f. check: V-ONWORD, V-DATA
- **H5 The face is never covered:** nothing is drawn over the presenter window; captions live inside the footage window below the chin line, or on the chest in F-B. check: V-FACE
- **H6 Truth:** every number on screen is in `plan/figures.json` with provenance, recomputes within display rounding, and is either spoken or the result of a declared formula; compared values share one `scale_id`. check: V-DATA
- **H7 Number format:** ₹ glyph (never Rs/INR), Indian grouping (₹1,31,190), lakh/crore compacts ("₹75 L", "₹1.25 Cr") on chips and tiles, full grouping for computed amounts; no K/M/B on rupee amounts. check: V-NUMFMT
- **H8 Every card earns its place:** each card, tile or tag shows a number, a named quantity, a spoken item or the mechanism; no decorative icons, no empty card older than 1.2 s (skeleton cards must fill within 1.2 s of entering). check: review
- **H9 Presenter presence:** share 88–100%; the only absence is the end card ≤ 3.5 s. check: V-PRESENCE
- **H10 Promise integrity:** the number of rank numerals equals the items delivered; every "let's see" / "how did this happen?" is answered on screen; the CTA keyword (if chosen) is on screen ≥ 1.5 s. check: V-PROMISE
- **H11 Dead air (spine talking_head):** ≤ 1 gap ≥ 150 ms per 15 s; jump cuts only on word boundaries ±1 f, and never more than 1 per 10 s (the frame should read as one take). check: V-CADENCE + review
- **H12 Layout lock:** one layout for the whole body; the only stage change is the hard cut into the end card (T-7). check: V-LAYOUT
- **H13 Spelling:** brand and product names exact; glossary terms enforced in captions and cards. check: V-CAPTION
- **H14 Audio:** −14 LUFS integrated, true peak ≤ −1.5 dBTP, bed ≥ 18 dB under the voice (NC-8). check: loudness gate
- **H15 Determinism:** every frame is a pure function of its index; no `Math.random`, timers or video tags (NC-9). check: `veos scenes-meta`

### 2.4 NEVER
- N1. Zooms, punch-ins, crash zooms, shakes, rotation snaps or Ken Burns on the presenter.
- N2. Stickers, stamps, emoji, marker scribbles, meme sounds, light leaks, RGB splits; flashes anywhere except T-9 in F-C.
- N3. Coloured words inside captions, word-by-word karaoke, ALL CAPS captions, caption pills (except the CS-2 scrim fallback).
- N4. A lone number on an empty background with nothing it compares to. Every hero number has its claim, its unit line or its partner.
- N5. Bars of compared options on different scales; a bar whose length disagrees with its value; a status tag that contradicts the bars.
- N6. Red or green used for anything but bad/good meaning. White text on `good` below 4.5:1 (use the template's `#26803A`, never the source's `#2E8B3A`).
- N7. Stock footage, stock icons as content, hooded-hacker or money-rain clichés, fetched logos, fetched screenshots.
- N8. Fake dashboards, fake bank statements, fake UIs presented as real.
- N9. Cards drawn over the presenter window, the IG UI bands (y < 110, y > 1500, right 110 px between y 900–1540), or the caption line.
- N10. A sponsor card without the spoken disclosure and the visible "Paid partnership" label (NC-12).
- N11. More than one layout in the body; splits, PiPs or bubbles that appear mid-reel.
- N12. A black tail > 0.2 s after the end card.

BN1… `[VAR]` buyer additions go here.

---

## §3 Worlds, layouts, stage moves, safe zones `[DNA; coordinates TUNE ±5%]`

### 3.1 Worlds
| ID | Kind | Look (colours come from the active theme) | Carries | Enter / exit |
|---|---|---|---|---|
| **W-ledger** | `card-world` | Vertical two-stop gradient (TH-teal `#0D2B2B` → `#2E7A72`; TH-maroon `#1E1411` → `#8E524D`), a soft radial glow 760 px at (820, 1560) drifting ±24/18 px, film noise 0.04, vignette 0.12. Looks like a blurred room behind frosted glass | All cards, chips, bars, tiles of F-A and F-B; the F-B top panel | Present from f0 to the end card; never changes mid-reel |
| **W-case** | `stage` | Near-black `#050805` → green `#135C2C`, noise 0.05, vignette 0.2 | F-C: the area under the still band and behind the presenter clip; the title card | From f0 to the end card |
| **W-endcard** | `void` | Pure `#000000` | The end card only | T-7 hard cut in; the reel ends on it |

### 3.2 Layout library
| ID | Engine | Presenter rect (px) | Graphic rect | Caption | Treatment | Share (format) |
|---|---|---|---|---|---|---|
| **L-inset-top** | `card` | x 96, y 112, w 888, h 500 (16:9), **square corners, 4 px `paper` border**, shadow 0.3 (measured v01/v02: window x 108–970, y 73–567, border 4 px, radius 0; the real top at y 73 sits in the IG band, so it moves to 112 here) | x 64–1016, y 660–1500 (the **board**) | `inside_footage`, 22 px above the window's bottom edge (centre ≈ y 568) | none | F-A 0.88–1.00 |
| **L-face-bottom** | `stack` | Bottom cell y 760–1920, footage `cover`, face 0.30 of cell height, eye line at 0.22 (≈ y 1015); a long 160 px fade in `stage` on both sides of the seam, so the room melts into the panel (measured v03: footage visible from y ≈ 450, blended to y ≈ 700; eyes y ≈ 925–1000). The real bottom ≈ 360 px goes to pure black (y 1560–1920, a heavy vignette under the chest) | Top cell x 64–1016, y 120–740 (the **panel**) | `fixed_y` centre y 1462 (on the chest) | none | F-B 0.88–1.00 |
| **L-cinema-top** | `card` | x 64, y 960, w 952, h 536 (16:9), radius 6, 2 px `paper` border, shadow 0.35 | x 0–1080, y 0–940 (the **still band**; the title card in the hook) | `inside_footage`, 22 px above the window's bottom edge (≈ y 1452) | GR-case-mono when the engine supports grades (§4.4) | F-C 0.90–1.00 |
| **L-endcard** | `hidden` | none | x 64–1016, y 110–1500 | captions hidden | — | 0–0.08, last ≤ 3.5 s |

**Layout rule:** one layout per reel body (H12). The end card is the only other layout.

### 3.3 Stage moves
| ID | Move | Recipe | Use |
|---|---|---|---|
| **G-1** | **Hold** | The presenter window never moves, scales or crops differently during the body | Always |
| **G-2** | **Cut to end card** | `via: cut` on the last word: the presenter and board vanish on one frame, W-endcard is black and the P-44 block slams in (scale 2.6 → 1.0, 18 px motion blur, 3 f; measured v01 @ 45.00–45.08) | The last 2.5–3.5 s, after the last spoken word or on the CTA line |

There are no other stage moves. A pop-back, split change or zoom is a DNA deviation.

### 3.4 Layout diagrams and the board grid

**L-inset-top (F-A)**
```
┌──────────────────────────────┐ 0
│   (IG top UI, keep clear)    │ ← y 0–110
│ ┌──────────────────────────┐ │ ← presenter window x 96–984, y 112–612 (16:9)
│ │      presenter (16:9)    │ │
│ │  caption line, 36 px     │ │ ← caption bottom 22 px above y 612 (centre ≈ 568)
│ └──────────────────────────┘ │
│ [TAB1][TAB2][TAB3][TAB4][T5] │ ← S-tabs y 648–692 (L-LIST only)
│  BOARD x 64–1016             │ ← board y 660–1500
│  lane 1  y 676–856           │
│  lane 2  y 870–1050          │
│  lane 3  y 1066–1186         │
│  lane 4  y 1200–1386         │
│  footer  y 1410–1500         │ ← summary line / sponsor / keyword
├──────────────────────────────┤ 1500
│   (IG bottom UI, keep clear) │
└──────────────────────────────┘ 1920
```

**Board grid, L-BUILD mode (rows of named quantities):**
| Lane | y | Holds |
|---|---|---|
| Row 1 | 676–856 | label 32 px caps (676–714; real ≈ 30 px, cap 21) · micro-label 28 px (714–748) · bar 56 px high x 64–600 (756–812; real 58 px, x 70–669) · value chip w 240 × h 96 at x 624 (736–832), figure 42 px (real ≈ 40) · outline tag 36 px at x 64 (820–856) |
| Row 2 | 870–1050 | same offsets +194 |
| Total | 1066–1186 | total card w 420 centred (x 330–750), number 56 px (real cap 37 px ≈ 53 px) + sub-line 28 px |
| Tiles | 1200–1386 | micro header 28 px (1200–1232) · 3 columns of tiles w 304, h 64, gap 20 (x 64 / 388 / 712), rows 1244 and 1322 |
| Footer | 1410–1500 | summary line 44 px (1410–1462) + helper 32 px (1466–1500) |

**Board grid, L-LIST mode (claim vs reality rows):**
| Lane | y | Holds |
|---|---|---|
| Tabs | 648–692 | N chip tabs, equal widths, gap 12, 28 px caps |
| Row k (k = 0…4) | 724 + 156·k → 860 + 156·k | rank numeral 100 px at x 64–150 · title 50 px at x 176 (real cap 36 px ≈ 51 px) · sub-label 32 px at x 176 (+56) · struck/claimed value 40 px right-aligned to x 700 with micro-label 28 px under it · reality tile x 720–960, h 120 (clear of the IG button column), centred in the row |
| Footer | under row 5: a saved-note line at the row's right (P-17) | — |

Five rows end at y 1484. **Six or seven items:** row pitch 124, numerals 96 px, the reality tile h 100 (still inside the floors). More than 7 items: split the reel.

**L-face-bottom (F-B)**
```
┌──────────────────────────────┐ 0
│ PANEL TITLE 44 px            │ ← S-panel-title y 128–188
│ [param][param][param] 28 px  │ ← y 208–252
│ ──●──────────────── slider   │ ← track y 300, tick labels 40 px y 322–362
│        [Costs more]          │ ← leader chip straddles row 1 top (y 376–426)
│ ┌[8%]═══════════  ₹2,00,000┐ │ ← bar row 1 y 410–510
│ ┌[11%]══════════  ₹1,63,250┐ │ ← bar row 2 y 538–638
│ Flat: on the full amount     │ ← explain lines 40 px y 650–694, 698–742 (v03 @ 0:40: y ≈ 675)
├≈≈≈≈≈≈≈≈ seam y 760 ≈≈≈≈≈≈≈≈≈≈┤ ← 160 px `stage` fade (footage shows from ≈ y 680)
│      presenter, full width   │ ← eyes ≈ y 1015
│      caption, 36 px, chest   │ ← centre y 1462
└──────────────────────────────┘ 1920
```
Opening stat cards (P-19) occupy y 220–520 (two cards w 456, h 300, gap 40) before they morph into the bar badges.

**L-cinema-top (F-C)**
```
┌──────────────────────────────┐ 0
│ case 01 / 07 ●○○○○○○  ledger │ ← case tag y 140–188 (x 64) · ledger slot x 656–1016, y 132–264
│                    ₹60,00,000│
│      STILL (monochrome,      │ ← still band y 0–940, held static
│      one accent object)      │
│   ░░░ fade into W-case ░░░   │ ← mask fade y 760–940
│ ┌──────────────────────────┐ │ ← presenter window x 64–1016, y 960–1496
│ │   presenter (16:9)       │ │
│ │   caption, 36 px         │ │ ← centre ≈ y 1452
│ └──────────────────────────┘ │
└──────────────────────────────┘ 1920
```
Title card (hook, 0–3 s): episode label y 128–164 at x 64; title lines (150 px, line height 0.86) at y 170 / 299 / 428 with x indents 64 / 300 / 110; chapter line 56 px at y 600 with a 160 × 4 px accent rule at y 588; the prop rests on a lit table plane at y 700–900.

### 3.5 Safe zones and bands
- Meaning text box: x 64–1016, y 110–1500 (`layout.safe`). The board, panel and still-band text stay inside it. **IG button column (NC-5):** from y 900 to y 1540 nothing that carries text reaches past x 960 (the like / comment / share buttons sit at x > 970): the board's reality tiles, the tile grid (P-05) and the keyword card (P-45) end at x 960.
- Caption band: inside the presenter window (F-A, F-C) or y 1440–1484 (F-B). Graphics never enter it.
- Headline band: none in F-A/F-B (`headline: none`); F-C title card y 128–660 during the hook only.
- Slot bands: S-tabs y 648–692; S-panel-title y 128–188; S-case-tag y 140–188; S-ledger y 132–264 (§16).

### 3.6 Presenter rules
- Share 88–100%; longest absence 3.5 s (the end card).
- The presenter returns only by never leaving: there are no cutaways.
- Crops: F-A and F-C show the full 16:9 frame (head top at 18–30% of the window height, eyes at 40%). F-B crops 9:16 from the take with the eye line at y ≈ 1015 and the head top at y 800–880 (v03: head top ≈ 790).
- Nothing is ever drawn behind or in front of the head (no E1). The presenter wears one plain dark top; the background is the same styled room in every reel (§12.1).

---

## §4 Colour, themes, grades `[roles' meanings DNA; brandable hex VAR; theme hues TUNE]`

### 4.1 Role palette
| Role | Hex (template) | Its one job | Text on it | Contrast | Brandable |
|---|---|---|---|---|---|
| `primary` | `#FFFFFF` ({{BV-02.primary|#FFFFFF}}) | The "you are here" highlight: the current chip tab, the slider handle, the end-card arrow, the CTA keyword card | `ink` | 18.9:1 | yes (VAR) |
| `accent` | `#40E87A` ({{BV-02.accent|#40E87A}}) | Story accent: F-C ledger digits, case dots, episode label, the one accent object in stills; the series tag in F-A/F-B | `ink` | 11.7:1 | yes (VAR) |
| `stage` | theme (`#14403D` teal, `#3A2420` maroon, `#0B1F10` case) | The world tone at the F-B seam fade. Never text | `paper` | ≥ 10:1 | theme-keyed (TUNE) |
| `data` | theme (`#1F5A5C` teal, `#5A2E2A` maroon, `#135C2C` case) | The **first** compared option: its stat card, bar fill and label badge | `paper` | 7.9:1 (teal) | theme-keyed (TUNE) |
| `night` | `#1C1C1C` | The **second** compared option: its stat card, bar fill and badge | `paper` | 17.0:1 | no |
| `bad` | `#C8283C` | Costs more, the false belief, the strike line, the empty dashed bar, the worse method tag | `paper` | 5.5:1 | **fixed** |
| `good` | `#26803A` | Cheaper, the true value's check, the better method tag | `paper` | 5.0:1 | **fixed** |
| `ink` | `#111111` | All text on white cards | — | 18.9:1 on paper | no |
| `paper` | `#FFFFFF` | Cards, chips, tiles, captions, summary lines on the world | — | 5.1:1 on the teal bottom, 6.1:1 on the maroon bottom | no |
| `muted` | `#6B6B6B` | Micro-labels on white ("you think", "a year", "her salary") | — | 5.3:1 on paper | no |
| `ghost` | `#D6CFCC` | Future items: unlit rank numerals (100 px, ≥ 3:1) and unlit tab pills (with `ink` text) | `ink` | 3.3:1 on the teal bottom, 3.9:1 on maroon (display ≥ 96 px only) | no |

`max_bright_per_frame` = 3 (white is not a bright hue; the bright ones are `primary` when branded, `accent`, `data`, `bad`, `good`).

### 4.2 Meanings
- **Axis 1, claim → reality:** grey (`muted` on cards, `ghost` on the world) = what you think / what is advertised; white tile with `ink` figure = what is true.
- **Axis 2, worse → better:** `bad` red = costs more, flat, false, empty; `good` green = cheaper, reducing, checked.
- **Two options compared:** option A is always `data` (the theme tone), option B always `night`. Their colour never encodes good or bad; the tags do.
- **Accent** means "this is the story's thread" (the money in the F-C ledger, the one coloured object in each still).
- **Brand colours** appear only on brand elements (the sponsor card's logo, the creator's thumbnail) and on `primary`.

### 4.3 Theme packs (`per_topic`)
| Pack | `W-ledger` gradient (top → bottom) | Glow | `data` / `stage` | Topic → theme rule |
|---|---|---|---|---|
| **TH-teal** (default) | `#0D2B2B` → `#2E7A72` | `#4A9A90` at 32%, r 760 at (820, 1560) | `#1F5A5C` / `#14403D` | How something works, building the numbers, comparisons, plans. Finance: salary, loans, EMIs, insurance, investing. Other niches: calories, macros, hours, sleep, reps, the price of a plan |
| **TH-maroon** | `#1E1411` → `#8E524D` | `#A8645C` at 30%, r 760 at (760, 1700) | `#5A2E2A` / `#3A2420` | A trap is about to be exposed: offers, discounts, hidden fees, scams, myths, "healthy" products, misleading labels |
| **TH-case** | `#050805` → `#135C2C` (world W-case) | none | `#135C2C` / `#0B1F10`; `accent` `#40E87A` | F-C story episodes only |

Rules:
- One theme per reel, declared in the reel header. The topic rule above decides it; when a reel is half mechanics and half trap, the **hook's** topic decides.
- F-C always uses TH-case; F-A and F-B never do.
- The buyer's brand colours (BV-02) land on `primary` and `accent`; the packs keep their own world hues, because the hue carries the topic.
- Every pack passes the contrast check against `paper` text (PV-8); `veos tokens` reports it.

### 4.4 Grades
- **Footage:** not regraded in F-A and F-B (the room keeps its natural warm light).
- **GR-case-mono** (F-C): the presenter clip and the stills are monochrome (`grayscale(1) contrast(1.12) brightness(0.92)`) with the accent hue isolated on one object. **Engine status:** the grade capability is not installed yet (Engine request ER-3). Today, the stills are monochrome because the creator supplies them that way (SH-2 spec) and the presenter clip stays in natural colour. Never fake the isolation by tinting the whole clip green.
- Grade events: none (max 0 per reel).

### 4.5 Rules
- ≤ 3 bright hues per frame (`max_bright_per_frame: 3`); a typical frame uses one (`data` or `accent`) plus at most one tag colour.
- Coloured text never sits directly on the world: red and green text always sits inside a filled chip (`bad`/`good` with `paper` text) or a white card.
- The world never changes colour mid-reel.
- Footage is not regraded, except GR-case-mono in F-C.

**Must match `tokens.json`** (roles, themes, worlds).

---

## §5 Type & caption system

### 5.1 Font map `[slots DNA; families TUNE within the font class]`
| Slot | Family | Weights | Font class (TUNE boundary) | Used for |
|---|---|---|---|---|
| `display` | Poppins | 600 / 700 / 800 | geometric sans 500–800 | row titles, labels, panel titles, summary lines, chips, tags |
| `body` | Poppins | 500 / 600 | geometric sans 400–600 | captions, sub-labels, micro-labels, explain lines |
| `numeric` | Poppins | 700 / 800, `font-variant-numeric: tabular-nums` | geometric sans 700–800 with tabular figures | every figure |
| `title` | Poppins | 800, line height 0.86 | geometric sans 800 | the F-C staggered title |

Allowed swaps (TUNE): Plus Jakarta Sans, Jost, Inter Tight (all bundled). Never a serif, a condensed face or a rounded display face. Hindi (Devanagari) captions and labels fall back to Noto Sans Devanagari 500/700.

### 5.2 Headline element `[COND]`
F-A and F-B: **`none`** (`type.headline.kind: none`). The claim is carried by the first caption sentence and the board itself; the F-B panel title (P-18) is a label, not a headline.

F-C: **`title_card`**, lifetime `hook`:

| Property | Spec |
|---|---|
| Text | 2–4 lowercase words in 3 staggered lines ("money / doesn't / behave"), Poppins 800, 150 px (TUNE 130–170), line height 0.86, tracking −1% |
| Layout | line x indents 64 / 300 / 110; tops y 170 / 299 / 428; ≤ 3 lines, ≤ 4 words |
| Colour | each line builds grey `#8C8C8C` → `paper` |
| f0 | the episode label ("episode one", 28 px `accent`) is on at f0; line 1 starts at 0.60 s, line 2 at 0.70 s, line 3 at 0.80 s (v04: 0.62 / 0.70 / 0.78) |
| Build | per line: blur 14 → 0 px, opacity 0 → 1, 3 f ease-out, no rise; each line lands grey and whitens over 10 f, so all three are white by ≈ 1.0 s (v04 @ 0.62–1.02) |
| Life | the chapter line ("that phone call", 56 px, 700) types under it from 1.6 s (1 character per frame) after a 160 × 4 px accent rule wipes in (6 f) |
| Exit | at ≈ 3.2 s the whole card (title, rule, chapter, prop) fades out over 4 f, then a hard cut into still 1 (T-6; v04 @ 3.20–3.36) |
| Read | ≤ 1.5 s |

### 5.3 Caption system profile `[DNA mechanics; fonts TUNE; language VAR]`
**CS-1 "Quiet sentence"** (`extends: lib:warikoo`), the default for every layout:

| Group | Value |
|---|---|
| Mode | `full` · role `support` · `mute_safe` |
| Chunking | unit `sentence`; 4–9 words per chunk (mean ≈ 6.5); ≤ 44 characters per line (the real lines run to 43 characters on one line, x 130–949, e.g. "One offer will be 30% off, another 20% off."; the E3 registry cap is 44); ≤ 2 lines (prefer 1); never split a name, a number or its unit ("₹2.5 lakhs" stays together); break on `. ? !` and on pauses ≥ 0.9 s; punctuation kept |
| Timing | lead 2 f before the first word; ≥ 0.25 s per word; tail 0.25 s; swap = **hard cut, 0 f** (the next sentence replaces the last on one frame; on a jump cut it lands on the cut frame; measured v01 @ 12.08, v03 @ 7.84, v04 @ 0.94); a pause ≤ 0.6 s holds the last chunk |
| Skin | `body` Poppins **500**, **36 px** (`TC-subtitle`, E3), line height 1.25, sentence case as spoken, tracking 0, `paper`, no stroke, shadow `0 1 4 rgba(0,0,0,.65)`, no container |
| Position | F-A and F-C: `inside_footage`, bottom edge 22 px above the presenter window's bottom edge, centred, max width 840 px (measured: Poppins ≈ 37 px, glyph band y 540–567 in a window ending at 567). F-B: `fixed_y`, centre y 1462, max width 800 px. `avoid_face` on |
| Emphasis | **none**. No bold, no colour, no size change, ever |
| Variants | karaoke, tiers, duet, stack: none |
| Hide | during T-7 (the end card) and any `captions.hide` range; captions never show on the end card |
| Language | Latin script by default (`transliteration: keep_english_terms`, spelling normalised); Devanagari supported (`hi/hi/Deva`); profanity masked `inner` (`S**T`); glossary from the creator's brand names |

**CS-2 "Quiet sentence on scrim"** (fallback): identical to CS-1, but on a pill (`ink` at 55%, radius 10, padding 6/16, no shadow). **Use it for the whole reel** when the take is bright behind the chin line (a white wall, window light) so that CS-1 measures below 7:1 in `veos measure`. Never mix CS-1 and CS-2 in one reel.

### 5.4 Other text systems
| System | Class | Recipe | Hold |
|---|---|---|---|
| Row label (P-01) | TC-label 32 px, redundant | `display` 800 caps, tracking 0.04, `paper` on the world | while the row lives |
| Micro-label | TC-label 28 px, redundant | `body` 500, `muted` on white / `paper` at 80% on the world; ≤ 4 words, taken from the spoken line or from the fixed set {you think, you actually get, you pay, you get, a year, a month, was X, saved, you think} | with its value |
| Row title (P-13) | TC-label 44 px | `display` 700, `paper`, ≤ 18 characters | while the row lives |
| Sub-label | TC-label 32 px, redundant | `body` 500, `paper` at 85%; ≤ 4 words taken from the spoken sentence of that row. If the words are not spoken, set it at 40 px | with the row |
| Value chip (P-02) | TC-display 48 px | `numeric` 800 `ink` on a white chip; unit line 28 px `muted` under it | with the row |
| Reality tile (P-15) | TC-display 64 px (final 96 px) | `numeric` 800 `ink` on white, micro-label under it | to the end of the list |
| Struck value (P-14) | TC-label 40 px | `numeric` 700 `paper` at 75%, strike 4 px `bad` | to the end of the list |
| Rank numeral (P-11) | TC-display 100 px | `numeric` 800; unlit `ghost`, lit `paper` | whole list |
| Chip tab (P-12) | TC-label 28 px caps, redundant | `display` 700, tracking 0.08; pill h 44, radius 22; unlit: `ghost` fill + `ink` text; lit and past: `paper` fill + `ink` text | whole list |
| Status tag (P-03 / P-04) | TC-label 28 px, redundant | outline: 2 px `paper` border, caps, `paper` text; filled: `bad`/`good` fill, `paper` text, sentence case ("Cheaper?") | with its row |
| Panel title (P-18) | TC-label 44 px | `display` 600 `paper`, left-aligned at x 64 | per section |
| Parameter chip (P-21) | TC-label 28 px, redundant | `body` 600 `ink` on `paper` at 92%, pill h 44 | whole calculation |
| Explain line (P-26) | TC-label 40 px | `body` 500 `paper`, left-aligned, ≤ 36 characters, "<Method>: <how>" pattern | to the end of the section |
| Summary line (P-09 / P-10) | TC-label 44 px + helper 32 px (redundant) | `display` 700 `paper` centred; helper `body` 500 at 80% | ≥ 2.0 s |
| Total card (P-06) | TC-display 56 px + sub-line 28 px | white card, `numeric` 800 | to the end |
| Ledger counter (P-40) | TC-display 56 px + header 24 px (TC-legal) + sub 28 px (redundant) | `numeric` 700 `accent`, right-aligned to x 1016, `accent` glow 28 px at 45% for 12 f after each landing | whole F-C body |
| Case tag (P-39) | TC-label 28 px, redundant | `body` 600 `paper` at 85% + 7 dots (8 px, gap 8; lit `accent`, unlit `paper` at 30%) | whole F-C body |
| Disclosure | TC-legal 24 px | `body` 500 `paper` at 75%, inside the sponsor card's top-right | the whole sponsor card |
| Credit | TC-legal 24 px | inserts toolkit default | with the insert |

### 5.5 Language and number rules
- Spelling: English words and brand names exact; Hinglish captions (when chosen) phonetic but consistent within a reel.
- Numbers on screen are always digits written by `ctx.fmtNum` (never typed): `₹1,31,190` (full, for computed amounts), `₹75 L` / `₹1.25 Cr` (short, for round amounts on chips and tiles), `44%` (percent, 0–1 decimals as stated), `2x` (ratios as spoken).
- **Chip rule:** a value the script says as "X lakh" or "X crore" uses `style: short`; a computed or exact amount uses `style: full`. One style per figure for the whole reel.
- Numbers follow the language: Indian grouping and ₹ for Hinglish / Hindi; international grouping (`$120,000`, `$1.2M`) for English (the default). Never mix both in one reel.
- Units: metric; non-money units through the format's `suffix` (" kcal", " g", " h", " km").
- Devanagari: no italics, no caps; tabs and tags keep Latin digits.
- The ₹ glyph is in Poppins; no pre-painting is needed.

---

## §6 Hook system

**Hook title (every style, 8 Oct 2026; above anything below):** the on-screen title promises the viewer something: an outcome they want, a curiosity gap, or who it's for ("How to go viral as a doctor creating content", not the label "Reels for Doctors"). It doesn't have to repeat the spoken words; it has to be true to what the reel delivers. A title shown as someone's words (in quotes) is still word for word. This section sets the title's shape (lines, sizes, word limits, case, the keyword device), never its voice. Write 8–10 candidates from the formulas below plus the proven patterns ("How to X as a Y", "Why your X isn't working", "The X nobody tells you", "Stop doing X", "Your X vs mine", a number or a contrast), score them on outcome, curiosity, who it's for and brevity, check the best against the stopper tests, and pick; any "write 3" below means this, and the next two go to the storyboard as alternates. A style with no on-screen title applies this to its post title.

### 6.1 Stopper tests
| Test | This style's number |
|---|---|
| ST-2 Mute | With the sound off, the first 3 s show the subject (caption) and the first quantity (board) |
| ST-3 Motion at f0 | The first board element enters on f0; the presenter is live |
| ST-5 Change count | ≥ 5 weighted SCs in 0–3 s (F-C ≥ 4) |
| ST-6 Payoff-by | First value on screen by 1.0 s (F-A, F-B); the title is complete by 3.0 s (F-C) |
| ST-4 Read time (F-C only) | The title reads in ≤ 1.5 s |

ST-1 (thumbnail) is not used: the style's cover is the post title, not frame 0.

### 6.2 Default archetype: HA-07 "Live number / ledger open" `[DNA]`
The spoken pattern is **state the subject's number, then start building the ledger under it**: "<Subject> earns ₹X a year. I earn ₹Y. But the house runs on my salary." There is no title, no tease and no question card; the reel starts mid-explanation with a quantity.

**Opening O-1 "Row build" (F-A, L-BUILD; from v01):**

| t (s) | Beat | Tone | On screen (board scene `board-1`, z3, kind `ledger`) | Caption | Motion (30 fps) | Cue |
|---|---|---|---|---|---|---|
| **0.00 (f0)** | Claim sentence starts | explain | Presenter live in the inset. Row-1 label "<NAME>" + micro-label "<whose / what>" entering | "<Subject> earns ₹X a year." (on from f0) | label: opacity 0 → 1, rise 6 px, 6 f | — |
| 0.13 | — | explain | Empty bar wipes in L → R under the label (x 64 → 600), grey at its leading edge, white as it grows | same | width 0 → 536, 7 f ease-out (v01 @ 0.12–0.36) | — |
| **≤ 1.0 (on "X")** | **Payoff** | explain | The chip pops right of the bar: a small `ghost` pill grows into the white chip "₹X L" + unit line "a year" | same | scale 0.25 → 1.08 → 1.00 over 4 f, `ghost` → white as it grows, value legible from f2 (v01 @ 0.40–0.52) | **reveal** |
| 1.0–2.0 | hold | explain | — | swap to "<Second subject> earns ₹Y." | caption hard swap | — |
| 2.0 | Row 2 | explain | Row-2 label + micro-label enter in lane 2 | same | 6 f | — |
| 2.13 | — | explain | Row-2 bar wipes in (on the same scale as row 1) | same | 7 f | — |
| on "Y" (≈ 2.5) | value 2 | explain | Row-2 chip: ghost → "₹Y L" | same | as above | — |
| on the twist word (≈ 2.8–3.2) | the turn | claim | Outline tag under row 2 ("RUNS THE HOUSE") | "But <the twist>." | rise 6 px, 6 f | — |

Weighted SCs in 0–3 s: bar 0.13, chip ≈ 0.8, row-2 label 2.0, bar 2.13, fill 2.5, tag 2.9, plus two caption swaps × 0.5 = **7** (target ≥ 5; the f0 entrance is not counted).

**Opening O-2 "Rank skeleton" (F-A, L-LIST; from v02, with its weak frame 0 fixed):**

| t (s) | Beat | On screen | Caption | Motion | Cue |
|---|---|---|---|---|---|
| **f0** | Promise sentence | Presenter live. The S-tabs row rises in (N pills, all `ghost`) | "These N <things> <hurt> you." | each pill fades in over 2 f, 3 f stagger (v02 @ 1.24–1.52) | — |
| 0.20 → 0.20 + 0.13·N | — | Rank numerals 1…N appear one by one in `ghost` | same | each: fade 3 f, 5 f stagger, no rise (v02 @ 1.40–1.88) | — |
| **≤ 1.0** | Payoff | Numeral "1" lights `paper`; tab 1 lights white (E6 swap) | same | colour 4 f | **list cue** |
| on item 1's claim word (≈ 1.5–2.5) | Claim | Row-1 title slides in from x 136 → 176 with its claim ("30% + 20% off") | "One offer is <claim>." | slide 40 px + fade, 8 f | — |
| +0.2 | — | Sub-label ("Stacked discounts") | same | fade 6 f | — |
| on "you think / we feel" | Claim value | "50%" + "you think" in grey, right of the title | "We feel we're getting <X>." | fade + rise 6 px, 6 f | — |
| on "No / only / actually" | **Reality** | The strike wipes across "50%" (6 f); the white tile "44%" + "you actually get" pops at x 776 | "It's only <Y>." | tile pops from a `ghost` pill: scale 0.25 → 1.08 → 1.0, 4 f; the strike snaps across "50%" in 2 f on the same beat (v02 @ 7.40–7.52, 13.54–13.62) | **reveal** |

SCs in 0–3 s: 5 numerals, the light-up, the row title and two caption swaps ≥ 7.

**Opening O-3 "Dual stat question" (F-B, L-CALC; from v03):**

| t (s) | Beat | On screen (panel scene `calc`, z3, kind `ledger`) | Caption | Motion | Cue |
|---|---|---|---|---|---|
| **f0** | The question starts | Panel title "Would you choose" (44 px) + ghost card A (`data` at 30%) | "Would you choose <option A>" | title fade 6 f; card fade 4 f | — |
| 0.17 | **Payoff** | Card A fills: "8%" (132 px) + unit "loan" (28 px) | same | `data` opacity 0.3 → 1 over 4 f; figure pop 1.05 → 1 over 6 f | **reveal** |
| 0.83 | Tag | The "Cheaper?" `good` chip drops onto card A's top edge | same | drop 12 px + fade, 6 f | — |
| 1.5 | Option B | Ghost card B → fills `night` "11%" + "loan" | "or <option B>? Let's see." | as card A | — |
| 1.83 | Axis | A white "Total <quantity>" bar skeleton slides up under both cards | same | rise 16 px, 8 f | — |
| 2.17–2.47 | **T-3 morph** | The cards shrink and blur into the two bar badges; the title swaps to the real question "Which <option> costs you more?" | same | 9 f (§9; v03 @ 2.16–2.44) | — |
| on the first parameter word (≈ 2.8) | Parameters | Parameter chip 1 ("₹2.5 lakh loan") | "The loan is ₹2.5 lakhs." | fade + rise 6 px, 6 f | — |

### 6.3 Allowed alternates `[DNA list; VAR choice per reel]`

**HA-02 "Headline + proof"** (F-A L-LIST, when the creator wants a stated title). For the first 2.5 s the board's top lane carries a 44 px title in the summary-line recipe ("<N> <things> that cheat you"); the proof is item 1's reality tile by 2.5 s.

| t | On screen | Caption |
|---|---|---|
| f0 | title line (P-09 recipe, lane 1) + presenter + tabs rising | the promise sentence |
| 0.4–1.2 | numerals 1…N | same |
| ≤ 2.5 | item 1: claim → strike → reality tile (P-15) = the proof | item 1's sentences |
| 2.5–3.0 | the title fades (6 f); row 1 settles in lane 1 | — |

Example (finance): title "5 offers that cheat you" → tile "44%". Example (fitness): title "5 'healthy' snacks that aren't" → tile "21 g sugar".

**HA-12 "Thesis typography"** (F-C default):

| t (s) | Beat | On screen | Caption | Motion | Cue |
|---|---|---|---|---|---|
| **f0** | "Episode number <n>:" | W-case world, presenter clip live (L-cinema-top), episode label "episode <n>" (`accent`) on, prop resting on the lit table plane (y 700–900) | "Episode number <n>:" | the prop idles (1° sway, 60 f period) | — |
| 0.60 / 0.70 / 0.80 | Title | The title lines build (§5.2) | "<Thesis sentence>." from ≈ 0.95 | 3 f per line; grey → white by 1.0 s | — |
| 1.2–1.6 | Prop life | The prop's corner lifts and curls | same | rotateX 0 → 35°, 12 f | — |
| 1.6–2.6 | Chapter | The accent rule wipes in; the chapter line types ("<chapter name>"); the prop flips and tumbles out of frame | "This episode is called '<chapter>'." | type 1 character/f; tumble 30 f with 6 px motion blur | **reveal** (prop flip) |
| **≈ 3.2** | Payoff | T-6: the title card fades out (4 f), hard cut into still 1; the case tag fades in at y 140 | "<Date / place>." | 4 f + cut; tag 4 f | — |

Examples: finance — "money / doesn't / behave" + "that phone call"; fitness — "the / perfect / diet" + "the 1,200-calorie summer".

### 6.4 Hook pairs by topic `[NICHE]` (pair type: claim → evidence; HA-07 / HA-02)
| Niche | Topic | Claim (grey, struck or questioned) | Evidence (number + where it comes from) | Card type |
|---|---|---|---|---|
| Finance [NICHE: example] | Stacked discounts | "30% + 20% off = 50% off" | 44% (`stacked_discount` of 30 and 20; script) | P-14 → P-15 strike reveal |
| Finance | Flat vs reducing loan | "8% is cheaper than 11%" | 8% flat ₹2,00,000 vs 11% reducing ₹1,63,250 over 10 years on ₹2.5 L (`flat_rate_interest`, `reducing_balance_emi`) | P-19 → P-20 → P-24 race bars |
| Finance | Two incomes | "Two salaries = double safety" | one salary stops: ₹50 L → ₹0, commitments unchanged (script) | P-01/P-02 rows → P-07 zero-out |
| Finance | Small SIP | "₹5,000 a month is too small to matter" | the value after 20 years at the stated rate (`compound` with a contribution) | P-23 slider + P-24 bars (invested vs value) |
| Finance | Cashback | "10% cashback on ₹20,000 = ₹2,000" | capped at ₹500 → 2.5% (`ratio`) | P-15 |
| Fitness [NICHE: example] | "Healthy" granola | "A healthy breakfast" | sugar grams per serving (script, or the pack label the creator films) | P-15 with a creator shot (P-51) |
| Fitness | Steps vs food | "10,000 steps lets me eat anything" | kcal burned vs kcal in one snack, on the same scale (script) | P-24 race bars |
| Fitness | Protein bars | "A protein bar = a protein meal" | protein grams per 100 kcal, bar vs meal (`ratio`) | P-34 two-column ledger |
| Fitness | Weekend cheat meals | "Two cheat meals don't matter" | the weekly surplus in kcal (`sum`) | P-01 rows → P-06 total |
| Fitness | Walking pace | "Walking slowly burns the same" | kcal per 30 min at two paces (script) | P-19 stat cards → P-24 |

The editor writes this reel's pair at P7 and appends it here in the buyer's copy.

### 6.5 Headline writing `[DNA formula; NICHE examples]`
F-A and F-B have no on-screen headline. What plays the headline's role is the **first caption sentence** plus the **post title**:
- **First-sentence formula:** `<subject> <verb> <number>`, `These <N> <things> <hurt> you` or `Would you choose <A> or <B>?`. 4–9 words, containing a number or a count; no adjectives like "shocking".
- **Post title formula (Hinglish by default, VAR):** `<NUMBER or KEY NOUN in caps> + <Hinglish clause> + <1 key word in caps>!` ("5 Online OFFERS Jo Aapko CHEAT Kar Rahe Hain!"); ≤ 9 words; exactly 2–3 words in caps.
- **F-B panel title:** a question ending in "?" ("Which loan costs you more?"), ≤ 30 characters; later sections swap to "How did this happen?" and "Same trap in <second case>".
- **F-C title:** 2–4 lowercase words that state a thesis ("money doesn't behave"), plus a 2–4 word chapter name.
- **Write 3 and pick by the stopper tests.** Banned: clickbait adjectives, emoji, "you won't believe", counts that don't match the list.

### 6.6 Hook sound
The hook may carry one cue: the **reveal** of the first value (O-1, O-3), the **list cue** on the first lit numeral (O-2), or the prop flip (HA-12). The bed enters after the hook (§11).

### 6.7 CTA `[DNA device set; VAR values]`
| Device | Spoken pattern | On-screen element | Hold | Where |
|---|---|---|---|---|
| `end_card` (default) | "<Moral sentence>. Do you agree?", then silence or "Watch this next." | P-44: black end card with the creator's next-video thumbnail (SH-3, else FB-3), a play chip, a 2-line title and a dashed curved arrow pointing down-right | 2.5–3.5 s | the last 2.5–3.5 s |
| `comment_keyword` | "Comment {{BV-08.keyword|KEYWORD}} and I'll send you <deliverable>." | P-45: white card in the board footer (or the panel bottom): "Comment" 32 px + **{{BV-08.keyword|KEYWORD}}** 72 px caps `ink` on `primary` | ≥ 1.5 s, to the end | the last sentence; then T-7 |
| `link_bio` | "The link is in my bio." / "Link given below." | P-46: white chip "Link in bio" + 3 animated chevrons pointing down | ≥ 1.5 s | the end, or with the sponsor card |
| `post_only` | none | none (the reel ends on the moral + question) | — | — |

The chosen device for this copy: **{{BV-08.device|end_card}}**. No silence is needed before the CTA (calm style); the CTA sentence follows the moral directly. End cards are specified in §25.

---

## §7 Structure & cadence `[DNA]`

### 7.1 Structure types (one per reel, declared in the reel header)
| ID | Format | Type | Arc (with share of runtime) | Source |
|---|---|---|---|---|
| **L-BUILD** | F-A | `ledger` | Parameters (rows of named quantities, 0–15%) → build (what they cover: tiles, total, 15–45%) → **stress test** ("what if X stopped / doubled?": zero-out or change, 45–65%) → moral (summary line, 65–90%) → question to the viewer + CTA (90–100%) | v01 |
| **L-LIST** | F-A | `ledger` (list) | Promise ("these N…", rank skeleton, 0–5%) → items 1…N, each with the identical ritual (7.3), ≈ 6–8 s per item → payoff on the last item (the biggest reality tile) → CTA | v02 |
| **L-CALC** | F-B | `ledger` | Question (two options, 0–6%) → parameters (chips, 6–12%) → step through the parameter (slider + race bars, 12–55%) → final verdict (leader chip final, 55–60%) → **why** (mechanism: segment bars + explain lines, 60–82%) → **transfer** ("same trap in <second case>", two-card stack, 82–92%) → sponsor or CTA (92–100%) | v03 |
| **S-CASE** | F-C | `story` | Title card (0–6%) → setting (date, place, stills, 6–15%) → the event chapters (stills every 1.5–3 s with the ledger changing state, 15–80%) → the turn (the twist, 80–92%) → the open question (92–100%; the next episode pays it off) | v04 |

### 7.2 Markers
| ID | Marker | Recipe | Used in |
|---|---|---|---|
| **SM-rank-list** | Rank numerals + chip tabs | N `ghost` numerals pre-drawn at f0–1.0 s; the active one turns `paper` on the ordinal word; S-tabs show "<NOUN> n" pills (future `ghost`, active and past `paper`) | L-LIST (default marker of the style) |
| **SM-panel-title** | Panel title swaps | The F-B question title changes per section ("Which loan costs you more?" → "How did this happen?" → "Same trap in insurance") | L-CALC |
| **SM-case-tag** | "case 01 / 07" + 7 dots | Persistent from the first still (S-case-tag); the episode's dot lit `accent` | S-CASE |
| none | spoken only | L-BUILD reels have no markers: the rows are the structure | L-BUILD |

Numbering is ascending (1 → N); the tabs never count down.

### 7.3 Unit ritual (identical for every item)
**L-LIST item ritual (≈ 6–8 s; v02 @ 0:02.5–0:39):**
1. **Ordinal word − 2 f:** the item's tab lights `paper` (E6 swap, 4 f) and its numeral turns `paper` (4 f). List cue SFX (the one allowed repeat).
2. **On the item's name (≤ 0.3 s later):** the title slides in from the left (x 136 → 176, 8 f), then the sub-label (+0.2 s, fade 6 f).
3. **On the claim value word:** the grey claimed value + "you think" appear (6 f).
4. **On the verdict word ("only", "actually", "but", "No"):** the white reality tile pops from a small `ghost` pill (scale 0.25 → 1.08 → 1.0, 4 f) with its micro-label, and the strike snaps across the claimed value in 2 f on the same beat (v02 @ 13.54: tile first, strike 2 f later). Reveal cue.
5. **Hold ≥ 1.2 s** with the next caption; then the next item.
6. The **last item escalates:** its reality tile grows to the 96 px variant (P-16) and a saved-note (P-17) sits under it.

**L-BUILD row ritual:** label (fade 3–6 f) → bar wipe (7 f) → chip pop on the number word (pill → white value, 4 f, P-02) → optional status tag on the role word (P-03).

**L-CALC step ritual (per parameter step, ≈ 3–5 s):** the slider handle moves to the step 8 f before the step word → option A's bar grows and its value rolls to land on its spoken number → option B's bar and value land on theirs → the leader chip hops if the leader changed (P-22).

**S-CASE beat ritual (≈ 1.5–3 s):** hard cut to the still on the noun or place word (T-5) → the still holds static (measured: no Ken Burns, drift ≤ 1% on 28 stills) → the ledger changes state only on a spoken money word (P-40). On the inciting event and on the turn (≤ 2 per reel) the cut becomes a T-9 white flash.

### 7.4 Open loops and re-hooks
- **Loops used:** "Let's see" (L-CALC opening), "What if <X> stopped?" (L-BUILD stress test), the unlit rank numerals (L-LIST), "But how did all this happen?" (S-CASE ending, paid off in the next episode; the episode itself pays off every number it shows).
- **Payoff rule:** every loop opened inside the reel is paid on screen within the reel, except the S-CASE closing question, which names the next episode.
- **Re-hooks:** class `short` needs none. When BV-17 moves a reel to `standard` (60–90 s), add one re-hook at 40–55%: the stress-test question line (P-10) in L-BUILD, the panel-title swap "How did this happen?" in L-CALC, the last tab still `ghost` in L-LIST.
- **Intro cap:** hook + any series card ≤ 15% of runtime (F-C title card ≤ 3.0 s).

### 7.5 Rhythm and energy curve
Calm and even: a reveal every ≈ 6–8 s, with 2–4 smaller builds between reveals. No comedy beats. The last item, step or ledger state is the biggest (a 96 px tile, the final leader verdict, the "recovered" state). The end is quiet: a summary line, a question to the viewer, the end card.

### 7.6 Cadence (state changes)
| Token | F-A | F-B | F-C |
|---|---|---|---|
| `sc_per_10s` | 4–7 | 4–7 | 3–6 |
| `hook_sc_3s` | 5 | 5 | 4 |
| `max_gap_s` (weight-1 SCs) | 2.5 | 2.5 | 3.0 |
| `max_static_s` | 2.5 (live footage counts as continuous motion) | 2.5 | 3.0 |
| `caption_weight` | 0.5 | 0.5 | 0.5 |
| `cuts_per_min` | A-roll jump cuts, same framing, at sentence ends: measured ≈ 9/min (v01 7 in 45 s, v02 6 in 40 s; median shot 5–6 s). Not enforced: a clean single take is fine | ≈ 16/min (v03, median shot 3.3 s, 1.6–8.8 s) | still cuts ≈ 34/min (v04: 28 stills, median 1.56 s, 0.56–2.96 s); presenter jump cuts rare |

What counts as an SC here: a board row/chip/tile/tag/bar entering or changing (declared as the board scene's `events`), a counter landing, a slider step, a still cut, the T-3 morph, a panel replace, a caption swap (× 0.5). The full-frame cut detector reads 0 cuts (the jump cuts sit inside a small window and never change the framing); that is expected. Measured board cadence: 3–10 visible changes per 10 s, longest still board 7–12 s in F-A while the presenter talks (v01 @ 30.5–43.2), ≤ 2.7 s in F-B and F-C.

---

## §8 Visual system: graphics, B-roll and patterns

### 8.1 Graphics role and budget
- `graphics: primary` (F-A, F-B): cards on screen 90–100% of the body; ≥ 25 patterns available, typically 10–16 used per 60 s.
- F-C `support`: stills carry the picture; furniture (case tag, ledger counter) is on 90%; cards ≤ 15%.
- **Numbers become pictures:** every spoken quantity becomes a chip, tile, bar, slider step or counter; comparisons use one axis; mechanisms become segment bars or explain lines.

### 8.2 Families
| ID | Family | Source class | The buyer supplies |
|---|---|---|---|
| **B-1** | Ledger rows (labels, bars, value chips, tiles, totals) | engine | — |
| **B-2** | Claim vs reality list (numerals, tabs, claims, strikes, reality tiles) | engine | — |
| **B-3** | Calculator panel (title, parameters, stat cards, slider, race bars, segments, explain lines) | engine (`VEOS.data`) | — |
| **B-4** | Status chips and tags | engine | — |
| **B-5** | Hero and gap counters | engine (`VEOS.data.counter`) | — |
| **B-6** | Case-file furniture (title stagger, episode label, case tag, ledger counter) | engine | series name/number (BV-13) |
| **B-7** | Story stills | buyer-owned (SH-2); substitute P-41 object plates | 15–25 monochrome stills per episode |
| **B-8** | Props | buyer-owned (SH-5, optional); substitute: a drawn note card | an alpha PNG prop |
| **B-9** | Brand and CTA (sponsor card, end card, keyword card, link chip) | engine + buyer assets | sponsor logo (SH-4), next-video thumbnail (SH-3) |
| **B-10** | Third-party moments (an advert, an app's offer screen, a post, a headline, a product) | creator-supplied third-party; else **created** with `renderer/inserts.js` (§12.5) | the files, only if they own or hold them |

**Rule B0 (one board per screen):** in F-A and F-B everything inside the board or panel is drawn by **one bespoke scene per section** (z3, `kind: "ledger"`, `text_class: "TC-label"`, `exception: "E3"`, bound to its figures with `figures`, `lands`, `scale` and every internal change declared in `events`). This keeps G2 at two text elements (board + captions) and lets rows nest without G1 declarations. Use `VEOS.data.bars` / `slider` / `counter` directly only when that helper is the **only** text on the board for its span; otherwise reproduce the helper's look inside the board scene with `ctx.fig`, `ctx.figAt`, `ctx.fmtNum` and `VEOS.data.width`. Separate scenes are allowed only for: the sponsor card, the keyword card, the end card, F-C stills, the case tag, the ledger counter and inserts.

### 8.3 Pattern specs
Frames at 30 fps. Every value comes from `plan/figures.json` and is written by `ctx.fmtNum`. "Board" = the section's board scene (B0).

**Ledger rows (B-1)**
| ID | Name | Type | On screen | Motion recipe | Use when | Text class | Needs |
|---|---|---|---|---|---|---|---|
| **P-01** | Label row | overlay | Caps label (32 px) + micro-label (28 px) + an empty white bar (h 56, radius 10) whose length is the value on the row's shared scale | label fade 3–6 f → bar width 0 → full, 7 f ease-out (grey leading edge whitening as it grows), starting 0–3 f after the label | a named quantity is introduced ("Ruchi earns…", "Option A takes…") | TC-label | figure (bar length) |
| **P-02** | Value chip (ghost → fill) | figure | A grey `ghost` placeholder chip (w 240, h 96, radius 12) right of the bar, then white with the value (48 px) + unit line (28 px `muted`) | one 4 f pop on the number word: a small `ghost` pill (scale 0.25) grows to 1.08 and settles to 1.00, turning white as it grows, the value legible from f2 (v01 @ 0.40–0.52); a value that changes later rolls 10 f | every spoken value of a row | TC-display | figure; lands |
| **P-05** | Tile wrap | overlay | Small white tiles (w 284, h 64, radius 10, 22 px gaps; `ink` 32 px) flowing into a 3-column grid at x 64–960 (clear of the IG button column x > 970) under a micro header ("what my ₹50 L covers") | header fade 6 f; each tile: fade + rise 8 px, 6 f, on its spoken item word; ≥ 0.6 s between tiles | a list of things a quantity pays for, contains or causes | TC-label (redundant) | — |
| **P-06** | Total card | figure | A wider white card centred (w 420, h 120): total 56 px + sub-line 28 px ("combined, every year") | rise 10 px + fade, 8 f; total rolls 12 f to land on the spoken total | a sum or combined value is said | TC-display | figure (`sum`) |
| **P-07** | Zero-out | state | A row's value counts down to 0 (12 f); its bar becomes an empty **dashed `bad` outline** (2 px, dash 10/8); the chip's unit line changes to "was ₹50 L" (`muted`) | count-down 12 f landing on "stopped / zero / gone"; bar fill fades out 6 f while the dashed outline draws 8 f | the stress test removes a quantity | TC-display | figure (step to 0) |
| **P-08** | Header swap | state | The micro header text changes in place ("what my ₹50 L covers" → "none of this gets halved") | E6 hard swap with a 4 f cross-fade inside a fixed rect | the meaning of a group changes | TC-label | E6 |
| **P-09** | Summary line | overlay | A bold centred takeaway (44 px `paper`) + helper line (32 px, 80%) in the footer lane | line: fade + rise 8 px, 8 f; helper +6 f; hold ≥ 2.0 s | the moral ("income drops instantly. / the commitments do not.") | TC-label | — |
| **P-10** | Stress-test question | overlay | The same footer line as a question ("what if one salary stopped?") | as P-09; replaced by the answer's summary line with a 6 f cross-fade (E6) | the "what if" turn of L-BUILD | TC-label | — |
| **P-52** | Conversion row | figure | A row "₹100 a day" → arrow → "₹36,500 a year" (two chips joined by a 3 px `paper` arrow that draws 6 f) | left chip as P-02; arrow 6 f; right chip rolls 12 f landing on its word | a per-day / per-unit amount becomes a per-year / total amount | TC-display | figure (`per_period` / `unit_convert`) |

**Claim vs reality list (B-2)**
| ID | Name | Type | On screen | Motion recipe | Use when | Text class | Needs |
|---|---|---|---|---|---|---|---|
| **P-11** | Rank skeleton | overlay | N rank numerals (100 px) stacked at x 64, pitch 156 px, all `ghost` | fade 3 f each, 5 f stagger, no rise, all on by 1.0 s | the promise of a count ("these 5…") | TC-display | — |
| **P-12** | Chip tabs | state | N pills "<NOUN> n" (28 px caps) across S-tabs; future `ghost`, active/past `paper` | fade 2 f each, 3 f stagger at f0; each lights by an E6 swap (4 f) on its ordinal word | every L-LIST reel (with P-11) | TC-label | E6, slot S-tabs |
| **P-13** | Claim row | overlay | The active numeral turns `paper`; the title (44 px) slides in at x 176; the sub-label (32 px) under it | numeral colour 4 f; title slide 40 px + fade, 8 f; sub-label +6 f | the item's name and claim | TC-label | — |
| **P-14** | You-think value | overlay | The claimed value (40 px, `paper` 75%) right-aligned to x 756 + micro "you think" (28 px) under it | fade + rise 6 px, 6 f, on the claim value word | the believed or advertised value | TC-label | figure (the claim as an input) |
| **P-15** | Strike reveal | figure | A 4 px `bad` strike line wipes across the claimed value; the white reality tile (x 720–960, h 120; value 64 px + micro "you actually get") pops beside it | tile: a `ghost` pill pops to full size, scale 0.25 → 1.08 → 1.0 over 4 f, white with its value from f2, on the true-number word; strike snaps L → R in 2 f on the same beat (v02 @ 7.40, 13.54) | the core move of the style: the truth replaces the claim | TC-display | figure (formula: stacked_discount, ratio, diff…) |
| **P-16** | Final tile grow | figure | The last item's reality tile at 96 px in a bigger card (w 330, h 150, x 686) | as P-15 (the same 4 f pop; v02 @ 38.46–38.58), then P-17's strike 4 f later | the last item, to escalate | TC-display | figure |
| **P-17** | Saved-you-think note | overlay | Under the last row, right-aligned: micro "saved, you think" + the struck saving (40 px) | fade 6 f, then strike 6 f on the verdict word | the item's apparent saving is exposed | TC-label | figure |
| **P-34** | Two-column ledger | figure | Two header chips ("you think" grey / "reality" white) over 2–4 paired rows: grey value left, white tile right | header 6 f; each pair: left fade 6 f, then right tile pop 7 f on its word | 2–4 paired claims (fitness labels, ingredient lists, plan features) | TC-label / TC-display | figures |

**Calculator panel (B-3)**
| ID | Name | Type | On screen | Motion recipe | Use when | Text class | Needs |
|---|---|---|---|---|---|---|---|
| **P-18** | Panel title | state | A question title at x 64, y 128–188 (44 px, `display` 600) | first entry fade 6 f; each later swap: old text fades 4 f, new text fades in 6 f in the same rect (E6) | every F-B section start | TC-label | slot S-panel-title, E6 |
| **P-19** | Stat card pair | figure | Two cards (w 456, h 300, radius 14) at y 220: A in `data`, B in `night`; value 132 px `paper` + unit 28 px; ghost (30% opacity) first | ghost fade 4 f; fill on the value word: opacity 0.3 → 1 over 4 f + figure pop 1.05 → 1 over 6 f | the opening "A or B?" | TC-display | figures |
| **P-20** | Cards → bars morph | stage (in-board) | The stat cards shrink and blur into the bar badges of P-24; the panel title swaps at the midpoint | 9 f: the cards shrink and slide to the badge rects with a 24 px horizontal motion blur mid-move (`ctx.blur(px, 0)`, built-in directional blur); the title cross-fades over f5–f8; then the white tracks wipe in L → R (5 f) and the grey skeleton fills extend (5 f) (v03 @ 2.16–2.72) | right after P-19, on "let's see" | — | T-3 |
| **P-21** | Parameter chips | overlay | 2–4 chips (28 px, h 44, gap 12) under the title: "₹2.5 lakh loan", "10 years", "Monthly EMI" | each: fade + rise 6 px, 6 f, on its spoken word | the calculation's inputs | TC-label (redundant) | figure inputs |
| **P-22** | Leader chip flip | state | The `bad` "Costs more" (or `good` "Cheaper") chip straddling the top-right corner of the leading bar hops to the other bar | out: fade + drop 8 px, 4 f; in on the other row: rise 8 px + fade, 6 f, on the verdict word | the leader changes or the verdict is said | TC-label | figures (leader by max) |
| **P-23** | Parameter slider | state | A 6 px track (x 130–930, `paper` 45%) with ticks at each step (40 px labels: 2, 4, 6, 8, 10) and a white handle (Ø 36, `primary`) | the handle moves to the next tick over 8 f, landing on the step word; scale pulse 1.15 over the move | stepping a parameter (years, months, servings, km) | TC-label | figure steps (x); running_state `param` |
| **P-24** | Race bars | figure | Two bar rows (h 100, gap 28): badge (`data` / `night`, 44 px label) + track + fill + value (48 px, right-aligned) on one shared scale | each fill grows over 10 f into the step's `at`; the value rolls 10 f; never re-scaled mid-reel | comparing two options over a parameter | TC-label / TC-display | figures with one `scale_id` |
| **P-25** | Segment bars | figure | Each bar redrawn as N equal segments: flat = N identical blocks; reducing = blocks shrinking step by step (each block's height ∝ that period's value) | the solid fill dissolves into segments L → R, 2 f per segment | explaining why (flat vs reducing, fixed vs declining, linear vs compounding) | — (inside P-24) | figure steps per period |
| **P-26** | Explain lines | overlay | Two lines under the bars (40 px): "<Method A>: <how>", "<Method B>: <how>" | each: fade + rise 6 px, 6 f, on the method word | the mechanism in words | TC-label | — |
| **P-27** | Method tags | overlay | Small tags hanging under each bar badge: "Flat rate" `bad`, "Reducing" `good` | drop 8 px + fade, 6 f, on the method word | naming the method of each option | TC-label (redundant) | — |
| **P-28** | Action chip | overlay | A white chip with the action ("Check the APR statement"), right-aligned under the bars | fade + rise 6 px, 6 f | what the viewer should do | TC-label | — |
| **P-29** | Panel replace | stage (in-board) | The whole panel content blurs out (6 f), the new section's skeleton (empty white cards) rises in (8 f) | T-4 | a transfer to a second case ("Same trap in insurance") | — | T-4 |
| **P-30** | Two-card stack | figure | Two full-width white cards (h 72, at y 220–292 and 312–384) titled "<Thing>" + micro "<what it means>" ("Premium / What you pay", "Cover / What you get"); empty skeleton first | skeleton rise 8 f; each title fades in on its word (6 f) | the second case's two quantities to compare | TC-label | — |
| **P-31** | Check chip | overlay | A white pill (h 44, y 408–452) with a `good` ✓ and the rule ("Look at both, not just one") | fade + scale 0.94 → 1, 6 f | the rule of the transfer | TC-label | — |

**Status tags (B-4)**
| ID | Name | Type | On screen | Motion recipe | Use when | Text class |
|---|---|---|---|---|---|---|
| **P-03** | Outline status tag | overlay | A caps tag (28 px, 2 px `paper` outline, radius 8, h 36) under a row ("RUNS THE HOUSE", "INVESTED") | rise 6 px + fade, 6 f, on the role word | naming a quantity's role | TC-label (redundant) |
| **P-04** | Colour status tag | overlay | A filled tag (`good` "Cheaper?" / `bad` "Costs more", sentence case 28 px) pinned to a card's top edge | drop 12 px + fade, 6 f | an early verdict or a question mark on an option | TC-label (redundant) |

**Hero and gap counters (B-5)**
| ID | Name | Type | On screen | Motion recipe | Use when | Text class | Needs |
|---|---|---|---|---|---|---|---|
| **P-32** | Hero counter | figure | One number (120 px `paper`, centred in the board's free lane) + label (40 px) | `VEOS.data.counter`: roll 18 f landing on the spoken number; pop 6 f | a single number is the point and nothing else is on the board | TC-display | figure |
| **P-33** | Gap counter | figure | The difference between two figures ("₹36,750 more") in a white card under the bars | roll 12 f; `diff` formula | the difference itself is said | TC-display | figure (`diff`) |

**Case-file furniture (B-6) and stills (B-7, B-8)**
| ID | Name | Type | On screen | Motion recipe | Use when | Text class | Needs |
|---|---|---|---|---|---|---|---|
| **P-35** | Title stagger | overlay | §5.2 title card | §5.2 | F-C hook | TC-display | headline |
| **P-36** | Prop float | overlay | The prop (SH-5 PNG, or the drawn note card FB-5) resting on a lit table plane, y 700–900, with a soft contact shadow | idle sway 1°/60 f → corner curl rotateX 0 → 35° (12 f) → flip and tumble out of frame (30 f, 6 px motion blur), ending by 2.8 s | F-C hook | — | asset or FB-5 |
| **P-37** | Episode label + chapter line | overlay | "episode <word>" (28 px `accent`) at y 128; the chapter line (56 px) with a 160 × 4 px accent rule at y 588 | label on at f0; rule wipe 6 f at 1.6 s; chapter types 1 character/f | F-C hook | TC-label / TC-display | series |
| **P-38** | Cinema still | footage-treatment | A creator still (monochrome, one accent object) filling y 0–940, held static (no Ken Burns), a top scrim (`#000` 0 → 55% over y 300 → 0) for the furniture, a mask fade into W-case over y 760–940 | hard cut on the noun/place word (T-5); hold 0.6–3.0 s, median 1.6 s (v04); never two stills of the same subject in a row | every S-CASE beat | — | asset (SH-2), `fx.clip` |
| **P-39** | Case tag | state | "case 01 / 07" (28 px) + 7 dots in S-case-tag | fades in at the first still (8 f); then fixed for the reel | every F-C reel | TC-label | series, slot |
| **P-40** | Ledger counter | state | In S-ledger, right-aligned: "ledger" (24 px TC-legal), the value (56 px `accent`), the state word (28 px: needed / handed over / spent / recovered) | rises in on the first money word (8 f); each change: the state word hard-swaps (E6) and the value counts linearly over 27–45 f (₹60,00,000 → ₹0 in ≈ 1.1 s, v04 @ 20.16), ending on the spoken amount; the `accent` glow 28 px stays on while counting and fades over 12 f | every money change in a story | TC-display | figure (steps with `label`), running_state `ledger`, E6 |
| **P-41** | Object plate (FB-2) | overlay | A Claude-built plate filling y 0–940: dark vignette on W-case, one line object drawn with `fx.icon` (e.g. `phone`, `doc`, `clock`, `car`, `key`) at 360 px in `paper` 70%, its key part in `accent` with a 40 px glow | held static; hard cut like P-38 | a missing still (FB-2) | — | `fx.icon` |
| **P-42** | Closing question hold | overlay | The last state of the ledger + the final caption ("But how did all this happen?"); the still holds 2–3 s | none (hold); the ledger's glow pulses once (12 f) | the S-CASE ending | — | — |

**Brand and CTA (B-9)**
| ID | Name | Type | On screen | Motion recipe | Use when | Text class | Needs |
|---|---|---|---|---|---|---|---|
| **P-43** | Sponsor card | overlay | A dark rounded card (`#14201F` at 96%, radius 14, full board width; h 100 in the F-A footer lane y 1400–1500, h 120 under the F-B transfer cards, y 480–600): logo (SH-4) or wordmark set in type (44 px) at left, a 2 px divider, "Talk to <brand>" (44 px) + "Link given below" (32 px), 3 chevrons (32 px) at right; "Paid partnership" (24 px TC-legal) top-right inside the card | rise 16 px + fade, 10 f (T-8); chevrons fade in one by one (4 f stagger) then pulse in sequence every 24 f | a sponsored reel | TC-label | asset or FB-4, disclosure |
| **P-44** | End card (thumbnail + arrow) | overlay | W-endcard black; the creator's thumbnail (16:9, x 126–954, y 560–1026, radius 16, 2 px `paper` 30% border); a play chip (88 × 62, `paper` fill, `ink` triangle) at x 126, y 1060; the next title in 2 lines (44 px, x 236–954); a dashed curved arrow (8 px `primary`, dash 18/14) from (880, 1200) to (760, 1440) with a 36 px head | hard cut in; the thumbnail + title block slams from scale 2.6 → 1.0 with an 18 px motion blur over 3 f (`ctx.blur(px, 90)`, built-in directional blur); the dashed arrow draws over 11 f from f1, then its head bobs 6 px every 30 f (v01 @ 45.00–45.40) | `end_card` CTA | TC-label | SH-3 or FB-3 |
| **P-45** | Keyword card | overlay | A `primary` card (x 64–960: w 896, h 100, radius 14; never into the IG button column x > 970) in the footer lane y 1400–1500 (F-A) or y 620–720 (F-B), one line: "Comment" (32 px `ink`) + the keyword (72 px caps 800 `ink`). In an L-LIST reel with 5+ rows the board exits first (T-4) and the card sits at y 1000–1100 | rise 12 px + fade, 8 f; one pulse 1.0 → 1.04 → 1.0 on the spoken keyword | `comment_keyword` CTA (`kind: "cta-keyword"`) | TC-display | BV-08 |
| **P-46** | Link chip | overlay | A white pill "Link in bio" (32 px) + 3 chevrons pointing down | fade 6 f; chevrons as P-43 | `link_bio` CTA | TC-label | — |

**Third-party moments (B-10; §12.5)**
| ID | Name | Type | On screen | Motion recipe | Use when | Needs |
|---|---|---|---|---|---|---|
| **P-47** | Quote row | overlay | `fx.quoteCard` (theme `light`, w 952) inside the board's lanes 1–2: the post or claim read aloud, verbatim | built-in rise + de-blur 10 f | someone's post, ad copy or quote is read aloud | insert record |
| **P-48** | Headline row | overlay | `fx.headlineCard` (light) with the exact headline and a `bad` highlight on the spoken phrase | built-in; highlight wipes 0.5 s per span | a news headline is cited | insert record |
| **P-49** | App row | overlay | `fx.appUI` (`kind: list`) as a generic checkout/offer screen: the advertised offer as list rows | built-in; rows on their words | an app's offer, plan or price screen is described | insert record |
| **P-50** | Name plate | overlay | `fx.logoPlate`: the brand or product name set in type with a monogram | built-in; pulses on the name | a brand or product is named (never a fetched logo) | insert record |
| **P-51** | Creator shot | overlay | `fx.shot`: the creator's own screenshot or photo (a pack label, a statement, a receipt) in the board with a highlight box on the figure | built-in; highlight on the number word | the creator supplied the real thing | asset (origin creator) |

52 patterns: P-01…P-52 (P-01–P-17, P-34, P-52 in F-A; P-18–P-33 in F-B; P-35–P-42 in F-C; P-43–P-51 in all).

### 8.4 Line → pattern lookup `[NICHE]`
| Line type | Example (finance / fitness) | Primary | Alternates |
|---|---|---|---|
| A named quantity | "Ruchi earns ₹75 lakhs" / "Breakfast is 450 kcal" | P-01 + P-02 | P-32 if nothing else is on the board |
| A second quantity to compare | "I earn ₹50 lakhs" / "Lunch is 700 kcal" | P-01 + P-02 (same scale) | P-24 |
| The role of a quantity | "the house runs on my salary" / "that's your fuel" | P-03 | P-04 |
| Things a quantity covers | "school fees, food, electricity…" / "rice, dal, paneer…" | P-05 (one tile per spoken item) | P-30 |
| A total | "₹1.25 crore combined" / "2,400 kcal a day" | P-06 | P-33 |
| "What if X stopped / doubled?" | "what if one salary stopped?" | P-10 → P-07 | P-08 |
| The moral | "both incomes are load-bearing now" | P-09 | — |
| A promise of N items | "these 5 offers cheat us" / "5 snacks that aren't healthy" | P-11 + P-12 | HA-02 title |
| An item's name and claim | "30% + 20% off" / "granola: 'no added sugar'" | P-13 | P-47 / P-49 when it's someone's ad |
| What you think | "we feel we're getting 50%" | P-14 | P-34 |
| What is true | "it's only 44%" / "it's 21 g of sugar" | P-15 | P-16 on the last item |
| An apparent saving that isn't | "you think you saved ₹500" | P-17 | P-15 |
| A per-unit amount becoming a total | "₹100 a day is ₹36,500 a year" / "200 kcal a day is 6 kg a year" | P-52 | P-32 |
| "Would you choose A or B?" | "an 8% loan or an 11% loan?" / "running or walking?" | P-19 → P-20 | P-24 directly |
| The inputs | "₹2.5 lakh loan, 10 years" / "30 minutes, 5 days a week" | P-21 | — |
| "After N years / weeks…" | "after 2 years the interest is…" | P-23 + P-24 | P-32 for one option |
| Who's ahead now | "the 8% loan is charging more" | P-22 | P-04 |
| How it happened (mechanism) | "flat on the full amount, reducing on what's left" | P-25 + P-26 + P-27 | P-30 |
| What to do | "check the APR statement" / "read the label per 100 g" | P-28 | P-31 |
| "The same trap in…" | "same trap in insurance" | P-29 → P-30 → P-31 | — |
| The difference | "₹36,750 more" | P-33 | P-15 |
| Story: a date / place / object / person | "24 May 1971", "a phone call" | P-38 (the creator's still) | P-41 |
| Story: money changes hands | "₹60 lakhs were withdrawn" | P-40 | P-32 (F-A) |
| Story: the open question | "but how did all this happen?" | P-42 | — |
| A sponsor | "talk to our sponsor X" | P-43 | — |
| CTA | "comment X" / "link in bio" / "watch this next" | P-45 / P-46 / P-44 | — |
| Someone else's post, ad, app or headline | "the app says 50% off" | P-49 (created) or P-51 (creator's screenshot) | P-47, P-48, P-50 |

### 8.5 Data and truth rules
See §18. In short: quantities are drawn on one scale per comparison; tiles are countable (one tile per spoken item); every number is real or script-stated; illustrative graphics carry the `example` label (NC-6); the status tag always agrees with the bars.

### 8.6 Comedy layer
OFF (`tone.comedy: off`, max `off`). The style is defined by its absence: no stickers, stamps or meme sounds.

### 8.7 Asset rules
- Real captures first: the creator's own statements, pack labels, receipts and app screens (blurred personal identifiers, NC-14) go in P-51.
- Mocks: only generic, unbranded recreated UIs (P-49).
- No stock images, no stock icons as content, no fetched logos; brand names are set in type (P-50).
- Third-party moments follow ask-then-create (§12.5).

### 8.8 Density and variety
- 25–40 board events per 60 s (each declared in `events`), 6–12 distinct patterns per 60 s.
- The same pattern may repeat back-to-back only inside a ritual (rows in L-BUILD, items in L-LIST, steps in L-CALC, stills in S-CASE).
- No card may stay empty (a ghost chip or skeleton) longer than 1.2 s.

---

## §9 Transitions & shot grammar `[DNA]`

### 9.1 Library
| ID | Transition | Frames | Recipe | SFX role |
|---|---|---|---|---|
| **T-1** | In-place build | 4–10 | An element enters on its word inside the existing board; nothing else moves | reveal (only on value landings) |
| **T-2** | Pill pop | 4 | A small grey pill grows (0.25 → 1.08 → 1.0) into the white value card, its value legible from f2 | reveal |
| **T-3** | Cards → bars morph | 9 | Stat cards shrink and slide to their bar-badge rects with a 24 px horizontal motion blur mid-move; the panel title cross-fades over f5–f8. Build: inside the board scene, each moving card takes `filter:${ctx.blur(px, 0)}` (directional, 0° = horizontal), px = 24 × sin(π · p) over the 9 f (peak mid-move, 0 at both ends); never a uniform CSS `blur()` | silent |
| **T-4** | Panel replace | 6 + 8 | The panel (or board) content blurs 0 → 10 px and fades out over 6 f; the next section's skeleton rises 16 px and fades in over 8 f | silent |
| **T-5** | Still cut | 0 | Hard cut between stills (F-C), on the noun or place word ±1 f; the presenter clip and the furniture do not change | silent (≤ 1 reveal cue per 10 s on a ledger landing instead) |
| **T-6** | Title fade + cut | 4 + 0 | The F-C title card fades out over 4 f, then a hard cut into still 1 | silent |
| **T-7** | Cut + slam to end card | 0 + 3 | `stage via: cut` to W-endcard; the P-44 block slams from scale 2.6 → 1.0 with 18 px motion blur over 3 f. Build: the P-44 scene with `in: "none"` scales itself 2.6 → 1.0 (ease out) over f0–f2 under `filter:${ctx.blur(px, 90)}` (directional along the slam, px 18 → 9 → 0), sharp from f3 | CTA (whoosh) |
| **T-8** | Sponsor rise | 10 | The sponsor card rises 16 px and fades in under the existing content | CTA |
| **T-9** | White flash (F-C only) | 1–2 | A full-frame white fill over the picture (presenter, stills and board included; captions stay sharp on top) at 85% on the cut frame, 40% on the next, then gone; the new still is already under it (v04 @ 7.04 = 1 f, 26.16–26.20 = 2 f). Build: core's built-in transition, no scene: `timeline.transitions` `{"t": <cut>, "type": "flash", "frames": 2, "pre": 0, "peak": 0.85, "decay": 1.1, "colour": "#FFFFFF"}` (frame 2 lands at 0.85 × 0.5^1.1 ≈ 40%); `"frames": 1` for the single-frame version | transition (soft hit) |

"Hard cuts only" applies to the A-roll: it is trimmed with same-framing jump cuts at sentence ends (§7.6), each carrying the caption swap and no transition. Never a punch-in or reframe to hide a cut.

### 9.2 Grammar
| Boundary | Use | Never |
|---|---|---|
| f0 | T-1 (the first board element enters on f0) | a fade from black, a title card in F-A/F-B |
| Hook → body | continue building (no transition) | a stage change, a world change |
| New item (L-LIST) | tab + numeral light-up, then T-1 | a board clear |
| New row (L-BUILD) | T-1 in the next lane | moving existing rows |
| Opening cards → working view (F-B) | T-3 | a hard cut |
| New section (F-B "why", "transfer") | T-4 | T-3 |
| A value lands | T-2 | a flash, a shake |
| Story beat (F-C) | T-5 | dissolves between stills |
| Inciting event, the turn (F-C) | T-9 | a flash in F-A / F-B, or more than 2 per reel |
| Sponsor | T-8 | covering the data |
| Last word → end card | T-7 | a black tail > 0.2 s |

### 9.3 Shot grammar
OFF (spine `talking_head`, source `talking_head`).

### 9.4 Budget (per 60 s)
T-1/T-2: unlimited (they are the rhythm). T-3: ≤ 1. T-4: ≤ 2. T-5: 15–25 in F-C only. T-6: 1 (F-C). T-7: 1. T-8: ≤ 1. T-9: ≤ 2 (F-C only). The same non-ritual transition never 3× in a row.

---

## §10 Motion, camera, layers, finishing `[DNA; motion tokens TUNE ±15%]`

### 10.1 Motion tokens (30 fps)
| Token | Value |
|---|---|
| Lead | 2 f before the trigger word |
| Entry ease | `cubic-bezier(0.22, 1, 0.36, 1)` (expo-out) |
| Exit ease | `cubic-bezier(0.64, 0, 0.78, 0)`, 5 f |
| Row / label enter | 6–8 f, rise 6 px + fade |
| Chip / tile pop | 4 f, from a `ghost` pill at scale 0.25 → 1.08 → 1.00, white from f2 (no separate ghost hold) |
| Number roll | 10 f (rows, bars), 12 f (totals), 18 f (hero counter), 27–45 f linear (F-C ledger); tabular figures; a 6 px vertical motion blur on the rolling digits only |
| Strike | 2 f, L → R, 4 px `bad`, on the tile's beat |
| Bar wipe / grow | 7 f (wipe), 10 f (race-bar grow), ease-out |
| Tabs / numerals stagger | 3 f / 5 f, fade only |
| Tile stagger | ≥ 0.6 s between spoken items (each tile on its own word); 4 f when a group is spoken as one phrase |
| Morph (T-3) | 9 f, 24 px horizontal motion blur (`ctx.blur(24, 0)` peak) |
| Slider step | 8 f into the step word |
| Counter glow | 12 f fade |
| Title line (F-C) | 3 f, 3 f stagger, grey → white 10 f; exit fade 4 f |
| End-card slam (T-7) | 3 f, scale 2.6 → 1.0, 18 px directional blur (`ctx.blur(18, 90)` → 0); arrow draw 11 f |
| Flash (T-9) | 1–2 f, 85% → 40% white (built-in `flash`, pre 0, decay 1.1) |
| Stills | static (no Ken Burns) |
| Hold | text ≥ 0.25 s per word; titles ≥ 10 f after building; summary lines ≥ 2.0 s |

### 10.2 Footage camera
`zoom_policy: none`. Measured at 25 fps with ORB on the presenter: per-frame scale change p99 < 0.1% and rotation p99 < 0.04° (v01, v02), cumulative drift ≤ 2% over 45 s, and the background stays put across every v03 jump cut. No Z-moves exist in this style: no punch-ins, crash zooms, push-drifts, shakes or rotations on the presenter, in any format. The only motion in the presenter window is the take itself.

### 10.3 Canvas camera
OFF (§21).

### 10.4 Layer order (back to front)
1. World (W-ledger / W-case / W-endcard), glow, noise
2. (z2) none in this style
3. Board / panel scene (z3); F-C still band (z3)
4. Presenter window (stage) with its 2 px border
5. Sponsor card, keyword card, inserts (z5)
6. Chrome slots: S-tabs (inside the board), S-panel-title, S-case-tag, S-ledger (z6)
7. Captions (CS-1)
8. — 11. unused (no big captions, comedy, banners or light passes)

The F-C still band sits under the presenter window and never overlaps it (the band ends at y 940, the window starts at y 960).

### 10.5 Finishing
Film noise 0.04 (F-A, F-B) / 0.05 (F-C) on the world only; vignette 0.12 / 0.2; a soft glow drifting ±24/18 px on the teal and maroon worlds. Card shadows: `0 10px 30px rgba(0,0,0,.18)`. No grain on the footage, no bloom, no flares.

---

## §11 Sound contract (minimal) `[VAR]`
Sound comes from the bundled SFX pack and its global rules S1–S6 (every cue marks a visible event, ≤ 2 uses per file, one list-cue exception, no consecutive repeats, catalogue ids only). This style adds only:

| Line | Decision |
|---|---|
| **Cue moments** | `reveals` (a value landing in P-02, P-06, P-15, P-16, P-24 verdicts, P-40 changes; ≤ 1 per 4 s), `list_cue` (each L-LIST item's light-up), `cta` (end card, keyword card, sponsor card). Still cuts and row builds are silent; T-9 may carry a soft hit and the T-7 slam a whoosh (both from the `transition` category) |
| **Meme cues** | off (comedy `off`) |
| **Music bed** | on, a calm low bed; enters after the hook (on the first beat after 3 s); F-C may start it from f0 under the title card |
| **Ducking** | the bed sits ≥ 18 dB under the voice while the voice speaks |
| **Loudness** | −14 LUFS integrated, true peak ≤ −1.5 dBTP; hard end ≤ 6 f after the end card's last frame (NC-8) |

Mirrored in `tokens.json → sound`.

---

## §12 Footage requirements, shot list, fallbacks, inserts

### 12.1 Setups `[DNA what the style assumes; VAR the buyer's actual setup]`
| Setup | Spec |
|---|---|
| **A: Seated teacher** (every format) | Camera at eye height, front-on, medium close-up (head and shoulders to mid-chest); landscape 16:9, 4K 25/30 fps preferred (1080p works for F-A and F-C); soft key from camera-left, gentle fill; a styled background at 1.5–3 m (a bookshelf, a plant and one personal object), slightly defocused; a plain dark crew-neck tee (no logos, no stripes); glasses fine; no visible mic; eye-line into the lens; one continuous take, read calmly |

Framing on output: F-A / F-C 16:9 window shows the full frame (head top at 18–30% of the window, eyes at ≈ 40%). F-B crops 9:16 out of the take (the eyes at y ≈ 1015).

### 12.2 Shot list
| ID | Shot | Spec | Count per 60 s | Must / optional | Formats |
|---|---|---|---|---|---|
| SH-1 | The A-roll take | Setup A, one take or word-boundary jump cuts | 1 | must | all |
| SH-2 | Story stills | Monochrome photos or images the creator owns or made; 4:5 or 9:16, ≥ 1080 px wide; one accent-coloured object per still if possible; one per story beat | 15–25 | must (F-C) | F-C |
| SH-3 | Next-video thumbnail | The creator's own 16:9 thumbnail, ≥ 1280 px wide | 0–1 | optional | all |
| SH-4 | Sponsor logo | Supplied by the creator, SVG or PNG with alpha | 0–1 | optional (sponsored reels) | F-A, F-B |
| SH-5 | Title prop | A cut-out PNG with alpha (a note, a key, a letter), ≥ 800 px | 0–1 | optional | F-C |
| SH-6 | Vertical or 4K take | A 1080×1920 vertical take or a 2160p landscape take for the F-B face cell | 1 | optional | F-B |

### 12.3 Fallbacks
| ID | For | What the engine does instead | Fidelity cost | Result |
|---|---|---|---|---|
| FB-1 | SH-1 | none | the style needs the presenter | `no_fallback` |
| FB-2 | SH-2 | P-41 object plates: a Claude-built monochrome plate per beat (an `fx.icon` line object on W-case with one accent glow), held static | no photographic atmosphere; reads as a motion-graphic case file | `degraded` |
| FB-3 | SH-3 | A created end card: the next video's title set in type on the theme gradient with a neutral play glyph | no thumbnail face | `holds` |
| FB-4 | SH-4 | The sponsor wordmark set in type (44 px, `paper`) inside P-43 | no brand logo | `holds` |
| FB-5 | SH-5 | A drawn prop: a rounded note card (`accent` at 70% with a darker border and a printed-pattern stripe) that curls and falls in CSS 3D | less photoreal | `holds` |
| FB-6 | SH-6 | Crop the 1080p landscape take at ≤ 1.35× and set the face cell's eye line at 0.26 | softer, tighter face | `degraded` |

Say at the checkpoint which fallbacks were used.

### 12.4 Props, reaction bank, matte, resolution
- Props: one hero prop per F-C episode (SH-5 or FB-5).
- Reaction bank: none (no cutaways in this style).
- Matte: none (nothing goes behind the presenter).
- Minimum source resolution: F-A and F-C need no crop beyond 1.0×; F-B needs a 2160p landscape or a vertical 1080×1920 source (a 1080p landscape take allows ≤ 1.35×, FB-6).

### 12.5 Third-party inserts: ask, then create `[REQ]`
Claude never fetches anyone else's media. Per reel:
1. **Analyse the transcript** (`veos inserts scan`) and list the moments that call for third-party material. In this style they are: an advertised offer or price screen, a product's pack label, a news headline, a post or quote, a brand or product name, a person in a story.
2. **Ask the creator once:** "For these N moments, do you have a screenshot, photo or clip you own? (drop the files, or say no)".
3. **Supplied:** P-51 `fx.shot` in the board (or P-38 in F-C), cropped and highlighted, never altered to say something it doesn't.
4. **Not supplied:** create it with the inserts toolkit: an advert or app offer → P-49 `fx.appUI` (`kind: list`); a quote or post → P-47 `fx.quoteCard`; a headline → P-48 `fx.headlineCard`; a brand → P-50 `fx.logoPlate`; a person → `fx.silhouette` (F-C); a story object → P-41.
5. **Record** every moment in `plan/inserts.json` (`{id, moment, origin: creator | created, file?, substitute_of?}`).

A created card quotes only what the script states (no label needed).

### 12.6 Frame rate and audio
30 fps CFR output (the source's 25 fps is conformed); 1080×1920, BT.709. Voice chain: high-pass 80 Hz, de-ess, light compression, −14 LUFS.

---

## §13 Output contract `[DNA]`

### 13.1 Core beat fields
`id`, `section`, `t0`/`t1`, `spoken`, `trigger {word, at}`, `tone`, `line_type`, `layout`, `visual` (one sentence), `layers` (scene ids), `pattern`, `sfx`.

### 13.2 Conditional fields (this style)
| Field | When |
|---|---|
| `caption {profile: CS-1 \| CS-2, overrides[]}` | always |
| `slot_content {S-tabs \| S-panel-title \| S-case-tag \| S-ledger: …}` | when a slot changes |
| `state_ops [{var: ledger \| param, op: set \| tick_to, value, at}]` | F-B steps, F-C ledger changes |
| `figure_id` | every beat that shows a number |
| `series {name, number, of}` | F-C, or when BV-13 turns the series on |
| `sponsor {id, disclosure}` | sponsored beats |
| `theme` | reel header only (`per_topic`) |
| `shot_id`, `fallback_used` | F-C stills (SH-2 / FB-2) |
| `insert {id, origin}` | third-party moments |
| `exception: E3 \| E6` | on the scene, and on the beat for E6 swaps |

### 13.3 Reel header
```yaml
reel:
  format: F-A                  # F-A | F-B | F-C
  theme: TH-maroon             # TH-teal | TH-maroon | TH-case (F-C)
  structure: L-LIST            # L-BUILD | L-LIST | L-CALC | S-CASE
  hook_archetype: HA-07        # HA-07 | HA-02 | HA-12
  opening: O-2                 # O-1 | O-2 | O-3 (HA-07 only)
  count: 5                     # L-LIST items
  keyword: null                # comment_keyword only
  cta: end_card
  state: {param: null, ledger: null}
  figures: plan/figures.json
  series: null                 # {name, number, of} for F-C
  sponsor: null
  captions: CS-1
```

### 13.4 Hook proposals (3 required)
```yaml
- name: "Rank skeleton: 5 offers"
  archetype: HA-07
  opening: O-2
  first_sentence: "These 5 online offers cheat us."
  pair: {claim: "30% + 20% off = 50% off", evidence: "44% (stacked_discount 30, 20)", card: P-15}
  post_title: "5 Online OFFERS Jo Aapko CHEAT Kar Rahe Hain!"
  storyboard: "f0 tabs rise | 0.2-0.85 numerals 1-5 | 0.95 tab 1 + numeral 1 lit | 1.6 '30% + 20% off' | 4.8 '50% you think' | 6.6 strike + 44% tile"
  sound: [list cue at 0.95, reveal at 6.6]
  stopper_test: {mute: pass, motion_f0: pass, sc_0_3s: 8, payoff_s: 0.95}
```

### 13.5 Checkpoint (before building)
1. 3 hook proposals with stopper-test results.
2. The beat sheet with tones and the board plan per section (which lane each row, tile or tag uses).
3. `plan/figures.json` and the `veos figures` output (shown vs recomputed for every number).
4. The state plan (F-B steps, F-C ledger states) and the series metadata.
5. The transition map and the SFX ledger.
6. The inserts record (creator-supplied vs created) and the fallbacks used.
7. Style stills: f0, the payoff frame (≤ 1.0 s), one mid-body board state, the reveal of the last item or final verdict, the end card.

**Wait for approval.**

---

## §14 Worked examples `[NICHE]`
Times are planning estimates; replace them with `words.edit.json` onsets.

### 14.1 F-A, L-LIST, TH-maroon — fitness [NICHE: example]: "5 'healthy' snacks that aren't"
**Header:** F-A · TH-maroon · L-LIST · HA-07 / O-2 · count 5 · CTA comment_keyword "LABELS". Every gram figure comes from the script (the creator read the labels) and lives in `plan/figures.json` as `from: script`.

**Hook (0–8 s):**
| t (s) | Spoken | Tone | Board | Caption | Cue |
|---|---|---|---|---|---|
| 0.00 | "These 5 'healthy' snacks are not healthy." | claim | S-tabs "SNACK 1…5" rising (ghost) | the sentence | — |
| 0.20–0.85 | — | — | Numerals 1–5 appear (ghost, 4 f stagger) | same | — |
| 0.95 | — | — | Tab 1 + numeral 1 light up | same | list cue |
| 1.6 | "Granola says 'no added sugar'." | claim | P-13 title "Granola" + sub-label "no added sugar" | the sentence | — |
| 3.4 | "So you think there's zero sugar in it." | claim | P-14 "0 g" + micro "you think" (input `claimed_sugar` = 0, script) | the sentence | — |
| 5.2 | "It has 21 grams of sugar per bowl." | reality | P-15 strike across "0 g"; tile "21 g" + micro "per bowl" | the sentence | reveal |

**Body plan:**
| Section | Spoken gist | Patterns |
|---|---|---|
| Item 2 (8–15 s) | "Fruit yoghurt: 'made with real fruit'… 4 teaspoons of sugar" | tab 2 → P-13 → P-14 "real fruit" → P-15 "16 g" |
| Item 3 (15–22 s) | "Protein bar: '20 g protein'… also 18 g sugar and 250 kcal" | P-13 → P-14 "20 g protein" → P-15 "250 kcal" (the creator chose the calorie figure as the reality) |
| Item 4 (22–29 s) | "Baked chips: '50% less fat'… the pack is 3 servings" | P-13 → P-14 "1 serving" → P-15 "3x" (ratio) |
| Item 5 (29–37 s) | "Packaged juice: 'no added sugar'… still 24 grams a glass, as much as a cola" | P-13 → P-14 "0 g" + "you think" → P-16 final tile "24 g" (96 px) + P-17 "a cola has 24 g" note |
| Moral (37–42 s) | "Read the label per 100 grams." | P-09 summary line "read it per 100 g" + helper "not per serving" |
| CTA (42–45 s) | "Comment LABELS and I'll send my label checklist." | P-45 keyword card "LABELS" → T-7 |

Figures: `granola_sugar` (none, script "21 grams"), `yoghurt_sugar` (none, script), `bar_kcal` (none, script), `chips_servings` (`ratio` of pack grams / serving grams, both script), `juice_sugar` and `cola_sugar` (none, script); formats use `suffix: " g"` / `" kcal"`, `currency: ""`. Third-party moments: the pack labels → ask the creator for their photos (P-51); without them, P-49 recreated generic label rows.

### 14.2 F-B, L-CALC, TH-teal — personal finance [NICHE: example]: "₹5,000 a month: 10 years or 20?"
**Header:** F-B · TH-teal · L-CALC · HA-07 / O-3 · CTA end_card. Inputs (script): ₹5,000 per month, 12% a year (the creator states it as an assumption → the figure is marked `illustrative: true` with the "example" tag), 10 and 20 years.

**Hook (0–4 s):**
| t (s) | Spoken | Panel | Caption | Cue |
|---|---|---|---|---|
| 0.00 | "Would you start investing at 25" | title "Would you start" + ghost card A | the sentence | — |
| 0.20 | — | card A fills "25" + unit "start age" (`data`) | same | reveal |
| 0.9 | — | `good` tag "Earlier?" drops on card A | same | — |
| 1.5 | "or at 35? Let's see." | card B fills "35" (`night`) | the sentence | — |
| 1.9 | — | "Value at 60" bar skeleton slides up | same | — |
| 2.3 | — | T-3 morph into two bar badges; title → "Which start makes more?" | same | — |
| 2.9 | "₹5,000 every month." | parameter chip "₹5,000 a month" | the sentence | — |

**Body plan:**
| Section | Spoken gist | Patterns | State / figures |
|---|---|---|---|
| Parameters (3–7 s) | "12% a year, till age 60" | P-21 chips "12% a year (example)", "till 60" | inputs `sip`, `rate`, `end_age` |
| Steps (7–28 s) | "After 10 years… 20… 25… 35" | P-23 slider (10/20/25/35) + P-24 race bars (both `compound` with `contribution`, one `scale_id`) + P-22 leader chip on "more" | `param` tick_to at each year word; bars land on each spoken value |
| Verdict (28–31 s) | "Starting at 25 ends with <X>; at 35, <Y>." | P-22 final leader `good` "Ends higher" + P-33 gap counter | `gap` = `diff` |
| Why (31–44 s) | "The first 10 years do the most work" | T-4 → P-25 segment bars (each segment = one decade's growth) + P-26 explain lines "Early: 35 years compounding" / "Late: 25 years compounding" | segments from figure steps |
| Transfer (44–52 s) | "Same with your EPF and PPF" | T-4 → P-30 two-card stack "Start date / when you begin", "Years left / what compounds" → P-31 "Start date beats amount" | — |
| CTA (52–56 s) | "Do you agree?" | T-7 → P-44 end card (SH-3, else FB-3) | — |

### 14.3 F-C, S-CASE, TH-case — business stories [NICHE: example]: "case 03 / 07 — the ₹40 crore order"
**Header:** F-C · TH-case · S-CASE · HA-12 · series {name: "Money Doesn't Behave", number: 3, of: 7} · CTA post_only. The story, dates and amounts are the creator's researched script; every amount is a figure input `from: script`. 18 creator stills (SH-2) + 4 object plates (FB-2).

**Hook (0–3 s):** f0 "episode three" + the prop (a purchase-order slip, SH-5 or FB-5) on the table; title lines "money / doesn't / behave" at 0.60 / 0.70 / 0.80; chapter "the ₹40 crore order" types at 1.6 s while the slip flips and falls; ≈ 3.2 s T-6 (fade 4 f + cut) into still 1 (a factory gate at dawn); the case tag "case 03 / 07" fades in.

**Body plan:**
| Section | Spoken gist | Stills / patterns | Ledger (P-40) |
|---|---|---|---|
| Setting (3–8 s) | "<Year>. A small factory in <city>." | P-38 ×3 (gate, office, ledger book) | — |
| The order (8–18 s) | "A buyer orders ₹40 crore of goods." | P-38 ×4; the ledger rises in on "₹40 crore" | ₹40,00,00,000 · ordered |
| The advance (18–26 s) | "He pays an advance of ₹4 crore." | P-38 ×3 | ₹4,00,00,000 · received |
| The turn (26–40 s) | "The goods ship. The rest never comes." | P-38 ×5 + P-41 ×2 (a ship, an empty account screen as an object plate) | ₹36,00,00,000 · unpaid (`diff`) |
| Ending (40–48 s) | "But how did a ₹4 crore advance hide a ₹36 crore hole?" | P-42 hold on the last still | final state glows once |

### 14.4 F-A, L-BUILD, TH-teal — productivity [NICHE: example]: "Where your 24 hours go"
O-1 opening: row "WORK" 9 h (P-01/P-02, `suffix: " h"`), row "SLEEP" 7 h, tag "NON-NEGOTIABLE" (P-03); P-05 tiles "commute, meals, chores, phone"; P-06 total "24 h"; P-10 "what if the commute doubled?" → P-07 zero-out on "free time" (3 h → 1 h, "was 3 h"); P-09 "the time comes from you, not your work"; CTA link_bio (P-46).

---

## §15 QA checklist `[DNA]`

**1. Profile conformance**
- [ ] Format, theme and structure declared; F-C uses TH-case; one layout for the whole body. (V-LAYOUT, V-THEME)
- [ ] Presenter share 88–100%; absence only on the end card ≤ 3.5 s. (V-PRESENCE)
- [ ] Duration 40–60 s (short). (review)

**2. Hook**
- [ ] f0: presenter + claim caption + a board element entering. (V-F0)
- [ ] First value by 1.0 s (F-C title by 3.0 s). (V-F0)
- [ ] ≥ 5 weighted SCs in 0–3 s (F-C ≥ 4). (V-CADENCE)

**3. Body and cadence**
- [ ] 4–7 SC per 10 s (F-C 3–6); no weight-1 gap > 2.5 s (3.0); nothing static > 2.5 s. (V-CADENCE)
- [ ] Every list item uses the identical ritual; the rank count equals the items delivered. (V-PROMISE)
- [ ] One board scene per section; ≤ 3 text blocks; nothing overlaps. (G1, G2)
- [ ] No empty card older than 1.2 s. (review)
- [ ] Motion matches §10.1: chips and tiles pop from a pill in 4 f, strikes 2 f, captions hard-swap, stills static, no presenter zoom; T-9 only in F-C, ≤ 2. (review)

**4. Captions**
- [ ] CS-1 (or CS-2 for the whole reel); 36 px, weight 500; ≤ 2 lines, ≤ 44 characters per line; contrast ≥ 7:1 (≥ 4.5:1 on CS-2). (V-TYPE, V-CAPTION)
- [ ] Shown ≤ 0.15 s before the first word; never cut before the last word. (V-CAPTION)
- [ ] No emphasis, no colour, no caps; spelling and glossary exact. (V-CAPTION)

**5. Modules**
- [ ] Chrome: slot rects constant ±4 px; tabs, panel title, case tag and ledger stay in their slots. (V-CHROME, pending in the engine → review)
- [ ] Running state: the ledger shows exactly the spoken state after each op; the slider handle sits on the spoken step. (V-STATE, pending → review)
- [ ] Data: `veos figures` clean; every number recomputes; compared bars share a scale; counters land within ±5 f of their words; ₹ grouping and compacts correct. (V-DATA, V-NUMFMT)
- [ ] Series: the case tag shows n / of from the reel header. (review)
- [ ] Brand: the sponsor card has the spoken disclosure and "Paid partnership" visible ≥ 2 s; the end card ≤ 3.5 s. (V-PROMISE, NC-12)

**6. Truth and inserts**
- [ ] Every third-party moment is creator-supplied or created; quotes verbatim. (V-INSERTS)
- [ ] Illustrative figures (assumed rates) carry the "example" tag. (V-DATA)
- [ ] Personal identifiers in creator screenshots are blurred. (NC-14)

**7. Sound contract**
- [ ] Cues only on reveals, the list cue and the CTA; no meme cues; S1–S6 clean. (S1–S6)
- [ ] The bed enters after the hook, ≥ 18 dB under the voice; −14 LUFS; true peak ≤ −1.5 dBTP. (loudness gate)

**8. End and export**
- [ ] CTA element held ≥ 1.5 s; hard end ≤ 6 f after the end card; no black tail > 0.2 s. (V-PROMISE, review)
- [ ] 1080×1920, 30 fps CFR. (review)

---

## §16 Frame template / persistent chrome `[COND: modules.chrome = true] [DNA rects; TUNE ±5%]`
The frame never changes; only the content inside it does.

| Slot | Rect (px) | z | Lifetime | Content | Entry | Swap |
|---|---|---|---|---|---|---|
| **S-frame** | x 96, y 112, w 888, h 500 (F-A) · x 64, y 960, w 952, h 536 (F-C) · bottom cell y 760–1920 (F-B) | stage | video | the presenter | none (on from f0) | none |
| **S-tabs** | x 64, y 648, w 952, h 44 | 6 (drawn inside the board scene) | section: L-LIST | chip tabs (P-12) | rise 12 px + fade 6 f, 2 f stagger | E6 colour swap 4 f |
| **S-panel-title** | x 64, y 128, w 952, h 60 | 5 (inside the panel scene) | video (F-B) | panel title (P-18) | fade 6 f | E6: fade 4 f out / 6 f in |
| **S-case-tag** | x 64, y 140, w 400, h 48 | 6 | after:3 (F-C) | "case nn / of" + dots (P-39) | fade 8 f | hard (it never changes inside a reel) |
| **S-ledger** | x 656, y 132, w 360, h 132 | 6 | from the first money word (F-C) | ledger counter (P-40) | rise 8 px + fade 8 f | E6: value roll 10–12 f, state word swap 4 f |

The beat sheet writes only `slot_content`. Slot rects stay constant within ±4 px for their lifetime (V-CHROME; the rule is pending in the engine, so the frame reviewer checks it). Slots never overlap each other or the presenter window. The case tag and the ledger counter each count as one text element for their whole life.

---

## §17 Running state & anchored graphics `[COND: modules.running_state = true; anchors = false] [DNA mechanics]`

### 17.1 State variables
| Var | Type | Start | Format | Display | Ops |
|---|---|---|---|---|---|
| `ledger` (F-C) | `ledger` with labelled states (needed → handed over → spent → recovered; or ordered → received → unpaid) | first money word | `profile.numbers`, style `full` | P-40 in S-ledger | `set {value, state}` on each spoken money word; values are figure steps with `label` |
| `param` (F-B) | `progress` over the slider's ticks | the first step | integers, or the parameter's unit suffix | P-23 | `tick_to <x>` 8 f before the step word |

Display rules: one persistent position; the value changes only on an op; it never contradicts the spoken or shown value; it persists across still cuts. **Engine status:** V-STATE is pending, so the ledger is built as a **figure** today: one `none`-formula figure whose steps carry `args: {value: <input>}` and `label: <state word>`, read in a bespoke scene with `ctx.figAt` and `ctx.fig(id).steps[i].label`. V-DATA then checks every landing.

### 17.2 Anchors
OFF. Nothing in this style follows a face or an object; every graphic sits on the board grid or in a slot.

### 17.3 Validator
V-STATE (pending): displayed ledger = the running state; `recovered` = `needed − spent` when the script says so (use `diff` so V-DATA proves it today).

---

## §18 Data contract `[COND: modules.data_figures = true] [DNA rules]`
Every chip, tile, bar, slider tick, counter, total and ledger value is a **figure** in `plan/figures.json`.

### 18.1 Rules
1. **Provenance:** every input is `from: script` (with `said`: the exact words), `creator` (asked once), `spoken@<t>`, or `buyer`. Literal claims inside `args` are errors.
2. **Formula first:** if the script derives a number (a total, a discount, an interest, a difference, a per-year amount), the figure uses the formula and the stated value is checked against it. Allowed formulas: `sum`, `diff`, `ratio`, `percent_change`, `stacked_discount`, `simple_interest`, `flat_rate_interest`, `reducing_balance_emi`, `compound`, `cagr`, `per_period`, `unit_convert`.
3. **Rounding:** when the creator rounds (₹1,31,190 for 1,31,193.6), set `round_to` (10) so the tolerance is ±5.
4. **Same axes:** compared bars, race bars and rows of one comparison share one `scale_id`; the scale's max is the largest value shown in that comparison for the whole reel (bars never re-scale).
5. **Landing:** counters and value chips land within ±5 f of the spoken number word (`lands`); slider steps land on their step word.
6. **Format:** chips and tiles of round lakh/crore values use `{"style": "short"}`; computed amounts use `{"style": "full"}`; non-money values use `{"currency": "", "suffix": " g"}` (or " kcal", " h"); percentages use `"percent"`.
7. **Illustrative:** an assumed rate or a hypothetical ("say 12% a year") is `illustrative: true`; the board shows the 24 px "example" tag next to it.
8. **Every number on screen** is in figures.json or spoken; integers ≤ 12 used as labels (rank numerals, tab numbers, slider ticks taken from figure steps) are exempt.

### 18.2 Worked figures (the calculator from the source, F-B)
```json
{
  "version": 1,
  "inputs": {
    "loan":      {"value": 250000, "unit": "INR", "from": "script", "said": "₹2.5 lakhs"},
    "years":     {"value": 10, "from": "script", "said": "A 10-year period"},
    "flat_rate": {"value": 8,  "unit": "%", "from": "script", "said": "an 8% loan"},
    "red_rate":  {"value": 11, "unit": "%", "from": "script", "said": "an 11% loan"}
  },
  "figures": [
    {"id": "flat", "kind": "bar", "label": "8%", "formula": "flat_rate_interest", "output": "interest_paid", "scale_id": "S-int",
     "args": {"principal": "loan", "rate_pct": "flat_rate", "years": "years"},
     "steps": [{"x": 2, "args": {"elapsed_years": 2}, "value": 40000, "at": 7.4},
               {"x": 4, "args": {"elapsed_years": 4}, "value": 80000, "at": 10.6},
               {"x": 6, "args": {"elapsed_years": 6}, "value": 120000, "at": 14.3},
               {"x": 8, "args": {"elapsed_years": 8}, "value": 160000, "at": 18.4},
               {"x": 10, "args": {"elapsed_years": 10}, "value": 200000, "at": 29.1}]},
    {"id": "red", "kind": "bar", "label": "11%", "formula": "reducing_balance_emi", "output": "interest_paid", "scale_id": "S-int", "round_to": 10,
     "args": {"principal": "loan", "rate_pct": "red_rate", "years": "years"},
     "steps": [{"x": 2, "args": {"elapsed_years": 2}, "value": 51880, "at": 8.6},
               {"x": 4, "args": {"elapsed_years": 4}, "value": 96226, "at": 12.6},
               {"x": 6, "args": {"elapsed_years": 6}, "value": 131190, "at": 15.6},
               {"x": 8, "args": {"elapsed_years": 8}, "value": 154488, "at": 20.4},
               {"x": 10, "args": {"elapsed_years": 10}, "value": 163250, "at": 30.6}]}
  ]
}
```
The panel scene binds `figures: ["flat", "red"]`, `scale: {id: "S-int", max: 200000}`, and `lands` at every step's `at`. Values on screen: `ctx.fmtNum(v, "flat")` → `₹1,20,000`; the leader chip sits on whichever `ctx.figAt(...).value` is larger.

### 18.3 Other figure shapes this style uses
| Pattern | Figure |
|---|---|
| P-15 discount reality | `{"id": "offer1", "kind": "hero_number", "formula": "stacked_discount", "args": {"discounts_pct": ["d1", "d2"]}, "value": 44, "format": "percent"}` with inputs `d1` 30, `d2` 20 (`from: script`); the claimed "50%" is its own input `claim1` (`from: script`, said "50% off") |
| P-06 total | `{"id": "total", "kind": "hero_number", "formula": "sum", "args": {"values": ["inc_a", "inc_b"]}, "value": 12500000, "format": {"style": "short"}}` → `₹1.25 Cr` |
| P-07 zero-out | a `none` figure with two steps: `{args: {value: "inc_b"}}` then `{args: {value: "zero"}, at: <"stopped">}` where `zero` = `{"value": 0, "from": "script", "said": "stopped"}` |
| P-40 ledger | `{"id": "ledger", "kind": "ledger", "formula": "none", "steps": [{"args": {"value": "needed"}, "label": "needed", "at": 11.2}, {"args": {"value": "handed"}, "label": "handed over", "at": 20.3}, {"args": {"value": "spent"}, "label": "spent", "at": 29.1}, {"args": {"value": "fig:recovered"}, "label": "recovered", "at": 46.2}]}` + `{"id": "recovered", "kind": "counter", "formula": "diff", "args": {"a": "needed", "b": "spent"}}` |
| P-52 conversion | `per_period` / `unit_convert` (`₹100 a day` × 365 → `₹36,500` via `{"formula": "unit_convert", "args": {"value": "daily", "rate": "days"}}`) |

### 18.4 Validator
V-DATA (recompute, provenance, landing ±5 f, shared scales, illustrative label) and V-NUMFMT (₹ glyph, Indian grouping, lakh/crore compacts, no K/M/B on rupees, figure numbers written exactly as `fmt_num`) run on every reel.

---

## §19 Evidence & citations
OFF (`modules.citations = false`): the source never shows outlet cards or credit lines. A cited headline is handled as a third-party moment (P-48, §12.5).

## §20 Dialogue
OFF (`modules.dialogue = false`): one presenter.

## §21 Canvas camera
OFF (`modules.canvas_camera = false`): the board never moves; graphics `primary` but the style is a fixed UI, not a canvas.

## §22 Ink & annotation layer
OFF (`modules.ink = false`): the only mark is the strike line, which is part of P-15.

## §23 Continuity
OFF (`modules.continuity = false`): no morph chains; the one morph (T-3) is local to F-B's opening.

---

## §24 Series furniture `[COND: modules.series = true] [DNA look; VAR name/number]`
- **When:** always in F-C; in F-A/F-B only when the buyer turns a series on (BV-13).
- **Series tag (P-39):** "case {n} / {of}" (`series.tag_format`), 28 px, at S-case-tag, from the first still to the end; 7 dots (or `of` dots, max 10): the current episode's dot lit `accent`, past ones `paper` 60%, future ones `paper` 30%. When a series is on in F-A (L-BUILD) the tag sits right-aligned inside the board at y 664–700 (x 616–1016); in L-LIST it is dropped (the tabs already show progress); in F-B it sits right-aligned in the panel at y 136–172.
- **Episode label (P-37):** "episode {word}" in `accent`, the hook's f0 text beat (F-C).
- **Series card:** none separate; the F-C title card is the series card (0–3 s, counts toward the 15% intro cap).
- **Episode counter / recap / teaser chips:** none.
- **Tokens:** `series {name, number, of, tag_format, dots, card, episode_label}`; the number comes from the reel header.

---

## §25 Sponsor, brand & end cards `[COND: modules.brand = true] [DNA look; VAR assets]`
- **Sponsor card (P-43):** placement F-A footer lane (y 1400–1500, after the summary line exits) or F-B under the transfer cards (y 480–600); never over the presenter, the captions or a live value. On screen 4–6 s. **Disclosure:** spoken ("our sponsor <brand>") **and** "Paid partnership" (TC-legal 24 px, inside the card, top-right) for the whole card (≥ 2 s; NC-12). Wording VAR: {{BV-01.name|the creator}} may change it via BV-14. The logo is the creator's file (SH-4) or the wordmark in type (FB-4). Brand colours only on the logo.
- **End card (P-44):** the `end_card` device; ≤ 3.5 s (`brand.endcard.max_s`); the title is readable ≥ 1.5 s; the black tail ≤ 0.2 s.
- **Keyword card (P-45), link chip (P-46):** §6.7.
- **Rules:** one brand element at a time; a sponsor card never shares the footer with a summary line (the summary line exits first, 5 f); the end card is always the last thing.

---

## Part C. Declared exceptions and the non-overridable core

### C.1 Non-overridable core
NC-1…NC-14 apply in full (structure Part C.1): the face is never covered; meaning text never overlaps; smooth motion; legibility floors (36 / 28 / 22 px absolute) and contrast; IG UI bands; truth; creator-owned media only; audio targets; determinism; ≤ 4 bright hues (this style: 3); sponsor disclosure; quote integrity; redaction of personal identifiers.

### C.2 Exceptions used by this template
| ID | Name | Limits in this template | Scenes that use it |
|---|---|---|---|
| E3 | `quiet_type` | `subtitle_min_px` 36, `label_min_px` 28 (redundant only), `contrast_min` 7.0, `pill_contrast_min` 4.5, `weight_min` 500, `max_lines` 2, `max_chars_line` 44 | captions (CS-1/CS-2); every board/panel scene (`exception: "E3"`, with `data-redundant` on micro-labels, tabs, parameter chips, tags, unit lines, sub-labels); the case tag; the ledger counter |
| E6 | `hard_swap` | `slot_tolerance_px` 4 | the ledger counter (value + state word), chip-tab state, the panel title swap, header swaps (P-08), the stress-test line swap (P-10); mark the container `data-slot` |

A scene declares one id. A board scene that needs both (labels under E3 and a tab swap) splits the tabs into the S-tabs scene with `exception: "E6"` and keeps E3 on the board.

### C.3 Buyer switches
Switching E3 off (VAR) raises captions to 54 px and labels to 40 px: the style still works, but the board loses lanes (L-LIST drops to 4 rows per screen). Adding any other exception is a DNA deviation.

---

## Part D. Personalisation

### D.1 Branding questions (one round, each with "keep the template default")
| ID | Question | Lands on | Default |
|---|---|---|---|
| BV-01 | Your name and handle | `creator.name`, `creator.handle`; end card, series tag | {{BV-01.name|the creator}} · {{BV-01.handle|@yourhandle}} |
| BV-02 | One or two brand colours | `roles.primary`, `roles.accent` (contrast-nudged against `ink`) | `#FFFFFF`, `#40E87A` |
| BV-05 | The language you speak and the caption language | `profile.language`, always asked: **English** → English captions (default) · **Hinglish** → romanised Hinglish captions · **Hindi** → Devanagari captions; numbers follow (BV-06) | English ({{BV-05.speech|en}} → {{BV-05.captions|en}}) |
| BV-08 | Your call to action | `profile.cta.chosen` + keyword/deliverable | end card |

### D.2 Lock map (this template)
| Lock | Paths |
|---|---|
| **DNA** | source type, spine, caption role/mechanics/emphasis none, graphics role, the layout family and "one layout per body", zoom policy none, comedy off, the board-per-section rule (B0), claim-vs-reality axis, the `bad`/`good` meanings, E3/E6 declarations, the theme policy `per_topic`, the hook archetype set, the structure types and rituals, the figure contract |
| **TUNE** | caption size 36–44 and weight 500–600; caption offset 14–40; type sizes in their ranges (tokens `locks`); layout rects ±5%; seam y 820–900; cadence ±15%; motion ±15%; theme world hues (dark-to-mid two-stop gradients); `data`/`stage`/`muted`/`ghost`/`night` within their contrast ranges; font families within the geometric-sans class; energy calm ↔ balanced; duration micro/short/standard; presenter share ±10 |
| **VAR** | name, handle, `primary`, `accent`, language pair, numbers format, CTA device and keyword, formats enabled, default theme, series on/off and its name/number, sponsor disclosure wording, end-card type, the sound contract lines, the buyer's setup |
| **NICHE** | §6.4 hook pairs, §8.4 lookup examples, §14 worked examples, App. A |

### D.3 How NICHE slots grow per reel
At P7 the editor appends the reel's claim → evidence pair to §6.4; at P5/P8 new line types go into §8.4 (mapped to existing patterns; ≤ 10 new niche patterns from existing families over time); after the first approved reel of each format it replaces that format's §14 example; approved first sentences and post titles go into App. A.

---

## Part E. Where this template departs from the source (and why)
| Source (measured) | Template | Why |
|---|---|---|
| Captions 30–34 px, weight 400 | 36 px, weight 500 (E3) | the E3 floor and weight minimum |
| Micro-labels 14–25 px, `#8A8A8A` on white (3.5:1) | 28 px, `#6B6B6B` (5.3:1), redundant only | NC-4 floors and contrast |
| Rank/tab ghost grey `#B7B0AD` (2.8:1 on the maroon bottom) | `#D6CFCC` (3.3–3.9:1), numerals 100 px | display contrast ≥ 3:1 |
| Green chip `#2E8B3A` with white text (4.3:1) | `#26803A` (5.0:1) | 4.5:1 for labels |
| Board and inset at x 32–108 px from the edges; rows down to y ≈ 1760 | 64 px margins; everything above y 1500 | G2 margins, NC-5 bands |
| v02 frame 0 is an empty column for 1.3 s | the first board element enters on f0 | V-F0 / ST-3 |
| v03 sponsor card shows no visible disclosure | "Paid partnership" in the card | NC-12 |
| v04 B/W stills look AI-generated; a 3D banknote prop | stills are the creator's own (SH-2) or object plates (FB-2); the prop is the creator's PNG or a drawn card | NC-7, the engine makes no imagery |
| v04 presenter clip graded green-mono | natural colour until the grade engine exists (ER-3) | capability missing |
| v04 flashes are a full white frame | T-9 peaks at 85% for 1 f, 40% the next | |
| "₹1.25 CR" | "₹1.25 Cr" | the engine's `fmt_num` short style (V-NUMFMT) |

---

## Part F. IDs used in this playbook
| Prefix | IDs |
|---|---|
| D / BD | D1–D8 / BD… |
| H / N / BN | H1–H15 / N1–N12 / BN… |
| E | E3, E6 |
| W / L / G | W-ledger, W-case, W-endcard / L-inset-top, L-face-bottom, L-cinema-top, L-endcard / G-1, G-2 |
| TH / GR | TH-teal, TH-maroon, TH-case / GR-case-mono |
| CS | CS-1, CS-2 |
| HA / ST / O | HA-07 (default), HA-02, HA-12 / ST-2, ST-3, ST-4 (F-C), ST-5, ST-6 / O-1, O-2, O-3 (openings) |
| Structures / SM | L-BUILD, L-LIST, L-CALC, S-CASE / SM-rank-list, SM-panel-title, SM-case-tag |
| B / P | B-1–B-10 / P-01–P-52 |
| T | T-1–T-8 |
| S (slots) | S-frame, S-tabs, S-panel-title, S-case-tag, S-ledger |
| SH / FB | SH-1–SH-6 / FB-1–FB-6 |
| F | F-A, F-B, F-C |
| ER | ER-1–ER-5 (engine requests, App. B) |

---

## App. A Hook & title bank `[NICHE]`
Each row: the post title (Hinglish by default), the first spoken sentence / caption, the archetype and opening. Finance and fitness are the example niches.

**F-A Ledger inset**
| # | Post title | First sentence | Archetype |
|---|---|---|---|
| 1 | 2 INCOMES Wale Ghar Mein Yeh GALTI Mat Karna! | "My wife earns ₹75 lakhs a year." | HA-07 / O-1 |
| 2 | 5 Online OFFERS Jo Aapko CHEAT Kar Rahe Hain! | "These 5 online offers cheat us." | HA-07 / O-2 |
| 3 | Aapki SALARY Kahan GAYAB Hoti Hai? | "Your ₹1 lakh salary leaves in 5 places." | HA-07 / O-1 |
| 4 | 4 BANK Charges Jo Koi NAHI Batata | "These 4 bank charges are hidden from you." | HA-07 / O-2 |
| 5 | ₹100 Roz Ka KHARCHA Kitna BADA Hai? | "₹100 a day is ₹36,500 a year." | HA-07 / O-1 (P-52) |
| 6 | 5 HEALTHY Snacks Jo Healthy NAHI Hain | "These 5 'healthy' snacks are not healthy." | HA-07 / O-2 |
| 7 | Aapki 2,000 CALORIES Kahan Jaati Hain? | "Your breakfast alone is 650 calories." | HA-07 / O-1 |
| 8 | Protein BAR vs Protein MEAL | "A protein bar has 20 grams of protein." | HA-07 / O-1 (P-34) |
| 9 | 3 CHEAT Meals Ka Asli HISAAB | "Three cheat meals add 2,400 calories a week." | HA-07 / O-1 |
| 10 | 5 LABELS Jo Aapko CONFUSE Karte Hain | "5 things on food labels mislead you." | HA-02 |

**F-B Face-bottom calculator**
| # | Post title | First sentence | Panel title |
|---|---|---|---|
| 1 | 8 Ka LOAN Ya 11 Ka LOAN, Kaunsa SASTA? | "Would you choose an 8% loan or an 11% loan?" | "Which loan costs you more?" |
| 2 | 25 Mein INVEST Karo Ya 35 Mein? | "Would you start investing at 25 or at 35?" | "Which start makes more?" |
| 3 | RENT Ya EMI, Kaunsa SAHI? | "Would you rent for ₹30,000 or pay a ₹45,000 EMI?" | "Which costs more in 10 years?" |
| 4 | Credit Card MINIMUM DUE Ka TRAP | "Would you pay the minimum or the full bill?" | "Which costs you more?" |
| 5 | FD Ya SIP, 10 SAAL Baad? | "Would you choose an FD or a SIP?" | "Which grows more?" |
| 6 | WALK Ya RUN, Zyada CALORIES Kismein? | "Would you walk 5 km or run 3 km?" | "Which burns more?" |
| 7 | 2 MEALS Ya 5 MEALS? | "Would you eat 2 big meals or 5 small ones?" | "Which adds up to more?" |
| 8 | GYM Membership Ka ASLI Kharcha | "Would you pay ₹2,000 a month or ₹18,000 a year?" | "Which costs less?" |
| 9 | Chini KAM Karo Ya BAND? | "Would you cut sugar by half or stop it?" | "Which changes more in 12 weeks?" |
| 10 | No Cost EMI Ka SACH | "Would you choose no-cost EMI or pay upfront?" | "Which costs you more?" |

**F-C Case file**
| # | Post title | First sentence | Title / chapter |
|---|---|---|---|
| 1 | Episode 1 of 7. Money Doesn't Behave. | "Episode number 1:" | money / doesn't / behave · that phone call |
| 2 | Episode 2 of 7. The Missing Ledger. | "Episode number 2:" | money / doesn't / behave · the missing ledger |
| 3 | Episode 3 of 7. The ₹40 Crore Order. | "Episode number 3:" | money / doesn't / behave · the ₹40 crore order |
| 4 | Episode 4 of 7. One Signature. | "Episode number 4:" | money / doesn't / behave · one signature |
| 5 | Episode 5 of 7. The Last Cheque. | "Episode number 5:" | money / doesn't / behave · the last cheque |
| 6 | Case 1. The Perfect Diet. | "Case number 1:" | the / perfect / diet · the 1,200-calorie summer |
| 7 | Case 2. The Miracle Powder. | "Case number 2:" | the / perfect / diet · the miracle powder |
| 8 | Case 3. 30 Days, 10 Kilos. | "Case number 3:" | the / perfect / diet · 30 days, 10 kilos |
| 9 | Case 4. The Detox Week. | "Case number 4:" | the / perfect / diet · the detox week |
| 10 | Case 5. The Coach Who Vanished. | "Case number 5:" | the / perfect / diet · the coach who vanished |

---

## App. B Evidence map `[DNA; templates only]`
The full map is `evidence.md` (every DNA rule → `vNN @ m:ss`). Summary:

| DNA element | Source |
|---|---|
| Framed 16:9 inset at the top, board below | v01 @ 0:00–0:44; v02 @ 0:00–0:39 |
| Face-bottom data panel | v03 @ 0:00–0:59 |
| Cinema-still band + 16:9 clip + case tag + ledger | v04 @ 0:03–0:49 |
| Quiet captions inside the footage | all four (v01 @ 0:00 "My wife Ruchi earns ₹75 lakhs a year.") |
| Label row → ghost chip → value | v01 @ 0:00.17–0:00.83 |
| Rank skeleton + chip tabs + strike reveal | v02 @ 0:01.3–0:39 |
| Dual stat → bars morph, slider, race bars, leader chip | v03 @ 0:00–0:32 |
| Segment bars, explain lines, method tags, action chip | v03 @ 0:33–0:49 |
| Transfer + two-card stack + check chip + sponsor card | v03 @ 0:50–0:59 |
| Title stagger + prop + chapter line | v04 @ 0:00–0:03 |
| End card with thumbnail and dashed arrow | v01 @ 0:45–0:48 |
| Theme per topic | v01/v03 teal, v02 maroon, v04 green |

**(unverified):** the speech language (no transcript), the caption transform, the sound bed, the v04 face grade's exact recipe.

**Engine requests:** ER-1 V-CHROME (slot rects), ER-2 V-STATE (ledger/param state), ER-3 footage grades with accent isolation (GR-case-mono), ER-4 a stack-cell fade that blends the footage edge into the world (the F-B seam), ER-5 per-step labels in `VEOS.data.counter` (the ledger's state word). Each has a fallback written above.
