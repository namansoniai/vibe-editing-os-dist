# Science Flash Style Playbook (template v2)

## The feel

This reel is a friend who can't wait to show you something. Frame 0 is the creator mid-gesture, hand already reaching
for the lens, two words on screen: THIS ANIMAL. Before you've decided anything they're gone and the thing itself fills
the frame, landing with a pull-back while a white bracket grows up beside a man standing next to it. As big as a school
bus. You're hooked by a picture, not a promise.

From there it's a conveyor belt of real things. Every sentence gets its own picture of exactly what's being said, cut on
the caption beat. When the voice names a part, a place or a number, a lime arrow, pin or bracket lands on that exact spot
as the word is spoken. You never search the frame: each line pays you with something you can see, and the next already
has a new picture waiting.

The creator flashes. Half a second at the start, a burst of wonder when the footage earns it ("so many more!"), a hand
into the lens at the end. They're punctuation, never a lecture: the footage is the star, and every cut back to them feels
like their excitement spilling over. Flash them in whenever a moment does that, and never to fill.

It's curiosity, never comedy. The footage keeps its own colours and the only colour the edit adds is lime. Lime always
points. Sizes are never bare numbers: they stand beside something you know, in both units. It breathes with the voice:
quick cuts in the hook, a diagram allowed to evolve while things are compared, a beat of stillness on the answer, the
biggest number last. Then it doesn't end. It asks the next question, a sticker gets tapped, and the creator is back for
one word.

**The test:** pause on any frame and you can name what the voice is talking about, because you're looking at it; if
anything is lime, it's pointing at it.

## What this playbook is

You're editing a creator's selfie narration of a curious script (how does this work, how big is it, what did they find)
over the clips, stills and screenshots they own, and you have the authority to make it the most gripping explainer in
their niche. This playbook is the style, pulled from three of the original creator's science reels (v01 a giant pterosaur,
v02 hidden geoglyphs under the Amazon, v03 super-resolution microscopy) and measured frame by frame. Read it all, every
time; take what fits the reel, invent where a moment needs more, and never break the feel above.

**Who it's for and what it needs.** Explainers of science, tech, food, health, places: anything with a real thing to
show. Input: one handheld selfie take of the whole script (its audio is the voice, its picture gives the flashes) plus the
creator's B-roll, ideally a short clip for every sentence; a missing picture of a real thing is fetched from the web, and
what no real picture covers becomes a built diagram or scale scene (§12). No
cut-out is needed. Captions follow the creator's language (English, Hinglish or Hindi, set in their copy). The look *is*
the creator's footage: the more real clips they bring, the better the reel. Machine values live in `tokens.json`; where
this text gives a number tokens also holds, they agree.

### Style directives (non-negotiable)
| # | Directive | Where it lives |
|---|---|---|
| D1 | **Subject-first stopper.** The creator owns frame 0 for half a second; the subject is full-frame by 0.7 s. No banner, no title card, ever | §6.2, §3.4 |
| D2 | **One sentence, one picture.** Every caption-length sentence gets its own literal clip, still or diagram, cut on the caption beat. A visual that doesn't show the named thing is wrong | §8.4, §7.3 |
| D3 | **Captions are the reading line.** ALL CAPS, white, condensed, one line, 1–7 words, cy 1470, hard swaps, never coloured | §5.3 |
| D4 | **One lime, one meaning: look here.** Lime marks the thing to look at. A second hue appears only as the neon-blue glow world or a red hazard / recording HUD | §4 |
| D5 | **Point at it, on the word.** When the voice names a part, place or number, an arrow, bracket, pin or chip lands on that exact spot within ±5 f of the word | §8.6, §2 |
| D6 | **Show the real thing.** The creator's clips first; the real paper, page, photo or clip the line names is fetched from the web when they don't have it (source noted, never on screen); only what no real picture covers is built | §12.4 |
| D7 | **Scale is literal and dual.** "How big / how heavy / how far" is drawn beside a known object, and the number is shown in both unit systems | §5.5, P-MEASURE |
| D8 | **Curiosity, not comedy; end on a question.** No memes, no stickers other than the CTA sticker. The last seconds ask the next question and tap subscribe | §6.7, §7.1 |

### Quick index
| § | What |
|---|---|
| §1 | Procedure: how to approach a reel in this style |
| §2 | Hard rules: the craft and the style's never-list |
| §3 | Worlds, layouts, stage moves (the flashes), safe zones, the person |
| §4 | Colour: one lime that points |
| §5 | Type and captions: the lime chip, CS-1 one-line caps, other text TX-1…TX-10, language and numbers |
| §6 | Hook system: stopper test, HA-10 host flash → subject (S / P / D), HA-13, HA-14, hook pairs, CTA sticker and cliffhanger |
| §7 | Structure and rhythm: explainer + cliffhanger, the unit ritual, open loops, rhythm by feel |
| §8 | Visual system (B-roll and patterns): families B-1…B-10, patterns, line → pattern lookup, truth, the ink layer and anchors, sources, assets |
| §9 | Transition system T-01…T-09 |
| §10 | Motion tokens, footage camera, layers, finishing |
| §11 | Sound |
| §12 | Footage handling: setup, shots and fallbacks, resolution, inserts |
| §13 | What your plan should settle |
| §14 | Worked examples (3) |
| §15 | Your look at the storyboard: the checklist |
| §16 | Build notes |
| App. A / B | Evidence map / hook-title bank |

---

## §1 Procedure: how to approach a reel in this style

You watch, listen, plan, build and look at the storyboard yourself; the edit skill has the mechanics. This style
lives or dies on two crafts: matching a real picture to every sentence, and putting the lime mark on the exact pixel of
the thing being named. Decide in this order.

1. **Bank the B-roll.** Before planning a single beat, watch every clip the creator gave you and write `plan/broll.md`:
   one row per clip `{asset, shot SH-4/5/6/7, subject, what's visible, best 2–6 s span, motion, third-party or
   not, orientation, resolution}`. This is your menu. A 16:9 clip under 1440 px tall goes full-bleed only briefly
   and moving (§12.3); otherwise it's a band clip.
2. **Find the units** (§7.1): HOOK, LOOP (the line the creator reacts on), COMPARE, MECHANISM steps, PAYOFF, CLIFFHANGER.
3. **Mark each sentence's trigger word**: the noun, number or place its picture must show. That word is where the cut
   lands and where the mark lands. Ask what the viewer should see on it; the lookup (§8.4) is vocabulary for the answer.
4. **Feel the tone of each line:** `awe` (scale, a reveal) · `explain` (a mechanism) · `warn` (a hazard, a limit) · `win`
   (the payoff) · `hype` (the creator's own exclamation) · `cta`. Awe wants the land and the bracket; hype wants the
   creator's face; explain wants the arrow hopping along the part.
5. **Write the hook** (§6): pick the HA-10 variant from the opening claim (S scale, P place, D difference), write 8–10
   flash-line + claim pairs, pick by the stopper test, keep two alternates.
6. **Match a shot to every sentence** from the bank: the trigger word's subject, the best span. No clip fits → fetch the
   real thing from the web (a photo, the paper, the page, §12.4), else a created visual (FB-4, §12.2), named in the plan.
7. **Place every mark** (§8.6): its target in the clip, static or tracked, the side the arrow comes from, the frame it
   lands on.
8. **Decide the flashes** (§3.4, §7.5): the f0 flash, each drop-in and the reaction that earns it, the closing flash.
9. **Write every number in both units** (§5.5), only as the script says it.
10. **Place the stickers and write the cliffhanger** (§6.7): the next question, the sticker taps, the last word.
11. **Plan the sound** (§11): the hook cut, the landings, the non-cut transitions, the taps. Plain cuts are silent.

---

## §2 Hard rules: the craft and the style's never-list

**Craft, by eye** (judge it on the storyboard, in context, the way an editor does):
- **Keep the person clear.** A flash is the person and the caption, so keep the face, the hair and the room above the
  head clear. The framing that does it: on the creator's frames (L-host) the only things over them are the caption on the
  chest (cy 1470) and, on the closing flash, the sticker below the chin; marks stay off faces, in the creator's footage or
  in a borrowed clip (§3.6). A caption that brushes the chin as the handheld sways is fine; a face buried by accident
  never is.
- **No text over text.** One chip or plate at a time; marks never sit inside the caption or sticker bands; a
  sticker never lands while a chip, plate or hero number is landing.
- **On the word.** The picture of the trigger word cuts in 2 f before it; its mark lands within ±5 f of it. Cuts sit on
  the caption beat (±1 f of the word boundary), never mid-word. Captions lead by 2 f.
- **Say what was said.** Every number on screen is said in the script (or shown in the creator's own source screenshot);
  a conversion to the other unit system is a format, not a new claim; the speaker's hedge stays ("~600 BCE", "ABOUT 250
  NM"). Headlines and quotes on paper cards are word for word. Illustrations (a created silhouette, a schematic map, a dot
  field) carry no numbers the script doesn't say and no labels.
- **Promise integrity.** Every "look at this / watch this" is followed by the thing within a second; the sticker is on
  screen when "SUBSCRIBE / FOLLOW" is said; a comment keyword, when chosen, is on screen ≥ 1.5 s.
- **Spelling.** Species, instruments, places and units exact (the glossary); a case-sensitive term keeps its case in a
  chip ("LiDAR").
- **Readable.** CS-1 captions are 48 px (the measured size, under E3: floor 46 px, weight ≥ 700, one line, contrast ≥
  7:1 from the white fill and black stroke); labels ≥ 40 px; every
  lime element carries its dark `edge` outline so it
  reads on bright skies and white paper. Text holds ≥ 0.25 s per word and ≥ 10 f after it finishes typing.
- **Audio.** −14 LUFS integrated, true peak ≤ −1.5 dBTP, the bed ≥ 18 dB under the voice, a hard end ≤ 6 f after the last
  word, no black tail, no end card.

**Never in this style:**
- A banner, slab, title card or lower-third over the hook. The first words are the caption.
- Generic stock that isn't the subject: glowing brains, spinning globes for "science", abstract particles, lab-coat stock,
  Matrix code. If no clip shows the named thing, build a diagram.
- Coloured caption words, caption pills, caption boxes or karaoke. Emphasis lives in chips and labels.
- Lime without its `edge` outline; lime chips on green or yellow footage (they turn red, P-ALERT-CHIP).
- Two arrows on the same thing, or so many marks the eye doesn't know where to look.
- Comedy: meme sounds, reaction stickers, emoji, crash zooms, freeze-frame roasts.
- Zoom presets on the creator's footage (snap punches, crash zooms, rotation snaps): the handheld selfie already moves.
- Effect packs: whip pans, glitch packs, film burns, light leaks, spins. A new move is welcome when it's built in this
  style's language (a cut, a land, a seam, a lens, a flash of light).
- A clip that only decorates, or a clip that keeps showing one thing while the voice has moved on to another.
- A picture that isn't the real thing passed off as it: a look-alike, an AI image, a page altered to say something else.
  Fetched pictures are the real ones, shown clean.
- A grade, LUT or tint on the footage.

---

## §3 Worlds, layouts, stage moves, safe zones

### 3.1 Worlds
| ID | Kind | Look | Carries | Enter / exit |
|---|---|---|---|---|
| **W-host** | footage | The creator's own room on a handheld selfie (shelf, plant, window light), not regraded | The f0 flash, the drop-ins, the closing flash | T-01 hard cut in and out |
| **W-void** | void | `#000000` | Footage that sits on black (microscopy, space, night shots, the P-BAND-CLIP sides), P-SPLIT-REVEAL | T-01 |
| **W-grid** | stage | Charcoal `#2A2B34`, 2 px grid lines `#4A4D5E` at 85 % every 120 px, noise 0.02, vignette 0.22 | Real-looking specimens side by side (P-VS-STACK), scale lineups, silhouettes | T-01 in; T-07 to W-glow |
| **W-glow** | stage | Navy radial gradient `#16207A` (centre x 540, y 860) → `#060A2C`, noise 0.02, vignette 0.35 | The x-ray version of the same diagram: neon-blue `accent` outlines with an 18 px glow, white bones and lines, lime or white labels | T-07 from W-grid; T-01 out |
| **W-paper** | paper | `#FFFFFF` | Paper pages, quotes, figure cards, map figures (black serif type, lime highlighter) | T-01 |

The B-roll itself is not a world: it's a full-bleed scene at z1 (P-BROLL-FULL) on top of W-void.

### 3.2 Layouts
| ID | Engine | The creator | The picture | Caption |
|---|---|---|---|---|
| **L-host** | `full` | 0, 0, 1080 × 1920: the handheld selfie as shot | none (only the caption and, at the very end, the sticker) | CS-1, `fixed_y` cy 1470 |
| **L-evidence** | `hidden` | none | 0, 0, 1080 × 1920: the full-bleed clip or still at z1, marks at z5–6 | CS-1, cy 1470 |
| **L-diagram** | `hidden` | none | x 64–1016, y 160–1240 (64, 160, 952 × 1080) on W-grid, W-glow, W-paper or W-void | CS-1, cy 1470 |

Every switch lands on a sentence boundary, a pause or a "but" (`layouts.schedule.switch_on`).

### 3.3 Layout diagrams
```
L-evidence (and L-diagram)              L-host
┌─────────────────────────┐ 0          ┌─────────────────────────┐ 0
│ (IG top UI)             │ ← 0–110    │ (IG top UI)             │
│                         │            │      ╭───────╮          │ ← head top y 180–420
│                         │            │      │ face  │  ✋       │   (handheld, arm's length)
│   ANNOTATION BAND       │ ← y 160–   │      ╰───────╯          │
│   arrows, brackets,     │   1240     │                         │
│   pins, chips, labels   │            │      torso              │
│   (on the target)       │            │                         │
│                         │            │ ┌──────────────┐        │ ← sticker only at the end:
│ ┌─────────────┐         │ ← sticker  │ │  SUBSCRIBE ☝ │        │   cx 540, cy 1320, 440×120
│ │ SUBSCRIBE ☝ │         │   y 1260–  │ └──────────────┘        │   (chin above y 1220)
│ └─────────────┘         │   1380     │                         │
│ WAS AS BIG AS A BUS,    │ ← caption  │ THIS ANIMAL             │ ← caption cy 1470
│                         │   cy 1470  │                         │
│ (IG bottom UI, no text) │ ← y > 1540 │ (IG bottom UI)          │
└─────────────────────────┘ 1920       └─────────────────────────┘ 1920
```

### 3.4 Stage moves: the flashes
| ID | Move | Recipe (30 fps) | Use |
|---|---|---|---|
| **G-1** | Flash-out | `stage: {layout: L-evidence, via: cut}` on the word boundary after the 2nd–3rd word, 0.50–0.70 s in; the subject scene's `t_in` is the same frame | The f0 flash → the subject |
| **G-2** | Drop-in | `via: cut` into L-host on the first word of the line; out with `via: cut` on its last word + 2 f | The loop line, a reaction ("so many more!"), a section break in a longer reel |
| **G-3** | Closing flash | `via: cut` into L-host on the CTA verb's sentence, 0.6–0.8 s (measured 0.61–0.73 s, v01 @ 0:58.46, v02 @ 0:36.0); hard end ≤ 6 f after the last word | "…SUBSCRIBE!" |

There are no splits, PiPs, cards or morphs between the creator and the footage: the creator never shares the frame with
B-roll. Every return is a hard cut, on a sentence start, with a big gesture or a facial reaction: the reaction is the
reason to cut back.

### 3.5 Safe zones and bands
| Band | y range | What may live there |
|---|---|---|
| IG top | 0–110 | nothing |
| Annotation | 160–1240, x 64–1016 (x ≤ 970 below y 900) | arrows, brackets, pins, chips, labels, plates, hero numbers, diagrams |
| Sticker | 1260–1380 | the CTA sticker (cx 540, cy 1320) only |
| Caption | 1420–1492 | CS-1 captions only |
| IG bottom | > 1540 | nothing readable |

Meaning text stays inside x 64–1016, y 110–1500; nothing readable in the right column x > 970 between y 900 and 1540.
Footage and diagram pictures run full-bleed behind these bands; text never leaves them.

### 3.6 The person
- **The creator flashes.** They're on screen for the f0 flash, for every drop-in a reaction earns, and for the closing
  flash; the footage carries everything else. Their absence is what makes each return land.
- **The crop:** as shot. Head top at y 180–420, face 22–34 % of the frame's height (arm's length), so the chin sits
  somewhere around y 600–1070. A wider take (face under 18 %) is cropped centred on the face up to 1.25× (a 1080p source
  allows ≤ 1.35×).
