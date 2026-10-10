# Ledger Explainer Style Playbook (template v2)

## The feel

This reel is a calm person doing the maths in front of you, and the maths wins the argument. Frame 0 is already working:
the creator framed in a clean window at the top, mid-sentence, saying a number, and under them the first row of a ledger
sliding in on a deep teal glow. Before the first second is out, that number lands in a white chip on the exact word. No
title, no tease, no "wait for it". The number is the hook.

Then the ledger builds, one row per sentence. A bar draws, a chip fills, a tile drops in on each thing named. The creator
never moves: no zoom, no punch-in, no shake. That stillness is what trust looks like: a friend who knows money doesn't wave
their arms, they write it down and turn the page towards you. And because nothing else moves, every change on the board
is loud.

The engine of attention is one move: the number you believed, then the real one. The claim sits there in grey, "you
think". On "actually" a white tile pops beside it with the truth, and a red line snaps through the lie on the same beat.
Fifty per cent off becomes forty-four. "No added sugar" becomes twenty-one grams. You feel slightly cheated and deeply
grateful, and you need the next item.

Colour stays quiet so the numbers can be loud. Teal for how money works, maroon for a trap about to be sprung, near-black
green for a story; red only ever means it costs you more, green only ever means it's true. The captions are small and
plain, inside the footage, because the board is doing the talking. It breathes like a good teacher: unhurried builds, a
held beat before each reveal, the last truth the biggest of all, then a quiet line and a question to you. Every number on
screen is one you could check on a calculator.

**The test:** pause on any frame and the one thing that just changed is the number being said, and you'd bet your own
money it's right.

## What this playbook is

You're editing one calm, seated talking-head take of a creator who explains how money (or anything countable) really
works, and you have the authority to make it the most trusted, most watched explainer in their niche. This playbook is the
style, pulled from four reels of the original creator (v01–v04), audited at full resolution and measured at full frame
rate, then sharpened. Read it all, every time. Use it the way a great editor uses a reference: take what fits this reel,
invent when a moment needs more, and never ship a frame that breaks the feel above.

**Who it's for and what it needs.** Creators who explain quantities: salaries, loans, discounts, investing, insurance, and
just as well calories, macros, hours or grams. Input: one front-on seated take (landscape 16:9, 4K preferred) and its
script; for the case-file format, 15–25 monochrome stills (the creator's own first, else real photos fetched from the
web, source noted). Everything else (cards, chips, bars, sliders, counters, the end card) is built. No cut-out is needed: the presenter lives in a fixed frame. Captions follow the creator's
language (English by default; Hinglish or Hindi set in their copy), and the numbers follow the language (₹ with Indian
grouping for Hinglish and Hindi, $ with international grouping for English). Machine values live in `tokens.json`; where
this text gives a number tokens also holds, they agree.

### Style directives (non-negotiable)
| # | Directive | Where it lives |
|---|---|---|
| D1 | **Teach with the graphic, never decorate.** Every card carries a number, a named quantity or the mechanism being said. No icons for flavour, no stock imagery | §8 |
| D2 | **Claim vs reality is the only comparison axis.** The false or assumed value is shown first in grey, then struck; the true value lands in a white tile | §4.2, P-14, P-15 |
| D3 | **Every number is right and recomputable.** It comes from the script, the creator, or a formula over those, and it lands within ±5 f of its spoken word. An illustration may use a made-up but realistic number (`illustrative: true`), with no label | §8.5 |
| D4 | **The presenter never moves.** No zooms, no punch-ins, no pop-backs, no layout that changes mid-reel. The frame is fixed for the whole body | §3.4, §10.2 |
| D5 | **Calm and trusted:** no shakes, no stickers, no meme sound, soft eases. The white flash belongs to the case file's story hinges only | §4.5, §9, §11 |
| D6 | **Small, plain captions inside the footage** (36 px, white, sentence case), never over the cards | §5.3 |
| D7 | **The topic picks the colour.** How-it-works and plans are teal; traps and myths are maroon; story episodes are case green | §4.3 |
| D8 | **Furniture without clutter:** series tags, ledger counters, sponsor and end cards slot into fixed places and never break the layout | §3.7, §6.7, §7.5 |

### Quick index
| § | What |
|---|---|
| §1 | Procedure: how to approach a reel in this style |
| §2 | Hard rules: the craft and the style's never-list |
| §3 | Formats F-A / F-B / F-C, worlds, layouts L-inset-top / L-face-bottom / L-cinema-top / L-endcard, stage moves, the board grid, safe zones, the slots, the person |
| §4 | Colour: roles, meanings, theme packs TH-teal / TH-maroon / TH-case, grades |
| §5 | Type and captions: the F-C title card, CS-1 quiet sentence (CS-2 on a scrim), other text, numbers |
| §6 | Hook system: HA-07 live number (openings O-1, O-2, O-3), HA-02, HA-12, hook pairs, writing, CTA and end cards |
| §7 | Structure and rhythm: L-BUILD, L-LIST, L-CALC, S-CASE, markers, the rituals, open loops, series furniture, rhythm |
| §8 | Visual system (B-roll and patterns): 10 families, P-01…P-52, line → pattern lookup, the data contract, running state |
| §9 | Transition system T-1…T-9 |
| §10 | Motion tokens, camera and zoom (none), layers, finishing |
| §11 | Sound |
| §12 | Footage handling: setup, shots SH-1…SH-6 and fallbacks FB-1…FB-6, third-party moments |
| §13 | What your plan should settle |
| §14 | Worked examples (4) |
| §15 | Your look at the storyboard: the checklist |
| §16 | Build notes |
| App. A / B | Evidence map / hook-title bank |

---

## §1 Procedure: how to approach a reel in this style

You watch, listen, plan, build and look at the storyboard yourself; the edit skill has the mechanics. This style's
craft is turning talk into a ledger the viewer can check: every quantity becomes a row, a chip, a tile, a bar or a step,
and every one of them lands on its word.

1. **Pick the format** (§3.1). The script steps one calculation through a changing parameter → F-B. It tells a story with
   dates, people and places → F-C. Everything else → F-A.
2. **Pick the theme** (§4.3) by the hook's topic: how something works → teal; a trap about to be exposed → maroon; a story
   episode → case. One theme for the whole reel.
3. **Do the maths first.** Write `plan/figures.json` before a single card: every number on screen as an input with
   provenance (`script` + `said`, `creator`, `spoken@t`) or a formula over inputs (§8.5). Run `veos figures` and settle
   every mismatch with the script now (a tool for the maths, never a gate). A wrong number is the one thing this style can't survive.
4. **Find the units and the trigger words.** Segment into the structure's units (§7.1): L-BUILD (parameters → build →
   stress test → moral → question), L-LIST (promise → item 1…N → payoff), L-CALC (question → parameters → steps → why →
   transfer), S-CASE (title → chapters → turn → open question). Mark the trigger word of every beat: the number word for a
   value, the item word for a tile, the verdict word ("only", "actually", "but", "No") for a strike. Mark jump-cut points on
   word boundaries only.
5. **Feel the tone of every line:** `explain` · `claim` (the belief or the advertised value: grey) · `reality` (the true
   value: the white tile) · `warn` (costs more, a risk: a red tag) · `win` (cheaper, fixed: a green tag) · `story` · `cta`.
6. **Write the hook** (§6): the opening, the first sentence with its number, the post title (8–10 candidates, the best by
   the stopper test, two alternates), the claim → evidence pair.
7. **Line → ledger move.** For every line: which row, chip, tile, bar or slider step it creates or changes, which lane of
   the board grid it lands in (§3.5), and which element it replaces. One board scene per section (§8.2). Decide where the
   board holds while the creator talks, and make the last item the biggest.
8. **Plan the state and the furniture:** the F-B parameter steps and the F-C ledger states with their `at` words (§8.6),
   the series number and case index (§7.5), the sponsor's logo (the creator's, else fetched from the sponsor's site) and
   the spoken disclosure line (§6.7).
9. **Get the third-party moments** (§12.4): the creator's files first, else the real thing fetched from the web (source
   noted); rebuild from exact text only when nothing usable turns up. Pick the fallbacks (§12.2).
10. **Plan the sound** (§11): reveals, the list cue and the CTA. Still cuts and row builds are silent.

---

## §2 Hard rules: the craft and the style's never-list

**Craft, by eye** (judge it on the storyboard, in context, the way an editor does):
- **Keep the person clear.** The trust lives in the face, so keep the presenter window (L-inset-top x 96–984, y 112–612;
  L-cinema-top x 64–1016, y 960–1496) and the face cell under the F-B seam clear of the board: cards, chips, tags and
  inserts live beside the window, not in it. The caption sits in the bottom strip of the window, below the chin (§3.8), or
  on the chest in F-B. A caption brushing the chin for a beat is fine; a face buried or a head chopped by accident never
  is.
- **No text over text.** One board scene per section, the captions in their own place, slots that never overlap each
  other or the window. Never two cards stacked by accident.
- **On the word.** A row, chip, tile or tag starts 2 f before its trigger word and is fully on within ±5 f of it; a value
  lands on its number word within ±5 f; a slider step lands on its step word. Jump cuts sit on word boundaries ±1 f;
  audio is never offset.
- **Numbers right.** Every number on screen is a figure in `plan/figures.json` with provenance, recomputes within display
  rounding, and is either spoken or the result of a formula over those; compared values share one `scale_id`. A number the
  creator says is shown exactly as said. Illustrations may use made-up but realistic numbers (`illustrative: true`), with
  no label. Never a fake bank statement, dashboard or app screen presented as the creator's real one.
- **Number format.** The ₹ glyph (never Rs or INR), Indian grouping (₹1,31,190), lakh and crore compacts on chips and
  tiles ("₹75 L", "₹1.25 Cr"), full grouping for computed amounts, never K/M/B on rupees. In English, `$` with
  international grouping (`$120,000`, `$1.2M`). Never both in one reel.
- **Promise integrity.** The rank numerals equal the items delivered; every "let's see" and "how did this happen?" is
  answered on screen (the S-CASE closing question is the one loop left open, and it names the next episode); the CTA
  keyword, if chosen, is on screen ≥ 1.5 s.
- **Spelling.** Brand and product names exact; glossary terms enforced in captions and on cards.
- **Readable.** Captions 36 px, weight 500, contrast ≥ 7:1 (≥ 4.5:1 on the CS-2 pill) under E3; labels 28–39 px only when
  redundant (the words are spoken in the same beat or shown larger beside them), otherwise ≥ 40 px. Red and green text sit
  only inside a filled chip or on a white card, never directly on the world. `ghost` only for display text ≥ 96 px or as a
  pill fill behind `ink` text. A skeleton card never waits empty: it fills within 1.2 s of entering.
- **Instagram's buttons.** Meaning text stays inside x 64–1016, y 110–1500; from y 900 to y 1540 nothing that carries text
  reaches past x 960 (the like, comment and share buttons sit at x > 970).
- **Sponsor disclosure.** A sponsor card always has the spoken disclosure and the visible "Paid partnership" label.
- **Audio.** −14 LUFS integrated, true peak ≤ −1.5 dBTP, the bed ≥ 18 dB under the voice, a hard end ≤ 6 f after the end
  card's last frame, no black tail longer than 0.2 s.

**Never in this style:**
- Zooms, punch-ins, crash zooms, shakes, rotation snaps or Ken Burns, on the presenter or on the stills.
- Stickers, stamps, emoji, marker scribbles, meme sounds, light leaks, RGB splits. White flashes on the ledger formats
  (F-A, F-B): the flash belongs to the case file's story.
- Coloured words inside captions, word-by-word karaoke, ALL CAPS captions, caption pills (except CS-2 for a whole reel).
- A lone number on an empty background with nothing it compares to. Every hero number has its claim, its unit line or its
  partner.
- Bars of compared options on different scales; a bar whose length disagrees with its value; a status tag that contradicts
  the bars.
- Red or green for anything but bad and good. White text on `good` below 4.5:1 (use `#26803A`, never the source's
  `#2E8B3A`).
