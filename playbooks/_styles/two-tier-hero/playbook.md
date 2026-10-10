# Two-Tier Hero Style Playbook (template v2)

## The feel

This reel talks like a poster. The first frame is already moving: the creator mid-gesture at their desk, a red glass and
a green glass in front of them or a photo held up to the lens, and before you've heard a full sentence a giant word slams
in behind their head, hair cutting across the letters like a magazine cover. Under their chin, the words they're saying
appear one by one, small, small, then one huge: the word you'd underline. You stop because you've read the point before
you decided to listen.

Then it never lets you settle. Every breath is cut out, and every cut changes the frame, wide then tight then wide, as if
the camera leans in on each sentence. Numbers aren't shown, they're performed: an amount rolls up behind the head and
ignites in neon on the exact syllable, zero glows red over one glass while the other counts up green. Whatever the creator
names flashes past, a halftone banknote, an inverted street, a dark glass card, and you're back on their face before
you've finished looking. The creator is the frame. The graphics stand behind them or flicker past, never in front of
their face.

Loud and quiet take turns. The hook, the money and the twist are loud: a slam, a roll, a blur-punch, a white flash. The
takeaway is quiet: wide, still, just the words on the chest, a breath before the next item. A warning turns the whole room
red and strobes. The last item carries the biggest number in the reel.

One neon per reel, and it means one thing: the number that matters to the viewer. White is the words. Red and green appear
only as a before and an after. The hierarchy is ruthless: at every moment exactly one thing is too big to miss, and it's
the thing they just said.

**The test:** shrink any frame to a thumbnail: exactly one word or number still shouts, and nothing sits in front of the
creator's face.

## What this playbook is

You're editing a desk talking-head reel of a creator who teaches careers, money, skills, tools or results, or tells a story
with numbers in it, and you have the authority to make it the most gripping reel in their niche. This playbook is the
style: how it looks, moves, sounds and thinks, pulled from five reference reels (Tharun Speaks, v01–v05), measured frame by
frame at full frame rate, then sharpened. Read it all, every time. Use it the way a great editor uses a reference: take
what fits this reel, invent when a moment needs more, and never ship a frame that breaks the feel above.

**Who it's for and what it needs.** Creators who talk to camera about things with a number or a name at their heart:
salaries, skills, tools, body results, years, a person's story. Input: one talking-head take at a desk (setup A, §12.1).
Props for the hook, their own B-roll, screens and a QR image lift it; every one is optional and has a built fallback (§12).
Real logos, headlines and pages the reel names are fetched from the web when the creator didn't supply them (§12.4).
The person cut-out (matte) is required: the heroes live behind the head. Captions follow the creator's language (English,
Hinglish or Hindi, set in their copy); heroes are English caps unless the captions are Hinglish or Hindi. Machine values
live in `tokens.json`; where this text gives a number tokens also holds, they agree.

### Style directives (non-negotiable)
| # | Directive | Where it lives |
|---|---|---|
| D1 | **The words are the graphic.** Every spoken word appears on screen, word by word, in two tiers. Graphics never replace the captions; they sit around them | §5.3 |
| D2 | **A hero behind the head by 1.7 s.** The first hero word or number lands behind the creator before 1.7 s and stays ≥ 1.5 s | §6.2, §5.2 |
| D3 | **Numbers are performed.** Every spoken amount, count, duration or year rolls, steps or slides into place on its word | §8.3 B-3, §8.5 |
| D4 | **Never static.** Live footage always moves, and something new is always arriving: a cut, a punch, a hero, an insert, the next caption word. The speech decides when | §7.5, §9.3 |
| D5 | **Concrete before abstract.** A prop, a product, a person or a card shows the thing named, on its noun (lead 2 f) | §8.4, §2 |
| D6 | **One neon per reel.** White + the reel's neon accent; red/green only as a result pair; never a third bright hue | §4 |
| D7 | **Short, stylised inserts.** A full-frame insert is a glance (measured 0.8–2.2 s), then straight back to the face; an explanation that needs longer moves into the stack with the face under it | §3.2, §8.3 P-31 |
| D8 | **Money reads the way the audience counts it.** Rupee amounts use ₹ and Indian grouping (₹1,20,000; ₹2.5 L; ₹1.2 Cr), never Rs or INR; other audiences get $ and K/M/B | §5.5 |

### Quick index
| § | What |
|---|---|
| §1 | Procedure: how to approach a reel in this style |
| §2 | Hard rules: the craft and the style's never-list |
| §3 | Worlds W-, layouts L-, stage moves G-, safe zones, the person |
| §4 | Colour, the rotating neon packs, grades and clip treatments |
| §5 | Type and captions: the hero recipes, caption profiles CS-1…CS-4, other text |
| §6 | Hook system: stopper test, HA-08 default, HA-01 / HA-07 / HA-05 alternates, hook pairs, hero writing, CTA and end cards |
| §7 | Structure and rhythm: markers SM-1…SM-4, the item ritual, open loops and the re-hook, the punch-cut pulse, the recurring motif |
| §8 | Visual system (B-roll and patterns): families B-1…B-7, patterns P-01…P-44, line → pattern lookup, data, anchors and ink, assets |
| §9 | Transition system T-01…T-12 |
| §10 | Motion tokens, camera Z-1…Z-7, tone treatment, layers, finishing |
| §11 | Sound |
| §12 | Footage handling: setups, shots and fallbacks, props, the cut-out, inserts |
| §13 | What your plan should settle |
| §14 | Worked examples (3) |
| §15 | Your look at the storyboard: the checklist |
| §16 | Build notes |
| App. A / B | Evidence map / hook-title bank |

---

## §1 Procedure: how to approach a reel in this style

You watch, listen, plan, build and look at the storyboard yourself; the edit skill has the mechanics. This style lives
or dies on a handful of decisions: which word is the hero, which word in each chunk is big, how each number is performed,
and where every cut falls. Make them in this order.

1. **Count on the cut-out.** Every hero stands behind the head, so the matte covers the whole A-roll (`matte: required`,
   so it starts right after the cut); make sure it's there before the storyboard, and look at the hair at 200% where a
   hero sits. Without a usable matte, the hero moves above the head as a P-05 lockup, clear
   of the head region by 40 px, and the plan says so.
2. **Feel the tone of every line:** `hype` · `explain` · `warn` · `win` · `cta`. The tone decides the colour, the camera
   move and the world (§10.3). Explanations go to the glass world, warnings go red, wins glow.
3. **Find the heroes.** One hook hero, one per item, and one for each moment the reel turns on: a grit word (P-01, P-02,
   P-05) for names and claims, a neon number (P-03, P-04, P-06) for every amount, count, duration or year. Write each
   hero's placement against the head (§5.2: centred behind it, split around it, or a lockup).
4. **Write the hook** (§6): pick the archetype (HA-08 by default), the prop or its fallback, and 8–10 connector + hero
   lines; pick by the stopper test (§6.1), keep two alternates.