- **What sits over them:** the CS-1 caption on the chest (cy 1470, 48 px; the line runs to about y 1496, inside the
  caption band y 1420–1492 plus its stroke), at least 340 px below even the lowest chin. On the closing flash, the sticker
  (440 × 120, y 1260–1380) sits below the chin with ≥ 40 px between the chin and the sticker's top: when the chin is lower
  than y 1220, the last sticker goes on the preceding B-roll beat instead and the closing flash carries only the caption.
  Nothing else belongs there: no chip, plate or mark on an L-host frame, and nothing above the head or over the hair,
  where the handheld sway moves them.
- **Behind them:** fair game, text included (`behind: true`), but it needs the cut-out, and this style rarely wants it:
  a flash is the person and the caption.
- **Faces in the footage:** marks never point at a face or cross one plus 40 px, in any clip.

---

## §4 Colour

### 4.1 Role palette
| Role | Hex | Its one job | Text on it | Contrast |
|---|---|---|---|---|
| `primary` **lime** | `#C6F000` | *Look here*: block arrows, keyword chips, typed keywords, diagram labels, map pins, ? marks, measure tags, hero numbers, the sticker, the highlighter on paper | `edge` | 8.6:1 |
| `accent` **neon blue** | `#2F6BFF` | The second voice, rare: neon outlines and glow in W-glow, the hand-drawn marker arrow (P-HAND-ARROW). Large text only | `paper` (large only) | 4.5:1 |
| `edge` **dark teal** | `#17454A` | The 5–6 px outline and hard shadow of every lime element; the text colour on lime | `paper` | 10.2:1 |
| `bad` **alarm red** | `#FF3B30` | A named hazard or limit, the REC HUD and trace markers, and the chip fill when lime would vanish on green or yellow footage | `paper` with a 4 px `edge` stroke | 3.6:1 (+ halo) |
| `good` **check green** | `#3DDC84` | A ✓ on a payoff, and nowhere else | `ink` | 11:1 |
| `paper` | `#FFFFFF` | Caption fill, measure brackets, dimension arrows, unit sub-lines, the paper world | — | — |
| `ink` | `#0A0A0A` | Serif text on paper (the caption stroke is pure `#000000`) | — | — |
| `night` | `#060A2C` | The W-glow floor (gradient from `#16207A`) | — | — |
| `grid` / `gridline` | `#2A2B34` / `#4A4D5E` | W-grid | — | — |

Measured in the reference: lime `#C6F000`, teal outline `#17454A`, grid ≈ `#2A2B34`, neon blue `#2F6BFF` / `#1E5BFF`, red
`#FF3B30`. Lime and blue are brandable: a creator's own colour can replace lime everywhere if it's a saturated light hue
that still reads on any footage behind the dark edge.

### 4.2 Meanings
- **Lime = look here.** The single accent. Its shape says what kind of "here": an arrow is a part, a bracket is a size, a
  pin is a place, a chip is the word to remember, a ? is the unknown.
- **Blue = the inside view.** Only in the glow world (the x-ray of the same diagram) and as the hand-drawn second arrow
  when a lime arrow is already on screen.
- **Red = hazard or recording.** A warning term, a REC HUD, trace markers. Never "wrong answer" theatre.
- **The footage keeps its own colours.** No grade, no LUT, no tint. A product's brand colours appear only inside the
  creator's own footage.

### 4.3 Rules
- Lime plus, at most, one other bright voice in a frame: blue or red, never both together.
- Every lime element has the `edge` outline (5–6 px) and a hard `edge` shadow 0/+6 px, no blur.
- On W-paper, lime is only a highlighter behind black serif text (the text stays `ink`), never lime text.
- A chip on green or yellow footage (lime against the footage around the chip under 3:1) switches to `bad` red with white
  text and a 4 px `edge` stroke (P-ALERT-CHIP; v02 @ 0:11 "LiDAR").
- Created worlds are flat colour; W-grid and W-glow carry their own vignette. Footage is never regraded.

---

## §5 Type and captions

### 5.1 Font map
| Slot | Family | Weight | Used for |
|---|---|---|---|
| `caption` | **Barlow Semi Condensed** | 700 | CS-1 captions |
| `display` | **Archivo Black** | its one black weight | chips, typed keywords, diagram labels, title plates, the sticker |
| `numeric` | **Montserrat** | 800–900 | hero numbers, dimension tags, ? marks, the REC tag |
| `body` | **Inter Tight** | 600–700 | unit sub-lines, leader labels, plate sub-lines, the sponsor line |
| `serif` | **Source Serif 4** | 400 / 700 | created paper and quote cards |

Measured faces: the captions are a semi-condensed DIN-like caps face (Barlow Semi Condensed); chips and labels are Archivo
Black. Brand wordmarks appear only inside the creator's own footage.

### 5.2 The headline element: the lime chip
There is no banner. The style's title device is the **keyword chip** (`type.headline.kind: chip`), with the **title
plate** as its two-line variant. Neither ever appears at frame 0.

| Property | Chip (P-KW-CHIP) | Title plate (P-TITLE-PLATE) |
|---|---|---|
| Fill | `primary` lime, radius 14, padding 8 / 24 | none (lime text on the footage) |
| Text | Archivo Black, **76 px** (64–84), ALL CAPS, `edge` colour | Archivo Black, **84 px** (72–96), ALL CAPS, lime, line height 1.0, 5 px `edge` stroke |
| Stroke / shadow | 5 px `edge` border; hard shadow 0/+6 px `edge` | stroke + 0/+6 px `edge` shadow |
| Sub-line | — | Inter Tight 600, 44 px, white (a date range or place: "~600 BCE – 850 CE") |
| Words / lines | ≤ 3 words, 1 line | ≤ 4 title words on ≤ 2 lines + the sub-line; ≤ 6 words in total |
| Position | Over the object, on its anchor; centre x 200–880, y 260–1180 | Upper third: centre y 520–760 |
| Entry | Typed: one letter per 2 f from the left, the box growing with the text; or a 7 f pop (0.6 → 1.08 → 1.0) for a long word | Line 1 types; line 2 types 4 f after; the sub-line rises 12 px + fades in over 8 f, 6 f after line 2 |
| Life | Holds still; one pulse (1.0 → 1.06 → 1.0, 6 f) if the word is said again | Holds |
| Lifetime | Until the shot cuts (≥ 1.0 s and ≥ words × 0.25 s + 10 f) | Until the shot cuts (≥ 1.5 s) |
| Exit | With the cut (0 f); a mid-shot exit fades over 4 f | Fades over 4 f |

Reference: "250 NANOMETERS" (v03 @ 0:09), "GEOGLYPHS" typed (v02 @ 0:04), "AQUIRY CIVILIZATION / ~600 BCE – 850 CE" (v02 @
0:26–0:28).

### 5.3 CS-1 captions: one line of white caps
| Group | Value |
|---|---|
| Mode | full, every spoken word; the picture still carries the meaning; the story reads muted |
| Chunking | `unit: line`; **1–7 words** (usually 3–6); **1 line**; ≤ **28 characters**; never split a name, number or unit; break on `, . ! ? …` and on pauses ≥ 0.6 s; a one-word chunk only for an exclamation ("SUBSCRIBE!") |
| Timing | Lead 2 f; min hold 0.25 s per word; **hard swap** (0 f); a chunk may hold 0.4 s into a pause, then clears; tail 0.12 s |
| Skin | **Barlow Semi Condensed 700, 48 px**, **UPPER**, tracking 0 (letters nearly touch), line height 1.1, `paper` white, **2 px black stroke** (`#000000`), shadow 0/+3 px rgba(0,0,0,.55); no container |
| Position | `fixed_y`, **centre y 1470** on every layout, centred at x 540, max width 952; `avoid_face` on |
| Punctuation | Kept as spoken: commas, "…", "!" ("WAS AS BIG AS A SCHOOL BUS,", "HIDDEN IN THE AMAZON…", "AND THIS!") |
| Emphasis | None. The caption is never coloured; the keyword goes into a chip (§5.2) |
| Hide | Never hidden (the black stroke keeps it readable even on the whiteout) |
| Language | English terms verbatim; the glossary spellings; profanity masked inside the word (S**T) |

**Measured:** the reference caption's cap height is 31 px (a 45–47 px font), bold, tight, a thin 2 px stroke, centre y
1518 (v01 @ 0:19, v03 @ 0:01). The style keeps the size at **48 px** (E3) and lifts it only to **cy 1470**, so its bottom
(≈ 1496) clears the y 1500 line above Instagram's buttons. 28 caps at 48 px are ≈ 640 px wide (the reference's
27-character line is 637 px). At 60 px it reads as a different, heavier style: don't.

### 5.4 Other text
| ID | Element | Recipe | Hold |
|---|---|---|---|
| **TX-1** | Typed keyword on footage (P-KW-WORD) | Archivo Black, 96 px (84–120), lime, 6 px `edge` stroke, 0/+6 shadow, no box; types one letter per 2 f with a white flare on the newest letter (v02 @ 0:04.3–4.8) | ≥ 1.0 s |
| **TX-2** | Diagram label | Archivo Black, 80 px (64–100), lime; the active label turns white and scales 1.25 | the diagram's span |
| **TX-3** | Leader label (P-LEADER-LABEL) | Inter Tight 700, 44 px caps, white with a 3 px black stroke, + a 3 px white leader line to the target; sub-line 40 px | ≥ 1.0 s |
| **TX-4** | Dimension tag (P-DIM-LABEL) | A lime pill, Montserrat 800 48 px `edge` text ("200 M") + the other unit beneath in Inter Tight 600 44 px white with a black stroke ("656 FT"); rotated to the dimension's angle (±35° max) | ≥ 1.2 s |
| **TX-5** | Hero number (P-HERO-NUMBER) | Montserrat 900, 96 px (84–140), lime, 5 px `edge` stroke; the other unit in Inter Tight 600 44 px white beneath; a white 8 px bracket under it | ≥ 1.5 s |
| **TX-8** | Sticker word (P-SUBSCRIBE-TAP) | Archivo Black, 56 px, `edge` text on a 440 × 120 lime button | ≈ 2.2–2.6 s including the 1 s fade |
| **TX-9** | REC HUD (P-REC-HUD) | "REC" Montserrat 900 56 px white + a 44 px `bad` dot with a 4 px white ring, top-centre y 210 | the shot |
| **TX-10** | Paper body text | Source Serif 4 400, 44 px, black; always next to a highlighted, readable span (headlines Source Serif 4 700, 56 px) | the card |

### 5.5 Language and numbers
- **Language:** captions follow the creator's speech. English is verbatim. Hinglish stays romanised, in the same caps.
  Hindi in Devanagari keeps the skin, size, stroke and position (Devanagari has no capitals, so the caps transform drops).
  Chips, labels and plates stay English, in their canonical spelling.
- **Spelling:** species, instruments and places are written in captions as spoken and in chips and labels in their
  canonical spelling ("LiDAR" keeps its case in a chip).
