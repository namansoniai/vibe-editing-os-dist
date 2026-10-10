# Lesson Frame Style Playbook (template v2)

## The feel

This reel is a lesson printed on a page, and the page never moves. A black page with a faint grid, a two-line title that
writes itself in the first second and then stays put like a textbook heading, one rounded card under it, and a line of
wide-spaced capitals ticking underneath like a metronome. Everything else holds still, so the eye has one place to go: the
card.

The card becomes whatever the creator names. They talk in short breaths, jump cut to jump cut, and the instant they say a
word the viewer needs, the card turns into it. "Codec" slams onto a white card in huge condensed capitals, and the real
options appear under it, one per word. "Yahan", and you're inside the actual export panel while an orange box traces
itself round the exact field, then slides to the next one on the next word. The bill, the dropdown, the toggle, the
washed-out upload beside the rich one: the viewer never imagines it, they see it. The word is only the name; the picture is
the lesson. A reel of word cards is a slideshow.

The creator is the teacher at the desk: big in the card for the rule, tucked in the corner while the screen teaches, never
gone for long. People trust a setting when the person they trust is right there, pointing at it.

Nothing decorates. No whooshes, no slides, no zooms between things: every change is a hard cut inside a frame that doesn't
budge, so each cut lands like a fact. Orange is the only colour that speaks, and it only ever says "this one". It moves the
way a good teacher talks: quick through the names, a dark card and a breath for the verdict, and late, on the line that
matters most, the camera leans in.

**The test:** pause on any frame: the card holds the creator or the actual thing they're naming; a word standing in for a
thing the card could show is wrong.

## What this playbook is

You're editing one talking-head take of a creator teaching a term, a setting, a mistake or a difference, and you have the
authority to make it the clearest lesson in their niche: the one people save because it showed them exactly where to
click. This playbook is the style, pulled from four reels of a software-teaching creator (v01 embedded vs separate
subtitles, v02 codec vs format, v03 render settings, v04 the bitrate mistake) and measured frame by frame. Read it all,
every time; take what fits the reel, invent where a moment needs more, and never break the feel above.