5. **Mark the keyword of every caption chunk** (the style's own craft). Walk the chunks (1–4 words) and mark at most one
   keyword per chunk (the big tier), by this priority: (1) a number with its unit word ("₹60", "3 skills"), (2) a proper
   noun or brand ("Germany", "Instagram"), (3) the topic noun ("degree", "portfolio"), (4) a contrast verb or adjective
   ("seriously", "acquired", "messy"). Never a pronoun, article, preposition or auxiliary. The keyword is the word the
   viewer would underline: plenty of chunks carry one, plenty don't, and a run of big words in a row stops being emphasis.
   Words a hero shows at that moment are **dropped from the caption** (`captions.overrides {i, text: ""}`) so the number
   or word appears once. Force or block a keyword with `captions.overrides {i, emph: true | false}`.
6. **Plan the numbers.** Every number gets a performance (odometer, steps, ruler, slider, pin, tiles, a prop pair) and a
   figure in `plan/figures.json` (§8.5).
7. **Pick the marker and the ritual** (§7): the hub for parallel items, the spotlight stack for steps, the token carousel
   for long ranked lists, spoken ordinals inside a story.
8. **Cut it.** Jump-cut every breath, retake and pause (≥ 150 ms) on word boundaries ±1 f; change the crop on every cut;
   put an animated move on the claim and number words; land every insert on its noun with the next clip treatment (§4.4).
9. **The anchor pass.** For every prop tag, counter and hand arrow, read sampled frames of the take and write the static
   anchor point of each target per shot (§8.6).
10. **Third-party moments:** fetch the real thing (the creator's files first, then the web, source noted); rebuild from
    exact words only when nothing usable turns up (§12.4).

---

## §2 Hard rules: the craft and the style's never-list

**Craft, by eye** (judge it on the storyboard, in context, the way an editor does):
- **Keep the person clear.** People come for the face, so keep the head region (face, hair and the room above the head
  top, from the cut-out) clear of front layers when the moment is about them: captions, hero connectors and trailers, prop
  tags, hand tags, chips, cards and arrows sit about 40 px off it. When the moment wants otherwise, that's editing; what's
  never fine is a head chopped or a face buried by accident. Captions sit on the chest, their top 200 px below the chin (CS-1). In L-stack the caption's bottom edge sits
  24 px above the seam (y 936) and the head stays inside the window below y 960 (§3.6). Behind the person is fair game:
  that's where the heroes live (`behind: true`).
- **The hero stays readable behind the head.** For its whole hold, ≥ 65% of its glyph area is visible and its first and
  last letters are clear of the head; one behind hero at a time; it holds ≥ 0.6 s (the style holds 1.5–3.0 s). If the
  creator moves into it, shorten the hold or move the hero; never accept a word you can't read. Behind heroes set
  `exception: "behind_text"` and `text_class: "TC-display"` so the engine measures the occlusion.
- **No text over text.** On screen at once, at most: one hero, one tag, the caption. Never two heroes; never a hero and a
  full-frame statement together; never a hero that repeats the caption at the same moment.
- **On the word.** Every hero, insert, card, tag and counter starts 2 f before its trigger word's onset and is fully landed
  within ±5 f; counters land on the number word ±5 f. Caption words appear 1 f before their onset. Cuts sit on word
  boundaries ±1 f; audio is never offset.
- **Say what was said.** Every number on screen traces to the script or the creator's input (`plan/figures.json`);
  results, earnings and prices are the creator's own or stated in the script. Illustrations may use made-up but realistic
  numbers, names and screens, with no label (`illustrative: true`). Never fake earnings screenshots, testimonials or
  dashboards presented as real.
- **Promise integrity.** The hook's count equals the items shown; every "till the end" or "last secret" is paid on screen;
  the CTA keyword, URL or QR is on screen ≥ 1.5 s.
- **Numbers formatted right.** ₹ glyph, Indian grouping and lakh/crore compacts for rupee audiences; $, international
  grouping and K/M/B otherwise (§5.5).
- **Spelling.** Captions as spoken; brand and product names exact, with their case ("MacBook", "Instagram"); glossary
  spellings exact; profanity masked inside the word (f**king).
- **Readable.** Heroes have a cap height ≥ 160 px (they read at 25% scale); captions never below 54 px (the connector tier
  is 56); text holds ≥ 0.25 s per word, titles ≥ 10 f after they finish building. Meaning text stays inside x 64–1016,
  y 110–1500, and never in y < 110, y > 1540, or x > 970 between y 900 and 1540 (Instagram's buttons). The one exception is
  the **edge bleed** (`exception: "E5"`): display type ≥ 180 px may run to 24 px from the frame edge, glyphs never cropped,
  never inside those button bands, one at a time.
- **Audio.** −14 LUFS integrated, true peak ≤ −1.5 dBTP, the bed ≥ 18 dB under the voice, a hard end ≤ 6 f after the last
  word, no black tail.

**Never in this style:**
- A hero in front of the face, or a hero the head covers so much it stops being a word.
- Coloured caption words. Captions are white on footage and dark worlds, ink on light worlds; emphasis is size only.
- A third bright hue; red used as decoration; the neon used for a loss.
- A full-screen slide that just sits there; text-heavy cards (more than 6 rows, or body text under 40 px carrying the
  point).
- Stock clichés: handshake stock, piles of cash, generic "success" sunsets, lightbulbs, rockets, matrix code.
- A drawn QR code. The QR card uses the creator's own QR image only (FB-7 otherwise).
- A zoom that returns to its start inside the shot (a punch holds until the next cut); camera shake.
- Lowercase heroes. Heroes are uppercase grit words or numerals; captions are as spoken.
- Handwriting fonts for anything but hand tags and branch labels (P-11, P-23, P-27, P-39).
- Crossfades, slow dissolves, fades from black, black tails.
- Effect packs: light leaks, film burns, RGB-split, lens-flare PNGs. A new move is welcome when it's built in this style's
  language.
- Fake third-party media: a made-up post, headline or clip passed off as real. Show the real one, fetched, or rebuild it
  from its exact words (§12.4).

---

## §3 Worlds, layouts, stage moves, safe zones

### 3.1 Worlds
| ID | Kind | Look | Carries | Enter / exit |
|---|---|---|---|---|
| **W-room** | footage | The creator's own desk room, low-key and warm (measured `#2A1C14`–`#4A3220` midtones), lamp bokeh, the desk surface in the bottom 15–25% | Everything spoken to camera, heroes, prop hooks | Hard cut, zoom-blur (T-02), punch |
| **W-glass** | stage | Navy `#0E1A44` → `#050713` (gradient `glass-navy`), a soft `accent` glow (16%, r 520 at x 540, y 820, slow drift), noise 0.03, vignette 0.25 | Glass app cards (P-24), spotlight stack (P-18), slider (P-14), recap (P-22), token carousel (P-19, with a violet `violet-stage` radial painted by the scene) | Hard cut on the noun (G-4) |
| **W-space** | void | `#040406` with faint white star dots (pitch 96, 10%), a drifting smoke glow; scenes add 2–3 slow nebula streaks | The constellation hub (SM-1, P-17), B&W statements | Smoke dissolve T-05 in; hard cut out |
| **W-fog** | stage | Radial grey `#ABABAB` (centre x 540, y 760) → `#4A4A4A`, noise 0.04 | Glowing outline flows (P-25): white lines, frosted nodes, metric tiles | Hard cut |
| **W-paper** | paper | Warm paper `#EEEDE9`, grain 0.05, vignette 0.08 | Face cut-out reveals (P-34), disintegrating words (P-37) | Hard cut |
| **W-grid** | canvas | `#EEF0F5` with 2 px `#D7DAE2` grid lines every 96 px | Product circles (P-33), branch maps (P-23), call frames (P-39) | Hard cut |
| **W-white** | canvas | Pure `#FFFFFF` | QR card (P-40), neon chip words on screenshots (P-28) | Hard cut or white flash T-04 |
| **W-black** | void | `#000000`, faint neon glow (8%) behind the centre | Statements (P-35), offer card (P-42), end lockup (P-41) | Hard cut |

A world switch lands on a spoken noun or ordinal, never mid-phrase. The light worlds (W-paper, W-grid, W-white) flip the
captions to ink (`colour_by_bg`).

### 3.2 Layouts
| ID | Engine | Presenter rect | Graphic rect | Caption |
|---|---|---|---|---|
| **L-full** | `full` | 0, 0, 1080 × 1920 (Z-1/Z-2 crops on top) | — (heroes behind the head, tags around the props) | CS-1 chest: top = face bottom + 200 px (cy 1180 when no face is found; usually y 1000–1320) |
| **L-stack** | `stack`, seam_y 960, top `graphic`, bottom `footage` | 0, 960, 1080 × 960 (face centred in the band, head top y 1040–1160) | 0, 0, 1080 × 960 | CS-3 `seam_above`: the block's bottom edge 24 px above the seam (y 936) |
| **L-graphic** | `hidden` | — | full frame | CS-4 fixed cy 1420 (CS-2 top band cy 300 over people B-roll) |

**When to use which.** L-full is home: the face, the hero, the words. L-graphic is a glance: an insert, a card or a world on
its noun, then back. L-stack is for the graphic that needs longer than a glance (a table, a document, a flow the creator
walks through): the face stays under it, so the viewer never loses the person. Every switch lands within ±0.25 s of a
word: a number, a claim word, a sentence start.

### 3.3 Stage moves
| ID | Move | Recipe (30 fps) | Use |
|---|---|---|---|
| **G-1** | Hard cut | `via: cut`, 0 f, on a word boundary ±1 f | Default between any two layouts and between takes |
| **G-2** | Zoom-blur cut | T-02 (§9.1): the outgoing shot pushes in and defocuses for 3 f, the incoming one arrives defocused and slightly zoomed and clears in 3 f | Into a graphic world, a new take or a hero moment |
| **G-3** | Split cut | `via: cut` into L-stack; the top graphic is already settled on the cut frame (its own entrance plays inside the band over 8 f) | Tables, documents, flows that need longer than a glance, resource folders |
| **G-4** | Graphic cut | Stage → L-graphic and `world` set on the same frame | Glass cards, B-roll, QR |
| **G-5** | Smoke dissolve | T-05: `via: fade-through` 6 f + a smoke scene (z11, 12 f) into W-space | Entering the hub the first time |
| **G-6** | Return punch | Hard cut back to L-full with Z-1 (tight) on the first returning word; the next cut goes wide (Z-2) | Every return to the face after an insert |

### 3.4 Layout diagrams
```
L-full (talking head + hero behind head)        L-stack (graphic over face)         L-graphic (insert / world)
┌─────────────────────────┐ 0                   ┌─────────────────────────┐ 0         ┌─────────────────────────┐ 0
│ (IG top UI, keep clear) │ ← 0–110             │ (IG top UI)             │           │ (IG top UI)             │
│ connector "spend"       │ ← 120–230, beside   │  title / table / doc    │ ← 140–740 │  top band: CS-2 y 300   │
│ ███ HERO 30 MINS ███    │ ← hero top 160–480  │  card x 64–1016         │           │  graphic zone           │
│ ███  ( head )   ███     │   hero bottom ≤ 900 │  CS-3 caption block     │ ← ≈770–936│  x 64–1016, y 200–1300  │
│        (face)           │ ← face ~560–1000    ├──── seam y 960 ─────────┤           │                         │
│   connector "you're"    │                     │       ( head )          │ ← head top│                         │
│   KEYWORD "seriously"   │ ← CS-1 1000–1320    │        (face)           │  1040–1160│  CS-4 caption y 1420    │
│   connector "missing"   │                     │                         │           │                         │
│  desk + props           │ ← props 1250–1700   │                         │           │                         │
│ (IG bottom UI)          │ ← 1540–1920         │ (IG bottom UI)          │           │ (IG bottom UI)          │
└─────────────────────────┘ 1920                └─────────────────────────┘ 1920      └─────────────────────────┘ 1920
```

### 3.5 Safe zones and bands
- Meaning-text box: x 64–1016, y 110–1500; nothing in y < 110, y > 1540, or x > 970 between y 900 and 1540.
- **Hero band:** top y 160–480, x 24–1056 (edge bleed), bottom edge ≤ 900. The connector sits above-left of the hero
  (y 120–230 on a wide crop), the trailer below-right; both clear of the head region by 40 px.
- **Caption bands:** CS-1 chest y 1000–1320 (top = face bottom + 200 px); CS-2 top band centre y 300, left-aligned; CS-3
  in L-stack, bottom edge y 936 (24 px above the seam), up to two lines (≈ y 770–936); CS-4 centre y 1420. Caption max
  width 860 px (x 110–970).
- **Prop band:** y 1250–1700 (the desk). Prop tags sit 40 px above the prop rim and never below y 1500 (text).
- **Graphic zone** in L-graphic: x 64–1016, y 200–1300. **Top graphic** in L-stack: its text stays inside y 140–740, so
  the caption block never lands on it.

### 3.6 The person
- **People come for the creator.** They're on screen most of the reel: an insert is a glance and the face comes back by
  G-1 or G-6 before the viewer misses it. When a graphic explanation needs longer, it continues in L-stack with the face
  under it rather than holding a faceless frame. (Measured on the five reels: the face is on screen about 60–75% of the
  runtime; the two long faceless runs seen, a 9 s glow flow and a 7 s offer, are the ones this style moves into L-stack.)
- **The head region** is the face, the hair and the room above the head top, taken from the cut-out. The engine's head box:
  `ctx.face()` gives eyebrows to chin; head top = face.y − 0.55 × face.h (the hair); head width = 1.25 × face.w. In front
  of it: nothing, unless the moment truly wants it. Behind it: the hero.
- **L-full** (setup A, wide): head top y 300–560, eyes y 620–820, chin y 800–1050, face x 330–750, which leaves the hero
  160–480 px of room above the head. On a Z-1 tight crop the head top rises to y 120–300. CS-1 rides the chest: its top
  200 px below the chin on every chunk (it follows the crop), centre x 540, max width 860, kept inside y 110–1500. The hero
  connector goes above-left of the hero, beside the head, never above it; on a tight crop with no room above the head, it
  sits beside the head or the hero carries alone.
- **L-stack:** the window is x 0, y 960, w 1080, h 960 with no breakout, so the head never draws above y 960; the face is
  centred in the band, head top y 1040–1160. CS-3's block sits on the bottom of the graphic: its bottom edge at y 936,
  24 px above the window and ≥ 104 px above the head top.
- **L-graphic:** no presenter. Over people or product B-roll whose subject sits in the centre, the caption moves to the CS-2
  top band so it stays off that subject's face.
- **Crops:** wide = the frame as shot; mid 1.15–1.22; tight 1.30–1.45 around the face (§10.2).
- Props stay in the desk band; the creator's hands may cross the captions (footage isn't a layer).

---

## §4 Colour system

### 4.1 Role palette
| Role | Hex | One job | Text on it | Contrast |
|---|---|---|---|---|
| `primary` | `#C6FF1A` (TH-lime; mint `#4DFFC4`, yellow `#FFF01F`) | The reel's neon: hero numbers, gains, the active node, keyword chips, the current year, glow | `ink` | 16.6:1 (lime), 15.4:1 (mint), 16.6:1 (yellow) |
| `accent` | `#4363F2` | Glass-world glow: card rims, spotlight stage, token halo, hub halo | `paper` | 4.9:1 |
| `bad` | `#FF2A1A` | Zero, loss, the wrong path, the alert grade | `ink` | 5.2:1 |
| `good` | `#2BFF6E` | The reached result in a result pair, ✓ | `ink` | 14.7:1 |
| `ink` | `#0B0B0B` | Text on light worlds and on neon chips | — | 19.7:1 on white |
| `paper` | `#FFFFFF` | Captions, grit heroes, card text on dark worlds | — | 20.1:1 on night |
| `canvas` / `grid` | `#EEEDE9` / `#D7DAE2` | Paper and grid worlds | ink 16.8:1 | |
| `night` | `#050713` | Glass and space worlds | paper 20.1:1 | |

A creator's brand colour replaces `primary` (and, if they give two, `accent`); `bad` and `good` never change.

### 4.2 Meanings
- **White = the words.** Captions, grit heroes, statements.
- **Neon (`primary`) = the number that matters to the viewer**: income, time, count, the active step. One neon per reel.
- **Red / green = a result pair only**: red the zero or the wrong path, green the reached result. When red and green are
  on screen, the neon is not.
- **Accent = the glass worlds' light.** Never on text.
- Brand colours appear only on the creator's own product and logo.

### 4.3 Theme packs (per-reel rotation)
| ID | `primary` | When |
|---|---|---|
| **TH-lime** | `#C6FF1A` | Rotation slot 1 (the creator's reels 1, 4, 7 …); money gains, freelancing, income. Default |
| **TH-mint** | `#4DFFC4` | Rotation slot 2 (reels 2, 5, 8 …); salaries, offers, programmes |
| **TH-yellow** | `#FFF01F` | Rotation slot 3 (reels 3, 6, 9 …); time, years, milestones |

The reel's header declares `theme`: the pack that follows the previous reel's pack in the creator's folder (lime → mint →
yellow → lime), so two consecutive reels never share a neon. If the creator set a brand colour, all three packs take it
and the rotation stops.

### 4.4 Grades and clip treatments
- **Footage grade:** none. The creator's room is not regraded; match only exposure and white balance between takes.
- **Grade event GR-alert** (`warn` beats, 0.8–1.6 s): the A-roll turns red monochrome (`grayscale(1) sepia(1) saturate(7)
  hue-rotate(-38deg) brightness(.9) contrast(1.15)`) with a ⚠ icon and a grit statement ("PROBLEM", v03 @0:29). It
  **strobes**: in the reference the red grade, ⚠ and "PROBLEM" flick on and off every 1–2 f for 0.75 s (measured v03
  @0:28.85–0:29.6), then hold on for the rest of the line; ⚠ and "PROBLEM" show only on the red frames. Built as a z11
  overlay scene (`mix-blend-mode: color` in `bad` at 85% over the footage). It's the alarm: spend it on the line that is
  truly a warning, usually the re-hook or the last item.
- **GR-bw** (`grayscale(1) contrast(1.25) brightness(0.95)`): the A-roll punch behind a statement when there's no second
  angle (P-31b, FB-6).
- **Clip treatments** on creator B-roll (one per clip; consecutive clips never share one; `clean` allowed between):

| ID | Recipe (CSS on the clip frame) | Use for |
|---|---|---|
| `halftone` | `grayscale(1) contrast(1.6)` + a dot overlay (`radial-gradient` 5 px dots, pitch 9 px, multiply) | Money, notes, objects (v05 @0:07) |
| `invert` | `invert(1) grayscale(.6) contrast(1.2)` for ≤ 0.6 s | A shock or "wait" beat (v05 @0:10) |
| `bw_vignette` | `grayscale(1) contrast(1.25)` + a 30% radial vignette | People, the past, "before" (v05 @0:33–0:35) |
| `warm_tint` | `sepia(.45) saturate(1.4) hue-rotate(-8deg) brightness(1.05)` | Team, life, office warmth (v05 @0:19–0:24) |
| `neon_mono` | `grayscale(1) contrast(1.15) brightness(1.08)` + a `primary` wash at 18% (`mix-blend-mode: color`) | People and objects in theme-tinted mono, montages (v05 @0:06.5 banknotes, @0:33.3 student) |
| `clean` | none | Products and screens that must read exactly |

B-roll motion, one per clip, alternating: an **entry punch** 1.00 → 1.14 over 8 f ease-out (measured 1.13–1.15 over 6–10 f,
v05 @0:33.36, @0:34.12, @0:35.04), or a **slow pull-out** 1.08 → 1.00 over the clip on people B-roll (measured 25–30 f,
v04 @0:13.7, @0:14.7, @0:16.8).

### 4.5 Rules
- At most two bright hues in a frame (`max_bright_per_frame: 2`): the reel's neon plus one of bad/good, or bad + good in a
  result pair (then no neon). White, black and greys aren't bright hues.
- Coloured text on light worlds sits on a chip (P-28) or has a 4 px ink stroke; neon text on dark grounds carries its glow.
- Glow only on neon numbers, the active node, tokens and the offer code; grit heroes have no glow (a soft
  0 4 24 rgba(0,0,0,.35) shadow only).
- The neon never marks a loss; red never marks a gain.

---

## §5 Type and captions

### 5.1 Font map
| Slot | Family | Weights | Class | Used for |
|---|---|---|---|---|
| `body` | **Inter Tight** | 700 (connector, plain), 800 (keyword) | neutral grotesk 600–800, tight tracking | Two-tier captions, hero connectors and trailers |
| `ui` | **Inter Tight** | 500–700 | neutral grotesk 400–700 | Glass cards, tables, tiles |
| `display` | **Anton** | 400 | condensed heavy caps | Grit hero words, statements, end lockups |
| `numeric` | **Barlow Condensed** | 600–700 | condensed sans 600–700 | Neon hero numbers, odometers, rulers, node labels, chips |
| `marker` | **Permanent Marker** | 400 | marker / handwritten caps | Hand tags, branch labels |

Devanagari captions fall back to Noto Sans Devanagari 700/800 (no italics; the tiers keep their sizes). The ₹ glyph, ✓, ✕
and ⚠ are pre-painted.

### 5.2 The hero: the headline element
There is no banner. The **hero** is the headline: the first thing read, readable at 25% scale, standing behind the head.
Three recipes:

| Recipe | HERO-W grit word (P-01, P-02) | HERO-N neon number (P-03, P-04, P-06) | HERO-L lockup (P-05) |
|---|---|---|---|
| Font | Anton 400, uppercase, tracking −0.5%, line height 0.86 (statements: v03 @0:09 "IT DOESN'T MATTER HOW / CAPABLE / YOU ARE" is condensed, a 3-line size ladder). The hook hero can be a **wide** heavy display instead (v03 "3 SKILLS": 835 px wide for 7 glyphs, cap 173 px): Archivo Black or Unbounded 900 for a 1–2 word hook hero | Barlow Condensed 700, tabular figures, tracking −1% | connector Inter Tight 700 52 px + HERO-W/N + trailer Inter Tight 700 52 px |
| Size | font 200–560 px; fit the word to 760–1032 px wide; cap height ≥ 160 px | font 240–520 px; `size = min(520, 1000 / (0.46 × characters))` (₹1,20,000 = 9 characters → 241 px) | hero as its recipe; connector above-left, trailer below-right of the hero box |
| Fill | off-white `#E0E0E0`–`#F0F0F0` (measured; not pure white) with a **distressed** grit mask: clumpy erosion patches 2–8 px plus thin scratches, ≈ 15–20% of the glyph eaten (v03 @0:00.5 "3 SKILLS", @0:09 "CAPABLE"). Built with layered `repeating-radial-gradient` mask holes (1.2 px dots, pitch 3.1 px and 4.7 px, offsets 17%/31% and 63%/12%) plus a third, coarser layer (3 px dots, pitch 9 px); a soft grey smoke haze (radial, 20–30% white) sits behind the hook hero; shadow 0 4 24 rgba(0,0,0,.35) | lands in `paper`, then turns `primary` with glow `0 0 28px primary, 0 0 64px primary@50%` over 4 f | connector and trailer `paper`, no glow |
| Position | top y 160–480; bottom ≤ 900; centred on the frame or split around the head (P-02) | top y 220–420, centred | the hero box as its recipe; the connector 12 px above its top-left corner |
| Placement vs head | **behind the head.** Single word: its baseline sits ≤ 0.45 × cap height below the head top, and the word is ≥ 2.6× the head width, so ≤ 35% of the glyph area can be covered. Two words: split around the head (gap = head width + 48 px) | behind the head, same rule; the first and last digits stay outside the head's x-span | the connector is in front, so it never touches the head region; the hero is behind |
| Entry | slam from the right: x +140 → 0 in 5 f with a 3-ghost horizontal smear (copies at −40/−80/−120 px, 35/20/10% opacity), crackle (mask offset ±2 px) f3–f8, settle 1.03 → 1.00 f5–f9 | tick roll (§10.1): the value updates every frame 10–24 f, fill ramps `paper` → `primary`, lands on the number word ±5 f, glow flickers 4 f then holds (or slot roll 14–22 f) | connector rises 24 px + fades in 6 f, 4–15 f before the hero; trailer pops on its own word |
| Life | pinned to the room: it rides every crop change and camera move with the footage (`follow_footage: true`; v04 @0:32.7, v05 @0:02.96); one optional pulse 1.00 → 1.04 → 1.00 in 6 f on a re-spoken word | same; the glow breathes ±8% over 1.2 s | — |
| Lifetime | 1.5–3.0 s (≥ 0.6 s minimum); the hook hero may hold up to 6 s across cuts on the same take (v05 "1,20,000" 1.0–6.5 s); ends on a world change | same | same |
| Exit | gone with the shot on a cut (preferred), or blur-out 5 f | same | same |
| Text class | TC-display | TC-display | connector/trailer TC-display (48–60 px) |

**Hero shape:** ≤ 3 words (one number + one unit word counts as 2), ≤ 2 lines, readable at 25% scale, one hero on screen.
A hero is an event, not wallpaper: the hook, each item's name or number, and the moments the reel turns on. Captions keep
running while a hero is up (they're in different bands).

### 5.3 Caption profiles (CS-…)
Four profiles share one skin; only the position changes. All extend the library profile `lib:tharun`.

| Field | CS-1 **Chest two-tier** (default, L-full) | CS-2 **Top band** (people / product B-roll) | CS-3 **Seam** (L-stack) | CS-4 **Graphic band** (L-graphic) |
|---|---|---|---|---|
| Mode | full · primary · mute_safe | same | same | same |
| Chunking | `group`, 1–4 words, ≤ 18 characters per line, ≤ 3 lines (connector / keyword / connector); never split a name, number or unit; new chunk on punctuation and on pauses ≥ 0.25 s (always at 0.6 s) | same | ≤ 2 lines | same as CS-1 |
| Timing | lead 1 f; words **appear one by one on their onsets in their final place** (`reveal: word`); chunk swap **hard** (0 f, measured: no pop or fade, v05 @0:00–0:00.6, v04 @0:07.8); captions blur with the picture through T-02; ≥ 0.25 s per word; tail 0.1 s; no pause hold | same | same | same |
| Skin | Inter Tight 700, **plain 72 px**, as-spoken case, tracking −3%, line height 0.92, `paper`, shadow 0 3 14 rgba(0,0,0,.5), no container | shadow 0 3 16 rgba(0,0,0,.6) | plain 64 px, shadow .65 | shadow 0 2 10 rgba(0,0,0,.35) |
| Two-tier variant | **connector 56 px (700) + keyword 136 px (800)** by default; measured keywords run 84–185 px ("Websites" cap 61 px ≈ 84 px; "rupees" x-height 101 px ≈ 185 px), sized so the keyword line spans ≈ 450–600 px; ratio 2.43 (min **1.7**: real chunks go as low as 1.75, "Websites / and / Apps"); stack `split`: connectors before the keyword above it, after it below it; a chunk without a keyword is plain 72 px | same | connector 56 + keyword 124 | same as CS-1 |
| Position | `chest`: top = face bottom + 200 px, kept inside y 110–1500; centre x 540, max width 860; avoids the face (moves below the chin) | `fixed_y` centre y 300, **left-aligned** at the safe left edge (real: x ≈ 95, small 48–56 px, v02 @0:00.5 "the story of", v04 @0:20 "here's a", v03 @0:11 "spend") | `seam_above` (the L-stack caption): the block's bottom edge 24 px above the seam y 960, so y 936; two lines at most (≈ y 770–936), clear of the window and the head below it | `fixed_y` centre y 1420 |
| Colour by ground | light ground → `ink`, dark → `paper` | same | paper | same |
| Emphasis | `size_tier` only: the keyword (§1 priority: number → name/brand → topic noun → contrast word); ≤ 1 per chunk, min score 1.3, never stop-words (the engine also holds keywords to one a second) | same | same | same |
| Hide | under z8 scenes (statements, big lockups) and during stage morphs | same | same | same |
| Language | Latin; keep English terms verbatim; don't normalise spelling; profanity mask `inner` (f**king); glossary from the reel | same | same | same |
| Text class | TC-subtitle (floor 54: connector 56 ✓) | same | same | same |

**Profile switching:** CS-1 is the default; L-stack switches to CS-3 and L-graphic to CS-4 automatically
(`captions.by_layout`); write `captions.overrides {t: [a, b], profile: "CS-2"}` for every full-frame B-roll span whose
subject's face or product sits in the centre (v04 @0:14–0:20 "here's a / MacStudio").

**Tier shapes from the reference (reproduce exactly this shape):**
```
v05 @0:02       v05 @0:03        v02 @0:20          v04 @0:48
   rupees        without a         you're             afford
 per   month      degree         seriously          a MacBook
                                 missing out.        rightnow
(kw + below)   (above + kw)    (above + kw + below) (above + kw + below)
```

### 5.4 Other text
| System | Class | Recipe | Hold |
|---|---|---|---|
| **Hand tag** (P-11, P-23, P-27, P-39) | TC-label | Permanent Marker 44–60 px uppercase, `paper` on dark / `ink` on light, rotated −6…+4°; arrow 6 px stroke drawn shaft 7 f then head 3 f, curving from the tag to the target | ≥ 1.0 s |
| **Condensed label** (node labels, "PROJECT 2", ruler years) | TC-label | Barlow Condensed 600, 44–64 px, uppercase, tracking +1% | ≥ 10 f after built |
| **Neon chip word** (P-28) | TC-display | Barlow Condensed 700, 80–120 px, uppercase, `primary` fill, `ink` text, radius 4, padding 4/18 | ≥ 0.6 s |
| **Card title / body** (P-22, P-24, P-26) | TC-label | Inter Tight 700 56–72 px / 500 40–46 px | ≥ 0.25 s per word |
| **Metric value** (P-16) | TC-display | Inter Tight 700 64–96 px, `ink` on white tiles | ≥ 0.8 s after landing |
| **Statement** (P-07, P-35, P-36) | TC-display | Anton 180–300 px, uppercase, grit, line height 0.88; lines appear per phrase 4 f | ≥ 0.25 s per word |

### 5.5 Language and numbers
- Captions as spoken (English verbatim by default; Hinglish captions are romanised, Hindi captions Devanagari). Keep
  English terms verbatim in Hinglish.
- Brand and tool names exact (glossary). Product names keep their case ("MacBook", "Instagram").
- Numbers through `ctx.fmtNum` with `profile.numbers`. For a rupee audience (Hinglish and Hindi, and English when the
  creator works in rupees): the ₹ glyph, Indian grouping (₹1,20,000), compacts ₹2.5 L / ₹1.2 Cr on chips and tags, the
  full form on heroes up to 9 characters (₹1,20,000), the short form beyond (₹12.5 L). Otherwise $, international
  grouping, K/M/B (1.2M). Years and counts plain ("2026", "3 SKILLS"). Units after numbers in the hero ("30 MINS",
  "5 YEARS", "₹60/DAY").
- Devanagari: no uppercase or italic; heroes in Devanagari use Noto Sans Devanagari 800 at the same sizes, no grit mask.

---

## §6 Hook system

This style has no banner: the hook's title is the hero and the words around it. Connector, hero and the first caption
chunk together promise the viewer something: an outcome they want ("you can make up to / ₹1,20,000 / per month"), a
curiosity gap ("the story of this / 18 YO / student will blow your mind"), or who it's for ("Don't ignore these /
3 SKILLS / if you're 16–20"). It has to be true to what the reel delivers. The hero is usually the word they say; when the
first line has no number and no name, it's the line's claim word or the topic count. Write 8–10 connector + hero lines
(§6.5), pick the strongest by the stopper test, and keep the next two as alternates. The post title follows the same rule.

### 6.1 The stopper test
| Test | This style's number |
|---|---|
| **Thumbnail** | The frame at 1.7 s at 25% scale: the hero reads (cap height ≥ 160 px → ≥ 40 px at 25%) and the face is visible |
| **Mute** | With sound off, 0–3 s tell the topic: captions run from f3 and the hero states the number or the claim |
| **Motion at f0** | A Z-6 settle-out or Z-4 settle-push starts at f0 on live footage (the frame is already moving) |
| **Read time** | The hero reads in ≤ 1.2 s (≤ 3 words) |
| **Payoff-by** | The hero is fully landed by 1.7 s (HA-08); the result by 2.0 s (HA-01); the number by 1.0 s (HA-07); the lockup by 0.7 s (HA-05) |

The first three seconds feel dense: the words build one by one, the hero slams in, the glow ignites, the crop changes, a
tag pops. Dense in time, never in space: one hero, one caption, one tag, each landing while the last one settles.

### 6.2 HA-08 Prop + hero (default)
The creator holds or points at a prop, one hero lands behind the head, and a two-tier caption names the payoff. Spoken
shape: "*[connector] [HERO] [payoff clause]*" ("the story of this **18 YO** student will blow your mind", v02; "you can
make up to **1,20,000** rupees per month", v05).

| t | Beat | Visual | Caption (CS-1) | Layout / camera | SFX moment |
|---|---|---|---|---|---|
| **f0** | Moving start | Live take, prop already in hand or on the desk; the frame starts mid-motion: Z-6 settle-out 1.22 → 1.00 over 12 f (v05 @0:00), or 1.5 → 1.00 over 13 f behind a 6 f T-06 defocus (v04 @0:00), or Z-4 settle-push 1.00 → 1.18 over 8 f (v03 @0:00); 50% of the move happens in the first 2 f, no return | First word appears by f3 (word reveal; v05 shows "you" on f0) | L-full | hook hit on f0 |
| 0.0–0.5 | Setup words | If the hero has a connector ("the story of this", "Don't ignore these", "spend"), it rises in above-left of the hero band (y 120–230, beside the head) by 0.5 s | Words build one by one: "you" → "you can" → "you can make" (plain 72 px) | L-full | — |
| 0.2–1.0 | Hero lands (word) | P-01/P-02 grit word slams in from the right behind the head (5 f smear, crackle) on its word (v03: hero enters at 0.20 s, sharp at 0.32 s) | The hero's word is dropped from the caption; the caption holds its connector | Z-1 tight crop (1.30×) on the next cut | hero impact |
| 0.8–1.5 | Hero lands (number) | P-03 odometer rolls 14–22 f behind the head, lands on the number word ±5 f | Caption keyword chunk waits for the unit ("rupees") | hold | counter roll |
| 1.5–1.8 | Hero ignites | Neon glow ignites on the number (4 f), or the grit word settles; **payoff by 1.7 s** | Next chunk: keyword tier ("rupees / per month") | — | — |
| 1.8–2.5 | Prop tag | P-11 hand tag + arrow to the prop ("STUDENT", 10 f), or P-20 three icon tiles pop at chest-bottom (3 f stagger), or P-12 card held to camera | Two-tier chunk with a keyword | Z-2 back to wide on a cut, or a Z-3 blur-punch mid-shot (v05 @0:02.96: 1.0 → 1.3 in 5 f, the hero rides it) | tag pop |
| 2.5–3.0 | Promise | Hero still up (hold ≥ 1.5 s total) | "will / blow / your mind" | — | — |
| 3.0–4.5 | Exit to the promise | Hero ends on the cut; T-02 zoom-blur cut, T-04 flash or G-4 cut into the first insert (a glass card, the headline card, a B-roll clip) on the noun | — | — | whoosh on the zoom-blur |

**Never skip the hero.** If the script's first line has no number and no name, use the line's claim word as a grit hero
("FREELANCER", "PROBLEM") or the topic count ("3 SKILLS").

### 6.3 Alternate hooks

**HA-01 Result pair (red → green)**, v01: "Here's how you can go from making ₹0 to ₹5 lakh a month". Needs PR-1 (two
glasses) or FB-2.

| t | Visual | Caption | Camera |
|---|---|---|---|
| f0 | Both props on the desk (red left, green right), the creator gesturing; Z-6 settle-out | "Here's how" | L-full wide |
| 0.5–1.1 | — | "you" → "you can" → "you can go" | — |
| 1.1–1.3 | T-02 zoom-blur cut | "making" | — |
| 1.3–2.0 | Punch tight on the **red** prop; P-08 red tag "₹0" pops 40 px above its rim (6 f): **result by 2.0 s** | "₹0" dropped from the caption | Z-1 tight on the prop |
| 2.0–2.2 | Whip-pan to the **green** prop, filmed in camera (6 f, motion blur; the counter keeps ticking through it, v01 @0:02.0; no prop take → T-02) | — | — |
| 2.2–2.9 | P-09 counter rolls ₹0 → ₹5,00,000 above the green rim in `good` (20 f, 5 visible values), lands on "5 lakh" ±5 f, glow | "to" | hold |
| 2.9–4.5 | Pull out: both tags visible (red ₹0, green ₹5,00,000); then a grit hero ("FREELANCER") behind the head with the connector "as a" | "as a" → hero | Z-2 wide |

It travels: "₹0 → ₹1,00,000 a month as a video editor" (two glasses), or a body result, "92 KG → 76 KG" (a red tag on an
old photo prop, a green tag on the creator).

**HA-07 Live number / ruler open**, v04: "5 years since I started running a creative agency".

| t | Visual | Caption | Camera |
|---|---|---|---|
| f0 | Focus-pull entry (v04 @0:00): T-06 defocus clears over 6 f while Z-6 settles 1.5 → 1.00 over 13 f, on a hair flick | — | L-full |
| 0.17–0.5 | P-13 year ruler slides in from the right across the chest (y 1100, 12 f) | — (CS-1 offset drops to 120 px while the ruler is up: the caption block ends above the ruler's top, y 1080, and stays below the chin; a chunk that won't fit waits for the ruler to leave) | — |
| 0.67 | The current year turns `primary` on the ruler | — | — |
| 1.0–1.33 | P-04 count steps "1" → "4 YEARS" → "5 YEARS" behind the head (4 f per step), neon glow: **number by 1.0 s** | — | Z-1 tight at 1.17 |
| 2.0–2.9 | P-05 lockup: connector "since I" + grit hero "STARTED / RUNNING", then "a" + "CREATIVE / AGENCY" | connectors only | Z-2 wide |

It travels: "3 YEARS since I quit my 9-to-5", "5 YEARS since we opened the café".

**HA-05 Claim lockup / promise chip**, v03: "Don't ignore these 3 skills if you're 16–20 years old".

| t | Visual | Caption | Camera |
|---|---|---|---|
| f0 | Connector "Don't Ignore These" fades in at y 120–230 (48 px), above-left, clear of the head | — | L-full |
| 0.17 | Grit hero "3 SKILLS" slams in from the right behind the head, crackle: **lockup by 0.7 s** | — | Z-4 settle-push from f0 (1.00 → 1.18, 8 f) |
| 0.8–2.0 | Hero holds | "16-20" → "16-20 years" → "16-20 years old" (plain) | — |
| 2.3–2.8 | P-20 three icon tiles pop at chest-bottom (3 f stagger) and drift up 40 px | "these are the" | — |
| 3.0 | Caption "3 skills"; T-05 smoke dissolve into the hub (SM-1) on "skills" | "3 skills" | — |

It travels: "Don't ignore these 3 SKILLS before 2027", "Stop doing these 3 EXERCISES".

### 6.4 Hook pairs by topic
The pair for HA-08 and HA-05 is **subject → reveal** (the prop or claim → the hero); for HA-01 **bad → good result**; for
HA-07 **subject → reveal by 1.0 s**.

| Topic shape | Hook | First subject (prop / line) | Hero (reveal by 1.7 s) | How each is shown |
|---|---|---|---|---|
| Income from zero ("freelancing income") | HA-01 | Red glass: "₹0" | Green glass: ₹1,00,000 a month | PR-1 glasses + P-08 / P-09; fallback P-10 vessels |
| Things to learn ("skills to learn") | HA-05 | "Don't ignore these" | **3 SKILLS** | P-05 lockup + P-20 tiles |
| A person's story ("a student's story") | HA-08 | Printed photo of the subject (creator-owned) | **19 YO** + "STUDENT" tag | PR-2 photo + P-11 hand tag; no photo (the creator's, or a public figure's from the web) → P-34 silhouette |
| An amount without a credential ("salary without a degree") | HA-08 | Handwritten card "DEGREE" | **₹1,20,000** per month | P-12 card + P-03 odometer |
| Years of doing it ("years of experience") | HA-07 | Year ruler | **5 YEARS** | P-13 + P-04 |
| A body result ("weight loss") | HA-01 | Old jeans or a photo (red tag "92 KG") | Green tag **76 KG** | Props + P-09; fallback P-10 with kg tags |
| Things to stop ("habits, routine") | HA-05 | "Stop doing these" | **3 HABITS** | P-05 + P-20 |
| A daily quantity ("protein, diet") | HA-08 | The food in hand (eggs, a bowl) | **120 G** protein | Prop + P-03 neon number |
| Time to a result | HA-07 | Day ruler (days 1…90) | **90 DAYS** | P-13 (days) + P-04 |

### 6.5 Hero writing
**Formula:** `[connector, 1–4 lowercase words, optional] + HERO (≤ 3 words, caps, or a number + unit) + [trailer, optional]`.
The hero is the one word the viewer must remember.

| Template | For example |
|---|---|
| Number + unit | "you can make up to **₹1,20,000** per month" |
| Count + noun | "Don't ignore these **3 SKILLS**" |
| Age / identity | "the story of this **18 YO** student" |
| Time | "**5 YEARS** since I started" · "spend **30 MINS** everyday" |
| Role / claim | "as a **FREELANCER**" · "**DEADLY · COMBO**" |
| Problem word | "**PROBLEM**" (warn, GR-alert) |

- Uppercase heroes, as-spoken captions. English heroes unless the captions are Hinglish or Hindi.
- Write 8–10, pick by the stopper test, keep two alternates for the storyboard.
- **Banned:** heroes longer than 3 words, vague hype ("GAME CHANGER"), numbers the script doesn't state, ₹ written as Rs.

### 6.6 Hook sound
The hook carries cues on its events (a hit on f0, the hero impact, the counter roll, the zoom-blur whoosh); the music bed
enters after the hook, on the first item marker (§11).

### 6.7 CTA and end cards
The device is the creator's (a QR card needs their QR image; otherwise a comment keyword or link in bio). Placement
`mid+end`: a first CTA flash at 55–75% of the runtime (1.5–2.0 s), the full CTA at the end.

| Device | Spoken pattern | On-screen element | Hold | Where |
|---|---|---|---|---|
| `qr` | "scan this QR code for the entire guide" | **P-40 QR card** on W-white: the creator's QR image 560 × 560 centred (top y 520); CS-4 caption in ink: "scan this / QR Code" above (centre y 380), "for the / entire guide" below (centre y 1220); a white flash in (T-04) | ≥ 1.5 s (2–4 s at the end) | mid + end |
| `comment_keyword` | "comment KEYWORD and I'll send it" | **P-43 keyword hero**: the keyword as a neon grit hero behind the head (kind `cta-keyword`), connector "comment" above-left; the caption keeps "and I'll send it" | ≥ 1.5 s | mid + end |
| `link_bio` | "link in bio" | Two-tier caption "link / in bio" + a hand arrow (P-11 style) pointing down-left toward the profile (stays above y 1500) | ≥ 1.5 s | end |
| `end_card` | the closing line | **P-41 end lockup** on W-black ("one last push / 90 DAYS / before 2026 ends") or **P-42 offer card** for the creator's own product | 1.5–4.0 s | end |

- **QR card (P-40):** 2–4 s at the end, 1.5–2.0 s mid-reel. **End lockup (P-41):** 1.5–3.0 s. **Offer card (P-42):** the
  creator's own product only; every number on it (seats, price, discount) from the script; the code line glows in
  `primary`.
- End cards last ≤ 4.0 s; the keyword, URL or QR is readable ≥ 1.5 s; the reel hard-ends ≤ 6 f after the last word (T-09).
- No SFX in the 1.0 s before the first CTA word; no animated camera move during the CTA words.
- **Sponsors:** none by default. A sponsored reel says so in speech and on screen: "Paid partnership" (Inter Tight 500
  24 px) top-left for ≥ 2 s.

---

## §7 Structure and rhythm

### 7.1 Structure: a list
Promise → items with an identical ritual → payoff → CTA, numbered ascending. When the items are skills or pillars of one
idea, the list is drawn as a **framework hub** (SM-1); when they're sequential steps, as a **spotlight stack** (SM-2).
Story reels ("the story of this 18 YO…") run the same ritual with beats instead of items: setup → twist → numbers →
lesson.

### 7.2 Markers (SM-…): one style per reel, at every item
| ID | Marker | Recipe | Use for |
|---|---|---|---|
| **SM-1** | **Constellation hub** (P-17) | W-space; the hub sphere + spokes; on the ordinal word the in-scene view flies to the item's node, the node grows 1.0 → 1.25 and glows `primary`, its label types 1 letter/f (Barlow Condensed 600, 56 px); 1.2–2.0 s; the overview returns at the recap ("LEARN THESE / 3 SKILLS") | 3–5 parallel items (skills, habits, pillars) |
| **SM-2** | **Spotlight stack** (P-18) | W-glass; a warm light cone from the top; the step's paper sheet ("STEP 2 / SOLID PORTFOLIO") floats down into the light over 14 f; earlier sheets lie on the desk below; 1.2–2.0 s | Sequential steps, roadmaps (3–6 steps) |
| **SM-3** | **Token carousel** (P-19) | Violet stage; two glowing outline hands hold the item's token (label inside), the queued tokens numbered in a row below; the token flips 6 f per item | 5+ items, ranked lists |
| **SM-4** | **Spoken only** | No marker graphic; the ordinal is the caption keyword ("first", "second") with a Z-1 punch, and the item's hero carries the name | Short lists (2–3) inside story reels |

Numbering ascending. **Recap: on** (the P-22 glass recap or the SM-1 overview before the CTA). Teaser chips: off.

### 7.3 The item ritual (the same for every item)
| Time (from the ordinal word onset) | Step |
|---|---|
| −2 f | Cut (G-4), or the smoke dissolve (G-5) the first time into W-space; the marker scene enters on the list cue |
| 0 → +36…60 f | The marker plays (node fly-to / sheet float / token flip); the CS-4 caption carries the ordinal + the item name as keyword |
| on the name word ±1 f | Back to L-full by G-6 (Z-1 tight); the **item hero** lands behind the head (P-01 grit name or P-03/P-04 number), hold 1.5–3.0 s |
| then | The evidence, one picture per noun: P-24 glass card, P-31 stylised clip, P-12 card, P-16 tiles, P-21 icons, P-27 site card; face and insert alternate, and the face comes back between inserts long enough to say the next words to you (a two-clip montage is the exception) |
| the takeaway line | Z-2 wide, a two-tier caption with the takeaway keyword, no graphic: the breathing beat |

The ritual is the one place repetition is the point: the viewer learns it and feels the count go up. The **last item
escalates**: its hero is a neon number (P-03) or a statement bleed (P-07), and it gets the GR-alert or the biggest insert
of the reel.

### 7.4 Open loops and the re-hook
- **Loops used:** the count loop (the hook's "3 skills" is paid by 3 markers), the deliverable loop ("scan / comment for
  the entire guide"), the "last one" loop ("the last secret", v03 @0:51).
- **Every promise is paid on screen.**
- **The re-hook.** Around the middle, where attention sags (in the reference between 40% and 60% of the runtime), a twist
  line ("the surprising part?" v02 @0:11, "weird part?" v05 @0:08, "Watch till the end" v03 @0:26) is shown as a two-tier
  caption with the twist word as keyword, after a beat of silence of up to 0.3 s, with **either** a GR-alert event and a
  "PROBLEM" statement (warn) **or** a grit hero behind the head ("LAST SECRET") + a Z-5 dutch roll.
- **The hook is over fast,** so the first marker arrives while the promise is still fresh.

### 7.5 Rhythm: the punch-cut pulse
- **It follows the speech.** Every breath, retake and pause is cut out; the cuts sit on word boundaries and every one
  changes the crop, so each sentence arrives in a new frame. The only silence left in is a deliberate beat (up to 0.3 s)
  before a twist line.
- **It never sits still, but it's never random.** Something new arrives when the words give it a reason: the next caption
  word, a crop change, a hero on the word that matters, an insert on the noun, a blur-punch on the claim. Live footage
  always moves; a graphic world always has something arriving inside it.
- **Loud and quiet take turns.** Heroes, numbers and inserts are the loud beats; the takeaway is quiet: wide, no graphic,
  just the words on the chest. That contrast is what makes the next hero hit.
- **The energy curve:** the hook at maximum (prop + hero + punches) → the items steady (the ritual) → the re-hook spikes →
  the last item escalates → the CTA clean (the white QR card or the keyword hero, no zoom-blur during the CTA words).
- There are no entertainment-only beats (comedy off): the energy comes from the cut, the hero and the performed numbers.
- For reference, measured on the five reels (a description, not a target): 25–48 cuts a minute (v01 26, v02 25, v03 25,
  v04 29, v05 48), median shot 0.96–2.08 s, p90 2.9–4.4 s; the longest single shots (5–9 s) are graphic worlds with motion
  inside; the longest A-roll shot is 3.9 s and carries a blur-punch inside (v01 @0:06.5–0:10.4); a hero every 8–15 s; an
  insert or card every 4–8 s.

### 7.6 The recurring motif
- **M-hub** (SM-1): the marbled sphere Ø 150–210 with a 36 px glow and its spokes; the same diagram (same node positions)
  returns at every item; the active node is lit (`primary`) and earlier nodes stay white; the overview returns at the
  recap.
- With SM-2 the recurring element is the sheet stack (it grows one sheet per step); with SM-3 the token row (one token moves
  up per item).
- No morph chain (hard cuts are the style); no bookend.

---

## §8 Visual system: B-roll and patterns

`graphics: support`: the words and the face carry this style, and the graphics land around them on the exact noun. Every
spoken number becomes a performed number (D3). Variety comes from the moment, never from a quota; the item ritual is the
one deliberate repeat.

### 8.1 Families (B-…)
| ID | Family | Source class | The creator supplies |
|---|---|---|---|
| **B-1** | Hero type (grit words, neon numbers, lockups, statements) | engine | nothing |
| **B-2** | Props and result pairs | creator-owned (props in the A-roll) / engine (fallbacks) | PR-1…PR-5 (optional) |
| **B-3** | Performed numbers (odometers, rulers, sliders, tiles) | engine | the numbers in the script |
| **B-4** | Markers and structure (hub, spotlight, tokens, icon tiles, recap, branch map) | engine | nothing |
| **B-5** | Explainer cards (glass cards, glow flows, tables, site cards, chips, folders, headline cards) | engine / creator-owned screenshots / fetched from the web / rebuilt | SH-5 screenshots (optional) |
| **B-6** | Stylised inserts (B-roll with treatments, people topline, product circle, cut-out reveal, mono statements, alert grade, disintegrate, chat mock, call frames) | creator-owned / fetched from the web / rebuilt | SH-4 clips, SH-6 second angle (optional) |
| **B-7** | CTA and end (QR card, end lockup, offer card, keyword hero) | engine + the creator's QR / offer | SH-7 QR or keyword |

### 8.2 How the graphics behave
- **On the noun, then gone.** An insert or card lands on the word it shows and leaves on a cut back to the face; nothing
  lingers past its word.
- **Behind or beside, never in front.** Heroes stand behind the head; tags and cards sit beside the creator or take the
  whole frame for a glance; the face stays clear.
- **One thing too big to miss.** One hero, one tag and the caption at most; when a card is up, the hero is gone.

### 8.3 Pattern specs (P-…)
All motion at 30 fps. "Engine" names the building block. Every text scene sets `text_class`; every behind hero sets
`behind: true, exception: "behind_text"` (or `"E5"` when it bleeds to the frame edge; a scene carries one exception id).

**B-1 Hero type**
| ID | Name | Type | On screen | Motion (30 fps) | Use when | Class · needs | Engine |
|---|---|---|---|---|---|---|---|
| **P-01** | HERO-GRIT-BEHIND | overlay | One 1–3 word grit-white Anton caps word behind the head, 760–1032 px wide, top y 160–480 | Slam from the right x +140 → 0 in 5 f with 3 smear ghosts; crackle f3–f8; settle 1.03 → 1.00 f5–f9; hold 1.5–3.0 s; ends on the cut | Hook hero, item names, claims ("3 SKILLS", "FOCUS", "FREELANCER") | TC-display · behind · matte (a hero bleeding past the 64 px margin declares `exception: "E5"` instead: one exception per scene) | `VEOS.scene({behind: true, kind: "hero_text", exception: "behind_text", z: 3})` |
| **P-02** | HERO-HEAD-GAP | overlay | Two words split around the head: word 1 left of it, word 2 right; gap = head width + 48 px (visible ≥ 85%) | Word 1 slides from the left, word 2 from the right 3 f later, each 5 f with smear | Two-word heroes ("18 YO", "15 DAYS", "DEADLY · COMBO") | TC-display · behind · head box | scene, x from `ctx.face()` |
| **P-03** | HERO-ODOMETER | figure | A neon number behind the head, digits in fixed tabular slots | Default **tick**: the value updates every frame (ease-out, 10–24 f; v01 @0:02.0 ₹1,50,263 → ₹3,80,853 one value per frame, @0:06.6 0 → 77.5% in 9 f), the fill ramps `paper` → `primary` during the roll, glow flickers on alternate frames for 4 f on landing; or **slot** (v05 @0:01): each slot rolls 14–22 f with vertical blur 12 → 0 px. Lands on the number word ±5 f; glow breathes ±8% / 1.2 s | Every money amount, big count, followers, salary | TC-display · behind + `exception: "E6"` on the digit slot · figure | `VEOS.data.counter({font: "numeric", glow: "primary"})` with `behind: true, kind: "hero_number"`, or bespoke with `ctx.figAt` |
| **P-04** | HERO-COUNT-STEPS | figure | A number that steps through 2–4 spoken values; the unit word joins at the last step ("1" → "4 YEARS" → "5 YEARS") | 4 f per step, scale 0.92 → 1.00 per step, glow on the final | Durations, ages, growth over time | TC-display · behind + E6 · figure (steps) | `VEOS.data.counter` with `steps` |
| **P-05** | HERO-LOCKUP | overlay | Connector (52 px) above-left + hero + trailer (52 px) below-right ("spend / 30 MINS / everyday", "the story of this / 18 YO / student") | Connector rise 24 px + fade 6 f before the hero; hero as P-01/P-03; trailer pops 6 f on its word | Heroes that need context; HA-05 hooks; the hero above the head when there's no matte | TC-display · behind (hero only) | one scene, connector in front and clear of the head (a second scene `z: 5`) |
| **P-06** | HERO-TICKER | figure | Numbers appear left → right one per spoken word ("18 19 20"), unit row under them ("Years … old") | Each number pops 4 f (scale 0.8 → 1.0) on its word; the newest is `primary` | Counting ages, years, attempts aloud | TC-display · behind · figure | scene with `events` per word |
| **P-07** | STATEMENT-BLEED | overlay | 2–4 lines of grit caps filling the width (edge bleed), behind the creator on A-roll, in front of a B-roll clip (clear of the subject's face) | Lines appear per phrase, 4 f each (rise 20 px); hold ≥ 0.25 s/word; captions hide (z8 on B-roll) | A principle or quote the reel turns on ("IT DOESN'T MATTER HOW CAPABLE YOU ARE / IF YOU CAN'T EXPLAIN IT CLEARLY") | TC-display · behind on A-roll · E5 | scene `z: 8` (B-roll) or `behind` (A-roll) |
| **P-08** | HERO-RED-ZERO | figure | The bad-state value in red glow over the bad prop or card ("₹0", "0 CLIENTS", "92 KG") | Pop 6 f (scale 0.6 → 1.05 → 1.0); red glow 0 0 24px bad | The "before" side of a result pair | TC-display · anchor · figure | scene + anchor point |

**B-2 Props and result pairs**
| ID | Name | Type | On screen | Motion | Use when | Class · needs | Engine |
|---|---|---|---|---|---|---|---|
| **P-09** | PROP-PAIR-TAGS | figure | Two real props (red / green); a red tag on the bad one, a `good` counter on the good one, 40 px above each rim | Red tag pops 6 f on its word; whip-pan or T-02 to the good prop; the counter rolls 20 f with 5 visible values and lands on the number word ±5 f | HA-01 hooks with PR-1 | TC-display · anchors (static, from the anchor pass) · figure | counter scene placed at the anchor |
| **P-10** | RESULT-PAIR-VESSELS | figure | FB-2: two drawn glass jars (SVG, 300 × 420 each) on W-glass or in the L-stack top band; liquid red at 8% vs `good` at 85% | Jars rise 10 f, 3 f stagger; the good liquid fills 0 → 85% over 18 f on the number word, with a meniscus wobble; tags as P-09 | HA-01 without props | TC-display · figure | bespoke scene (canvas) |
| **P-11** | PROP-HAND-TAG | annotation | One prop + a hand tag ("STUDENT") + a curved arrow to it | Arrow shaft 7 f + head 3 f, then the tag writes on L → R 10 f | Naming what the prop is (a photo, a device, a person) | TC-label · ink · anchor | scene with an SVG path (`stroke-dashoffset`) |
| **P-12** | PAPER-CARD-PROP | overlay | A handwritten card held to camera (real) or FB-3: a white card 360 × 200, rotated −6°, marker word 72 px `ink`, beside the creator at chest (x 120–480 or 600–960) | Real: the card flickers to an inverted neon outline for 1–2 f twice while held (v05 @0:03.3; a z5 scene masked to the card's anchor box). Drawn: pop 6 f with a 2° wobble for 10 f | A keyword the viewer must remember ("DEGREE", "₹60/DAY") | TC-label / display | scene (drawn) |
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
| **P-17** | CONSTELLATION-HUB | state | W-space: a white marbled sphere Ø 180 with 6–9 thin spokes to white node dots; item nodes Ø 44 labelled in condensed caps 56 px; the active node `primary` glow | Overview: spokes draw 12 f. Per item: the whole diagram translates/scales in-scene so the active node lands at (620, 760) over 18 f (ease in-out), the node grows 1.0 → 1.25, its label types 1 letter/f | SM-1 | TC-label · the motif M-hub | `VEOS.fx.diagram` (nodes circle, edges line) inside one transformed scene |
| **P-18** | SPOTLIGHT-STACK | state | W-glass: a warm cone (rgba(255,236,190,.32), a neutral light, not a role) from the top centre; a paper sheet 420 × 560 with "STEP n" (40 px) + title (Barlow 600 56 px) floats into the light; earlier sheets lie on the desk below | Entered by T-02 (v01 @0:17.8); sheet descends 60 px + rotates −6° → −2° over 14 f, glows; earlier sheets slide left 40 px; the whole stage pushes in 1.00 → 1.3–1.6 over the beat, accelerating (in-scene scale, v01 @0:10.6, @0:18.2, @0:52.9) | SM-2 | TC-label | bespoke scene |
| **P-19** | TOKEN-CAROUSEL | state | Violet radial stage (`violet-stage`, z1); two glowing `accent` outline hands hold a Ø 300 token with the item label (Inter Tight 700 44 px); queued tokens Ø 110 numbered below at y 1300–1420 | Token flips on Y 6 f per item; the next numbered token travels up 12 f | SM-3 | TC-label | bespoke scene (SVG hands) |
| **P-20** | ICON-TILE-ROW | overlay | 3 white glass tiles 150 × 150 radius 32 with line icons, at chest-bottom (centre y 1240), x 240 / 540 / 840 | Pop 6 f with 3 f stagger, then drift up 40 px over 1.0 s; exit fade 5 f | Announcing a count ("3 skills", "3 tools") | no text (icons) | `VEOS.fx.card` × 3 or bespoke with `fx.icon` |
| **P-21** | ICON-LABEL-PAIR | overlay | White icon circles Ø 100 + condensed labels 44 px, one each side of the head (y 160–420, outside the head region), appearing one per spoken item ("ONE SKILL TO SELL" + "GREAT COMMUNICATION") | Pop 6 f on each item word; hold to the end of the pair | Combining two ideas ("deadly combo") | TC-label | bespoke |
| **P-22** | RECAP-GLASS-LIST | state | W-glass: a frosted glass card 760 × 620 radius 36, ghost header "CONCLUSION" 40 px, rows typed as spoken (title 56 px, sub-bullets 42 px) | Rows appear on their words 4 f each; the card drifts up 30 px; exits blurring back 8 f | The recap before the CTA | TC-label | `VEOS.fx.card` (glass) with body |
| **P-23** | BRANCH-MAP | annotation | W-grid: a polaroid of the creator (a still from the A-roll, 14 px white border, rotated 2°) top-centre; hand branches curve down to 2–3 icon tiles with marker labels ("BUILDING STUFF", "CREATIVE FIELDS") | Polaroid drops 8 f; each branch draws 10 f and its label writes 10 f on the spoken option | "Either X or Y" choices | TC-label · ink | bespoke |

**B-5 Explainer cards**
| ID | Name | Type | On screen | Motion | Use when | Class · needs | Engine |
|---|---|---|---|---|---|---|---|
| **P-24** | GLASS-APP-CARD | overlay | W-glass: a window card 520 × 360 radius 28, white 10% fill, 2 px `accent` rim at 40%, inner glow, three window dots, an icon on top (fx.icon 72 px), title Inter Tight 700 60 px; a ghost of the previous card above, blurred 12 px | Card rises 60 px + de-blurs over 10 f; the next card pushes it up and out (T-10) | Naming a skill, tool or category ("Building", "Video Editing", "AI Automation") | TC-label | `VEOS.fx.card({theme: "glass"})` |
| **P-25** | GLASS-FLOW | state | W-fog: white glowing outline nodes (Ø 260 circles with icons) and frosted cards connected by 4 px glowing lines; node titles 64 px (`ink` in the light centre, `paper` at the edges) | The view travels node to node in-scene (18 f each, ease in-out); each line draws 10 f; icons pulse 6 f on their word | A mechanism or pipeline ("scrapes data → filters jobs → writes the email") | TC-label | `VEOS.fx.diagram` with in-scene translate |
| **P-26** | STEP-TABLE | figure | L-stack top band: a dark card with a grit title ("5 SIMPLE STEPS", Anton 96 px) and up to 5 rows (number 44 px + two columns, Inter Tight 500 40 px), its text inside y 140–740 | Rows appear on their spoken step, 4 f each; the active row brightens, others 60% | A routine or plan the creator walks through, longer than a glance | TC-label | bespoke in the stack's graphic rect |
| **P-27** | SITE-CARD-TAG | overlay | A site/app card 460 × 640 (the creator's screenshot SH-5, the real page captured from the web, or a recreated generic UI) top-left of the frame clear of the head region by 40 px + a condensed tag ("PROJECT 2", 52 px) top-right with a hand arrow to the card | Card rises 10 f; arrow 10 f; the tag pops 6 f | Showing examples one by one ("project 2, project 3, project 5??") | TC-label · ink · insert (if third-party) | `VEOS.fx.shot` / `fx.appUI` + arrow scene |
| **P-28** | NEON-CHIP-WORD | overlay | W-white: a screenshot or card (creator or recreated) with a condensed keyword on a `primary` chip stamped at its lower-left edge ("TWEAKING,", "HOSTING") | Chip pops 6 f (scale 1.2 → 1.0); the card pushes in 1.00 → 1.04 over the beat | A feature or step name on a product view | TC-display | `VEOS.fx.shot` + chip scene (`overlaps` the card) |
| **P-29** | DOC-FOLDER | overlay | L-stack top band or W-space: a folder icon 180 px (drawn) + label "Detailed Document" 44 px; a cursor glides in 12 f and clicks (folder scale 0.94 → 1.0) | As stated | The deliverable / resources ("I've attached a detailed document") | TC-label | bespoke (`fx.icon` folder + cursor) |
| **P-30** | PAPER-HEADLINE-CARD | overlay | A newspaper-style headline card (the masthead set in type, the date and the exact headline from the real article, fetched, `primary` highlight bars on the spoken phrase), in the L-stack top band | Card rises 10 f; highlight bars wipe word by word from the phrase's word | A story or news fact the script states | TC-label · insert | `VEOS.fx.headlineCard({theme: "paper"})` |

**B-6 Stylised inserts**
| ID | Name | Type | On screen | Motion | Use when | Class · needs | Engine |
|---|---|---|---|---|---|---|---|
| **P-31** | STYLISED-CLIP | footage-treatment | A creator B-roll clip full-bleed (L-graphic), a glance (measured 0.8–2.2 s), with one treatment (§4.4); CS-4 caption (CS-2 when a face or product sits centre) | In on the noun by a T-04 flash or a hard cut; an entry punch 1.00 → 1.14 over 8 f ease-out, or a slow pull-out 1.08 → 1.00 over the clip (§4.4); consecutive clips never share a treatment. **Variant P-31b** (FB-4/FB-6): a Z-1 punch of the A-roll with GR-bw for ≤ 1.2 s. **Variant P-31c** flicker montage (T-12): 5–8 clips × 5 f, one treatment, one caption | Any concrete noun the creator has footage of (office, team, city, money, a laptop) | footage | `VEOS.fx.clip({kenburns: [1, 1.04]})` + CSS filter |
| **P-32** | PEOPLE-TOPLINE | footage-treatment | Team/people B-roll with the two-tier caption in the top band naming the object ("here's a / MacStudio") | As P-31; the topline caption appears with the cut; its keyword may slide in from the left with motion blur, 6 f (v04 @0:22.06) | Showing who uses what, team members, clients | footage | `fx.clip` + `captions.overrides` CS-2 |
| **P-33** | PRODUCT-CIRCLE | overlay | W-grid: a big `accent` circle Ø 760 (centre y 1000) with 2–4 product cut-outs (creator photos) or `fx.logoPlate` tiles; the two-tier caption across it ("uses an / apple device") | Circle scales 0.6 → 1.0 in 10 f; products pop 4 f stagger; a slow 2° rotation | A category of products or tools | TC-label (plates) · insert if third-party | bespoke + `fx.logoPlate` |
| **P-34** | FACE-CUTOUT-REVEAL | overlay | W-paper: a grit statement in `ink` (Anton 200 px, "HIMSELF / REVEALED") with the person's cut-out (the creator's photo, or a public figure's real photo fetched from the web) or `fx.silhouette` in front of its middle; or tool icons orbiting the cut-out | Statement lines slam 4 f each; the cut-out pops 6 f; orbit 1 rev / 4 s | Introducing a person the story is about | TC-display · insert (person) | bespoke / `fx.silhouette` |
| **P-35** | MONO-STATEMENT | overlay | W-black: a B&W illustration or creator photo (GR-bw) with a grit statement above and a second line below that appends ("MOST PEOPLE GET DISTRACTED" / "ONCE" → "ONCE EVERY 2 MINS") | Image push 1.00 → 1.05; line 2 grows on its words (4 f per word) | A sharp fact about people or habits | TC-display · figure if a number | bespoke |
| **P-36** | ALERT-GRADE | footage-treatment | A-roll under GR-alert (red monochrome) + a ⚠ icon (160 px, paper with ink glyph) + a grit statement "PROBLEM" (paper 220 px) at chest | Grade strobes on the word (every 1–2 f for 0.75 s; §4.4), then holds and releases on a cut; ⚠ and statement appear only on the red frames, statement slams 5 f on the first | `warn` lines; the re-hook; the escalated last item | TC-display · grade event | z11 overlay (`mix-blend-mode: color`) + scene |
| **P-37** | WORD-DISINTEGRATE | overlay | W-paper: a grit word in `ink` ("CRUSH YOU") with a small chip above ("AI"); it breaks into 40–60 seeded particles that drift right | Hold 0.6 s, then particles over 12 f (`ctx.rngStable`) | "replace", "destroy", "crush" lines | TC-display | bespoke canvas scene |
| **P-38** | DM-SHARE-MOCK | overlay | A recreated generic chat screen (dark, no platform logo): the creator's video thumbnail as a sent message + a typed bubble with the spoken line ("bro, let's do this together?") | Bubble types 1 word per 3 f; send 4 f | The "send this to a friend" CTA | TC-label · insert (created) | `VEOS.fx.appUI({kind: "chat"})` |
| **P-39** | CALL-FRAMES | overlay | W-grid: two framed stills (the creator's call screenshots, 10 px white border, soft shadow) stacked; a neon hand tag with an arrow names the person (only the name the script says) | Frames drop 8 f, 4 f stagger; arrow 10 f; tag 6 f | "I hired him over a call", testimonials the creator owns | TC-label · ink · insert (creator) | `VEOS.fx.shot` × 2 + arrow scene |

**B-7 CTA and end**
| ID | Name | Type | On screen | Motion | Use when | Class · needs | Engine |
|---|---|---|---|---|---|---|---|
| **P-40** | QR-CARD | overlay | W-white: the creator's QR image 560 × 560 centred (top y 520), CS-4 captions in ink above and below (§6.7) | White flash in (T-04); QR scales 0.96 → 1.00 in 8 f; stays still for the scan | CTA `qr`; also the mid-reel flash | asset | `VEOS.fx.shot({asset: "qr", chrome: false})` |
| **P-41** | END-LOCKUP | overlay | W-black: three-tier lockup centred: connector (Inter Tight 700 48 px) above-left, grit hero (Anton 260–320 px), trailer (48 px) below-right ("one last push / 90 DAYS / before 2026 ends") | Connector 6 f, hero slam 5 f, trailer 6 f; hold 1.5–3.0 s; hard end | `end_card` close | TC-display | bespoke, `kind: "end-card"` |
| **P-42** | OFFER-CARD | overlay | W-black: lockup ("NOT JUST A / VIDEO EDITING / COHORT 14": connector 44 px caps, neon Barlow 700 200 px, trailer 44 px), a scarcity line from the script ("100 seats left", 44 px), a glowing code line in `primary` ("USE CODE …", 52 px), the URL 40 px | Lines appear per spoken phrase 4 f; the code glow breathes | Promoting the creator's own product (numbers only from the script) | TC-display/label | bespoke, `kind: "end-card"` |
| **P-43** | KEYWORD-HERO | overlay | A-roll: the CTA keyword as a neon grit hero behind the head, connector "comment" above-left (§6.7) | As P-01; the keyword glow breathes ±8% | CTA `comment_keyword` | TC-display · behind | scene `kind: "cta-keyword"`, `behind: true` |

### 8.4 Line → pattern lookup
Vocabulary, not a decision table: it tells you what this style reaches for. Ask what the moment needs, then use it.

| Line type | Primary | Alternates |
|---|---|---|
| A money amount ("₹1,20,000 a month", "₹60 a day") | P-03 neon odometer behind the head | P-15 pin-on-line, P-12 card |
| A count of items ("3 skills", "5 habits") | P-01/P-05 grit hero + P-20 tiles | P-21 icon pair |
| A duration or year ("5 years since", "90 days") | P-13 ruler + P-04 count steps | P-06 ticker |
| Zero → result ("from ₹0 to …", "92 kg to 76 kg") | P-09 prop pair tags | P-10 vessels (no props), P-14 slider |
| A threshold / sweet spot ("5–6 projects", "35–40 minutes") | P-14 stat slider | P-15 |
| Naming a skill, tool or category | P-24 glass card | P-01 grit hero, P-33 product circle |
| A mechanism / pipeline ("it scrapes, filters, writes") | P-25 glass flow (L-graphic for a glance, then L-stack) | P-26 table |
| A routine or step list the creator walks through | P-26 step table in L-stack | P-22 recap |
| A person's story ("this 18-year-old built…") | P-02 hero + P-11 tag on the photo prop, then P-30 headline card | P-34 cut-out reveal (silhouette if there's no photo) |
| A news or public fact | P-30 headline card (the real article, fetched; exact words) | — |
| The creator's own team, office, clients | P-32 people topline / P-31 clip | P-39 call frames |
| A product or device | P-33 product circle / P-31 clean clip | P-11 tag on the real device |
| Examples of work ("project 2, 3, 5") | P-27 site cards with tags | P-28 chip words |
| A warning / problem / mistake | P-36 alert grade + "PROBLEM" | P-07 statement |
| A principle or quote to remember | P-07 statement bleed | P-35 mono statement |
| "Replace / crush / destroy" | P-37 disintegrate | P-07 |
| Either/or choice | P-23 branch map | P-21 icon pair |
| Funnel or result metrics stated | P-16 metric tiles | P-03 for the single biggest one |
| Without a credential ("without a degree / college") | P-12 card "DEGREE" (real or drawn) | P-01 grit "NO DEGREE" |
| Reaching out to people ("send cold emails", "outreach") | P-25 glass flow | P-38 chat mock |
| Building proof ("build a portfolio") | P-18 spotlight sheet (if a step) / P-27 site cards | P-24 |
| A daily quantity ("eat 120 g protein") | P-03 neon number + P-31 clean clip of the thing | P-12 card |
| A daily count or distance ("walk 8,000 steps") | P-13 ruler (steps axis) or P-15 pin | P-03 |
| What most people do wrong ("most people quit in week 2") | P-35 mono statement + P-06 ticker | P-07 |
| Deliverable ("I've attached a document / guide") | P-29 doc folder | P-40 QR flash |
| "Send this to a friend" | P-38 DM mock | caption only |
| Comment / scan / link CTA | P-43 / P-40 / caption "link / in bio" | P-41 |

### 8.5 Data and truth
- Every displayed number is a figure in `plan/figures.json` written by `ctx.fmtNum`; counters land on the spoken word
  ±5 f. Kinds: `hero_number` (P-03), `counter` (P-04, P-06, P-09, P-16), `slider` (P-13, P-14), `line` (P-15).
- **Inputs** come from the script with the spoken words (`from: script, said: "one lakh twenty thousand"`), or `spoken@t`.
  Formulas from the safe set (`sum`, `diff`, `ratio`, `percent_change`, `per_period`, `compound`, `cagr`, `unit_convert`);
  most heroes are stated values (`none`).
- **Format** from `profile.numbers` (§5.5): `₹1,20,000` (full) on heroes ≤ 9 characters, `₹12.5 L` (short) beyond;
  percentages `99%`; durations as integers with the unit word.
- **Countable where possible:** "3 skills" = three tiles; "5 projects" = five cards; "₹0 → ₹1,00,000" = two glasses.
- **Same axes:** a result pair uses two identical vessels or tags at the same size; sliders keep one scale through the reel.
- **Claims are real, illustrations are free.** The creator's results, earnings, prices and testimonials are their own or
  script-stated. A roll that only suggests growth, or a generic UI, may carry made-up but realistic numbers, with no label
  (`illustrative: true`).
- Example (§14.3): `{"inputs": {"salary": {"value": 120000, "from": "script", "said": "one lakh twenty thousand"}}, "figures": [{"id": "salary", "kind": "hero_number", "formula": "none", "value": 120000, "steps": [{"value": 120000, "at": 4.95}], "format": {"currency": "₹", "style": "full"}}]}`.

### 8.6 Anchors and the ink layer
- **Anchor targets:** `prop:<label>` (the red glass, the green glass, the photo, a desk chip), `object:<label>` (a laptop, a
  card), `face` (the hero placement and the chest caption use the engine's face boxes).
- **Mode `static`.** In the anchor pass (§1) read sampled frames of the hook take and write one anchor point per target per
  shot (x, y of the prop's rim centre). Tags sit 40 px above that point; arrows end 12 px short of it. If the prop moves
  more than 60 px during the tag's hold, end the tag at the next cut instead of following it.
- An anchored element keeps clear of the head region (about 40 px); a tag's text never sits below y 1500.
- **Ink stroke:** `paper` on dark grounds, `ink` on light ones (or `primary`), 5–7 px, round caps, wobble 1.2 px, drawn over
  10 f with an 8° overshoot at the head. Marks: arrow, curved arrow (P-11, P-27, P-39), branch (P-23), underline (under a
  card word, 6 f). Labels: Permanent Marker 44–60 px caps (§5.4).
- At most two marks on screen; marks finish drawing before the next scene starts; an arrow always ends on its target.

### 8.7 Assets
- **Real first:** the creator's own props, B-roll, screenshots and QR image.
- **Allowed mocks:** generic, unbranded UIs (`fx.appUI`, `fx.device`); never a look-alike of a real brand; made-up but
  realistic numbers inside them are fine (`illustrative: true`, no label), never the creator's results invented.
- **No stock clichés.** A product is the creator's photo of it, or its real logo (the creator's file, else fetched from
  the web) on an `fx.logoPlate`; the name set in type only when no logo can be found.
- **Third-party moments:** fetch the real thing, source noted (§12.4).
- **No comedy layer.** The reference has no gags; the energy is the cut. If the creator wants a light touch, a sticker
  (emoji or a 1–2 word chip, 6 f pop) lands only between heroes, beside the face, with no meme sounds.

---

## §9 Transition system

### 9.1 Library (measured at full frame rate, converted 25 → 30 fps)
| ID | Transition | Frames | Recipe | SFX role |
|---|---|---|---|---|
| **T-01** | Jump cut + crop change | 0 | Hard cut on a word boundary ±1 f; the crop changes on the cut (Z-1 / Z-2; 49 of 56 measured face-to-face cuts change crop, median ×1.32). The bulk of all boundaries (≈ 60–70%) | none |
| **T-02** | **Zoom-blur cut** (no streak bars: none in the reference) | 3 + 3 | Built in: `{"t": <cut>, "type": "zoom-blur", "frames": 6, "pre": 3, "punch": 0.12, "amount": 0.18, "at": "face", "layers": "all"}`: the outgoing shot pushes 1.00 → 1.12 into the cut with a blur ramp, the incoming one arrives ≈ 1.10 and blurred and clears in 3 f; `layers: "all"` so captions and heroes blur with the picture (v01 @0:06.46, @0:17.79). No camera events and no z11 defocus scene | whoosh |
| **T-03** | Punch cut | 0 | = T-01 into the tight or mid level (Z-1 with `crop: "tight"` or `"mid"`) or back to wide (Z-2); always a different level from the shot before | none (soft tap on a hero) |
| **T-04** | White flash | 1 (2) | One full-white frame on the cut: `{"t", "type": "flash", "frames": 1, "pre": 0, "peak": 1}` (pure white, or `colour` = white tinted 8% toward `primary`, v05 @0:33.33). Major (2 f) into a new take or the re-hook (v03 @0:28.57): two 1 f flashes on consecutive frames, `peak: 0.7` on the frame before the cut, then `peak: 1` on the cut. Captions stay on top (`layers` default) | camera / shine |
| **T-05** | Smoke dissolve | 12 | `fade-through` 6 f + a smoke overlay scene (blurred white clouds, 0 → 40% → 0) over 12 f into W-space | riser end |
| **T-06** | Focus pull in | 6 | The incoming shot starts defocused, built in on the footage: `"blur": [{"t": <cut>, "kind": "defocus", "px": 20, "frames": 6, "shape": "decay"}]`, always with a Z-6 settle-out under it (v04 @0:00: `p.land: 1.5`, 13 f) | none |
| **T-07** | Split cut | 0 | Hard cut into L-stack; the top graphic is already settled on the cut frame (v03 @0:12.87) | pop |
| **T-08** | Disintegrate out | 12 | P-37 particles leave, then a hard cut | swish |
| **T-09** | Hard end | 0 | Last frame ≤ 6 f after the last word; no fade, no black tail | none |
| **T-10** | Card push | 12 | The current glass card rises 60–80 px, defocuses to 10 px and dims to 50% (it stays as a ghost above); the next card rises from 300 px below, scaling 0.5 → 1.0 with blur 12 → 0 over 12 f; its title types on at 1 letter/f (v01 @0:12.9) | swish (soft) |
| **T-11** | Panel push | 13 | Horizontal push, built in: `{"t", "type": "push", "dir": "left", "frames": 13}`: the outgoing world (footage window and world together) slides out left while the incoming shot slides in from the right, ease in-out, peak ≈ 130 px/f (v04 @0:53.8). Graphic → face returns only | swish |
| **T-12** | Flicker montage | 5 per clip | 5–8 creator clips of 5 f each (0.16 s at 25 fps) under one caption, one shared treatment (`neon_mono`), entered by a 2 f overexposed T-04 (v05 @0:06.52–0:07.56); ≤ 1.5 s in all | riser end / hit |

### 9.2 Grammar
| Boundary | Use | Never |
|---|---|---|
| Frame 0 | Z-6 settle-out (or T-06 + Z-6 from 1.5) or Z-4 settle-push on live footage | A static frame, a fade from black |
| Into the hook hero | Hero slam on its word (no cut needed) | A hero that appears without motion |
| Hook → first insert | T-04 flash or T-02 zoom-blur cut on the noun | A crossfade |
| A-roll ↔ A-roll | T-01 / T-03 with a crop change (wide → tight → mid → wide …) | A cut that keeps the crop: it reads as a glitch |
| Inside a long A-roll shot | One animated move: Z-3 blur-punch on the claim word, Z-4 settle-push, or Z-6 settle-out on a new take | A zoom that bounces back inside the shot |
| Into B-roll / a new take | T-04 flash (1 f) or T-02 | A slow dissolve |
| New item | G-4 cut into the marker world (T-05 smoke the first time into W-space; T-02 otherwise) | A slow dissolve |
| Back to the face | G-6 return punch (Z-1 tight first), or T-11 from a graphic world | A world fade |
| Card → card | T-10 card push | A still jump |
| Number lands | Glow ignite on the number (no camera shake: none in the reference) | Shake |
| CTA | T-04 white flash into W-white (QR) or a T-01 cut to the keyword hero | A zoom-blur during the CTA words |
| Last word | T-09 | A black tail |

### 9.3 How the moves breathe
The jump cut with a crop change is the heartbeat: it's most of the cuts and it's silent. The zoom-blur cut and the
blur-punch are the accents: on a new take, a hero moment, a claim word, a number. The white flash is the doorway into an
insert or a new take; flash as often as the style calls for. The smoke dissolve, the disintegrate, the panel push and the
flicker montage are events: each is a moment the reel builds toward, so each keeps its surprise. Vary the accents so the
eye never predicts the next one; the wide-tight alternation is the one deliberate repeat, because it's the rhythm itself.

For reference, measured on v01–v05 (a description, not a target): 25–48 cuts a minute; zoom-blur cuts and blur-punches
together 8.5–18 a minute; one-frame flashes 3–14 a minute (v05 14, v01 7, v04 6).

---

## §10 Motion tokens, camera and zoom, layers, finishing

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
| Hold | Titles ≥ 10 f after built; text ≥ 0.25 s per word; heroes ≥ 1.5 s (≥ 0.6 s minimum) |

### 10.2 Footage camera (`zoom_policy: presets`)
Measured with ORB affine tracking on every frame of v01–v05. Crop levels (face width vs the reel's widest A-roll crop):
**wide 1.00 · mid 1.15–1.22 · tight 1.30–1.45** (median crop change on a cut ×1.32; v04 reaches ×2 on 4K-class sources;
the 1080p cap is 1.35). On top of the cut crops, an animated move about every ten seconds (measured 0.3–1.1 every ten
seconds, median 0.8). Every move **holds until the next cut**: no zoom ever returns to its start inside a shot.

| ID | Preset | Measured (reference) | Recipe (30 fps) | Use |
|---|---|---|---|---|
| **Z-1** | `snap-punch` "tight on the cut" | crop jumps ×1.21–1.39 on the cut frame, then creeps +2–4% over 6 f (v01 @0:25.16 ×1.38, @0:49.56 ×1.29; v02 @1:14.88 ×1.28; v03 @0:48.52 ×1.21) | On the cut: `{"t", "preset": "snap-punch", "crop": "tight"}` (1 f, 1.325 = the preset's `levels.tight` midpoint) or `"crop": "mid"` (1.185), held to the next cut; crops are about the face | The tight / mid half of the alternation (hype, explain, warn, win) |
| **Z-2** | `pull-out` "wide on the cut" | — | `{"t", "preset": "pull-out"}`: → 1.00 (the wide level) in 1 f on the cut | The wide half, takeaways, CTA |
| **Z-3** | `crash-zoom` "blur-punch" | 1.00 → 1.26–1.44 over 8–13 f, peak speed +8–10%/f at f3–f5 with motion blur (v04 @0:07.72 ×1.26, @0:32.72 ×1.44; v05 @0:02.96 ×1.30) | 1.00 → 1.30 over 12 f, `ease: "inOut"` (peak speed mid-move, as measured), engine motion blur; behind heroes ride it (`follow_footage: true`). On a mid / tight crop write `p.from: "inherit"` with `p.scale` ≤ 1.35 so it pushes on from the crop on screen instead of snapping back to 1.00 | On the claim / number word mid-shot; hero moments |
| **Z-4** | `settle-push` | 1.00 → 1.10–1.19 over 7–16 f, ease-out (v01 @0:00.24, @0:05.0, @1:27.4; v02 @0:00.08, @0:32.64; v03 @0:00, @0:32.96) | 1.00 → 1.12 over 14 f (1.18 / 8 f at f0) | f0, explanations, the recap, the last line |
| **Z-5** | `rotation-snap` "dutch roll" | ≈ 1°/f for 5–6 f → 5–6° with a 1.05 push (v05 @0:25.7, @0:31.7) | 0 → 5° with scale 1.16 over 7 f, linear, reset at the next cut | The re-hook, a warning, a "wait" beat: a tilt that says "listen", spent where the reel turns |
| **Z-6** | `settle-out` | starts zoomed and eases out: 1.22 → 1.00 / 12 f (v05 @0:00), 1.53 → 1.00 / 13 f under a defocus (v04 @0:00), 1.15 → 1.00 / 15–23 f on new takes (v03 @0:29.92, v05 @0:18.36, v01 @0:30.28, @1:15.04) | `land: 1.22` → 1.00 over 12 f, ease out (`p.land` up to 1.5 with T-06, `p.frames` 13) | f0, the first frame of a new take, after a T-02 |
| **Z-7** | `zoom-through` "crash-in" | accelerating 1.00 → 1.56 over 18 f, ends on a cut (v01 @0:08.56) | 1.00 → 1.5 over 20 f (`ease: "in"` in the preset), cut on the last frame | Into a graphic world on its noun; an entrance, saved for the world that deserves it |

- Every cut changes the crop level; change the kind of animated move from one to the next so the camera feels alive, not
  mechanical.
- Camera moves sit ≥ 0.4 s apart; never an animated move during the CTA words.
- A 1080p source allows ≤ 1.35× total (crop × move); 4K is needed beyond. Zooms never push the face out of the frame.
- A behind hero rides every camera move (`follow_footage: true`), as in the reference (v04 @0:32.7 "15 DAYS" grows with the
  punch); cap Z-3 at 1.15 while a hero is up so the hero stays ≥ 90% inside the frame and readable behind the head.
- Captions never move with the camera.

### 10.3 Tone decides the treatment
| Tone | Colour | Camera | Also |
|---|---|---|---|
| `hype` | `primary` | Z-1 snap-punch | a neon number or grit word hero |
| `explain` | `accent` | Z-4 settle-push | W-glass |
| `warn` | `bad` | Z-5 dutch roll | GR-alert |
| `win` | `good` | Z-1 snap-punch | the reached result glows |
| `cta` | `primary` | Z-2 pull-out | W-white |

### 10.4 Diagram travel
The hub and the glow flow travel inside one scene by translating and scaling the diagram (eased, ≥ 18 f per move); there
is no canvas camera in this style.

### 10.5 Layer order (back to front)
1. World background (z1) / footage
2. **Behind heroes (`behind: true`, z3): grit words, neon numbers, the keyword hero, statement bleeds on A-roll**
3. The person cut-out (matte): the head and shoulders occlude the hero
4. Cards, clips, data (z3–4)
5. Hand tags, labels, prop tags (z5)
6. Markers (z6)
7. Captions (z7, CS-1…CS-4)
8. Statements and end lockups (z8; captions hide)
9. Smoke and grade overlay scenes (z11, momentary). Flashes, the zoom-blur cut, the panel push and the footage defocus are
   drawn by core (`timeline.transitions` / `timeline.blur`), not as scenes

### 10.6 Finishing
- No film grain on footage, no vignette on footage (the room is shot dark already). Vignette lives only inside worlds
  (§3.1) and the `bw_vignette` treatment.
- Grit texture only on Anton heroes and statements; glow only on neon numbers, the active node, tokens and the offer code.
- Cards: radius 28–36, soft shadows (0 20 60 rgba(0,0,0,.45)); no hard offset shadows anywhere.

---

## §11 Sound

The reference reels' sound couldn't be measured, so this is a decision, not a measurement: sound marks the picture's events
and never plays on its own.
| Line | Direction |
|---|---|
| **Where sound goes** | The hook (an f0 hit, the hero impact, the counter roll); transitions (T-02 zoom-blur whooshes, T-04 flashes, T-05 smoke, T-11 pushes); reveals (heroes, counters landing, cards, tiles); the **list cue** (one file for every item marker, the one sound allowed to repeat); the CTA (the QR flash or the keyword hero). Jump cuts are silent |
| **Meme sounds** | None |
| **The bed** | On; it enters on the first item marker, after the hook |
| **Ducking** | The bed sits ≥ 18 dB under the voice while the voice speaks |
| **Silence** | Nothing in the 1.0 s before the first CTA word |
| **Loudness** | −14 LUFS integrated, true peak ≤ −1.5 dBTP; a hard end ≤ 6 f after the last word |

Sounds come from the bundled SFX catalogue: no file more than twice in a reel except the list cue, never the same file back
to back, every cue on a picture event. Dense where the picture is dense (the hook), sparse on the takeaways.

---

## §12 Footage handling

### 12.1 Setups
| Setup | Spec |
|---|---|
| **A: desk, front-on** (all A-roll) | Seated at a desk, camera at eye level 70–90 cm away, vertical 1080 × 1920 or 4K; low-key warm practicals behind (lamp bokeh, a shelf); a dark or earth-tone plain tee/hoodie (no big logos: captions sit on the chest); the desk surface visible in the bottom 15–25% for props. **Framing:** head top y 300–560, eyes y 620–820, chin y 800–1050, face x 330–750 (the hero needs 160–480 px of room above the head) |
| **B: side angle** (optional) | The creator working at the same desk from three-quarter or profile, 3–6 s per clip, for statement bleeds and focus beats |
| Frame rate / audio | 25–60 fps (conformed to 30 CFR); a lavalier or shotgun mic out of frame |

### 12.2 Shots and fallbacks
| ID | Shot | Spec | Without it |
|---|---|---|---|
| **SH-1** | A-roll (must) | The whole script at the desk (setup A); retakes welcome (they become jump cuts) | — |
| **SH-2** | Hook prop take | The first 3–4 s performed with 1–2 props in hand or on the desk at chest-to-desk height (PR-1…PR-5) | **FB-2:** P-10 result-pair vessels or a drawn P-12 card/photo, in the L-stack top band or on W-glass, with the same tags and counters. No tangible object in the hands; the hook loses its physical surprise (degraded) |
| **SH-3** | Handwritten cards | White card or paper, black marker, 1–2 words or a number ("₹60/DAY"), shown to the lens on the word | **FB-3:** the P-12 drawn card pops beside the creator at chest height, clear of the face. No in-hand action (holds) |
| **SH-4** | Own B-roll | 1–3 s clips: team, office, clients, the product, the city, life moments the creator owns | **FB-4:** an engine visual on the noun: P-24 glass card, P-33 circle with logo plates, a silhouette, or P-31b (an A-roll punch with a treatment). Fewer real-world cutaways (holds) |
| **SH-5** | Screens | Screen recordings or screenshots of the named tools, sites, documents (creator-owned) | **FB-5:** the real page captured from the web in a P-27 card; else `fx.appUI` / `fx.device` recreated generic UI, or a P-24 card with the real logo. No real product footage (holds) |
| **SH-6** | Side angle | Setup B, 3–6 s | **FB-6:** a Z-1 tight punch of the A-roll with GR-bw behind the statement. No second angle (holds) |
| **SH-7** | CTA target | The QR image (PNG, ≥ 600 px), or the URL, or the keyword | **FB-7:** switch the CTA to `comment_keyword` (P-43) or `link_bio`; never draw a QR. No scan action (holds) |
| **SH-8** | Desk list | 3–5 chips/tokens/cards in a row on the desk for list reels | **FB-8:** the P-19 token carousel carries the count. No physical list (holds) |

The plan lists every fallback the reel uses.

### 12.3 Props, the reaction bank, the cut-out, resolution
- **Props:** PR-1 two clear glasses (red-tinted / green-tinted water) for result pairs; PR-2 a printed photo of the story's
  subject (creator-owned) or of the creator; PR-3 2–4 handwritten cards; PR-4 3–5 chips or tokens; PR-5 the device or
  product the reel is about.
- **Reaction bank** (2–3 s each, optional): pointing at the lens; counting fingers 1–5; palms-up shrug; leaning in.
- **The cut-out (required):** the engine's matte over the whole clip; hair checked at 200% where heroes sit.
- **Resolution:** a 1080p source allows punches ≤ 1.35×; 4K allows 2×. Z-1 is 1.325× (works on 1080p).

### 12.4 Third-party moments: fetch the real thing
When the reel names a real person, news story, company product, another creator's clip or a brand, the viewer should see
the real one.
1. The creator's own files in their folder come first.
2. Otherwise search the web and fetch it: the real logo, the real headline and article, the real product page (captured
   and framed on the part that matters), a public figure's real photo. Note where it came from.
3. Use it as it is (crop, frame, highlight), never altered to say something it doesn't; a headline or post is shown word
   for word.
4. **Nothing usable to be found:** rebuild it from its exact words (no labels, no credit lines):
   - a person's photo → `fx.silhouette` (P-34 variant) with the name from the script;
   - a news story → `fx.headlineCard` (P-30) with the exact headline words;
   - another product's screen → `fx.appUI` generic UI (P-27);
   - a logo → `fx.logoPlate` (the name set in type);
   - another creator's clip → `fx.appUI({kind: "video"})` with a caption, or a P-24 card.

Patterns that show third-party material: P-27, P-30, P-34, P-39.

### 12.5 Frame rate and audio
30 fps CFR output, 1080 × 1920, BT.709. Voice chain: high-pass 80 Hz, de-ess, light compression, −14 LUFS.

---

## §13 What your plan should settle

Your `ideas.md` is a page or two, for you. In this style it has decided, before any code:
1. **The tone of every line,** and so every beat's colour, camera move and world (§10.3).
2. **The hook:** the archetype, the prop (or its fallback), the connector + hero line with its two alternates, every hook
   beat to the frame, the frame the hero lands on (by 1.7 s).
3. **Every hero:** its text, recipe (P-01…P-06, P-43), placement against the head (centre, head gap, lockup), colour
   (`paper` or `primary`), hold, and the caption words it drops.
4. **The caption keyword of every chunk,** and every override (CS-2 spans, dropped words, forced or blocked keywords).
5. **The numbers:** a performance and a figure for every amount, count, duration and year.
6. **The cut map:** every jump cut on its word boundary with its crop level (wide / mid / tight), every animated move,
   every insert on its noun with its treatment, every layout switch and world, every transition.
7. **The structure:** the marker and the ritual, the re-hook, the escalated last item, the recap.
8. **The anchors** for every prop tag, counter and hand arrow, from the anchor pass.
9. **The inserts** (the creator's, fetched or rebuilt) and the fallbacks used.
10. **The sound:** the cue moments, the list cue, the bed's entry.
11. **The CTA:** the device, the mid flash, the end.
12. **The moments you'll look at hardest on the storyboard:** f0 (the thumbnail); the hero at 1.7 s, readable, with the hair crossing it
    cleanly and nothing in front of the head; one item marker; one glass card; one stylised clip; one L-stack frame (the
    caption clear of the window and of the graphic's text); the CTA.

One hero beat, fully decided:
```yaml
- section: HOOK
  t0: 0.84
  t1: 2.10
  spoken: "you can make up to one lakh twenty thousand rupees per month"
  trigger: {word: "twenty", at: 1.12}
  tone: hype
  layout: L-full
  visual: "Neon ₹1,20,000 rolls behind the head and ignites lime; caption 'rupees / per month' on the chest"
  pattern: P-03
  caption: {profile: CS-1, keyword: "rupees", drop: ["one", "lakh", "twenty", "thousand"]}
  hero: {pattern: P-03, text: "₹1,20,000", kind: number, placement: centre, colour: primary, hold_s: 2.2}
  figure_id: salary
  camera: Z-1
  transition_in: T-01
```

---

## §14 Worked examples

Times are planning estimates: take the real ones from the words. They show the standard; match it, then beat it.

### 14.1 Careers and money: "₹0 to ₹1 lakh a month editing videos as a student" (HA-01, SM-2, TH-lime, CTA qr)
Props: PR-1 two glasses (red, lime-green). 72 s.

| t (s) | Spoken | Tone | Visual | Caption (CS-1) | Camera / transition |
|---|---|---|---|---|---|
| f0 | — | hype | Desk, red glass left, green glass right; the creator mid-gesture; Z-6 settle-out | — | Z-6 |
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

Figures: `zero` (0, script "zero"), `target` (1,00,000, script "one lakh"), `pct_fail` (99, script), `projects` (5–6 range,
script), `gigs` (216, script). Mid-CTA QR flash at 44 s (61%).

### 14.2 Fitness and nutrition: "Stop doing these 3 exercises if your back hurts" (HA-05, SM-1, TH-mint, CTA comment_keyword "BACK")
No props. 58 s.

| t (s) | Spoken | Tone | Visual | Caption | Camera |
|---|---|---|---|---|---|
| f0 | — | hype | Connector "Stop doing these" fades in at y 140–220, above-left and clear of the head; Z-4 settle-push | — | Z-4 |
| 0.17 | "these" | hype | P-01 grit "3 EXERCISES" slams in behind the head (lockup by 0.7 s) | — | — |
| 0.8 | "if your back hurts" | warn | Hero holds | "if your / back / hurts" (keyword "back") | Z-1 |
| 2.2 | "every morning" | warn | P-20 three icon tiles (back, dumbbell, clock) pop at chest-bottom | "every / morning" | Z-2 |
| 3.0 | "number one" | explain | T-05 smoke dissolve into W-space; P-17 hub overview, node 1 lights | "number / one" | — |

| Section | Spoken (gist) | Tone | Layout / world | Patterns | Hero |
|---|---|---|---|---|---|
| Item 1 3–15 s | "Toe touches with straight legs" | warn → explain | SM-1 node 1 "TOE TOUCH"; L-full; own clip of the wrong form (`bw_vignette`), then the right form (`clean`) | P-17, P-31 ×2 | P-01 "TOE TOUCH" |
| Item 2 15–27 s | "Sit-ups load the spine" | explain | SM-1 node 2; P-07 statement bleed "YOUR SPINE / ISN'T A HINGE" behind the creator; P-12 drawn card "PLANK" | P-17, P-07, P-12 | — (the statement is the hero beat) |
| Re-hook 27–30 s | "The third one surprises everyone" | hype | Z-5 dutch roll; P-01 "LAST ONE" behind the head | — | P-01 |
| Item 3 30–44 s | "Heavy deadlifts in week one" | warn | SM-1 node 3; P-36 GR-alert + "PROBLEM"; P-13 day ruler "WEEK 1 → WEEK 6" | P-17, P-36, P-13 | P-04 "6 WEEKS" (figure) |
| Recap 44–50 s | "So skip these three" | explain | SM-1 overview returns: "SKIP THESE / 3" + all nodes lit | P-17 | — |
| CTA 50–58 s | "Comment BACK and I'll send you my 10-minute routine" | cta | P-43 keyword hero "BACK" (mint glow) behind the head, connector "comment"; caption "and I'll send / my 10-minute / routine" | P-43 | P-43 |

Figures: `weeks` (6, script), `routine_min` (10, script).

### 14.3 Careers and money, a story reel: "This 19-year-old makes ₹1,20,000 a month without a degree" (HA-08 default, SM-4, TH-yellow, CTA end_card + link_bio)
Props: PR-2 a printed photo of the creator's own student (consent given; creator-owned), PR-3 card "DEGREE". 64 s.

| t (s) | Spoken | Tone | Visual | Caption | Camera |
|---|---|---|---|---|---|
| f0 | — | hype | The creator holds the photo to the lens, mid-motion; Z-6 settle-out; T-04 1 f white flash on the photo at 0.5 (the v02 polaroid flash) | — | Z-6 |
| 0.0 | "the story of this" | hype | Connector "the story of this" top-left, beside the head (P-05) | (dropped: the connector shows it) | — |
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
| Numbers 26–40 s | "Two years ago he joined our first batch" | explain | P-13 year ruler "2024 → 2026", the current year yellow; L-stack P-30 headline card (the real article, fetched) only if the script quotes one (else none) | P-13 | P-04 "2 YEARS" |
| Lesson 40–54 s | "Skills beat degrees when you show proof" | win | P-07 statement "SKILLS / BEAT / DEGREES" on a creator clip; P-27 his portfolio site card (creator-owned) + tag "HIS SITE" | P-07, P-27 | — |
| CTA 54–64 s | "If you want the same roadmap, link in bio" | cta | Caption "link / in bio" + arrow; then P-41 end lockup "one last push / 90 DAYS / before 2026 ends" 2.5 s; hard end | P-41 | — |

Figures: `age` (19), `salary` (1,20,000), `daily` (60), `years` (2). Inserts: I1 the student's photo (creator), I2 clips
(creator). No third-party media.

---

## §15 Your look at the storyboard: the checklist

Watch it once as a stranger with a thumb over the next reel, then once as the editor whose name is on it. Fix what
bothers you, in one pass.

**The style (does it feel like §The feel?)**
- Frame 0 is already moving, the face and the prop (when used) in frame, the first caption word by f3; the hook hero
  lands by 1.7 s and reads at thumbnail size.
- Every caption builds word by word in two tiers, keyword 136 / connector 56 / plain 72 (ratio ≥ 1.7), one keyword at
  most per chunk, and the keyword is the word you'd underline.
- Every cut changes the crop; animated moves land on claims and numbers and hold to the next cut; nothing ever bounces
  back.
- Every number is performed, never just shown.
- Inserts are glances on their nouns, treatments rotating; the face is never more than a glance away.
- Every item follows the ritual with one marker style; the re-hook lands near the middle; the last item is the biggest.
- One neon, white words, red/green only as a pair; the takeaways are quiet.
- Start to end: it never lets you settle, and at every moment one thing shouts.

**Craft (by eye, in context)**
- The creator's face reads whenever the moment is about them; on L-stack frames the caption ends above the window. Nothing
  chops the head or buries the face by accident.
- Every behind hero reads: most of it visible, first and last letters clear of the head, the hair crossing it cleanly;
  one at a time.
- No text over text by accident: one hero, one tag, the caption; the hero's words dropped from the caption; the L-stack
  graphic's text above the caption block.
- Every hero, insert, tag and counter lands on its word; cuts on word boundaries; nothing lingers after its point.
- Every number is what was said, formatted for the audience (₹ + Indian grouping, or $ + K/M/B); illustrations carry no
  labels; no invented results; fetched headlines and posts word for word.
- Names and brands spelt exactly; profanity masked; the hook's count = the items shown; every loop paid; the CTA
  keyword/URL/QR readable.
- Captions and heroes read at phone size; meaning text out of Instagram's button bands.
- The file itself (1080 × 1920, 30 fps, −14 LUFS, a hard end ≤ 6 f after the last word, no black tail) is the render's
  job; it checks it.

---

## §16 Build notes

- **Fonts:** Inter Tight 500–800, Anton, Barlow Condensed 600/700, Permanent Marker, Archivo Black or Unbounded 900 (the
  wide hook hero), Noto Sans Devanagari 700/800. Pre-paint ₹ ✓ ✕ ⚠.
- **Scene building blocks** (write them as helpers at the top of `plan/scenes.js`, then reuse them across the reel):

| Block | Role |
|---|---|
| `GritHero` | The grit word: Anton, the layered mask (§5.2), slam + smear ghosts + crackle, `behind: true`, `exception: "behind_text"`, `follow_footage: true` (P-01, P-02, P-05, P-07, P-43) |
| `NeonNumber` | `VEOS.data.counter({font: "numeric", glow: "primary"})` with tick, slot or steps, behind the head (P-03, P-04, P-06) |
| `PropTag` | Anchored tags and counters + SVG arrows (`stroke-dashoffset`) (P-08, P-09, P-11, P-44) |
| `GlassCard` | `VEOS.fx.card({theme: "glass"})` + the T-10 push (P-22, P-24) |
| `Diagram` | `VEOS.fx.diagram` inside one transformed scene for hub and flow travel (P-17, P-25) |
| `Clip` | `VEOS.fx.clip` + the treatment CSS (P-31, P-32) |
| `Alert` | The z11 `mix-blend-mode: color` overlay + ⚠ + the statement (P-36) |
| `EndCards` | `kind: "end-card"` (P-41, P-42), `kind: "cta-keyword"` (P-43), `VEOS.fx.shot({asset: "qr", chrome: false})` (P-40) |
| Camera and cuts | Z-1…Z-7 = `timeline.camera` presets; T-02 / T-04 / T-11 = `timeline.transitions`; T-06 = `timeline.blur` |

---

## Appendix A. Evidence map
The full map (every element → `vNN @ m:ss`), the measurement method and the unverified list are in `evidence.md`. In
short:
| Element | Source |
|---|---|
| Two-tier chest captions | v05 @0:02, @0:03, @0:06, @0:22; v02 @0:20, @1:14; v04 @0:40–0:48; v01 @1:16–1:17 |
| Hero behind the head | v03 @0:00.17–0:03; v02 @0:00.83–0:02; v05 @0:01–0:06; v04 @0:01–0:03, @0:32–0:33; v01 @0:07 |
| Punch-cut rhythm and the camera (measured per frame) | crop change on 49 of 56 face cuts; Z-3 v04 @0:07.72, @0:32.72, v05 @0:02.96; Z-6 v04 @0:00, v05 @0:00; T-02 v01 @0:06.46, @0:17.79; T-04 v03 @0:28.57, v05 @0:33.33 |
| Prop hooks | v01 beakers @0:00–0:04; v02 polaroid @0:00–0:03; v05 cards @0:03–0:04, @0:14–0:15; v02 chips @0:25–1:15 |
| Stylised inserts, rotating neon, QR CTA | v05 @0:07 halftone, @0:10 invert, @0:33–0:35 B&W; lime v01/v02, yellow v04, mint v05; QR in all five reels |

Not verifiable from the reels: the speech language and caption transform (no transcripts), all sound, exact hero land
times against the audio.

## Appendix B. Hook-title bank
`<…>` slots are filled per reel; **bold** = the hero. Write 8–10 per reel and pick by the stopper test.
| # | Template (connector + **HERO** + trailer) | Hook | For example |
|---|---|---|---|
| 1 | "you can make up to **<AMOUNT>** / per month / without <credential>" | HA-08 | "you can make up to **₹1,20,000** / per month / without a degree" |
| 2 | "Don't ignore these **<N> <THINGS>** / if you're <who>" | HA-05 | "Don't ignore these **3 SKILLS** / if you're 16–20" |
| 3 | "from **<ZERO> → <RESULT>** (two tags) / as a <role>" | HA-01 | "from **₹0 → ₹1 LAKH** / as a video editor" |
| 4 | "**<N> YEARS** / since I **<STARTED> <THING>**" | HA-07 | "**5 YEARS** / since I **STARTED RUNNING** a **CREATIVE AGENCY**" |
| 5 | "the story of this **<AGE> YO** / <who> will blow your mind" | HA-08 | "the story of this **19 YO** / student will blow your mind" |
| 6 | "Stop doing these **<N> <THINGS>** / if your <pain>" | HA-05 | "Stop doing these **3 EXERCISES** / if your back hurts" |
| 7 | "**<BEFORE> → <AFTER>** (two tags) / in <time>" | HA-01 | "**92 KG → 76 KG** / in 90 days" |
| 8 | "<verb> **<AMOUNT> <UNIT>** / <thing> every day" | HA-08 | "eat **120 G** / protein every day" |
| 9 | "day 1 to **<N> DAYS** / of <habit>" | HA-07 | "day 1 to **90 DAYS** / of walking" |
| 10 | "the only **<N> <THINGS>** / you need for <goal>" | HA-05 | "the only **3 TOOLS** / you need to start freelancing" |