- **Grouping:** international (`130,000`) by default; Indian (`1,30,000`) when the creator's copy sets an Indian language.
- **Dual units.** Every length, mass, volume, temperature and speed on screen carries both systems: the spoken unit first,
  the other beneath (graphics) or in brackets (chips), written by `ctx.fmtNum(v, {unit, units: "metric"})` and
  `ctx.fmtNum(v, {unit, units: "imperial"})`; one decimal for converted values under 100. Units below a millimetre (µm,
  nm) have no everyday imperial pair: they stay metric, with a familiar comparison instead ("1/1000 OF A HAIR").
- **Ranges** use a spaced en dash: "130,000 – 150,000 KG". **Approximations** keep the speaker's hedge: "~600 BCE",
  "ABOUT 250 NM".
- **Currency:** `$` by default; `₹` with Indian grouping for Indian-language copies. Money is never converted.
- **Captions** show a number as spoken (digits for 10 and up, words for one to nine); graphics always show digits.

---

## §6 Hook system

**The hook title** promises the viewer something: an outcome they want, a curiosity gap, or who it's for ("How to go viral
as a doctor creating content", never the label "Reels for Doctors"). It needn't repeat the spoken words; it must be true
to what the reel delivers. In this style there's no title card: the hook title is the flash line plus the claim chunk, read
in the captions over the creator and then the subject, and the post title carries the same promise. Their shape is fixed
(§6.5); their voice is yours to make irresistible.

### 6.1 The stopper test
1. **Thumbnail:** frame 0 at 25 % scale: the creator's face (≥ 22 % of the frame's height) mid-gesture, and the caption
   still legible as a line.
2. **Mute:** the captions alone tell the claim by 3 s ("THIS ANIMAL / WAS AS BIG AS A SCHOOL BUS,").
3. **Motion at f0:** the hand is already moving on frame 0 (a wave, a reach toward the lens).
4. **Payoff:** the subject is full-frame by **0.7 s**.

The opening feels like a door flung open: half a second of a person who can't wait, then the thing itself, landing,
measured, pointed at, and a second clip before you've finished reading the first.

### 6.2 HA-10 Host flash → subject (default; variant S, scale reveal)
Spoken pattern: "[THIS SUBJECT] / [was as big as / could …] [a familiar comparison], / [a second fact], / and [did it in a
really surprising way]!"

| t (s) | Frames | Beat | Visual | Caption (CS-1) | Layout / motion | Sound |
|---|---|---|---|---|---|---|
| **0.00–0.60** | f0–f17 | Host flash | L-host. The creator on the handheld selfie, mid-gesture (an open hand moving toward the lens), saying the first 2–3 words | "THIS ANIMAL" (chunk 1 at f0) | No zoom; the handheld sway is the motion | — (a dry first frame) |
| **0.60** | f18 (±3 f, on the word boundary after word 2–3) | Cut to the subject | **G-1 hard cut** to the subject full-bleed (P-BROLL-FULL, `kind: subject`); **P-LAND** ×1.13 → 1.0 over 16 f (expo-out) | Hard swap to the claim: "WAS AS BIG AS A SCHOOL BUS," | L-evidence | **Hook cue** on the cut |
| 0.60–1.03 | f18–f31 | Scale proof | **P-MEASURE:** from the cut frame, a white 8 px arrow-line grows from the ground line to the top of the subject (13 f, ease-out) while the shot lands, beside a person or known object in the shot | holds | — | A reveal cue when the line tops out |
| 1.47–1.93 | f44–f57 | Hold | The bracket holds; the clip's own move continues | holds | — | — |
| **1.93** | f58 (±9 f, on the next clause) | Second fact | Hard cut to the second clip (the same subject, a new angle) | "MAY HAVE WEIGHED" → "AS MUCH AS A GRIZZLY BEAR," | — | — |
| 2.10–3.00 | f63–f90 | Point | **P-LIME-ARROW** lands on the feature the line names (pops on in 1 f, nudges 20 px in over 6 f), then holds | swaps on the comma | — | A reveal cue on landing |
| 3.0–4.8 | — | Proof run | One or two more one-line clips, each with its mark (P-ARROW-HOP, P-KW-CHIP) | one chunk per clip | — | — |
| **4.8–6.6** | — | Loop drop-in | **G-2 drop-in** to the creator (1.5–2.0 s), a big reaction on the open-loop line | "AND DID IT IN A REALLY FREAKY WAY!" | L-host | — |
| 6.6 | — | Into COMPARE | Hard cut to the diagram world (P-VS-STACK) | the next chunk | L-diagram | A transition cue |

Never hold the flash past 0.9 s, never put a chip, plate or sticker on the flash, and never open on B-roll with the
creator coming later (that's HA-14, an alternate with its own reason).

### 6.3 Variants and alternates
**HA-10 variants** (the same 0.0–0.7 s; the reveal differs):

| Variant | Use when the opening claim is about… | The 0.6–2.6 s reveal | Reference |
|---|---|---|---|
| **HA-10.S Scale** (default) | how big / heavy / far / fast | P-MEASURE or P-DIM-LABEL on the subject beside a known thing | v01 @ 0:00.67–0:01.8 |
| **HA-10.P Place** | where something was found or happens | P-PLACE-DOLLY on a map or aerial (1.0 → 1.5 with a −15° roll over 21 f) + P-MAP-PIN growing at 0.75 s with a ripple; a cut at ≈ 1.75 s to the close-up with a P-LIME-ARROW | v02 @ 0:00.58–0:02.6 |
| **HA-10.D Difference** | before/after, old vs new, blurry vs sharp | Image A in the top half on black ("BETWEEN THIS…"); at 1.3 s image B wipes in below from the seam (T-02, 9 f) ("AND THIS!"); at 2.46 s P-SNAP-PUSH, a 0 f punch-in cut ×2.46, on "BOTH" | v03 @ 0:00.62–0:02.5 |

**HA-10.P**
| t | Visual | Caption |
|---|---|---|
| 0.00–0.55 | Host flash, a hand toward the lens | "THEY FOUND SOMETHING" |
| 0.58 | Cut to the aerial or map of the region; the place name set in type, tilted onto the ground plane; P-PLACE-DOLLY starts | "HIDDEN IN [PLACE]…" |
| 0.75 | P-MAP-PIN grows from its tip (0 → 1, 8 f) + a ripple ring (18 f) on the exact site; the map keeps dollying | holds |
| 1.75 | Cut to the close-up of the find | "[HUNDREDS OF …]" |
| 1.95 | P-LIME-ARROW pops onto the structure, nudges 20 px in, holds | holds |
| 2.6 | T-04 state swap: the same frame in another render (colour map, night/day, x-ray) + a second arrow | the next chunk |

**HA-10.D**
| t | Visual | Caption |
|---|---|---|
| 0.00–0.60 | Host flash, a frown and a reach toward the lens | "LOOK AT THE DIFFERENCE" |
| 0.62 | Cut to W-void: image A in the top half (y 260–760) | "BETWEEN THIS…" |
| 1.30–1.60 | T-02 seam wipe: image B draws in below the seam (y 760–1240) | "AND THIS!" |
| 2.46 | P-SNAP-PUSH: a punch-in cut ×2.46 on the seam (0 f) | "BOTH IMAGES" |
| 3.5–5.0 | P-HAND-ARROW (accent blue) draws from A down into B | "BUT THIS ONE WAS TAKEN WITH A" |

**Alternates (other archetypes)**
| ID | When | Recipe | Reason to choose it |
|---|---|---|---|
| **HA-13 Cold action** | The single best clip is an action (a launch, a collapse, an animal taking off) and the opening words describe it | f0 = the action clip moving + caption chunk 1; the first cut by 2.1 s; the creator's drop-in at 3–6 s carries the loop line | Rare: only when the action clip stops a thumb better than the creator's face would |
| **HA-14 Cold authority** | The script opens mid-thought on one striking image ("This is the sharpest picture of a cell ever taken.") | f0 = the strongest still or clip + the caption; the strongest image by 1.0 s; the creator's drop-in by 6 s | Only when the opening flash (SH-2) is unusable and the narration take's first words have no gesture (FB-2) |

### 6.4 Hook pairs by topic
The pair is **subject → reveal**: the flash words, and what lands on the subject by 0.7–2.0 s. When the topic is new, build
the pair the same way.

| Topic | Flash words (0.0–0.6 s) | Reveal by 0.7–2.0 s | Variant |
|---|---|---|---|
| A giant pterosaur (v01) | "THIS ANIMAL" | The creature beside a man; P-MEASURE grows to its head | S |
| Geoglyphs under the Amazon (v02) | "THEY FOUND SOMETHING" | Map dolly + pin on the site; cut to the LiDAR relief with an arrow | P |
| Super-resolution microscopy (v03) | "LOOK AT THE DIFFERENCE" | The blurry nucleus on top, the crisp one wiping in below | D |
| Data-centre scale | "THIS BUILDING" | Aerial of the data centre; P-DIM-LABEL along its length in m / ft; a person silhouette for scale | S |
| Chip transistors | "THIS CHIP" | Macro of the chip; P-SNAP-PUSH into the die; P-KW-CHIP "[N] BILLION SWITCHES" | S |
| Phone night mode | "LOOK AT THE DIFFERENCE" | The dark, noisy photo (top) → the night-mode photo (bottom), seam wipe | D |
| Undersea cables | "THEY RUN UNDER THE OCEAN" | Map dolly + pins at both landing stations; P-DIM-LABEL along the route in km / mi | P |
| Satellite internet | "THERE ARE THOUSANDS" | Night-sky clip; P-QMARK-SWARM → the dots resolve into satellites; P-LIME-ARROW on one | S |
| Sugar in a soda | "THIS CAN" | The can beside a stack of sugar cubes; P-MEASURE up the stack; P-HERO-NUMBER g / oz | S |
| Gut bacteria | "INSIDE YOUR GUT" | Microscope clip; P-KW-CHIP "TRILLIONS"; P-LIME-ARROW on one cell | S |
| Where coffee grows | "EVERY CUP STARTS HERE" | Map dolly to the growing belt + pin; P-DIM-LABEL altitude in m / ft | P |
| Sleep and the brain | "WHILE YOU SLEEP" | Brain-scan still; P-OUTLINE-TRACE around the region named; P-KW-CHIP with the region's name | S |

### 6.5 Headline writing (the first words)
There's no banner, so the headline is the **flash line + the claim chunk**:
- **Flash line (chunk 1, f0):** 2–3 words, a demonstrative ("this") or "they / look" + the subject: "THIS ANIMAL", "THEY
  FOUND SOMETHING", "LOOK AT THE DIFFERENCE", "THIS CHIP", "INSIDE YOUR GUT".
- **Claim chunk (chunk 2, 0.6 s):** the size or novelty claim against something familiar, ≤ 7 words: "WAS AS BIG AS A
  SCHOOL BUS,", "HIDDEN IN THE AMAZON…", "BETWEEN THIS…".
- **Loop line (the drop-in, ≈ 5–6 s):** an exclamation that promises a mechanism: "AND DID IT IN A REALLY FREAKY WAY!",
  "THAN WE EVER KNEW ABOUT!".
- **Post title (App. B):** "How This [Thing] Could [Verb]", "They Found Something Hidden In [Place]", "This [Instrument] Is
  Insane". Title Case.
- **Never:** "You won't believe", "scientists are baffled", a claim the reel doesn't show, a comparison object the clip
  doesn't show, emoji in captions.
- Write 8–10 flash-line + claim pairs, pick by the mute read and the subject-by-0.7 s test, keep the next two as
  alternates.

### 6.6 Hook sound
A cue on the G-1 cut and one on the first mark landing (§11). The bed runs from f0, ≥ 18 dB under the voice. Frame 0 is
dry: the creator's voice is the first sound.

### 6.7 CTA: the scheduled sticker and the cliffhanger
**The device:** subscribe by default. The sticker word is **FOLLOW** on Instagram-first reels and **SUBSCRIBE** when the
reel is also posted as a YouTube Short (the reference word). With a comment keyword the final sticker reads **"COMMENT
[KEYWORD]"** (`kind: "cta-keyword"`, P-KEYWORD-TAP); with link in bio it reads **"LINK IN BIO"**.

**The schedule.** The sticker is the reel's recurring nudge, tapped by a cursor every so often, and the last tap lands on
the spoken CTA.
| Sticker | When | Over | Spoken? |
|---|---|---|---|
| **S1** | Once the viewer is hooked and the story is rolling: a sentence end on a B-roll or diagram beat with the sticker band (y 1260–1380) free (the reference: 12–25 s) | B-roll / diagram | No |
| **S2** | In a longer reel, a sentence end around two-thirds of the way through | B-roll / diagram | No |
| **S3** | The CTA word at the end ("…SUBSCRIBE!" / "…FOLLOW!" / "…COMMENT [KEYWORD]!") | The closing flash (G-3), or the cliffhanger visual when the creator's chin is below y 1220 | **Yes** |

Spread them so each one feels like a nudge, not a nag (the reference taps are about 20–30 s apart, `schedule_every_s`
20: v01 @ 0:25 / 0:57, v02 @ 0:14 / 0:35, v03 @ 0:12 / 0:52). Never in the hook; never while a chip, plate or hero number
is landing.

**Sticker recipe (P-SUBSCRIBE-TAP):** a 440 × 120 lime button at cx 540, cy 1320, radius 16, 5 px `edge` border, hard
shadow 0/+8 px `edge`, the word in Archivo Black 56 px `edge`. **Measured motion** (v01 @ 0:24.52–26.9, v02 @
0:34.9–36.7): it **rises in** from 28 px lower with a 6 f fade, ease-out, no scale pop (width constant). A white hand
cursor (64 px, 3 px `edge` outline) slides in from the lower right (+150, +90) over 8 f, **0.9 s after** the button lands,
to its lower-right corner; the **tap comes 8 f later**: the button goes to 0.94 for 3 f and three 4 px lime spark lines
burst from its upper-left corner over 6 f. The sticker is a z8 overlay that **rides across cuts** (two or three clips run
under it). Exit: a slow fade to 0 over 30 f (1.0 s). S1 and S2 last 2.2–2.6 s in all; S3 enters 1.1–1.7 s before the end
over the last B-roll beats and holds through the closing flash.

**The cliffhanger (P-CLIFFHANGER, the last few seconds):** "BUT [the bigger / smaller / next question]…" over a teaser
visual (the next subject as a dark silhouette, or a hero number under P-QMARK-SWARM), then "[TO SEE / LEARN] THAT," with
S3 rising in, then the closing flash on "SUBSCRIBE!" (G-3). A held breath of up to 0.4 s before "BUT" is the one pause the
reel allows. Hard end ≤ 6 f after the last word; no end card.

**A sponsored reel:** the sponsor is said aloud and a "[the creator's handle] · Paid partnership" line (Inter Tight 600, 24 px,
white at 75 %, top-left at x 64, y 140) holds for ≥ 2 s. It's a legal disclosure, the only small print the style allows.

---

## §7 Structure and rhythm

### 7.1 Structure: an explainer with a cliffhanger
| Section | Span in a 55 s reel | What happens | Layout |
|---|---|---|---|
| **HOOK** | 0–5 s | HA-10: flash → subject → two or three proof clips with marks | L-host → L-evidence |
| **LOOP** | 5–7 s | The creator drops in (G-2) with the open-loop exclamation | L-host |
| **COMPARE** | 7–16 s | The subject against one or two familiar things on the same axes: P-VS-STACK → P-VS-FOCUS → P-XRAY-SWAP, or two clips in sequence with matching framing | L-diagram, L-evidence |
| **MECHANISM** | 16–46 s | Three or four steps, each a unit ritual (§7.3); one sustained analogy (P-ANALOGY-SCENE) may carry a stretch | L-evidence, L-diagram |
| **PAYOFF** | 46–51 s | The answer made visible: P-HERO-NUMBER, the crisp result (P-SPLIT-REVEAL), or the subject doing the thing; a ✓ if it's a win | L-evidence |
| **CLIFFHANGER** | the last 3–5 s | P-CLIFFHANGER + S3 + the closing flash | L-evidence → L-host |

A shorter reel (35–45 s) shrinks COMPARE to a few seconds and MECHANISM to two steps.

### 7.2 Markers
No numbered badges: the steps are spoken. In COMPARE, the parallel labels of P-VS-STACK ("BIRD / PTEROSAUR / BAT", v01 @
0:07–0:14) are the list, and the active row lights up (P-VS-FOCUS). A creator who runs a numbered series can add a "#[N]"
lime chip top-right (x 900–1016, y 130–176) for 1 s at the first subject cut.

### 7.3 The unit ritual (every MECHANISM step)
1. **Cut** (T-01) on the step's first caption chunk to the literal subject of the sentence (P-BROLL-FULL / P-STILL-PUSH /
   P-BAND-CLIP).