**Who it's for and what it needs.** Teachers of things that live somewhere: settings, apps, terms, bills, formats, money
rules, camera options. One talking-head take is enough for a lesson reel (F-A); a walkthrough (F-B) needs their screen
recordings. Their screenshots and recordings make the strongest cards; anything they don't have is the real thing
fetched from the web (a logo, a post, the app's own panel), else built as a generic, unbranded screen (§12). No cut-out: the presenter lives in the card or in a rounded tile. Captions follow the creator's
language (English, Hinglish or Hindi, set in their copy); the title, term cards and chips stay English. Machine values live
in `tokens.json`; where this text gives a number tokens also holds, they agree.

### Style directives (non-negotiable)
| # | Directive | Where it lives |
|---|---|---|
| D1 | **The frame never moves.** Title, card rect, caption slot and credit slot keep their rects (±4 px) for their whole lifetime; only what's inside the card changes | §3.4, §3.7 |
| D2 | **The title promises.** Line 1 names who or what is at stake, line 2 delivers the twist; it reads by 0.8 s and stays for the whole F-A reel | §5.2, §6.5 |
| D3 | **Name it → show it.** When a term, setting, value, number, object or place is spoken, the card shows it within ±5 f: first its name if it needs one, then the thing itself (the screen, the field with the box, the object, the difference). A word card never stands in for something the card could show | §7.3, §8.2, §8.4 |
| D4 | **Hard cuts only.** No whips, flashes, slides or zoom transitions. Card content, layouts, callouts and the credit chip cut on and off. The only camera moves are a few late pushes and pull-outs on the face card (Z-2 / Z-3) | §9, §10.2 |
| D5 | **One accent.** Orange (`primary`) is the only bright hue on the page, plus the small credit chip; there is no good/bad colour axis | §4 |
| D6 | **Captions are a metronome.** Every spoken word is captioned in tracked capitals under the card, 2–4 words at a time, hard-swapped; captions never carry colour or emphasis | §5.3 |
| D7 | **Teach in short breaths.** The creator speaks in 2–4-word bursts; dead air is cut; jump cuts keep the same framing (measured: no re-crop) | §7.5, §10.2 |
| D8 | **The bottom band is empty.** Nothing at all below y 1536 (the original reels leave about 340 px empty; this style keeps 384 px for Instagram's buttons) | §3.6 |

### Quick index
| § | What |
|---|---|
| §1 | Procedure: how to approach a reel in this style |
| §2 | Hard rules: the craft and the style's never-list |
| §3 | Formats, the page and its themes, layouts, the frame template (slots), stage moves, safe zones, the person |
| §4 | Colour system |
| §5 | Type and captions: the title lockup, CS-1 / CS-2 tracked caps, card text |
| §6 | Hook system: stopper test, HA-05 claim lockup (H-1), H-2, H-3, H-4, hook pairs, lockup writing, CTA and the credit chip |
| §7 | Structure and rhythm: the tutorial arc, SM-1, the unit ritual U-1…U-5, open loops, rhythm by feel |
| §8 | Visual system (B-roll and patterns): families, picture first, P-01…P-34, line → pattern lookup, data and truth, the annotation layer, assets |
| §9 | Transition system T-01…T-07 |
| §10 | Motion tokens, camera Z-1…Z-3, layers, finishing |
| §11 | Sound |
| §12 | Footage handling: setups, shots and fallbacks, the presenter tile, inserts |
| §13 | What your plan should settle |
| §14 | Worked examples (3) |
| §15 | Your look at the storyboard: the checklist |
| §16 | Build notes |
| App. A / B | Evidence map / hook-title bank |

---

## §1 Procedure: how to approach a reel in this style

You watch, listen, plan, build and look at the storyboard yourself; the edit skill has the mechanics. This style's
craft is two decisions: what the card turns into on every word that names something, and where exactly, inside a screen,
the orange box lands.

1. **Pick the format and the page.** Mostly "click here, set this, then this" → F-B Screen Walkthrough; one concept, mistake
   or difference explained to camera → F-A Lesson Frame (§3.1). The card mostly shows dark app UI → TH-light; otherwise
   TH-dark (§3.2). One format and one page for the whole reel.
2. **List what the viewer must see.** Go through the words and write down every term, setting, value, number, file name,
   object, place and pointing word ("yahan", "ye dekho", "this one", "from this to this"). Next to each, write the picture:
   the screen it lives in, the field the box lands on, the object on a picture card, the two versions side by side. Only
   then decide which ones also get a name card first. If a line has a thing and your plan shows only its word, go back.
3. **Build the field map** (this style's precision step). For every screenshot and recording: look at its frames, list each
   field the creator names, and write the field's rect **in card coordinates** (for recordings, also the local time and
   scroll position at which it's visible). These rects become the box keyframes (§8.6). A field you can't locate gets a
   chevron (P-17), never a guessed box.
4. **Feel the tone of each line:** `hype` (the claim) · `explain` · `warn` (a mistake, "this is wrong") · `win` (the fixed
   value, the right setting) · `cta`. Explanations want the screen, verdicts want a dark card, rules want the face.
5. **Write the lockup** (§6.5): 8–10 candidates, the best by the stopper test (§6.1), two alternates. Pick the hook (H-1…H-4)
   and its first proof card.
6. **Mark the triggers.** Every card cut 2 f before its word; every jump cut on a word boundary; every pause over 150 ms
   cut.
7. **Plan each unit** (§7.3: name → unpack → show where → rule → number) and the reel's peak: the verdict card, and the one
   late lean-in on the line that matters most.
8. **Third-party moments** (§12.5): list them, then use the creator's file, else fetch the real one from the web (source
   noted); rebuild only what can't be found.
9. **Place the credit chip's two windows** and decide the CTA chip text (§6.7).
10. **Plan the sound** (§11): sparse; the cut is the beat.

---

## §2 Hard rules: the craft and the style's never-list

**Craft, by eye** (judge it on the storyboard, in context, the way an editor does):
- **Keep the person clear.** People come for the teacher, so keep the face, hair and the room above the head clear of
  front layers when the moment is about them (the geometry is in §3.8): callouts on the face card sit on the chest or the
  empty side, about 40 px clear of the head region; the caption band (y 1313–1377) sits 25 px under the card; marks stay
  off the presenter tile; and on **L-insert-hook** cy 1345 would cross the eyes of its face card (y ≈ 1368), so the hook
  hides its captions (`timeline.captions.hide` over it). What's never fine is a head chopped or a face buried by accident.
  Behind the person is fair game, text included (`behind: true`), but this style runs without a cut-out, so in practice
  nothing draws behind them.
- **No text over text.** The lockup, one card text group and the caption are the most a frame holds; never two boxes.
- **On the word.** Term cards, picture cards, box moves, callouts and chips start 2 f before their word and are fully on
  within ±5 f; the highlight box starts tracing about 12 f before its field word (any lead up to 15 f counts as on the word)
  and closes on it. Jump cuts sit on word boundaries ±1 f; caption sync leads by no more than 150 ms.
- **Say what was said.** A number, value or setting the creator says is shown exactly as said. Illustrations (a recreated
  statement, a sample app screen, a made-up file size) may use made-up but realistic numbers and names, with no label
  (`illustrative: true`). A recreated panel is generic and unbranded and never passed off as the creator's own capture.
- **A box only where you looked.** No box on a field the field map doesn't contain; one mark at a time.
- **Promise integrity.** A count in the lockup ("3 settings", "Essential #3") equals the units shown; a question asked in
  the hook is answered on a card; a CTA keyword is on the chip ≥ 1.5 s.
- **Spelling.** English words, tool names, formats and numbers exact ("H.264", "1080 × 1920"); romanised Hinglish follows
  the creator's own spelling and stays consistent inside a reel.
- **Readable.** Captions 44 px under the quiet-type exception E3 (44–53 px, weight ≥ 500, 1 line, ≤ 24 characters,
  contrast ≥ 7:1; white on the black box is 21:1); labels 28–39 px only when the same word is spoken or shown larger
  (`redundant: true`); display text never below 40 px. On-screen text holds ≥ 0.25 s per word (captions ≥ 0.15 s per word),
  titles ≥ 10 f after they finish building.
- **Privacy.** Emails, account numbers and file paths with names are blurred in screenshots and recordings for their whole
  time on screen.
- **Audio.** −14 LUFS integrated, true peak ≤ −1.5 dBTP, the bed 20 dB under the voice, a hard end ≤ 6 f after the last
  word, no black tail over 0.2 s.
- **The bands.** Nothing (no text, no graphic, no presenter) below y 1536, except the face card of L-insert-hook, which
  bleeds to y 1800 with nothing on it.

**Never in this style:**
- A card that only names a thing the card could show. The term card is the name; the screen, the field, the object or the
  difference is the lesson, and it follows.
- Transition effects: whips, flashes, light leaks, glitches, zoom-throughs, slides, morphs between layouts, crossfades.
- Punch or shake presets (snap-punch, crash-zoom, shake, rotation-snap), re-crop alternation on jump cuts.
- Coloured, bold, glowing or enlarged words inside captions; karaoke; emoji in captions or the lockup.
- A second title, banner, slab or sticker. The lockup is the only headline.
- Stock footage, AI scenes, decorative B-roll montages. An aside (P-26 / P-27) is short, in the card, and shows the line.
- A second bright hue beside orange (the chip aside); red/green verdict colours; gradients beyond the hairline.
- Text or graphics in the top 330 px of an F-A frame.
- Readable code, logs or long paragraphs as the point of a card: a screenshot's small text is texture, and the box and the
  caption carry the meaning.
- Memes or other creators' footage as decoration. A logo, app icon or clip appears only when the lesson names it, and then
  it's the real one (§12.5).
- A card change with no spoken trigger (no filler swaps).
- Moving, resizing or fading the card rect itself; any title animation after it settles (f24, 0.8 s).
- An outro card or end card.

---

## §3 Worlds, layouts, stage moves, safe zones

### 3.1 Formats
| ID | Name | When | Layouts | Default hook | What differs |
|---|---|---|---|---|---|
| F-A | Lesson Frame | One concept, mistake, difference or rule explained to camera (most reels) | L-lesson, L-term-pip, L-term-full | H-1 (HA-05 claim lockup) | The title lives from f0 to the last frame |
| F-B | Screen Walkthrough | Step-by-step settings, where-to-click, app walkthroughs | L-insert-hook, L-lesson, L-screen, L-term-pip, L-term-full, L-full | H-3 (HA-02 insert hook) | The title lives for the hook only, at S-title y 812–1026 between the insert and the face card; the presenter may step aside more (the recording carries the lesson); footage matters more |

Both formats share the page, the same 4:3 card rect, the same tracked-caps captions in the same slot, the same highlight
box, the same credit chip and the same empty bottom band. Only the title's lifetime and what mostly fills the card change.
Pick F-B when most of the script is "click here, set this, then this"; otherwise F-A.

### 3.2 The page (the one world) and its themes
| ID | Kind | Look | Carries | Enter / exit |
|---|---|---|---|---|
| **W-page** | `canvas` | TH-dark: `night` `#000000` with a grid of rounded dashes (14 × 7 px, `#121212`, pitch 29.5 × 24.7 px, measured v02), noise 0.02. On pure black the caption's black box is invisible, as in the reference. TH-light: `canvas` `#FBF3F1` with 1 px grid lines `#EDE1DE`, pitch 180. No vignette, no glow | Everything: the frame is printed on it | Present from f0 to the end; the theme never flips inside a reel |

The page shows wherever the stage doesn't: above and below the card, around the presenter tile, behind a dark term card. In
L-full the footage covers it.

| Theme | Page | Lockup, credit arrow and script | When |
|---|---|---|---|
| TH-dark (default) | `#000000`, the dash grid above | `paper` | Concepts, terms, mistakes, differences, opinions: the card mostly shows the face, term cards, picture cards |
| TH-light | `#FBF3F1`, 180 px line grid | `ink` | Walkthroughs whose card shows dark app UI for a good part of the reel (about 40 % or more: export settings, editors, dashboards): the pale page sets off the dark screenshots |

The accent (`primary`) and the chip (`accent`) are the same on both pages.

### 3.3 Layouts
| ID | Engine | The creator | The card (graphic rect) | Caption |
|---|---|---|---|---|
| **L-lesson** | `card` | The card itself: x 72, y 568, 936 × 720, radius 40, crop 4:3, face 0.30, eye 0.40, shadow 0.25 | — (the card is the presenter) | CS-1, cy 1345 |
| **L-term-pip** | `card` | A tile x 700, y 948, 288 × 320, radius 28, face 0.42, eye 0.36, shadow 0.30 | x 72, y 568, 936 × 720 (the term, dialog or picture card fills it) | CS-1, cy 1345 |
| **L-term-full** | `hidden` | none | x 72, y 568, 936 × 720 (a dark term card or a difference card) | CS-1, cy 1345 |
| **L-insert-hook** | `card` | The card moved down: x 72, y 1080, 936 × 720, radius 40, crop 4:3, face 0.30, eye 0.40, shadow 0.25 | The insert x 72, y 150, 936 × 610 | CS-1, cy 1345; **hidden** over the hook (`timeline.captions.hide`) |
| **L-screen** | `card` | A tile x 92, y 968, 300 × 300, radius 28, face 0.42, eye 0.36, shadow 0.30 | x 72, y 568, 936 × 720 (the recording) | CS-1, cy 1345 |
| **L-full** | `full` | Full frame | none | CS-1, cy 1210 (S-caption-full) |

**How the layouts take turns.** F-A lives on L-lesson and cuts to L-term-pip or L-term-full the moment a thing is named,
then back to the face for the rule; a face run lasts as long as the thought, a card as long as there's something on it to
look at. F-B lives on L-screen, one step after another, and comes back to L-lesson or L-full for the rule lines between
them.

### 3.4 The frame template (the slots)
The whole style is this frame. The beat sheet writes only what's in each slot; scenes paint into these rects and nowhere
else.

| Slot | Rect (x, y, w, h) | Radius | z | Lifetime | Holds | Entry (once) | Content swap |
|---|---|---|---|---|---|---|---|
| S-title | F-A: 64, 330, 952, 214. F-B: 64, 812, 952, 214 | 0 | 6 | F-A the whole reel; F-B the hook | the lockup | P-01 build (f2–f24) | none (it never changes) |
| S-insert | 72, 150, 936, 610 | 40 | 3 | the hook (F-B H-3 only) | a 16:9 clip, a phone mock, an icon row, a created scene card | present at f0 | hard, every 0.8–2.0 s |
| S-card | 72, 568, 936, 720 | 40 | 3–4 | the whole reel | face, term card (light, dark, marker), question, picture, difference, dialog, screen, B-roll, reaction | present at f0 (F-B: from the composition cut) | hard (E6), on the trigger word −2 f |
| S-caption | 64, 1313, 952, 64 | 0 | 7 | the whole reel, hidden on L-insert-hook | captions (CS-1 / CS-2) | hard | hard (E6), about every 0.6 s |
| S-credit | 360, 1396, 460, 136 | 0 | 6 | after 5 s, in its two windows | the credit, the CTA chip | P-04 (6 f flicker; hard off) | fade 6 f (credit → CTA text) |
| S-caption-full | 64, 1178, 952, 64 | 0 | 7 | L-full only | captions | hard | hard |
| S-credit-full | 360, 1262, 460, 136 | 0 | 6 | L-full only, inside the credit windows | the credit, the CTA chip | cuts with the layout | — |

- Slot rects stay constant (±4 px) for their lifetime; slots never overlap; the gaps (25 px card → caption, 19 px caption →
  credit) are fixed. The presenter tile is part of S-card's content and sits only at its layout's tile rect.
- Swaps inside S-card and S-caption are hard: mark each card scene's container `data-slot` and declare `exception: "E6"`.
- The lockup counts as one text element for the whole reel; with the caption and one card text group, a frame holds three
  (the small credit chip isn't counted).

### 3.5 Stage moves (all cuts)
| ID | Move | Recipe | Use |
|---|---|---|---|
| **G-1** | Card content cut | `stage.via: cut` between L-lesson and L-term-pip / L-term-full / L-screen on the trigger word (−2 f). The S-card rect is identical before and after; only its content changes | Every term, thing, field or step |
| **G-2** | Composition cut | F-B only: at the end of H-3, one hard cut from L-insert-hook (insert + lockup + face card) to L-screen or L-lesson; the insert and the lockup end on that frame and the captions start on it | Hook → body in F-B |
| **G-3** | Full-bleed cut | F-B only: `via: cut` L-lesson ↔ L-full; the caption moves to S-caption-full, the credit to S-credit-full | A personal aside or a rule line said with energy (v01) |
| **G-4** | Jump cut | A cutmap jump cut at the same framing (Z-1, §10.2); callouts cut on or off with it | Every breath inside L-lesson and L-full |
| **G-5** | Tile hold | The presenter tile stays at its rect while term, picture and dialog cards swap above it (no tile move between consecutive L-term-pip beats) | Consecutive cards |

Never `panel-drop`, `pop-back`, `shrink-to-card`, `grow-from-card`, `slide-*`, `pip-*`, `morph`, `dim` or `fade-through`.

### 3.6 Layout diagrams and safe zones
**L-lesson (F-A, most of the reel)**
```
┌──────────────────────────────┐ 0
│        (empty page)          │ ← y 0-330: nothing (IG top UI + air)
│      95% Creators            │ ← line 1 cy 378, Inter Tight 800 86 px
│  don't know this difference  │ ← line 2 cy 466, EB Garamond italic 72 px
│   ───────═══════───────      │ ← hairline y 518, x 170-900
│ ╭──────────────────────────╮ │ ← S-card y 568
│ │                          │ │
│ │   presenter (4:3 crop)   │ │   x 72-1008, radius 40
│ │   head top y 610-720     │ │   eyes y ≈ 856
│ ╰──────────────────────────╯ │ ← y 1288
│      KOI BHI SOFTWARE        │ ← S-caption y 1313-1377, cy 1345 (44 px caps, +0.10 em)
│   ↖ lessons by               │ ← S-credit y 1396-1532 (windows only)
│        [ @yourhandle ]       │
│        (empty band)          │ ← y 1536-1920: nothing
└──────────────────────────────┘ 1920
```
**L-term-pip (term, picture or dialog card with the presenter tile)**
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
**L-insert-hook (F-B hook)**
```
│ ╭──────────────────────────╮ │ y 150   S-insert: 16:9 clip or phone mock (P-23 / P-24)
│ │        insert            │ │
│ ╰──────────────────────────╯ │ y 760
│   Best Export Settings       │ ← line 1 cy 862
│     for Instagram reels      │ ← line 2 cy 948, hairline y 1000 (S-title ends y 1026)
│ ╭──────────────────────────╮ │ y 1080  face card 936 × 720, eyes y ≈ 1368
│ │        presenter         │ │         NO caption on this layout (cy 1345 would cross the eyes)
│ ╰──────────────────────────╯ │ y 1800  (bleeds into the bottom band: presenter only, no text)
```
**L-screen (F-B steps)**
```
│        (empty page, no title)│ y 0-568
│ ╭──────────────────────────╮ │ y 568   the recording, cropped to the panel (P-19 / P-20)
│ │  Format  [ MP4      v ]  │ │ ← orange box on the named field (P-16)
│ │╭──────╮ Codec [H.264  v] │ │
│ ││ tile │                  │ │ ← presenter tile x 92-392, y 968-1268
│ ╰┴──────┴──────────────────╯ │ y 1288
│        FORMAT MP4 RAKHO      │ ← caption cy 1345 (the box shows on TH-light)
```
**L-full (F-B asides)**
```
│ full-bleed presenter         │ ← head top y 150-330
│                              │
│     [ AB TUM LOG JAB BHI ]   │ ← S-caption-full y 1178-1242, cy 1210, black box
│   ↖ lessons by [@handle]     │ ← S-credit-full y 1262-1398
│                              │
```

| Band | y | Content |
|---|---|---|
| Top empty | 0–330 | Nothing in F-A (in F-B the insert may start at y 150 during the hook only) |
| Title | 330–544 | S-title (F-A, its rect 64, 330, 952, 214); empty in F-B after the hook |
| Card | 568–1288 | S-card |
| Caption | 1313–1377 | S-caption (cy 1345) |
| Credit | 1396–1532 | S-credit, in its windows; empty otherwise |
| Bottom empty | 1536–1920 | Nothing |

Meaning text stays inside x 64–1016 and y 330–1536 (y 140–1536 on L-full and during the F-B hook). The right button column
(x > 970, y 900–1540) only ever holds the card's right edge (x 1008) and the presenter tile, never text.

### 3.7 Why the frame holds still
The stillness is the style. Because the title, the card edge, the caption line and the credit slot never move, every hard
cut inside the card reads as new information, and the viewer's eye never has to search. Never animate the frame to add
energy; add it inside the card, with the next picture.

### 3.8 The person
- **The face is never gone for long.** In the card, in the tile, or full frame in F-B asides; the only absences are a dark
  term card, a difference card or an aside, and none lasts more than 3.0 s. Screen and picture cards always carry the tile.
- **The card crop (L-lesson):** head top at y 610–720 (setup A frames for it), face 0.30 of the card's height, eyes at 0.40
  (y ≈ 856). The card clips the head; there's no breakout, so nothing reaches above the card's top edge at y 568, and the
  lockup's hairline (y 518) sits 50 px above it. Callouts stay on the chest or the empty side, 40 px clear of the face, the
  hair and the room above the head.
- **The tile (L-term-pip x 700–988, y 948–1268; L-screen x 92–392, y 968–1268):** face 0.42 of the tile, eye 0.36, the head
  top 10–30 px below the tile's top edge. Variant chips (row y 880) end above the tile; boxes, chevrons and cursors finish
  before they would reach it.
- **The hook card (L-insert-hook):** the same 4:3 crop moved to y 1080–1800; eyes at y ≈ 1368; no captions, no text, no
  credit on it; the lockup above ends at y 1026.
- **Full frame (L-full):** head top at y 150–330, never under the caption box (y 1178–1242) or the credit (y 1262–1398),
  which sit on the chest.
- **Returns** are always hard cuts back to L-lesson (or L-full in F-B). The creator never slides, shrinks or grows.

---

## §4 Colour system

### 4.1 Role palette
| Role | Hex | One job | Text on it | Contrast |
|---|---|---|---|---|
| `primary` orange | `#F59E0B` | "This one": the title hairline, the highlight box on dark UI, the state line of a dark term card | `ink` | 8.9:1 |
| `accent` chip green | `#1E7A3A` | The credit chip fill, and nothing else | `paper` | 5.4:1 |
| `ink` | `#0F0F0F` | Text on white cards and on the light page | — | — |
| `paper` | `#FFFFFF` | The lockup on the dark page, caption text, white term and picture cards | — | — |
| `night` | `#000000` | The TH-dark page | — | paper 20:1 |
| `canvas` | `#FBF3F1` | The TH-light page | — | ink 18:1 |
| `grid` | `#1C1C1C` (role; the TH-dark dashes are `#121212`) / `#EDE1DE` (light lines) | Page texture | — | — |
| `charcoal` | `#2A2A2E` | The dark term card fill | `paper` / `primary` | 14:1 / 6.7:1 |
| `termink` | `#2B2B2E` | The term word and pill text on white | — | 14:1 on white, 8.2:1 on the pill |
| `mute` | `#6B6B70` | The second tone of a variant chip ("Apple **Pro Res**"); the hairline between the halves of a difference card | — | 5.3:1 on white |
| `pill` | `#E4E4E7` | The Essential #N pill fill | `termink` | 8.2:1 |

Gradient: `hairline` only (transparent → `#E08A1E` → `#F5B04A` → `#E08A1E` → transparent, left to right). `primary` and
`accent` take the creator's brand colours when they give them (contrast-nudged against `ink` and `paper`); every other role
stays.

### 4.2 Meanings
- **Orange = "this one":** the field being named, the state that matters ("AUTOMATIC"), the line under the claim, the one
  detail that differs. It's the viewer's finger.
- **The chip colour = the creator's mark:** the handle, the keyword; nothing else uses it.
- **White card = the name or the thing; charcoal card = the verdict or an announcement** ("THIS IS WRONG", "FORMAT").
- There is no bad/good axis and no colour for comparisons: comparisons are made by sequence and position (P-30), by showing
  both versions (P-34) and by where the orange lands, never by red vs green.
- Tools' brand colours appear only inside the creator's own screenshots and recordings.

### 4.3 Rules
- Two bright hues per frame at most: `primary` and the chip's `accent`.
- Coloured text exists only as the first line of a dark term card (orange on charcoal, 6.7:1) and the chip label.
- The highlight box is `primary` (orange) on TH-dark and `paper` (white) on TH-light, always over dark UI (v02 orange, v03
  white); over a light UI (a white settings sheet, a white statement) it's `ink` on both pages.
- On TH-light the caption's black box shows as a box, which is intended (v03).
- Footage is never graded (match only exposure and white balance between takes); screenshots are never recoloured.

---

## §5 Type and captions

### 5.1 Font map
| Slot | Family | Weight / style | Used for |
|---|---|---|---|
| `display` | **Inter Tight** | 800, tracking −0.02 em | Lockup line 1 |
| `serif` | **EB Garamond** | 500 italic | Lockup line 2 |
| `body` | **Space Grotesk** | 500, ALL CAPS, +0.10 em | Captions |
| `numeric` | **Anton** | 400 | Term words, picture-card names, number and keyword callouts, dark term cards |
| `ui` | **Inter Tight** | 500–700 | Variant chips, question cards, the Essential pill, the credit chip |
| `marker` | **Permanent Marker** | 400 | The brush term word (P-09) |
| `script` | **Caveat** | 400 | The credit script line ("lessons by") |
| `deva` | **Noto Sans Devanagari** | 600 | Captions when the caption script is Devanagari (CS-2) |

All bundled. The original reels used Inter, a Newsreader-like italic, a squarer tech sans for the captions, a Bebas-like
condensed and a thin handwriting; these are the closest bundled faces.

### 5.2 The title lockup (the headline element)
| Property | Recipe |
|---|---|
| Kind / lifetime | `lockup`; F-A the whole reel (f0 → the last frame); F-B the hook (it ends with G-2). The scene declares `kind: "lockup"` and `text_content` = both lines |
| Line 1 | Inter Tight 800, **86 px**, tracking −0.02 em, centred, cy **378**; `paper` on TH-dark, `ink` on TH-light; 2–4 words, Title Case, may start with a number ("95% Editors") |
| Line 2 | EB Garamond italic 500, **72 px**, centred, cy **466**; the same colour as line 1; 3–5 words, sentence case |
| Hairline | y **518** (measured 514–521), x 170–900 (measured 175–892), 3 px core + 8 px glow (the `hairline` gradient, `primary` glow at 60 %), fading to transparent at both ends |
| Box | none: no fill, no stroke, no shadow, no rotation |
| F-B position | line 1 cy 862, line 2 cy 948, hairline y 1000 (S-title y 812–1026) |
| Frame 0 | f0: nothing of the lockup yet (the face card and the first caption are already up). **f2–3 (0.08 s):** line 2 reveals **left to right** as a soft-edged wipe (≈ 60 px feather) with blur 8 → 0 px, over 6 f (expo-out); the hairline draws left to right with it, 6 f (v02 @ 0.12–0.25 s, full-rate strip). **f11–12 (0.38 s):** line 1 reveals left to right **character by character** (≈ 1 f per character), each character blur 8 → 0 and grey → white over 4 f; the first word is legible by f14. **f22–24 (0.75–0.8 s):** settled and fully readable (v02 @ 0.72 s). The F-B H-3 hook may start line 1 at f0 (v03) |
| Life | None after f24: no pulse, no flip, no underline wipe, no colour change |
| Exit | F-A: none. F-B: a hard cut with the hook composition (G-2) |
| Shape | 2 lines exactly, ≤ 9 words (line 1 2–4, line 2 3–5), ≤ 26 characters per line, English, reads in ≤ 1.2 s; no emoji, no chips, no CAPS words except acronyms |

### 5.3 The captions: tracked caps, a metronome
**CS-1 (default, Latin script)**, `extends: lib:editing_explained`:

| Group | Value |
|---|---|
| Mode | `full`, `support`, `mute_safe`: every word captioned, serving the card, never carrying emphasis |
| Chunking | `group`, 2–4 words (mean ≈ 2.8), 1 line, ≤ 24 characters; never split a name, number or unit ("1080 X 1920", "H.264"); a pause ≥ 0.6 s always breaks; sentence ends break; punctuation stripped |
| Timing | Lead 1 f; min hold 0.15 s per word (a chunk lives ≈ 0.4–0.9 s, ≈ 0.6 s typical); swap **hard** (E6, 0 f); in a pause the last chunk holds ≤ 0.4 s, then hides. After a card cut the caption swaps 1 f later |
| Skin | Space Grotesk 500, **44 px** (E3; measured cap height 28–31 px; the original face is a squarer tech sans, Saira/Exo-like; word gaps visibly wide, about 2 spaces), **ALL CAPS**, tracking **+0.10 em**, `#FFFFFF`, no stroke, no shadow, line height 1.1; container **box**: `#000000` 100 %, radius 0, padding 6 / 14 px (invisible on the dark page, a visible black box on TH-light and over L-full footage) |
| Position | `fixed_y` cy **1345** (S-caption y 1313–1377) in L-lesson, L-term-pip, L-term-full and L-screen; cy **1210** (S-caption-full y 1178–1242) in L-full; **hidden on L-insert-hook** (`timeline.captions.hide` over the hook: the face card's eyes sit at y ≈ 1368); centred, max width 952; `avoid_face` on |
| Emphasis | **none**: no colour, weight or size change on any word |
| Hide | On L-insert-hook (the whole F-B hook, until the composition cut); under transitions and z8 scenes (none planned). **Not** hidden under a dark term card even when it repeats the words (v04 @ 0:37.0: the "THIS IS WRONG" card with the same caption) |
| Language | The creator's language in Latin script: English, or romanised Hinglish as in the reference reels; English words kept as spoken ("CODEC H.264", "FRAME REORDERING AAPNE"); the creator's romanisation, consistent within the reel; numbers as digits without grouping ("50000 KBPS"); glossary terms exact; profanity masked inside the word (S**T) |

**CS-2 (Devanagari)**, chosen when the captions are Hindi in Devanagari: identical except Noto Sans Devanagari 600, **50 px**,
case as spoken (Devanagari has no capitals), tracking 0, line height 1.25. English terms stay in Latin script inside the
chunk. Same positions, same hide on L-insert-hook.

Measured on the reference reels: a hard swap about every 0.62 s (v02: 74 swaps in 46 s); 44 px measured at v02 @ 0:01.5
("USE KARTE HO", caps y 1328–1359).

### 5.4 Card text
| Element | Recipe | Hold |
|---|---|---|
| Term word (white card) | Anton 150–190 px (170 default), `termink`, soft shadow 0 10 18 rgba(0,0,0,.28), centred at card x 540, cy 720 (or cy 640 when a pill or strip sits under it); 1 word or 1 token (".MOV", "H.264"); ≤ 9 characters at 190 px, ≤ 12 at 150 px | the card's span (≥ 1.0 s) |
| Dark term card text | Anton 140–180 px, 1–3 words on ≤ 2 lines, centred at the card centre (540, 928); line 1 `primary` when it names the state ("AUTOMATIC"), line 2 `paper` ("HOTA HAI"); or both `paper` ("THIS IS / WRONG"); text shadow 0 6 16 rgba(0,0,0,.5) | 0.8–1.5 s |
| Brush term word | Permanent Marker 140–160 px, `ink`, left-aligned at x 112, cy 690 | the card's span |
| Picture-card name (P-33) | Anton 72 px, `termink`, right-aligned at x 968, cy 660; ≤ 8 characters; only when the name isn't obvious from the picture | the card's span |
| Difference labels (P-34) | Anton 72 px, `termink`, centred over each half (cx 314 and 766, cy 630) | the card's span |
| Variant chips | Inter Tight 500, 56 px, `ink`, plain text (no pill), a row at y 880, starting x 148, 48 px gaps; a two-tone chip writes the family in `ink` and the variant in `mute` ("Apple **Pro Res**") | until the card leaves |
| Question card | Inter Tight 600, 78 px, line height 1.0, `ink`, 2 lines, centred at x 540, top y 690 | 1.0–2.0 s |
| Essential pill (SM-1) | Inter Tight 600 italic, 40 px, `termink` on `pill`, radius 26, padding 6 / 22, at x 112, y 600 | the card's span |
| Number on card | Anton 190 px (170–210), `paper`, shadow 0 6 20 rgba(0,0,0,.45), number + unit glued ("50,000KB/S"), centred, baseline y 1252 (36 px above the card's bottom) | ≥ 0.8 s, to the end of the phrase |
| Number beside the head | Anton 64 px number + Anton 44 px note under it ("BHI NI CHAHIYE"), `paper`, its right edge 36 px inside the card on the side away from the face | ≥ 0.8 s |
| Keyword on card | Anton 110–140 px, `paper`, shadow as above, baseline y 1252 | ≥ 0.8 s |
| Credit script | Caveat 34 px, `paper` (TH-dark) / `ink` (TH-light), baseline y 1468, starting x 452 | its window |
| Credit chip | Inter Tight 700, 28 px, `paper` on `accent`, radius 6, padding 4 / 14, top-left at x 560, y 1486 | its window |

### 5.5 Language and numbers
- **Captions** follow the creator's speech (§5.3). **The lockup, term cards, picture names, chips and question cards are
  English** (Title Case line 1; sentence case line 2 and questions; ALL CAPS term words). A Hinglish card is allowed only for
  a spoken verdict ("HOTA HAI", "BHI NI CHAHIYE").
- **Numbers:** callouts use international grouping and glue the unit ("50,000KB/S", "1080 × 1920", "30 FPS"); captions keep
  digits ungrouped as spoken ("50000 KBPS"). English copies use `$` and K/M/B; Hinglish and Hindi copies use `₹` with Indian
  grouping and lakh/crore ("₹1,20,000"). Units are metric.
- **Devanagari (CS-2):** no ALL CAPS, no tracking; Latin terms stay Latin.

---

## §6 Hook system

**The hook title** promises the viewer something: an outcome they want, a curiosity gap, or who it's for ("How to go viral
as a doctor creating content", never the label "Reels for Doctors"). It needn't repeat the spoken words; it must be true to
what the reel delivers. In this style the title is the two-line lockup: line 1 names who or what is at stake, line 2 lands
the twist, and read together they're one sentence the viewer feels caught by ("95% Creators / don't know this
difference"). Its shape is fixed (§5.2); its voice is yours to make irresistible.

This style doesn't open on a result or a fight. The stopper is the claim itself, read in a quiet, premium frame while the
creator is already mid-sentence and gesturing at the lens, and then paid off by a card that shows the thing within three
seconds.

### 6.1 The stopper test
1. **Thumbnail:** the frame at 0.8 s at 25 % scale shows the claim (lockup line 1 is 21.5 px at that scale) and the face
   card.
2. **Mute:** the first 3 s tell the story: the lockup states the claim, the captions carry the spoken question, and the
   first card proves it by 3.0 s.
3. **Motion at f0:** live talking-head footage in the card at f0 (and the insert already playing in H-3).
4. **One read:** the lockup reads in ≤ 1.2 s and is complete by 0.8 s.
5. **Payoff:** the lockup reads by 0.8 s (always by 0.9 s); the first proof card (a picture, a term card with its thing, a
   dialog card, a screen card or a callout) lands by 3.0 s.

The opening feels quiet and certain: the title writes itself, the captions tick, a jump cut or two on the creator's
breaths, and then the first hard cut into the card, on the first word that names something.

### 6.2 HA-05 Claim lockup, hook H-1 (default, F-A)
Spoken pattern: a direct address that sets up the claim, mid-sentence from f0 ("Chahe tum koi bhi software use karte ho,
tumne hamesha dekha hoga…"). The lockup states the stake; the first card lands on the first term (v02).

| t | Visual | Caption (CS-1) | Layout / camera | Sound |
|---|---|---|---|---|
| **f0** | The dark page; the face card (L-lesson) already playing, the creator mid-word, looking at the lens; no lockup yet | the first chunk already on ("CHAHE TUM") | L-lesson, crop 1.00 | — |
| 0.08 (f2–3) | Lockup line 2 wipes in left to right with blur (6 f); the hairline draws with it | (same) | — | — |
| 0.38 (f11–12) | Line 1 reveals character by character (≈ 1 f each) | — | — | — |
| 0.50 | The second chunk; a natural gesture toward the lens (an OK sign, a point) | "KOI BHI SOFTWARE" | — | — |
| 0.8 (f24) | The lockup settles | — | — | — |
| 1.0–1.6 | A jump cut on the next breath (same framing); the caption swaps 1 f after the cut | "USE KARTE HO" | Z-1 jump cut | — |
| 1.6–2.7 | The creator points down toward the card or looks down; a jump cut | "TUMNE HAMESHA" → "DEKHA HOGA" | Z-1 jump cut | — |
| **2.7–3.0** | **The first card:** a hard cut (G-1) to the white term card with the term word ("CODEC"), the presenter tile bottom-right | the term alone ("CODEC") | L-term-pip via cut | a reveal (the card) |
| 3.0–9.0 | The real variants pop one per spoken word (P-07), then the thing itself: the export dialog (P-15) with the box tracing onto Codec | "H.264" → "H.265" → … | — | reveals on the landings |

### 6.3 Alternate hooks
**H-2 Question lockup (HA-05 variant)** (v04): the creator asks the viewer a direct question; the lockup names the mistake;
the answer lands as a marker term card with the actual setting under it.

| t | Visual | Caption | Layout / camera |
|---|---|---|---|
| f0 | The face card, the creator glancing down, mid-word | "MERA EK" | L-lesson 1.00 |
| 0.17–0.67 | The lockup builds (line 2 first) | "QUESTION HAI" → "TUM LOGON SE" | — |
| 1.2 | A jump cut (same framing); an index finger points at the lens (the gesture fills the card) | "MUJHE HONEST ANSWER KARNA" | Z-1 jump cut |
| 2.17 | A jump cut | "SEARCH NA KARNA" | Z-1 |
| 2.83 | The last breath of the question | "GOOGLE PE" | — |
| **3.0** | **The answer card:** white, the Essential pill ("Essential #3"), the brush term word ("Bit Rate"), a strip of the settings panel with the orange box drawing on the field (P-09) | the next chunk | L-term-pip via cut |

For example, in money: "Mera ek question hai… credit card ka bill aata hai toh tum kitna pay karte ho?" → the answer card
"Essential #1 / Minimum Due" with a strip of the bill and the box on "Minimum Amount Due".

**H-3 Insert hook (HA-02 Headline + proof), the default for F-B** (v03, v01): the proof plays before a word is said.

| t | Visual | Caption | Layout / camera |
|---|---|---|---|
| **f0** | L-insert-hook: the insert already playing in S-insert (a 16:9 clip of the creator's result, or a phone mock looping their own reel or app screen, P-23 / P-24); the face card below; lockup line 1 starting between them | hidden (`timeline.captions.hide` over the hook) | L-insert-hook |
| 0.17–0.67 | Lockup line 2 + hairline in; line 1 complete | hidden | — |
| 0.8–1.0 | The insert swaps hard to its second clip or screen | hidden | — |
| 1.6–1.9 | The insert swaps again (the third screen: the app's export screen) | hidden | — |
| **2.7–4.3** | **Composition cut (G-2):** the insert and the lockup end; the reel continues in L-screen (the first step) or L-lesson; captions start on this frame | the first chunk | L-screen / L-lesson via cut |

For example: the phone mock plays the creator's own reel, then their editor's export screen, then the upload screen; the
lockup reads "Best Export Settings / for Instagram reels".

**H-4 Term first (HA-04 Topic build):** the term card is already in the card at f0, the presenter tile in its corner; for
when the term itself is the hook ("HDR", "CIBIL"). Built from the term-card timing of v02 @ 0:02.8 and v04 @ 0:03, moved to
f0.

| t | Visual | Caption | Layout |
|---|---|---|---|
| f0 | The white term card with the term word settled, the presenter tile talking | the first chunk | L-term-pip |
| 0.17–0.67 | The lockup builds | — | — |
| 0.9–1.8 | One or two variant chips pop on their words | — | — |
| 1.8–2.4 | A hard cut to the face card (L-lesson) for the claim line | — | L-lesson via cut |
| 2.4–3.0 | A jump cut on the next breath | — | Z-1 |

For example: "HDR" at f0, the chips "10-bit" and "HLG" on their words.

### 6.4 Hook pairs by topic
The pair is **claim → proof in the card**: the lockup makes the claim, and the first card shows the thing that proves it.
When the topic is new, build the pair the same way, and make the proof a picture wherever there's one to show.

| Topic | Claim (lockup) | Proof in the card | By |
|---|---|---|---|
| Credit-card minimum due | "This Mistake is / costing you interest" | P-09: "Essential #1" + brush "Minimum Due" + a strip of the creator's own bill screenshot with the box on "Minimum Amount Due" | 3.0 s |
| SIP vs lump sum | "90% Investors / mix up these two" | P-06 "SIP" with chips "monthly" and "auto-debit", then P-06 "LUMP SUM" | 2.8 s |
| UPI Lite | "Your UPI App / has a hidden mode" | P-06 "UPI LITE", chips "no PIN" and "small payments", then the app screen with the box on the toggle | 2.8 s |
| Export settings for reels | "Best Export Settings / for Instagram reels" | H-3: a phone insert of the creator's reel → L-screen with the box on "Resolution" | f0 / 2.7 s |
| HDR vs SDR | "95% Creators / don't know this difference" | P-06 "HDR" with chips "10-bit" and "HLG"; later P-06 "SDR" | 2.8 s |
| Shooting reels in 4K | "Stop Shooting 4K / for your reels" | P-08 dark card "4K ≠ / BETTER", then the camera-settings screenshot with the box on "1080p · 30" | 2.9 s |

### 6.5 Lockup writing
**Formula:** line 1 = **the stake** (who or what, 2–4 words, Title Case: a share of people "95% Editors", a superlative "Best
Render Settings", a gate "Only Pro Editors", "This Mistake is") + line 2 = **the twist** (3–5 words, sentence case: what they
don't know or what it does: "don't know this difference", "ruining your video", "use this kind of subtitle", "for social
media"). Read together, the two lines are one sentence.

| Template | Line 1 | Line 2 |
|---|---|---|
| Most people | "[N]% [People]" | "don't know this difference" |
| Mistake | "This Mistake is" | "ruining your [thing]" |
| Gate | "Only Pro [People]" | "use this kind of [thing]" |
| Best | "Best [Thing] Settings" | "for [platform / use]" |
| Hidden | "Your [Tool]" | "has a hidden [feature]" |
| Stop | "Stop [doing X]" | "for your [goal]" |

- English always, even when the speech and captions are Hinglish.
- No emoji, no chips, no CAPS words (acronyms excepted), no exclamation or question marks.
- A number in line 1 is true or clearly the creator's own spoken estimate ("95%" only if they say it).
- Write 8–10, pick by the stopper test, keep two alternates. Never: vague hype ("Game changer", "Mind-blowing"), a claim the
  reel doesn't prove, more than 9 words.

### 6.6 Hook sound
At most one cue in the hook, on its first card reveal (H-1, H-2, H-4) or on the composition cut (H-3). No cue at f0. The bed
enters after the hook, on the first unit.

### 6.7 CTA, the credit chip and the sponsor chip
The style's only furniture besides the title is a small credit unit under the caption: a hand-drawn arrow pointing up at
the caption, a handwritten line and a little green chip. It's the creator's mark, shown in two windows, and at the end it
becomes the call to action. No CTA graphic ever enters the card, and there's no end card.

| Device | Spoken pattern | On screen (the credit unit in its last window) | Hold | Where |
|---|---|---|---|---|
| `none` (default) | none | script "lessons by" + the chip = the creator's handle, in both windows | its windows | early + end |
| `follow_save_stack` | "Aise aur lessons ke liye follow kar lo" (the last sentence) | script "follow for more" + the chip = the handle | ≥ 1.5 s, to the end | end |
| `comment_keyword` | "Comment karo KEYWORD, main bhej dunga" | script "comment" + the chip = the keyword (P-31) | ≥ 1.5 s, to the end | end |
| `link_bio` | "Poori guide link in bio" | script "full guide" + the chip "link in bio" | ≥ 1.5 s | end |

| Element | Recipe | When |
|---|---|---|
| **Credit unit** (P-04) | A hand-drawn arrow (2.5 px, `paper` / `ink`, 70 px, from (440, 1440) up-left to (390, 1404), pointing at the caption) + the script line (Caveat 34 px, baseline y 1468, starting x 452) + the chip (Inter Tight 700 28 px, `paper` on `accent`, radius 6, padding 4 / 14, at x 560, y 1486); on TH-light the arrow and script are `ink` | W1 and W2 |
| **CTA chip** (P-31) | The same unit; the script line and the chip text change with a 6 f fade on the CTA sentence | W2, from the CTA sentence to the end (≥ 1.5 s) |
| **Sponsor chip** | Only when a reel is sponsored: the chip reads the sponsor's name set in type, the script line reads "in partnership with", and a "Paid partnership" line (24 px) sits 12 px under the chip for ≥ 2 s | W1 (replaces the credit) |

**The windows.** W1 opens on the first sentence boundary near 5 s and closes near 14 s (tokens: 5–14 s); W2 covers the last
11 s. Between them the slot is empty (every reference reel hides it mid-video), and it never shows during the hook. In L-full
the unit moves to S-credit-full. The last 1.0 s before the CTA sentence carries no cue.

---

## §7 Structure and rhythm

### 7.1 Structure: a tutorial
- **F-A:** the claim (lockup + hook) → term 1 (name it → show it → where it lives → the rule) → term 2 … (one to four terms)
  → the verdict or the rule → (the CTA line).
- **F-B:** the insert hook → step 1 … step N (each: name the field → the box on it → say the value) → the closing rule on the
  face card → (the CTA line).

### 7.2 Markers
- **SM-1 Essential pill:** "Essential #N" (Inter Tight 600 italic 40 px, `termink` on `pill`, radius 26) at the top-left of
  the term card (x 112, y 600), only when the reel is part of a numbered set of essentials or the lockup promises a count.
  Numbering ascends. When the reel teaches one idea, the markers are spoken only.
- F-B steps aren't numbered on screen; the caption and the box carry the step.
- No recap card, no teaser chips.

### 7.3 The unit ritual (every term in F-A, every step in F-B)
| Step | Frames | What |
|---|---|---|
| **U-1 Name** | the trigger −2 f | A hard cut (G-1) to the name: a white term card (P-06) for a definition, a marker card (P-09) for the essential, a dark card (P-08) for a verdict or an announcement, a question card (P-11) for a turn. The caption shows the term alone when it's spoken alone. When the thing can be shown straight away (an object, a screen), skip the name and cut to the picture (P-33) |
| **U-2 Unpack** | +8 f → the card's end | Variant chips pop one per spoken variant (P-07), each on its word, never closer than 18 f; only the variants they actually name, and a long list belongs on a second card |
| **U-3 Show it, show where** | the field word −2 f (the box: about −12 f) | Cut to the thing itself: the dialog card (P-15), the screen card (P-19), the picture card (P-33) or the difference card (P-34); the highlight box traces onto the field (14–16 f) and slides to each next field on its word (7 f) |
| **U-4 Rule** | the rule line | Cut back to the face card (L-lesson); jump cuts on the breaths; a late rule or verdict line may carry a Z-2 push or a Z-3 pull-out |
| **U-5 Number** | the number word −2 f | A number or keyword callout on the face card (P-12 / P-13 / P-14), cut on with a jump cut (no animation), off on the next cut, held ≥ 0.8 s |

U-2 and U-5 come only when the speech has variants and numbers. U-3 is the heart of the unit: a unit that names a thing and
never shows it isn't finished. The ritual is the one place repetition is the point: the viewer learns it and leans forward
for the next "show where".

### 7.4 Open loops
- **The question loop (H-2):** a question in the first 3 s is answered by the next card, by 3.0 s.
- **The count loop:** a lockup or spoken count ("3 settings") is paid by that many units; the Essential pill numbers them.
- **The deliverable loop:** only with `comment_keyword`.
- These reels are short, so there are no separate re-hooks: each new card is the re-hook, and the hook is over in a few
  seconds so the first unit arrives while the claim is fresh.

### 7.5 Rhythm by feel
- **Calm on the surface, quick underneath.** The frame never moves, the delivery is steady, but the card changes the instant
  a thing is named and the caption ticks every half-second or so. That contrast is the energy: a still frame with fast,
  purposeful changes inside it.
- **It follows the speech.** The creator talks in short bursts and the dead air is cut, so jump cuts land on the breaths;
  names come fast and get their card on the word; the verdict gets a breath and a dark card; the rule gets the face.
- **Show, then come back.** A card holds as long as there's something on it to look at (the chips arriving, the box moving
  field to field); when it has nothing new to give, cut back to the face. A face run lasts as long as the thought.
- **The energy curve:** the claim (quiet, certain) → the units at an even, confident pace, each a little proof → the verdict,
  the reel's peak (a dark card, and late in the reel the slow push on the line that matters most) → a calm last line on the
  face card → the CTA on the chip.
- **No entertainment beats** by default. With comedy `light`, a single reaction (P-27) can land where it's earned, never in
  the hook or the last 3 s.
- For reference, measured on the four reels (a description, not a target): a caption swap about every 0.62 s; jump cuts
  every 1–3 s at the same framing; the longest talking stretch with no cut, card or callout 3.4 s (v04 @ 0:21.5–0:24.8);
  the face on screen 62–80 % of the F-A-type reels and 15 % of v03, where the recording carried the reel; camera moves only
  in v02's back half (a push, a small push, a pull-out, a push); durations 32.5–47.2 s.

---

## §8 Visual system: B-roll and patterns

The card carries the lesson. Whenever the creator names something, the card shows it, and the most useful thing it can show
is the thing itself: the real screen with the box on the field, the bill with the due line, the dropdown landing on the
value, the two versions side by side. Term cards give a thing its name; they're never the whole lesson.

### 8.1 Families
| ID | Family | Source | What the creator supplies |
|---|---|---|---|
| B-1 | Frame furniture (the lockup, the hairline, the credit chip) | built | their handle, the CTA |
| B-2 | The presenter card and tile | the creator | the talking-head take (SH-1) |
| B-3 | Term cards (light, dark, marker, question, chips, pill) | built | nothing |
| B-4 | Callouts on the face card (number, keyword) | built | nothing |
| B-5 | Dialog cards (a screenshot + the box) | the creator's screenshots; else the real panel from the web; else a recreated panel (FB-3) | screenshots (SH-3) |
| B-6 | Screen cards (a recording + the box) | the creator's recordings; else the real panel from the web; else a recreated panel (FB-2) | recordings (SH-2) |
| B-7 | Ink (the highlight box, the chevron, the cursor) | built | nothing |
| B-8 | Hook inserts (a clip, a phone mock, an icon row) | the creator; anything third-party is the real one fetched from the web, else rebuilt | SH-4 (optional) |
| B-9 | Asides (their own B-roll, a reaction clip) | the creator; a reaction fetched from the web; else rebuilt | SH-5 (optional) |
| B-10 | Picture and difference cards (the thing itself, built) | built: recreated generic screens, devices, documents, line-art objects; or the creator's own photo | optional: their screenshots or photos |

### 8.2 Picture first
- **Every unit shows something.** For each thing named, decide what the viewer sees: the creator's capture first, a
  recreated screen or object (P-33) when they have none, both versions side by side (P-34) when the point is a difference.
- **Pointing words get a place.** "Yahan", "ye dekho", "this one", "from this to this": the box lands on the place they
  mean, on the word, and moves when they move on.
- **Illustrations are welcome.** A recreated statement with a realistic amount, a sample upload looking washed out, an app
  screen with made-up rows: no label. A value the creator says is shown exactly as said.
- **Numbers live where they live.** A spoken value goes on its field (P-16 on the dropdown, the amount on the statement) or
  lands as a big Anton callout on the face card (P-12). This style draws no charts, bars or crowds of icons.
- **Variety comes from the lesson**, never from a quota: the unit ritual is the deliberate repeat, and inside it the pictures
  change because the things change.

### 8.3 Pattern specs
Frames at 30 fps. Building blocks: `VEOS.scene` (bespoke HTML/canvas), `ctx.videoFrame` (recordings), `VEOS.fx.shot`
(screenshots with highlights), `VEOS.fx.appUI` (recreated UI), `VEOS.fx.device` (a phone frame), `VEOS.fx.icon` (line
icons), `VEOS.fx.logoPlate`, `VEOS.fx.clip`, the camera presets `push-drift` (Z-2) / `pull-out` (Z-3), and the layouts of
§3.3.

| ID | Pattern | On screen | Motion (30 fps) | Use | Build | Needs |
|---|---|---|---|---|---|---|
| **P-01** | Lockup build | The two-line title + hairline (§5.2) | Line 2 at f2–3: a soft L→R wipe + blur 8→0, 6 f expo-out, the hairline drawing with it; line 1 at f11–12, a character-by-character L→R blur reveal (≈ 1 f per character, 4 f each); settled at f22–24 | Every reel, f0 | B-1; scene `kind: "lockup"`, z 6, `events: [0.1, 0.4, 0.9]` | — |
| **P-02** | Lockup mid (F-B hook) | The same lockup at S-title y 812–1026, between the insert and the face card | As P-01; line 1 may start at f0; ends on the G-2 cut (`out: "none"`) | H-3 | B-1 | — |
| **P-03** | Face card | The creator in the 936 × 720 card, radius 40, soft shadow (0 24 48 rgba(0,0,0,.25)) | A hard cut in; live footage | The default state; the rule; the claim | B-2 | L-lesson |
| **P-04** | Credit chip | A hand-drawn arrow (2.5 px, 70 px long, pointing up-left at the caption) + the script line ("lessons by") + the chip (the handle) (§6.7) | The whole unit cuts on with a 6 f flicker: on 3 f, off 1, on 1, off 1, then on (v04 @ 0:05.43); exit hard off in 1 frame (v04 @ 0:10.2) | Window W1 and window W2 (§6.7) | B-1; z 6 | S-credit |
| **P-05** | Jump cut | A cut inside the take at the **same framing** (scale 1.00 ± 2 %, measured on 30+ cuts); the pose changes, the crop doesn't | A hard cut on a word boundary; the caption swaps on the next frame | On the breaths of every talking run in L-lesson / L-full | B-2 | cutmap |
| **P-06** | Term card, light | A white card (`paper`, radius 40, filling S-card) with the term word (Anton 170 px, `termink`, shadow) at cy 720; the presenter tile bottom-right | Card and word cut on together (G-1, L-term-pip); the word is static from its first frame, no settle (v02 @ 0:02.82) | A term is named or defined ("codec", "minimum due", "HDR"), before the card shows the thing | B-3; scene z 3 (under the tile) | L-term-pip |
| **P-07** | Variant chips | Plain-text chips in a row under the term (Inter Tight 500 56 px; two-tone allowed) | Each: a soft left-to-right character reveal with blur 4→0, 8 f, no rise, starting 2 f before its caption word (v02 @ 0:03.95–4.22); ≥ 18 f apart; never re-flows earlier chips | Spoken variants, types, options, examples ("H.264, H.265, ProRes") | B-3; nested in P-06 (`overlaps`) | P-06 |
| **P-08** | Term card, dark | A charcoal card filling S-card, 1–3 condensed words on ≤ 2 lines (line 1 `primary` for the state, line 2 `paper`); no presenter | A hard cut in and out (L-term-full); the text is static; held 0.7–1.5 s (v04 @ 0:36.97–0:37.70) | A verdict ("THIS IS WRONG"), a state ("AUTOMATIC HOTA HAI"), an announced term ("FORMAT"), an announcement gag ("LADIES & GENTLEMEN") | B-3 | L-term-full |
| **P-09** | Term card, marker | A white card; the Essential pill (P-10) top-left; the brush term word (Permanent Marker 150 px) at x 112, cy 690; a strip of the settings panel (≤ 160 px tall) at y 800–960 with the highlight box drawing on its field; the presenter tile | A hard cut; the box draws (6 f) on the field word | The answer to a hook question; "the essential setting": the name and the place in one card | B-3 + B-5 + B-7 | L-term-pip; field map |
| **P-10** | Essential pill (SM-1) | The "Essential #N" pill (§5.4) | Arrives with its card (no motion of its own) | Numbered essentials | B-3 | P-06 / P-09 |
| **P-11** | Question card | A white card, a 2-line sentence-case question (Inter Tight 600 78 px, `ink`), the presenter tile | A hard cut; the text fades in over 6 f | The creator turns the lesson with a question ("Why Automatic is good then?") | B-3 | L-term-pip, 1.0–2.0 s |
| **P-12** | Number on card | A number + unit (Anton 190 px, `paper`, shadow) at the card's bottom, over the creator's chest | Hard on, on the jump cut nearest the number word (≤ 3 f before it); hard off on the next cut (v04 @ 0:18.10 on, 0:33.30 off) | A spoken value that matters ("50,000KB/S", "₹500", "30 FPS") | B-4; `overlaps` the face card; 40 px clear of the head region | L-lesson |
| **P-13** | Number beside the head | A number (64 px) + a 2–3-word note (44 px), stacked, on the empty side of the card | Hard on / off with cuts, as P-12 | A secondary value said in passing ("10,000KB/S bhi ni chahiye") | B-4 | L-lesson; the head region |
| **P-14** | Keyword on card | A format, file or product name (Anton 110–140 px, `paper`) at the card's bottom | As P-12 | A name the viewer must remember (".MOV", "APPLE PRORES 4444") | B-4 | L-lesson |
| **P-15** | Dialog card | A white card; the creator's screenshot (dark UI) inset at x 92–868, y 588–1168, radius 22, cropped to the panel; the presenter tile bottom-right, overlapping its corner | A hard cut; the screenshot settles 1.02 → 1.00 over 7 f (expo-out), then drifts in ≈ +0.1 % per frame for the card's span (v02 @ 0:09.02) | Where a setting lives in an app | B-5 (`fx.shot`, `chrome: false`) | L-term-pip; field map |
| **P-16** | Highlight box | A 4 px rectangle (`primary` on TH-dark, `paper` on TH-light, `ink` on a light UI), radius 6, 8 px padding around the field | First: the stroke traces from the **top-right corner leftwards, then down** (counter-clockwise), 14–16 f, starting ≈ 12 f before the field word and closing on it (v02 @ 0:09.15–0:09.55). Next field: position and size slide over 7 f (inOut) on the field word −2 f. Exits with the card | Every named field, value or button, and every pointing word (one box at a time) | B-7 (§8.6) | field-map keyframes |
| **P-17** | Chevron pointer | A white double chevron (« or ⌄), 96 px, 24 px outside the target, pointing at it | Pops 0.8 → 1 in 6 f; bobs 6 px toward the target on an 18 f cycle | A target under 40 px tall, a dropdown arrow, or a field the box can't frame cleanly | B-7 | field map |
| **P-18** | Cursor glide | A white arrow cursor (44 px, 2 px ink outline) gliding to the field; a click ring (r 10 → 34, 8 f, `paper` 60 % → 0) | Glide 12 f inOut, landing on the field word −2 f | Screenshots only (recordings show the real cursor) | B-7 | field map |
| **P-19** | Screen card | The creator's recording filling S-card (cover-cropped to the panel), the presenter tile bottom-left (L-screen) | A hard cut; plays at 1× (`kind: "video"`, continuous) | F-B steps | B-6 (`ctx.videoFrame`) | L-screen |
| **P-20** | Screen focus | The crop window inside the recording moves to the next panel region | Pan / zoom 14 f inOut, scale 1.0–1.6×, only when the next field is outside the current crop; never while a field name is being spoken | Long panels (the sections of an export dialog) | B-6 | field map |
| **P-21** | Value pick | The box sits on a dropdown; when the recording opens it, the box resizes onto the chosen option on the value word | Resize 7 f | "24 → 32", "Auto → 30" | B-7 | field map |
| **P-22** | Panel strip | A horizontal crop (≤ 160 px tall) of a screenshot showing one row group, inside a term card | Static; its box draws over 6 f | Inside P-09 / P-11 | B-5 | — |
| **P-23** | Top insert (16:9) | A 16:9 clip in S-insert (936 × 527, radius 40, centred in y 150–760) | A hard swap to the next clip every 0.8–2.0 s; plays at 1× | H-3: the creator's own result, or the reference clip (theirs, else fetched) | B-8 | L-insert-hook |
| **P-24** | Phone insert | A generic phone frame (300 × 610, radius 44, 10 px bezel) centred in S-insert, looping the creator's reel or app screen | The clip swaps every 0.8–1.0 s, hard | H-3 for app and reel topics | B-8 (`fx.device` phone + `ctx.videoFrame`) | L-insert-hook |
| **P-25** | Icon row | The tools named, as a row of logo plates (`fx.logoPlate` with each tool's real logo: the creator's dock capture, else fetched from the web; the name set in type only when none can be found) | Plates pop over 6 f, 4 f stagger | "Premiere, DaVinci, CapCut, sab mein" | B-8 | S-card or S-insert |
| **P-26** | B-roll in card | The creator's own B-roll (desk, setup, their result) in S-card, ≤ 1.5 s | A hard cut in and out | "Aur ye meri footage hai…" (it shows the line) | B-9 | L-lesson geometry (`fx.clip`) |
| **P-27** | Reaction in card | A reaction clip ≤ 1.2 s in S-card (the creator's, else the real one fetched); rebuilt, it's a P-08 announcement card with the line | A hard cut | Comedy `light` only, on the one moment that earns it | B-9 | comedy light |
| **P-28** | Full-bleed face | L-full: the creator full frame, the boxed caption at cy 1210, the credit under it | A hard cut (G-3); jump cuts continue at the same framing | F-B asides and rule lines, for as long as the aside lasts | B-2 | L-full |
| **P-29** | Card only (no title) | F-B body: the face card with an empty page above it | A hard cut | F-B rule lines between steps | B-2 | L-lesson |
| **P-30** | Term sequence | 2–4 terms compared by sequence: an identical card skin and position, each followed by its dialog, picture or screen card | The ritual U-1…U-3 per term | "Difference between X and Y" reels | B-3 | — |
| **P-31** | CTA chip | The credit unit in W2, carrying the CTA text (§6.7) | As P-04; the text changes with a 6 f fade | The CTA sentence | B-1 | S-credit |
| **P-32** | Recreated panel | `fx.appUI` kind `settings`: a generic, unbranded settings panel with the field names and values the creator says | Rows fade in with a 4 f stagger on first show, then static; the box as P-16 | FB-2 / FB-3, when neither the creator nor the web has the real panel | B-5 / B-6 rebuilt | — |
| **P-33** | Picture card | A white card (`paper`, radius 40, filling S-card) showing the thing itself: a recreated screen in a generic phone (`fx.device`, 300 × 610, radius 44, 10 px bezel) or a panel (`fx.appUI`), a document or statement, a line-art object (`fx.icon` or bespoke SVG, ≈ 360 px, `termink` strokes 8 px), or the creator's photo (`fx.shot`); centred in the picture zone x 112–672, y 600–1248 (centre 392, 924), clear of the presenter tile; an optional name (Anton 72 px, `termink`, right-aligned at x 968, cy 660) | A hard cut with the card (G-1), static on its first frame like P-06; then the thing acts on its words: the P-16 box traces onto the part being named, a value steps hard in its field (E6), a toggle flips (0 f), a row lights `primary` | Something the viewer should see that isn't in the creator's captures: the bill, the statement, the camera's screen, the file, the result. Also the straight-to-the-picture U-1 | B-10; `VEOS.scene` with `fx.device` / `fx.appUI` / `fx.icon` / `fx.shot`; `illustrative: true` when made up | L-term-pip |
| **P-34** | Difference card | One white card holding the same thing twice, left and right (each half 420 × 560, at x 104–524 and x 556–976, y 680–1240), split by a 2 px `mute` hairline at x 540 (y 640–1216); an Anton 72 px `termink` label over each half (cx 314 and 766, cy 630): the wrong, old or X on the left, the right, new or Y on the right. The difference is in the pictures themselves (the same frame graded two ways, the same file at two sizes, the same bill paid two ways), never red vs green | A hard cut in with the left half and its label; the right half and its label cut on hard on its word (0 f); the P-16 box then traces onto the one detail that differs | "X vs Y", "galat vs sahi", "pehle vs ab", whenever the difference can be seen | B-10; bespoke `VEOS.scene`; `illustrative: true` when made up | L-term-full (no tile; back to the face within 3.0 s) |

### 8.4 Line → pattern lookup
Vocabulary, not a decision table: it tells you what this style reaches for. Ask what the viewer should see right now, then
use it.

| Line type | Primary | Alternates | For example |
|---|---|---|---|
| The claim or setup | P-03 + P-01 | P-23 / P-24 (F-B) | "Chahe tum koi bhi software use karte ho…" over the face card while the lockup writes itself |
| A term is named or defined | P-06, then the thing (P-15, P-19, P-33) | P-08 (announced), P-09 (the essential) | "codec" → CODEC, then the export dialog with the box on Codec |
| Variants, types or examples of a term | P-07 on the term card | P-25 (tools) | "H.264, H.265, ProRes", one chip per word |
| Where it lives ("yahan pe", "is setting mein", "click karo") | P-15 + P-16 (F-A), P-19 + P-16 (F-B) | P-17, P-18, P-32 | The creator's bill screenshot, the box on "Minimum Amount Due" |
| The speaker points ("ye dekho", "this one", "this, this and this") | P-16 on each place, moving on each word | P-17 | Three fields in one panel, the box sliding to each on its "this" |
| A value is chosen ("32 select karo", "MP4 rakho") | P-21 | a P-16 move | The resolution dropdown landing on 1080 × 1920, then P-12 "1080 × 1920" |
| A setting to switch ("auto-debit on karo") | P-19 or P-32 + P-16 on the toggle | P-33 (the toggle flips on the word) | The auto-pay toggle flipping on "on" |
| A thing that isn't on a screen (an object, a document, a result) | P-33 | P-26 (the creator's own B-roll) | "bill aata hai" → a recreated statement on a phone, the box on the due line |
| A range or a scale ("300 se 900 tak") | P-33 (the screen that shows it, the box on where they are) | P-06 + P-07 chips | "CIBIL" with chips "300" and "900", then the score screen with the box on the number |
| A difference you can see (X vs Y, wrong vs right, before vs after) | P-34 | P-30 (term sequence) | The same frame twice: rich in the editor, washed out on Instagram |
| A spoken number with a unit | P-12 | P-13 (secondary), P-16 on its field | "50,000KB/S" at the card's bottom |
| A number that lives somewhere | P-16 on the field that shows it, or P-33 with the number in place | P-12 | "40% tak interest" → the interest line on the statement, boxed |
| A file, format or product name to remember | P-14 | P-06 | ".MOV" |
| A verdict ("ye galat hai", "automatic hota hai") | P-08 | P-12 | "4K ≠ / BETTER" |
| A question that turns the lesson | P-11 | — | "Why Automatic is / good then?" |
| Many tools have it ("CapCut, VN, InShot, sab mein") | P-25 | — | Type-set plates popping in a row |
| A personal aside or proof of the creator's work | P-26 | P-28 (F-B) | Their desk, their own finished reel |
| A joke or reaction (comedy light only) | P-27 | P-08 announcement | "LADIES & GENTLEMEN" |
| The rule or takeaway | P-03 (late in the reel: + Z-2 push or Z-3 pull-out) | P-28 (F-B) | "Hamesha total pay karo" with a slow push |
| The CTA | P-31 | — | The chip switching to "comment" + BILL |

### 8.5 Data and truth
- No charts and no computed numbers. Every number on screen is a value the creator says, a value visible in their own
  capture, or a realistic illustration inside a picture card (`illustrative: true`, no label).
- Callout numbers use the spoken value exactly, formatted per §5.5; captions keep the spoken digits.
- A recreated panel (P-32, P-33) uses the field names and values the creator says, in generic, unbranded styling.
- A claim like "95% editors" stays in the lockup only when the creator says it.

### 8.6 The annotation layer: box, chevron, cursor
| Token | Value |
|---|---|
| Stroke | `primary` on TH-dark, `paper` on TH-light, `ink` over a light UI; 4 px wide (3 px on targets under 40 px tall); no wobble (a clean UI rectangle, not a hand-drawn mark) |
| Box | Radius 6, padding 8 px around the field's rect; the stroke traces from the top-right corner leftwards then down (counter-clockwise) over 14–16 f (15 f default), starting ≈ 12 f before the field word and closing on it; slides position and size over 7 f inOut to the next field |
| Chevron | White double chevron, 96 px, 24 px outside the target, bobbing 6 px per 18 f |
| Cursor | White arrow, 44 px, 2 px ink outline; glide 12 f; click ring 8 f |
| On screen | One mark at a time (a box, or a chevron, or a cursor) |

Marks used: **box** (P-16, P-21), **chevron** (P-17), **cursor** (P-18). No circles, scribbles, arrows with heads,
underlines or brackets.

Targets come from the **field map** (§1 step 3): for each screenshot, recording or picture card, every named field's rect
in card coordinates, and for recordings the local time range in which the field sits at that rect (re-read the frames after
any scroll).
- The box always sits on the field being named, from its word until the next field's word.
- Marks finish before the card cuts away; they stay off the presenter tile and the face.
- When a recording scrolls under a static box, cut the box at the scroll start and redraw it on the new rect when the field
  is still again (6 f).
- No mark on a field the field map doesn't contain.

### 8.7 Comedy: off unless the creator turns it on
Calm teaching is the default. With comedy `light`: P-27 only (a reaction clip ≤ 1.2 s, the creator's or fetched, or its
P-08 rebuild), never on a teaching beat's trigger word, never with a meme sound.

### 8.8 Assets
- Real captures first: the creator's own screen recordings and screenshots for every app or setting (SH-2, SH-3), cropped
  to the panel being discussed, identifiers blurred.
- What they don't have: the real panel or page captured from the web (identifiers blurred), else built as generic,
  unbranded panels and devices (P-32, P-33) with the values they say; no labels.
- Logos and app icons: the creator's own dock capture, else the real logos fetched from the web, on plates (P-25); type-set
  plates only when none can be found.
- Film clips, memes, other creators' reels: fetch the real thing, source noted (§12.5).
- No stock footage, no AI scenes, no decorative B-roll.

---

## §9 Transition system

### 9.1 Library (hard cuts only)
| ID | Transition | Frames | Recipe | Sound |
|---|---|---|---|---|
| **T-01** | Jump cut | 0 | A cutmap cut inside the talking head on a word boundary ±1 f; pairs with P-05 | silent |
| **T-02** | Card content cut (G-1) | 0 | `stage.via: cut` + the card scene's `t_in` on the same frame | a reveal (on a new card) |
| **T-03** | Composition cut (G-2) | 0 | F-B hook → body: the insert and lockup scenes end, the stage cuts, captions start | a reveal |
| **T-04** | Full-bleed cut (G-3) | 0 | L-lesson ↔ L-full | silent |
| **T-05** | Lockup build | 25 | The lockup's entry (P-01); not a scene transition | silent |
| **T-06** | Credit window in / out | 6 / 0 | The P-04 flicker on and the hard off | silent |
| **T-07** | Hard end | 0 | The last frame ≤ 6 f after the last word, on the face card | — |

### 9.2 Grammar
| Boundary | Use | Never |
|---|---|---|
| Frame 0 | Already playing (no fade-in) | A fade from black, a title card |
| Hook → body | F-A: T-02 to the first card; F-B: T-03 | Any animated transition |
| A new term, thing or step | T-02 on the trigger word −2 f | A slide, a pop, a crossfade |
| Back to the creator | T-02 (or T-04 into L-full) | A grow or a pop-back |
| Inside a talking run | T-01 with P-05 | Smooth zooms |
| A number or keyword lands | The callout cuts on with the nearest jump cut | A shake, a flash, a scale-in |
| Last word | T-07 | An outro card, a black tail |

### 9.3 How the moves breathe
Every move here is a cut, so the rhythm lives in where the cuts fall, not in how they look. Jump cuts sit on the creator's
breaths and keep the face card alive; card cuts sit on the words that name things and carry the lesson; the face comes back
the moment the card has nothing new. Because nothing ever slides, the few smooth moves in the reel, the late push and the
pull-out on the face, feel enormous. Keep them for the line that deserves them.

---

## §10 Motion tokens, camera and zoom, layers, finishing

### 10.1 Motion tokens (30 fps)
| Token | Value |
|---|---|
| Beat lead | 2 f before the trigger word (the caption leads 1 f) |
| Entry ease | `cubic-bezier(0.22, 1, 0.36, 1)` (expo-out) |
| Exit ease | `cubic-bezier(0.64, 0, 0.78, 0)`, 5–6 f, used only by callouts and the credit chip |
| Lockup reveal | Line 2: an L→R soft wipe + blur 8 → 0, 6 f, at f2–3; line 1: an L→R per-character blur reveal at f11–12, ≈ 1 f per character, 4 f each; settled f22–24 |
| Hairline draw | 6 f, left to right, with line 2 |
| Term, dark-card and picture-card text | None: on with the cut, static |
| Variant chip | An L→R character reveal + blur 4 → 0, 8 f, no rise; ≥ 18 f between chips |
| Callouts | Hard on / off with jump cuts (0 f) |
| Highlight box | A stroke trace from the top-right, counter-clockwise, 15 f (14–16), starting 12 f before the word; slide 7 f inOut |
| Screenshot settle | 1.02 → 1.00, 7 f expo-out, then +0.1 %/f drift |
| Chevron | Pop 6 f; bob 6 px per 18 f |
| Credit chip | Flicker-on 6 f (on 3, off 1, on 1, off 1, on); exit hard (0 f) |
| Holds | Titles ≥ 10 f after building; on-screen text ≥ 0.25 s per word (captions under E3: ≥ 0.15 s per word) |

### 10.2 Footage camera and zoom (`zoom_policy: presets`)
Measured at the full frame rate (background-registered scale between frames): the jump cuts keep the framing (scale 1.00 ±
2 % across 30+ cuts in v01, v02, v04). The only camera moves are smooth pushes and pull-outs on the face card, all in v02's
back half (0:31–0:42); v01, v03 and v04 have none.

| ID | Preset | Recipe (30 fps) | Use |
|---|---|---|---|
| **Z-1** | none (cutmap) | A jump cut at the same framing; no camera event | Every breath of talking (P-05) |
| **Z-2** | `push-drift` | 1.00 → 1.28 over 18 f, accelerating (`ease: "in"`, built into the preset; measured +0.5 %/f rising to +4 %/f), starting on a jump cut; it holds the push until the next card cut or stage cut, which resets to 1.00 (v02 @ 0:41.20–0:41.77). Small variant: 1.00 → 1.08 over 14 f (v02 @ 0:31.8, 0:34.7) | A rule or verdict line said with emphasis, in the back half |
| **Z-3** | `pull-out` | 1.15 → 1.00 over 33 f, near-linear (`ease: "linear"`; −0.4 %/f), starting **mid-shot from the tighter crop** (v02 @ 0:38.77–0:39.8): when the face card is already tighter than 1.00 (a held Z-2), write `{"preset": "pull-out", "p": {"from": "inherit"}}` so it pulls from the crop on screen with no snap. From a 1.00 card, start it on a jump cut at the preset's 1.15 | A widening line ("lossless", "the whole picture"), in the back half |

- The camera is a late, rare instrument: a lean-in or two in the back half, each on the line that earns it, and never in the
  hook. Alternate push and pull so it feels like a person leaning in, not a machine (v02: push, small push, pull, push).
- Only in L-lesson; never inside L-term-pip, L-screen, L-insert-hook or L-full. The stage resets the camera at every layout
  cut, so the first face-card shot after a card is always 1.00.
- No punch, shake, rotation or zoom-through. A Z-2 at 1.28 needs a source ≥ 1080 px wide.

### 10.3 Layer order (back to front)
1. W-page (z 1).
2. Card scenes that fill S-card or S-insert: term, picture, difference, dialog and screen cards, inserts, B-roll (z 3).
3. The stage window: the face card or the presenter tile (z 4).
4. Callouts on the face card, variant chips, the Essential pill, the highlight box, chevron and cursor (z 5).
5. The lockup and the credit chip (z 6).
6. Captions (z 7, auto).

z 8–11 aren't used.

### 10.4 Finishing
- The card: radius 40; soft shadow 0 24 48 rgba(0,0,0,.25) (visible on TH-light, invisible on TH-dark); a screenshot inside
  a white card gets radius 22 and no border.
- Page noise 0.02 on TH-dark; nothing on TH-light.
- Glow: only the hairline (8 px, `primary` at 60 %).
- No grain, no vignette, no bloom, no light leaks, no colour grade.

---

## §11 Sound

The cut is the beat; sound only marks a card landing. (The reference reels' sound couldn't be measured, so this is a
decision, not a measurement.)

| Line | Direction |
|---|---|
| **Where sound goes** | Reveals: a term, picture, dark or question card landing; the first box draw on a new card; a number callout. The list cue: the unit entry when the reel numbers its essentials or F-B steps (one file, at each unit). The hook carries at most one cue, on its first card (H-1, H-2, H-4) or the composition cut (H-3). Jump cuts, caption swaps, box slides and the credit chip are silent. Sparse: if in doubt, leave it out |
| **Meme sounds** | None (comedy `light` adds none either) |
| **The bed** | On: a calm bed, entering after the hook (on the first unit) |
| **Ducking** | The bed sits 20 dB under the voice while the voice speaks |
| **Loudness** | −14 LUFS integrated, true peak ≤ −1.5 dBTP; a hard end ≤ 6 f after the last word |

A second of silence before the CTA sentence.

---

## §12 Footage handling

### 12.1 Setups
| Setup | Spec |
|---|---|
| **A** Talking head | Webcam or phone, seated front-on, chest-up, the lens at eye level or slightly below; a plain lit room with one practical lamp or plant behind; a 16:9 or 9:16 source (the card crops 4:3), framed so the head top lands at y 610–720 in the card; 30 fps (VFR conformed); plain clothing (no fine stripes: the card downsamples) |
| **B** Screen capture | The app at 100 % UI scale on a 1080p+ display, no webcam overlay (the engine draws the presenter tile), the cursor visible, slow deliberate moves; one recording per step, or one continuous take with clean pauses |

### 12.2 Shots and fallbacks
| ID | Shot | Spec | Formats | Without it |
|---|---|---|---|---|
| SH-1 | Talking head in short breaths | Setup A; 2–4 words per breath; gestures toward the lens (an OK sign, a point) | F-A, F-B (must) | **FB-1** none: the style is the creator teaching |
| SH-2 | A screen recording per step | Setup B; 3–12 s each; the cursor rests on each field as it's named | F-B (must) | **FB-2** the real panel captured from the web (the app's own docs or help pages) with the box stepping through it; else a P-32 recreated settings panel (`fx.appUI` kind `settings`, generic, unbranded) with the spoken field names and values. Either costs the real UI motion and scroll (degraded) |
| SH-3 | Screenshots of the named panels | PNG, full resolution, cropped later | F-A (optional) | **FB-3** the real panel captured from the web inside the dialog card; else the same recreated strip, or a P-33 picture card (degraded: a generic UI instead of the real panel) |
| SH-4 | A hook proof clip | 2–4 s of the creator's own result or phone screen recording | F-B (optional) | **FB-4** the H-1 claim lockup instead of the insert hook; no proof clip in the first 2.7 s (holds) |
| SH-5 | Their own B-roll | 1–2 s of the creator's desk, setup or result | F-A, F-B (optional) | **FB-5** skip the aside, or show the thing on a picture card; stay on the face card with a jump cut (holds) |

Mention the fallbacks you used when you show the storyboard.

### 12.3 The presenter tile, the reaction bank, resolution
- **The tile:** the reference term and dialog cards show the creator as a cut-out leaning in at the card's corner; the
  engine has no cut-out picture-in-picture, so the creator sits in a rounded tile (L-term-pip 288 × 320, L-screen
  300 × 300, radius 28). No matte is needed for this style.
- **Props:** none.
- **Reaction bank** (natural gestures to keep in the cut): an OK sign to camera, an index finger at the lens, a two-hand
  "frame", a shrug, a hand-wave "no". Keep them; on the face card they're the creator's own graphics.
- **Resolution:** the Z-2 push (1.28) needs a source ≥ 1080 px wide (a 16:9 1080p webcam gives ample room in the 936 px
  card). Screenshots under 1600 px wide: crop tighter and treat their small text as texture. A recording under 1080 px tall:
  its field text is texture too, and the box and caption carry the meaning.

### 12.4 Frame rate and audio
30 fps CFR, 1080 × 1920, BT.709. One voice track: high-pass 80 Hz, de-ess, light compression, −14 LUFS.

### 12.5 Third-party inserts: fetch the real thing
When the lesson names a real film scene, reel, logo, app or product UI, the viewer should see the real one. The creator's
own files in their folder come first; otherwise search the web and fetch it, and note where it came from. Use it as it is
(cropped, framed in the card, the box on the part that matters), never altered to say something it doesn't. Only when
nothing usable turns up, rebuild it from its exact words, with no labels and no credit lines.

| Moment | The real thing (the creator's, else fetched) | Rebuilt (nothing usable found) |
|---|---|---|
| A film or TV scene that evokes the topic (v01's hook) | the clip | A P-08 dark card with the concept ("SUBTITLES / BURNED IN"), a P-33 picture card of the idea, or `fx.appUI` kind `video` with a generic frame |
| A celebrity or creator reaction meme (comedy light) | the clip | A P-08 announcement card with the line |
| Another creator's reel in the phone mock | the reel | `fx.appUI` kind `video` inside the phone frame |
| App icons, tool logos (v04's dock) | the creator's dock capture, else each real logo | P-25 type-set logo plates |
| A product's UI the creator didn't record | the real panel, captured from the app's site or docs | A P-32 recreated panel or a P-33 picture card |

---

## §13 What your plan should settle

Your `ideas.md` is a page or two, for you. In this style it has decided, before any code:
1. **The format and the page:** F-A or F-B, TH-dark or TH-light (§3.1, §3.2).
2. **The hook:** the lockup (8–10 candidates, the pick, two alternates), the hook (H-1…H-4), its first proof card and its
   time.
3. **The picture list:** every term, setting, value, number, object and pointing word, with what the card shows for each,
   and which ones get a name card first. No unit ends without a picture.
4. **The field map:** every box rect in card coordinates, per asset (for recordings, the local time and scroll), and every
   chevron where a box can't frame cleanly.
5. **The card map, beat by beat:** `slot_content` and the ink marks (below), the layout, the trigger word, the tone.
6. **The camera:** the late push or pull-out, if any, and its line.
7. **The furniture:** the credit windows, the chip's text, the CTA device.
8. **The inserts** (the creator's, fetched or rebuilt) and the fallbacks used.
9. **The sound:** the few cues, the list cue, the bed's entry.
10. **The moments you'll look at hardest on the storyboard:** f0 and 0.8 s (the lockup complete), the first card, one picture or dialog card
    with the box on its field, one callout on the face card (the head clear), in F-B an L-insert-hook frame (no caption, the
    face clear) and an L-screen frame (the box off the tile), and the last frame.

**Beat fields this style adds:**
- `slot_content`: `{S-card: "face" | "term_light:<WORD>" | "term_dark:<LINES>" | "term_marker:<WORD>" | "question" |
  "picture:<thing>" | "difference:<A>|<B>" | "dialog:<asset>" | "screen:<asset>" | "broll:<asset>" | "reaction:<insert>",
  S-title: "lockup" | "none", S-credit: "credit" | "cta" | "none", S-insert: "<asset>"}`
- `ink`: `[{mark: box | chevron | cursor, target: "field:<name>", rect: {x, y, w, h} (card coordinates), at, frames}]`,
  from the field map.
- `exception`: `E3` (captions, inherited) or `E6` (caption and slot swaps).

A beat from 14.1, for the shape:
```yaml
- id: 6
  section: TERM-1
  t0: 3.00
  t1: 5.20
  spoken: "agar tum sirf minimum due pay karte ho"
  trigger: {word: "minimum", at: 3.06}
  tone: warn
  layout: L-term-pip
  pattern: P-09
  visual: "White card: 'Essential #1' pill, brush 'Minimum Due', the creator's bill strip with the orange box drawing on 'Minimum Amount Due'; presenter tile bottom-right"
  slot_content: {S-card: "term_marker:Minimum Due", S-title: lockup, S-credit: none}
  ink: [{mark: box, target: "field:Minimum Amount Due", rect: {x: 132, y: 846, w: 520, h: 64}, at: 3.06, frames: 6}]
  caption: {profile: CS-1, overrides: []}
```

---

## §14 Worked examples

Times are planning estimates: take the real ones from the words. Every card cut sits on its word −2 f. They show the
standard; match it, then beat it.

### 14.1 Money, F-A Lesson Frame, H-2 question hook: "credit card minimum due"
- **Lockup:** "This Mistake is / costing you interest". **Page:** TH-dark. **Count:** 3 essentials (pills #1–#3). **CTA:**
  `comment_keyword` "BILL".

**The hook (0–3.0 s)**
| t (s) | Spoken | Visual | Caption chunks | Layout / camera |
|---|---|---|---|---|
| f0 | "Mera ek…" | The face card, the creator glancing down | "MERA EK" | L-lesson 1.00 |
| 0.17–0.67 | "…question hai" | The lockup builds (line 2 + hairline, then line 1) | "QUESTION HAI" | — |
| 1.10 | "honestly batana" | A jump cut; a finger at the lens | "HONESTLY BATANA" | Z-1 |
| 1.80 | "credit card ka bill aata hai" | A jump cut | "CREDIT CARD KA" → "BILL AATA HAI" | Z-1 |
| 2.60 | "toh tum kitna pay karte ho?" | — | "TOH TUM KITNA" → "PAY KARTE HO" | — |
| **3.00** | "Agar sirf minimum…" | **P-09:** "Essential #1", brush "Minimum Due", the creator's bill strip (account number blurred), the orange box drawing on "Minimum Amount Due" | "AGAR SIRF MINIMUM" | L-term-pip (cut) |

**The body**
| Section | t (s) | Spoken (gist) | Tone | Layout | Patterns |
|---|---|---|---|---|---|
| TERM-1 | 3.0–5.2 | "agar tum sirf minimum due pay karte ho" | warn | L-term-pip | P-09, P-10, P-16 |
| | 5.2–7.4 | "toh baaki bill pe interest lagta hai" | warn | L-term-pip | **P-33:** a recreated statement on a generic phone (illustrative): "Minimum paid ₹2,000", "Balance carried ₹38,000"; the box traces onto the balance line on "baaki" (5.6) and slides to a new row "Interest ₹1,240" that cuts on hard on "interest" (6.6); **credit W1 5.4–13.0** (P-04) |
| | 7.4–8.6 | "interest lagta hai" (repeated as the verdict) | warn | L-term-full | P-08 "INTEREST" (`primary`) / "LAGTA HAI" (`paper`) |
| | 8.6–12.4 | "aur kuch cards pe ye saal ka 40% tak hota hai" | warn | L-lesson | P-05; **P-12 "40%"** on "40%" (10.2), held to 11.4 |
| TERM-2 | 12.4–14.0 | "Toh sahi tarika kya hai?" | explain | L-term-pip | P-11 "So what's the / right way?" |
| | 14.0–17.4 | "total amount due, poora, due date se pehle" | win | L-term-pip | P-06 "TOTAL DUE" + P-10 "Essential #2" + P-07 chips "full amount" (15.1), "before due date" (16.3) |
| | 17.4–20.4 | "app mein yahan dikhega… aur yahan pay" | explain | L-term-pip | P-15 the creator's card-app screenshot; P-16 on "Total Amount Due" (17.5) → slides to "Pay" (19.6) |
| | 20.4–24.0 | "hamesha total pay karo, minimum nahi" | win | L-lesson | P-03, P-05 ×2 |
| TERM-3 | 24.0–27.0 | "Aur agar ek saath nahi ho raha, toh EMI mein convert karo" | explain | L-term-pip | P-06 "EMI" + P-10 "Essential #3" + P-07 "convert" (25.2), "lower rate" (26.1) |
| | 27.0–29.6 | "is option se" | explain | L-term-pip | P-15 the screenshot "Convert to EMI"; P-16 on the option (27.3); **credit W2 27.0–38.0** |
| | 29.6–31.4 | "interest kam lagega" | win | L-lesson | P-03, P-05; the first Z-2 small push (1.00 → 1.08) on "kam" |
| RULE | 31.4–32.8 | "minimum due bill paid nahi hai" | warn | L-term-full | P-08 "MINIMUM DUE ≠" (`primary`) / "BILL PAID" (`paper`) |
| | 32.8–34.4 | "yaad rakhna" | explain | L-lesson | P-03 |
| CTA | 34.4–38.0 | "Comment karo BILL, main checklist bhej dunga" | cta | L-lesson | **P-31:** the W2 chip switches to "comment" + "BILL" at 34.4 (a second of silence before) |

Cue moments: 3.0 (P-09 lands), 6.6 (the interest row on the statement), 7.4 (P-08), 10.2 (P-12), 12.4 and 24.0 (the list
cue: the Essential #2 and #3 entries share one file), 31.4 (P-08). The bed from 3.0. Inserts: the bill and card-app
screenshots (the creator's; FB-3 a recreated statement if not); the statement in P-33 is created.

### 14.2 Creator tools, F-B Screen Walkthrough, H-3 insert hook: "export settings for reels"
- **Lockup:** "Best Export Settings / for Instagram reels". **Page:** TH-light (the card shows a dark editor UI). **CTA:**
  `follow_save_stack`. **Assets:** SH-4 the creator's own reel (phone insert), SH-2 one recording of their editor's export
  panel (34 s) and one of the upload screen (6 s).

**The hook (0–2.8 s)**
| t (s) | Visual | Caption | Layout |
|---|---|---|---|
| f0 | L-insert-hook: the phone insert (P-24) playing the creator's reel; the face card below; lockup line 1 starting between them (P-02) | hidden | L-insert-hook |
| 0.17–0.67 | Line 2 + hairline; the lockup complete | hidden | — |
| 0.90 | The phone cuts to the editor's timeline screen | hidden | — |
| 1.80 | The phone cuts to the export screen | hidden | — |
| **2.80** | **G-2 composition cut** to L-screen: the export panel recording, the box drawing on "Resolution" | "RESOLUTION SABSE PEHLE" | L-screen (cut) |

**The body**
| Section | t (s) | Spoken (gist) | Layout | Patterns |
|---|---|---|---|---|
| STEP-1 | 2.8–6.8 | "resolution 1080 by 1920 rakho" | L-screen | P-19, P-16 on "Resolution" (2.8); **P-21** the box onto "1080 × 1920" (4.6); credit W1 5.0–13.0 |
| STEP-2 | 6.8–9.6 | "frame rate 30" | L-screen | P-16 slides to "Frame rate" (6.8); P-21 onto "30" (7.9) |
| aside | 9.6–12.4 | "60 tabhi, jab shoot bhi 60 pe kiya ho" | L-full | P-28 full-bleed, the caption at cy 1210, the credit in S-credit-full; P-05 ×1 |
| STEP-3 | 12.4–16.6 | "bitrate recommended pe rakho" | L-screen | **P-20** the focus pans to the quality section (12.4, 14 f); P-16 on "Bitrate" (13.0); P-21 onto "Recommended" (14.2) |
| verdict | 16.6–17.8 | "zyada bitrate se quality nahi badhti" | L-term-full | P-08 "HIGHER ≠" (`primary`) / "BETTER" (`paper`) |
| STEP-4 | 17.8–23.0 | "format MP4, codec H.264" | L-screen | P-16 on "Format" (18.0) → "MP4" (19.4) → "Codec" (20.6) → "H.264" (21.6) |
| RULE | 23.0–26.4 | "bas ye chaar settings" | L-lesson | P-29 card only (no title), P-05 ×2; credit W2 from 25.0 |
| STEP-5 | 26.4–31.4 | "aur upload karte waqt high quality on" | L-screen | P-19 the upload recording; P-17 chevron at the small toggle (28.3) |
| CTA | 31.4–35.0 | "aise aur settings ke liye follow kar lo" | L-full | P-28; P-31 the chip reads "follow for more" + the handle (31.4) |

Cue moments: 2.8 (the composition cut), the list cue at each STEP entry (6.8, 12.4, 17.8, 26.4: one file), 16.6 (P-08). The
bed from 2.8.

### 14.3 Creator tools, F-A Lesson Frame, H-1 claim lockup, a term sequence: "HDR vs SDR"
- **Lockup:** "95% Creators / don't know this difference". **Page:** TH-dark. **CTA:** `none` (the credit chip: "lessons
  by" + the handle).

| Section | t (s) | Spoken (gist) | Layout | Patterns |
|---|---|---|---|---|
| HOOK | 0–2.8 | "Chahe tum phone se shoot karo ya camera se, tumne settings mein dekha hoga…" | L-lesson | P-01, P-03; jump cuts at 1.1 and 2.0 |
| TERM-1 | 2.8–4.6 | "HDR" | L-term-pip | P-06 "HDR" |
| | 4.6–8.2 | "10-bit, HLG… zyada colours, zyada brightness range" | L-term-pip | P-07 "10-bit" (4.8), "HLG" (5.9); credit W1 5.2–12.0 |
| | 8.2–10.6 | "phone mein yahan milega" | L-term-pip | P-15 the creator's camera-settings screenshot; P-16 on "HDR video" (8.4) |
| TERM-2 | 10.6–12.4 | "aur SDR" | L-term-pip | P-06 "SDR" (P-30: the same skin, the same position) |
| | 12.4–15.0 | "8-bit, normal range, har phone pe same dikhta hai" | L-term-pip | P-07 "8-bit" (12.6), "every screen" (13.9) |
| RULE | 15.0–16.4 | "Instagram pe HDR kabhi kabhi…" | L-lesson | P-03, P-05 |
| | 16.4–18.6 | "…washed out…" | L-term-full | **P-34:** the same sunset frame twice (illustrative): left "EDITOR", rich colour; right "INSTAGRAM", grey and lifted, cutting on hard on "washed" (16.6); the box traces onto the flat sky on the right (17.4). Alternate: P-14 "WASHED OUT" on the face card |
| | 18.6–19.6 | "…dikhta hai" | L-lesson | P-03 (the face for the end of the phrase) |
| verdict | 19.6–20.8 | "toh HDR hamesha better nahi hai" | L-term-full | P-08 "HDR ≠" / "ALWAYS BETTER" |
| where | 20.8–24.4 | "reels ke liye ye toggle off rakho" | L-term-pip | P-15 the same screenshot; P-17 chevron at the small toggle (21.4) |
| close | 24.4–32.0 | "jab tak tumhara editor HDR export na kare" | L-lesson | P-03, P-05 ×3; Z-3 pull-out from 1.15 on "export" (the reel's one smooth move); credit W2 22.0–32.0 |

Cue moments: 2.8 and 10.6 (the term entries, one list-cue file), 8.4 (the first box), 16.6 (the washed-out half), 19.6
(P-08). The bed from 2.8. The difference card is the moment the viewer *sees* why it matters; the face comes back for the
end of the phrase before the verdict card, so it's never gone for long.

---

## §15 Your look at the storyboard: the checklist

Watch it once as a stranger with a thumb over the next reel, then once as the editor whose name is on it. Fix what
bothers you, in one pass.

**The style (does it feel like §The feel?)**
- Frame 0: the creator is already talking in the card (or the proof insert is already playing); the title writes itself
  and reads by 0.8 s; the first card lands by 3.0 s.
- Pause anywhere: the card holds the creator or the actual thing being named. Every unit shows its thing (a screen, a
  field with the box, a picture, a difference), not only its name.
- Every pointing word got its place, on the word.
- The frame never moves; every change is a hard cut inside the card.
- Orange appears only on "this one"; nothing else is bright except the chip.
- It breathes like a teacher talks: quick names, a dark card for the verdict, the face for the rule, and at most a late,
  deliberate lean-in.
- Start to end: you know exactly where to click, or exactly what the term means, and you'd save it.

**Craft (by eye, in context)**
- The face reads whenever the moment is about the creator: callouts on the chest or the empty side, the caption below the
  card, marks off the tile, no caption on the L-insert-hook face. Nothing chops the head or buries the face by accident.
- No text over text: the lockup, one card text group, the caption; one mark at a time.
- Every card, picture, box move, callout and chip lands on its word (the box's trace may start ≈ 12 f early and closes
  on the word); jump cuts on word boundaries; nothing lingers after its point.
- Every number shown is spoken, in the creator's capture, or a realistic illustration with no label; values the creator
  says are exact; fetched panels and posts word for word; identifiers blurred for their whole time on screen.
- Every box sits on a field from the field map; names, tools and formats spelt exactly.
- The promised count = the units shown; a hook question is answered on a card; the CTA keyword readable on the chip.
- Captions: CS-1 44 px ALL CAPS, +0.10 em, 1 line, 2–4 words, hard swaps, no emphasis, cy 1345 (1210 in L-full, hidden
  on L-insert-hook).
- Nothing below y 1536 (except the L-insert-hook face card); the frame's rects hold still.
- The file itself (1080 × 1920, 30 fps, −14 LUFS, a hard end ≤ 6 f after the last word on the face card, no black tail)
  is the render's job; it checks it. No outro card.

---

## §16 Build notes
- **Fonts:** Inter Tight, EB Garamond (italic), Space Grotesk, Anton, Permanent Marker, Caveat, Noto Sans Devanagari, all
  bundled. Pre-paint the ₹, ×, ✓ and ≠ glyphs (warm-up) before they're first used.
- **Determinism:** every frame is a function of its index; no CSS animation in scenes; recordings play through
  `ctx.videoFrame`.
- **Swaps:** card scenes in S-card mark their container `data-slot` and declare `exception: "E6"` (hard swaps inside a rect
  constant to ±4 px); captions inherit E3 and E6 from the profile.
- **Slot constancy:** judge it by eye on the storyboard (the card edge, the title, the caption line and the credit slot
  don't move).
- **Credit windows** are set by each credit scene's `t_in` / `t_out` (the slot itself has no window field).
- **The box's early start:** the trace starts at the scene time `word − 12 f` (`hilite_lead_frames: 12`); a lead of up to 15 f
  still reads as on the word.
- **Picture and difference cards** are bespoke `VEOS.scene`s inside the S-card rect, z 3 under the tile, built from
  `fx.device`, `fx.appUI`, `fx.icon` and `fx.shot`; a value that steps in place uses an E6 `data-slot`; mark made-up content
  `illustrative: true`.

---

## Appendix A. Evidence map
The full map (every element → `vNN @ m:ss`) is in `evidence.md`. Sources: four native 1080 × 1920 reels (v01 subtitles 34.1 s,
v02 codec vs format 46.5 s, v03 render settings 32.5 s, v04 the bitrate mistake 47.2 s), their frame sheets, a fidelity
audit (6 Oct 2026, pixel-measured) and a full-frame-rate completeness pass (7 Oct 2026).

| What | Evidence |
|---|---|
| The persistent lockup and its build (line 2 at f2–3, line 1 at f11–12, settled f22–24) | v02 @ 0.05–0.85 s; v04 @ 0:00.67–0:46 |
| The card rect x 72–1008, y 568–1288, radius ≈ 40 | v02 @ 0:06, 0:10; v04 @ 0:18; v03 @ 0:09 |
| Jump cuts at the same framing; camera moves only in v02's back half | 30+ cuts across v01, v02, v04; v02 @ 0:31.8–0:41.77 |
| The box tracing from the top-right, 14–16 f, ≈ 12 f early | v02 @ 0:09.15–0:09.55 |
| The credit chip's two windows and its flicker | v04 @ 0:05.43 / 0:10.2; every reel hides it mid-video |

Not verifiable from the reels: the speech language (read from burnt-in captions), all sound, the exact caption timing, and
the presenter cut-out on term cards (drawn here as a rounded tile).

## Appendix B. Hook-title bank
`[…]` slots are filled per reel. Line 1 is the stake (Inter Tight, Title Case), line 2 the twist (EB Garamond italic,
sentence case).

| # | Line 1 | Line 2 | Format · hook | For example |
|---|---|---|---|---|
| 1 | [N]% [People] | don't know this difference | F-A · H-1 | "95% Creators / don't know this difference" (HDR vs SDR) |
| 2 | This Mistake is | ruining your [thing] | F-A · H-2 | "This Mistake is / ruining your credit score" |
| 3 | This Mistake is | costing you [loss] | F-A · H-2 | "This Mistake is / costing you interest" |
| 4 | Only Pro [People] | use this [setting] | F-A · H-1 | "Only Pro Editors / use this kind of subtitle" |
| 5 | Your [Tool] | has a hidden mode | F-A · H-4 | "Your UPI App / has a hidden mode" |
| 6 | Stop [doing X] | for your [goal] | F-A · H-1 | "Stop Shooting 4K / for your reels" |
| 7 | [N] Settings | every [person] should change | F-A · H-1 | "3 Settings / every phone user should change" |
| 8 | [Term] vs [Term] | explained in 30 seconds | F-A · H-4 | "SIP vs Lump Sum / explained in 30 seconds" |
| 9 | Nobody Tells You | what [term] means | F-A · H-4 | "Nobody Tells You / what CIBIL means" |
| 10 | The [Thing] Rule | most people get wrong | F-A · H-2 | "The 50-30-20 Rule / most people get wrong" |
| 11 | Best [Tool] Settings | for [use] | F-B · H-3 | "Best Export Settings / for Instagram reels" |
| 12 | Set Up [Feature] | in under a minute | F-B · H-3 | "Set Up Auto-Pay / in under a minute" |
| 13 | Turn This Off | before you [action] | F-B · H-3 | "Turn This Off / before you upload" |
| 14 | [N] Settings | your [app] hides from you | F-B · H-3 | "5 Settings / your banking app hides" |
| 15 | Read Your [Document] | like a [pro] | F-B · H-3 | "Read Your Statement / like a banker" |
| 16 | Fix [Problem] | in [N] clicks | F-B · H-3 | "Fix Blurry Uploads / in 3 clicks" |
| 17 | The Right Way | to [action] | F-B · H-3 | "The Right Way / to file your ITR" |
| 18 | Where to Find | [hidden setting] | F-B · H-3 | "Where to Find / your UPI limit" |
| 19 | [App] Settings | I change first | F-B · H-3 | "Camera Settings / I change first" |
