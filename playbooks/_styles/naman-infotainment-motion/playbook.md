# Naman · Infotainment Motion Style Playbook (template v2)

## The feel

This reel roasts the viewer, then saves them. The first frame is a fight: their sad, generic version of the thing, red
marker all over it, a yellow slab shouting at the top, and the creator already cut out in front of it, pointing like they
caught you. You stop because it's about you. Then it pays off: the bad version shatters, the premium one slides in under
a streak of orange light, and for a second it feels expensive. That's the whole promise: bad to premium, and you get to
watch the change happen.

After the hook it never sits still, but it is never random. Every number becomes something you can count: five friends on
a sofa, five thousand dots pouring in, a phone cracking. Every risk becomes a machine you understand without the jargon: a
bouncer, a gift box, a wall slamming up. The creator is always there, in the panel, in the bubble or standing in front of
the card, because people come for a person, not for slides.

The jokes are earned. When the creator mocks the viewer, the edit mocks with them: a stamp, a freeze, a meme hit in the
gap after the word. When they explain, it goes clean and quiet. When they reveal, it goes premium. Never mix them. It
breathes the way they talk: fast on lists, a hold before the reveal, a pop-back to the face for the opinion, the last item
bigger than everything before it. Yellow is the loudest thing on screen, always.

**The test:** if a frame could belong to any other creator's reel, it's wrong.

## What this playbook is

You're editing a talking-head reel (selfie or tripod) of a creator who teaches by building, fixing and comparing, and you
have the authority to make it the best reel in their niche. This playbook is the style: how it looks, moves, sounds and
thinks, pulled from a real creator's proven October reels (r01–r10) and his own written direction, then sharpened. Read
it all, every time. Use it the way a great editor uses a reference: take what fits this reel, invent when a moment needs
more, and never ship a frame that breaks the feel above.

**Who it's for and what it needs.** Creators who build or teach things people can see: apps, sites, tools, money, fitness
plans, anything with a bad version and a good one. Input: one talking-head take, ideally plus screen captures of what they
name and their own finished result; anything missing gets fetched from the web or built (§12). The person cut-out (matte) is needed in almost
every reel. Captions follow the creator's language (English, Hinglish or Hindi, set in their copy); the slab, chips and
labels are English, Instagram-native. Machine values live in `tokens.json`; where this text gives a number tokens also
holds, they agree.

### Style directives (non-negotiable)
| # | Directive | Where it lives |
|---|---|---|
| D1 | **The hook is a visual stopper.** Motion graphics in the first second make the reel stand out from everything else in the feed | §6.1, §6.2, VS-1…VS-8 |
| D2 | **Mocking tone gets meme sounds.** When the creator roasts the viewer's bad result or assumption, the beat gets the right meme hit | §11.3, tones §10.3 |
| D3 | **Result first, always.** The hook shows the viewer's *bad* result and then the creator's *premium* one ("ye tumhari website hai… aur ye maine vibe coding se banayi") | §6.2 |
| D4 | **The yellow Headline Slab is the strongest element.** It is the first thing people read | §5.2, §6.5, App. B |
| D5 | **Numbers, scale and risk become elite motion graphics.** 5 users vs 5,000 users, hacks, checks, money: the viewer *sees* what the creator *says* | §3.5, §8.3 P-40…P-60, §8.5 |
| D6 | **Bright colours:** yellow first, plus a disciplined set of bright accents, each with one job | §4 |
| D7 | **No sound file repeats more than 2× in a reel.** The one exception is the parallel list cue: item 1, 2, 3… share one sound | §11.2 |
| D8 | **Infotainment:** information + entertainment. Splits, coming back on screen, dynamic zooms and snappy zooms are the language | §3.4, §7.5, §9, §10.2 |

### Quick index
| § | What |
|---|---|
| §1 | Procedure: how to approach a reel in this style |
| §2 | Hard rules: the craft and the style's never-list |
| §3 | Worlds, screen modes, stage moves, safe zones, the person |
| §4 | Colour system |
| §5 | Type and captions: Headline Slab, CS-1 subtitles, CS-2 chunky, CS-3 glow, labels, stickers |
| §6 | Hook system: stopper test, Result-First Roast, alternates, result pairs, slab writing, CTA |
| §7 | Structure and rhythm: markers, item ritual, open loops, the energy curve |
| §8 | Visual system (B-roll and patterns): families, patterns P-01…P-68, line → pattern lookup, Data Theatre, comedy layer, assets |
| §9 | Transition system T-01…T-24 |
| §10 | Motion tokens, zoom system Z-1…Z-7, tones, layers, finishing |
| §11 | Sound: the ledger, meme sounds, pools, bed, mix |
| §12 | Footage handling: setups, crops, matte, reaction bank, fallbacks, inserts |
| §13 | What your plan should settle |
| §14 | Worked examples (4) |
| §15 | Your look at the storyboard: the checklist |
| §16 | Build notes |
| App. A / B | Evidence map / hook-title bank |

---

## §1 Procedure: how to approach a reel in this style

You watch, listen, plan, build and look at the storyboard yourself; the edit skill has the mechanics. These are the
decisions this style lives or dies on, in the order that makes them easy.

1. **Feel the tone of every line.** `hype` · `mock` · `awe` · `explain` · `warn` · `win` · `cta`. The tone decides the
   colour, the zoom, the caption treatment and the sound (§10.3). A line is `mock` when the creator roasts the viewer's
   result, assumption or habit ("wo ekdam bekaar hai", "paanch nithalle dost", "hackers ke liye gift"). Get this right and
   half the edit is decided.
2. **Find the result pair** (§6.4). What is the viewer's *bad* state, and what is the creator's *premium* or *fixed* state?
   Decide how each gets on screen: captured from the creator's own build, or built live as a generic, unbranded mock.
3. **Write the slab** (§6.5): 8–10 candidates, pick by the stopper test (§6.1), keep the next two as alternates.
4. **Plan the data story.** Every number, comparison and risk gets a Data Theatre machine (P-40…P-60) that makes the
   viewer *see* it (§8.5), with its figure in `plan/figures.json`.
5. **Plan the comedy.** Which lines are roasts, and what the edit does on each: stamp, marker, freeze, crash zoom, meme hit
   (§8.6, §11.3). Everything else stays clean.
6. **Plan the moves.** Worlds, panel drops, pop-backs, the bubble, the item ritual (§3.4, §7.3, §9.2). Decide where it
   holds still on purpose and where the last item escalates.
7. **Plan the sound ledger** (§11.2): every cue on a visible event, one list cue, meme files once each.
8. **Count on the cut-out.** The depth sandwich, the bubble, the lean-in and the silhouette strobe all need it (`matte:
   required`, so it starts right after the cut); make sure it's there before the storyboard.

---

## §2 Hard rules: the craft and the style's never-list

**Craft, by eye** (judge it on the storyboard, in context, the way an editor does):
- **Keep the person clear.** People come for the face, so keep it and the hair clear of front layers when the moment is
  about them. The framing that does it: the slab's bottom edge ≥ 40 px above the head top, captions at chest height,
  stickers, stamps and marker circles beside the face. When the moment wants otherwise (a sticker slammed on in a roast, a
  caption crossing the chin for a beat), that's editing; what's never fine is a head chopped or a face buried by accident.
  Behind the person is fair game: cards, objects and text (G-5).
- **No text over text.** A subtitle under a title, a sticker over the slab, a label across a chip: never by accident.
- **On the word.** Every tool, number, command, step and risk lands its visual 2 f before the word and is fully on within
  ±5 f; a tool card lands within ±1 f of the tool's name. Cuts sit on word boundaries ±1 f; audio is never offset.
- **Say what was said.** A number or quote the creator says is shown exactly as said. Illustrations may use made-up but
  realistic numbers and screens, with no label. Never present invented revenue, testimonials or dashboards as real.
- **Promise integrity.** The slab's count equals the items shown; every "end mein dunga" is paid off on screen; the CTA
  keyword is on screen.
- **Spelling.** Romanised Hinglish may be phonetic; English words and brand names are exact.
- **Readable.** Text holds ≥ 0.25 s per word and titles ≥ 10 f after they finish building. Contrast never fails: no white
  or yellow text on the white canvas, no dark logo on dark footage, no red or pink text on the night stage without a
  3 px white outline or a chip, no pink text on white without an ink stroke.
- **Audio.** −14 LUFS integrated, true peak ≤ −1.5 dBTP, the bed under the voice, a hard end ≤ 6 f after the last word,
  no black tail.

**Never in this style:**
- Readable code, stack traces or raw error logs as the main visual. Illegible code-shaped lines are fine as texture inside
  a scanner, magnifier or blur (P-52). Commands go in chips.
- Raw full-bleed screen recordings. Use a card, a device mock, the depth sandwich, or a short full-screen moment inside a
  frame.
- Meme sounds or comedy visuals on `explain`, `awe` or `cta` beats, or under a trigger word.
- Coloured words inside subtitles; Comedy Pink outside the comedy layer; more than yellow plus two bright hues in one frame.
- Clichés: hooded hackers, glowing robot brains, Matrix rain, random stock tech footage, money rain, stock charts going up.
  Show the mechanism instead (red cursors, a gift box, a data wall, a bouncer, a leaking bucket).
- Effect packs: RGB-split, film burns, lens-flare PNGs. A new move is welcome when it's built in this style's language.
- Visuals that only decorate. Every motion graphic shows the thing being said.

---

## §3 Worlds, screen modes, stage moves, safe zones