2. **Land** stills and pages (P-LAND); moving clips run their own motion.
3. **Point** on the trigger word: the mark that matches the line (an arrow at a part, a bracket at a size, a pin at a
   place, a chip at a term) lands within ±5 f.
4. **Evolve** inside the shot when the line names a second part: P-ARROW-HOP (the arrow travels to the next part) or a
   second mark.
5. **Swap** to the next clip on the next sentence; marks and chips stay to the last frame and leave **with the cut** (v01
   @ 0:01.93).

A step lasts as long as its idea: one clip for a quick fact, three for a mechanism that needs walking through.

### 7.4 Open loops
- **The loop line** (the LOOP drop-in) promises a mechanism ("…in a really freaky way!"); the MECHANISM pays it on screen.
- **"Look at / watch this"** is paid within a second by the thing itself (v01 @ 0:29 "BUT JUST WATCH THIS" → the bat
  walks).
- **The cliffhanger** is the only promise left open: it points to the next reel.
- **Re-hooks:** in a longer reel, a drop-in at a section break does the job: the creator's face back, reacting, is the
  freshest thing the viewer has seen in twenty seconds. The intro (hook + loop) is over fast, so the first comparison
  arrives while the promise is fresh.

### 7.5 Rhythm by feel
- **The voice is the conveyor.** Every sentence brings a new picture on its caption beat, and nothing waits: no dead air,
  pauses tightened to a breath. The one held breath is before the cliffhanger's "But…".
- **It never sits still, but it's never random.** Moving clips carry their own camera move; a still or a page lands and
  holds, and something arrives on it (a wipe, a punch, a mark, a highlight) because the words give it a reason. When a
  shot has nothing new to show, cut.
- **The energy curve:** the hook is the fastest stretch (a cut on nearly every caption) → COMPARE breathes (one diagram
  evolving while the things are compared) → MECHANISM is steady (a cut on each sentence; the analogy, if there is one,
  may breathe longer as long as its own marks keep landing) → the PAYOFF gets a beat of stillness on the answer, the
  biggest number of the reel → the CLIFFHANGER is quick.
- **The flashes are punctuation.** The creator cuts in when wonder spills over: the loop line, a "so many more!", a
  section break, the close. Flash them as often as the reel has those moments; never to fill a gap and never long enough
  to become a talking head. A flash reads from about half a second; a drop-in lasts as long as the reaction.
- **Marks escalate with the line:** one arrow for a part, a hop when the line walks the structure, a pincer when it names
  two, the hero number and the bracket for the payoff.
- For reference, measured on the three reels (a description, not a target): the creator is on screen 4–11 % of the
  runtime and can be gone for nearly a whole minute (v01: 0:06.6 to 0:57.5); the median shot is 1.8 s (p90 4.7 s, the
  longest 9.8 s, an analogy carried by its marks); 16–36 cuts a minute; ≈ 85 % of boundaries are plain cuts.
- No comedy beats. The entertainment is wonder: scale shots, reveals and the creator's reactions.

### 7.6 Recurring devices
- **The lime pointer** is the reel's constant: every step has one, so the viewer learns that lime means "look here" and
  looks there instantly.
- **The sticker** comes back as a nudge and the last tap closes the reel (§6.7).
- **The creator** returns three ways: the f0 flash, the drop-in, the closing flash. Always a hard cut, always a reaction.

---

## §8 Visual system: B-roll and patterns

The creator's footage carries the reel; graphics point at it, label it, measure it, and replace it only where no clip
exists. **Numbers become pictures** whenever they are about size, amount or distance: a bracket against a known object, a
dimension tag on the object, a lineup on one ground line, a hero number with both units. Never a bare number card.
Variety comes from the script's own moments; the unit ritual is the one deliberate repeat. When the lime arrow has led a
few shots in a row, let the next line's mark be a bracket, a chip, a pincer or a label.

### 8.1 Families
| ID | Family | Source | The creator supplies | Created substitute when missing |
|---|---|---|---|---|
| **B-1** | Subject B-roll clip, full-bleed | the creator's own or held, else the real clip fetched from the web | a short clip (2–6 s) for nearly every sentence (SH-4) | a fetched still (B-2), else a B-3 / B-4 diagram (FB-4) |
| **B-2** | Still (photo, render, figure image) with a land | the creator's own or held, else the real one fetched from the web | stills ≥ 1500 px tall (SH-7) | B-3 diagram |
| **B-3** | Created diagram on W-grid / W-glow / W-void | built | — | — |
| **B-4** | Created scale scene (silhouettes, rulers, lineups) | built | — | — |
| **B-5** | Paper / quote / figure card on W-paper | the creator's screenshot (SH-6), else the real page captured from the web, else created | the page screenshot with outlet, date, headline | `fx.headlineCard`, `fx.quoteCard` |
| **B-6** | Ink annotation (arrows, brackets, pins, ? marks, traces) | built | — | — |
| **B-7** | Type (chips, typed keywords, plates, hero numbers, leader labels) | built | — | — |
| **B-8** | The creator's footage (flash, drop-in, close) | the creator (SH-1–SH-3) | the selfie narration | none (FB-1) |
| **B-9** | CTA sticker | built | — | — |
| **B-10** | Map (aerial, globe, figure map) | the creator's map clip or still, else a real map or the paper's figure fetched from the web, else a created schematic | map footage or a map figure they hold | P-MAP-SCHEMATIC |

### 8.2 Building blocks
Motion is in frames at 30 fps. "Anchor" means the mark follows its target in the clip (§8.6). Engine names are `VEOS.fx.*`
or a bespoke `VEOS.scene`.

### 8.3 Pattern specs

**The creator (B-8)**
| ID | Type | On screen | Motion | When | Engine / needs |
|---|---|---|---|---|---|
| **P-HOST-FLASH** | stage | The creator's selfie, mid-gesture, the first 2–3 words | Hard cut in at f0, hard cut out at 0.50–0.70 s (G-1); no zoom | f0 of every HA-10 reel | `stage: [{t:0, layout:"L-host"}, {t:0.6, layout:"L-evidence", via:"cut"}]` |
| **P-HOST-DROPIN** | stage | The creator reacting big on one line | As long as the reaction (1.5–2.5 s in the reference), hard cuts both ends (G-2) | The loop line; a reaction the footage earns; a section break in a longer reel | stage entries |
| **P-HOST-CLOSE** | stage | The creator on the CTA sentence, pointing down at the sticker or reaching into the lens | 0.6–0.8 s to the hard end (G-3), the hand reaching into the lens (v01 @ 0:58.46, v02 @ 0:36.0) | Every reel's last words | stage entry + the S3 sticker |

**Footage (B-1, B-2)**
| ID | Type | On screen | Motion | When | Engine / needs |
|---|---|---|---|---|---|
| **P-BROLL-FULL** | footage-treatment | The creator's clip (or the real one fetched), full-bleed 9:16 cover crop on the subject | Hard cut in; the clip's own camera move is the motion (measured ≈ 1 %/s push or pull, v01 @ 0:02.0, 0:14.4); a scene push 1.00 → 1.03 only when the clip is locked off. The hook subject and any clip that must read as "huge" use P-LAND first | Every sentence with a matching clip | `fx.clip({z:1, in:"none", out:"none", kind:"subject", focus})` (+ `kenburns: [1, 1.03]` only when locked off); a fetched clip's source noted |
| **P-STILL-PUSH** | footage-treatment | A still, full-bleed | P-LAND in (×1.8 → 1.0), then **holds still** (v03 @ 0:00.84–2.42 static); the events on it (a wipe, a punch, a mark) carry it. A still with nothing arriving on it soon gets a slow 1.00 → 1.04 drift | A photo, render or figure image | `fx.clip({z:1, asset: still, focus, land: {from: 1.8, frames: 10}})` (holds after landing; `kenburns: [1, 1.04]` only when nothing lands on it) |
| **P-BAND-CLIP** | footage-treatment | A 16:9 clip as a 1080 × 608 band at cy 800 over a blurred (24 px), 45 %-dimmed copy of itself | Push 1.00 → 1.04 inside the band | 16:9 clips too small to crop (§12.3) or whose crop loses the subject | two `fx.clip` scenes (z1 the blurred copy with `dim: 0.55`, z2 the band) |
| **P-SNAP-PUSH** | footage-treatment | The current shot punched in ×2.0–2.5 on the detail (a punch-in **cut**) | 0 f: the very next frame is ×2.46 on the detail (v03 @ 0:02.46), on the caption swap; then holds still. A 1080p source caps at ×1.6 | "BOTH", "LOOK", "RIGHT HERE" on a detail: save it for the line that tells you to look | the clip scene's own scale keyed to an `event` |
| **P-SPLIT-REVEAL** | footage-treatment | Image A in the top half (y 260–760), image B drawn in below a seam at y 760 | A lands with P-LAND (×1.8 → 1.0, 8 f) and holds; B wipes downward from the seam in 9 f (T-02) starting on the "AND THIS!" swap; then P-SNAP-PUSH on the seam | "the difference between this… and this" | image A `fx.clip({x: 0, y: 260, w: 1080, h: 500, land: {from: 1.8, frames: 8}})`; image B a clip scene with a `clip-path` driven by `lt`; `events` at the wipe |
| **P-STATE-SWAP** | cut | The same framing in another render (colour map, x-ray, night/day, before/after) | Hard cut (T-04); the marks keep their anchors | "revealing…", "and in infrared…" | two clip scenes, the same `focus` |
| **P-WHITEOUT** | footage-treatment | The frame flooding to white as content ("all you'd see is a blinding glow") | An ease-in ramp to ≈ 95 % white over 18 f (luma 70 → 240, v03 @ 0:22.85–23.6), hold 3–6 f, recede over 15 f to ≈ 60 % white (the scene stays glowing); the captions stay on (black stroke) | A literal glare, blinding or overexposure line, whenever the script has one | the built-in transition on the peak frame: `{"t": <peak>, "type": "flash", "colour": "#FFFFFF", "peak": 0.95, "pre": 18, "frames": 30, "decay": 1.2}` (18 f up, the peak, 12 f down onto the veil; the picture layers only, so the captions stay on top); the ≈ 60 % rest glow is a static z2 white veil (opacity 0.6) from the peak to the cut |
| **P-LENS-IRIS** | footage-treatment | A circular viewer (a lens or porthole) with a tick-marked ring; the subject inside | The circle opens from r 0 → 430 px in 12–14 f (T-05); the ring ticks rotate 6°/s | "through the microscope / telescope / lens" | bespoke scene: `clip-path: circle()` + an SVG ring |
| **P-LAND** | footage-treatment | The new picture arrives scaled up on its subject and pulls back to its resting frame | Scale ×1.12–1.2 (footage) or ×1.8–3.7 (stills, pages, split image A) → 1.0 over 10–16 f, expo-out, starting on the cut frame; then the shot holds or runs its own motion (v01 @ 0:00.70 ×1.13 / 16 f; v03 @ 0:00.63 ×1.8 / 10 f; v02 @ 0:06.63 ×3.7 / 10 f) | Every still, page and split; the hook subject; the cliffhanger lineup. Once per shot, on its cut; never on the creator's footage | `fx.clip({asset, focus, land: {from, frames}})` (expo-out by default; `in` becomes `none`, so the shot never fades up): footage `{from: 1.13, frames: 16}`, stills `{from: 1.8, frames: 10}`, pages `{from: 3.0, frames: 10}` (`fx.clip` caps `from` at 3; v02's page lands from 3.7) |
| **P-RECAP-RUN** | cut | Three or four shots already seen in this reel, re-cut at 0.4–0.6 s each, no marks | Hard cuts on a steady beat under one summary line | "…revealing what was hidden before!" (v02 @ 0:20.1–22.4); under the cliffhanger / CTA line (v02 @ 0:34.8–35.7) | `fx.clip` scenes reusing assets |
| **P-PLACE-DOLLY** | footage-treatment | A map or aerial pushing toward the site; the place name set in type and tilted onto the ground plane (white 60 %, Montserrat 800, 72 px) | Scale 1.00 → 1.50 over 21 f (ease in-out: ≈ 1 %/f for the first 5 f, peak ≈ 5 %/f mid) **with a −12 to −16° roll** around the site (v02 @ 0:00.62–1.29); the name rides with the map | "in [place]", "hidden in…" | `fx.clip({asset, focus: <site>, kenburns: [1.5, 1.5], land: {from: 0.667, frames: 21, ease: "inOut"}, rotate: [0, -15]})` (1.0 → 1.5 with the roll eased with the land, then held; the image is scaled to keep covering) + a z5 label that rides the same scale and roll |