- Stock footage, stock icons as content, hooded-hacker or money-rain clichés. A real logo or screenshot the reel names is
  the real thing (the creator's or fetched), never a generic stand-in.
- Decorative icons, empty cards, a card that says nothing the creator said.
- More than one layout in the body; splits, PiPs or bubbles that appear mid-reel.
- More than three bright hues in a frame.
- Anything after the end card.

---

## §3 Worlds, layouts, stage moves, safe zones

### 3.1 Formats: three frames around one calm presenter
| Field | F-A Ledger inset (default) | F-B Face-bottom calculator | F-C Case file |
|---|---|---|---|
| When | Build the numbers (2–4 named quantities → total → stress test → moral), or a claim-vs-reality list of 3–7 items | One calculation stepped through a parameter (years, months, servings): two options on one axis → why → transfer to a second case | A documentary story told as one episode of a numbered series, with a running ledger |
| Layouts | `L-inset-top`, `L-endcard` | `L-face-bottom`, `L-endcard` | `L-cinema-top`, `L-endcard` |
| Structure | L-BUILD or L-LIST | L-CALC | S-CASE |
| Hook default | HA-07 (opening O-1 row build or O-2 rank skeleton) | HA-07 (opening O-3 dual stat question) | HA-12 thesis typography |
| Graphics | primary: the board carries the argument | primary: the panel carries the argument | support: the stills carry the story; the case tag and the ledger counter are the furniture |
| Needs | the take | the take (a vertical or 4K take is best, §12) | the take + 15–25 monochrome stills the creator owns |
| Theme | TH-teal or TH-maroon by topic | TH-teal or TH-maroon by topic | TH-case only |

**What the three share:** the same calm presenter in a fixed frame, the same Poppins figures with the language's grouping,
the same claim-vs-reality colour axis, the same quiet in-footage captions. Only the frame around the presenter changes.

### 3.2 Worlds
| ID | Kind | Look (colours come from the active theme) | Carries | Enter / exit |
|---|---|---|---|---|
| **W-ledger** | `card-world` | A vertical two-stop gradient (TH-teal `#0D2B2B` → `#2E7A72`; TH-maroon `#1E1411` → `#8E524D`), a soft radial glow r 760 at (820, 1560) drifting ±24/18 px, film noise 0.04, vignette 0.12. It looks like a blurred room behind frosted glass | All the cards, chips, bars and tiles of F-A and F-B; the F-B top panel | Present from f0 to the end card; never changes mid-reel |
| **W-case** | `stage` | Near-black `#050805` → green `#135C2C`, noise 0.05, vignette 0.2 | F-C: the area under the still band and behind the presenter clip; the title card | From f0 to the end card |
| **W-endcard** | `void` | Pure `#000000` | The end card only | T-7 hard cut in; the reel ends on it |

### 3.3 Layouts
| ID | Engine | The presenter (px) | The graphic area | Caption |
|---|---|---|---|---|
| **L-inset-top** | `card` | x 96, y 112, w 888, h 500 (16:9), **square corners, 4 px `paper` border**, shadow 0.3, face 0.3, eye 0.4 (measured v01/v02: window x 108–970, y 73–567, border 4 px, radius 0; the real top at y 73 sits in Instagram's top band, so it moves to 112 here) | The **board**: x 64–1016, y 660–1500 (the graphic rect is x 64–960, w 896: below y 900 board text ends at x 960) | `inside_footage`, its bottom 22 px above the window's bottom edge (centre ≈ y 568) |
| **L-face-bottom** | `stack` | The bottom cell y 760–1920, footage `cover`, face 0.30 of the cell height, eye line at 0.22 (≈ y 1015); a 220 px `stage` blend on both sides of the seam, so the room melts into the panel (measured v03: footage visible from y ≈ 450, blended to y ≈ 700; eyes y ≈ 925–1000). The real bottom ≈ 360 px goes to black (y 1560–1920, a heavy vignette under the chest) | The **panel**: x 64–1016, y 120–740 | `fixed_y`, centre y 1462 (on the chest) |
| **L-cinema-top** | `card` | x 64, y 960, w 952, h 536 (16:9), radius 6, 2 px `paper` border, shadow 0.35, face 0.3, eye 0.4 | The **still band**: x 0–1080, y 0–940 (the title card in the hook) | `inside_footage`, its bottom 22 px above the window's bottom edge (centre ≈ y 1452) |
| **L-endcard** | `hidden` | none | x 64–960, y 110–1500 | hidden: captions never show on the end card |

**One layout for the whole body.** The end card is the only other layout, and the reel ends on it (≤ 3.5 s).

### 3.4 Stage moves
| ID | Move | Recipe | Use |
|---|---|---|---|
| **G-1** | **Hold** | The presenter window never moves, scales or crops differently during the body | Always |
| **G-2** | **Cut to end card** | `via: cut` on the last word: the presenter and the board vanish on one frame, W-endcard is black and the P-44 block slams in (scale 2.6 → 1.0, 18 px motion blur, 3 f; measured v01 @ 45.00–45.08) | The last 2.5–3.5 s, after the last spoken word or on the CTA line |

There are no other stage moves. A pop-back, a split change or a zoom would break the one promise this style makes: the
person stays put and the numbers move.

### 3.5 Layout diagrams and the board grid

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
| Row 2 | 870–1050 | the same offsets +194 |
| Total | 1066–1186 | total card w 420 centred (x 330–750), number 56 px (real cap 37 px ≈ 53 px) + sub-line 28 px |
| Tiles | 1200–1386 | micro header 28 px (1200–1232) · 3 columns of tiles w 284, h 64, gap 22 (x 64 / 370 / 676, ending at x 960), rows 1244 and 1322 |
| Footer | 1410–1500 | summary line 44 px (1410–1462) + helper 32 px (1466–1500) |

**Board grid, L-LIST mode (claim vs reality rows):**
| Lane | y | Holds |
|---|---|---|
| Tabs | 648–692 | N chip tabs, equal widths, gap 12, 28 px caps |
| Row k (k = 0…4) | 724 + 156·k → 860 + 156·k | rank numeral 100 px at x 64–150 · title 50 px at x 176 (real cap 36 px ≈ 51 px) · sub-label 32 px at x 176 (+56) · struck/claimed value 40 px right-aligned to x 700 with micro-label 28 px under it · reality tile x 720–960, h 120 (clear of the IG button column), centred in the row |
| Footer | under row 5: a saved-note line at the row's right (P-17) | — |

Five rows end at y 1484. **Six or seven items:** row pitch 124, numerals 96 px, the reality tile h 100 (still inside the
floors). More than seven items: split the reel. The last row's escalated tile (P-16) is wider (x 630–960), so its claimed
value moves left and right-aligns to x 610.

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
├≈≈≈≈≈≈≈≈ seam y 760 ≈≈≈≈≈≈≈≈≈≈┤ ← 220 px `stage` blend (footage shows from ≈ y 680)
│      presenter, full width   │ ← eyes ≈ y 1015
│      caption, 36 px, chest   │ ← centre y 1462
└──────────────────────────────┘ 1920
```
The opening stat cards (P-19) occupy y 220–520 (two cards w 456, h 300, gap 40) before they morph into the bar badges.

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
The title card (hook, 0–3 s): the episode label y 128–164 at x 64; title lines (150 px, line height 0.86) at y 170 / 299 /
428 with x indents 64 / 300 / 110; the chapter line 56 px at y 600 with a 160 × 4 px accent rule at y 588; the prop rests
on a lit table plane at y 700–900.

### 3.6 Safe zones and bands
- **Meaning text:** x 64–1016, y 110–1500 (`layout.safe`). The board, the panel and the still-band text stay inside it.
  From y 900 to y 1540 nothing that carries text reaches past x 960: the board's reality tiles, the tile grid (P-05), the
  footer sponsor card (P-43) and the keyword card (P-45) end at x 960.
- **Captions:** inside the presenter window (F-A, F-C) or the band y 1440–1484 (F-B). Graphics never enter it.
- **Headline:** none in F-A and F-B; the F-C title card fills y 128–660 during the hook only.
- **Slots:** S-tabs y 648–692; S-panel-title y 128–188; S-case-tag y 140–188; S-ledger y 132–264 (§3.7).

### 3.7 The frame and its slots
The frame never changes; only the content inside it does. The plan writes only `slot_content`.

| Slot | Rect (px) | z | Lifetime | Content | Entry | Swap |
|---|---|---|---|---|---|---|
| **S-frame** | x 96, y 112, w 888, h 500 (F-A) · x 64, y 960, w 952, h 536 (F-C) · the bottom cell y 760–1920 (F-B) | stage | the whole reel | the presenter | none (on from f0) | none |
| **S-tabs** | x 64, y 648, w 952, h 44 | 6 (drawn inside the board scene) | the L-LIST section | chip tabs (P-12) | the pills fade in 2 f each, 3 f stagger, rising 6 px | E6 colour swap, 4 f |
| **S-panel-title** | x 64, y 128, w 952, h 60 | 5 (inside the panel scene) | the whole F-B reel | the panel title (P-18) | fade 6 f | E6: the old text fades 4 f, the new fades in 6 f |
| **S-case-tag** | x 64, y 140, w 400, h 48 | 6 | F-C, after the title card | "case nn / of" + dots (P-39) | fade 8 f | none (it never changes inside a reel) |
| **S-ledger** | x 656, y 132, w 360, h 132 | 6 | F-C, from the first money word | the ledger counter (P-40) | rise 8 px + fade 8 f | E6: the state word hard-swaps, the value counts as P-40 |

Slot rects stay constant within ±4 px for their lifetime (look at them on the storyboard). Slots never overlap each other or
the presenter window. The case tag and the ledger counter each count as one text element for their whole life.

### 3.8 The person
- **Never leaves.** The presenter is on screen for the whole body; the only absence is the end card (≤ 3.5 s). There are
  no cutaways, so there's nothing to come back from.
- **Framing.** F-A and F-C show the full 16:9 frame: the head top at 18–30 % of the window height, the eyes at 40 %
  (L-inset-top: eyes ≈ y 312, head top ≈ y 202–262; L-cinema-top: eyes ≈ y 1174). F-B crops 9:16 from the take with the
  eye line at y ≈ 1015 and the head top at y 800–880 (v03: head top ≈ 790).
- **The head region and the caption.** In L-inset-top the caption's bottom sits at y 590 (one line ≈ y 545–590; a second
  line reaches up to ≈ y 500), the bottom strip of the window, under the chin, which falls around y 360–420. In
  L-cinema-top the caption sits at ≈ y 1430–1474 under a chin around y 1230–1290. In F-B the caption band y 1440–1484 is on
  the chest, about 400 px below the eyes. If a take is framed lower than the setup (a chin in the bottom fifth of the
  window), the caption doesn't climb onto the face: set the window's crop higher in the take, once, for the whole reel.
- **Behind and in front.** Behind the person is fair game in this engine, text included (`behind: true`), but this style
  has no cut-out: the presenter is a framed window and the board lives beside it, not in it. Keep the front of the head
  clear unless the moment wants otherwise, judged by eye.
- **Wardrobe and room.** One plain dark top; the same styled room in every reel (§12.1).

---

## §4 Colour system

### 4.1 Role palette
| Role | Hex | Its one job | Text on it | Contrast |
|---|---|---|---|---|
| `primary` | `#FFFFFF` | The "you are here" highlight: the current chip tab, the slider handle, the end-card arrow, the CTA keyword card | `ink` | 18.9:1 |
| `accent` | `#40E87A` | The story's thread: F-C ledger digits, case dots, the episode label, the one accent object in stills; the series tag in F-A/F-B | `ink` | 11.7:1 |
| `stage` | by theme (`#14403D` teal, `#3A2420` maroon, `#0B1F10` case) | The world tone at the F-B seam blend. Never text | `paper` | ≥ 10:1 |
| `data` | by theme (`#1F5A5C` teal, `#5A2E2A` maroon, `#135C2C` case) | The **first** compared option: its stat card, bar fill and label badge | `paper` | 7.9:1 (teal) |
| `night` | `#1C1C1C` | The **second** compared option: its stat card, bar fill and badge | `paper` | 17.0:1 |
| `bad` | `#C8283C` | Costs more, the false belief, the strike line, the empty dashed bar, the worse method tag | `paper` | 5.5:1 |
| `good` | `#26803A` | Cheaper, the true value's check, the better method tag | `paper` | 5.0:1 |
| `ink` | `#111111` | All text on white cards | — | 18.9:1 on paper |
| `paper` | `#FFFFFF` | Cards, chips, tiles, captions, summary lines on the world | — | 5.1:1 on the teal bottom, 6.1:1 on the maroon bottom |
| `muted` | `#6B6B6B` | Micro-labels on white ("you think", "a year", "her salary") | — | 5.3:1 on paper |
| `ghost` | `#D6CFCC` | Future items: unlit rank numerals (100 px, ≥ 3:1) and unlit tab pills (with `ink` text) | `ink` | 3.3:1 on the teal bottom, 3.9:1 on maroon (display ≥ 96 px only) |

The creator's brand colours land on `primary` and `accent` only (set in their copy); `bad` and `good` are fixed, and the
packs keep their own world hues, because the hue carries the topic. The bright hues are `primary` when branded, `accent`,
`data`, `bad` and `good`; white isn't one of them.

### 4.2 Meanings
- **Axis 1, claim → reality:** grey (`muted` on cards, `ghost` on the world) = what you think, what is advertised; a white
  tile with an `ink` figure = what is true.
- **Axis 2, worse → better:** `bad` red = costs more, flat, false, empty; `good` green = cheaper, reducing, checked.
- **Two options compared:** option A is always `data` (the theme tone), option B always `night`. Their colour never
  encodes good or bad; the tags do.
- **Accent** means "this is the story's thread" (the money in the F-C ledger, the one coloured object in each still).
- **Brand colours** appear only on brand elements (the sponsor card's logo, the creator's thumbnail) and on `primary`.

### 4.3 Theme packs (one per reel, chosen by topic)
| Pack | `W-ledger` gradient (top → bottom) | Glow | `data` / `stage` | Topic → theme |
|---|---|---|---|---|
| **TH-teal** (default) | `#0D2B2B` → `#2E7A72` | `#4A9A90` at 32 %, r 760 at (820, 1560) | `#1F5A5C` / `#14403D` | How something works, building the numbers, comparisons, plans. Money: salary, loans, EMIs, insurance, investing. Elsewhere: calories, macros, hours, sleep, reps, the price of a plan |
| **TH-maroon** | `#1E1411` → `#8E524D` | `#A8645C` at 30 %, r 760 at (760, 1700) | `#5A2E2A` / `#3A2420` | A trap is about to be exposed: offers, discounts, hidden fees, scams, myths, "healthy" products, misleading labels |
| **TH-case** | `#050805` → `#135C2C` (world W-case, noise 0.05) | none | `#135C2C` / `#0B1F10`; `accent` `#40E87A` | F-C story episodes only |

- One theme per reel. When a reel is half mechanics and half trap, the **hook's** topic decides.
- F-C always uses TH-case; F-A and F-B never do.
- Every pack keeps `paper` text readable on its lightest stop.

### 4.4 Grades
- **Footage:** not regraded in F-A and F-B (the room keeps its natural warm light).
- **GR-case-mono** (F-C): the look is a monochrome presenter clip and stills (`grayscale(1) contrast(1.12)
  brightness(0.92)`) with the accent hue isolated on one object. The engine can't isolate the accent on a clip yet, so
  the stills are monochrome (the creator's come that way, SH-2; a fetched photo gets the grayscale filter in its scene)
  and the presenter clip stays in natural colour. Never fake the isolation by tinting the whole clip green.
- No grade events: the look never changes mid-reel.

### 4.5 Rules
- Three bright hues at most in a frame; a typical frame uses one (`data` or `accent`) plus at most one tag colour.
- Coloured text never sits directly on the world: red and green text always sit inside a filled chip (`bad`/`good` with
  `paper` text) or on a white card.
- The world never changes colour mid-reel.
- Footage is not regraded, except GR-case-mono in F-C when the engine can do it.

---

## §5 Type and captions

### 5.1 Font map
| Slot | Family | Weights | Used for |
|---|---|---|---|
| `display` | Poppins | 600 / 700 / 800 | row titles, labels, panel titles, summary lines, chips, tags |
| `body` | Poppins | 500 / 600 | captions, sub-labels, micro-labels, explain lines |
| `numeric` | Poppins | 700 / 800, `font-variant-numeric: tabular-nums` | every figure |
| `title` | Poppins | 800, line height 0.86 | the F-C staggered title |

The family stays a geometric sans (Plus Jakarta Sans, Jost or Inter Tight are the bundled swaps); never a serif, a
condensed face or a rounded display face. Hindi (Devanagari) captions and labels fall back to Noto Sans Devanagari 500/700.

### 5.2 The headline element
F-A and F-B: **none** (`type.headline.kind: none`). The claim is carried by the first caption sentence and the board itself;
the F-B panel title (P-18) is a label, not a headline.

F-C: **the title card** (`title_card`, lifetime `hook`):

| Property | Spec |
|---|---|
| Text | 2–4 lowercase words in 3 staggered lines ("money / doesn't / behave"), Poppins 800, 150 px, line height 0.86, tracking −1 % |
| Layout | line x indents 64 / 300 / 110; tops y 170 / 299 / 428; ≤ 3 lines, ≤ 4 words |
| Colour | each line lands grey `#8C8C8C` and whitens to `paper` |
| f0 | the episode label ("episode one", 28 px `accent`) is on at f0; line 1 starts at 0.60 s, line 2 at 0.70 s, line 3 at 0.80 s (measured v04: 0.62 / 0.70 / 0.78) |
| Build | per line: blur 14 → 0 px, opacity 0 → 1, 3 f ease-out, no rise; each line lands grey and whitens over 10 f, so all three are white by ≈ 1.0 s (v04 @ 0.62–1.02) |
| Life | the chapter line ("that phone call", 56 px, 700) types under it from 1.6 s (1 character per frame) after a 160 × 4 px accent rule wipes in (6 f) |
| Exit | at ≈ 3.2 s the whole card (title, rule, chapter, prop) fades out over 4 f, then a hard cut into still 1 (T-6; v04 @ 3.20–3.36) |
| Read | ≤ 1.5 s |

### 5.3 Caption profiles
**CS-1 "Quiet sentence"** (`extends: lib:warikoo`), the default for every layout. The caption is a quiet companion to the
board: it says the sentence, small and plain, and never competes with a number.

| Group | Value |
|---|---|
| Mode | `full` · role `support` · `mute_safe` |
| Chunking | unit `sentence`; 4–9 words per chunk (mean ≈ 6.5); ≤ 44 characters per line (the real lines run to 43 characters on one line, x 130–949, e.g. "One offer will be 30% off, another 20% off."); ≤ 2 lines (prefer 1); never split a name, a number or its unit ("₹2.5 lakhs" stays together); break on `. ? !` and on pauses ≥ 0.9 s; punctuation kept |
| Timing | lead 2 f before the first word; ≥ 0.25 s per word; tail 0.25 s; swap = **hard cut, 0 f** (the next sentence replaces the last on one frame; on a jump cut it lands on the cut frame; measured v01 @ 12.08, v03 @ 7.84, v04 @ 0.94); a pause ≤ 0.6 s holds the last chunk |
| Skin | `body` Poppins **500**, **36 px** (`TC-subtitle`, E3), line height 1.25, sentence case as spoken, tracking 0, `paper`, no stroke, shadow `0 1 4 rgba(0,0,0,.65)`, no container |
| Position | F-A and F-C: `inside_footage`, its bottom edge 22 px above the presenter window's bottom edge, centred, max width 840 px (measured: Poppins ≈ 37 px, glyph band y 540–567 in a window ending at 567). F-B: `fixed_y`, centre y 1462, max width 800 px. `avoid_face` on |
| Emphasis | **none**. No bold, no colour, no size change, ever |
| Variants | karaoke, tiers, duet, stack: none |
| Hide | during T-7 and on the end card |
| Language | Latin script by default (`transliteration: keep_english_terms`, spelling normalised); Devanagari supported (`hi/hi/Deva`); profanity masked `inner` (`S**T`); glossary from the creator's brand names. Spoken numbers stay digits ("₹2.5 lakhs", "51,880"); Hinglish speech may be captioned as clean English sentences when the copy says so, keeping English terms and brand names verbatim |

**CS-2 "Quiet sentence on scrim"** (fallback): identical to CS-1, but on a pill (`ink` at 55 %, radius 10, padding 6/16, no
shadow). **Use it for the whole reel** when the take is bright behind the chin line (a white wall, window light) so that
CS-1 measures below 7:1. Never mix CS-1 and CS-2 in one reel.

### 5.4 Other text
| System | Class | Recipe | Hold |
|---|---|---|---|
| Row label (P-01) | TC-label 32 px, redundant | `display` 800 caps, tracking 0.04, `paper` on the world | while the row lives |
| Micro-label | TC-label 28 px, redundant | `body` 500, `muted` on white / `paper` at 80 % on the world; ≤ 4 words, taken from the spoken line or from the fixed set {you think, you actually get, you pay, you get, a year, a month, was X, saved} | with its value |
| Row title (P-13) | TC-label 50 px | `display` 700, `paper`, ≤ 18 characters | while the row lives |
| Sub-label | TC-label 32 px, redundant | `body` 500, `paper` at 85 %; ≤ 4 words taken from the spoken sentence of that row. If the words are not spoken, set it at 40 px | with the row |
| Value chip (P-02) | TC-display 42 px | `numeric` 800 `ink` on a white chip; unit line 28 px `muted` under it | with the row |
| Reality tile (P-15) | TC-display 56 px (final 96 px) | `numeric` 800 `ink` on white, micro-label under it | to the end of the list |
| Struck value (P-14) | TC-label 40 px | `numeric` 700 `paper` at 75 %, strike 4 px `bad` | to the end of the list |
| Rank numeral (P-11) | TC-display 100 px | `numeric` 800; unlit `ghost`, lit `paper` | the whole list |
| Chip tab (P-12) | TC-label 28 px caps, redundant | `display` 700, tracking 0.08; pill h 44, radius 22; unlit: `ghost` fill + `ink` text; lit and past: `paper` fill + `ink` text | the whole list |
| Status tag (P-03 / P-04) | TC-label 28 px, redundant | `display` 800; outline: 2 px `paper` border, caps, `paper` text; filled: `bad`/`good` fill, `paper` text, sentence case ("Cheaper?") | with its row |
| Panel title (P-18) | TC-label 44 px | `display` 600 `paper`, left-aligned at x 64 | per section |
| Parameter chip (P-21) | TC-label 28 px, redundant | `body` 600 `ink` on `paper` at 92 %, pill h 44 | the whole calculation |
| Stat card (P-19) | TC-display 132 px | `numeric` 800 `paper` + unit 28 px | the opening |
| Explain line (P-26) | TC-label 40 px | `body` 500 `paper`, left-aligned, ≤ 36 characters, "<Method>: <how>" | to the end of the section |
| Summary line (P-09 / P-10) | TC-label 44 px + helper 32 px (redundant) | `display` 700 `paper` centred; helper `body` 500 at 80 % | ≥ 2.0 s |
| Total card (P-06) | TC-display 56 px + sub-line 28 px | a white card, `numeric` 800 | to the end |
| Ledger counter (P-40) | TC-display 56 px + the header in the 24 px legal class + sub 28 px (redundant) | `numeric` 700 `accent`, right-aligned to x 1016, an `accent` glow 28 px at 45 % for 12 f after each landing | the whole F-C body |
| Case tag (P-39) | TC-label 28 px, redundant | `body` 600 `paper` at 85 % + 7 dots (8 px, gap 8; lit `accent`, unlit `paper` at 30 %) | the whole F-C body |
| Keyword card (P-45) | TC-display 72 px | `display` 800 caps `ink` | to the end |
| Disclosure | the 24 px legal class | `body` 500 `paper` at 75 %, inside the sponsor card's top-right | the whole sponsor card |

### 5.5 Language and numbers
- Spelling: English words and brand names exact; Hinglish captions (when chosen) phonetic but consistent within a reel.
- Numbers on screen are always digits written by `ctx.fmtNum` (never typed): `₹1,31,190` (full, for computed amounts),
  `₹75 L` / `₹1.25 Cr` (short, for round amounts on chips and tiles), `44%` (percent, 0–1 decimals as stated), `2x`
  (ratios as spoken).
- **Chip rule:** a value the script says as "X lakh" or "X crore" uses `style: short`; a computed or exact amount uses
  `style: full`. One style per figure for the whole reel.
- Numbers follow the language: Indian grouping and ₹ for Hinglish and Hindi; international grouping (`$120,000`, `$1.2M`)
  for English (the default). Never mix both in one reel.
- Units: metric; non-money units through the format's `suffix` (" kcal", " g", " h", " km").
- Devanagari: no italics, no caps; tabs and tags keep Latin digits.
- The ₹ glyph is in Poppins; no pre-painting is needed.

---

## §6 Hook system

In this style the hook isn't a title: it's a number. F-A and F-B open mid-explanation, on the first quantity, with the
ledger already building under the creator; the first caption sentence carries the number and the board proves it inside
the first second. The promise to the viewer lives in the **post title** (and, in F-C, the title card): it promises an
outcome, a curiosity gap or who it's for ("5 online offers that are cheating you", not "Online offers explained"). It
doesn't have to repeat the spoken words; it has to be true to what the reel delivers. Write 8–10 candidates from §6.5 and
the proven patterns ("How to X as a Y", "Why your X isn't working", "The X nobody tells you", "Stop doing X", a number or
a contrast), score them on outcome, curiosity, who it's for and brevity, pick the best by the stopper test, and keep the
next two as alternates.

### 6.1 The stopper test
- **On mute,** the first three seconds show the subject (the caption) and the first quantity (the board).
- **Motion at f0:** the first board element is already entering on frame 0, and the presenter is live. A board with
  nothing moving at f0 fails (the original's weak v02 opening, an empty column for 1.3 s, is not copied).
- **Payoff:** the first number or data row is visible by 1.0 s (F-A, F-B); the F-C title is complete by 3.0 s and reads in
  ≤ 1.5 s.
- **Dense in time, never in space:** a row, its chip, a second row, a tag and two caption swaps inside three seconds, each
  landing as the last one settles.

The cover is the post title, not frame 0, so there's no thumbnail test.

### 6.2 The default hook: HA-07 "Live number / ledger open"
The spoken pattern is **state the subject's number, then start building the ledger under it**: "<Subject> earns ₹X a year.
I earn ₹Y. But the house runs on my salary." There is no title, no tease and no question card; the reel starts
mid-explanation with a quantity.

**Opening O-1 "Row build"** (F-A, L-BUILD; from v01):

| t (s) | Beat | Tone | On screen (board scene `board-1`, z3, kind `ledger`) | Caption | Motion (30 fps) | Cue |
|---|---|---|---|---|---|---|
| **0.00 (f0)** | The claim sentence starts | explain | Presenter live in the inset. The row-1 label "<NAME>" + micro-label "<whose / what>" entering | "<Subject> earns ₹X a year." (on from f0) | label: opacity 0 → 1, rise 6 px, 6 f | — |
| 0.13 | — | explain | The empty bar wipes in L → R under the label (x 64 → 600), grey at its leading edge, white as it grows | same | width 0 → 536, 7 f ease-out (v01 @ 0.12–0.36) | — |
| **≤ 1.0 (on "X")** | **Payoff** | explain | The chip pops right of the bar: a small `ghost` pill grows into the white chip "₹X L" + unit line "a year" | same | scale 0.25 → 1.08 → 1.00 over 4 f, `ghost` → white as it grows, the value legible from f2 (v01 @ 0.40–0.52) | **reveal** |
| 1.0–2.0 | hold | explain | — | swap to "<Second subject> earns ₹Y." | caption hard swap | — |
| 2.0 | Row 2 | explain | The row-2 label + micro-label enter in lane 2 | same | 6 f | — |
| 2.13 | — | explain | The row-2 bar wipes in (on the same scale as row 1) | same | 7 f | — |
| on "Y" (≈ 2.5) | value 2 | explain | The row-2 chip: ghost → "₹Y L" | same | as above | — |
| on the twist word (≈ 2.8–3.2) | the turn | claim | An outline tag under row 2 ("RUNS THE HOUSE") | "But <the twist>." | rise 6 px, 6 f | — |

Seven things change in the first three seconds, and none of them fights another: that's the density this hook is built for.

**Opening O-2 "Rank skeleton"** (F-A, L-LIST; from v02, with its weak frame 0 fixed):

| t (s) | Beat | On screen | Caption | Motion | Cue |
|---|---|---|---|---|---|
| **f0** | The promise sentence | Presenter live. The S-tabs row rises in (N pills, all `ghost`) | "These N <things> <hurt> you." | each pill fades in over 2 f, 3 f stagger (v02 @ 1.24–1.52) | — |
| 0.20 → 0.20 + 0.13·N | — | The rank numerals 1…N appear one by one in `ghost` | same | each: fade 3 f, 5 f stagger, no rise (v02 @ 1.40–1.88) | — |
| **≤ 1.0** | Payoff | The numeral "1" lights `paper`; tab 1 lights white (E6 swap) | same | colour 4 f | **list cue** |
| on item 1's claim word (≈ 1.5–2.5) | Claim | The row-1 title slides in from x 136 → 176 with its claim ("30% + 20% off") | "One offer is <claim>." | slide 40 px + fade, 8 f | — |
| +0.2 | — | The sub-label ("Stacked discounts") | same | fade 6 f | — |
| on "you think / we feel" | Claim value | "50%" + "you think" in grey, right-aligned to x 700 | "We feel we're getting <X>." | fade + rise 6 px, 6 f | — |
| on "No / only / actually" | **Reality** | The white tile "44%" + "you actually get" pops in the reality-tile column (x 720–960), and the strike snaps across "50%" | "It's only <Y>." | the tile pops from a `ghost` pill: scale 0.25 → 1.08 → 1.0, 4 f; the strike snaps across "50%" in 2 f on the same beat (v02 @ 7.40–7.52, 13.54–13.62) | **reveal** |

The unlit numerals are the open loop: the viewer can see how many are left.

**Opening O-3 "Dual stat question"** (F-B, L-CALC; from v03):

| t (s) | Beat | On screen (panel scene `calc`, z3, kind `ledger`) | Caption | Motion | Cue |
|---|---|---|---|---|---|
| **f0** | The question starts | The panel title "Would you choose" (44 px) + ghost card A (`data` at 30 %) | "Would you choose <option A>" | title fade 6 f; card fade 4 f | — |
| 0.17 | **Payoff** | Card A fills: "8%" (132 px) + unit "loan" (28 px) | same | `data` opacity 0.3 → 1 over 4 f; figure pop 1.05 → 1 over 6 f | **reveal** |
| 0.83 | Tag | The "Cheaper?" `good` chip drops onto card A's top edge | same | drop 12 px + fade, 6 f | — |
| 1.5 | Option B | Ghost card B → fills `night` "11%" + "loan" | "or <option B>? Let's see." | as card A | — |
| 1.83 | Axis | A white "Total <quantity>" bar skeleton slides up under both cards | same | rise 16 px, 8 f | — |
| 2.17–2.47 | **T-3 morph** | The cards shrink and blur into the two bar badges; the title swaps to the real question "Which <option> costs you more?" | same | 9 f (§9; v03 @ 2.16–2.44) | — |
| on the first parameter word (≈ 2.8) | Parameters | Parameter chip 1 ("₹2.5 lakh loan") | "The loan is ₹2.5 lakhs." | fade + rise 6 px, 6 f | — |

### 6.3 Alternate hooks

**HA-02 "Headline + proof"** (F-A L-LIST, when the creator wants a stated title). For the first 2.5 s the board's top lane
carries a 44 px title in the summary-line recipe ("<N> <things> that cheat you"); the proof is item 1's reality tile by 2.5 s.

| t | On screen | Caption |
|---|---|---|
| f0 | the title line (P-09 recipe, lane 1) + presenter + tabs rising | the promise sentence |
| 0.4–1.2 | numerals 1…N | same |
| ≤ 2.5 | item 1: claim → strike → reality tile (P-15) = the proof | item 1's sentences |
| 2.5–3.0 | the title fades (6 f); row 1 settles in lane 1 | — |

For example: the title "5 offers that cheat you" → the tile "44%"; "5 'healthy' snacks that aren't" → "21 g sugar".

**HA-12 "Thesis typography"** (F-C default):

| t (s) | Beat | On screen | Caption | Motion | Cue |
|---|---|---|---|---|---|
| **f0** | "Episode number <n>:" | W-case world, the presenter clip live (L-cinema-top), the episode label "episode <n>" (`accent`) on, the prop resting on the lit table plane (y 700–900) | "Episode number <n>:" | the prop idles (1° sway, 60 f period) | — |
| 0.60 / 0.70 / 0.80 | Title | The title lines build (§5.2) | "<Thesis sentence>." from ≈ 0.95 | 3 f per line; grey → white by 1.0 s | — |
| 1.2–1.6 | Prop life | The prop's corner lifts and curls | same | rotateX 0 → 35°, 12 f | — |
| 1.6–2.6 | Chapter | The accent rule wipes in; the chapter line types ("<chapter name>"); the prop flips and tumbles out of frame | "This episode is called '<chapter>'." | type 1 character/f; tumble 30 f with 6 px motion blur | **reveal** (prop flip) |
| **≈ 3.2** | Payoff | T-6: the title card fades out (4 f), hard cut into still 1; the case tag fades in at y 140 | "<Date / place>." | 4 f + cut; tag 4 f | — |

For example: "money / doesn't / behave" + "that phone call"; in fitness, "the / perfect / diet" + "the 1,200-calorie summer".

### 6.4 Hook pairs by topic (claim → evidence)
| Topic | Claim (grey, struck or questioned) | Evidence (the number and where it comes from) | Card |
|---|---|---|---|
| Stacked discounts | "30% + 20% off = 50% off" | 44% (`stacked_discount` of 30 and 20; script) | P-14 → P-15 strike reveal |
| Flat vs reducing loan | "8% is cheaper than 11%" | 8% flat ₹2,00,000 vs 11% reducing ₹1,63,250 over 10 years on ₹2.5 L (`flat_rate_interest`, `reducing_balance_emi`) | P-19 → P-20 → P-24 race bars |
| Two incomes | "Two salaries = double safety" | one salary stops: ₹50 L → ₹0, commitments unchanged (script) | P-01/P-02 rows → P-07 zero-out |
| Small SIP | "₹5,000 a month is too small to matter" | the value after 20 years at the stated rate (`compound` with a contribution) | P-23 slider + P-24 bars (invested vs value) |
| Cashback | "10% cashback on ₹20,000 = ₹2,000" | capped at ₹500 → 2.5 % (`ratio`) | P-15 |
| "Healthy" granola | "A healthy breakfast" | sugar grams per serving (script, or the pack label the creator films) | P-15 with a creator shot (P-51) |
| Steps vs food | "10,000 steps lets me eat anything" | kcal burned vs kcal in one snack, on the same scale (script) | P-24 race bars |
| Protein bars | "A protein bar = a protein meal" | protein grams per 100 kcal, bar vs meal (`ratio`) | P-34 two-column ledger |

### 6.5 Writing the first sentence and the titles
F-A and F-B have no on-screen headline. What plays the headline's role is the **first caption sentence** plus the **post
title**:
- **The first sentence:** `<subject> <verb> <number>`, `These <N> <things> <hurt> you` or `Would you choose <A> or <B>?`.
  4–9 words, containing a number or a count; no adjectives like "shocking".
- **The post title** (in the creator's language; the original's Hinglish shape works well):
  `<NUMBER or KEY NOUN in caps> + <clause> + <1 key word in caps>!` ("5 Online OFFERS Jo Aapko CHEAT Kar Rahe Hain!");
  ≤ 9 words; exactly 2–3 words in caps.
- **The F-B panel title:** a question ending in "?" ("Which loan costs you more?"), ≤ 30 characters; later sections swap
  to "How did this happen?" and "Same trap in <second case>".
- **The F-C title:** 2–4 lowercase words that state a thesis ("money doesn't behave"), plus a 2–4 word chapter name.
- Banned: clickbait adjectives, emoji, "you won't believe", counts that don't match the list.

### 6.6 Hook sound
The hook carries one cue: the **reveal** of the first value (O-1, O-3), the **list cue** on the first lit numeral (O-2),
or the prop flip (HA-12). The bed enters after the hook (§11).

### 6.7 CTA, sponsor and end cards
| Device | Spoken pattern | On-screen element | Hold | Where |
|---|---|---|---|---|
| `end_card` (default) | "<Moral sentence>. Do you agree?", then silence or "Watch this next." | P-44: the black end card with the creator's next-video thumbnail (SH-3, else FB-3), a play chip, a 2-line title and a dashed curved arrow pointing down-right | 2.5–3.5 s | the last 2.5–3.5 s |
| `comment_keyword` | "Comment KEYWORD and I'll send you <deliverable>." | P-45: a white card in the board footer (or the panel bottom): "Comment" 32 px + **the reel's keyword** 72 px caps `ink` on `primary` | ≥ 1.5 s, to the end | the last sentence; then T-7 |
| `link_bio` | "The link is in my bio." / "Link given below." | P-46: a white chip "Link in bio" + 3 animated chevrons pointing down | ≥ 1.5 s | the end, or with the sponsor card |
| `post_only` | none | none (the reel ends on the moral + question) | — | — |

The end card is the default; the creator's copy may choose another device. The calm style needs no silence before the
CTA: the CTA sentence follows the moral directly.

- **The end card (P-44):** ≤ 3.5 s; the title readable ≥ 1.5 s; no black tail longer than 0.2 s. It's always the last
  thing.
- **The sponsor card (P-43):** in the F-A footer lane (y 1400–1500, after the summary line exits) or in F-B under the
  transfer cards (y 480–600); never over the presenter, the captions or a live value. On screen 4–6 s. **Disclosure:**
  spoken ("our sponsor <brand>") **and** "Paid partnership" (the 24 px legal class, inside the card, top-right) for the
  whole card (≥ 2 s). The creator's copy may change the wording. The logo is the creator's file (SH-4), else the real logo
  fetched from the sponsor's site, else the wordmark set in type (FB-4). Brand colours only on the logo.
- **One brand element at a time:** a sponsor card never shares the footer with a summary line (the summary line exits
  first, 5 f).

---

## §7 Structure and rhythm

### 7.1 Structure types (one per reel)
| ID | Format | Type | Arc | Source |
|---|---|---|---|---|
| **L-BUILD** | F-A | `ledger` | Parameters (rows of named quantities) → the build (what they cover: tiles, the total) → **the stress test** ("what if X stopped / doubled?": a zero-out or a change), landing past the middle → the moral (a summary line) → a question to the viewer + CTA | v01 |
| **L-LIST** | F-A | `ledger` (list) | The promise ("these N…", the rank skeleton, over in a breath) → items 1…N, each with the identical ritual (§7.3) → the payoff on the last item (the biggest reality tile) → CTA | v02 |
| **L-CALC** | F-B | `ledger` | The question (two options) → the parameters (chips) → stepping through the parameter (slider + race bars: the long middle) → the final verdict (the leader chip, final) → **why** (the mechanism: segment bars + explain lines) → **the transfer** ("same trap in <second case>", the two-card stack) → sponsor or CTA | v03 |
| **S-CASE** | F-C | `story` | The title card → the setting (date, place, stills) → the event chapters (stills cut on the story's nouns while the ledger changes state: the bulk of the reel) → the turn (the twist) → the open question (the next episode pays it off) | v04 |

### 7.2 Markers
| ID | Marker | Recipe | Used in |
|---|---|---|---|
| **SM-rank-list** | Rank numerals + chip tabs | N `ghost` numerals pre-drawn at f0–1.0 s; the active one turns `paper` on the ordinal word; S-tabs show "<NOUN> n" pills (future `ghost`, active and past `paper`) | L-LIST (the style's default marker) |
| **SM-panel-title** | Panel title swaps | The F-B question title changes per section ("Which loan costs you more?" → "How did this happen?" → "Same trap in insurance") | L-CALC |
| **SM-case-tag** | "case 01 / 07" + 7 dots | Persistent from the first still (S-case-tag); the episode's dot lit `accent` | S-CASE |
| none | spoken only | L-BUILD reels have no markers: the rows are the structure | L-BUILD |

Numbering is ascending (1 → N); the tabs never count down.

### 7.3 The rituals (identical for every item)
**L-LIST item ritual** (v02 @ 0:02.5–0:39):
1. **The ordinal word − 2 f:** the item's tab lights `paper` (E6 swap, 4 f) and its numeral turns `paper` (4 f). The list
   cue (the one sound that repeats).
2. **On the item's name** (≤ 0.3 s later): the title slides in from the left (x 136 → 176, 8 f), then the sub-label
   (+0.2 s, fade 6 f).
3. **On the claim value word:** the grey claimed value + "you think" appear (6 f).
4. **On the verdict word** ("only", "actually", "but", "No"): the white reality tile pops from a small `ghost` pill (scale
   0.25 → 1.08 → 1.0, 4 f) with its micro-label, and the strike snaps across the claimed value in 2 f on the same beat
   (v02 @ 13.54: the tile first, the strike 2 f later). The reveal cue.
5. **Hold ≥ 1.2 s** with the next caption, so the truth sinks in; then the next item.
6. **The last item escalates:** its reality tile grows to the 96 px variant (P-16) and a saved-note (P-17) sits under it.

Each item takes as long as the creator needs to tell it (6–8 s in the original); the ritual never changes, so the viewer
learns it on item 1 and starts predicting the strike.

**L-BUILD row ritual:** the label (fade 3–6 f) → the bar wipe (7 f) → the chip pop on the number word (pill → white value,
4 f, P-02) → an optional status tag on the role word (P-03).

**L-CALC step ritual** (per parameter step, ≈ 3–5 s): the slider handle moves to the step 8 f before the step word →
option A's bar grows and its value rolls to land on its spoken number → option B's bar and value land on theirs → the
leader chip hops if the leader changed (P-22).

**S-CASE beat ritual** (≈ 1.5–3 s): a hard cut to the still on the noun or place word (T-5) → the still holds static
(measured: no Ken Burns, drift ≤ 1 % on 28 stills) → the ledger changes state only on a spoken money word (P-40). On the
inciting event and on the turn, the cut becomes a T-9 white flash.

### 7.4 Open loops and the re-hook
- **Loops used:** "Let's see" (the L-CALC opening), "What if <X> stopped?" (the L-BUILD stress test), the unlit rank
  numerals (L-LIST), "But how did all this happen?" (the S-CASE ending, paid off in the next episode; the episode itself
  pays off every number it shows).
- **Payoff:** every loop opened inside the reel is paid on screen within the reel, except the S-CASE closing question,
  which names the next episode.
- **The re-hook:** a short reel needs none. A reel that runs past a minute gets one near the middle: the stress-test
  question line (P-10) in L-BUILD, the panel-title swap "How did this happen?" in L-CALC, the last tab still `ghost` in
  L-LIST.
- The hook is over fast, so the first number arrives while the promise is fresh; the F-C title card is done by ≈ 3.2 s.

### 7.5 Series furniture
- **When:** always in F-C; in F-A and F-B only when the creator runs a series.
- **The series tag (P-39):** "case {n} / {of}" (`series.tag_format`), 28 px, at S-case-tag, from the first still to the
  end; 7 dots (or `of` dots, up to 10): the current episode's dot lit `accent`, past ones `paper` 60 %, future ones `paper`
  30 %. With a series in F-A (L-BUILD) the tag sits right-aligned inside the board at y 664–700 (x 616–1016); in L-LIST it
  is dropped (the tabs already show progress); in F-B it sits right-aligned in the panel at y 136–172.
- **The episode label (P-37):** "episode {word}" in `accent`, the hook's f0 text beat (F-C).
- **The series card:** none separate; the F-C title card is the series card (0–3 s).
- **Episode counters, recaps, teaser chips:** none.
- The number comes from the reel header (`series {name, number, of}`).

### 7.6 Rhythm, by feel
- **Calm and even, never flat.** Something on the board changes when the words give it a reason: a row on its name, a
  chip on its number, a tile on its item, a strike on "actually". Between the reveals, smaller builds keep the eye busy;
  the reveal is the moment that gets the cue and the beat of air before it.
- **The board may hold.** In F-A the board can sit still for a long stretch while the creator talks the moral through
  (measured up to 7–12 s in v01 @ 30.5–43.2): the live face is the motion, and the board has said its piece. In F-B and
  F-C it moves on sooner: a slider steps, a still cuts.
- **The last is the biggest.** The last item, step or ledger state is the largest thing in the reel: a 96 px tile, the
  final verdict, the recovered sum.
- **The end is quiet:** a summary line, a question to the viewer, the end card.
- **Jump cuts** trim the take at sentence ends with the same framing, each carrying the caption swap and no transition;
  the frame should read as one take, and a clean single take is fine.
- No comedy beats, ever.

For reference, measured on the four reels (a description, not a target): roughly 28–35 visible changes a minute, caption
swaps every 1.5–3.5 s, jump cuts about 9 a minute in F-A (median shot 5–6 s) and about 16 in F-B (median 3.3 s), still
cuts about 34 a minute in F-C (28 stills, median 1.56 s, 0.56–2.96 s).

---

## §8 Visual system: B-roll and patterns

### 8.1 How the graphics behave
- **F-A and F-B:** the graphics are the argument. The board or the panel is on screen for the whole body.
- **F-C:** the stills carry the picture; the furniture (the case tag, the ledger counter) is always on; cards are rare.
- **Numbers become pictures:** every spoken quantity becomes a chip, a tile, a bar, a slider step or a counter;
  comparisons use one axis; mechanisms become segment bars or explain lines.
- **Variety comes from the moment, never from a quota;** the rituals (rows, items, steps, stills) are the deliberate
  repeats.

### 8.2 Families (B-…)
| ID | Family | Source | The creator supplies |
|---|---|---|---|
| **B-1** | Ledger rows (labels, bars, value chips, tiles, totals) | engine | — |
| **B-2** | Claim vs reality list (numerals, tabs, claims, strikes, reality tiles) | engine | — |
| **B-3** | Calculator panel (title, parameters, stat cards, slider, race bars, segments, explain lines) | engine (`VEOS.data`) | — |
| **B-4** | Status chips and tags | engine | — |
| **B-5** | Hero and gap counters | engine (`VEOS.data.counter`) | — |
| **B-6** | Case-file furniture (title stagger, episode label, case tag, ledger counter) | engine | the series name and number |
| **B-7** | Story stills | the creator's own (SH-2); else real photos fetched from the web (source noted, grayscale); substitute P-41 object plates | 15–25 monochrome stills per episode |
| **B-8** | Props | the creator's own (SH-5, optional); substitute: a drawn note card | an alpha PNG prop |
| **B-9** | Brand and CTA (sponsor card, end card, keyword card, link chip) | engine + the creator's assets | a sponsor logo (SH-4), the next-video thumbnail (SH-3) |
| **B-10** | Third-party moments (an advert, an app's offer screen, a post, a headline, a product) | the creator's files; else the real thing fetched from the web; else **created** with `renderer/inserts.js` (§12.4) | the files, if they own or hold them |

**One board per screen (B0).** In F-A and F-B everything inside the board or panel is drawn by **one bespoke scene per
section** (z3, `kind: "ledger"`, `text_class: "TC-label"`, `exception: "E3"`, bound to its figures with `figures`, `lands`
and `scale`, and every internal change declared in `events`). This keeps the screen at two text elements (the board and the
captions) and lets rows nest without overlap declarations. Use `VEOS.data.bars` / `slider` / `counter` directly only when
that helper is the **only** text on the board for its span; otherwise reproduce the helper's look inside the board scene
with `ctx.fig`, `ctx.figAt`, `ctx.fmtNum` and `VEOS.data.width`. Separate scenes only for: the sponsor card, the keyword
card, the end card, F-C stills, the case tag, the ledger counter and inserts.

### 8.3 Pattern specs (P-…)
Frames at 30 fps. Every value comes from `plan/figures.json` and is written by `ctx.fmtNum`. "Board" = the section's board
scene (B0).

**Ledger rows (B-1)**
| ID | Name | Type | On screen | Motion recipe | Use when | Text class | Needs |
|---|---|---|---|---|---|---|---|
| **P-01** | Label row | overlay | Caps label (32 px) + micro-label (28 px) + an empty white bar (h 56, radius 10) whose length is the value on the row's shared scale | label fade 3–6 f → bar width 0 → full, 7 f ease-out (a grey leading edge whitening as it grows), starting 0–3 f after the label | a named quantity is introduced ("Ruchi earns…", "Option A takes…") | TC-label | figure (bar length) |
| **P-02** | Value chip (ghost → fill) | figure | A grey `ghost` placeholder chip (w 240, h 96, radius 12) right of the bar, then white with the value (42 px) + unit line (28 px `muted`) | one 4 f pop on the number word: a small `ghost` pill (scale 0.25) grows to 1.08 and settles to 1.00, turning white as it grows, the value legible from f2 (v01 @ 0.40–0.52); a value that changes later rolls 10 f | every spoken value of a row | TC-display | figure; lands |
| **P-05** | Tile wrap | overlay | Small white tiles (w 284, h 64, radius 10, 22 px gaps; `ink` 32 px) flowing into a 3-column grid at x 64–960 (clear of the IG button column x > 970) under a micro header ("what my ₹50 L covers") | header fade 6 f; each tile: fade + rise 8 px, 6 f, on its spoken item word; ≥ 0.6 s between tiles | a list of things a quantity pays for, contains or causes | TC-label (redundant) | — |
| **P-06** | Total card | figure | A wider white card centred (w 420, h 120): the total 56 px + sub-line 28 px ("combined, every year") | rise 10 px + fade, 8 f; the total rolls 12 f to land on the spoken total | a sum or combined value is said | TC-display | figure (`sum`) |
| **P-07** | Zero-out | state | A row's value counts down to 0 (12 f); its bar becomes an empty **dashed `bad` outline** (2 px, dash 10/8); the chip's unit line changes to "was ₹50 L" (`muted`) | count-down 12 f landing on "stopped / zero / gone"; the bar fill fades out 6 f while the dashed outline draws 8 f | the stress test removes a quantity | TC-display | figure (step to 0) |
| **P-08** | Header swap | state | The micro header text changes in place ("what my ₹50 L covers" → "none of this gets halved") | E6 hard swap with a 4 f cross-fade inside a fixed rect | the meaning of a group changes | TC-label | E6 |
| **P-09** | Summary line | overlay | A bold centred takeaway (44 px `paper`) + a helper line (32 px, 80 %) in the footer lane | line: fade + rise 8 px, 8 f; helper +6 f; hold ≥ 2.0 s | the moral ("income drops instantly. / the commitments do not.") | TC-label | — |
| **P-10** | Stress-test question | overlay | The same footer line as a question ("what if one salary stopped?") | as P-09; replaced by the answer's summary line with a 6 f cross-fade (E6) | the "what if" turn of L-BUILD | TC-label | — |
| **P-52** | Conversion row | figure | A row "₹100 a day" → arrow → "₹36,500 a year" (two chips joined by a 3 px `paper` arrow that draws 6 f) | the left chip as P-02; the arrow 6 f; the right chip rolls 12 f landing on its word | a per-day or per-unit amount becomes a per-year or total amount | TC-display | figure (`per_period` / `unit_convert`) |

**Claim vs reality list (B-2)**
| ID | Name | Type | On screen | Motion recipe | Use when | Text class | Needs |
|---|---|---|---|---|---|---|---|
| **P-11** | Rank skeleton | overlay | N rank numerals (100 px) stacked at x 64, pitch 156 px, all `ghost` | fade 3 f each, 5 f stagger, no rise, all on by 1.0 s | the promise of a count ("these 5…") | TC-display | — |
| **P-12** | Chip tabs | state | N pills "<NOUN> n" (28 px caps) across S-tabs; future `ghost`, active and past `paper` | fade 2 f each, 3 f stagger at f0; each lights by an E6 swap (4 f) on its ordinal word | every L-LIST reel (with P-11) | TC-label | E6, slot S-tabs |
| **P-13** | Claim row | overlay | The active numeral turns `paper`; the title (50 px) slides in at x 176; the sub-label (32 px) under it | numeral colour 4 f; title slide 40 px + fade, 8 f; sub-label +6 f | the item's name and claim | TC-label | — |
| **P-14** | You-think value | overlay | The claimed value (40 px, `paper` 75 %) right-aligned to x 700 + micro "you think" (28 px) under it | fade + rise 6 px, 6 f, on the claim value word | the believed or advertised value | TC-label | figure (the claim as an input) |
| **P-15** | Strike reveal | figure | A 4 px `bad` strike line wipes across the claimed value; the white reality tile (x 720–960, h 120; value 56 px + micro "you actually get") pops beside it | the tile: a `ghost` pill pops to full size, scale 0.25 → 1.08 → 1.0 over 4 f, white with its value from f2, on the true-number word; the strike snaps L → R in 2 f on the same beat (v02 @ 7.40, 13.54) | the core move of the style: the truth replaces the claim | TC-display | figure (formula: stacked_discount, ratio, diff…) |
| **P-16** | Final tile grow | figure | The last item's reality tile at 96 px in a bigger card (w 330, h 150, x 630–960; the claimed value right-aligns to x 610) | as P-15 (the same 4 f pop; v02 @ 38.46–38.58), then P-17's strike 4 f later | the last item, to escalate | TC-display | figure |
| **P-17** | Saved-you-think note | overlay | Under the last row, right-aligned: micro "saved, you think" + the struck saving (40 px) | fade 6 f, then the strike 6 f on the verdict word | the item's apparent saving is exposed | TC-label | figure |
| **P-34** | Two-column ledger | figure | Two header chips ("you think" grey / "reality" white) over 2–4 paired rows: the grey value left, the white tile right | header 6 f; each pair: left fade 6 f, then the right tile pops 7 f on its word | 2–4 paired claims (food labels, ingredient lists, plan features) | TC-label / TC-display | figures |

**Calculator panel (B-3)**
| ID | Name | Type | On screen | Motion recipe | Use when | Text class | Needs |
|---|---|---|---|---|---|---|---|
| **P-18** | Panel title | state | A question title at x 64, y 128–188 (44 px, `display` 600) | first entry fade 6 f; each later swap: the old text fades 4 f, the new fades in 6 f in the same rect (E6) | every F-B section start | TC-label | slot S-panel-title, E6 |
| **P-19** | Stat card pair | figure | Two cards (w 456, h 300, radius 14) at y 220: A in `data`, B in `night`; the value 132 px `paper` + unit 28 px; ghost (30 % opacity) first | ghost fade 4 f; fill on the value word: opacity 0.3 → 1 over 4 f + figure pop 1.05 → 1 over 6 f | the opening "A or B?" | TC-display | figures |
| **P-20** | Cards → bars morph | stage (in-board) | The stat cards shrink and blur into the bar badges of P-24; the panel title swaps at the midpoint | 9 f: the cards shrink and slide to the badge rects with a 24 px horizontal motion blur mid-move (`ctx.blur(px, 0)`, the built-in directional blur); the title cross-fades over f5–f8; then the white tracks wipe in L → R (5 f) and the grey skeleton fills extend (5 f) (v03 @ 2.16–2.72) | right after P-19, on "let's see" | — | T-3 |
| **P-21** | Parameter chips | overlay | 2–4 chips (28 px, h 44, gap 12) under the title: "₹2.5 lakh loan", "10 years", "Monthly EMI" | each: fade + rise 6 px, 6 f, on its spoken word | the calculation's inputs | TC-label (redundant) | figure inputs |
| **P-22** | Leader chip flip | state | The `bad` "Costs more" (or `good` "Cheaper") chip straddling the top-right corner of the leading bar hops to the other bar | out: fade + drop 8 px, 4 f; in on the other row: rise 8 px + fade, 6 f, on the verdict word | the leader changes or the verdict is said | TC-label | figures (leader by max) |
| **P-23** | Parameter slider | state | A 6 px track (x 130–930, `paper` 45 %) with ticks at each step (40 px labels: 2, 4, 6, 8, 10) and a white handle (Ø 36, `primary`) | the handle moves to the next tick over 8 f, landing on the step word; a scale pulse 1.15 over the move | stepping a parameter (years, months, servings, km) | TC-label | figure steps (x); running state `param` |
| **P-24** | Race bars | figure | Two bar rows (h 100, gap 28): badge (`data` / `night`, 44 px label) + track + fill + value (48 px, right-aligned) on one shared scale | each fill grows over 10 f into the step's `at`; the value rolls 10 f; never re-scaled mid-reel | comparing two options over a parameter | TC-label / TC-display | figures with one `scale_id` |
| **P-25** | Segment bars | figure | Each bar redrawn as N equal segments: flat = N identical blocks; reducing = blocks shrinking step by step (each block's height ∝ that period's value) | the solid fill dissolves into segments L → R, 2 f per segment | explaining why (flat vs reducing, fixed vs declining, linear vs compounding) | — (inside P-24) | figure steps per period |
| **P-26** | Explain lines | overlay | Two lines under the bars (40 px): "<Method A>: <how>", "<Method B>: <how>" | each: fade + rise 6 px, 6 f, on the method word | the mechanism in words | TC-label | — |
| **P-27** | Method tags | overlay | Small tags hanging under each bar badge: "Flat rate" `bad`, "Reducing" `good` | drop 8 px + fade, 6 f, on the method word | naming the method of each option | TC-label (redundant) | — |
| **P-28** | Action chip | overlay | A white chip with the action ("Check the APR statement"), right-aligned under the bars | fade + rise 6 px, 6 f | what the viewer should do | TC-label | — |
| **P-29** | Panel replace | stage (in-board) | The whole panel content blurs out (6 f), the new section's skeleton (empty white cards) rises in (8 f) | T-4 | a transfer to a second case ("Same trap in insurance") | — | T-4 |
| **P-30** | Two-card stack | figure | Two full-width white cards (h 72, at y 220–292 and 312–384) titled "<Thing>" + micro "<what it means>" ("Premium / What you pay", "Cover / What you get"); the empty skeleton first | skeleton rise 8 f; each title fades in on its word (6 f) | the second case's two quantities to compare | TC-label | — |
| **P-31** | Check chip | overlay | A white pill (h 44, y 408–452) with a `good` ✓ and the rule ("Look at both, not just one") | fade + scale 0.94 → 1, 6 f | the rule of the transfer | TC-label | — |

**Status tags (B-4)**
| ID | Name | Type | On screen | Motion recipe | Use when | Text class |
|---|---|---|---|---|---|---|
| **P-03** | Outline status tag | overlay | A caps tag (28 px, 2 px `paper` outline, radius 8, h 36) under a row ("RUNS THE HOUSE", "INVESTED") | rise 6 px + fade, 6 f, on the role word | naming a quantity's role | TC-label (redundant) |
| **P-04** | Colour status tag | overlay | A filled tag (`good` "Cheaper?" / `bad` "Costs more", sentence case 28 px) pinned to a card's top edge | drop 12 px + fade, 6 f | an early verdict or a question mark on an option | TC-label (redundant) |

**Hero and gap counters (B-5)**
| ID | Name | Type | On screen | Motion recipe | Use when | Text class | Needs |
|---|---|---|---|---|---|---|---|
| **P-32** | Hero counter | figure | One number (120 px `paper`, centred in the board's free lane) + a label (40 px) | `VEOS.data.counter`: roll 18 f landing on the spoken number; pop 6 f | a single number is the point and nothing else is on the board | TC-display | figure |
| **P-33** | Gap counter | figure | The difference between two figures ("₹36,750 more") in a white card under the bars | roll 12 f; `diff` formula | the difference itself is said | TC-display | figure (`diff`) |

**Case-file furniture (B-6) and stills (B-7, B-8)**
| ID | Name | Type | On screen | Motion recipe | Use when | Text class | Needs |
|---|---|---|---|---|---|---|---|
| **P-35** | Title stagger | overlay | The §5.2 title card | §5.2 | the F-C hook | TC-display | headline |
| **P-36** | Prop float | overlay | The prop (SH-5 PNG, or the drawn note card FB-5) resting on a lit table plane, y 700–900, with a soft contact shadow | idle sway 1°/60 f → corner curl rotateX 0 → 35° (12 f) → flip and tumble out of frame (30 f, 6 px motion blur), ending by 2.8 s | the F-C hook | — | asset or FB-5 |
| **P-37** | Episode label + chapter line | overlay | "episode <word>" (28 px `accent`) at y 128; the chapter line (56 px) with a 160 × 4 px accent rule at y 588 | the label on at f0; the rule wipes 6 f at 1.6 s; the chapter types 1 character/f | the F-C hook | TC-label / TC-display | series |
| **P-38** | Cinema still | footage-treatment | A story still (the creator's, else a real photo fetched; monochrome, one accent object) filling y 0–940, held static (no Ken Burns), a top scrim (`#000` 0 → 55 % over y 300 → 0) for the furniture, a mask fade into W-case over y 760–940 | a hard cut on the noun or place word (T-5); hold 0.6–3.0 s, median 1.6 s (v04); every cut brings a new subject, because a cut is the story moving | every S-CASE beat | — | asset (SH-2), `fx.clip` |
| **P-39** | Case tag | state | "case 01 / 07" (28 px) + 7 dots in S-case-tag | fades in at the first still (8 f); then fixed for the reel | every F-C reel | TC-label | series, slot |
| **P-40** | Ledger counter | state | In S-ledger, right-aligned: "ledger" (24 px legal class), the value (56 px `accent`), the state word (28 px: needed / handed over / spent / recovered) | rises in on the first money word (8 f); each change: the state word hard-swaps (E6) at the roll start and the value counts linearly over 27–45 f (₹60,00,000 → ₹0 in ≈ 1.1 s, v04 @ 20.16), ending on the spoken amount; the `accent` glow 28 px stays on while counting and fades over 12 f | every money change in a story | TC-display | figure (steps with `label`), running state `ledger`, E6 |
| **P-41** | Object plate (FB-2) | overlay | A Claude-built plate filling y 0–940: a dark vignette on W-case, one line object drawn with `fx.icon` (e.g. `phone`, `doc`, `clock`, `car`, `key`) at 360 px in `paper` 70 %, its key part in `accent` with a 40 px glow | held static; a hard cut like P-38 | a missing still (FB-2) | — | `fx.icon` |
| **P-42** | Closing question hold | overlay | The last state of the ledger + the final caption ("But how did all this happen?"); the still holds 2–3 s | none (a hold); the ledger's glow pulses once (12 f) | the S-CASE ending | — | — |

**Brand and CTA (B-9)**
| ID | Name | Type | On screen | Motion recipe | Use when | Text class | Needs |
|---|---|---|---|---|---|---|---|
| **P-43** | Sponsor card | overlay | A dark rounded card (`#14201F` at 96 %, radius 14; x 64–960 and h 100 in the F-A footer lane y 1400–1500, the full panel width and h 120 under the F-B transfer cards, y 480–600): the logo (SH-4, else fetched from the sponsor's site) or the wordmark set in type (44 px) at left, a 2 px divider, "Talk to <brand>" (44 px) + "Link given below" (32 px), 3 chevrons (32 px) at right; "Paid partnership" (the 24 px legal class) top-right inside the card | rise 16 px + fade, 10 f (T-8); the chevrons fade in one by one (4 f stagger) then pulse in sequence every 24 f | a sponsored reel | TC-label | asset or FB-4, disclosure |
| **P-44** | End card (thumbnail + arrow) | overlay | W-endcard black; the creator's thumbnail (16:9, x 126–954, y 560–1026, radius 16, 2 px `paper` 30 % border); a play chip (88 × 62, `paper` fill, `ink` triangle) at x 126, y 1060; the next title in 2 lines (44 px, x 236–954); a dashed curved arrow (8 px `primary`, dash 18/14) from (880, 1200) to (760, 1440) with a 36 px head | a hard cut in; the thumbnail + title block slams from scale 2.6 → 1.0 with an 18 px motion blur over 3 f (`ctx.blur(px, 90)`, the built-in directional blur); the dashed arrow draws over 11 f from f1, then its head bobs 6 px every 30 f (v01 @ 45.00–45.40) | the `end_card` CTA | TC-label | SH-3 or FB-3 |
| **P-45** | Keyword card | overlay | A `primary` card (x 64–960: w 896, h 100, radius 14; never into the IG button column x > 970) in the footer lane y 1400–1500 (F-A) or y 620–720 (F-B), one line: "Comment" (32 px `ink`) + the keyword (72 px caps 800 `ink`). In an L-LIST reel with 5+ rows the board exits first (T-4) and the card sits at y 1000–1100 | rise 12 px + fade, 8 f; one pulse 1.0 → 1.04 → 1.0 on the spoken keyword | the `comment_keyword` CTA (`kind: "cta-keyword"`) | TC-display | the reel's keyword |
| **P-46** | Link chip | overlay | A white pill "Link in bio" (32 px) + 3 chevrons pointing down | fade 6 f; chevrons as P-43 | the `link_bio` CTA | TC-label | — |

**Third-party moments (B-10; §12.4)**
| ID | Name | Type | On screen | Motion recipe | Use when | Needs |
|---|---|---|---|---|---|---|
| **P-47** | Quote row | overlay | `fx.quoteCard` (theme `light`, w 952) inside the board's lanes 1–2: the post or claim read aloud, word for word | built-in rise + de-blur 10 f | someone's post, ad copy or quote is read aloud and the real one can't be found | the exact words |
| **P-48** | Headline row | overlay | `fx.headlineCard` (light) with the exact headline and a `bad` highlight on the spoken phrase | built-in; the highlight wipes 0.5 s per span | a news headline is cited and the real page can't be found | the exact headline |
| **P-49** | App row | overlay | `fx.appUI` (`kind: list`) as a generic checkout or offer screen: the advertised offer as list rows | built-in; rows on their words | an app's offer, plan or price screen is described and no real screen turns up | the offer as said |
| **P-50** | Name plate | overlay | `fx.logoPlate`: the brand or product name set in type with a monogram | built-in; pulses on the name | a brand or product is named and its real logo can't be found | the name |
| **P-51** | Real shot | overlay | `fx.shot`: the real thing in the board with a highlight box on the figure: the creator's own screenshot or photo (a pack label, a statement, a receipt), else the real logo, post, headline or offer page fetched from the web | built-in; the highlight on the number word | the real thing exists (the creator's file, or fetched with its source noted) | asset (origin creator or fetched) |

52 patterns, P-01…P-52: P-01–P-17, P-34 and P-52 live in F-A; P-18–P-33 in F-B; P-35–P-42 in F-C; P-43–P-51 in all three.
A moment none of them covers gets a new device built from these families, in this style's language: white rounded cards,
Poppins figures, the claim-vs-reality axis, a pop on the word.

### 8.4 Line → pattern lookup
Vocabulary, not a decision table: it tells you what this style reaches for. Ask what the moment needs, then use it.

| Line type | For example | Primary | Alternates |
|---|---|---|---|
| A named quantity | "Ruchi earns ₹75 lakhs" | P-01 + P-02 | P-32 if nothing else is on the board |
| A second quantity to compare | "I earn ₹50 lakhs" | P-01 + P-02 (same scale) | P-24 |
| The role of a quantity | "the house runs on my salary" | P-03 | P-04 |
| Things a quantity covers | "school fees, food, electricity…" | P-05 (one tile per spoken item) | P-30 |
| A total | "₹1.25 crore combined" | P-06 | P-33 |
| "What if X stopped / doubled?" | "what if one salary stopped?" | P-10 → P-07 | P-08 |
| The moral | "both incomes are load-bearing now" | P-09 | — |
| A promise of N items | "these 5 offers cheat us" | P-11 + P-12 | HA-02 title |
| An item's name and claim | "granola: 'no added sugar'" | P-13 | P-47 / P-49 when it's someone's ad |
| What you think | "we feel we're getting 50%" | P-14 | P-34 |
| What is true | "it's only 44%" | P-15 | P-16 on the last item |
| An apparent saving that isn't | "you think you saved ₹500" | P-17 | P-15 |
| A per-unit amount becoming a total | "₹100 a day is ₹36,500 a year" | P-52 | P-32 |
| "Would you choose A or B?" | "an 8% loan or an 11% loan?" | P-19 → P-20 | P-24 directly |
| The inputs | "₹2.5 lakh loan, 10 years" | P-21 | — |
| "After N years / weeks…" | "after 2 years the interest is…" | P-23 + P-24 | P-32 for one option |
| Who's ahead now | "the 8% loan is charging more" | P-22 | P-04 |
| How it happened (mechanism) | "flat on the full amount, reducing on what's left" | P-25 + P-26 + P-27 | P-30 |
| What to do | "read the label per 100 g" | P-28 | P-31 |
| "The same trap in…" | "same trap in insurance" | P-29 → P-30 → P-31 | — |
| The difference | "₹36,750 more" | P-33 | P-15 |
| Story: a date / place / object / person | "24 May 1971", "a phone call" | P-38 (the creator's still, else a real photo fetched) | P-41 |
| Story: money changes hands | "₹60 lakhs were withdrawn" | P-40 | P-32 (F-A) |
| Story: the open question | "but how did all this happen?" | P-42 | — |
| A sponsor | "talk to our sponsor X" | P-43 | — |
| CTA | "comment X" / "link in bio" / "watch this next" | P-45 / P-46 / P-44 | — |
| Someone else's post, ad, app or headline | "the app says 50% off" | P-51 (the real thing: the creator's screenshot or fetched) | P-49, P-47, P-48, P-50 (rebuilt from the exact words) |

### 8.5 The data contract
Every chip, tile, bar, slider tick, counter, total and ledger value is a **figure** in `plan/figures.json`. This is the
style's spine: the viewer trusts the board because every number on it would survive a calculator.

1. **Provenance:** every input is `from: script` (with `said`: the exact words), `creator` (stated by them), `spoken@<t>`, or
   set in the creator's copy. Literal claims inside `args` are errors.
2. **Formula first:** if the script derives a number (a total, a discount, an interest, a difference, a per-year amount),
   the figure uses the formula and the stated value is checked against it. Allowed formulas: `sum`, `diff`, `ratio`,
   `percent_change`, `stacked_discount`, `simple_interest`, `flat_rate_interest`, `reducing_balance_emi`, `compound`,
   `cagr`, `per_period`, `unit_convert`.
3. **Rounding:** when the creator rounds (₹1,31,190 for 1,31,193.6), set `round_to` (10) so the tolerance is ±5.
4. **Same axes:** compared bars, race bars and the rows of one comparison share one `scale_id`; the scale's max is the
   largest value shown in that comparison for the whole reel (bars never re-scale).
5. **Landing:** counters and value chips land within ±5 f of the spoken number word (`lands`); slider steps land on their
   step word.
6. **Format:** chips and tiles of round lakh/crore values use `{"style": "short"}`; computed amounts use
   `{"style": "full"}`; non-money values use `{"currency": "", "suffix": " g"}` (or " kcal", " h"); percentages use
   `"percent"`.
7. **Illustrative:** an assumed rate or a hypothetical ("say 12% a year") is `illustrative: true` in figures.json. It
   carries no label on screen: it's an illustration, and the creator says it as one. It never stands in for the creator's
   own result.
8. **Every number on screen** is in figures.json or spoken; integers ≤ 12 used as labels (rank numerals, tab numbers,
   slider ticks taken from figure steps) are exempt.

`veos figures` recomputes every figure, checks provenance, the landings (±5 f), the shared scales and the number format
(the ₹ glyph, Indian grouping, lakh/crore compacts, no K/M/B on rupees, every figure written exactly as `fmt_num` writes
it). Run it on every reel: it's the calculator, and a wrong number is the one thing to fix.

**Worked figures (the calculator from the source, F-B):**
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
The panel scene binds `figures: ["flat", "red"]`, `scale: {id: "S-int", max: 200000}`, and `lands` at every step's `at`.
Values on screen: `ctx.fmtNum(v, "flat")` → `₹1,20,000`; the leader chip sits on whichever `ctx.figAt(...).value` is larger.

**Other figure shapes this style uses:**
| Pattern | Figure |
|---|---|
| P-15 discount reality | `{"id": "offer1", "kind": "hero_number", "formula": "stacked_discount", "args": {"discounts_pct": ["d1", "d2"]}, "value": 44, "format": "percent"}` with inputs `d1` 30, `d2` 20 (`from: script`); the claimed "50%" is its own input `claim1` (`from: script`, said "50% off") |
| P-06 total | `{"id": "total", "kind": "hero_number", "formula": "sum", "args": {"values": ["inc_a", "inc_b"]}, "value": 12500000, "format": {"style": "short"}}` → `₹1.25 Cr` |
| P-07 zero-out | a `none` figure with two steps: `{args: {value: "inc_b"}}` then `{args: {value: "zero"}, at: <"stopped">}` where `zero` = `{"value": 0, "from": "script", "said": "stopped"}` |
| P-40 ledger | `{"id": "ledger", "kind": "ledger", "formula": "none", "steps": [{"args": {"value": "needed"}, "label": "needed", "at": 11.2}, {"args": {"value": "handed"}, "label": "handed over", "at": 20.3}, {"args": {"value": "spent"}, "label": "spent", "at": 29.1}, {"args": {"value": "fig:recovered"}, "label": "recovered", "at": 46.2}]}` + `{"id": "recovered", "kind": "counter", "formula": "diff", "args": {"a": "needed", "b": "spent"}}` |
| P-52 conversion | `per_period` / `unit_convert` (`₹100 a day` × 365 → `₹36,500` via `{"formula": "unit_convert", "args": {"value": "daily", "rate": "days"}}`) |

### 8.6 Running state: the ledger and the slider
| Var | Type | Start | Format | Display | Ops |
|---|---|---|---|---|---|
| `ledger` (F-C) | `ledger` with labelled states (needed → handed over → spent → recovered; or ordered → received → unpaid) | the first money word | the reel's number format, style `full` | P-40 in S-ledger | `set {value, state}` on each spoken money word; the values are figure steps with `label` |
| `param` (F-B) | `progress` over the slider's ticks | the first step | integers, or the parameter's unit suffix | P-23 | `tick_to <x>` 8 f before the step word |

One persistent position; the value changes only on an op; it never contradicts the spoken or shown value; it persists
across still cuts. `recovered` = `needed − spent` when the script says so (a `diff` figure proves it).

**How to build it today:** the ledger is built as a **figure**: one `none`-formula figure whose steps carry
`args: {value: <input>}` and `label: <state word>`, read in a bespoke scene with `ctx.figAt` and `ctx.fig(id).steps[i].label`
(the counter helper has no per-step labels). `veos figures` then checks every landing.

Nothing in this style follows a face or an object: every graphic sits on the board grid or in a slot.

### 8.7 Comedy layer
Off. The style is defined by its absence: no stickers, stamps or meme sounds. The only mark is the strike line, and it's
part of P-15.

### 8.8 Assets
- Real captures first: the creator's own statements, pack labels, receipts and app screens go in P-51, with personal
  identifiers (account numbers, names, addresses) blurred for their whole time on screen.
- Then the real thing from the web for what the reel names: the brand's logo, the app's offer page, the post, the
  headline, captured and framed in P-51, source noted.
- Mocks: only generic, unbranded recreated UIs (P-49), when no real screen turns up.
- No stock images, no stock icons as content; a brand set in type (P-50) only when its real logo can't be found.
- Third-party moments: fetch the real thing (§12.4).

---

## §9 Transition system

### 9.1 Library
| ID | Transition | Frames | Recipe | Cue role |
|---|---|---|---|---|
| **T-1** | In-place build | 4–10 | An element enters on its word inside the existing board; nothing else moves | reveal (only on value landings) |
| **T-2** | Pill pop | 4 | A small grey pill grows (0.25 → 1.08 → 1.0) into the white value card, its value legible from f2 | reveal |
| **T-3** | Cards → bars morph | 9 | The stat cards shrink and slide to their bar-badge rects with a 24 px horizontal motion blur mid-move; the panel title cross-fades over f5–f8. Build: inside the board scene, each moving card takes `filter:${ctx.blur(px, 0)}` (directional, 0° = horizontal), px = 24 × sin(π · p) over the 9 f (peak mid-move, 0 at both ends); never a uniform CSS `blur()` | silent |
| **T-4** | Panel replace | 6 + 8 | The panel (or board) content blurs 0 → 10 px and fades out over 6 f; the next section's skeleton rises 16 px and fades in over 8 f | silent |
| **T-5** | Still cut | 0 | A hard cut between stills (F-C), on the noun or place word ±1 f; the presenter clip and the furniture don't change | silent (a ledger landing may carry a reveal instead) |
| **T-6** | Title fade + cut | 4 + 0 | The F-C title card fades out over 4 f, then a hard cut into still 1 | silent |
| **T-7** | Cut + slam to end card | 0 + 3 | `stage via: cut` to W-endcard; the P-44 block slams from scale 2.6 → 1.0 with an 18 px motion blur over 3 f. Build: the P-44 scene with `in: "none"` scales itself 2.6 → 1.0 (ease out) over f0–f2 under `filter:${ctx.blur(px, 90)}` (directional along the slam, px 18 → 9 → 0), sharp from f3 | CTA (whoosh) |
| **T-8** | Sponsor rise | 10 | The sponsor card rises 16 px and fades in under the existing content | CTA |
| **T-9** | White flash (F-C) | 1–2 | A full-frame white fill over the picture (presenter, stills and board included; captions stay sharp on top) at 85 % on the cut frame, 40 % on the next, then gone; the new still is already under it (v04 @ 7.04 = 1 f, 26.16–26.20 = 2 f). Build: core's built-in transition, no scene: `timeline.transitions` `{"t": <cut>, "type": "flash", "frames": 2, "pre": 0, "peak": 0.85, "decay": 1.1, "colour": "#FFFFFF"}` (frame 2 lands at 0.85 × 0.5^1.1 ≈ 40 %); `"frames": 1` for the single-frame version | transition (soft hit) |

"Hard cuts only" applies to the take: it's trimmed with same-framing jump cuts at sentence ends (§7.6), each carrying the
caption swap and no transition. Never a punch-in or a reframe to hide a cut.

### 9.2 Grammar
| Boundary | Use | Never |
|---|---|---|
| f0 | T-1 (the first board element enters on f0) | a fade from black, a title card in F-A/F-B |
| Hook → body | keep building (no transition) | a stage change, a world change |
| New item (L-LIST) | tab + numeral light-up, then T-1 | a board clear |
| New row (L-BUILD) | T-1 in the next lane | moving existing rows |
| Opening cards → working view (F-B) | T-3 | a hard cut |
| New section (F-B "why", "transfer") | T-4 | T-3 |
| A value lands | T-2 | a flash, a shake |
| Story beat (F-C) | T-5 | dissolves between stills |
| The inciting event, the turn (F-C) | T-9 | a flash in F-A / F-B, or on an ordinary beat |
| Sponsor | T-8 | covering the data |
| Last word → end card | T-7 | a black tail > 0.2 s |

### 9.3 How the moves breathe
- T-1 and T-2 are the rhythm itself: the board builds in place, on the words, all the way through.
- The morph (T-3) happens once, where F-B's opening question turns into the working view; it's the one moment the panel
  changes shape.
- A panel replace (T-4) is a new chapter (the "why", the transfer), so it only comes at a section start.
- The white flash (T-9) belongs to the story's two hinges, the inciting event and the turn. Spent anywhere else it stops
  meaning "everything just changed".
- The end-card slam (T-7) is the last thing in the reel, once.

---

## §10 Motion tokens, camera and zoom, layers, finishing

### 10.1 Motion tokens (30 fps)
| Token | Value |
|---|---|
| Lead | 2 f before the trigger word |
| Entry ease | `cubic-bezier(0.22, 1, 0.36, 1)` (expo-out) |
| Exit ease | `cubic-bezier(0.64, 0, 0.78, 0)`, 5 f |
| Row / label enter | 6–8 f, rise 6 px + fade |
| Chip / tile pop | 4 f, from a `ghost` pill at scale 0.25 → 1.08 → 1.00, white from f2 (no separate ghost hold) |
| Number roll | 10 f (rows, bars), 12 f (totals), 18 f (the hero counter), 27–45 f linear (the F-C ledger); tabular figures; a 6 px vertical motion blur on the rolling digits only |
| Strike | 2 f, L → R, 4 px `bad`, on the tile's beat |
| Bar wipe / grow | 7 f (wipe), 10 f (race-bar grow), ease-out |
| Tabs / numerals stagger | 3 f / 5 f, fade only |
| Tile stagger | ≥ 0.6 s between spoken items (each tile on its own word); 4 f when a group is spoken as one phrase |
| Morph (T-3) | 9 f, 24 px horizontal motion blur (`ctx.blur(24, 0)` peak) |
| Slider step | 8 f into the step word |
| Counter glow | 12 f fade |
| Title line (F-C) | 3 f, 3 f stagger, grey → white 10 f; exit fade 4 f |
| End-card slam (T-7) | 3 f, scale 2.6 → 1.0, 18 px directional blur (`ctx.blur(18, 90)` → 0); arrow draw 11 f |
| Flash (T-9) | 1–2 f, 85 % → 40 % white (built-in `flash`, pre 0, decay 1.1) |
| Stills | static (no Ken Burns) |
| Hold | text ≥ 0.25 s per word; titles ≥ 10 f after building; summary lines ≥ 2.0 s |

### 10.2 Footage camera
`zoom_policy: none`. Measured at 25 fps with ORB on the presenter: per-frame scale change p99 < 0.1 % and rotation p99
< 0.04° (v01, v02), cumulative drift ≤ 2 % over 45 s, and the background stays put across every v03 jump cut. There are no
Z-moves in this style: no punch-ins, crash zooms, push-drifts, shakes or rotations on the presenter, in any format. The only
motion in the presenter window is the take itself.

The board doesn't move either: it's a fixed UI, not a canvas, so there's no canvas camera.

### 10.3 Layer order (back to front)
1. The world (W-ledger / W-case / W-endcard), its glow and noise
2. (z2) none in this style
3. The board or panel scene (z3); the F-C still band (z3)
4. The presenter window (stage) with its border
5. The sponsor card, the keyword card, inserts (z5)
6. The chrome slots: S-tabs (inside the board), S-panel-title, S-case-tag, S-ledger (z6)
7. Captions (CS-1)

Nothing else: no big captions, comedy, banners or light passes. The F-C still band sits under the presenter window and
never overlaps it (the band ends at y 940, the window starts at y 960).

### 10.4 Finishing
Film noise 0.04 (F-A, F-B) / 0.05 (F-C) on the world only; vignette 0.12 / 0.2; a soft glow drifting ±24/18 px on the teal
and maroon worlds. Card shadows: `0 10px 30px rgba(0,0,0,.18)`. No grain on the footage, no bloom, no flares.

---

## §11 Sound

Sound is minimal and it never decorates: a cue marks a number landing that matters. If in doubt, leave it out. Cues come
from the bundled SFX pack (catalogue ids only), each on a visible event.

| Line | Decision |
|---|---|
| **Cue moments** | `reveals` (a value landing in P-02, P-06, P-15, P-16, the P-24 verdicts, the P-40 changes; sparse, so each one means "this is the number"), `list_cue` (each L-LIST item's light-up, the one sound that repeats), `cta` (the end card, the keyword card, the sponsor card). Still cuts and row builds are silent; T-9 may carry a soft hit and the T-7 slam a whoosh (both from the `transition` category) |
| **Meme cues** | off |
| **Music bed** | on, a calm low bed; it enters after the hook (on the first beat after 3 s); F-C may start it from f0 under the title card |
| **Ducking** | the bed sits ≥ 18 dB under the voice while the voice speaks |
| **Loudness** | −14 LUFS integrated, true peak ≤ −1.5 dBTP; a hard end ≤ 6 f after the end card's last frame |

---

## §12 Footage handling

### 12.1 Setups
| Setup | Spec |
|---|---|
| **A: Seated teacher** (every format) | Camera at eye height, front-on, medium close-up (head and shoulders to mid-chest); landscape 16:9, 4K 25/30 fps preferred (1080p works for F-A and F-C); a soft key from camera-left, gentle fill; a styled background at 1.5–3 m (a bookshelf, a plant and one personal object), slightly defocused; a plain dark crew-neck tee (no logos, no stripes); glasses fine; no visible mic; eye-line into the lens; one continuous take, read calmly |

Framing on output: the F-A / F-C 16:9 window shows the full frame (the head top at 18–30 % of the window, the eyes at
≈ 40 %). F-B crops 9:16 out of the take (the eyes at y ≈ 1015).

### 12.2 Shots and fallbacks
| ID | Shot | Spec | How many | Must / optional | Formats |
|---|---|---|---|---|---|
| SH-1 | The take | Setup A, one take or word-boundary jump cuts | 1 | must | all |
| SH-2 | Story stills | Monochrome photos or images the creator owns or made (else real photos of the place, person or object fetched from the web, source noted, set to grayscale); 4:5 or 9:16, ≥ 1080 px wide; one accent-coloured object per still if possible; one per story beat | 15–25 for an episode | must (F-C) | F-C |
| SH-3 | Next-video thumbnail | The creator's own 16:9 thumbnail, ≥ 1280 px wide | 0–1 | optional | all |
| SH-4 | Sponsor logo | The creator's file, else fetched from the sponsor's site; SVG or PNG with alpha | 0–1 | optional (sponsored reels) | F-A, F-B |
| SH-5 | Title prop | A cut-out PNG with alpha (a note, a key, a letter), ≥ 800 px | 0–1 | optional | F-C |
| SH-6 | Vertical or 4K take | A 1080×1920 vertical take or a 2160p landscape take for the F-B face cell | 1 | optional | F-B |

| ID | For | What happens instead | What it costs | Result |
|---|---|---|---|---|
| FB-1 | SH-1 | none | the style needs the presenter | `no_fallback` |
| FB-2 | SH-2, nowhere to be found | P-41 object plates: a Claude-built monochrome plate per beat (an `fx.icon` line object on W-case with one accent glow), held static | no photographic atmosphere; it reads as a motion-graphic case file | `degraded` |
| FB-3 | SH-3 | A created end card: the next video's title set in type on the theme gradient with a neutral play glyph | no thumbnail face | `holds` |
| FB-4 | SH-4, nowhere to be found | The sponsor wordmark set in type (44 px, `paper`) inside P-43 | no brand logo | `holds` |
| FB-5 | SH-5 | A drawn prop: a rounded note card (`accent` at 70 % with a darker border and a printed-pattern stripe) that curls and falls in CSS 3D | less photoreal | `holds` |
| FB-6 | SH-6 | Crop the 1080p landscape take at ≤ 1.35× and set the face cell's eye line at 0.26 | a softer, tighter face | `degraded` |

Tell the creator which fallbacks were used.

### 12.3 Props, the reaction bank, the cut-out, resolution
- Props: one hero prop per F-C episode (SH-5 or FB-5).
- Reaction bank: none (no cutaways in this style).
- The cut-out: not needed. The presenter is always a framed window, and nothing is drawn inside it.
- Minimum source resolution: F-A and F-C need no crop beyond 1.0×; F-B needs a 2160p landscape or a vertical 1080×1920
  source (a 1080p landscape take allows ≤ 1.35×, FB-6).

### 12.4 Third-party moments: fetch the real thing
When the creator names a real offer, product, headline, post, brand or person, the viewer should see the real one. Per
reel:
1. **List the moments** in the transcript that call for third-party material. In this style they are: an advertised offer
   or price screen, a product's pack label, a news headline, a post or quote, a brand or product name, a person in a story.
2. **The creator's own files first:** screenshots, photos and clips in their folder.
3. **Otherwise search the web and fetch it:** the brand's real logo, the offer or product page (captured and framed on the
   part that matters), the real headline or post, a public photo of the person. Note where it came from.
4. **Use it as it is:** P-51 `fx.shot` in the board (or P-38 in F-C), cropped and highlighted, never altered to say
   something it doesn't; a headline or post word for word; personal identifiers blurred.
5. **Nothing usable to be found:** rebuild it from its exact words with the created-substitute toolkit: an advert or app
   offer → P-49 `fx.appUI` (`kind: list`); a quote or post → P-47 `fx.quoteCard`; a headline → P-48 `fx.headlineCard`; a
   brand → P-50 `fx.logoPlate`; a person → `fx.silhouette` (F-C); a story object → P-41.

A created card quotes only what the script states, word for word; it needs no label and no credit line.

### 12.5 Frame rate and audio
30 fps CFR output (a 25 fps source is conformed); 1080×1920, BT.709. Voice chain: high-pass 80 Hz, de-ess, light
compression, −14 LUFS.

---

## §13 What your plan should settle

Your `ideas.md` is a page or two, for you. In this style it has decided, before any code:
1. **The format, the theme and the structure,** and why (§3.1, §4.3, §7.1).
2. **The numbers:** `plan/figures.json` with provenance or a formula for every number on screen, `veos figures` run and
   every mismatch settled (shown vs recomputed for every one), and the `figure_id` on every beat that shows a number. Illustrations marked
   `illustrative: true`.
3. **The hook:** the archetype and opening, the first sentence with its number, every hook beat to the frame, the frame
   the first number lands (≤ 1.0 s; the F-C title by 3.0 s), the post title with its two alternates (and the F-C title and
   chapter).
4. **The tone and the trigger word of every line,** and so which beats are grey claims, white truths, red tags, green tags.
5. **The board per section:** one board scene per section (B0) with its `figures`, `lands`, `scale` and `events`; for
   every line, the lane it lands in and what it creates, changes or replaces; where the board holds; the escalated last
   item. `exception: "E3"` on board scenes, `"E6"` on the swaps.
6. **The state and the furniture:** the F-B parameter steps and the F-C ledger states (`state_ops [{var, op, value, at}]`),
   every `slot_content` change, `series {name, number, of}` for F-C.
7. **The moves in exact numbers:** the jump cuts (on sentence ends), T-3 and T-4 places and frames, every T-5 still cut on
   its word, the T-9 hinges, the T-7 cut into the end card.
8. **The third-party moments** (creator / fetched, with its source / created) and the fallbacks used (`shot_id`,
   `fallback_used` on F-C stills).
9. **The sound:** the reveal cues, the list cue, the CTA cue, the bed's entry.
10. **The CTA:** the device, the keyword (if any), the end card's thumbnail or FB-3; the sponsor card and its disclosure if
    sponsored.
11. **The moments you'll look at hardest on the storyboard:** f0 (the presenter live, the claim caption, a board element entering); the
    payoff frame (≤ 1.0 s); one mid-body board state; the reveal of the last item or the final verdict; the end card. On
    each, look at the person: the caption under the chin, the window clear of the board.

The reel header and one hook, fully decided:
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

hook:
  name: "Rank skeleton: 5 offers"
  archetype: HA-07
  opening: O-2
  first_sentence: "These 5 online offers cheat us."
  pair: {claim: "30% + 20% off = 50% off", evidence: "44% (stacked_discount 30, 20)", card: P-15}
  post_title: "5 Online OFFERS Jo Aapko CHEAT Kar Rahe Hain!"
  alternates: ["Online Offers Ka SACH: 50% OFF Asli Mein Kitna?", "Ye 5 DISCOUNTS Aapko BEWAKOOF Bana Rahe Hain"]
  storyboard: "f0 tabs rise | 0.2-0.85 numerals 1-5 | 0.95 tab 1 + numeral 1 lit | 1.6 '30% + 20% off' | 4.8 '50% you think' | 6.6 strike + 44% tile"
  sound: [list cue at 0.95, reveal at 6.6]
  stopper: {mute: pass, motion_f0: pass, payoff_s: 0.95}
```

---

## §14 Worked examples

Times are planning estimates; the real onsets come from the cut. Each one shows the standard: match it, then beat it.

### 14.1 F-A, L-LIST, TH-maroon, fitness: "5 'healthy' snacks that aren't"
**Header:** F-A · TH-maroon · L-LIST · HA-07 / O-2 · count 5 · CTA comment_keyword "LABELS". Every gram figure comes from
the script (the creator read the labels) and lives in `plan/figures.json` as `from: script`.

**Hook (0–8 s):**
| t (s) | Spoken | Tone | Board | Caption | Cue |
|---|---|---|---|---|---|
| 0.00 | "These 5 'healthy' snacks are not healthy." | claim | S-tabs "SNACK 1…5" rising (ghost) | the sentence | — |
| 0.20–0.85 | — | — | Numerals 1–5 appear (ghost, 5 f stagger) | same | — |
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

Figures: `granola_sugar` (none, script "21 grams"), `yoghurt_sugar` (none, script), `bar_kcal` (none, script),
`chips_servings` (`ratio` of pack grams / serving grams, both script), `juice_sugar` and `cola_sugar` (none, script);
formats use `suffix: " g"` / `" kcal"`, `currency: ""`. Third-party moments: the pack labels → the creator's photos if
they're in the folder, else the brands' product pages fetched from the web (P-51, source noted); without either, P-49
recreated generic label rows.

### 14.2 F-B, L-CALC, TH-teal, personal finance: "₹5,000 a month: 10 years or 20?"
**Header:** F-B · TH-teal · L-CALC · HA-07 / O-3 · CTA end_card. Inputs (script): ₹5,000 per month, 12 % a year (the
creator states it as an assumption, so the rate input is `illustrative: true`; it shows as said, with no label), 10 and
20 years.

**Hook (0–4 s):**
| t (s) | Spoken | Panel | Caption | Cue |
|---|---|---|---|---|
| 0.00 | "Would you start investing at 25" | title "Would you start" + ghost card A | the sentence | — |
| 0.20 | — | card A fills "25" + unit "start age" (`data`) | same | reveal |
| 0.9 | — | `good` tag "Earlier?" drops on card A | same | — |
| 1.5 | "or at 35? Let's see." | card B fills "35" (`night`) | the sentence | — |
| 1.9 | — | the "Value at 60" bar skeleton slides up | same | — |
| 2.3 | — | T-3 morph into two bar badges; the title → "Which start makes more?" | same | — |
| 2.9 | "₹5,000 every month." | parameter chip "₹5,000 a month" | the sentence | — |

**Body plan:**
| Section | Spoken gist | Patterns | State / figures |
|---|---|---|---|
| Parameters (3–7 s) | "12% a year, till age 60" | P-21 chips "12% a year", "till 60" | inputs `sip`, `rate` (illustrative), `end_age` |
| Steps (7–28 s) | "After 10 years… 20… 25… 35" | P-23 slider (10/20/25/35) + P-24 race bars (both `compound` with `contribution`, one `scale_id`) + P-22 leader chip on "more" | `param` tick_to at each year word; the bars land on each spoken value |
| Verdict (28–31 s) | "Starting at 25 ends with <X>; at 35, <Y>." | P-22 final leader `good` "Ends higher" + P-33 gap counter | `gap` = `diff` |
| Why (31–44 s) | "The first 10 years do the most work" | T-4 → P-25 segment bars (each segment = one decade's growth) + P-26 explain lines "Early: 35 years compounding" / "Late: 25 years compounding" | segments from figure steps |
| Transfer (44–52 s) | "Same with your EPF and PPF" | T-4 → P-30 two-card stack "Start date / when you begin", "Years left / what compounds" → P-31 "Start date beats amount" | — |
| CTA (52–56 s) | "Do you agree?" | T-7 → P-44 end card (SH-3, else FB-3) | — |

### 14.3 F-C, S-CASE, TH-case, business stories: "case 03 / 07, the ₹40 crore order"
**Header:** F-C · TH-case · S-CASE · HA-12 · series {name: "Money Doesn't Behave", number: 3, of: 7} · CTA post_only. The
story, dates and amounts are the creator's researched script; every amount is a figure input `from: script`. 18 creator
stills (SH-2) + 4 object plates (FB-2) for beats no real photo fits.

**Hook (0–3 s):** f0 "episode three" + the prop (a purchase-order slip, SH-5 or FB-5) on the table; the title lines "money
/ doesn't / behave" at 0.60 / 0.70 / 0.80; the chapter "the ₹40 crore order" types at 1.6 s while the slip flips and falls;
at ≈ 3.2 s T-6 (fade 4 f + cut) into still 1 (a factory gate at dawn); the case tag "case 03 / 07" fades in.

**Body plan:**
| Section | Spoken gist | Stills / patterns | Ledger (P-40) |
|---|---|---|---|
| Setting (3–8 s) | "<Year>. A small factory in <city>." | P-38 ×3 (gate, office, ledger book) | — |
| The order (8–18 s) | "A customer orders ₹40 crore of goods." | P-38 ×4; the ledger rises in on "₹40 crore"; T-9 on the order (the inciting event) | ₹40,00,00,000 · ordered |
| The advance (18–26 s) | "He pays an advance of ₹4 crore." | P-38 ×3 | ₹4,00,00,000 · received |
| The turn (26–40 s) | "The goods ship. The rest never comes." | T-9 on "never comes"; P-38 ×5 + P-41 ×2 (a ship, an empty account screen as an object plate) | ₹36,00,00,000 · unpaid (`diff`) |
| Ending (40–48 s) | "But how did a ₹4 crore advance hide a ₹36 crore hole?" | P-42 hold on the last still | the final state glows once |

### 14.4 F-A, L-BUILD, TH-teal, productivity: "Where your 24 hours go"
The O-1 opening: row "WORK" 9 h (P-01/P-02, `suffix: " h"`), row "SLEEP" 7 h, the tag "NON-NEGOTIABLE" (P-03); P-05 tiles
"commute, meals, chores, phone"; P-06 total "24 h"; P-10 "what if the commute doubled?" → P-07 zero-out on "free time"
(3 h → 1 h, "was 3 h"); P-09 "the time comes from you, not your work"; CTA link_bio (P-46).

---

## §15 Your look at the storyboard: the checklist

Watch it once as a stranger with a thumb over the next reel, then once as the editor whose name is on it. Fix what
bothers you, in one pass.

**The style (does it feel like §The feel?)**
- Frame 0: the presenter live, the claim caption, a board element already entering; the first number by 1.0 s (the F-C
  title by 3.0 s); the first three seconds read on mute.
- The presenter never moves: no zoom, no punch-in, no shake; one layout for the whole body; jump cuts keep the framing.
- Every card earns its place: each one shows a number, a named quantity, a spoken item or the mechanism.
- The claim-vs-reality axis is clean: grey claims, white truths, the strike on the verdict word; red only for "costs
  more", green only for "true".
- The rituals are identical item to item, step to step; the last item, step or ledger state is the biggest.
- The motion matches §10.1: chips and tiles pop from a pill in 4 f, strikes 2 f, captions hard-swap, stills static; the
  white flash only on the F-C story's hinges.
- Captions quiet: no emphasis, no colour, no caps.
- Sound sparse: cues only on reveals, the list cue and the CTA; no meme cues; the bed after the hook.
- Start to end: at every moment the one thing that just changed is the number being said, and you'd trust it.

**Craft (by eye, in context)**
- The person: the presenter window and the F-B face cell clear of the board; the caption in the window's bottom strip
  under the chin (F-A, F-C) or on the chest (F-B); nothing chops the head or buries the face by accident.
- No text over text by accident: one board scene per section; slots steady and never overlapping each other or the
  window; nothing in the caption's place.
- On the word: rows, chips, tiles and tags land on their word; values and counters land on their number word; slider
  steps on their step word; jump cuts on word boundaries.
- Numbers right: every number recomputes (`veos figures`); compared bars share a scale; the ₹ glyph, grouping and
  compacts (or `$` and K/M/B in English) correct; illustrations carry no label and never pose as the creator's result.
- Promise: the rank count equals the items delivered; every "let's see" answered; the CTA keyword (if any) readable; the
  sponsor card has the spoken disclosure and "Paid partnership" visible.
- Spelling and glossary exact in captions and on cards; quotes and fetched posts word for word; personal identifiers in
  screenshots blurred.
- Readable on a phone: CS-1 (or CS-2 for the whole reel) 36 px, weight 500, ≤ 2 lines; small labels only when redundant;
  red and green text only in chips or on cards; no skeleton left waiting empty.
- Meaning text clear of Instagram's buttons.
- The file itself (1080 × 1920, 30 fps, −14 LUFS, the bed under the voice, the end card ≤ 3.5 s and a hard end after it,
  no black tail) is the render's job; it checks it.

---

## §16 Build notes

- **Fonts:** Poppins 500 / 600 / 700 / 800 (tabular figures for every number), Noto Sans Devanagari 500/700 for Hindi. The
  ₹ glyph is in Poppins.
- **Board scenes (B0):** z3, `kind: "ledger"`, `text_class: "TC-label"`, `exception: "E3"`, with `figures`, `lands`,
  `scale` and every internal change in `events`; mark micro-labels, tabs, parameter chips, tags, unit lines and sub-labels
  `data-redundant`.
- **E3 quiet type** (captions and every board/panel scene, the case tag, the ledger counter): `subtitle_min_px` 36,
  `label_min_px` 28 (redundant only), `contrast_min` 7.0, `pill_contrast_min` 4.5, `weight_min` 500, `max_lines` 2,
  `max_chars_line` 44. Captions inherit it from CS-1. It's what makes the ledger look like a calm UI rather than a reel
  (the original measures 30–34 px captions and 14–25 px labels; these are the floors above them).
- **E6 hard swaps** (`slot_tolerance_px` 4): the ledger counter (value + state word), the chip-tab state, the panel title
  swap, header swaps (P-08), the stress-test line swap (P-10). Mark the container `data-slot`; its first entry and final
  exit stay eased; the plan's beat carries the E6 too.
- **One exception per scene.** A board scene that needs both (labels under E3 and a tab swap) splits the tabs into the
  S-tabs scene with `exception: "E6"` and keeps E3 on the board.
- **Helpers:** `ctx.fig`, `ctx.figAt`, `ctx.fmtNum`, `VEOS.data.width` inside board scenes; `VEOS.data.bars` / `slider` /
  `counter` only when the helper is the only text on the board for its span (§8.2). The F-C ledger is a figure with
  labelled steps (§8.6).
- **Built-ins:** T-9 is a `timeline.transitions` flash (no scene); T-3 and T-7 blurs are the directional `ctx.blur(px,
  angle)`, never a uniform CSS `blur()`.
- **Determinism:** every frame is a pure function of its index; no `Math.random`, timers or video tags in scenes.

---

## Appendix A. Evidence map
The full map (every element → `vNN @ m:ss`), the fidelity audit (6 Oct 2026), the completeness pass at full frame rate
(7 Oct 2026) and the unverified list are in `evidence.md`. In short:

| Element | Source |
|---|---|
| Framed 16:9 inset at the top, the board below | v01 @ 0:00–0:44; v02 @ 0:00–0:39 |
| Face-bottom data panel | v03 @ 0:00–0:59 |
| Cinema-still band + 16:9 clip + case tag + ledger | v04 @ 0:03–0:49 |
| Quiet captions inside the footage | all four (v01 @ 0:00 "My wife Ruchi earns ₹75 lakhs a year.") |
| Label row → ghost chip → value | v01 @ 0:00.17–0:00.83 |
| Rank skeleton + chip tabs + strike reveal | v02 @ 0:01.3–0:39 |
| Dual stat → bars morph, slider, race bars, leader chip | v03 @ 0:00–0:32 |
| Title stagger + prop + chapter line | v04 @ 0:00–0:03 |
| End card with thumbnail and dashed arrow | v01 @ 0:45–0:48 |

Not copied from the original reels: captions at 30–34 px and labels at 14–25 px (raised to the E3 floors); the source's
`#2E8B3A` green (4.3:1, now `#26803A`); margins of 32–108 px with rows down to y ≈ 1760 (now 64 px margins, everything
above y 1500); v02's empty frame 0; v03's sponsor card with no visible disclosure; v04's AI-looking stills and 3D banknote
prop (the stills are the creator's own or object plates); v04's green-mono presenter clip (natural colour until the
engine can isolate an accent); "₹1.25 CR" (the engine writes "₹1.25 Cr"). Not verifiable: the speech language (no
transcripts), the caption transform, the sound bed.

## Appendix B. Hook-title bank
Post titles in the original's Hinglish shape (§6.5), with the first sentence that opens the reel.

**F-A Ledger inset**
| # | Post title | First sentence | Opening |
|---|---|---|---|
| 1 | 2 INCOMES Wale Ghar Mein Yeh GALTI Mat Karna! | "My wife earns ₹75 lakhs a year." | HA-07 / O-1 |
| 2 | 5 Online OFFERS Jo Aapko CHEAT Kar Rahe Hain! | "These 5 online offers cheat us." | HA-07 / O-2 |
| 3 | Aapki SALARY Kahan GAYAB Hoti Hai? | "Your ₹1 lakh salary leaves in 5 places." | HA-07 / O-1 |
| 4 | 4 BANK Charges Jo Koi NAHI Batata | "These 4 bank charges are hidden from you." | HA-07 / O-2 |
| 5 | ₹100 Roz Ka KHARCHA Kitna BADA Hai? | "₹100 a day is ₹36,500 a year." | HA-07 / O-1 (P-52) |
| 6 | 5 HEALTHY Snacks Jo Healthy NAHI Hain | "These 5 'healthy' snacks are not healthy." | HA-07 / O-2 |
| 7 | Aapki 2,000 CALORIES Kahan Jaati Hain? | "Your breakfast alone is 650 calories." | HA-07 / O-1 |
| 8 | Protein BAR vs Protein MEAL | "A protein bar has 20 grams of protein." | HA-07 / O-1 (P-34) |
| 9 | 5 LABELS Jo Aapko CONFUSE Karte Hain | "5 things on food labels mislead you." | HA-02 |

**F-B Face-bottom calculator**
| # | Post title | First sentence | Panel title |
|---|---|---|---|
| 1 | 8 Ka LOAN Ya 11 Ka LOAN, Kaunsa SASTA? | "Would you choose an 8% loan or an 11% loan?" | "Which loan costs you more?" |
| 2 | 25 Mein INVEST Karo Ya 35 Mein? | "Would you start investing at 25 or at 35?" | "Which start makes more?" |
| 3 | RENT Ya EMI, Kaunsa SAHI? | "Would you rent for ₹30,000 or pay a ₹45,000 EMI?" | "Which costs more in 10 years?" |
| 4 | Credit Card MINIMUM DUE Ka TRAP | "Would you pay the minimum or the full bill?" | "Which costs you more?" |
| 5 | FD Ya SIP, 10 SAAL Baad? | "Would you choose an FD or a SIP?" | "Which grows more?" |
| 6 | No Cost EMI Ka SACH | "Would you choose no-cost EMI or pay upfront?" | "Which costs you more?" |
| 7 | WALK Ya RUN, Zyada CALORIES Kismein? | "Would you walk 5 km or run 3 km?" | "Which burns more?" |
| 8 | GYM Membership Ka ASLI Kharcha | "Would you pay ₹2,000 a month or ₹18,000 a year?" | "Which costs less?" |

**F-C Case file**
| # | Post title | First sentence | Title / chapter |
|---|---|---|---|
| 1 | Episode 1 of 7. Money Doesn't Behave. | "Episode number 1:" | money / doesn't / behave · that phone call |
| 2 | Episode 2 of 7. The Missing Ledger. | "Episode number 2:" | money / doesn't / behave · the missing ledger |
| 3 | Episode 3 of 7. The ₹40 Crore Order. | "Episode number 3:" | money / doesn't / behave · the ₹40 crore order |
| 4 | Episode 4 of 7. One Signature. | "Episode number 4:" | money / doesn't / behave · one signature |
| 5 | Case 1. The Perfect Diet. | "Case number 1:" | the / perfect / diet · the 1,200-calorie summer |
| 6 | Case 2. The Miracle Powder. | "Case number 2:" | the / perfect / diet · the miracle powder |
| 7 | Case 3. 30 Days, 10 Kilos. | "Case number 3:" | the / perfect / diet · 30 days, 10 kilos |