### 3.1 Worlds
| ID | World (timeline id) | Look | Carries | Enter / exit |
|---|---|---|---|---|
| **W-1** | **Studio** (`studio`) | The creator's own footage: low-key, warm practicals, not regraded | Claims, roasts, opinions, asides, the CTA | Hard cut, T-17 pop-back, zooms |
| **W-2** | **Canvas** (`canvas`) | `#FCFCFC` with a dashed `#C5C5C5` grid (2 px, dash 14/10, pitch 141 px) | Tools, sites, prompts, docs, step-by-step explanations | T-04 panel drop in; T-01 or T-17 out |
| **W-3** | **Data Stage** (`data`) | Night `#07070C`, cyan dot grid (`#00D8FF` at 10 %, pitch 60 px, r 2.2), a radial glow 700 px across (r 350) at 14 % drifting ±20 px | Numbers, scale, crashes, money, risk, comparisons | T-18 zoom-through or T-04 (dark); out with T-17 or T-01 |
| **W-4** | **Blueprint** (`blueprint`) | Navy `#091B31`, a fine `#1A3A50` line grid (1 px, pitch 30) with brighter major lines every 120 px (`#19394E`, 2 px) | Step-by-step items on a dark canvas (r09's "plan mode" items); the dark alternative to W-2 | T-04 in; T-17 out |

Switching worlds is a beat in itself: land it on an ordinal or a discourse word ("pehla", "but", "ab"). `S-DARK` is the
canvas split on the Data Stage world, the way the last item escalates.

### 3.2 Screen modes
The modes are how you think about the frame; each runs on one engine layout (`tokens.layouts`).

| Mode | What | Layout | When |
|---|---|---|---|
| `HOOK` | The Result-First Roast (§6.2): slab + result + the creator cut out in front (G-5), then the count and loop under the same slab | `L-full` | The opening, until item 1 |
| `F` | Full-frame talking head + CS-1 subtitles, alive with zooms Z-1…Z-7 | `L-full` | Claims, roasts, opinions, asides |
| `S` | Canvas split: card(s) on top, the creator in the panel below (`P-BLEED` top y 1135, or `P-INSET` x 12–1068, y 1008–1881) | `L-panel` / `L-inset`, world `canvas` | Tools, sites, prompts, how-tos |
| `D` | Data Stage split or full: the night stage running a Data Theatre machine; the creator in the panel or the bubble | `L-panel` / `L-inset` / `L-bubble`, world `data` | Every number, comparison and risk |
| `V` | Versus split: left/right halves on the same axes (bad vs premium, 5 vs 5,000); the creator in the bubble or a centre strip | `L-bubble` | A head-to-head |
| `R` | Reaction bubble: a full-screen B-roll or Data Stage with the creator in a circle | `L-bubble` | The visual must stay big while they react |
| `I` | An inset card in the top band over `F` | `L-full` + a card scene | A quick reference while they talk |
| `K` | A card over the creator's blurred self | `L-dim` (blur 14 px, luma −0.45) | A doc or quote that needs the whole frame's attention |
| `U` | A full-screen UI mock (the comment or share flow) | `L-hidden` | A short, framed moment; they're back a beat later |
| (G-3) | Slide-aside comparison | `L-slide` | Pointing at a duel, a tall phone mock beside them |

`S` and `D` share the panel and inset geometry; the world tells them apart.

### 3.3 Layout diagrams
**`S` canvas split (P-BLEED):**
```
┌─────────────────────────┐ 0
│  (IG top UI, keep clear)│ ← y 0–110
│   Tool Title (serif)    │ ← title band y 190–300 (or the step marker)
│  ╭───────────────────╮  │
│  │  CARD: real site, │  │ ← card zone x 24–1056, y 300–900, radius 40
│  │  prompt, doc, UI  │  │
│  ╰───────────────────╯  │
│   black subtitle here   │ ← CS-1 black, centre y = panel top − 60 (1075)
│╭───────────────────────╮│ ← SPEAKER PANEL top y 1135, top radius 64
││  the creator (footage)││   x 12–1068, bleeds off the bottom
└┴───────────────────────┴┘ 1920
```
**`HOOK` (frame 0):**
```
┌─────────────────────────┐ 0
│ ▛ HEADLINE SLAB  −1.5° ▜│ ← top y 150 (band 140–200), x 40–1040, 2 lines ≈ 230 px
│ ▙ …vs [MINE] 🔥  shadow▟│
│   ╭──────────────╮ 4°   │ ← result card (browser/phone mock), y ≈ 420–1100 (measured r01, r05, r06, r09)
│   │ bad result,  │      │
│   │ red circles  ╰──╮   │ ← the creator's cut-out overlaps the card corner by 60–140 px (G-5)
│   ╰──────────── (head)  │   head top ≥ 40 px below the slab bottom
│  CHUNKY keyword (CS-2)  │ ← block y 1140–1440, on the open side of the face
│      (the creator)      │
└─────────────────────────┘ 1920
```
**`D` / `R` Data Stage with the bubble:**
```
┌─────────────────────────┐
│ · · · dot grid (60 px)  │
│  graphic zone x 40–1040 │ ← y 160–1080: crowd, gauge, machine (one idea)
│   700 px glow behind    │
│        the hero         │
│  white subtitle (CS-1)  │ ← cy 1300
│ ◯ bubble Ø 300          │ ← centre (210, 1560), 8 px paper ring + 12 px ink shadow
└─────────────────────────┘
```

### 3.4 Stage moves (G-…)
How the creator moves between layouts. These moves are the style: plan every one on purpose.

| ID | Move | Recipe (30 fps) | Use |
|---|---|---|---|
| **G-1** | **Panel drop** | T-04 (`via: panel-drop`, 5 f): a hard cut to the full-frame take, then it drops into the panel in 4–5 f with heavy vertical motion blur (measured r01); the canvas or stage is revealed; the marker rises 3–4 f after the panel lands, then the card | Into every item |
| **G-2** | **Pop-back** | T-17 (`{"layout": "full", "via": "pop-back", "dur": 5, "overshoot": 0.1}`): the item graphics clear on f0 (hard), the panel grows to full frame in 2 f, overshoots to ≈ 1.10 and settles to 1.00 by f5 (measured r01, three times). The next jump cut may punch (Z-1) | Back to the creator for a roast, an opinion, a punchline |
| **G-3** | **Slide-aside** | T-23 (`via: slide-aside`, 8 f): the panel narrows and slides left to x 0–450 (rounded right edge); the B-roll takes x 470–1060 | Pointing at a duel; explaining beside a tall phone mock |
| **G-4** | **Reaction bubble** | T-24 (`via: bubble-shrink`, 8 f): the footage shrinks into a Ø 300 circle (8 px `paper` ring + 12 px ink shadow) at bottom-left (centre x 210, y 1560), elastic overshoot 1.15; the bubble bounces 1.0 → 1.12 → 1.0 on punch words. **Large variant** (r09): Ø 490 centred (280, 1480) when the graphic ends above y 1200 (`layout.bubble_large`) | Full-screen Data Stage, versus or UI moments |
| **G-5** | **Depth sandwich** | The cut-out is drawn **in front of** the graphic: the card sits behind the creator (`behind: true`, layer 4) and they overlap its bottom edge or corner by 60–140 px. Parallax: the card drifts ±12 px against them. Cards, objects or text can live back there | Hook, premium reveal, hero numbers |
| **G-6** | **Lean-in** | The creator's cut-out slides in from the right edge (10 f, ease-out) pointing at the card, hips cropped by the frame | "Ye dekho", pointing at a flaw |
| **G-7** | **World swap** | The creator stays full frame, but the cut-out replaces the room behind them with a world (Data Stage dots, a hard cut on the trigger word). The backdrop then **tints with the state**: neutral night/cyan → red on the crash word → green on the fix (measured r06). Cards sit beside the head as in G-5. Build: a full-frame `behind: true` scene (z ≤ 4) painting the world under the cut-out | Data hooks (HA-07) and warn → fix beats where the creator keeps talking to camera |

### 3.5 Data Stage (`D`)
- **Background:** W-3, with a 700 px radial glow behind the hero element (`accent` `#FF6A00` or `data` `#00D8FF` at 14 %)
  drifting ±20 px.
- **Layout:** the graphic zone is x 40–1040, y 160–1080. The creator sits in a `P-INSET` panel (dark-rimmed) or the G-4
  bubble. Captions are white CS-1 at panel top − 60 (bubble: cy 1300).
- **Neon only where it matters:** glows on the hero element and the state change (OK → crash). Everything else stays flat.
- **Scale honesty:** quantities are countable things: 5 avatars, 5,000 dots (literally 5,000, seeded positions), N shield
  segments.

### 3.6 Safe zones and bands
- Meaning text sits within x 64–1016, y 110–1500. The bottom ≈ 380 px and the right ≈ 110 px are covered by Instagram's
  buttons; only the speaker panel or the bubble lives there.
- **Slab band:** top edge y 140–200 (default 150).
- **Caption band:** on full frame, centre y 1150–1450 (CS-1 at 1300); in the splits the subtitle rides the panel at
  panel top − 60 (1075 on `L-panel`, 948 on `L-inset`).
- **Chunky block (CS-2):** y 1140–1440 (measured: helper centre ≈ 1280, keyword cap band 1200–1430).
- **Card zone:** x 24–1056, y 300–900, radius 40, with the title band y 190–300 above it.
- **Bubble:** its bottom edge stays above y 1740.

### 3.7 The person
People come for the creator, so they're on screen or one beat away: in the panel, the bubble, the depth sandwich or full
frame. A full-screen graphic without them is a short, deliberate moment (about 2.5 s at most in the reference reels), and
they come back by a G-2 pop-back or a hard cut on a roast or opinion word. Keep their face clear unless the moment wants
otherwise (§2). Crops per mode are in §12.2.

---

## §4 Colour system

### 4.1 Bright palette (each hue has one job)
| Role (token) | Name | Hex | Job | Text on it |
|---|---|---|---|---|
| `primary` | **Hype Yellow** | `#FCF700` | The Headline Slab, keyword chips, the CTA keyword, list-cue highlights. *The* brand colour | `ink` (17:1) |
| `accent` | **Blaze Orange** | `#FF6A00` | Premium energy: reveal light sweeps, the T-01 streak, `awe` glows, marker underlines | `ink` (7.5:1) |
| `bad` | **Alarm Red** | `#E9181E` | Their bad result, danger, crash, blocked, "bilkul mat", flaw circles | `paper` (4.55:1; large text) |
| `good` | **Volt Green** | `#22F06A` | The premium result, fixed, secure, money, ✓ | `ink` (13:1) |
| `data` | **Electric Cyan** | `#00D8FF` | Tech, data, systems, users, requests; the Data Stage accent | `ink` (12:1) |
| `concept` | **Ultra Violet** | `#8A5CFF` | Concept and tool names (CS-3 glow), step badges | `paper` (the engine nudges it to `#8455F8` for 4.5:1) |
| `comedy` | **Comedy Pink** | `#FF2E8B` | **Comedy layer only:** stickers, roast labels, freeze-frame marks | `paper` bold (large only) / `ink` |
| `ink` | Ink | `#0B0B0B` | Text, strokes, hard shadows | — |
| `paper` | Paper | `#FFFFFF` | White text, cards, chips, sticker outlines | — |
| `canvas` / `grid` | Canvas / Grid | `#FCFCFC` / `#C5C5C5` | The canvas world | — |
| `night` | Night | `#07070C` | The Data Stage | — |

Gradients (CS-3 glow keywords and badges only):
- Violet (`concept`) `#B48CFF → #8A5CFF → #5B2FD6`
- Volt (`good`) `#9BFFC2 → #22F06A → #0FB24A`
- Cyan (`data`) `#9CF0FF → #00D8FF → #0089C7`
- Blaze (`accent`) `#FFC27A → #FF6A00 → #D93D00`

The light-streak ramp (T-01, T-20) stays as measured: `#F94F00` → `#FCEF2D`.

### 4.2 Meanings (every world)
- **Yellow** = read this / the hook / do this.
- **Red** = their bad result, danger, crash, blocked.
- **Green** = the premium result, fixed, secure, money.
- **Orange** = premium energy and light.
- **Cyan** = tech, data, users.
- **Violet** = the concept or tool name.
- **Pink** = it's a joke.
- A tool's own brand colours appear only on its name and logo.

**The before/after axis is always red → green.** Bad gets red marks; premium gets a green chip and an orange light sweep.

### 4.3 Rules
- At most **yellow + 2** bright hues in one frame.
- One hue per caption block. Subtitles are never coloured.
- On the canvas, coloured text needs an `ink` stroke ≥ 4 px, or sits on a chip.
- On the Data Stage, red and pink text gets a 3 px white outline or sits on a chip.
- Footage is never regraded (low-key, warm, the room's own magenta practicals); only exposure and white balance are matched
  between setups. Graphics never borrow the room's magenta.
- If the creator's copy swaps the yellow for their brand colour, it must still carry ink at ≥ 7:1 and stay the loudest
  thing on screen (setup nudges it).

---

## §5 Type and captions

### 5.1 Font map
| Slot | Role | Family (weight) |
|---|---|---|
| `display` | **Headline Slab**, glow keywords, labels, data words | **Inter Tight** (900 slab; 800–900 labels) |
| `chunky` | Chunky captions (CS-2), stickers | **Lilita One** (400); Gagalin when installed |
| `body` | Subtitles (CS-1) | **Plus Jakarta Sans** (800, lowercase) |
| `numeric` | Hero numbers, badges | **Anton** (400) |
| `serif` | Helper lines, tool titles, premium site type | **Instrument Serif** (400 italic) |
| `marker` | **Comedy marker** (roast notes) | **Permanent Marker** (400) |
| `kinetic` | Imperative 3D cards (KT-RED) | **Montserrat** (900 italic) |
| `ui` | Chips, prompt text | **Jost** (500 / 700) |
| `pixel` | Pixel titles | **Silkscreen** (700) |
| `mono` | Code-shaped texture only | **JetBrains Mono** |

Pre-paint ₹ ✓ ✕ → and every emoji used. Brand wordmarks and logos are image assets, never fonts.

### 5.2 `CAP-BANNER`: the Headline Slab
The strongest element on screen (D4). Scene `kind: "banner"`, z 10, `chips: [{text, role}]`, `lines`, text class `TC-display`.

| Property | Recipe |
|---|---|
| Slab | `primary` fill, **6 px `ink` stroke**, **hard shadow +12/+14 px `ink`** (no blur), radius 26, rotated **−1.5°**. x 40–1040, top y **150**, height auto (2 lines ≈ 230 px) |
| Text | `ink`, Inter Tight 900, **66–78 px**, line height 1.02, tracking −2 %, centred, **always 2 lines**: the setup on line 1, the chip and emoji on line 2 (every final reel). ≤ 9 words; a third line only when a number needs it |
| Keyword chip | 1–2 words in CAPS inside the slab, radius 14, padding 2/16. `ink` with yellow text (default); `bad` with white text (bad, danger); `good` with ink text (premium, fixed); `data` with ink text (data) |
| Emoji | ≤ 2, at line ends (🤢🔥💀🎁🔐💥🚀✅). Never mid-line |
| Underline | An `accent` marker swipe (8 px, slightly wavy) wipes under the chip word L → R over 6 f, **when that word is spoken** |
| Frame 0 | **Fully readable and already at rest** (measured r01, r06, r07, r10: the slab doesn't move in f0–f20). The f0 motion comes from the T-02 strobe, the card or the caption. A settle (1.04 → 1.00 by f4) is fine when nothing else moves on f0 |
| Life | A chip pulse (1.0 → 1.12 → 1.0, 6 f) on the spoken keyword. The **slab flip** (T-21) at the transformation beat: the chip flips to its opposite ("SLOP" → "PREMIUM", red → green). One flip |
| Exit | **Rockets up** off-frame in 4 f with vertical blur, 1–2 f before the cut into item 1 (preset `rocket`), or blurs out inside T-04. Never a hard pop mid-sentence |
| Lifetime | The hook: it stays up through the count and loop until item 1 (≥ 0.25 s per word, at least 2.5 s, at most 14 s; measured 5.9–13.9 s) |
| Variants | **B-VERSUS** "Your X 🤢 vs MINE 🔥" (two chips, red and green). **B-NUMBER** with a giant numeral chip ("5 ✅ → 5,000 💥"). **B-WARN**: the slab stays yellow, the chip is red, the emoji 🎁 / 🔓 |

### 5.3 CS-1 `CAP-SUB`: subtitles (every word of the talking sections)
This style uses the engine's **legacy** subtitle profile (`tokens.captions.legacy`, `profiles` empty on purpose), so the
captions render exactly as the creator's do.
| | Recipe |
|---|---|
| Chunking | 2–3 words per card, 1 line; never split a name, number or unit |
| Timing | lead 2 f; hold ≥ 0.25 s per word; hard swap (or a 2 f blur dissolve); hidden in pauses |
| Skin | Plus Jakarta Sans 800, 54–60 px (57 rendered), **lowercase**; white with a soft shadow on footage and the Data Stage; `#111` on the canvas; no container |
| Position | cy 1300 in `F`; panel top − 60 in `S`/`D` (1075 on `L-panel`, 948 on `L-inset`); cy 1300 on the bubble, slide-aside and dim layouts. The colour flips with the world (black on `canvas`, white elsewhere) |
| Emphasis | None. Subtitles are never coloured; emphasis lives in CS-2 and CS-3 |
| Hide | During the hook (timeline `captions: {"subtitles": "auto", "hide": [[0, <hook end>]]}`) and under z8 scenes (CS-2, CS-3, KT, big labels). **Not** during stage moves: they stay on through T-04 and T-17 and ride the moving panel (measured; tokens `captions.hide_on_morph: false`) |
| Language | Latin script; Hinglish romanised from the script text; English words and brand names exact; profanity masked inside the word (S**T) |

### 5.4 CS-2 `CAP-CHUNKY`: the hook, the early loop, the end CTA
A z8 text scene, `TC-display`. This is the voice of the hook.
- Chunky rounded unicase (Lilita One; Gagalin when installed).
- **Keyword line 84–112 px**, auto-fitted to ≤ 940 px wide, in `primary`, or a role hue by tone (`bad` red for the roast
  word, `concept` violet, a tool's brand colour for its name), with a 6 px `ink` stroke and a hard shadow +6/+8.
- **Helper line 60–80 px** in white, same face.
- **On the open side of the face:** centred when the face is centred; left-aligned from x 48 when the face sits right;
  right-aligned to x 970 when it sits left (970 keeps Instagram's button column clear). Block y 1140–1440.
- **The swap (measured r01, r06, r10):** the helper line swaps hard (0 f); the keyword **pops** from ≈ 0.5 → 1.0 in 2 f
  (preset `pop`) and grows by word-append ("PURPLE" → "PURPLE GRADIENT") while the helper changes under it. Hard 1-frame
  pops, a 1–2 f clear between blocks.
- The roast word gets the full **squash-pop** instead: scale y 0.7 → 1.15 → 1, x 1.2 → 0.95 → 1 over 3 f.

### 5.5 CS-3 `CAP-GLOW`: keyword titles
A z8 text scene, `TC-display`, for naming a concept so it sticks.
- Inter Tight 900, cap height 150–220 px, a §4.1 gradient by role plus a same-hue glow of 20–40 px.
- Typed at 1 letter per frame, or a 1-frame smear landing sharp.
- Helper: white Instrument Serif italic, 70–80 px, under the right half, fading in over 4 f.
- Holds ≥ 10 f; subtitles hide while it's up. It's a moment, not wallpaper: save it for the words that deserve a title.

### 5.6 Other text
| System | Recipe | Hold |
|---|---|---|
| **Edge labels** (`TC-label`) | On the card's bottom edge, white Inter Tight 800, 90–120 px, swapped per noun | ≥ 10 f |
| **Serif tool titles** (`TC-display`) | Above cards (title band y 190–300), Instrument Serif italic 90 px, letter-by-letter blur reveal | ≥ 10 f |
| **Stacked feature words** (`TC-label`) | Black on the canvas, left-aligned, one per spoken item | to the item's end |
| **Kinetic type `KT`** (`TC-display`) | **KT-RED** imperatives (Montserrat 900 italic, `#FF2A2A`, extrude `#B3001B`, −7°); **KT-TYPE** ghost-letter typewriter; **KT-PIXEL** (Silkscreen); **KT-ACRONYM** (letters expand into words); **KT-ARC** (text on an arc) | ≥ 10 f |
| **Comedy marker `CAP-MARKER`** (`mock` only, `TC-label`) | Permanent Marker 56–72 px, `bad` red on light backgrounds or `comedy` pink with a white outline on dark ones, rotated −4…+6°, written on with a 10 f L → R wipe; paired with the ink marks of §8.6 ("purple gradient 🤢", "same 3 cards", "ye tum ho 😭", "5 nithalle dost") | ≥ 0.25 s per word |
| **Hero numbers `HERO-NUM`** (`TC-display`) | Anton 260–520 px, white or a role colour, a 6 px ink stroke on the canvas, a glow on the Data Stage. Always **counts** (a slot roll or an ease-out count over 18–30 f) or **assembles** from particles (P-59). Lands with a Z-5 shake and a reveal cue. The comma format follows the script ("5,000") | ≥ 10 f after landing |
| **Stickers `STICKER`** (`mock` only, `TC-label`) | An emoji or a 1–3 word pink/white label: 10 px white outline, hard shadow +6/+8 ink, rotated ±8°. Pops 0 → 1.25 → 0.95 → 1.0 over 6 f, wobbles ±3° for 12 f. One on screen at a time, beside the face unless the roast is aimed right at it. Set: 💀 🤡 🤦 😭 🗑️ 🎁 "bruh" "AI SLOP" "BEKAAR" (write the topic's own roast word) | 12–30 f |
| **Chips** (`TC-label`) | Jost 700, ≥ 40 px, radius 14, `primary` / `data` / `good` / `bad` fill with its text-on colour | ≥ 0.25 s per word |

### 5.7 Language and numbers
- The slab, chips and labels are English (Instagram-native); the spoken hook stays in the creator's language. ALL-CAPS
  chips and the slab are Latin script.
- Numbers follow the script ("5,000", "₹10,000"), never compacted: the number is the picture. The copy's number format
  decides grouping and currency (international and `$` by default; Indian grouping and `₹` for Hinglish and Hindi
  copies). `₹` is pre-painted, never "Rs" or "INR".

---

## §6 Hook system

**The hook title** promises the viewer something: an outcome they want, a curiosity gap, or who it's for ("How to go viral
as a doctor creating content", never the label "Reels for Doctors"). It needn't repeat the spoken words; it must be true to
what the reel delivers. In this style the title *is* the slab: its shape (two lines, ≤ 9 words, one chip, ≤ 2 emoji) is
fixed; its voice is yours to make irresistible.

### 6.1 The stopper test (frame 0 and the first 3 s)
1. **Thumbnail:** frame 0 at 25 % scale still says what this is about: the slab reads (its text ≥ 16 px at that scale),
   and the result and the creator are both visible.
2. **Mute:** with the sound off, the first 3 s tell the story (bad → premium, or failure → fix).
3. **Motion at f0:** something is already moving on frame 0 (the strobe, the card tilting in, the chunky word).
4. **One read:** the slab reads in ≤ 1.5 s.
5. **Payoff:** a result is on screen by 2.0 s; the premium or fixed state by 4.6 s.
6. **Feed contrast:** in a strip of six random reel thumbnails, ours has the highest-contrast element (the yellow slab
   with its ink shadow) and a clear "two states" picture.

The first three seconds feel *dense*: the card lands, the circles draw, the chunky word swaps, the stamp slams. Dense in
time, never in space: each thing lands while the last one settles.

### 6.2 HA-01 Result-First Roast (default)
Use it for every "build / fix / do it better" reel. The spoken pattern: "*Ye tumhara `<thing>` hai* [bad]… *aur ye maine
`<method>` se banaya* [premium]." Times are the shape; take the real ones from the words.

| t | Beat | Tone | Visual | Caption | Zoom / move | Sound (§11) |
|---|---|---|---|---|---|---|
| **f0** | Stopper frame | hype | **Slab** already at rest (B-VERSUS) + the **bad result** (browser or phone mock, tilted 4°) mid-frame + the **creator cut out** over its bottom corner (G-5), already pointing. The T-02 strobe and the card tilting in carry the motion | — | card tilt-in | sub-hit on f0 (`abstract-hit-sub-bass-07`) |
| 0.1–1.4 | "Ye tumhara `<thing>` hai…" | mock | The card pushes in (1.00 → 1.08). **Flaw markup (P-62):** 2–3 red marker circles draw on the real flaws, with notes ("purple gradient", "same 3 cards", "centred text") | CS-2 "ye tumhara / **`<THING>`**" | Z-7 rotation snap | a marker swipe per circle, each a different file |
| 1.4–2.1 | The punchline ("…ekdam garbage / AI slop") | mock | **Stamp verdict (P-63)** "AI SLOP" slams onto the card (−12°, scale 1.6 → 1) + Z-5 shake + 💀 sticker. A Z-2 crash zoom on the smirk if the line earns it | CS-2 "**GARBAGE**" in red | Z-5, or Z-2 | **a meme hit in the gap after the word** |
| 2.1–2.6 | The pivot ("…aur ye") | awe | **The bad card exits (T-19 Shatter):** it cracks and falls in shards with gravity and spin | — | Z-3 snap pull-out | a riser into the reveal (`zoom-in-riser-zoom-in-riser`) |
| 2.6–4.6 | "…maine `<method>` se banaya" | awe | **Premium reveal (T-20 light sweep):** the orange streak crosses L → R and the premium result is there behind it, in 3D tilt (rotateY 18° → 0 over 14 f) with live motion inside. **Slab flip (T-21)** "SLOP" → "PREMIUM" (red → green). The creator stays in front (G-5) | CS-2 "`<method>` / **SE**" | Z-4 push drift | impact + shine on the flip |
| 4.6–7.5 | The count ("ye 3 `<items>`…") | hype | Feature chips **orbit** the premium card (P-66). **Count tiles** pop one per item, ≈ 0.4 s apart, on the count word: violet 3D "?" cubes (r01), film-strip numbered tiles (r07), or a numbered list whose rows fade in 3 f apart (r06) | CS-2 "**3 `<ITEMS>`**" | Z-1 cut-punch on the count | a pop |
| 7.5–13 | The loop ("reel end tak dekhna… DM mein bhej dunga") | hype | The tiles and the premium card hold under the slab; jump cuts alternate plain and Z-1 | CS-2 "END TAK / DEKH LENA / BHEJ DUNGA" | Z-1 / plain | — |
| exit | — | — | The slab rockets up (4 f); a hard cut to the item take; T-04 panel drop into item 1 on "pehla" | — | — | a whoosh not used yet |

**Never skip the premium state.** Even when the script's hook only roasts, the premium or fixed state appears by 4.6 s:
that's the open loop. The hook and its loop are over before the reel's first quarter is (the reference hooks ran
5.9–13.9 s); a reel with no spoken loop ends its hook at about 6 s (r07).

**Measured hook motion (r01, 30 fps):** f1–f5 a white cut-out silhouette on alternate frames (T-02, three flashes) over a
still slab and card; the CS-2 keyword pops at 0.73 s; the marker circles and notes draw 2.3–3.0 s; the stamp lands
1.6 → 1.0 in 2 f at 3.23 s on a jump cut with a 4 f shake; the bad card shatters at 4.87 s (2 f white haze, shards over
9 f) under a light streak that reveals the premium site by 5.27 s; the footage slowly pushes in (Z-4) between cuts.

**Visual stoppers (VS): combine two or three in a hook**
| ID | Device | Recipe |
|---|---|---|
| VS-1 | **Bad card with flaw markup** | P-62 on a browser or phone mock: red circles + marker notes |
| VS-2 | **Depth sandwich** | The creator's cut-out in front of the result card (G-5), with parallax |
| VS-3 | **Stamp verdict** | P-63 stamp + shake + meme hit |
| VS-4 | **Shatter → light sweep** | T-19 + T-20, bad to premium in ≈ 12 f (measured r01). Alternate exit (r07): the bad card **shrinks to a corner thumbnail** (≈ 25 % size, bottom-left of the card zone, 6–8 f) and stays as the reference while the premium card takes its place |
| VS-5 | **Versus from f0** | Mode V: bad on the left (red frame), premium on the right (green frame); a diagonal wipe divider animates on f0–8 |
| VS-6 | **Number made of people** | P-59: the hero number assembles from 5,000 dots that were people |
| VS-7 | **Metaphor object** | A gift box, vault or bouncer pops in with squash, already doing its thing |
| VS-8 | **Silhouette strobe / zoom-blur slam** | T-02 / T-03, always together with a result |

### 6.3 Alternate hooks
Every alternate still shows a result, or the proof of the claim, in the first two seconds. The creator's hook formulas map
onto them:

| HF | Formula | Hook |
|---|---|---|
| HF-1 | Clone skit / argument | **HA-14** Cold authority |
| HF-2 | Money claim + proof | **HA-02** Headline + proof |
| HF-3 | POV / "You found…" | HA-01 (POV-outcome slab) |
| HF-4 | Reverse psychology ("bilkul mat banana") | HA-01 (the bad result first) |
| HF-5 | Pain point + contrarian agreement | HA-01 |
| **HF-6** | **Before / after: the Result-First Roast** | **HA-01 (default)** |
| HF-7 | FOMO / newness | HA-02 |
| HF-8 | Time-ask | HA-02 |
| HF-9 | "Skip this if…" | HA-01 (skip-this slab) |
| HF-10 | Mock quote of the viewer ("Kya bro, Claude ne banaya hai toh secure hoga bro?") | HA-01 (mock-quote variant, r10) |
| — | Number / scale open ("5 users ✅ 5,000 users 💥") | **HA-07** Live number |

**HA-02 Headline + proof** (a money claim, FOMO, a time-ask):
| t | Visual | Caption | Camera | Sound |
|---|---|---|---|---|
| f0 | Slab (B-NUMBER or count + promise) + the creator full frame; a proof card (a screenshot of their own result, or phone-filmed proof P-17) tilting in | — | — | sub-hit |
| 0.2–1.5 | The proof card pushes in; the key figure gets a marker circle (P-62 in `good` green when it's their own win) | CS-2 claim words | Z-1 on the number | pop |
| 1.5–2.5 | The hero number counts (HERO-NUM), or the proof zooms through to its detail | CS-2 keyword | Z-5 on the landing | impact |
| 2.5–6 | Count tiles + loop; the slab rockets out into item 1 | CS-2 "end tak dekhna" | Z-1 | pop, whoosh |
Example: "Claude Code se ₹40,000 ka client project 2 din mein" (proof: the creator's invoice, private data blurred).

**HA-07 Live number** (scale, money growing, "N vs N × 1,000"):
| t | Visual | Caption | Camera | Sound |
|---|---|---|---|---|
| f0 | B-NUMBER slab + the Data Stage with a crowd counter already pouring (P-40) on a phone mock; the creator in the panel or cut out (G-7 world swap) | — | — | sub-hit |
| 0.2–2.0 | The small case (5 avatars) → zoom-out (P-41) to the big case; the gauge swings to red (P-42) | CS-2 "5,000 / USERS" | — | data cue |
| 2.0–4.5 | The crash device (P-43), or the payoff number lands; the slab chip pulses red | CS-2 verdict word | Z-5 | glitch + a meme hit if `mock` |
| 4.5–6 | G-2 pop-back + Z-1; N tiles rise | CS-2 "4 CHEEZEIN" | Z-1 | pop |
Example: r06 (§14.2).

**HA-14 Cold authority** (a clone skit, an argument):
| t | Visual | Caption | Camera | Sound |
|---|---|---|---|---|
| f0 | A mid-sentence skit line on setup D (clone A), the CS-2 caption up at f0, the slab already readable | CS-2 quote | Z-7 | — |
| 0.3–1.5 | Cut to clone B's reaction: a freeze-frame roast (P-64) on the wrong belief | CS-2 roast | Z-2 | meme |
| 1.5–2.5 | The result card (wrong vs right) slides in beside them (G-3) | CS-2 keyword | — | whoosh |
Example: "Bhai Lovable se app bana li, ab launch?" / "Ruk."

### 6.4 Result pairs by topic
**This is the most important table for literal visuals.** Pick one per reel; when the topic is new, invent the pair in the
same spirit: a bad state the viewer recognises as theirs, and a premium state they want.

| Topic | Bad state (red) | Premium / fixed state (green) | Pattern |
|---|---|---|---|
| Website design (r01, r05) | Purple-gradient AI-slop site: centred text, 3 identical cards | A dark premium motion site, serif display type, live animation | P-61 |
| Website "alive" (r07) | A site opening on a static photo, 😴 | The same site with a looping video background | P-60 (mode V) |
| Launch checklist (r03) | A broken launch: missing items flagged red | Every item ticked green, "LIVE 🚀" | P-58 checklist variant |
| App UX (r02) | Crowded icons, a frozen Save spinner | A clean bar, an instant update | P-61 on a phone mock |
| Scale (r06) | 5,000 users → the app cracks and goes black | 5,000 users → the app smooth, the gauge green | P-40 + P-43 |
| Security (r10) | The app as a **gift box** opened by a swarm of red cursors | A vault: shield 7/7, cursors bounce off | P-49 → P-58 |
| AI team / dev team (r04, r08) | One stressed person juggling 6 tasks | 6 agent cards working in parallel, all ✓ | P-44 versus lanes |
| Prompts (r09) | A vague one-line prompt → generic output | A structured prompt → a shipped app | P-61 with prompt cards |

The machinery travels to any niche: savings shrinking against an inflation bar → the same money split by a plan and
overtaking it (P-44 + P-45); a salary draining out of a leaking bucket by day 12 → jars still full on day 30 (P-47 variant);
a credit-card balance climbing every month → a counter hitting 0 under a "DEBT-FREE ✓" stamp (P-40 + P-63). §14.4 is a
full plan in that niche.

### 6.5 Slab writing (the first thing people read)
**Formula:** `[viewer-pointed setup] + [KEYWORD CHIP] + [≤ 2 emoji]`, ≤ 9 words, saying the same thing as the result pair
on screen.

| Template | Example |
|---|---|
| **Versus** (default with a result pair) | "Your Claude website 🤢 vs **MINE** 🔥" |
| **Number** | "**5** users ✅ **5,000** users 💥" |
| **Warning** | "Your Claude app is a **GIFT** for hackers 🎁" |
| **POV outcome** | "POV: your website finally looks **PREMIUM**" |
| **Count + promise** | "**3** Claude skills that kill AI slop" |
| **Skip-this** | "Skip this if you like **BORING** websites 😴" |

- Sentence case + one CAPS chip. English is the slab's language; the spoken hook stays in the creator's.
- Write 8–10, pick by the stopper test, and keep the next two as alternates (they go to the storyboard and to Trial Reels).
- Never vague hype ("Game changer!!"), never more than 2 emoji, never a count that doesn't match, never a claim the reel
  doesn't prove.

### 6.6 Hook sound
The hook carries cues but no music bed. Every hook cue is a different file. One meme hit in the hook, on the punchline's
gap. The `mock` → `awe` switch is marked by sound: the meme hit, then a riser, then a cinematic impact. The bed enters on
the T-04 into item 1.

### 6.7 CTA
Devices: comment keyword (default), DM, link in bio; an early loop mid-reel and the end CTA.
1. **The early loop** (CS-2, in the hook's tail): "reel end tak dekhna… saare `<deliverable>` DM mein".
2. **The end CTA:** the creator pops back (G-2) for "comment kar do **KEYWORD**" (the reel's keyword).
   - **P-68 key-cap:** the keyword on a 3D yellow keyboard key (≈ 680 × 200 px, centre y ≈ 1300, ink stroke, an olive-yellow
     extrude below; the white CS-2 helper "comment kar do" sits just above it). It pops in with a bounce, holds ≈ 1.7 s,
     presses down (8 f, it dims) with a click, then the deliverable card flies into a DM bubble (a 14 f arc). The
     deliverable is a **dark doc card** (near-black fill, white title, the key words in `bad` red, a red "PDF" tag, tilted
     6–10°) in the top band y 250–750, often as a fanned stack; the DM target is a yellow circle with ✈️ or a cyan
     "DM ➜" chip (measured r01, r09, r10).
   - The keyword is on screen ≥ 1.5 s (`kind: "cta-keyword"`, its text contains the keyword).
   - With DM: the key-cap reads "DM **KEYWORD**". With link in bio: the key-cap becomes a "link in bio ↗" chip held
     ≥ 1.5 s.
3. **The community card** (P-29, measured r01): a dark rounded card in the top band (y 120–330) with the creator's community
   name and a one-line sub; member avatar dots pop in one by one (≈ 9 f apart), one or two chat bubbles slide in ("new
   drop", "you got first access"), and a tilted yellow sticker label ("FIRST ACCESS ⚡") slides in at its corner. Then a
   yellow "`<link>` → bio 👇" chip (ink text, hard ink shadow, pops 7 f) replaces it for the last second. Skip the card when
   the creator has no community; the whole CTA runs about 5–7 s.
4. **The sign-off** (the creator's own, e.g. "peace out"), then a hard end ≤ 6 f after the last word (T-16). The CTA is
   tone `cta`: no meme sounds, and silence in the second before its first word.
5. **A sponsor** (only when the reel is paid): a `paper` card with the sponsor's logo (theirs, else fetched from their
   site) and one line in the card zone, clear of the face and the data; the "Paid partnership" disclosure held ≥ 2 s and said in speech. No roast and
   no meme sound on the sponsor's product.

---

## §7 Structure and rhythm

### 7.1 Structure: a list
promise (hook + count) → loop → items (the same ritual each time) → the escalated last item / payoff → CTA. Items count up.

### 7.2 Markers (SM-…): one style per reel, at every item
| ID | Marker | Recipe |
|---|---|---|
| SM-1 | Numbered chapter badge (default) | A violet gradient 3D cube badge (≈ 300 px), Anton numeral; it rises from behind the panel 3–4 f after T-04 lands with a small overshoot, then bobs ±6 px while it holds to the item's end (measured r01) |
| SM-2 | "N Step" arc | Arc + dot + italic numeral, 10 f |
| SM-3 | White number circle | Ø 150, slides up 12 f |
| SM-5 | Countdown tiles | N tiles rise; the active tile lights **yellow** at each item (a spine) |
| SM-6 | Serif tool title | The title is the marker |
| SM-7 | KT step card | KT-RED / "LAST STEP" |
| **SM-8** | **Shield segments** (risk and security lists) | An N-segment shield in the top-left badge position; each item lights its segment green with a check (P-58) |
| **SM-9** | **Progress rail** | Top band y 120–190, two forms: (a) a thin rail with N numbered circle notches and an end-cap of the deliverable ("PDF", "TEAM"; r06, r08); (b) a row of N rounded chips (Anton numeral + a small icon per item, r09): done = `good` green + ✓, current = `primary` yellow, upcoming = `concept` violet outline on dark, a lock on the last. The active notch or chip pops; the rail stays up on every world, over footage too. **Chapter interstitial** at each item (r09, ≈ 0.8 s): a hard cut to the creator dimmed (`L-dim`); the rail drops to frame centre and scales ×2 (2 f); the item's chip lights yellow with its label under it (serif helper); hold ≈ 10 f; then a **zoom-through the yellow chip** (×6 in 3 f, the rail scene's own scale) until yellow fills the frame, a 2 f white flash (`VEOS.fx.flash({up: 1, hold: 0, decay: 2, peak: 0.85})`), and the item's world lands (canvas + panel) |

Pick SM-8 for risk and check lists, SM-9 for "N things" with a fixed count of four or more, SM-1 otherwise.

### 7.3 The item ritual (the same for every item)
1. G-1 panel drop (or T-18 zoom-through into the Data Stage, or the SM-9 chapter interstitial) 0–8 f before the ordinal
   word, on the **list cue** (the one sound allowed to repeat). One entry type per reel.
2. The marker, 0.6–1.2 s.
3. The title + card, or the Data Theatre machine, on the tool or risk name (±1 f).
4. Two to four evolving visuals, one per noun.
5. **Pop-back (G-2)** to the creator for the opinion, aside or roast, with a Z-1 or Z-2.
6. A reaction bubble (G-4) when the visual has to stay full screen while they react.

The ritual is the one place repetition is the point: the viewer learns it and feels the count go up.

### 7.4 Open loops
- The count loop: the markers count up to N.
- "The last one is the most dangerous / the best" (r10: "last wala sabse khatarnak").
- The deliverable loop: the thing in the DM.
- Every loop is paid off on screen.

### 7.5 Rhythm: infotainment
- **Information and entertainment take turns.** The entertainment comes back often enough that the viewer never feels
  lectured: a roast, a skit line, the bubble, a freeze, a sticker. Every joke also carries information; no filler jokes.
  Never two comedy beats back to back: an `explain` or `win` beat sits between them.
- **The energy curve:** the hook at maximum → item 1 high → the middle items steady, alternating worlds → the last item
  escalates (the Data Stage or `S-DARK`, a bigger hero move, the bed dropping out before it) → the CTA clean and confident.
- **It follows the speech.** Fast lists get fast changes; the pause before a reveal gets a hold; the opinion gets the
  face. Long talking stretches stay alive through the subtitle swaps, the cut-punches and the zooms, not by piling
  graphics on. Vary the moves so the eye never predicts the next one; the item ritual is the deliberate exception.

---

## §8 Visual system: B-roll and patterns

Graphics carry the argument in this style. **Numbers become pictures** (D5): every quantity, comparison or risk the creator
says is something the viewer can count, compare or watch break.

### 8.1 Families (B-…)
| ID | Family | Source | Notes |
|---|---|---|---|
| B-1 | Screen-recording card | the creator's captures (else the real page captured from the web, else a B-15 mock) | Real captures in rounded cards (radius 40) |
| B-2 | Screenshot / doc card | the creator's files (else the real one fetched from the web, else a recreated UI or quote card) | READMEs, docs, chat screens |
| B-3 | Prompt card | built | "Prompt:" header + text, typewriter |
| B-4 | Chip / command | built | `/command layout`, `Ctrl+C`, a key term |
| B-5 | Logo / wordmark | the creator's logo files, else the real logo fetched from the web (a logo plate, the name set in type, only when none can be found) | Real marks in their brand colours |
| B-6 | Silhouette illustration | built | Flat B&W vector people |
| B-7 | Kinetic-type card | built | KT-… |
| B-8 | Proof / data card | the creator's proof + built | Counters, phone-filmed proof |
| B-9 | Flow diagram | built | Dots, connectors, chips |
| B-10 | Icon pop | built | PDF, emoji |
| B-11 | UI mock | built | The IG comment / share flow |
| **B-12** | **Data Theatre** | built | Procedural people, requests, packets, coins, gauges, shields on the Data Stage: thousands of seeded elements, synced to words |
| **B-13** | **Metaphor machine** | built | A physical metaphor that *does the mechanism*: book index, bouncer gate, gift box, vault, data wall, shape sorter, leaking bucket |
| **B-14** | **Comedy layer** | built | Marker notes, stamps, stickers, freezes, crash zooms. `mock` beats only |
| **B-15** | **Device mock (built live)** | built | A browser window and a phone frame drawn in the renderer, so what's inside can crash, crack, scroll or transform |

B-12 and B-13 carry every number, comparison and risk. B-14 lives only on `mock` beats.

### 8.2 Staging choreography (every pattern)
Lead −2 f → land ≤ 5 f → read it (something keeps moving inside) → **evolve** (add, split, zoom through) or **swap**.
Evolve inside an item; swap between items.

### 8.3 Pattern specs (P-…)
**Core patterns**
| ID | Pattern | What's on screen | Motion (30 fps) | Use |
|---|---|---|---|---|
| P-01 | Site card | A real site/app capture in a rounded card (radius 40), card zone y 300–900 | Rises 10 f expo-out; slow scroll inside, 40 px/s | Naming a site, app or tool |
| P-02 | Montage | 3–5 captures swapping in one card frame | 6–8 f per capture, T-12 push swaps | "Itne saare…": lists of examples |
| P-03 | Before / after card | One card split by a diagonal wipe: before (red frame) / after (green frame) | Wipe 10 f L → R | Small fixes inside an item |
| P-05 | Tool title + card | A serif tool title (90 px) in the title band + the tool's card | Letter-by-letter blur reveal, 1 letter/f; the card rises 8–12 f | Every new tool or step |
| P-06 | Feature list | Stacked feature words (black on canvas), left-aligned beside the card | One word per spoken item, rise 6 f, 4 f stagger | "Ye X, Y aur Z karta hai" |
| P-07 | Edge labels | A white Inter Tight 800 label on the card's bottom edge | Swap per noun, 4 f blur swap | Naming parts of a card |
| P-08 | Prompt card | "Prompt:" header + Jost text | Typewriter 1 letter/f, blur 6 → 0 | Every prompt or command said |
| P-09 | Prompt → agent | The prompt card flies into a chat/agent window; the output card emerges | Fly 10 f arc; the output builds 12 f | "Bas ye prompt daalo, aur…" |
| P-10 | Command chips | Jost 700 chips (`/command`, `Ctrl+C`) | Pop 7 f, 3 f stagger | Commands and shortcuts |
| P-11 | Logo stack | 2–4 real logos (the creator's or fetched) in a row | Pop 6 f, 4 f stagger | Naming several tools or brands |
| P-12 | Silhouettes | Flat B&W people, 1–6 | Rise 8 f, staggered | People, roles, audiences |
| P-13 | KT card | KT-RED / KT-TYPE / KT-PIXEL / KT-ACRONYM / KT-ARC | Per §5.6 | Imperatives, "MAT KARNA" |
| P-14 | Counter card | A counter chip with the spoken number | Slot roll 24 f, lands on the word | A single small stated number |
| P-15 | Doc pop | A PDF/doc icon pops with its real title | Pop 7 f + 12 f float | Deliverables, docs |
| P-16 | Screenshot / doc card | A doc, README or chat screenshot in a card | Push-in 1.00 → 1.06 over the beat | Showing a doc or a message |
| P-17 | Phone-filmed proof | The creator's own result filmed on a phone, in a phone frame | Tilt-in 10 f, live | Proof claims (HA-02) |
| P-18 | Glow keyword title | A CS-3 glow title, violet gradient | Typed 1 letter/f, holds ≥ 10 f | Naming a concept |
| **P-23** | **Flow diagram** | Dots, connectors and chips (A → B → C) on the canvas | Connectors draw 8 f each; chips pop on their words | How something works (not data) |
| **P-29** | **Community card** | The dark community card + avatar dots + chat bubbles + a tilted yellow sticker label, then the "link → bio 👇" chip (§6.7) | The card pops 7 f; avatars pop ≈ 9 f apart; the sticker slides in 6 f; holds ≥ 1.5 s | The end CTA |
| **P-30** | **Comment-flow UI mock** | An IG comment box typing the keyword, then the DM arriving | Types 1 letter/f; the DM slides 10 f | An alternate comment CTA |
| **P-35** | **Live preview** | The premium result playing live inside a device mock | Loops; 3D tilt settle 14 f | Showing the premium build |

**Data Theatre (B-12, mode `D`)**
| ID | Pattern | What's on screen | Motion (30 fps) |
|---|---|---|---|
| **P-40** | **Crowd counter** | Countable people: 5 avatar circles on a sofa row → 5,000 dots. A counter chip shows the real number from speech | Avatars pop with a 4 f stagger. The counter slot-rolls 24 f. New dots pour in from the top as a stream (seeded, 120 dots per frame) |
| **P-41** | **Zoom-out reveal** ("powers of ten") | Tight on 5 people, then the camera pulls out ×12 to reveal they're 5 dots in a sea of 5,000 | 20 f ease-in-out pull-out; dots fade in by distance ring |
| **P-42** | **Load gauge** | A semicircle gauge (green → yellow → red zones), a needle, a label ("SERVER" / "BUDGET") | The needle follows the count (4 f lag), shivers ±2° in the red, sparks at max |
| **P-43** | **Crash device** | A phone/browser mock running the app: rows lag, a spinner appears, the screen glitches, **cracks draw** from an impact point, then black + 💀 | Lag 10 f → glitch 6 f → cracks 8 f → black. Z-5 shake. App states are drawn, never a fake error dump |
| **P-44** | **Versus lanes** | Two identical frames side by side (or stacked) on the same axes: the bad/small case left, the premium/large case right | Both animate in sync; the loser desaturates 40 % and gets a red frame, the winner a green frame and a glow |
| **P-45** | **Overflow bars** | Two bars on one axis; one overflows and breaks through the frame's top edge | Grow 18 f; the overflow pushes the frame (Z-5) |
| **P-46** | **Book index** (a database index) | Left: a scanner reads table rows one by one (slow, a timer ticking, rows flashing). Right: an index tab jumps straight to row #4217 (a laser line) | Left scans 1 row/f; right jumps in 6 f + ✓ |
| **P-47** | **Fan-out** (a cache; "make once, serve many") | One source card is built once, then copies fly to 12 avatars instantly; the source chimney stays idle | Build 12 f; copies fly with a 2 f stagger |
| **P-48** | **Load-test swarm** | Thousands of ghost users (translucent cyan) sent at a staging app; the break point gets a red marker circle ("yahan tootega") | The swarm builds over 30 f; the crack pulses at the weak component |
| **P-49** | **Gift-box exploit** | The app as a yellow gift box with an ink bow and a "your app" label; the lid pops and a swarm of **red cursors** climbs in | Lid pop 6 f (squash); cursors stream 40 f with seeded jitter |
| **P-50** | **Bouncer gate** (rate limits, filters) | Cyan pellets stream at a gate; a steady few pass, the flood bounces back red; a "spam ❌" stamp | One passes every 6 f; bounces with spring |
| **P-51** | **Shape sorter** (validation) | Inputs fall toward a slot; the right shapes pass with a green ✓, the wrong ones bounce off with a red ✕ | Fall with gravity 14 f; reject bounce 8 f |
| **P-52** | **Key hunt** (hidden secrets) | A magnifier scans illegible code-shaped lines and finds a glowing 🔑 "API KEY"; the old key crumbles, a new one is minted | Scan 20 f; find pulse; crumble 10 f; mint 8 f |
| **P-53** | **Ghost package** | A row of boxes, one translucent and flickering ("doesn't exist 👻"), one cracked ("kamzor") | Ghost flicker 2 f on/off; crack 6 f |
| **P-54** | **Scary → simple** | A wall of blurred, illegible red error texture morphs into one friendly line ("Kuch galat ho gaya, dobara try karo") | Blur-to-card morph 12 f |
| **P-55** | **Upload filter** | Files drop at a gate: a ".exe" bounces, an oversized file is squeezed and rejected, a valid image passes | 3 files, 10 f each |
| **P-56** | **Data wall** (access control) | User A's cursor drags toward User B's folder; a red laser wall slams up; a "BLOCKED" stamp; a green "RLS ON" chip | Drag 14 f, wall 4 f + Z-5, stamp 5 f |
| **P-57** | **X-ray scan** | A scan line passes down the mock; weak spots light up as red holes with labels | Scan 24 f; holes pop with a 3 f stagger |
| **P-58** | **Shield meter** (a checklist spine) | An N-segment shield; each check lights a segment green with ✓; the final "7/7 SECURE" | 6 f per segment; the full shield glints |
| **P-59** | **Hero number from people** | The giant number ("5,000") assembles from the crowd's dots flying into the glyph shapes | 24 f gather, then a Z-5 slam |
| **P-60** | **Static vs alive** (mode V) | Left: the still version, 😴, grey. Right: the same with live motion, sparkles, a green "ALIVE" chip | Left frozen; right loops |

In other niches the machines re-skin: P-40 counts coins instead of people; P-42 becomes a "BUDGET" gauge; P-47 is a salary
splitting into jars; P-50 is an auto-debit rule stopping impulse buys; P-56 is a wall between "savings" and "spends".

**Result and comedy (B-14, B-15)**
| ID | Pattern | What | Motion |
|---|---|---|---|
| **P-61** | **Bad → premium** | The hook's core: the bad card → shatter (T-19) → the light-sweep premium (T-20) | §6.2 |
| **P-62** | **Flaw markup** | Red marker circles + Permanent Marker notes on the real flaws (§8.6) | Circle 8 f, note 10 f, 6 f stagger |
| **P-63** | **Stamp verdict** | Rubber-stamp text ("AI SLOP", "BEKAAR", "BLOCKED", "SECURE ✓") in `bad` or `good`, a 6 px rough-edged border | Scale 1.6 → 1 in 3 f, rotate −12°, Z-5 shake on the same frame, 3 dots of ink splatter; the roast keyword (CS-2) pops on the same beat |
| **P-64** | **Freeze-frame roast** | The footage freezes (desaturated 60 %, a 1.25× crash zoom), a pink marker circle + arrow + note ("ye tum ho 😭"), a "⏸" icon top-left | Freezes on the word, holds 18–30 f, unfreezes with a Z-3 |
| **P-65** | **Meme sticker** | A STICKER (§5.6) near the subject | Pop 6 f, wobble 12 f |
| **P-66** | **Depth hero + orbit** | The premium result behind the creator (G-5); 3–4 feature chips orbit it on an ellipse | 1 revolution per 4 s; chips scale by depth |
| **P-67** | **Slab flip** | T-21 on the slab's chip | 4 f |
| **P-68** | **Key-cap CTA** | The keyword on a 3D yellow keyboard key; it presses; the deliverable flies into a DM bubble (§6.7) | Press 8 f, then a 14 f arc flight |

Build notes: every pattern is a scene in `plan/scenes.js` (crowds and shards on one `<canvas>` per layer; counters and
figures through `VEOS.data` and `ctx.fmtNum`); stage moves are `timeline.stage` vias; zooms are `timeline.camera` presets;
a real product's UI is the real one, the creator's or fetched (§12.6); device mocks carry the generic result pairs.

### 8.4 Line → pattern lookup
Vocabulary, not a decision table: it tells you what this style reaches for. Ask what the moment needs, then use it.

| Line type | Primary | Alternates |
|---|---|---|
| "Ye tumhara `<thing>` hai" (a roast of the viewer's result) | P-61 + P-62 + P-63 | P-64 |
| "Aur ye maine banaya" (the premium result) | P-61 reveal + P-66 | P-35 live preview |
| "N log aaye / users / traffic / customers" | P-40 Crowd counter | P-41, P-59 |
| "Phat jayega / slow / crash / fail" | P-43 Crash device + P-42 | P-45 |
| A small vs big comparison | P-44 Versus lanes | P-45, P-60 |
| How a fix works (index, cache, queue, automation) | Metaphor machine P-46 / P-47 | P-23 flow |
| "Test kar lo / try it before" | P-48 Load-test swarm | P-42 |
| "X is unsafe / a gift for scammers" | P-49 Gift-box exploit | P-57 |
| Limits / filters / spam | P-50 Bouncer gate | — |
| Validation / rules / eligibility | P-51 Shape sorter | — |
| Secrets / keys / passwords | P-52 Key hunt | — |
| Fake or weak dependencies / products | P-53 Ghost package | — |
| Scary messages / jargon simplified | P-54 Scary → simple | — |
| Uploads / what gets in | P-55 Upload filter | — |
| "One person sees another's data / money" | P-56 Data wall | — |
| Checklist progress | P-58 Shield meter (SM-8) | SM-9 |
| A mocking aside about the viewer | P-64 freeze-frame or P-65 sticker + Z-2 | Mode R bubble |
| Static vs living | P-60 | P-44 |
| A tool / step / site (not data) | P-05, P-06, P-08, P-10, P-01 | P-16, P-09 |
| A concept's name | P-18 glow title | P-13 KT |
| Proof of the creator's own result | P-17 | P-14 |
| "Inflation khaa jayega" (something outgrowing something) | P-45 overflow bars | P-44 |
| "Har mahine ₹X daalo, Y saal mein…" (growth over time) | P-40 as coins + HERO-NUM (figure `compound`) | P-44 |
| A third-party moment (a tweet, headline, another creator's clip, a product UI) | the creator's file, or the real one fetched from the web, in a card (P-16) | rebuilt from its exact text: quote card, headline card, recreated UI (§12.6) |
| The comment CTA | P-68 Key-cap CTA | P-30 |

### 8.5 Data Theatre rules (D5: make them *see* it)
1. **Quantity is countable.** 5 is five avatars and 5,000 is five thousand dots. Never a lone number on a card.
2. **Same axes.** A comparison uses identical frames and scales (P-44; one `scale_id`); only the variable changes.
3. **Show the mechanism, not the jargon.** An index is a book index, caching is make-once-serve-many, rate limiting is a
   bouncer. The label names it once (CS-3 violet), then the machine runs.
4. **A state change is a colour change.** OK is cyan or green, stressed is yellow, broken is red. The change lands on the
   spoken word ("aaye", "phat jayega").
5. **One idea per screen.** At most three animated groups at once; everything else dims 40 %.
6. **Synced to speech:** counts finish on the number word (±5 f), crashes land on the crash word, fixes land on the fix
   verb.
7. **Say what was said.** A number the creator says is shown as said, as a figure in `plan/figures.json` with its
   provenance (the script, or `spoken@<t>`); derived numbers come from a formula (`sum`, `diff`, `ratio`,
   `percent_change`, `per_period`, `unit_convert`; finance reels may add `compound` / `cagr`), never typed. A number the
   script frames as hypothetical ("agar 5,000 users aaye") is an illustration: `illustrative: true`, no label. Every number
   is written with `ctx.fmtNum` in the copy's format.
8. **Escalate.** The last item gets the biggest data move: a hero number, the full-screen stage, the bubble.

Figure kinds this style uses: `counter` (P-14, P-40), `hero_number` (HERO-NUM, P-59), `bar` (P-45), a two-lane `counter`
on one `scale_id` (P-44), `grid_fill` (P-40 crowds, P-58 shield), `ledger` (P-47 jars). Gauges (P-42) follow a counter.

### 8.6 The comedy layer and the ink
- **Who's in it:** CAP-MARKER notes, marker circles and arrows, stamps (P-63), stickers (P-65), freeze-frame roasts (P-64 /
  T-22), crash zooms (Z-2), rotation snaps (Z-7), meme hits (§11.3).
- **When:** `mock` beats only, plus the one `win` relief sound. Never on `explain`, `awe` or `cta`, never under a trigger
  word. Comedy Pink appears only here.
- **How much:** a joke lands because the edit around it is clean. Every comedy device is a punchline; spend them on the
  roasts that deserve them, and the crash zoom and the freeze on the very best.
- **The ink** (the roast is drawn by hand): circles draw on in 8 f, overshooting the start point by 15°; arrows draw the
  shaft in 6 f, then the head in 2 f; underlines wipe L → R over 6 f, slightly wavy; marker notes wipe on over 10 f. Strokes
  6–8 px (circles 8 px) with a 1.5 px wobble, in `bad` red on light backgrounds and `comedy` pink with a 3 px white outline
  on dark ones; the slab's underline is `accent`. At most three marks on screen, 6 f apart, finished before the next scene.
  Marks sit on the real flaw (the gradient, the three identical cards, the 3 % rate) or around the creator's frozen frame,
  beside the face rather than on it: a circle around the head keeps ≈ 40 px clearance and the arrow points from outside. Placed
  statically at the beat start. An `explain` beat may use a single neutral `accent` underline.
- **If the creator's copy turns comedy down** (`profile.tone.comedy`): `light` keeps the visual gags and drops the meme
  sounds; `off` turns `mock` beats into `explain` beats.

### 8.7 Assets
- **Real captures** for the tools, sites and prompts the creator names: their own screen recordings first, else the real
  page captured from the web.
- **Result mocks** (the bad and premium sites, phone apps) are built live as **generic, unbranded** designs (B-15), or
  captured from the creator's real builds (better for the premium state).
- No AI stock scenes, no stock clichés. Blur private data (emails, keys, account numbers). Logos: the creator's files
  first, else the real logo fetched from the web; a logo plate only when none can be found.
- Third-party moments: fetch the real thing, source noted (§12.6).

---

## §9 Transition system (T-…)

### 9.1 Library (30 fps)
| ID | Transition | Frames | Recipe | Sound role |
|---|---|---|---|---|
| T-01 | Orange light streak | 8–10 | A diagonal `accent` light bar (white-hot core ≈ 36 px, a thick orange glow ≈ 100 px, `#F94F00` → `#FCEF2D`, ≈ 20° off vertical) crosses the frame L → R, bright and even for ≈ 9 f with near-linear travel; the change happens under it at mid-crossing (measured r01, r06, r07). Build: one `VEOS.fx.streak` bar `{at, frames: 9, angle: 20, count: 1, spread: 0, bar: true, width: 100, color: "accent", glow: 100}`; the engine adds the white-hot core and holds it at full strength for the whole sweep | flash / whoosh |
| T-02 | Silhouette strobe | 6 | f0 shows the composed frame; f1, f3 and f5 replace the creator with a solid white cut-out silhouette (three flashes in the first 6 f), measured r01 | impact |
| T-03 | Zoom-blur slam | 6–7 | A radial zoom blur 1.0 → 1.25 into the cut; the new shot lands sharp at 1.0. Built in: `{"t", "type": "zoom-blur", "frames": 7, "pre": 4, "punch": 0.25, "at": "face"}` | whoosh + sub-hit |
| T-04 | Panel drop | 4–5 (+ marker 3–4, card 8–12) | G-1: a hard cut to the take, then the full frame drops into the panel with heavy vertical motion blur; the canvas or stage is revealed; the marker, then the card, rise | list cue / whoosh |
| T-05 | Warm leak lift | 15 | A slow warm leak lifts across the frame, cross-revealing the next shot (calm `awe` moments). Built in: `{"t", "type": "leak", "frames": 15}` | shine |
| T-06 | Return to full | 0 or 4–8 | A hard cut, or the panel rises back to full | — |
| T-07 | Invert flicker | 4–6 | 1–2 frames of colour invert | glitch |
| T-08 | Exposure pop | 2 | Exposure +0.6 for 2 frames on a landing | impact |
| T-09 | Jump cut | 0 | A cut on a word boundary (±1 f) inside the take | — |
| T-10 | Whip blur jump | 3–4 per side | A horizontal motion blur out of shot A and into shot B. Built in: `{"t", "type": "whip", "dir": "left", "frames": 8, "pre": 4}` (`dir: "right"` for the reverse) | whoosh |
| T-11 | Card grow | 10–13 | The card grows from a chip or icon to the card zone | pop |
| T-12 | Card push swap / dissolve evolve | 4–5 + 6–8, or 3–4 | The old card pushes out (4–5 f), the new one pushes in (6–8 f). Inside an item the card more often **dissolves** into its next state in 3–4 f (book → index page → versus lanes, measured r06), sometimes after a diagonal shine passes over it (6 f) | swish |
| T-13 | Smear inset | 4–5 | A smeared inset card stretches in from an edge | swish |
| T-14 | Shrink-zoom to dark | 6 | The frame shrinks and zooms into black, landing on the Data Stage | whoosh |
| T-15 | Haze cut | 1 | One frame of white haze over the cut. Built in: `{"t", "type": "flash", "frames": 1, "pre": 0, "peak": 0.5}` | — |
| T-16 | Hard end | 0 | The last frame, ≤ 6 f after the last word; no black tail | — |
| **T-17** | **Pop-back** (G-2) | 5 | f0 the item graphics clear (hard); f1–2 the panel grows to full frame (light vertical blur); f2 overshoot ≈ 1.10; f3–5 settle to 1.00 (measured r01). Stage entry `{"via": "pop-back", "dur": 5, "overshoot": 0.1}`; the subtitles stay on through it. The next jump cut may take a Z-1 punch | swoosh-up |
| **T-18** | **Zoom-through** | 10–12 | The camera dives into an object (a phone screen, the pointing hand, a card node): 1 → 6× with radial blur on the last 4 f. The object's fill becomes the next scene's background (the phone screen → the Data Stage) | zoom whoosh |
| **T-19** | **Shatter** (the bad exit) | 10–12 | The card freezes; a **full-frame white haze** for 2 f (≈ 70 % → 30 %, over the creator too); then angular shards (the stamp and markers break with it) burst outward and fall with seeded spin and gravity over ≈ 9 f, their edges catching a 2 px white highlight (measured r01, r06). Build: `VEOS.fx.flash({at, up: 1, hold: 0, decay: 3, peak: 0.7})` + `VEOS.fx.shatter({at, hold: 2, frames: 9, cols: 3, rows: 3, x, y, w, h})` on the card's rect: it breaks the card scene as it was on the break frame (18 shards; put the impact `cx, cy` on the stamp). No asset needed. The stamp and markers are separate scenes: end them on the shatter frame | glass/impact, with a meme hit before it if `mock` |
| **T-20** | **Light-sweep reveal** (the premium entry) | 8–12 | Starts while the shards still fall: the T-01 streak crosses L → R and the premium card is there behind it (r01), or slides in from the right edge in 4 f (r06), or the whole composition pushes 1.0 → 1.5 in 6 f with the streak (r07: Z-2 with `p.target: "all"`, cards included). A bloom flare on exit | riser into an impact |
| **T-21** | **Slab flip** | 3–4 | The slab chip rotates on the X axis 0 → 90° (2 f), swaps text and colour, 90 → 0 (2 f); the slab bumps 1.04 (measured r06 "5,000" red → green ✅; r10 "KISSING HACKERS" → "SECURE ✓") | shine |
| **T-22** | **Freeze-frame** | 0 + hold | The footage freezes on the punch word, desaturates 60 % over 3 f, Z-2 crash 1.25×; P-64's marks draw; it unfreezes with Z-3 | record scratch or sudden stop (a meme, once) |
| **T-23** | **Slide-aside** (G-3) | 8 | The panel narrows to x 0–450 with rounded right corners; the B-roll grows into x 470–1060 | soft swish |
| **T-24** | **Bubble shrink / grow** (G-4) | 8 | The footage → a Ø 300 circle at bottom-left (elastic overshoot 1.15); the reverse returns to full frame | pop (shrink) / swoosh (grow) |

### 9.2 Grammar
| Boundary | Use | Never |
|---|---|---|
| Frame 0 | The slab at rest + T-02 / T-03 / the VS devices | A static or faded-in frame |
| Bad → premium (the hook) | **T-19 → T-20** (+ T-21 on the slab) | A crossfade, a hard cut |
| Hook → item 1 | T-04 (canvas) or **T-18** (into the Data Stage) | — |
| A new item | T-04 / T-18 / the SM-9 chapter interstitial + the marker on the ordinal word (one entry type per reel) | A bare hard cut |
| Item → the creator (an opinion, a roast) | **T-17 pop-back** (default) or T-01 | — |
| The creator → a full-screen graphic while they keep talking | T-24 bubble | — |
| A comparison | T-23 slide-aside or a mode V wipe | — |
| A mock punchline on the creator | T-22 freeze or Z-2 | — |
| Card → card | T-11 / T-12 / evolve | A still jump |
| A number lands | Z-5 shake + T-08 | — |
| The last word | T-16 | A black tail |

### 9.3 The transition map (part of the plan; sounds are catalogue ids)
```yaml
transitions:                    # the r01 hook
  - {t: 0.00, id: VS-1+G-5, to: HOOK, cue: abstract-hit-sub-bass-07}
  - {t: 2.10, id: T-19, from: bad, to: premium, cue: zoom-in-riser-zoom-in-riser}
  - {t: 2.60, id: T-20, cue: cinematic-hits-2025-02-19-18-27-16-utc-cinematic-hit-4}
  - {t: 2.62, id: T-21, cue: short-shine-2025-08-27-06-45-01-utc-short-shine-2}
  - {t: 7.40, id: T-18, from: HOOK, to: D, note: "on 'Pehla'", cue: zoom-2025-05-09-19-11-57-utc-zoom-2}
  - {t: 14.2, id: T-17, from: D, to: F, cue: swoosh-2025-01-08-03-02-26-utc-swoosh-06}
```

### 9.4 How the moves breathe
T-17 is the workhorse (T-01 was the old one; reach for it when a beat wants heat). The shatter and the light sweep belong
to the hook, and come back once at most, for a payoff that deserves them. Every item enters the same way; everything else
varies so no move feels like a loop.

---

## §10 Motion tokens, camera and zoom system, layers, finishing

### 10.1 Motion tokens (30 fps)
| Token | Value |
|---|---|
| Beat lead | 2 f before the onset |
| Keyword pop (CS-2) | Scale 0.5 → 1.0 in 2 f, no overshoot (measured) |
| Squash-pop (the roast word, stickers) | Scale y 0.7 → 1.15 → 1, x 1.2 → 0.95 → 1, 3 f |
| Elastic overshoot (bubble, badges) | `cubic-bezier(0.34, 1.56, 0.64, 1)`, 8 f |
| Entries | `cubic-bezier(0.22, 1, 0.36, 1)` (expo-out) |
| Exits | `cubic-bezier(0.64, 0, 0.78, 0)`, 4–5 f |
| In-out | `cubic-bezier(0.65, 0, 0.35, 1)` |
| Marker circle draw | 8 f, overshooting the start by 15° |
| Typewriter | 1 letter per frame, blur 6 → 0 |
| Counter | 18–30 f ease-out, or a slot roll |
| Stamp | Scale 1.6 → 1 in 3 f, rotate −12°, with Z-5 on the same frame (measured r01) |
| Shake (Z-5) | ±10 px, 4 f, seeded, decaying, + a 1.03 bump |
| Slab rocket exit | 4 f up with vertical blur |
| Idle bob (badges, count tiles) | ±6 px sine, 1.5 s period |
| Orbit | 1 revolution per 4 s, ellipse aspect 0.35, chips scale 0.8–1.1 by depth |
| Crowd pour | Seeded positions, 120 elements per frame, each with an 8 f fall |
| Hold | Titles ≥ 10 f after complete; text ≥ 0.25 s per word |

Every crowd, particle and shake is seeded from the frame number, so a frame always renders the same.

### 10.2 Zoom system (Z-1…Z-7): snappy, dynamic, always on meaning
| ID | Zoom (preset) | Recipe | Tone / use |
|---|---|---|---|
| **Z-1** | **Cut-punch** (`snap-punch`) | **The common form (measured):** on a jump cut the new take lands already reframed, 1.00 → 1.10 (tripod; measured 1.08–1.12) or 1.25 (selfie), held until the next cut, then reset on the cut after. A 3 f animated version with motion blur works on a word inside one take | `hype` / `win` emphasis; jump cuts alternate plain and punched |
| **Z-2** | **Crash zoom** (`crash-zoom`) | 1.00 → 1.50 in 5 f, ease-out, with a ±3° roll, held 8–20 f or to the next cut. With `{"preset": "crash-zoom", "p": {"target": "all"}}` the whole composition, cards on z1–6 included, pushes (r07, with a T-01 streak); captions and z7+ stay put | A `mock` reaction or a premium reveal: the best roast of the reel |
| **Z-3** | **Snap pull-out** (`pull-out`) | 1.35 → 1.00 in 4 f | Revealing a graphic beside them, an unfreeze, the `cta` |
| **Z-4** | **Push drift** (`push-drift`) | 1.00 → 1.06 over the beat (the hook's footage between cuts; cards drift with a 2–4° tilt while their content ticks) | `awe`, the premium reveal, a calm explanation |
| **Z-5** | **Impact shake** (`shake`) | ±10 px over 4 f + a 1.03 bump | Stamps, hero numbers, crashes, walls, `warn` |
| **Z-6** | **Zoom-through** (`zoom-through`) | = T-18 (1 → 6× in 10–12 f) | World changes |
| **Z-7** | **Rotation snap** (`rotation-snap`) | 0 → −3.5° in 3 f, reset at the next cut | The `mock` tilt ("ye tumhara `<thing>`…"); a seasoning, not a habit |

**How to zoom:**
- Zoom on meaning (emphasis, a roast, a reveal), never on every cut. Selfie jump cuts alternate: plain, Z-1, plain, Z-7…
- Change the kind of zoom from one to the next so the camera feels alive, not mechanical. Two camera moves closer than
  about 0.4 s read as a stutter.
- A zoom never pushes the face out of the safe frame or up under the slab.
- Source resolution: a 1080-wide source punches cleanly to about 1.35×; the crash zoom wants a 4K source (≥ 1836 px wide
  covers even a 1.7× crash); on 1080p, cap it near 1.35×.

### 10.3 Tone decides the treatment
| Tone | Colour | Zoom | Visual treatment | Sound family (§11) | Sound vs voice |
|---|---|---|---|---|---|
| `hype` | Yellow | Z-1 | The slab, chips, CS-2, count tiles | Whoosh, sub-hit, pop | −14…−20 dB |
| `mock` | Pink / red | Z-2, Z-7, T-22 | The comedy layer: stamps, markers, stickers | **Meme hits** (§11.3), marker swipe, stamp thud | Meme −6…−12 dB (it must be heard) |
| `awe` | Orange / green | Z-4 | Clean premium: the T-20 sweep, glow, no comedy | Riser → cinematic hit, shine, sparkle | −12…−16 dB |
| `explain` | Cyan / violet | rare | Cards, flows, machines | UI pops, digital text, light typing | −22…−28 dB |
| `warn` | Red | Z-5 | Tension: red states, the crash device, alarms | Tension riser, alarm, glitch, low boom | −14…−20 dB |
| `win` | Green | Z-1 | ✓, shields filling, green stamps | Ding, level up, correct; the one `win` meme ("sukoon") | −16…−22 dB |
| `cta` | Yellow | Z-3 | The key-cap, the community card; no meme sounds | Key click, shine, swoosh | −18…−22 dB |

### 10.4 Layer order (back to front; engine z)
1. Background (canvas / night stage / footage), z1
2. Glow, z2
3. Cards and Data Theatre, z3
4. **The creator's cut-out** (cards marked `behind: true` sit under it: the depth sandwich) *or* the speaker panel, z4
5. Labels and stacked words, z5
6. Markers and badges, z6
7. CS-1 subtitles, z7
8. CS-3 glow / CS-2 chunky, z8
9. The comedy layer (marker notes, stamps, stickers), z9
10. The Headline Slab, z10
11. Light passes (T-01, the T-20 sweep, T-08), z11

### 10.5 Finishing
- No grain, no vignette. Glow only on Data Stage hero elements, CS-3, badges and the T-20 sweep.
- Card radius 24–55 (default 40). Hard ink shadows only on the slab, chips, stickers and stamps (the "sticker" family);
  soft shadows on content cards.

---

## §11 Sound design

### 11.1 Tone palettes
The tone of each beat picks the sound family and its level (§10.3). A sound marks a real visual moment: a card landing, a
word popping, a move, a number landing, a warning, the key-cap. No cue without a visible event; silence beats a wrong sound.
Never more than two cues overlapping, and no cue on a trigger word's consonant (shift it ±2 f).

### 11.2 The ledger (D7)
Every reel's sounds go into a ledger: file → uses → times.
- **Any file ≤ 2 uses.** The one exception is the **parallel list cue**: the single sound that marks the entries of item 1,
  2, 3…; it may repeat once per item. Only one file per reel is the list cue.
- **Meme files: one use each.**
- **No file on two consecutive cues.** Rotate inside a pool (Woosh 01 → Swoosh 02 → Fast Swish → Woosh 03…).
- This is the creator's own directive, born from "the same whoosh everywhere": keep the count as you place the cues.

### 11.3 Meme sounds (D2, `mock` only)
**When:** the creator mocks the viewer's result, assumption or habit ("wo ekdam bekaar hai", "paanch nithalle dost",
"hackers ke liye gift", "Kya bro…"). Never on an explanation, a premium reveal or the CTA.

**How:**
- The hit lands in the **gap right after the punch word** (0–4 f after the word ends), never over a word.
- Pair it with a visual: a stamp, a freeze, a crash zoom or a sticker.
- A meme hit is a punchline: each a different file, and space them so each one lands on its own.
- Don't duck the voice for them. Trim tails to ≤ 1.2 s (the vine boom to 0.9 s).

| Meme (catalogue id) | Use it for |
|---|---|
| `vine-boom-sound-effect-128k` | The verdict lands: the "AI SLOP" stamp, a shocking fact about their thing |
| `fahh-sound-effect-sowasfx-sowasfx` | Facepalm: their bad result, a classic mistake |
| `record-scratch-record-scratch` / `scratchrecord-ec04-40-2` | "Wait, what?": a freeze-frame, the record-stop before a pivot |
| `sudden-stop-sound-effect-anne-ghanda-vlog` | A hard freeze-frame roast (P-64) |
| `shocked-sound-effect-shravan-10-sound-effects` | Indian TV-serial shock: the crash zoom on "hackers ka gift", "app phat gaya" |
| `windows-xp-error-meme-doomtheboom` | Their app or site breaks (the crash device, an error moment), trimmed to the "dun" |
| `disappointed-sound-effect-hd` | A crowd "ohhh": a letdown (their app after 5,000 users) |
| `crowd-aww-sound-effect` / `aww` | Mock sympathy: "5 nithalle dost" |
| `cartoon-dizzy-bang-with-chirps-01-2025-02-17-20-48-05-utc-39281-cartoon-dizzy-bang-with-chirps-01-full` | The app gets knocked out (P-43's end) |
| `funny-pan-hit-sound-effect-128k` / `slap-sound-effect-128k` | A reality-check slap on a wrong belief |
| `funny-effect-20` | A deflating claim ("secure hoga bro?" → no) |
| `comedyaccent-mix64-44-4-rev` | The suck-in right before a punchline |
| `06830-tabla-up-triple-collect` | A desi flourish on a cheeky reveal |
| `windows-startup-meme-sound-effect` | A "booting up" gag (the AI starts working), trimmed |
| `shorts-experiment-memes-sukun-ka-naam-suna-hai-means` | **`win` only, once in a reel:** the satisfying fix ("itna sukoon"), trimmed |

**Never:** profanity; rage and screams; romantic or kiss cues (unless the script is literally about it); devotional chants;
regional-language clips that don't match the reel; AI voice-overs; any copyrighted song.

### 11.4 Premium pools (rotate; ≤ 2 uses per file)
Pick from the SFX catalogue by role and vibe; these are the anchors the reference reels used.
| Job | Catalogue role | Anchors |
|---|---|---|
| Whoosh / move | `whoosh`, `swish` | `fast-swish-movement-fast-swish-movement` (the usual list cue), `swoosh-2025-01-08-03-02-26-utc-swoosh-06`, `zoom-2025-05-09-19-11-57-utc-zoom-2` |
| Hook hit / impact | `sub-hit`, `impact` | `abstract-hit-sub-bass-07`, `cinematic-hits-2025-02-19-18-27-16-utc-cinematic-hit-4`, `electric-hit-2025-02-20-01-45-58-utc-electric-hit-1` |
| Riser | `riser` | `zoom-in-riser-zoom-in-riser`, `tension-riser-2025-08-27-06-26-50-utc-tension-riser-1` (`warn`) |
| UI pop / click | `pop`, `click`, `tap` | `game-pop-up-2025-08-27-06-39-58-utc-game-pop-up-2`, `pop-up-pop-up`, `selection-click`, `digital-click` |
| Shine / win | `shine`, `ding`, `chime`, `sparkle` | `short-shine-2025-08-27-06-45-01-utc-short-shine-2`, `level-up`, `ui-sparkle` |
| Marker / ink | `swish` | `marker-swipe-9`, the board-marker circle and line files |
| Data | `typing`, `riser`, `click`, `cash` | `digital-scan` (X-ray, key hunt), `digital-text-2026-05-18-01-34-24-utc-digital-text-01`, `telemetry-graph-rising-01-2025-08-27-06-33-50-utc-36877-telemetry-graph-rising-01-full` (counters, gauges), `cash-machine-2025-02-19-03-33-58-utc-cash-machine` |
| Danger / failure | `glitch`, `alarm` | `glitch-2025-01-08-02-40-44-utc-glitch-04` (system failure) |
| Camera / freeze | `camera` | `camera-shutter-2025-02-19-17-59-23-utc-dslr-camera-shutter-v1` |

### 11.5 Bed, silence, outro, mix
- **The bed:** ducked hip-hop / trap / lo-fi, 80–146 BPM, 18–22 dB under the voice. It enters on the hook → item 1
  transition (the hook is dry of music). Never a copyrighted song.
- **Drop-out:** mute the bed for 0.5–1 s before the biggest payoff or reveal; it returns on the hit.
- **Record-stop:** ≤ 0.3 s of near-silence before a pivot or punchline (a meme scratch may sit there).
- **Before the CTA:** a second of quiet before its first word.
- **Outro:** a hard stop ≤ 6 f after the sign-off; an optional ≤ 1 s button no louder than the voice.
- **Mix:** voice chain (high-pass 80 Hz, de-ess, light compression) → −14 LUFS integrated, true peak ≤ −1.5 dBTP.

---

## §12 Footage handling

### 12.1 Setups
| Setup | Use | Framing |
|---|---|---|
| A: Selfie | Handheld front camera at arm's length: roasts, reactions, crash zooms | head top y 180–420 |
| B: Tripod seated | At the desk (monitors behind): panel and full | head top y 260–520 |
| C: Tripod standing | At the desk / monitors | head top y 200–420 |
| D: Skit wide | High angle, clone passes (HA-14) | head top y 300–700 |

Low-key warm practicals; a dark plain tee reads best under the yellow slab; the mic may be visible.

### 12.2 Crops
- `F`: as shot, with the Z-zooms.
- `S` / `D` panel: the head top sits at panel top + 60…110, the face at x 340–560.
- **Bubble (G-4):** the face centred in the circle, filling 70 % of Ø 300.
- **Slide-aside (G-3):** the face centred in x 0–450.
- **Depth sandwich (G-5):** the cut-out placed so the head top sits ≥ 40 px below the slab's bottom and a hand or shoulder
  overlaps the card corner by 60–140 px.

### 12.3 The cut-out (required)
The engine's matte (or DaVinci Resolve Magic Mask / RobustVideoMatting; `rembg` `u2net_human_seg` for stills). Feather 2 px,
choke 1 px, temporal smoothing; check the hair at 200 %. The alpha covers the whole clip: the depth sandwich, the bubble, the
lean-in, the silhouette strobe and the world swap all depend on it.

### 12.4 The reaction bank
When the creator has recorded one, 2–3 s of each: a smirk at camera, a facepalm, a slow head-shake, a pointing-up "ye
dekho", a shocked face, a shrug, a "chef's kiss". They feed the T-22 freezes, the G-4 bubble and the G-6 lean-in when the
main take has no usable reaction; without them, FB-3.

### 12.5 Shots and fallbacks
| ID | Shot | Spec | Without it |
|---|---|---|---|
| SH-1 | Screen captures | Every tool, site, prompt and doc named; ≥ 1080 px wide, 30 fps | **FB-1:** the real page captured from the web in a card; else a generic, unbranded device mock (B-15) or a recreated UI card (it holds) |
| SH-2 | The creator's own premium result | Their own site/app/result screen, live | **FB-2:** the premium state built live (a dark motion site, serif display, live animation); not their own build, but it holds |
| SH-3 | The reaction bank | §12.4 | **FB-3:** a T-22 freeze of the nearest usable frame of the main take (a weaker face) |

### 12.6 Third-party moments: fetch the real thing
When the creator names a real tweet, headline, article, another creator's reel, a product UI, a person or a brand, the
viewer should see the real one.
1. The creator's own files in their folder come first.
2. Otherwise search the web and fetch it: the real logo, the real post, the real page (captured and framed on the part
   that matters). Note where it came from.
3. Use it as it is (cropped, framed in a card, highlighted in marker), never altered to say something it doesn't; a post or
   headline is shown word for word.
4. Nothing usable to be found: rebuild it from its exact words: a quote card, a headline card, a recreated UI (the B-15
   look), a diagram or data card, a logo plate (the name set in type in a neutral chip), a silhouette instead of a person.
   No labels, no credit lines.

The result pairs are generic mocks or the creator's own builds, so they aren't third-party moments; a real product's UI
shown by name is.

### 12.7 Frame rate and audio
Output 1080×1920, 30 fps CFR (conform phone VFR), BT.709. The reference finals are 60 fps files carrying 30 fps content:
build at 30. One voice track.

---

## §13 What your plan should settle

Your `ideas.md` is a page or two, for you. In this style it has decided, before any code:
1. **The hook:** the result pair and how each state is produced (captured or built live); the slab text with its
   alternates; the VS devices; every hook beat to the frame.
2. **The tone of every line**, and so every beat's colour, zoom and sound family.
3. **The data story:** a Data Theatre machine for every number, comparison and risk, with its figures.
4. **The moves:** the worlds, every panel drop and pop-back, the item ritual and its marker, the transition map (§9.3).
5. **The comedy:** which lines are roasts and which device each one gets.
6. **The sound ledger** (keep it in your notes as you go):
```yaml
sfx_ledger:
  vine-boom-sound-effect-128k: {uses: 1, at: [1.70], role: meme}
  fast-swish-movement-fast-swish-movement: {uses: 4, at: [7.4, 15.1, 22.6, 31.0], role: LIST-CUE}   # the one allowed repeat
  woosh-2025-08-27-02-12-31-utc-woosh-02: {uses: 2, at: [12.0, 27.3]}
```
7. **The moments you'll look at hardest on the storyboard:** f0 (the thumbnail), the roast, the reveal, one Data Theatre
   beat, one pop-back, the CTA key-cap.

---

## §14 Worked examples

The first three are the reference reels themselves (spoken in Hinglish; the style works the same in English). Times are
estimates: take the real ones from the words. They show the standard; match it, then beat it.

### 14.1 Hook, r01 "Claude ko ye 3 design skills sikha do" (keyword SKILLS)
- **Spoken:** "Haan bhai, Claude se website bana li, wahi purple gradient, wahi AI slop, ab isko aisa banate hain."
- **Slab:** "Your Claude website 🤢 vs **MINE** 🔥" (B-VERSUS). HA-01.

| t (s) | Spoken | Tone | Visual | Caption | Zoom | Sound (catalogue id) |
|---|---|---|---|---|---|---|
| f0 | — | hype | Slab + the bad site card (tilted 4°) + the cut-out pointing at it (G-5), T-02 strobe | — | — | `abstract-hit-sub-bass-07` |
| 0.2 | "Haan bhai, Claude se website bana li" | mock | Card push-in; circle 1 "purple gradient" | CS-2 "Claude se / **WEBSITE**" (Claude in its brand colour) | Z-7 | `marker-swipe-9` |
| 1.0 | "wahi purple gradient" | mock | Circle 2 "same 3 cards", circle 3 "centred text" | CS-2 "wahi purple / **GRADIENT**" | — | `selection-click`, `digital-click` |
| 1.7 | "wahi AI slop" | mock | **Stamp "AI SLOP"** + Z-5 + 💀 sticker | CS-2 "**AI SLOP**" in red | Z-5 | **`vine-boom-sound-effect-128k`** (+2 f after "slop") |
| 2.3 | "ab isko" | awe | **Shatter** (T-19) | — | Z-3 | `zoom-in-riser-zoom-in-riser` |
| 2.7 | "aisa banate hain" | awe | **Light-sweep reveal** of the premium site (T-20) + slab flip "SLOP" → "PREMIUM" | CS-2 "aisa / **BANATE HAIN**" | Z-4 | `cinematic-hits-2025-02-19-18-27-16-utc-cinematic-hit-4` + `short-shine-2025-08-27-06-45-01-utc-short-shine-2` |
| 4.6 | "Main khud yahi teen skills…" | hype | The three skill names orbit the premium site (P-66) + 3 tiles | CS-2 "**3 SKILLS**" | Z-1 | `game-pop-up-2025-08-27-06-39-58-utc-game-pop-up-2` |
| 9.6 | "Pehla, …" | explain | T-04 into item 1 (canvas), the slab rockets up | black CS-1 | — | **List cue:** `fast-swish-movement-fast-swish-movement` (items 1–3 + the bonus) |

The body (r01): each skill = SM-1 badge → P-05 serif title + P-01 card → P-07 / P-10 chips → G-2 pop-back with a CS-3 glow
word ("BUTTER") → P-03 before/after; the end = G-2 + P-68 key-cap "SKILLS" + P-29 community card.

### 14.2 Data plan, r06 "Users aate hi tumhara app tootega" (keyword SCALE)
**Slab:** "**5** users ✅ **5,000** users 💥" (B-NUMBER, HA-07). **Result pair:** the app smooth with 5 friends → the app
cracking at 5,000. **Spine:** SM-9 progress rail (4 notches). **Figures:** `users_small = 5` and `users_big = 5000`, both
from the script (the 5,000 is the script's own "what if": `illustrative: true`).

| Section | Spoken (gist) | Tone | Mode / pattern |
|---|---|---|---|
| Hook 0–2 | "sirf tumhare paanch nithalle dost hi use karenge" | mock | `D` (G-7 world swap): 5 lazy avatars on a sofa (P-40) on the app phone. Marker note "5 nithalle dost 😴". `crowd-aww-sound-effect` in the gap |
| Hook 2–4.5 | "jaise hi paanch hazaar log aaye, wo phat jayega" | warn | P-41 zoom-out to 5,000 dots pouring in → P-42 gauge to red → **P-43 crash device** (cracks, black, 💀); the backdrop tints red. The slab chip "5,000" pulses red. `glitch-2025-01-08-02-40-44-utc-glitch-04` + `shocked-sound-effect-shravan-10-sound-effects` (the meme, once) |
| Hook 4.5–6 | "agar tumne ye chaar cheezein nahi ki toh!" | hype | G-2 pop-back + Z-1. 4 tiles rise; the slab chip flips red → green ✅ |
| Loop | "Tension mat lo… last mein de dunga" | hype | CS-2; the rail appears |
| 1 Indexes | "book ke peeche wala index…" | explain → win | T-18 into the phone → `D`: **P-46 book index**. Left: a slow scan with a ticking clock. Right: the index jump ✓. Violet CS-3 "INDEX"; the creator in the bubble |
| 2 Caching | "ek baar bana ke save kar lo, har user ko turant" | explain → win | **P-47 fan-out**: 1 card → 12 users; the database chimney idles |
| 3 Load testing | "Claude hazaaron fake users bhej ke bata dega kahan tootega" | warn → win | **P-48 load-test swarm** with ghost users; a marker circle "yahan tootega" |
| 4 Skip Kubernetes | "Kubernetes ke chakkar mein mat padna… asli problem database" | mock → explain | KT-RED "MAT PADNA" + a freeze-frame roast (P-64, `record-scratch-record-scratch`), then **P-44 versus lanes**: "Kubernetes maze" vs "auto-scale host ✓", the database highlighted |
| CTA | "comment kar do SCALE" | cta | G-2 pop-back, **P-68 key-cap "SCALE"** → the deliverable "SCALE – 4 prompts so your app survives going viral" flies to the DM; P-29 card |

### 14.3 Risk plan, r10 "Claude ka app = hackers ka gift" (keyword SECURE)
**Slab:** "Your Claude app is a **GIFT** for hackers 🎁" (B-WARN, HA-01 mock-quote variant). **Spine:** SM-8 shield (7
segments). **The last item escalates** ("sabse khatarnak").

| Item | Spoken | Pattern |
|---|---|---|
| Hook | "Kya bro, Claude ne app banaya hai toh secure bhi hoga bro?" (the mock quote) | Z-7 + `funny-effect-20` deflate; the app card wobbles |
| Hook | "Hackers ke liye toh gift hai ye." | **P-49 gift box** opened by red cursors + `windows-xp-error-meme-doomtheboom` (trimmed) → T-21 slab chip "GIFT" → "SECURE ✓" at the fix promise |
| 1 Rate limiting | "koi tumhari API ko spam na kar paaye" | **P-50 bouncer gate** |
| 2 Input validation | "jo format se match na kare, seedha reject" | **P-51 shape sorter** |
| 3 API keys | "mili toh sirf delete nahi, badlo" | **P-52 key hunt** (`digital-scan`) |
| 4 AI packages | "kuch exist hi nahi karte, kuch kamzor" | **P-53 ghost package** |
| 5 Error messages | "sirf simple message, code ki details nahi" | **P-54 scary → simple** |
| 6 File uploads | "type aur size limit… file kabhi chalni nahi chahiye" | **P-55 upload filter** |
| 7 Access control (the escalation) | "ek user doosre ka data toh nahi dekh sakta? RLS on karo" | The bed drops out 0.6 s → `S-DARK` → **P-56 data wall** "BLOCKED" + Z-5 → shield 7/7 "SECURE ✓" (`level-up`) |
| CTA | "comment kar do SECURE" | P-68 key-cap → the deliverable "SECURE – 7 security checks before launch" |

### 14.4 Full plan in another niche, "Tumhari savings ko inflation kha raha hai" (keyword PLAN)
This shows the same machine on money. **Slab:** "Your savings 🤢 vs **MINE** 🔥" (B-VERSUS, HA-01). **Result pair:** bad =
₹1,00,000 parked at 3 % shrinking in real value against 6 % inflation; premium = the same money split by the creator's
3-rule plan, its bar beating inflation. **Spine:** SM-1 badges (3 rules). **Figures:** `principal = 100000`,
`savings_rate = 3 %`, `inflation = 6 %` (all script); `real_value_5y` = `compound` (illustrative).

| t / section | Spoken (gist) | Tone | Visual (pattern) | Caption | Zoom / move | Sound |
|---|---|---|---|---|---|---|
| f0 | — | hype | Slab + a generic "bank app" phone mock showing ₹1,00,000, tilted 4°, + the cut-out pointing (G-5) | — | — | sub-hit |
| 0.2–1.4 | "Ye tumhari savings hai, 3 % pe padi hui" | mock | Marker circle "3 % interest 😴"; a red down-arrow on the balance | CS-2 "ye tumhari / **SAVINGS**" | Z-7 | marker swipe |
| 1.4–2.1 | "…aur inflation 6 % kha raha hai" | mock | **P-45 overflow bars**: the red inflation bar breaks through the top past the savings bar + stamp "SHRINKING" + 💀 | CS-2 "**INFLATION**" red | Z-5 | a meme hit in the gap |
| 2.1–2.6 | "Aur ye…" | awe | T-19 shatter of the bank card | — | Z-3 | riser |
| 2.6–4.6 | "…mera plan" | awe | T-20 light-sweep reveal: 3 jars (P-47 variant) filling, a green bar overtaking inflation; the slab chip flips "SHRINKING" → "GROWING" | CS-2 "mera / **PLAN**" | Z-4 | impact + shine |
| 4.6–7 | "3 rules, end tak dekhna" | hype | 3 count tiles rise; chips orbit the jars (P-66) | CS-2 "**3 RULES**" | Z-1 | pop |
| Item 1 (emergency fund) | "pehle 6 mahine ka kharcha alag" | explain → win | T-04 → `S`: SM-1 "1" → P-05 serif title "Emergency fund" → P-40 as 6 month-coins dropping into one jar (the counter lands on "6") | black CS-1 | — | list cue |
| Pop-back | "aur tum? credit card pe emergency chala rahe ho" | mock | G-2 + P-64 freeze "ye tum ho 😭" | CS-1 | Z-2 | a meme hit (a different file) |
| Item 2 (auto-invest) | "salary aate hi auto-debit" | explain | T-18 into the phone → `D`: **P-50 bouncer** = the auto-debit rule letting the SIP through first, impulse buys bouncing red | white CS-1, bubble | — | list cue |
| Item 3 (the comparison, escalated) | "₹10,000 mahina, 20 saal" | warn → win | `S-DARK`: **P-44 versus lanes** on one scale: "savings account" vs "index fund", counters rolling to the script's two numbers (figure `compound` ×2, one `scale_id`, illustrative); HERO-NUM on the winner + Z-5 | CS-3 "COMPOUNDING" | Z-5 | impact |
| CTA | "comment karo PLAN" | cta | G-2, P-68 key-cap "PLAN" → the deliverable "PLAN – my 3-rule savings sheet" into a DM bubble; P-29 card | CS-2 | Z-3 | key click + shine |

---

## §15 Your look at the storyboard: the checklist

Watch it once as a stranger with a thumb over the next reel, then once as the editor whose name is on it. Fix what
bothers you, in one pass.

**The style (does it feel like §The feel?)**
- Frame 0 passes the stopper test: the slab reads at thumbnail size, the result and the creator are visible, something
  moves.
- Result first: a result in the first two seconds, the premium state before the hook ends, the shatter and the light
  sweep between them.
- Every number, comparison and risk is a machine you can watch, not a number on a card.
- Every item enters the same way; pop-backs bring the creator back for opinions and roasts; the last item is the biggest.
- Comedy only on roasts, never two in a row; explanations clean; reveals premium.
- Yellow is the loudest thing on screen; red → green is the before/after; pink only in the comedy layer.
- The sound ledger holds (no file over 2 uses except the list cue; meme files once; no file twice in a row); the hook is
  dry of music; the bed drops out before the big payoff.
- Start to end: it never sits still, and it's never random.

**Craft (by eye, in context)**
- The creator's face reads whenever the moment is about them; nothing chops the head or buries the face by accident.
- No text over text by accident; titles hold long enough to read; subtitles out of the way under titles and through the
  hook.
- Every visual lands on its word; cuts sit on word boundaries; nothing teleports, nothing lingers after its point.
- Every number and quote is what was said; illustrations carry no labels; the result mocks are generic or the creator's
  own; fetched posts and headlines word for word; private data blurred.
- English words and brand names spelt exactly, on every card and in the captions.
- Promises paid off: the slab count = the items shown; the CTA keyword readable on its key-cap; the deliverable's title
  correct.
- The file itself (1080×1920, 30 fps, −14 LUFS, a hard end ≤ 6 f after the last word, no black tail) is the render's
  job; it checks it.

---

## §16 Build notes

- **The renderer** is frame-deterministic HTML at 30 fps: crowds of 5,000 seeded people, shard physics, gauges that follow
  counters and word-synced machines are all generated from the words and the plan, so a revision re-renders in minutes.
- **Fonts:** Inter Tight 900, Plus Jakarta Sans 800, Anton, Instrument Serif italic, Permanent Marker, Montserrat 900
  italic, Jost, Silkscreen, Lilita One (+ Gagalin if installed). Pre-paint ₹ ✓ ✕ → and the emoji used.
- **Scene building blocks** (write them as helpers at the top of `plan/scenes.js`, then reuse them across the reel):

| Block | Role |
|---|---|
| `Slab` | The Headline Slab: stroke, offset shadow, chip, marker underline, pulse, flip (T-21), rocket exit (`kind: "banner"`) |
| `DeviceMock` | Browser and phone frames whose content can scroll, lag, glitch, crack (SVG crack paths) and go black |
| `ResultPair` | The bad and premium generators (generic, unbranded) or the creator's captured clips |
| `Shatter` | `VEOS.fx.flash` haze + `VEOS.fx.shatter` (T-19) |
| `LightSweep` | The `VEOS.fx.streak` light bar (T-01 / T-20) |
| `DataStage` | The `data` world + the hero glow drift |
| `Crowd` | A seeded N-person field (avatars → dots), pour, gather-into-glyph (P-40, P-41, P-59) |
| `Gauge` / `Lanes` / `Bars` | P-42, P-44, P-45 (`VEOS.data` + `ctx.fmtNum` for every number) |
| `Machines` | BookIndex, Fanout, Bouncer, ShapeSorter, KeyHunt, GhostPackage, UploadFilter, DataWall, XRay, Shield (P-46…P-58) |
| `Comedy` | MarkerNote, MarkerCircle, Stamp, Sticker, FreezeFrame (P-62…P-65, T-22; `kind: "meme"` on stickers and stamps) |
| Camera | Z-1…Z-7 = `timeline.camera` presets (seeded shake) |
| Stage | G-1…G-7 = `timeline.stage` vias + `behind: true` cards for the depth sandwich and the world swap |
| `KeyCapCTA` | P-68 (`kind: "cta-keyword"`) |
| Ledger | `timeline.sfx` cues (catalogue ids) |

- **Performance:** draw crowds and shards on one `<canvas>` per layer, not DOM nodes; 5,000 dots at 1080×1920 render in
  under 20 ms a frame.

---

## Appendix A. Evidence map
The full map is in `evidence.md`. In short:
| Element | Source |
|---|---|
| Result-first hook, the slab as the strongest element, meme sounds on mocking tone, data motion graphics, the bright palette, no repeated sound files, zooms and splits | The original creator's written directives (D1–D8), 3 Oct 2026 |
| The yellow slab, chunky captions, the canvas split, the panel drop, the orange streak, the silhouette strobe, the zoom-blur slam, the bed after the hook, the DM deliverable CTA | His analysis of 10 reference reels |
| Measured recipes (slab at rest on f0, the hook motion, T-01, T-17, T-19, T-20, SM-9, G-7, W-4, the CS-2 swap and placement, the key-cap and community card) | His finished October reels r01–r10, measured frame by frame |

## Appendix B. Hook-title bank
Ten slabs in the style's voice; fill the slots from the transcript, write 8–10 per reel and pick by the stopper test.
| # | Template | Hook | From the reference reels |
|---|---|---|---|
| 1 | Your `<thing>` 🤢 vs **MINE** 🔥 | HA-01 | Your Claude website 🤢 vs **MINE** 🔥 (r01, SKILLS) |
| 2 | Your `<thing>` is **`<ROAST WORD>`** 💀 | HA-01 | Your vibe-coded app is **BEKAAR** 💀 (r02, FIX) |
| 3 | Don't `<act>` before this **`<CHECKLIST>`** ✅ | HA-01 | Don't launch before this **CHECKLIST** ✅ (r03, LAUNCH) |
| 4 | One person. A full **`<TEAM>`** 🤖 | HA-02 | One person. A full **AI TEAM** 🤖 (r04, TEAM) |
| 5 | **`<N> FREE`** `<tools>` that make `<X>` like a pro | HA-02 | **4 FREE** tools that make Claude build like a pro (r05, TOOLS) |
| 6 | **`<n>`** `<units>` ✅ **`<N>`** `<units>` 💥 | HA-07 | **5** users ✅ **5,000** users 💥 (r06, SCALE) |
| 7 | Your `<thing>`: `<dull state>` 😴 Mine: **`<ALIVE>`** 🔥 | HA-01 | Your site: a photo 😴 Mine: **ALIVE** 🔥 (r07, PREMIUM) |
| 8 | `<Tool>` = your full **`<TEAM>`** | HA-02 | Claude Code = your full **DEV TEAM** (r08, DEV) |
| 9 | **`<N>`** `<things>`. **`<n>`** `<results>`. `<time>`. | HA-02 | **7** prompts. **4** apps. 6 months. (r09, PROMPTS) |
| 10 | Your `<thing>` is a **GIFT** for `<attackers>` 🎁 | HA-01 | Your Claude app is a **GIFT** for hackers 🎁 (r10, SECURE) |

Alternates that also worked: **3** Claude skills that kill AI slop · **5** reasons nobody uses your app · **15** checks
before your site goes live · Your one-person company's **AI TEAM** · Claude builds like a **PRO** with these 🔥 · Your app
**CRASHES** at 5,000 users 💀 · Make your website come **ALIVE** · Turn Claude Code into a **DEV TEAM** 👨‍💻 · The **7**
prompts behind my 4 apps · **7** security checks before you launch 🔐.