**Ink annotation (B-6)**
| ID | Type | On screen | Motion | When | Engine / needs |
|---|---|---|---|---|---|
| **P-LIME-ARROW** | annotation | A chunky lime block arrow (≈ 210 px across, 200–220, × 150 px), 6 px `edge` outline, hard shadow 0/+6, the tip 24 px off the target | **Pops on at full size in 1 f**, 6 f after the cut, nudges 20 px toward the target over 6 f (ease-out), then **holds** (drift ≤ 3 px, no bob; v02 @ 0:01.95–2.53); exits hard on the cut | "this part", any named feature | bespoke SVG scene; **anchor** |
| **P-ARROW-HOP** | annotation | The same arrow gliding along the structure to the next named part | Glides along the part over 1.5–2.5 s (sine in-out), re-aiming as it goes (← to ↓, v01 @ 0:15.4–17.9); a jump to an unrelated part is 8 f in-out | The line names a second or third part, or the length of one part (v01 @ 0:15–0:18) | the arrow scene with `events` at each hop; **anchor** |
| **P-PINCER-ARROWS** | annotation | Two curved lime marker arrows from both sides converging on two points | Each shaft draws in 8 f (stroke-dashoffset), the head pops in 2 f; the second starts 4 f after the first | "both its legs and its thumbs", two matching parts (v01 @ 0:33) | SVG paths; **anchor ×2** |
| **P-HAND-ARROW** | annotation | A hand-drawn curved marker arrow in `accent` blue, 20 px stroke | Shaft draws in 10 f, head in 2 f; no bob | A second mark when a lime one is on screen, or "this one" between two images (v03 @ 0:04, 0:29) | SVG path; **anchor** |
| **P-MEASURE** | annotation | A white 8 px measure line with a 56 px flat foot cap and an arrowhead at the top, beside the subject; a person or known object in frame for scale | Starts on the cut frame and grows from the ground line to the top in 13 f (ease-out, v01 @ 0:00.70–1.12) while the shot lands (P-LAND); holds to the cut | "as big / tall / long as" (v01 @ 0:00.8–0:01.8) | SVG scene; **anchor** (ground y, top y) |
| **P-DIM-LABEL** | annotation | A white two-headed arrow along a dimension of the object + a TX-4 dual-unit tag rotated to it | The arrow grows outward over 22 f and the tag **rolls its number with the arrow's length** (10 m / 3 ft → 170 → 196 → **200 m / 656 ft**, v02 @ 0:05.05–5.8), landing on the spoken value ±5 f | "[N] metres across", an exact size (v02 @ 0:05–0:06) | SVG + an HTML tag; **anchor** (two endpoints); `fmtNum` dual; the roll is bespoke |
| **P-MAP-PIN** | annotation | A lime map pin (64 × 88 px, `edge` outline) + a lime ripple ring | Grows from its tip 0 → 1.0 in 8 f (ease-out, no drop) while the map dollies; the ring r 0 → 90 px over 18 f, fading out; one repeat ring at +24 f | The exact place (v02 @ 0:00.75–1.0) | SVG scene; **anchor** |
| **P-QMARK-SWARM** | annotation | 3–5 lime "?" glyphs (Montserrat 900, 72–110 px, `edge` stroke) scattered around an unclear area | Pop in with a 3 f stagger (0 → 1.15 → 1), wobble ±6° every 20 f | "no one knows", "we don't know", "what is the smallest…?" (v02 @ 0:31, v03 @ 0:26, v01 @ 0:57) | bespoke scene; seeded positions (`ctx.rngStable`) |
| **P-REC-HUD** | annotation | The TX-9 REC tag + red triangle markers (28 px) on the points being recorded | REC fades in over 6 f; the markers pop with a 2 f stagger as they're named | "recording / tracking / mapping each…" (v03 @ 0:32–0:37) | bespoke scene; **anchor** per marker |
| **P-OUTLINE-TRACE** | annotation | A neon outline (6 px, `bad` red or `accent` blue + a 14 px glow) tracing the shape of a region | Draws along its path in 18–24 f | "the whole region / every one of these" (v03 @ 0:37) | an SVG path from the target's outline |
| **P-LEADER-LABEL** | annotation | The TX-3 label + a 3 px white leader line to the part | The line draws from the part in 6 f, the label fades in over 6 f | Naming one or two parts in a still or a slow shot (v03 @ 0:51 "HEMOGLOBIN 6.5NM") | HTML + SVG; **anchor** |

**Type (B-7)**
| ID | Type | On screen | Motion | When | Engine / needs |
|---|---|---|---|---|---|
| **P-KW-CHIP** | overlay | The §5.2 lime chip with the term (≤ 3 words) | Types one letter per 2 f, the box growing with it; or pops in 7 f | A term or number the viewer must keep ("250 NANOMETERS", v03 @ 0:09) | `kind: "chip"`; near the anchor |
| **P-KW-WORD** | overlay | The TX-1 typed lime word on the footage, no box | Types one letter per 2 f with a white glow flare (24 px blur, fading over 4 f) on the newest letter (v02 @ 0:04.3–4.8); holds to the cut | A new named thing the shot shows ("GEOGLYPHS", v02 @ 0:04) | `kind: "chip"`; the text from `VEOS.fx.typewriter(word, lt, {at, cps: 15, flare: {color: "#FFFFFF", px: 24, frames: 4}})` |
| **P-ALERT-CHIP** | overlay | The chip in `bad` red with white text and a 4 px `edge` stroke | As P-KW-CHIP | A hazard term, or any chip over green or yellow footage (v02 @ 0:11 "LiDAR") | `kind: "chip"`, roles [bad] |
| **P-TITLE-PLATE** | overlay | The §5.2 two-line lime title + the white sub-line | Types line by line; the sub-line rises | Naming a people, place, era or mission with a date range (v02 @ 0:26–0:28) | `kind: "plate"` |
| **P-HERO-NUMBER** | overlay | The TX-5 lime number, the other unit beneath, a white bracket | Static text revealed by the scene's P-LAND pull-back (no count, v01 @ 0:56.6–58.3); on screen as the number is said | The payoff number, or the biggest number in the reel (v01 @ 0:57) | `kind: "hero"`; `ctx.fmtNum` metric + imperial; `events` at the landing |

**Diagrams and scale (B-3, B-4)**
| ID | Type | On screen | Motion | When | Engine / needs |
|---|---|---|---|---|---|
| **P-VS-STACK** | stage | Two or three specimens stacked on W-grid at y ≈ 420, 820, 1180, each with a TX-2 lime label locked above it; one scale | **Conveyor scroll:** the grid scrolls up and each specimen + label rides in from below the frame (≈ 490 px in the first 5 f, ease-out, then ≈ 35 px/f), the next ≈ 10 f later, until the stack settles (v01 @ 0:06.63–0:09) | "X vs Y vs Z", the COMPARE section (v01 @ 0:07–0:09) | `fx.diagram` or a bespoke scene; one element (labels internal) |
| **P-VS-FOCUS** | state | The active specimen scales 1.25 and gets a 6 px `accent` outline panel (radius 24); the others shrink to 0.85 and dim 30 % | 10 f in-out per focus change, on the specimen's name | Walking through the stack one by one (v01 @ 0:13–0:14, 0:37–0:40) | the P-VS-STACK scene with `events` |
| **P-XRAY-SWAP** | state | The same stack turns into neon-blue outlines with white bones on W-glow | T-07 bloom flip: brighten to ≈ 80 % white over 6 f, cut to W-glow at the peak, the glow blooms down over 5 f; the labels turn white (v01 @ 0:09.93–10.27) | "inside / underneath / the skeleton / how it's built" (v01 @ 0:10) | a world flip + the diagram redrawn + the built-in `flash` transition (T-07) on the cut |
| **P-SCALE-LINEUP** | figure | 3–5 objects in size order on one ground line (W-grid), a human silhouette (1.75 m) as the reference, a dual-unit tag under each | Objects join in size order from the right, each first a pale 40 % ghost silhouette that turns solid over 8 f, ≈ 10 f apart; the lineup pulls back slowly (×1.3 → 1.0 over ≈ 1.7 s, v01 @ 0:56.6–58.3) | "smaller than / bigger than", sizes across orders of magnitude (v03 @ 0:50–0:52) | bespoke scene; `fmtNum` dual |
| **P-SCALE-PERSON** | figure | A flat white human silhouette (1.75 m) beside the created subject + P-MEASURE | The silhouette fades in over 6 f, then the bracket grows | Scale with no scale footage (FB-5) | bespoke SVG |
| **P-BLUR-VS-SHARP** | figure | The same created dot field: blurred (24 px) on top, crisp dots below | Built for P-SPLIT-REVEAL with created imagery: the crisp half wipes in from the seam | "blurry vs crisp", resolution, focus (a created stand-in for v03 @ 0:01–0:03) | bespoke canvas on W-void (`ctx.rngStable` dots) |
| **P-MECHANISM-LOOP** | figure | A 2–4 s looping flow diagram: 2–4 nodes (icons from `fx.icon`) linked by lime arrows; a dot travels the path | Nodes pop 6 f apart; the dot travels 24 f per edge; loops | How a process works when no clip shows it (FB-4) | `fx.diagram` (edges `style: arrow`, `dot: true`) |
| **P-ANALOGY-SCENE** | stage | One familiar scene held for a stretch to explain a mechanism (a stadium of lights, a crowd, a kitchen), the creator's footage or created | Its own cuts and marks keep landing (REC HUD, arrows, ? swarm, whiteout), so it never sits | "Imagine you're…" (v03 @ 0:17–0:38). One analogy carries a reel: it's the mechanism's whole explanation, not a decoration | `events` on every new mark |
| **P-MAP-SCHEMATIC** | figure | A created flat map: land `#2A2B34`, water `#060A2C`, a white 3 px coastline, the place name set in type; P-MAP-PIN on it | P-PLACE-DOLLY on it | A place with no map footage (FB-4) | bespoke canvas; generic shapes only (a real map, the creator's or fetched, goes in P-FIGURE-CARD / P-PLACE-DOLLY instead) |

**Paper and source (B-5)**
| ID | Type | On screen | Motion | When | Engine / needs |
|---|---|---|---|---|---|
| **P-PAPER-HILITE** | overlay | The paper or article page on W-paper (the creator's screenshot, else the real page captured with `veos capture`, else a created headline card); a lime highlighter sweeps over the exact spoken phrase | **P-LAND from ×3.5 on the headline to the full page in 10 f** (expo-out, v02 @ 0:06.63–7.0; ×3.0 in `fx.clip`), then holds dead still; the highlight wipes left → right at 0.5 s per span, starting on the phrase's first word | "a study / paper / report found…" (v02 @ 0:07–0:09) | `fx.shot({asset, highlights})` or `fx.headlineCard({masthead, date, headline, highlight, hlRole:"primary"})`; the source noted |
| **P-QUOTE-HILITE** | overlay | A pull-quote paragraph on W-paper (Source Serif 4), the spoken sentence highlighted lime | The paragraph fades in, then the highlight wipes as it's read | A researcher's quote read aloud (v02 @ 0:32–0:34) | `fx.quoteCard` / `fx.shot`; word for word |
| **P-FIGURE-CARD** | overlay | A paper figure (map, chart, micrograph) on W-paper, pushed in on the region named | Push 1.00 → 1.15 toward the region over the shot; a P-LIME-ARROW or ring on the region | "over this area", a figure from the paper (v02 @ 0:13) | `fx.shot({asset})`; the creator's file, else the paper's real figure fetched (else P-MAP-SCHEMATIC / P-MECHANISM-LOOP) |

**CTA (B-9)**
| ID | Type | On screen | Motion | When | Engine / needs |
|---|---|---|---|---|---|
| **P-SUBSCRIBE-TAP** | overlay | The §6.7 sticker + the hand cursor | Rises 28 px + fades in over 6 f, the cursor in over 8 f at +0.9 s, the tap 8 f later with sparks; rides across cuts; fades out over 30 f | S1, S2, S3 | bespoke scene `kind: "cta-sticker"`, z8, `events` at the tap |
| **P-KEYWORD-TAP** | overlay | The same button reading "COMMENT [KEYWORD]" (the width grows to fit, max 760) | As P-SUBSCRIBE-TAP; holds ≥ 1.5 s | S3 when the CTA is a comment keyword | `kind: "cta-keyword"` |
| **P-CLIFFHANGER** | stage | The next question's teaser: a dark silhouette of the next subject or a ? swarm over a hero number; then S3 and the closing flash | §6.7 | The last few seconds of every reel | scenes + G-3 |

### 8.4 Line → pattern lookup
Vocabulary, not a decision table: it tells you what this style reaches for. Ask what the viewer should see on the trigger
word, then use it, or invent something in this style's language.

| Line type (what the voice says) | Primary | Alternates | Created substitute (nothing real found) |
|---|---|---|---|
| Opening subject ("this animal / chip / can") | P-HOST-FLASH → P-BROLL-FULL | — | P-SCALE-PERSON on W-grid |
| How big / tall / long / heavy | P-MEASURE | P-DIM-LABEL, P-HERO-NUMBER | P-SCALE-PERSON, P-SCALE-LINEUP |
| An exact size of a part | P-DIM-LABEL | P-LEADER-LABEL | — |
| "This part / here / its wing" | P-LIME-ARROW | P-ARROW-HOP, P-HAND-ARROW | an arrow on a created diagram |
| Two matching parts | P-PINCER-ARROWS | two P-LIME-ARROWs | — |
| A new term | P-KW-WORD | P-KW-CHIP | a chip on W-grid |
| A number to keep | P-KW-CHIP | P-HERO-NUMBER | — |
| A hazard / limit | P-ALERT-CHIP | P-OUTLINE-TRACE (red) | — |
| "X vs Y vs Z" | P-VS-STACK → P-VS-FOCUS | two clips in sequence, the same framing | P-VS-STACK with created specimens |
| "Inside / underneath / built like" | P-XRAY-SWAP | P-STATE-SWAP | P-XRAY-SWAP |
| "The difference between this and this" | P-SPLIT-REVEAL | P-STATE-SWAP | P-BLUR-VS-SHARP |
| "Where" / a place | P-PLACE-DOLLY + P-MAP-PIN | P-FIGURE-CARD | P-MAP-SCHEMATIC + P-MAP-PIN |
| "A study / paper found" | P-PAPER-HILITE | P-FIGURE-CARD | `fx.headlineCard` |
| A quote from a researcher | P-QUOTE-HILITE | — | `fx.quoteCard` |
| "Imagine…" (an analogy) | P-ANALOGY-SCENE | P-MECHANISM-LOOP | P-MECHANISM-LOOP |
| How a process works | P-BROLL-FULL sequence + P-ARROW-HOP | P-MECHANISM-LOOP | P-MECHANISM-LOOP |
| "Through the lens / microscope" | P-LENS-IRIS | P-SNAP-PUSH | P-LENS-IRIS on a created image |
| "Recording / tracking each one" | P-REC-HUD | P-OUTLINE-TRACE | — |
| "Blinding / glare / all you'd see" | P-WHITEOUT | — | — |
| "Nobody knows / what is…?" | P-QMARK-SWARM | — | — |
| A people / era / mission name | P-TITLE-PLATE | P-KW-CHIP | — |
| "Look at / watch this" | P-SNAP-PUSH (the thing within a second) | P-LIME-ARROW | — |
| A summary of what was just shown | P-RECAP-RUN | — | — |
| A reaction ("so many more!") | P-HOST-DROPIN | — | — |
| The next question | P-CLIFFHANGER | — | — |
| "Subscribe / follow" | P-SUBSCRIBE-TAP + P-HOST-CLOSE | P-KEYWORD-TAP | — |

For example, the same vocabulary in tech: "each transistor is 5 nanometres wide" → P-KW-CHIP "5 NANOMETRES" + a
P-SCALE-LINEUP (hair → cell → virus → transistor); "the cable runs 6,600 km across the Atlantic" → P-PLACE-DOLLY +
P-DIM-LABEL "6,600 KM / 4,101 MI"; "the model predicts the next word" → P-MECHANISM-LOOP.

### 8.5 Data and truth
- Every number on screen is said in the script, or shown in the real source page. The style states
  numbers; it doesn't compute them: a reel whose script needs a calculation shows P-HERO-NUMBER on the stated result only.
- **Same axes.** P-VS-STACK and P-SCALE-LINEUP draw everything at one scale; when the sizes span more than 100×, they say
  so with a break mark (two slanted white lines) and a tag per object.
- **Illustrations** (a created silhouette, a schematic map, a dot field, a created specimen) may look realistic; they carry
  no labels and no numbers except script-stated ones.
- **CG and artist's impressions** (the creator's, or the real ones fetched) are shown as given.
- **No comedy layer:** no stickers, stamps, meme sounds or freeze-frame roasts, in any reel.

### 8.6 The ink layer and anchors
| Mark | Stroke / shape | Colour | Draw-on | Life |
|---|---|---|---|---|
| **Block arrow** (P-LIME-ARROW, P-ARROW-HOP) | A filled chunky arrow ≈ 210 × 150 px, the shaft 40 % of the head's width; 6 px `edge` outline; hard shadow 0/+6 | `primary` | pops on in 1 f, nudges 20 px in over 6 f | holds; glides along the part over 1.5–2.5 s when the line follows it |
| **Marker arrow** (P-PINCER-ARROWS) | A curved stroke 16–24 px wide, round caps, a filled 56 px head; 4 px `edge` outline | `primary` | shaft 8 f, head 2 f | holds |
| **Hand arrow** (P-HAND-ARROW) | A curved stroke 20 px, round caps, an open head | `accent` | shaft 10 f, head 2 f | holds |
| **Measure bracket** (P-MEASURE) | An 8 px line, a 56 px flat foot cap, a top arrowhead | `paper` | grows 13 f from the ground, from the cut frame | holds |
| **Dimension arrow** (P-DIM-LABEL) | A 6 px two-headed line + the TX-4 tag | `paper` + a `primary` tag | grows over 22 f; the tag's number rolls with the length | holds |
| **Pin + ripple** (P-MAP-PIN) | A 64 × 88 px pin, `edge` outline; a 4 px ripple ring | `primary` | grows from its tip over 8 f; the ripple 18 f, repeated once | holds |
| **? marks** (P-QMARK-SWARM) | Montserrat 900 glyphs 72–110 px, 5 px `edge` stroke | `primary` | pop, 3 f stagger | wobble ±6° every 20 f |
| **Trace** (P-OUTLINE-TRACE) | A 6 px line + a 14 px glow along the region's outline | `bad` or `accent` | 18–24 f along the path | holds |
| **Leader line** (P-LEADER-LABEL) | 3 px | `paper` | 6 f from the part | holds |
| **Highlighter** (P-PAPER-HILITE) | A lime bar behind the words, 0.9 × the line height | `primary` | 0.5 s per span, left → right | holds |

**How the marks behave.** A mark sits on the thing being named, lands on its word, finishes drawing before the next cut
and leaves with it (0 f). One mark is the usual; a second arrives when the line names a second thing; three is the most
the eye can follow. When two marks point at nearby targets they come from opposite sides (P-PINCER-ARROWS). Marks stay
off faces and out of the caption and sticker bands.

**Anchors: the mark on the exact pixel.** Every arrow, bracket, pin, trace, leader line and chip that refers to something
inside a clip is anchored to it.
- **Targets:** a part in the clip ("the wing joint", "the stack top"), a region, or a pair of points for brackets and
  dimension arrows. A face is rarely the thing named; when it is, point from beside it.
- **Static** when the target moves less than 40 px over the mark's life: one position, read off a still of the clip after
  the full-bleed crop and the land.
- **Tracked** when it moves: a track on the clip (`veos track --clip <asset>`, SCENES-API §13), and the mark's
  scene gets `anchor: {track, point, offset, place, clip_t0}` so it rides the target frame by frame. Look at the track's
  preview before you trust it.
- **Placement:** the arrow's tip sits 24 px outside the target's edge, pointing in; the arrow's body lies outside the
  target and outside the caption and sticker bands, and keeps about 40 px clear of a face. On every frame the mark stays
  within 40 px of its target.

### 8.7 Sources
- **No credit or source lines on screen, anywhere.** Real editing doesn't caption its footage with where it came from: a
  borrowed or fetched clip is shown clean, like the creator's own; where it came from is noted in the project
  (`veos asset add --source`), not in the picture. Made-up or recreated pictures carry no credit and no label either.
- **Source cards (P-PAPER-HILITE):** when the line is "a study found…", the page itself is the picture: the creator's
  screenshot, else the real page captured from the web (`fx.shot`), else a created `fx.headlineCard` with the outlet set
  in type, the date and the exact headline; the
  spoken spans swept in lime; the body text is decorative, the highlighted span readable.
- Headlines and quotes are word for word; one card per claim. A claim with no source is shown with footage only (no
  card), and you tell the creator when you show the storyboard.

### 8.8 Assets
- **The creator's own or held footage first,** then the real thing fetched from the web. One clip per sentence; the clip
  must show the named thing.
- **Created visuals** (diagrams, schematic maps, silhouettes, scale lineups) are generic shapes: no traced brand logos or
  real UIs.
- **Logos:** a brand or institution named on screen gets its real logo (the creator's file, else fetched); `fx.logoPlate`
  (the name set in type) only when none can be found.
- **Third-party moments:** fetch the real thing (§12.4).

---

## §9 Transition system

### 9.1 Library
| ID | Transition | Frames | Recipe | Sound |
|---|---|---|---|---|
| **T-01** | Caption-beat cut | 0 | A hard cut on the caption swap frame (±1 f of the word boundary). The language of the style: ≈ 85 % of the reference's boundaries | none, except the hook cut |
| **T-02** | Seam wipe | 8–10 | Image B draws downward from a horizontal seam (y 760) with a 2 px white edge line that fades after | a soft swish |
| **T-03** | Whiteout | 18 + 3–6 + 15 | Ease-in to ≈ 95 % white in 18 f, hold, recede to ≈ 60 % in 15 f (P-WHITEOUT: the built-in `flash`, `pre: 18`, `peak: 0.95`, over a 0.6 white veil) | a rising shimmer |
| **T-04** | State swap | 0 | The same framing, another render (P-STATE-SWAP); the marks persist | a tick / click |
| **T-05** | Lens iris | 12–14 | A circle opens from r 0 to 430 px with a tick ring (P-LENS-IRIS) | a soft whoosh |
| **T-06** | Place dolly | 21 | Push 1.0 → 1.5 with a −15° roll into a map or aerial, then T-01 to the close-up (P-PLACE-DOLLY) | an air whoosh |
| **T-07** | Bloom flip | 6 + 5 | Brighten W-grid to ≈ 80 % white in 6 f, cut to W-glow at the peak, the bloom decays over 5 f (P-XRAY-SWAP): built-in `{"t": <cut>, "type": "flash", "colour": "#FFFFFF", "peak": 0.8, "pre": 6, "frames": 11}` | a digital sweep |
| **T-08** | Punch-in cut | 0 | The same image ×2.0–2.5 on the detail on the next frame (P-SNAP-PUSH) | a zoom tick |
| **T-09** | Recap run | 0 × 3–4 | Hard cuts every 0.4–0.6 s through shots already seen (P-RECAP-RUN) | none |

### 9.2 Grammar
| Boundary | Use | Never |
|---|---|---|
| f0 | The host flash already moving | A fade-in, a title |
| Creator → subject (hook) | T-01 on the word boundary (G-1) | A dissolve, a zoom |
| Clip → clip | T-01 on the caption beat | A dissolve, a whip |
| Same subject, new render | T-04 | T-01 to a different angle |
| A → B comparison image | T-02 | A side-by-side split |
| Into a place | T-06 | T-01 straight to the close-up (it loses the "where") |
| Diagram → inside view | T-07 | — |
| Through a lens | T-05 | — |
| Glare, blinding light | T-03 | — |
| Back to the creator | T-01 (G-2 / G-3) | A morph, a PiP |
| A summary line ("revealing…", the CTA line) | T-09 recap run of 3–4 earlier shots | New footage with no source |
| The last word | A hard end ≤ 6 f after it | An end card, a black tail |

### 9.3 Cut rules
- **R-1** Cut on the caption beat (±1 f), never mid-word.
- **R-2** Cut on the motion beat when a clip has one inside the sentence (a wingbeat, a pour, a flash).

### 9.4 How the moves breathe
The plain cut is the style: it keeps the conveyor running and makes every picture feel like it arrived on the word. The
other moves are meanings, not decorations: the seam wipe *is* "this and this", the dolly *is* "where", the iris *is* "through
the lens", the bloom flip *is* "inside", the whiteout *is* the glare. Use each whenever the script says its thing, as often
as it says it, and let a run of plain cuts sit between them so each special move reads as an event. Vary the kind from one
special move to the next.

---

## §10 Motion tokens, camera, layers, finishing

### 10.1 Motion tokens (30 fps)
| Token | Value |
|---|---|
| Beat lead | the picture 2 f before the trigger word; marks land within ±5 f |
| Entries | `cubic-bezier(0.22, 1, 0.36, 1)` (expo-out), 6–10 f |
| Exits (mid-shot) | `cubic-bezier(0.64, 0, 0.78, 0)`, 4 f |
| Arrows, pins, stickers | back-out `cubic-bezier(0.34, 1.56, 0.64, 1)`, 7–8 f; pop overshoot 0.08 |
| Exits | marks, chips and labels leave **with the cut** (0 f); the sticker fades over 30 f; a chip leaving mid-shot fades over 4 f |
| Arrow land | pops on in 1 f, 6 f after the cut; nudges 20 px toward the target over 6 f, ease-out; then holds (no bob) |
| Arrow glide | 1.5–2.5 s along the part, sine in-out; a hop to an unrelated part 8 f in-out |
| Land (P-LAND) | footage ×1.12–1.2 (×1.13 over 16 f), stills ×1.8 over 10 f, pages ×3.0 over 10 f (measured up to ×3.7; `fx.clip` caps at 3.0) → 1.0, expo-out, from the cut frame: `fx.clip({land: {from, frames}})` |
| Bracket grow | 13 f ease-out, from the cut frame |
| Pin grow | from its tip over 8 f, no drop; ripple r 0 → 90 px over 18 f |
| Chip type-on | one letter per 2 f + a white flare on the newest letter (`fx.typewriter` `cps: 15`, `flare: {color: "#FFFFFF", px: 24, frames: 4}`); pop 7 f (0.6 → 1.08 → 1.0) |
| Hand arrow | shaft 10 f (dashoffset), head 2 f |
| Slow push | none on moving clips (their own ≈ 1 %/s move is enough); locked-off clips 1.00 → 1.03; stills hold after P-LAND |
| Snap push | a 0 f punch-in cut to ×2.46 (range ×2.0–2.5; ×1.6 at most on a 1080p source) |
| Number roll | 18 f ease-out, landing on the spoken number ±5 f (the dimension tag rolls with its 22 f arrow) |
| Sticker | rise 28 px + fade in over 6 f; the cursor in over 8 f at +0.9 s; the tap 8 f later; fade out over 30 f; 2.2–2.6 s in all; S3 enters 1.1–1.7 s before the end |
| Hold | text ≥ 0.25 s per word; chips ≥ 10 f after typing ends |

### 10.2 Footage camera (`zoom_policy: none`)
No camera presets on the creator's footage: the handheld selfie moves on its own and the flashes are too short. All land,
punch and dolly motion is scene-level on the B-roll (P-LAND, P-SNAP-PUSH, P-PLACE-DOLLY), one move at a time.
**Measured: no shake, no rotation, no whip anywhere** (16 full-frame-rate bursts: the host flashes move ≤ 0.3 % in scale
per frame; the B-roll moves are the clips' own); the only roll is the place dolly's. The canvas camera stays off: the
pushes live inside the scenes.

### 10.3 Layer order (back to front)
| z | Layer |
|---|---|
| 1 | The B-roll clip or still full-bleed (P-BROLL-FULL, P-STILL-PUSH, the P-BAND-CLIP blur copy), or the world (W-grid, W-glow, W-paper, W-void) |
| 2 | The band clip (P-BAND-CLIP), the whiteout veil, glow |
| 3 | Diagrams, paper cards, scale scenes |
| 4 | The creator's footage on L-host |
| 5 | Chips, typed keywords, plates, hero numbers, leader labels, dimension tags |
| 6 | Ink: arrows, brackets, pins, ? marks, traces |
| 7 | CS-1 captions |
| 8 | The CTA sticker + cursor |

### 10.4 Finishing
- No grain. No vignette on footage; W-grid (0.22) and W-glow (0.35) carry their own.
- Glow only on the W-glow outlines (`accent`, 14–18 px) and P-OUTLINE-TRACE.
- Footage is never regraded; match only exposure between the creator's takes.
- Hard shadows (0/+6–8 px, no blur) only on lime elements and the sticker. Captions use their 2 px stroke + the 0/+3
  shadow.

---

## §11 Sound

Wonder is quiet. The voice carries the reel; sound marks a landing. (The reference reels' sound couldn't be measured, so
this is a decision, not a measurement.)
| Line | Direction |
|---|---|
| **Where sound goes** | The hook (the G-1 cut and the first mark landing); reveals (a chip, plate, hero number, pin or bracket landing, when the landing is the point of the line); the non-cut transitions (T-02, T-03, T-05, T-06, T-07, T-08); the sticker tap click. Plain T-01 cuts are silent. No list cue. Sparse: if in doubt, leave it out |
| **Meme sounds** | None |
| **The bed** | On from f0, curious, light, mid-tempo, ≥ 18 dB under the voice; it may drop out for up to 0.6 s before the payoff number |
| **Ducking** | The bed sits 18 dB under the voice while it speaks; a creator clip's own audio is muted unless it's the point (an animal call, a machine noise), then 12 dB or more under the voice |
| **Loudness** | −14 LUFS integrated, true peak ≤ −1.5 dBTP; a hard end ≤ 6 f after the last word |

---

## §12 Footage handling

### 12.1 Setup
| Setup | Spec |
|---|---|
| **A: Handheld selfie** | The phone's front camera at arm's length, 9:16, 1080 × 1920 or better, 30 fps; eye level or slightly above; head top at y 180–420, the face 22–34 % of the frame's height; a home office behind (a shelf, a plant, a lamp), a soft window key from the side; one saturated wardrobe colour (blue, red, green); hands in frame: every line gets an open-hand gesture toward the lens. Mic: a clip-on or the phone, the room quiet (this audio is the voice-over) |

### 12.2 Shots and fallbacks
| ID | Shot | Spec | Must | Without it |
|---|---|---|---|---|
| **SH-1** | Narration take | The whole script on setup A, one to three takes, read with energy; its audio is the voice-over | **must** | **FB-1** none: the selfie narration is both the voice and the flashes. Ask the creator to record it (one phone take, ≈ 3 minutes); the reel can't be made in this style without it |
| **SH-2** | Opening flash | The first 2–3 words with a big open-hand gesture (a wave or a reach), three takes | **must** | **FB-2** the first 2–3 words of the SH-1 take become the flash: a weaker gesture at f0, but it holds |
| **SH-3** | Reaction drop-ins | The loop line and the payoff line performed big (eyes wide, a hand to the head) | optional | **FB-3** the SH-1 line with the most energy becomes the drop-in: a less performed reaction, but it holds |
| **SH-4** | Subject B-roll | A clip of the exact thing named, one per sentence, 2–6 s each, vertical or 16:9 ≥ 1080 px tall, the creator's own or held (their shots, licensed stock in their account, CG they commissioned, captures of their own simulations) | **must** | **FB-4** per missing sentence: the real thing fetched from the web (a photo with P-LAND, a clip, the paper's figure); when nothing real turns up, a created visual: P-VS-STACK, P-SCALE-LINEUP, P-SCALE-PERSON, P-MECHANISM-LOOP, P-BLUR-VS-SHARP, P-MAP-SCHEMATIC, or a headline / quote card. Built beats lose real-world footage and read as a diagram explainer: it holds while about half the runtime or more is still real pictures, degrades below that, and when real footage falls under about a fifth, tell the creator the style isn't working for this reel |
| **SH-5** | Scale reference | The subject next to a person or a known object | optional | **FB-5** P-SCALE-PERSON + P-MEASURE beside the created subject on W-grid: no photographic scale, but it holds |
| **SH-6** | Source screenshots | The paper, article or figure page with the outlet, date and exact headline visible | optional | **FB-6** the real page captured from the web (`veos capture --selector` on the headline); when it can't be found, `fx.headlineCard` / `fx.quoteCard` with the exact words: no real page, but it holds |
| **SH-7** | Stills | Photos, renders, figure images ≥ 1500 px tall | optional | **FB-7** the real one fetched from the web; else a created diagram, or the nearest SH-4 clip with its slow push (P-BROLL-FULL): less literal (degraded) |

### 12.3 Props, reactions and resolution
- **Props:** none required. A physical prop for a scale shot (a ruler, a coin, a can) makes SH-5 easy.
- **Reactions worth recording at the shoot** (2 s each): an open hand to the lens, a wave, an eyes-wide "so many more!", a
  frown + reach ("look at the difference"), a point down (for the S3 sticker).
- **Cut-out:** none.
- **Resolution:** vertical clips ≥ 1080 px tall go full-bleed. A 16:9 clip goes full-bleed by a centre-on-subject crop
  only when it's ≥ 1440 px tall (≤ 1.33× upscale), or ≥ 1080 px tall **and** at most 3 s **and** moving (the softness
  hides in motion); otherwise P-BAND-CLIP. A P-SNAP-PUSH at ×2.4 needs a 4K source or a still ≥ 3000 px tall; below that,
  cap the punch at ×1.6 (soft micrographs and maps may go to ×2.4, as v03 @ 0:02.46 does).

### 12.4 Third-party moments: fetch the real thing
In this style almost every borrowed picture is a clip, a photo or a paper, so this runs on every reel. When the line
names a real thing (a documentary subject, a research figure, an article, a product, a person), the viewer should see the
real one.
1. **The creator's own files** in their folder come first (the B-roll bank).
2. **Otherwise search the web and fetch it:** the real photo or clip of the subject, the paper's own figure, the article
   page (captured and framed on the headline). Note where each came from (`veos asset add --source`); the picture itself
   carries no source line.
3. **Use it as it is** (crop, land, annotate), never altered to say something else; a headline or quote word for word.
4. **Nothing usable to be found:** build it from the script's words, with no labels and no credit lines: the FB-4 diagram
   set, `fx.headlineCard` (the outlet set in type, the exact headline), `fx.quoteCard` (word for word), `fx.silhouette` (a
   person), `fx.logoPlate` (a product or institution).

### 12.5 Frame rate and audio
Output 1080 × 1920, 30 fps CFR, BT.709. The voice chain on the SH-1 audio: high-pass 80 Hz, de-ess, light compression,
−14 LUFS.

---

## §13 What your plan should settle

Your `ideas.md` is a page or two, for you. In this style it has decided, before any code:
1. **The B-roll match:** every sentence → its clip and span (the creator's, fetched, or the created visual and which
   fallback), its trigger word, and how much of the reel is real footage.
2. **The hook:** the HA-10 variant (or HA-13 / HA-14 and why), the flash line + claim chunk with two alternates, the
   subject shot, the first mark and its frame.
3. **The flashes:** the f0 flash's cut frame, every drop-in with the reaction that earns it, the closing flash.
4. **Every mark:** its target, static or tracked (the track id), the side it comes from, the frame it lands on.
5. **Every number** in both units, each one spoken (and its hedge kept).
6. **The inserts:** the creator's, fetched (with the source), or rebuilt.
7. **The stickers:** S1, S2, S3 times and the cliffhanger's question.
8. **The transitions and the sound:** the special moves and what each one means; the few cues.
9. **The moments you'll look at hardest on the storyboard:** f0 (the host flash), 0.7 s (the subject with its bracket or
   pin), one arrow beat (the tip on the target), one diagram beat, the payoff, and S3 on the closing flash (the sticker
   below the chin, the caption on the chest, the face clear).

---

## §14 Worked examples

Times are planning estimates: take the real ones from the words. Numbers are each script's own (spoken); a real reel
shows only what its script says. Together they cover the three HA-10 variants. They show the standard; match it, then
beat it.

### 14.1 Food and health science: "This is how much sugar is in one can" (HA-10.S, 46 s)
**Clips the creator has:** the selfie take; a can on a kitchen counter (vertical); sugar cubes being stacked (vertical); a
spoon of sugar pouring (16:9, 4K); a 2 s macro of a soda pour; a screenshot of a health agency's guideline page; no liver
or insulin footage.

| t (s) | Spoken | Tone | Visual | Caption | Layout | Sound |
|---|---|---|---|---|---|---|
| 0.00 | "This can…" | awe | P-HOST-FLASH: the creator waving the can at the lens | "THIS CAN" | L-host | — |
| 0.57 | "…has more sugar than you'd ever put in your coffee," | awe | G-1 cut to the can beside a stack of 9 sugar cubes (P-BROLL-FULL, P-LAND ×1.13); P-MEASURE grows up the stack 0.63–1.43 | "HAS MORE SUGAR THAN YOU'D" → (1.30) "EVER PUT IN YOUR COFFEE," | L-evidence | the hook cut; the bracket topping out |
| 1.95 | "thirty-five grams," | awe | P-SNAP-PUSH ×1.35 on the stack (event 1.95); P-HERO-NUMBER "35 G" / "1.2 OZ" revealed by its land at 2.05, fully on as "grams" is said (2.40) | "THIRTY-FIVE GRAMS," | | the hero landing |
| 2.95 | "about nine sugar cubes," | explain | Cut to the cubes falling into a glass (P-BROLL-FULL); P-LIME-ARROW lands on the cubes at 3.10 | "ABOUT NINE SUGAR CUBES," | | — |
| 4.30 | "and your body handles it in a really sneaky way!" | hype | P-HOST-DROPIN (1.8 s), eyes wide | "AND YOUR BODY HANDLES IT" → "IN A REALLY SNEAKY WAY!" | L-host | — |

In three seconds the viewer has seen the can, watched it measured, read the number and seen the cubes fall: dense in time,
one thing at a time.

| Section | Span | Spoken gist | Patterns |
|---|---|---|---|
| COMPARE | 6.1–13.5 | "A can, a doughnut and a bowl of fruit can have similar sugar…" | P-VS-STACK on W-grid: CAN / DOUGHNUT / FRUIT BOWL (created specimens: flat illustrations) → P-VS-FOCUS on CAN as it's named → P-XRAY-SWAP to W-glow: each turns into a neon outline with its sugar as stacked cubes inside (one scale) |
| MECHANISM-1 | 13.5–21.0 | "Liquid sugar hits your blood fast…" | The pour macro (P-BROLL-FULL) + P-KW-WORD "GLUCOSE"; the S1 sticker at 17.2 over the pour; P-MECHANISM-LOOP (gut → blood → liver, a dot travelling) because there's no organ footage (FB-4) |
| MECHANISM-2 | 21.0–30.5 | "Your liver turns the extra into fat…" | P-MECHANISM-LOOP continues with the liver node lit; P-ALERT-CHIP "FAT STORAGE" over the liver node |
| MECHANISM-3 | 30.5–37.5 | "Guidelines say about 25 grams a day for most adults…" | The creator's screenshot of the guideline page: P-PAPER-HILITE on the exact sentence (the agency's name is on the page itself); the S2 sticker at 33.8 |
| PAYOFF | 37.5–41.5 | "One can is already over the line." | P-SCALE-LINEUP: the 25 g line vs the 35 g stack, one ground line, "25 G / 0.9 OZ" and "35 G / 1.2 OZ" tags; no ✓ (it's a warning): the 35 g stack's top glows `bad` |
| CLIFFHANGER | 41.5–46.0 | "But the drink with the most hidden sugar isn't soda… to find out which, follow!" | Dark silhouettes of 3 bottles + P-QMARK-SWARM; S3 "FOLLOW" rises in at 44.3 over the silhouettes; P-HOST-CLOSE 44.9–46.0 pointing down at it |

The creator is on screen three times: the flash, the "sneaky way!" drop-in, the close. Inserts: the guideline page (the
creator's screenshot); the organ path is created (P-MECHANISM-LOOP, no label: a diagram, not a reconstruction).

### 14.2 Tech: "Why your phone can see in the dark" (HA-10.D, 50 s)
**Clips:** the selfie take; the creator's own night photo taken twice (normal mode, night mode); a screen recording of the
camera app; a 4K tripod time-lapse of a dark street; a macro of the phone's camera lens; no sensor footage.

| t (s) | Spoken | Tone | Visual | Caption | Layout | Sound |
|---|---|---|---|---|---|---|
| 0.00 | "Look at the difference…" | awe | P-HOST-FLASH: a frown, reaching toward the lens | "LOOK AT THE DIFFERENCE" | L-host | — |
| 0.60 | "between this…" | awe | G-1 cut to W-void: the normal-mode photo in the top half (y 260–760, P-LAND ×1.8); a P-LIME-ARROW lands on its noisy shadows at 0.90 | "BETWEEN THIS…" | L-evidence | the hook cut |
| 1.30 | "…and this!" | awe | T-02 seam wipe: the night-mode photo draws in below (9 f) | "AND THIS!" | | the seam swish |
| 2.20 | "Same phone, same street, same second." | explain | P-SNAP-PUSH ×1.35 on the seam (the 1080p photos cap the punch) | "SAME PHONE, SAME STREET," → (2.90) "SAME SECOND." | | — |
| 3.60 | "The trick is that it never takes just one photo," | explain | P-HAND-ARROW (accent) draws from the top photo into the bottom one | "THE TRICK IS THAT IT NEVER" → "TAKES JUST ONE PHOTO," | | the arrow draw |
| 5.40 | "and that changes everything!" | hype | P-HOST-DROPIN 1.6 s | "AND THAT CHANGES EVERYTHING!" | L-host | — |

| Section | Span | Spoken gist | Patterns |
|---|---|---|---|
| COMPARE | 7.0–15.0 | "A normal photo grabs light for a fraction of a second; night mode grabs many" | P-SCALE-LINEUP turned into time: one frame tile vs a row of 12 frame tiles on W-grid (created), no units (it's time); P-KW-CHIP "12 FRAMES" (spoken) |
| MECHANISM-1 | 15.0–23.5 | "Each frame is noisy, but the noise is random…" | A created dot-field P-BLUR-VS-SHARP: 12 noisy layers stacking into a clean one (each layer a seeded dot field); the S1 sticker at 18.4 |
| MECHANISM-2 | 23.5–32.0 | "So the phone lines them up and averages them…" | The creator's camera-app screen recording (P-BAND-CLIP: 16:9 at 1080p, 5 s) + P-LEADER-LABEL on the shutter's progress ring "HOLD STILL" |
| MECHANISM-3 | 32.0–40.0 | "…and a model guesses the colours the sensor missed." | The lens macro (P-BROLL-FULL) + P-LENS-IRIS into the created sensor grid (W-void), P-OUTLINE-TRACE (accent) around one pixel group; the S2 sticker at 34.9 |
| PAYOFF | 40.0–45.0 | "That's how a tiny lens sees what your eyes can't." | Back to the split: P-SPLIT-REVEAL replayed + a `good` ✓ chip "NIGHT MODE" |
| CLIFFHANGER | 45.0–50.0 | "But some phones can see through fog… to see how, subscribe!" | The street time-lapse darkened to a silhouette + P-QMARK-SWARM; S3 "SUBSCRIBE" at 48.2; P-HOST-CLOSE 48.8–50.0 |

### 14.3 Tech: "Where your photos actually live" (HA-10.P, 40 s)
**Clips:** the selfie take; an aerial drone clip of a data-centre campus (licensed in the creator's stock
account); a server-rack walk-through (the creator's own visit); a still of a cooling tower; no map
footage.

| t (s) | Spoken | Tone | Visual | Caption | Layout | Sound |
|---|---|---|---|---|---|---|
| 0.00 | "Your photos live here…" | awe | P-HOST-FLASH: the creator pointing down at the phone | "YOUR PHOTOS LIVE HERE…" | L-host | — |
| 0.58 | "…in a building you've never heard of," | awe | G-1 cut to P-MAP-SCHEMATIC (created: no map footage), the region's name in type, P-PLACE-DOLLY 1.0 → 1.5 + the roll; P-MAP-PIN grows at 0.75 + its ripple | "IN A BUILDING YOU'VE" → "NEVER HEARD OF," | L-diagram | the hook cut; the pin |
| 1.75 | "as long as ten football fields." | awe | Cut to the aerial clip; P-DIM-LABEL along the roof, rolling to "1,000 M" / "3,281 FT" (the script's number) | "AS LONG AS TEN FOOTBALL FIELDS." | L-evidence | the tag landing |
| 3.40 | "Inside, it's loud, hot and full of blinking lights" | explain | Cut to the rack walk-through; P-LIME-ARROW on a blinking rack (tracked: the camera walks) | "INSIDE, IT'S LOUD, HOT" → "AND FULL OF BLINKING LIGHTS" | | — |
| 5.20 | "and it never, ever turns off!" | hype | P-HOST-DROPIN 1.7 s | "AND IT NEVER, EVER TURNS OFF!" | L-host | — |

| Section | Span | Spoken gist | Patterns |
|---|---|---|---|
| COMPARE | 6.9–12.5 | "Your phone holds about a thousand photos; this building holds billions" | P-SCALE-LINEUP: a phone silhouette → a shelf → the building, each with its photo-count chip (spoken) |
| MECHANISM-1 | 12.5–20.0 | "Every photo is copied to at least three places" | P-MAP-SCHEMATIC again with 3 pins growing in sequence + P-MECHANISM-LOOP arrows between them; the S1 sticker at 15.6 |
| MECHANISM-2 | 20.0–28.5 | "and all those machines make heat" | The cooling-tower still (P-STILL-PUSH) + P-HERO-NUMBER "40 °C" / "104 °F" (spoken) + P-ALERT-CHIP "HEAT" |
| PAYOFF | 28.5–34.0 | "So the 'cloud' is really a very big, very hot room." | The aerial again, P-SNAP-PUSH ×1.35 on the roof; P-KW-WORD "THE CLOUD" |
| CLIFFHANGER | 34.0–40.0 | "But one company put theirs under the sea… to see it, subscribe!" | A dark created silhouette of a capsule on W-void + P-QMARK-SWARM; S3 at 38.4; P-HOST-CLOSE 38.9–40.0 |

A 40 s reel gets one mid-reel sticker and the last: two taps are plenty at this length.

---

## §15 Your look at the storyboard: the checklist

Watch it once as a stranger with a thumb over the next reel, then once as the editor whose name is on it. Fix what
bothers you, in one pass.

**The style (does it feel like §The feel?)**
- Frame 0: the creator mid-gesture with the first words; the subject full-frame by 0.7 s, landing, measured or pinned.
- One sentence, one picture: pause anywhere and the frame shows what the voice is saying.
- Lime is the only colour the edit adds, and every lime thing points at something.
- Sizes stand beside something familiar, in both units; the biggest number lands at the payoff with a beat of stillness.
- The creator flashes in on reactions, by hard cuts, and never lingers into a talking head.
- It never sits still and never feels random; the special moves each mean something.
- Curiosity, never comedy; the reel ends on the next question.
- Start to end: you learned something you could tell a friend, and you want the next one.

**Craft (by eye, in context)**
- On the creator's frames the face reads: the caption on the chest, the closing sticker below the chin; nothing buries
  the face or crowds the hair by accident.
- Every mark sits on its target on every frame and stays off faces.
- No text over text by accident: one chip or plate at a time; marks out of the caption and sticker bands; no sticker
  landing on a chip.
- Every picture cuts in on its trigger word and every mark lands on its word; cuts on the caption beat; nothing lingers
  after its point.
- CS-1: ALL CAPS, one line, hard swaps, one height, never coloured, readable on a phone; glossary spellings exact.
- Every number on screen is in the script, in both unit systems, with the speaker's hedge; headlines and quotes word for
  word, fetched pages included; illustrations carry no labels; no credit or source lines on screen.
- "Look at this" is paid within a second; the sticker is on screen on "SUBSCRIBE / FOLLOW"; a comment keyword readable.
- The file itself (1080 × 1920, 30 fps, −14 LUFS, a hard end ≤ 6 f after the last word, no black tail) is the render's
  job; it checks it.

---

## §16 Build notes
- **Fonts to pre-load:** Barlow Semi Condensed 700, Archivo Black, Montserrat 800 / 900, Inter Tight 600 / 700, Source
  Serif 4 400 / 700.
- **Engine built-ins this style leans on:** P-LAND = `fx.clip({land: {from, frames}})` (expo-out, no fade-up);
  P-PLACE-DOLLY = `fx.clip({kenburns, land, rotate})`; the typed-letter flare = `fx.typewriter({flare})`; T-03 whiteout and
  T-07 bloom flip = the built-in `flash` transition (the whiteout adds a static 0.6 veil for its rest glow).
- **Still bespoke:** the rolling dimension tag (P-DIM-LABEL) rolls inside its own scene (the style computes no figures),
  the block arrow, the sticker with its cursor, the conveyor stack, the lens iris.
- **Marks on moving targets** ride tracks (§8.6), never hand-written keyframes.
- Every scatter and wobble is seeded (`ctx.rngStable`), so each frame always renders the same.

---

## Appendix A. Evidence map
The full map (every element → `vNN @ m:ss`) is in `evidence.md`. Sources: the analysis `analysis/short/cleo-abram.md`, its
frame sheets for v01 (59.1 s), v02 (36.7 s) and v03 (53.7 s), a full-resolution fidelity audit and a full-frame-rate motion
completeness pass (Oct 2026).
| Element | Where |
|---|---|
| Host flash at f0, the cut to the subject at 0.58–0.67 s | v01 @ 0:00.0–0:00.67; v02 @ 0:00.0–0:00.58; v03 @ 0:00.0–0:00.62 |
| The three HA-10 reveals (scale, place, difference) | v01 @ 0:00.67–0:01.83; v02 @ 0:00.67–0:02.83; v03 @ 0:00.67–0:02.83 |
| CS-1 measured 45–47 px, cy 1518 | v01 @ 0:19, v03 @ 0:01.2 |
| Lime arrows, chips, pin, ? marks, the sticker | v01 @ 0:15–0:17; v02 @ 0:02–0:06; v03 @ 0:09–0:14 |

Not verifiable from the reels: the speech language beyond the burnt-in captions, all sound (the bed and the cues are a
decision), the CTA's spoken word on Instagram (the reference says "SUBSCRIBE!").

## Appendix B. Hook-title bank
Flash words (f0) + the claim chunk + the post title. `[SLOTS]` come from the reel's script; numbers only as the script
states them.

| # | Variant | Flash words → claim chunk | Post title | For example |
|---|---|---|---|---|
| 1 | HA-10.S | "THIS [THING]" → "IS AS BIG AS A [FAMILIAR OBJECT]," | How This [Thing] Got So Big | "THIS BUILDING" → "IS AS LONG AS TEN FOOTBALL FIELDS," |
| 2 | HA-10.S | "THIS [ANIMAL / MACHINE]" → "CAN [VERB] FASTER THAN A [FAMILIAR THING]," | How This [Thing] Could [Verb] | "THIS ANIMAL" → "WAS AS BIG AS A SCHOOL BUS," |
| 3 | HA-10.P | "THEY FOUND SOMETHING" → "HIDDEN UNDER [PLACE]…" | They Found Something Hidden Under [Place] | "THEY FOUND SOMETHING" → "HIDDEN IN THE AMAZON…" |
| 4 | HA-10.P | "EVERY [EVERYDAY THING]" → "STARTS IN [PLACE]," | Where Your [Everyday Thing] Actually Comes From | "EVERY CUP" → "STARTS IN THE MOUNTAINS," |
| 5 | HA-10.D | "LOOK AT THE DIFFERENCE" → "BETWEEN THIS…" / "AND THIS!" | This [Instrument / Technique] Is Insane | "LOOK AT THE DIFFERENCE" → "BETWEEN THIS…" |
| 6 | HA-10.D | "SAME [THING]," → "SAME [SETTING], WATCH THIS!" | Why Your [Device] Can [Surprising Ability] | "SAME PHONE," → "SAME STREET, WATCH THIS!" |
| 7 | HA-10.S | "INSIDE YOUR [BODY PART]" → "ARE [NUMBER] [THINGS]," | What's Really Inside Your [Body Part] | "INSIDE YOUR GUT" → "ARE TRILLIONS OF BACTERIA," |
| 8 | HA-13 | (action clip) "[THING] JUST [DID SOMETHING]," → the creator: "AND NOBODY EXPECTED IT!" | The Day [Thing] [Did Something] | — |
| 9 | HA-14 | (the strongest image) "THIS IS THE [SHARPEST / BIGGEST] [THING] EVER [VERBED]." | The [Sharpest / Biggest] [Thing] Ever [Verbed] | "THIS IS THE SHARPEST PICTURE OF A CELL EVER TAKEN." |
| 10 | HA-10.S | "THIS TINY [THING]" → "HOLDS MORE [X] THAN [BIG FAMILIAR THING]," | How Something This Small Holds So Much [X] | "THIS TINY CHIP" → "HOLDS MORE SWITCHES THAN…" |
