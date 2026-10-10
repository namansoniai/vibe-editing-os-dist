# Device Whip Style Playbook (template v2)

## The feel

This reel feels like a friend who just picked up a gadget and can't wait to show you the thing nobody told you about. The
first frame is the device swinging at the lens, the picture punching in on it, a heavy blue italic title snapping on
underneath, one phrase at a time. Before you've finished reading, the whole frame whips: a blur, a flash, a spin, and
you're looking down at the device in a hand, a thumb already doing the trick. You didn't watch someone talk about a
phone. You held it.

That whip is the engine. It's the moment the reel stops telling and starts showing, and every section pays it off
again: each new item, each result, each exit back to the face arrives on a whip, and everything inside an item is a cut
you never notice. A feature is named, you're on the device. An opinion, you're back on the face. One full picture at a
time, never split, never boxed, each held exactly as long as the sentence that earned it: quick on the tricks, a held
breath before the result, the best one last.

The device is the hero and the real thing is the proof: real screen, real hand, real colours, never a render. Graphics
only point at it: a cyan light that runs up its edges once, when you should look; a ripple where the finger lands; a red
counter that rolls up across every cut as the reel pushes something to its limit, breaking into hard step-punches right
before the answer. The words stay quiet, one small white caption line at the same height all reel, because the device is
what you're reading. Blue is the hook, red is the count, cyan is "look here"; nothing else gets a colour. The joke lives
on the creator's face, never in a sound effect.

It ends clean: a reaction, or a hard cut to black and a name that smears in, and stops.

**The test:** pause on any frame and you're looking either at the creator's face or at the real device in a hand, and you
can tell which one the words are about.

## What this playbook is

You're editing a hands-on tech or gadget reel: the creator talking with a device in hand, plus the close-ups they shot of
that device in their hand. You have the authority to make it the most watchable review in their niche. This playbook is
the style, pulled from three of Mrwhosetheboss's reels (v01 an invitation story, v02 five iPhone tricks, v03 a count-up
test), measured frame by frame at full resolution and at full frame rate. Read it all, every time; take what fits this
reel, invent where a moment needs more, and never break the feel above.

**Who it's for and what it needs.** Creators who review or demo things you hold: phones, earbuds, watches, kitchen and home
gadgets, tools. Input: one talking-head take with the device in hand (spine `hybrid`: the face and the device alternate as
equals) and 4–12 POV clips of the device in one hand, from a second camera or a phone; a hold-up or lean-in hook shot,
clamp shots for count-ups, macro details and native screen recordings help (§12). The POV footage *is* the style: without
it the reel falls back to screen recordings in a drawn phone and reads as a different style. Reels run about half a minute
to fifty seconds. No cut-out: nothing in this style layers behind the person. Captions follow the creator's language
(English verbatim by default; Hinglish stays romanised; §5.5); the title is always Latin italic caps. Machine values live
in `tokens.json`; where this text gives a number tokens also holds, they agree.

### Style directives (non-negotiable)
| # | Directive | Where it lives |
|---|---|---|
| D1 | **The device is the hero.** Every sentence that names a feature, setting, button, number on the device or an action on it shows that thing on the real device, landed within ±5 f of the word | §1, §8.4, §2 |
| D2 | **Whip on the section change.** The hook ends in a whip into the device by 2.5 s. After that, whips mark section changes (a new item, a result, the reaction after a result) in either direction; inside an item every change is a hard cut | §6.2, §9.1, §9.2 |
| D3 | **One picture at a time.** Face or POV, full frame. No splits, no PiP, nothing stacked on the POV beyond its overlays (P-18, P-22, P-23, P-25, P-26, P-27) | §3.2, §2 |
| D4 | **Quiet type.** Captions are small, white, one line, never coloured. The only coloured text is the hook title (blue), the counter (red) and a verdict chip | §5 |
| D5 | **Count what you do.** A repeated action is counted on screen with the counter, which persists across cuts and never shows a number the footage hasn't earned | §8.6 |
| D6 | **Show the real thing.** The real device and its real screen, filmed by the creator. A drawn phone or a recreated screen appears only as a fallback, and it looks drawn, so nobody mistakes it for the device | §12.2, §8.5 |
| D7 | **The joke is on the creator's face.** Humour lands on a reaction shot or a line to camera, never in a meme sound | §8.8 |
| D8 | **End clean.** Last line → hard cut to black → the wordmark card builds in (≈ 14 f) and holds, ≤ 5 s in all; or a hard end ≤ 6 f after the punchline when there's no CTA | §6.7, P-30, P-32 |

### Quick index
| § | What |
|---|---|
| §1 | Procedure: how to approach a reel in this style (shot pairing is the craft) |
| §2 | Hard rules: the craft and the style's never-list |
| §3 | Worlds, layouts, stage moves, layout diagrams, safe zones, the person |
| §4 | Colour system: three colours, three jobs |
| §5 | Type and captions: the Title Stagger, CS-1 "quiet line" and rule CY, other text |
| §6 | Hook system: stopper test, HA-17 Device whip (H-A title whip, H-B question ring), alternates, hook pairs, title writing, CTA and the end card |
| §7 | Structure and rhythm: RS-LIST, RS-COUNT, RS-STORY, SM-COUNTER, the unit ritual, open loops, rhythm by feel |
| §8 | Visual system (B-roll and patterns): families B-1…B-12, P-01…P-34, line → pattern lookup, truth, the counter, anchors, comedy, assets |
| §9 | Transition system: T-WHIP, T-WHIP-S, T-WHIP-L and the cuts, grammar, shot grammar R-1…R-8, how the moves breathe |
| §10 | Motion tokens, camera and zoom Z-0…Z-5, layers, finishing |
| §11 | Sound |
| §12 | Footage handling: setups, shots and fallbacks, the POV capture checklist, inserts |
| §13 | What your plan should settle |
| §14 | Worked examples (3) |
| §15 | Your look at the storyboard: the checklist |
| §16 | Build notes: the title, the counter, the ring, the POV clip, the whip timeline |
| App. A / B | Evidence map / hook-title bank |

---

## §1 Procedure: how to approach a reel in this style

You watch, listen, plan, build and look at the storyboard yourself; the edit skill has the mechanics. This style's
craft is **shot pairing**: deciding, sentence by sentence, whether the viewer sees the face or the device, and which POV
take shows the exact thing being said. Get that right and the reel feels like holding the device yourself.

1. **Log the device footage.** Sort every clip by shot (§12.2): A-roll SH-1/3/4/8/9, POV SH-2/5/6, screen recording SH-7.
   For each POV clip write one line: what it shows (feature, setting, result), where the action starts and resolves (clip
   seconds), its still windows (≥ 0.5 s with the device not moving: the ring and tap anchors live there), and whether its
   UI text reads at 1080 × 1920. Contact sheets of each clip make this fast. Measure the device position in the hook shot
   and in every POV still window you'll annotate.
2. **Spell the glossary.** Every device, app and brand name exactly as its maker writes it (iPhone, AirPods, Wi-Fi, Wear
   OS). Personal identifiers on screen get masked in captions and blurred in the picture.
3. **Shape the talk.** `HOOK` (0 → the whip landing), `ITEM-n` (RS-LIST), `REP-n` (RS-COUNT), `TURN` (the result), `END`
   (reaction + CTA). Pick the shape (§7.1). Mark jump-cut points on pauses ≥ 150 ms at word boundaries.
4. **Pair every sentence with a picture.** Find its **trigger word**: the feature noun, the action verb, the number, the
   result word. A sentence that names a feature, setting, button, number on the device, or an action on it → **the
   device (POV)**, cut on that word. Opinion, reaction, joke, setup and transitions → **the face**. Then pick the POV take
   that shows that exact thing; if none exists, name the fallback (§12.2). A device moment that runs long gets a second
   take, an angle or a POV snap, so neither picture outstays its welcome.
5. **Feel the tone of each line:** `hype` (title, whip, counter tick) · `explain` (POV + captions only) · `awe` (the result
   full-bleed, a slow push, captions only) · `win` (a good verdict) · `warn` (a bad verdict) · `joke` (a reaction shot, at
   most a sticker; no meme sound) · `cta` (the end card).
6. **Write the hook** (§6): pick H-A (title whip) or H-B (question ring) from the footage, or an alternate; write 8–10
   titles, pick by the stopper test, keep two alternates; plan the whip landing by 2.5 s.
7. **Place the whips.** One at every section change, into the device or back out to the face; hard cuts everywhere else
   (§9.2). Choose each one's kind (zoom-flash, spin, linear) and its device point.
8. **Plan the graphics that point:** the count plan for RS-COUNT (label, every op and its frame, the finale; §8.6), the ring
   and ripple anchors from the still windows (§8.7), the caption height for the whole reel (rule CY, §5.3), the
   third-party moments (§12.5) and the end card (§6.7).
9. **Plan the sound** (§11): a cue on the hook, on every whip, on the reveals and on the counter; cuts and step punches
   silent.

---

## §2 Hard rules: the craft and the style's never-list

**Craft, by eye** (judge it on the storyboard, in context, the way an editor does):
- **Keep the person clear.** People come for the face, so keep it, the hair and the room above the head clear of front
  layers when the moment is about them. The framing that does it: on the face shot everything this style draws sits low
  (the title, the counter, the captions, the verdict chip, the bubble) or beside the face (the sticker); a ring or bubble
  keeps 40 px clear of the head region, and a ring on a device held next to the face is skipped. When the moment wants
  otherwise (a caption crossing the chin for a beat), that's editing; what's never fine is a head chopped or a face buried
  by accident. The geometry is in §3.7.
- **No text over text.** The title and the captions never share the hook frame when the title repeats the spoken line
  (captions hide under it); the title and the counter never share a frame; graphics stay out of the caption band
  (cy ± 72) while captions show; one overlay on a POV at a time.
- **On the word.** A POV cut lands 2 f before its trigger word and is fully on within ±5 f; a counter tick lands within
  ±3 f of the repetition's result appearing on screen (or of the spoken number, when it's spoken). Cuts sit on word
  boundaries ±1 f; the audio is never offset; the A-roll voice runs continuously under every POV insert.
- **Say what was said.** The counter counts real repetitions in the footage; a spec or number the reel claims comes from
  the script or the device's own screen; no invented benchmarks or ratings presented as real. Furniture inside a recreated
  screen may use made-up but realistic values, no label.
- **Promise integrity.** A count in the title equals the items shown; a "can it…?" title is answered on screen by the TURN;
  the counter's final value equals the last repetition shown; the CTA keyword is on screen ≥ 1.5 s.
- **Spelling.** Device, app and brand names exactly as their makers write them, in captions and chips.
- **Readable.** Captions 56 px with their 3 px black outline; when UI text is the point, the device screen fills ≥ 45 % of
  frame height for ≥ 1.0 s, or a P-27 loupe or a P-22 chip carries it. Text holds ≥ 0.25 s per word.
- **Privacy.** Notifications, contact names, phone numbers, emails and account ids on a device screen are blurred for their
  whole time on screen, unless they're the creator's own demo data.
- **Audio.** −14 LUFS integrated, true peak ≤ −1.5 dBTP, the bed ≥ 18 dB under the voice, a hard end ≤ 6 f after the last
  word (CTA `none`), no black tail over 0.2 s, an end card never over 5 s.

**Never in this style:**
- A split screen, a PiP bubble of the face, a card stacked over the POV beyond its overlays.
- Coloured, enlarged or bold words inside captions; chunky or kinetic word-stack captions; captions that move height
  mid-reel.
- A title anywhere but the hook, or a second title.
- A whip inside an item (setup → POV of the same feature after the first, POV → POV, rep → rep): those are hard cuts.
- Stock footage, manufacturer promo clips or renders of the device. The creator's own POV only.
- A drawn phone or a recreated UI presented as the real device.
- Meme sounds; a sticker or any comedy mark on the device screen (the only marks on the device are the ring, the tap
  ripple and the loupe).
- Regrading, tinting or stylising the POV: the device's real screen colours are the content.
- Captions sitting on the UI that's being read: choose the caption height for the reel (rule CY) and nudge the POV
  framing (`focus`, ≤ 80 px) instead.
- Decorative graphics: lens flares, light leaks, RGB splits, particle bursts, emoji rain.

---

## §3 Worlds, layouts, stage moves, safe zones

### 3.1 Worlds
| ID | Kind | Look | Carries | Enter / exit |
|---|---|---|---|---|
| **W-studio** | `footage` | The creator's own set: warm or coloured practicals, deep shallow-focus bokeh (f/1.8–2.8), the presenter sharp. The background colour comes from the footage (an amber library in v02, an RGB room in v01, a daylight garden in v03); base `#000000` | A-roll: claims, opinions, reactions, setup | Hard cut; the whip leaves it |
| **W-void** | `void` | `#000000` under the full-bleed POV clip and the end card | POV inserts (drawn as P-06/P-07 scenes over it), end card | A whip or T-CUT in and out; a hard cut to black into the end card |
| **W-blur-set** | `footage` (blur 36 px, brightness 0.55, pad 40) | The A-roll itself, blurred and darkened | Fallback only: the drawn phone of P-11 (FB-1/FB-2) | `dim` stage move, 8 f |

The set is never replaced, matted or regraded. Its colour is whatever the creator shot.

### 3.2 Layout library
| ID | Engine | Presenter | Graphic | Caption |
|---|---|---|---|---|
| **L-full** | `full` | Full frame 1080 × 1920, head top y 160–320, face x 300–780 | none (title, counter, chips over it) | CS-1, cy 1400 (or 1270 by rule CY) |
| **L-pov** | `hidden` | none (absent) | The POV clip full-bleed (x 0, y 0, 1080 × 1920) as a z1 plate scene | CS-1, cy 1400 (or 1270) |
| **L-device-dim** | `full` + `dim {blur_px: 18, luma: −0.35}` | Full frame, blurred and dimmed | Drawn phone x 250, y 260, w 580, h 1060 (P-11) | CS-1, cy 1400 (or 1270) |
| **L-endcard** | `hidden` | none | End card (P-32) on W-void, x 0, y 0, 1080 × 1920 | none |

**How the two pictures trade places.** L-full and L-pov alternate: the device comes in on the trigger word, the face comes
back on the sentence boundary. People come for the creator *and* the device, so the reel keeps handing the screen back
and forth; neither ever sits long enough to go stale.

**Why L-pov is `hidden`, not a card:** the POV clip covers the whole frame, so the presenter footage is switched off for
that span and the clip is drawn as a scene (`VEOS.fx.clip` or the `pov()` block of §16, a z1 plate, full-bleed,
`kind: "broll"`, `continuous: true`; z1 so the footage blur of a whip reaches it). When the creator spoke the line *while*
filming the POV (voice recorded on that take), cut the take into the EDL as its own segment instead: the stage stays
`full` and the beat carries `shot_id`.

### 3.3 Stage moves
| ID | Move | Recipe (30 fps) | Use |
|---|---|---|---|
| **G-1** | **Whip-in** | T-WHIP / T-WHIP-S / T-WHIP-L (§9.1) with stage `cut` to L-pov on the landing frame | The hook; the first POV of a new item |
| **G-2** | **Hard return** | T-CUT: stage `cut` to L-full on the first word of the opinion or reaction sentence | Returns to the face inside an item |
| **G-2b** | **Whip-out** | T-WHIP (zoom on the POV, flash, land on the face) or T-WHIP-L / T-WHIP-S, stage `cut` to L-full | After a result, or POV → the next item's setup (v02 @ 17.9, 24.4, 29.8; v03 @ 7.9, 37.9) |
| **G-3** | **POV → POV** | T-CUT between two POV takes (a new action, angle or macro), or a step punch (P-21) on the same clamp shot | A device moment too long for one take; each repetition in RS-COUNT |
| **G-4** | **Dim to device** | `via: dim` 8 f: the A-roll blurs and darkens while the drawn phone rises over 10 f (P-11) | Fallback FB-1/FB-2 only |
| **G-5** | **Cut to end** | Hard cut to black (P-30) on the last word's end, stage `cut` to L-endcard, the card builds in (§6.7) | The end card |

### 3.4 Layout diagrams
**L-full, hook (H-A title whip):**
```
┌─────────────────────────┐ 0
│  (IG top UI, keep clear)│ ← y 0–110
│        ╭──────╮         │
│   face │device│ (soft)  │ ← device held up 30–40 cm from the lens, y ≈ 280–1200
│  (soft)│ held │         │   face soft behind it (f/2); device bottom above y 1210
│        ╰──────╯         │
│   WHAT THEY             │ ← TITLE phrase, cy 1340, one line, max_w 952, pops in (2 f, blur)
│                         │   (captions hidden until the whip lands)
│                         │
│ (IG bottom UI: y > 1540)│
└─────────────────────────┘ 1920
```
**L-full, body:**
```
┌─────────────────────────┐ 0
│                         │ ← y 0–110 clear; the room above the head stays empty
│        (head top        │ ← head top y 160–320, face x 300–780
│         y 160–320)      │
│          FACE           │
│     torso + device      │ ← the device in hand for most of the face time
│      Reframes: 7        │ ← counter cy 1280 (= caption cy − 120), RS-COUNT only
│  small white caption    │ ← CS-1 cy 1400 (low), or 1270 (mid; the counter then at 1150)
│                         │
│ (IG bottom UI: y > 1540)│
└─────────────────────────┘ 1920
```
**L-pov:**
```
┌─────────────────────────┐ 0
│   setting chip (P-22)   │ ← chips cy 250 (top band), POV only
│     ╭───────────╮       │
│     │  SCREEN   │       │ ← device screen 40–65 % of frame height,
│     │  (UI)     │       │   centre x 380–700, centre y 700–1000
│     │           │       │
│     ╰───────────╯ hand  │ ← hand and wrist from a bottom corner
│  small white caption    │ ← cy 1400: UI to read stays above y 1340
│                         │
└─────────────────────────┘ 1920
```
**L-device-dim (fallback):**
```
┌─────────────────────────┐ 0
│ (A-roll blurred 18 px,  │
│   luma −0.35)           │
│      ╭──────────╮       │ ← drawn phone x 250–830, y 260–1320, tilt −6°, float ±6 px
│      │ recording│       │
│      ╰──────────╯       │
│  small white caption    │ ← cy 1400
└─────────────────────────┘ 1920
```
**L-endcard:**
```
┌─────────────────────────┐ 0
│  artwork band y 0–330   │ ← the creator's artwork, else the created band (P-32)
│                         │
│      YOURNAME           │ ← wordmark cy 860, Barlow Condensed 700 caps, fit to ≈ 820 px wide, white
│                         │
│  ╭ Comment KEYWORD ╮    │ ← CTA chip cy 1180 (comment_keyword / link_bio)
│  bottom band y 1000–1500│
└─────────────────────────┘ 1920
```

### 3.5 Safe zones and bands
- Meaning text stays inside x 64–1016, y 110–1500: nothing in y > 1540, nothing in the right 110 px between y 900 and
  1540 (Instagram's buttons).
- **Caption band:** cy 1400 (`low`) or 1270 (`mid`), one line, ~63 px tall. Graphics stay out of cy ± 72 while captions
  show.
- **Counter band:** cy = caption cy − 120 (1280 or 1150), ~86 px tall.
- **Title band:** cy 1340 (measured v02 @ 0:00.4–1.0), hook only; captions are hidden while it shows (H-A).
- **Chip band:** cy 250, POV only. Verdict chips use the counter band when no counter is on screen.
- **Bubble band:** y 1060–1300 on L-full (above the low caption band with ≥ 40 px of air); with caption height `mid` the
  bubble moves to y 860–1100.

### 3.6 Which picture, when
- The face carries setup, opinion, reaction and the joke; the device carries everything you can point at. A face run lasts
  as long as the thought; a POV lasts as long as the action takes to complete and read.
- The return to the face is a hard cut on the first word of its sentence (G-2), or a whip-out after a result (G-2b).
- The A-roll stays as shot: 9:16 vertical, the same framing across jump cuts (no punch reframes; a Z-3 snap only on a
  joke).
- The device is in the creator's hand for most of the face time: it tells the viewer the face and the POV are the same
  moment.

### 3.7 The person
- **L-full (the face):** full frame, head top y 160–320, face x 300–780; the room above the head (y 110 up to the head top)
  stays empty. Everything drawn on the face shot sits well below the chin: the title band cy 1340 (hook only), the counter
  at cy 1280 or 1150, the caption band at cy 1400 or 1270 (56 px), the verdict chip in the counter band, the bubble in
  y 1060–1300 (or 860–1100 with the `mid` caption height). If a creator sits so low that the bubble would touch the chin,
  it goes on the POV instead. The sticker sits beside the face at shoulder height, off the face and hair unless the joke
  is aimed right at it.
- **Top-of-frame graphics belong off the face shot.** The setting chip (cy 250) and the notification drop (y 150–330)
  live on the POV or the dimmed set, where no head is on screen; a sponsor's "Paid partnership" label at x 64, y 140 goes
  on a POV shot of the sponsor's product.
- **The ring and the ripples** sit on the device. When the device is held next to the face and the ring's box (+14 px)
  would reach within 40 px of the head, skip the ring.
- **The hold-up hook** puts the device in front of a soft face on purpose: that's footage, not a layer. The title sits
  under the device, never over the face or the device screen.
- **L-pov and L-endcard** have no presenter. **L-device-dim** blurs (18 px) and darkens the A-roll into a backdrop, which
  the engine treats as no face on screen, so the drawn phone may sit over the blurred figure; the moment the face is sharp
  again, keep it clear.
- **No cut-out** (`matte: none`). Behind the person is fair game in principle; this style simply has no layer there.

---

## §4 Colour system

### 4.1 Role palette
| Role | Hex | One job | Text on it |
|---|---|---|---|
| `primary` | `#1570C8` | The hook's blue (sampled mid-letter on the reference title, v02 @ 0:00.6): the end-card keyword chip, and the family the title gradient lives in | `paper` |
| `accent` | `#D80018` | The running counter label (sampled v03 @ 0:06) | `paper` |
| `highlight` | `#4FE1FF` | The neon ring sweep on the device, tap ripples | `ink` |
| `bad` | `#D92D20` | "FAILS / NOPE" verdict chip | `paper` |
| `good` | `#1A7F38` | "WORKS / PASSED" verdict chip | `paper` |
| `title_top` | `#4A9BE8` | The light top of the title (a lighter tint of `primary`) | — |
| `title_shadow` | `#06143D` | The title's hard extrusion | — |
| `counter_stroke` | `#4A0610` | The 3 px stroke around the counter | — |
| `ink` | `#0B0B0F` | Text on chips and bubbles | — |
| `paper` | `#FFFFFF` | Captions, the title stroke, bubbles, the wordmark | — |
| `bubble_text` | `#2C2C30` | Message-bubble body text | — |
| `night` | `#000000` | End card, POV underlay | — |

Gradients (tokens `gradients`): **`title`**, top to bottom `#5AA2FF` → `#1A64FF` → `#1450D6`, the fill the title is built
with (§16 reads it from tokens); **`endcard_band`**, `#1A64FF` → `#0A1A4A` → `#000000`, the created end-card band when the
creator has no artwork. A creator's brand colours can replace `primary` and `accent` (the counter red) in their copy;
`title_top` stays a lighter tint of `primary`, `title_shadow` a very dark shade of its hue, and `counter_stroke` a very dark
shade of `accent`. `good` and `bad` never change.

### 4.2 Meanings
- **Blue = "watch this":** only the hook title and the CTA keyword.
- **Red = the count:** only the counter label. Red never means "bad" outside the verdict chip.
- **Cyan = "look here on the device":** only the ring and tap ripples, always on the device.
- **Green / red verdicts** are the only good/bad axis, and only as chips.
- Other companies' brand colours appear only inside the creator's own footage (their device, their UI).

### 4.3 Rules
- The blue title, the red counter and the cyan ring each own a moment; they're never all on screen together. The title is
  hook-only, and the title and the counter never share a frame.
- The title is never drawn without its white stroke and extrusion (it sits on busy footage); the counter never without its
  dark stroke.
- No grade, no LUT, no tint, no black-and-white event. The look is made at the shoot (warm practicals, shallow depth of
  field, a sharp presenter). Match exposure and white balance between the A-roll and the POV; nothing else.

---

## §5 Type and captions

### 5.1 Font map
| Slot | Family | Weight / style | Used for |
|---|---|---|---|
| `display` | **Montserrat** | 900 italic, caps | The hook title (P-01) |
| `body` | **Poppins** | 600 | Captions (CS-1) |
| `label` | **Poppins** | 700 | Counter label, setting chips, verdict chips, CTA chip (keyword 800) |
| `numeric` | **Poppins** | 700, tabular figures | Counter digits |
| `ui` | **Inter Tight** | 500 / 700 | Message bubbles, notification drops, recreated UI, the paid-partnership label |
| `wordmark` | **Barlow Condensed** | 700 caps | End-card wordmark |

All are bundled OFL fonts. A creator's logo is an image asset, never a font. The reference fonts couldn't be identified
exactly; these are the closest bundled matches to the measured shapes (App. A).

### 5.2 The headline element: the Title Stagger (P-01)
Kind `lockup` (one line at a time), lifetime `hook`. It is the whole hook's typography and it never comes back.

| Property | Recipe |
|---|---|
| Text | The hook title (a promise the reel keeps; it may repeat the spoken hook line or say it better), ALL CAPS, **2–3 phrases of ≤ 3 words**, ≤ 9 words in all, 0 emoji. Digits for numbers |
| Type | Montserrat 900 italic, **76 px**, line height 1.0, tracking +0.01 em, one line per phrase, centred on cx 540, max width 952 px; a phrase that measures wider shrinks to ≥ 68 px, else it's split (measured: "DON'T TELL YOU" 686 px wide, cap 56 px, v02 @ 0:00.6) |
| Fill | The vertical `title` gradient (`#5AA2FF` → `#1A64FF` at 55 % → `#1450D6`), clipped to the glyphs |
| Stroke | 3 px `paper` outside the glyphs (draw a 6 px stroke with `paint-order: stroke fill`) |
| Extrusion | Hard, no blur, out to (+4, +6) px in `title_shadow`: `2px 3px 0` + `4px 6px 0`, plus a soft `0 8px 18px rgba(0,0,0,.35)` |
| Position | cy **1340** (measured v02 @ 0:00.1–1.3), below the held-up device. Frame SH-3 so the device's bottom edge sits above y 1210 (C-9); never over the device screen |
| Entry ("pop") | Phrase 1 appears on **f1–f2**: scale 0.70 → 1.00 about its centre, a horizontal motion blur 12 → 0 px, opacity 0.5 → 1, expo-out; sharp on f3 (v02 @ 0.067–0.10). It lands while the Z-4 open punch is still running |
| Swap | A **2 f blurred crossover**: the old phrase fades 1 → 0 while the new one pops 0.85 → 1.00 with a 10 px horizontal blur; both are on screen for 1 f (v02 @ 0.30–0.37, 0.70–0.73). Each swap is a declared scene `event`. No slide, no ghost trail |
| Timing | Phrase k enters 2 f before its first spoken word, but never before the previous phrase has held 0.25 s × its words; the whole title reads in ≤ 2.25 s (the source swaps faster, 0.23–0.4 s a phrase; the hold wins) |
| Life | No pulse, no drift. The title is the whole hook |
| Exit | None of its own: it stays up to the whip and is blurred away with the frame (scale 1 → 1.5 about the device point + opacity 1 → 0 over the whip's 3–4 out-frames). Never a pop mid-word |
| Captions | Hidden from f0 until the whip lands (`captions.hide: [[0, t_whip_cut]]`) when the title repeats the spoken hook line; a title in its own words leaves the captions on |

### 5.3 Caption system: CS-1 "quiet line"
`extends: "lib:mrwhose"`, tuned to the measured frames. Small, white, one line, at one height for the whole reel. It
serves the picture and never competes with it.

| Group | CS-1 |
|---|---|
| Mode | `full` / `support` / `mute_safe`: every spoken line is captioned |
| Chunking | `unit: line`; **3–6 words** a chunk; `max_chars_line` 30; **1 line**; never split a name, number or unit; a sentence end always breaks (`punct_break`); a pause ≥ 0.9 s always breaks |
| Timing | Lead 2 f before the first word; hold ≥ 0.25 s per word; **hard swap** (0 f; the reference swaps straight); `pause_hold_s` 0.6 (the last chunk stays up through a short pause, then clears); tail 0.12 s after the last word |
| Skin | Poppins **600**, **56 px**, `TC-subtitle`, sentence case (as spoken), tracking 0, line height 1.12, `paper` white, a clearly visible 3 px `#000000` outline under the fill + shadow `0 3px 10px rgba(0,0,0,.6)`; no container (measured: "Can your iPhone" 473 px wide, v03 @ 0:00.5) |
| Position | `fixed_y`, cx 540, max width 952, centred; **cy set once for the reel** by rule CY: **1400 (`low`, default)** or **1270 (`mid`)**; `avoid_face` on |
| Emphasis | **None.** No colour, no bold, no size change |
| Hide | Under z8 scenes; on the 3 peak frames of a T-WHIP; during the H-A title (timeline `captions.hide`); during the end card |
| Language | Latin script; `keep_english_terms`; spelling normalised to the glossary (device and app names exact); profanity masked `inner` (S**T) |

**Rule CY (the caption height for the reel).** Take the middle frame of every POV clip used in a beat where UI text must
be read, plus every SH-5 clamp shot. For each candidate (`low` 1400 / `mid` 1270), add up the beat time in which the
caption band (cy ± 40 px) or the counter band (cy − 120 ± 45 px, RS-COUNT only) overlaps (a) UI text being read, (b) the
finger's tap point, (c) the device's own controls in use. Pick the candidate with less overlap; on a tie, `low`. Write it
once as a token patch, `plan/tokens.override.json` → `{"patch": {"captions.profiles.CS-1.position.cy": 1400}}` (range
1240–1440), and in the reel header as `caption_y`. The height never changes inside a reel.

Measured reference: the reference captions sit at y ≈ 1607 (v02) and ≈ 1273 (v03). 1607 is inside Instagram's bottom
band, so `low` is lifted to 1400; `mid` keeps the v03 placement.

### 5.4 Other text
| System | Class | Recipe | Hold |
|---|---|---|---|
| **Counter label** (P-18) | TC-display | "{Label}: {n}", Poppins 700 **80 px**, `accent` fill, 3 px `counter_stroke` stroke + `0 3px 8px rgba(0,0,0,.45)`; centred cx 540, cy = caption cy − 120; a fixed-width box sized for "{Label}: 888" so the rect never moves (measured: "Reframes: 1" 474 px wide, cy 1158, v03 @ 0:06) | From the first counted repetition until 8 f before the result climax (P-12) or the end |
| **Setting chip** (P-22) | TC-label | `paper` pill at 94 % opacity, `ink` Poppins 700 **44 px**, radius 22, padding 10 / 26; cy 250 on the POV | ≥ 1.2 s |
| **Verdict chip** (P-25) | TC-label | "WORKS ✓" on `good` / "FAILS ✕" or "NOPE" on `bad`, `paper` Poppins 700 caps **48 px**, radius 24, padding 12 / 30 | ≥ 1.0 s |
| **Message bubble** (P-23) | TC-label | White bubble, radius 34, max width 640, `bubble_text` Inter Tight 500 **42 px** (key noun 700), avatar Ø 112 with a 4 px white ring, meta "Name · 10:37" Inter Tight 600 26 px at 80 % white under the bubble's right edge | ≥ 2.0 s and the whole spoken line |
| **Notification drop** (P-24) | TC-label | Rounded 36 px banner, `#1C1C1E` at 88 %, a generic app glyph, title Inter Tight 700 40 px + body 500 40 px, white | ≥ 1.5 s |
| **End-card wordmark** (P-32) | TC-display | The creator's name in Barlow Condensed 700 caps, fit to ≈ 820 px wide (110–200 px), white, cy 860, no tracking | The end card (≤ 5 s) |
| **CTA chip** (P-33) | TC-display | "Comment" Poppins 700 48 px white + the keyword in a `primary` chip, Poppins 800 caps 64 px, `paper` text, radius 20 | ≥ 1.5 s |
| **Paid-partnership label** | — | Inter Tight 600 caps 24 px, tracking 0.08 em, white at 80 % | ≥ 2.0 s at the sponsor's first mention |

### 5.5 Language and numbers
- Captions are the creator's speech, verbatim, in their language (`en` by default). Hinglish captions stay romanised;
  English terms stay as spoken. A Hindi speaker's captions follow their copy's setting.
- The title is ALL CAPS in Latin script: Devanagari has no italic caps, so a Hindi or Hinglish speaker gets an English or
  romanised title.
- Device, app, setting and brand names are spelled exactly (the glossary). Product names keep their maker's case (iPhone,
  not Iphone).
- Numbers: digits on screen ("600", "20"), international grouping (1,200), `$` by default (an Indian creator gets ₹ and
  Indian grouping when their copy says so). Specs keep their units with a thin space ("5 mm", "120 Hz").
- The counter label is one noun in title case, ≤ 12 characters ("Reframes", "Batches", "Drops", "Tries", "Washes").

---

## §6 Hook system

**The hook title** promises the viewer something about the device in their hand: a secret ("what they don't tell you
about your phone"), a test ("can your phone actually…?"), a limit, a mistake they're making. It doesn't have to repeat the
spoken words; it has to be true to what the reel delivers. A title shown as someone's words (in quotes) is word for word.
Write 8–10 candidates from the formulas in §6.5 and the proven shapes ("How to X as a Y", "Why your X isn't working", "The
X nobody tells you", "Stop doing X", "Your X vs mine", a number, a contrast), score them on outcome, curiosity, who it's
for and brevity, check the best against the stopper test, pick one, and keep the next two as alternates.

Frame 0 always shows the device (in hand, held up or on its clamp, ≥ 15 % of frame height) **and** the question or title
(title phrase 1 entering, or the first caption chunk at f0), with something already moving. And the hook always ends in a
whip into the device: the whip starts by 2.2 s and its cut into the POV lands by **2.5 s** (measured 1.33 s in v02, 2.53 s
in v03); 2.7 s at the very latest when the spoken title runs long, and then the title drops to 2 phrases. Even when the
body's first POV comes later by a hard cut, the hook's first entry into the device is a whip.

### 6.1 The stopper test
| Test | In this style |
|---|---|
| Thumbnail | f0 at 25 % scale: the device is recognisable and the title phrase (76 px → 19 px) or the first caption chunk reads |
| Mute | By 3 s, without sound: a device + a question or claim about it + the whip into it |
| Motion at f0 | The device swinging in (H-A) or the presenter leaning to the device (H-B), plus the Z-4 open punch, the title pop or the ring sweep |
| Read time | A title of ≤ 9 words reads in ≤ 2.25 s at 0.25 s a word; a question chunk (3–6 words) in ≤ 1.5 s |
| Payoff | The whip into the device by **2.5 s** |

The first three seconds feel dense: the punch, the phrases swapping, the ring running up the device, the whip. Dense in
time, never in space: one phrase on screen at a time, each landing while the last one settles.

### 6.2 HA-17 Device whip (default)
Two variants of the engine's HA-17 Device whip (tokens `hooks.variants`: H-A = `HA-17.A`, H-B = `HA-17.B`;
`meta.hook_archetype` stays `HA-17`). Pick by the footage: **H-A** when an SH-3 hold-up exists and the spoken hook is a
line of ≤ 9 words; **H-B** when the device sits on a clamp (SH-4) or the hook is a question longer than 9 words.

**H-A "Title whip"** (spoken: "What they don't tell you about your phone." ≈ 2.0 s)

| t (s) | Frame | Visual | Title / captions | Layout / camera | Cue moment |
|---|---|---|---|---|---|
| 0.00 | f0 | SH-3: the device swinging toward the lens (live, motion-blurred), face soft behind | — | L-full; Z-4 `crash-zoom` 1.0 → 1.4 over f1–f5 (ease-out), held to the whip | **hook**: one cue on the punch + title |
| 0.03–0.10 | f1–f3 | The punch runs; the device fills ≥ 30 % of frame height by f12 | P-01 phrase 1 "WHAT THEY" pops in at cy 1340 (f1–f2), sharp f3 | — | — |
| 0.40–0.70 | f12–f21 | P-03 sweep up the device outline (only when the device is still from f9; otherwise skip it) | — | — | reveal (optional) |
| 0.50 | f15 | — | Phrase 2 "DON'T TELL YOU" (2 f crossover) | — | — |
| 1.25 | f38 | — | Phrase 3 "ABOUT YOUR PHONE" | — | — |
| 2.00 | f60 | T-WHIP-S (default with a hand-held device) or T-WHIP: Z-5 roll / Z-1 zoom, blur pass; the title blurs away with the frame | — | camera | **transition**: whip cue |
| 2.17–2.27 | f65–f68 | Cut: stage L-pov; the item-1 POV clip lands blurred and settles over 3 f | Captions resume on the first sharp POV frame | T-WHIP-S marker, stage cut | — |
| 2.27–4.5 | | Item 1 on the device (P-06 + P-10 push) | CS-1 chunks | L-pov | — |

The source lands the whip at 1.33 s (v02); land it as early as the spoken title allows.

**H-B "Question ring"** (spoken: "Can your phone actually see the back of your head?" ≈ 2.3 s)

| t (s) | Frame | Visual | Captions | Layout / camera | Cue moment |
|---|---|---|---|---|---|
| 0.00 | f0 | SH-4: the presenter lunging in toward the device on its clamp (live) | Chunk 1 "Can your phone" at f0 | L-full | **hook**: one cue on the sweep (0.3 s) |
| 0.30–0.60 | f9–f18 | P-03 sweep runs up the device outline (`kind: "device"`) once the presenter has settled (v03 @ 0.30–0.57) | — | — | — |
| 0.83 | f25 | — | Chunk 2 "actually see" | — | — |
| 1.30 | f39 | The presenter presses the device: P-26 tap ripple at the touch point | — | — | — |
| 1.67 | f50 | — | Chunk 3 "the back of your head?" | — | — |
| 2.20 | f66 | T-WHIP: Z-1 `zoom-through` 1.0 → 1.6 over 7 f about the device + P-05 radial blur + the flash lift (v03 @ 2.47–2.74) | (hidden across the 3 peak frames) | camera | **transition**: whip cue |
| 2.47 | f74 | Cut to SH-5: the clamped device full frame, finger tapping | Chunk 4 "So using the new…" | L-pov, T-WHIP marker | — |

Something new arrives every second of this hook (the ring, a chunk, the ripple, the next chunk, the whip), each one with a
reason in the words.

### 6.3 Alternate hooks
**HA-02 Headline + proof.** Use when the *result* is the hook ("this is what 20 edits do to a photo").

| t | Visual | Text | Payoff |
|---|---|---|---|
| f0 | SH-3 hold-up with the result **already on the device screen** (scene `kind: "device"` on the ring or `satisfies: ["proof"]` on the title) | P-01 phrase 1 | — |
| 0.4–1.9 | Sweep up the device; phrases 2–3 | P-01 | — |
| ≤ 2.3 | T-WHIP into the result full-bleed (P-12, short) | captions resume | proof ≤ 2.5 s |

For example: "THIS PHOTO / WAS EDITED / 20 TIMES".

**HA-10 Host flash → subject.** Use when the device action needs no setup and is fast (a 2-second trick).

| t | Visual | Text | Payoff |
|---|---|---|---|
| f0 | A-roll mid-gesture toward the device | Chunk 1 at f0 | — |
| ≤ 0.7 | T-WHIP (6 f version) or T-CUT into the POV of the action | captions continue | subject full frame ≤ 0.7 s |

For example: "Hold the space bar." → POV thumb on the keyboard at 0.6 s.

**HA-14 Cold authority.** Use for RS-STORY (one device moment told as a story).

| t | Visual | Text | Payoff |
|---|---|---|---|
| f0 | A-roll mid-sentence with the device moving in hand (v01 @ 0:00) | Chunk 1 at f0 | — |
| ≤ 1.0 | The strongest image: the device held up to the lens, or the POV of the message or result | captions continue | ≤ 1.0 s |
| ≤ 3.0 | First T-WHIP into the device | — | — |

For example: "So my phone did something weird last night."

### 6.4 Hook pairs by topic (subject → reveal)
| Topic | First subject (f0) | The reveal (by) | Variant |
|---|---|---|---|
| Phone keyboard trick | Phone held up; "WHAT THEY / DON'T TELL YOU / ABOUT YOUR PHONE" | POV: thumb holds the space bar, the cursor glides (2.3 s) | H-A |
| Burst-photo limit | Phone on a clamp, ring; "How many photos can one burst take?" | POV: shutter held, the burst number climbing (2.5 s) | H-B |
| AI photo edit pushed to the limit | Phone on a monopod, ring | POV: edit 1 result; counter "Edits: 1" (2.5 s) | H-B (RS-COUNT) |
| Battery-health myth | Phone held up; "STOP CHARGING / YOUR PHONE / LIKE THIS" | POV: the battery settings screen (2.3 s) | H-A |
| Air fryer hidden button | Fryer on the counter, presenter beside it; "THE AIR FRYER / BUTTON NOBODY / PRESSES" | POV: finger long-presses, the display changes (2.3 s) | H-A |
| Blender ice test | Blender on the counter, ring; "Can a 30-dollar blender crush ice twenty times?" | POV top-down into the jar, batch 1 crushed; "Batches: 1" (2.5 s) | H-B (RS-COUNT) |
| Milk frother trick | Frother held up; "YOU'VE BEEN / FROTHING MILK / WRONG" | POV: the wand angle that makes foam (2.3 s) | H-A |
| Knife sharpener test | Sharpener held up, ring | POV: a paper slice after pass 1; "Passes: 1" (2.5 s) | H-B (RS-COUNT) |

### 6.5 Title writing
**Formula:** `[setup] / [twist] / [the device]` in 2–3 phrases of ≤ 3 words, ALL CAPS, ≤ 9 words: a promise true to the
reel (it need not be the spoken hook line). The device (or its category) is named in the last phrase.

| Template | For example |
|---|---|
| **Secret** (default) | WHAT THEY / DON'T TELL YOU / ABOUT YOUR {DEVICE} |
| **Can it** | CAN YOUR {DEVICE} / ACTUALLY / {DO X}? |
| **Limit** | I PUSHED / {FEATURE} / TO THE LIMIT |
| **Stop** | STOP USING / YOUR {DEVICE} / LIKE THIS |
| **Count** | {N} {DEVICE} TRICKS / YOU NEVER USE |
| **Wrong** | YOU'VE BEEN / USING {X} / WRONG |
| **Price** | THE {PRICE} {DEVICE} / THAT BEATS / {RIVAL} |

- Write 8–10, pick by the stopper test (thumbnail, read time, mute), keep two alternates.
- **Banned:** "INSANE", "MIND-BLOWING", "YOU WON'T BELIEVE", emoji, a count the reel doesn't deliver, a claim the footage
  doesn't show.

### 6.6 Hook sound
One cue on the title entry or the ring, one on the whip; the music bed enters on the whip landing (§11).

### 6.7 CTA and the end card
| Device | Spoken pattern | On screen | Hold | Silence before |
|---|---|---|---|---|
| `end_card` (default) | none needed; the last line is the reaction | P-30 cut to black → P-32 wordmark card | 2.5–4.0 s | 1.0 s with no cue before the card |
| `comment_keyword` | "Comment KEYWORD and I'll send you …" | P-32 + P-33 keyword chip | keyword ≥ 1.5 s | 1.0 s |
| `link_bio` | "It's linked in my bio." | P-32 + a "Link in bio" chip (P-33 recipe, no keyword) | ≥ 1.5 s | 1.0 s |
| `none` | — | Hard end ≤ 6 f after the last word, on a reaction | — | — |

The CTA device, the keyword and the wordmark (the creator's name) come from the creator's copy.

**The end card (P-32), built:**
- **Enter (T-BLACK):** a hard cut to black 2 f after the last word ends (no fade; v01 @ 22.42), ≤ 3 f of pure black, then
  the card **builds in over ≈ 14 f**: the wordmark letters appear left → right, each smearing in from a horizontal blur
  (16 → 0 px, 3 f each, 1 f stagger), while the artwork bands fade and rise 20 px (v01 @ 22.47–22.90).
- **Layout:** W-void black. Wordmark = the creator's name in Barlow Condensed 700 caps, fit to ≈ 820 px wide (110–200 px),
  white, cy 860, no tracking. Top artwork band y 0–330 and bottom band y 1000–1500: the creator's own artwork or logo
  (`origin: creator`); without it, the created band: the `endcard_band` gradient with 9 seeded angular shards in
  `primary` at 30–60 % opacity drifting 20 px/s (deterministic: seeded from the frame number).
- **CTA line** (cy 1180): `comment_keyword` → P-33 "Comment" + keyword chip; `link_bio` → "Link in bio" chip; `end_card`
  alone → no line.
- **Hold:** 2.5–4.4 s after the build, ≤ 5.0 s in all (v01 ≈ 4.9 s); the keyword ≥ 1.5 s.
- **Exit:** the wordmark stretches sideways with a horizontal smear while the card zoom-blurs (1.0 → 1.5) and darkens to
  black over 5 f, then a hard end (v01 @ 27.17–27.37).
- `kind: "end-card"` on the card scene; `kind: "cta-keyword"` on the keyword chip.

**Sponsored reels:** the sponsor's product is filmed like any device (POV); a "Paid partnership" label (§5.4) at x 64,
y 140 on the first POV shot of the product, for ≥ 2 s at the first mention, plus the spoken disclosure. The sponsor's logo
appears only on the end card's top band: the sponsor's own file, else the real logo fetched from their site.

---

## §7 Structure and rhythm

### 7.1 Structure: a list, in three reel shapes
One format, F-A "Device Whip", carries every reel. The structure is `list`; the reel header declares its shape
(`structure.shape`).

| Shape | Arc | When | Evidence |
|---|---|---|---|
| **RS-LIST** | hook → items (2–5) by the ritual → best item last → reaction → END | Hidden features, settings, tips, "N things" | v02 (five tricks, no numbering) |
| **RS-COUNT** | hook (question) → setup (what is counted, rep 1) → reps 2…N with the counter → re-hook "let's push it" → TURN (the result held) → reaction → END | "Can it do X?", stress tests, "how many times…" | v03 (Reframes 1 → 20) |
| **RS-STORY** | cold line with the device in hand → the moment on the device (message, result) → context → payoff → END card | One device moment, an invite, an unboxing story | v01 (a message, the wide shot, the end card) |

RS-STORY is a list of one item.

### 7.2 Markers
- **RS-LIST: spoken only.** No numbers on screen; each item opens with the cut into the device on the feature noun. The
  order words ("next", "and this one") are spoken, not shown.
- **RS-COUNT: SM-COUNTER.** The counter label (P-18) is the marker and the structure; numbering ascends (§8.6).
- **RS-STORY: none.**

### 7.3 The unit ritual (the same every time)
**RS-LIST item:**
1. A face setup sentence, device in hand (P-14 / P-15), long enough to plant the item.
2. Into the device on the feature word, lead 2 f: a **whip** (T-WHIP, T-WHIP-S or T-WHIP-L, changing kind from one to the
   next) when it opens the item; a T-CUT or T-MATCH otherwise.
3. The POV (P-06 / P-09) with a P-10 push, carrying at most one overlay (a P-22 chip, a P-26 ripple, a P-27 loupe or the
   P-03 ring).
4. A second POV take (G-3) when the device moment runs long.
5. Back to the face for the "why it matters" or the reaction: a hard return (G-2) inside the item; a whip-out (G-2b) when
   the POV just showed the item's result and the next line moves on (about every second item in v02).

**RS-COUNT repetition:**
1. The POV clamp take (SH-5, P-07): the action.
2. The result appears on the device → counter tick (P-19) within ±3 f of it.
3. Every few repetitions, a face reaction (P-16); the counter stays up across the cut; a striking result exits to it by a
   whip-out (G-2b, v03 @ 7.9).
4. Repetitions not shown are skipped with a jump on the cut (P-20, e.g. 5 → 7).
5. **Finale:** the last 4–6 repetitions run as P-21 step punches on one clamp take, one every 0.5 s, then a whip into the
   TURN.

### 7.4 Open loops
- **Loops used:** the title's question or "can it" (paid at the TURN, on screen); "to the limit" (paid by the final count);
  "the best one is last" (RS-LIST, paid by the last item).
- **Re-hook:** a short reel needs none. Past about 45 s, plant one around the middle: a face line that raises the stakes
  ("now let's go to twenty") and a T-WHIP into the next POV.
- The hook is over fast (the whip lands by 2.5 s), so the first item arrives while the promise is fresh.

### 7.5 Rhythm by feel
- **The speech is the rhythm.** Face for the thought, device for the thing, and each holds exactly as long as its sentence
  earns: a lone "Next one:" is a beat, an opinion a couple of seconds, a scroll through a menu as long as the scroll. The
  picture never sits still because live footage never does, and a long POV gets a push, a snap or a second take before it
  can go flat.
- **Fast hook, steady items, a held result.** The hook is the densest moment. The items settle into the face-device swing.
  A joke or a reaction beat lands near the middle. Then the **TURN**: the result held longest of anything in the reel, the
  counter gone first, the captions alone with it. Then a short reaction and out.
- **One breath before the answer.** The voice runs continuously under the POVs; the one deliberate silence (≤ 0.4 s) sits
  right before the result reveal.
- **Escalate.** RS-LIST saves the best trick for last. RS-COUNT speeds up as it climbs: the later repetitions get shorter,
  then the step-punch run (P-21) fires before the TURN.
- **Entertainment comes back often enough that it never feels like a manual:** a reaction shot, a self-aware line to
  camera. Never two jokes back to back.
- **The story shape holds longer.** RS-STORY can stay on one face take while the bubble or the wide does the moving (v01
  holds one take 13.8 s under the bubble).
- For reference, measured on the three reels (a description, not a target): v02 28 cuts a minute, median shot 1.6 s
  (p90 4.0 s), 7 whips in 37 s; v03 42 cuts a minute, median shot 1.0 s (p90 2.7 s), 3 whips in 45 s; the longest
  no-cut stretch 4.4 s (v02), 4.7 s (v03); face on screen about 35 % (v02), 45 % (v03), 75 % (v01); the longest
  device-only runs about 4–5 s.

Every face ↔ device switch is a `transitions` entry (`T-WHIP`, `T-WHIP-S`, `T-WHIP-L`, `T-CUT`, `T-MATCH`), so the timeline
knows it's a cut; jump cuts inside the A-roll come from the cut map.

---

## §8 Visual system: B-roll and patterns

### 8.1 The role of graphics
- The device POV is footage, not graphics; the graphics are the overlays that point at it: the title, the counter, the
  ring, ripples, chips, bubbles, verdicts, the end card. They're there when the words call for them and gone the rest of
  the time.
- **Numbers become pictures, on the device:** a spoken number in a device beat is visible on the device's own screen (POV)
  or, when the screen can't be read, on a P-22 chip; a repeated action becomes the P-18 counter. A number is never a
  free-floating hero graphic in this style.
- Variety comes from the moment: a new feature, a new angle, a macro, a result. The repetition ritual of RS-COUNT is the one
  deliberate repeat. One overlay on a POV at a time: the device is the picture.

### 8.2 Families
| ID | Family | Source | The creator supplies |
|---|---|---|---|
| **B-1** | A-roll talking head (SH-1/3/4/8/9) | the creator's | The main take; optional hold-up, lean-in, wide and reaction shots |
| **B-2** | Device POV (SH-2/5/6) | the creator's | 4–12 POV clips (must) |
| **B-3** | Screen recording (SH-7) | the creator's | Native recordings of each UI step (backup) |
| **B-4** | Hook type | engine | — |
| **B-5** | Device marks: ring, tap ripple, loupe | engine | — |
| **B-6** | State and verdicts: counter, verdict chips | engine | — |
| **B-7** | Setting chips | engine | — |
| **B-8** | Created UI: drawn phone, message bubble, notification, logo plate, headline card | engine (the rebuilds of §12.5, when nothing real turns up) | — |
| **B-9** | Real third-party: a friend's message screenshot, a news headline, another brand's logo or product still | the creator's files, else fetched from the web (source noted); rebuilt as B-8 only when nothing usable turns up | Their files when they have them (§12.5) |
| **B-10** | End card | engine + the creator's artwork | Optional logo or artwork |
| **B-11** | Comedy (light) | engine | — |
| **B-12** | Transition passes (whip blur, flash, cut to black: core built-ins) | engine | — |

### 8.3 Pattern specs
Frames at 30 fps. "z" is the scene layer. Every text scene sets `text_class`.

**Hook and transitions**
| ID | Name | Type | On screen | Motion recipe | When | Family | Needs |
|---|---|---|---|---|---|---|---|
| **P-01** | Title Stagger | overlay | §5.2 title, one phrase at a time, cy 1340 | Phrase pops in over 2 f (scale 0.70 → 1, horizontal blur 12 → 0 px, opacity 0.5 → 1); swaps by a 2 f blurred crossover; no exit of its own, blurred away inside the hook whip. z10, `kind: "lockup"`, `satisfies: ["question"]` (+ `"device"` when the f0 frame shows the device ≥ 15 % of frame height) | H-A, HA-02 | B-4 / TC-display | events per swap |
| **P-02** | Question Chunks | overlay | The hook question in CS-1 captions from f0, no title | Caption engine; chunk 1 at f0 | H-B, HA-10, HA-14 | captions / TC-subtitle | — |
| **P-03** | Ring Sweep | annotation | The device outline + 14 px (radius = device corner radius + 14) drawn as a glowing segment ≈ 45 % of the outline height on both sides at once: white 4 px core, `highlight` 8 px stroke, glow `0 0 18px` at 70 % + `0 0 40px` at 35 % | The segment travels **bottom → top** over 9 f (ease-in-out): f1 the bottom corners light, f4–f5 mid sides, f7–f8 the top edge, f9 gone; its tail fades as it climbs; no hold (v03 @ 0.30–0.57). z6, `kind: "device"`, events [0.15] | The hook (H-B always, H-A when the device is still); "look at this", the moment of attention in the body. It's a spotlight: it only means something when it's rare | B-5 | an anchor on the device (§8.7) |
| **P-04** | Hold-up | cut | SH-3: the device swung to 30–40 cm from the lens, face soft behind | The footage itself; the title sits under the device | H-A f0 | B-1 | SH-3 |
| **P-05** | Whip Pass | transition pass | Drawn by core, no scene: T-WHIP = a footage **radial blur** centred on the device point (`timeline.blur` `kind: "radial"`, `at: [x, y]`) + a **white flash** (`timeline.transitions` `type: "flash"`); T-WHIP-S / T-WHIP-L = the built-in **`whip`** transition (directional smear + travel) | Flash (T-WHIP only): white 0 → 28 % over the 4 out-frames, peak on the cut, back to 0 over 3 land frames (measured luma +25–31 %, v02 @ 10.6, v03 @ 2.5). Radial blur over f−2…f+1, the picture fully blurred (measured 3 f) | Inside every whip | B-12 | the device point (screen px from the look frame, or the POV screen centre) |

**Device POV**
| ID | Name | Type | On screen | Motion recipe | When | Family | Needs |
|---|---|---|---|---|---|---|---|
| **P-06** | POV Hand | cut | SH-2 full-bleed: the device in one hand, screen 40–65 % of frame height, the set blurred behind | `VEOS.fx.clip` (or `pov()`, §16) z1 plate, `kind: "broll"`, `continuous: true`, `kenburns: [1.0, 1.06]` over the shot, `focus` on the screen centre; enters via a whip or T-CUT | A feature, setting or action is named | B-2 | SH-2 |
| **P-07** | POV Clamp | cut | SH-5 full-bleed: the device locked off on its clamp, a finger enters | No push (stillness shows the change); 1.0–3.0 s a take; the finale switches to P-21 step punches | RS-COUNT repetitions; a step-by-step setting | B-2 | SH-5 |
| **P-08** | Macro Push | footage-treatment | SH-6: an icon, port, button or texture, tilted 15–25° | `kenburns: [1.00, 1.12]` over 3–4 s, eased in-out | A tiny detail is the point ("the clock icon actually ticks") | B-2 | SH-6 |
| **P-09** | Scroll Run | cut | POV of a continuous interaction (scrolling, a dial, a slider) | Holds until the interaction resolves; an `events` mark where the UI changes; a long one splits into two takes | "Watch what happens when…" | B-2 | SH-2 |
| **P-10** | POV Push | footage-treatment | Any POV longer than 2.5 s | `kenburns: [1.00, 1.08]` + a declared event at the UI change | Keeps a long POV alive | B-2 | — |
| **P-10b** | POV Snap | footage-treatment | The POV clip jumps closer on the action word (the shutter, the result appearing) | Scale 1.00 → 1.25 over 6 f (≈ +5 % a frame, ease-out at the end), then hold to the cut; about the screen centre (v02 @ 8.17–8.33) | The action word of a POV over 2 s; it's the POV's one punch, so save it for the moments that deserve it | B-2 | a ≥ 1440 px wide POV for no visible softness |
| **P-11** | Drawn Phone | fallback | A generic phone frame (radius 64, 14 px `#111` bezel, a pill-shaped island) 580 × 1060 at x 250, y 260, tilt −6°, float ±6 px on a 3 s sine; the screen plays the SH-7 recording (`ctx.videoFrame`) or a recreated UI (`fx.appUI`) | Rise 12 f + de-blur 12 → 0 px; exit fall 8 f; stage `dim` 8 f underneath (L-device-dim). **3D variant** (no device footage, a still screen): `VEOS.fx.three({box: {x: 220, y: 300, w: 640, h: 1100}, insert: "<insert id>", objects: [{kind: "device", screen: "<screenshot asset>", rot: [0, -24, -6], keys: [{at: 0, rot: [0, -40, -6], scale: 0.9}, {at: 0.4, rot: [0, -24, -6], scale: 1, ease: "expoOut"}]}]})`. No `camera`: the phone fills its box by default (≈ 1050 px tall, the spec size). `insert` is a plain field the engine reads. The screenshot is a phone-size capture: `veos capture <url> --size 390x844@3x` (1170 × 2532) → `veos asset add --source <url>`; a recording stays 2D (`screen` takes an image); one 3D scene on screen at a time (≈ 70–95 ms a frame) | FB-1 / FB-2 only | B-8 | SH-7 or a recreated UI |
| **P-12** | Result Full-bleed | cut | The TURN: the device's output (the photo, the finished batch, the screen result) full frame | `kenburns: [1.00, 1.10]` over 2–5 s; the counter exits 8 f before it; captions continue; no other graphic | The climax, the answer to the title | B-2 | SH-2 / SH-5 |
| **P-13** | Wide Context | cut | SH-8: the presenter using the device in the room | 2–6 s; captions only | RS-STORY context, "so I'm sitting there…" | B-1 | SH-8 |

**A-roll**
| ID | Name | Type | On screen | Motion recipe | When | Family | Needs |
|---|---|---|---|---|---|---|---|
| **P-14** | Talk | cut | SH-1: the presenter, device in hand | Z-2 push-drift on holds over 3 s | Setup, opinion, why | B-1 | SH-1 |
| **P-15** | Point | cut | The presenter holds up or points at the device on "this / look / here" | The next cut is a whip into the device | The line before a device beat | B-1 | SH-1 |
| **P-16** | Reaction | cut | SH-9 or a natural A-roll reaction (laugh, disbelief, wince) | 0.8–2.0 s; an optional Z-3 snap-punch on the best one | After a result; tone `joke` | B-1 / B-11 | SH-9 |
| **P-17** | Jump Cut | cut | The A-roll with a pause removed | Hard cut on the word boundary; no reframe | Every pause ≥ 150 ms inside an A-roll run | B-1 | — |

**State, marks and chips**
| ID | Name | Type | On screen | Motion recipe | When | Family | Needs |
|---|---|---|---|---|---|---|---|
| **P-18** | Counter Label | state | "{Label}: {n}" (§5.4), centred cx 540, cy = caption cy − 120, fixed-width box | In 8 f (rise 24 px + fade, scale 0.9 → 1) on the first op; persists across every cut; out 8 f fade. z6, `text_class: "TC-display"`, events at every op | RS-COUNT, from repetition 1 | B-6 / TC-display | state var `count` |
| **P-19** | Counter Tick | state event | The value changes 1–2 f after the op's cut | **Odometer roll**: only the digits that change move; the old digits slide up and out of a clipped box while the new ones rise in from one line below, 4 f, ease-out; the label never moves; no scale bump, no flash (v03 @ 40.30–40.40, 40.80–40.87) | Each counted repetition, ±3 f of its result | B-6 | op |
| **P-20** | Counter Jump | state event | Skipped repetitions: 5 → 7 on the cut | One roll straight to the new value; never rolls through skipped values, never counts down | A repetition not shown | B-6 | op |
| **P-21** | Final Run (step punches) | state event + footage-treatment | The last 4–6 repetitions on one locked-off clamp take: each repetition is a hard **step punch** (+6 to +23 % scale, about the screen, no easing) with a counter tick, every 0.5 s (v03 @ 40.23–42.77: 1.00 → 1.10 → 1.16 → 1.43) | Steps on the cut frame; the tick rolls 1–2 f later; the counter exits 8 f before P-12 | RS-COUNT finale, the run-up to the TURN | B-6 / B-2 | ops, SH-5 |
| **P-22** | Setting Chip | overlay | §5.4 chip naming the setting or spec ("Snooze: 9 min", "Burst: 600") | Pop 7 f (scale 0.8 → 1.04 → 1); hold ≥ 1.2 s; out blur 5 f. z5, cy 250, POV only | The UI text is too small to read; a spec is named | B-7 / TC-label | — |
| **P-23** | Message Bubble | overlay (created UI) | §5.4 bubble with avatar initials, the message text, "Name · time" | **Flies out of the device**: starts as a 12 px-high sliver at the device screen, stretches sideways toward its resting x with a horizontal motion blur 16 → 0 px while its height opens, over 6 f (ease-out); the avatar lands last (f5); then it drifts with the footage (`follow_footage: true`: the scene rides the footage transform, drawn in footage px); out fade 6 f. z5, bubble band y 1060–1300, x from 80; ≥ 40 px clear of the head region (v01 @ 5.18–5.38) | Someone's message, DM or email is read out | B-8 (or B-9 via `fx.shot`) / TC-label | the real message, else its exact words |
| **P-24** | Notification Drop | overlay (created UI) | §5.4 banner at y 150–330, on the POV or the dimmed set (not on the face shot: it would land on the head) | Slides from y −200 to 150 over 10 f (expo-out); hold ≥ 1.5 s; out up 8 f. z5 | An alert, reminder or app notification is the point | B-8 / TC-label | the real app's name and glyph |
| **P-25** | Verdict Chip | overlay | "WORKS ✓" (`good`) / "FAILS ✕" or "NOPE" (`bad`) | Stamp-in 5 f (scale 1.4 → 1, rotate −4° → 0); hold ≥ 1.0 s; fade 5 f. z6, the counter band when no counter is up, else cy 250 on the POV | A test result, a comparison winner: a verdict is a punchline | B-6 / TC-label | — |
| **P-26** | Tap Ripple | annotation | Two concentric `highlight` rings, 5 px, at the finger's touch point | Ø 40 → 160 px over 10 f, opacity 0.9 → 0, the second ring 3 f later. z6 | A tap or press that matters | B-5 | anchor (tap point) |
| **P-27** | Loupe | annotation | A Ø 360 circle with a 6 px `paper` ring and a soft shadow, showing the POV frame at 1.8× around a UI point; placed on the opposite side of the point, never covering it | Pop 7 f; hold ≥ 1.2 s; out 5 f. z5 | Tiny UI text is the point | B-5 | anchor; a 4K POV or the SH-7 recording |
| **P-28** | Two Devices | cut | Both devices in one POV frame (two hands, or side by side on the desk) | Captions only; P-25 on the winner | A comparison ("old vs new") | B-2 | SH-2 |

**Comedy, inserts and end**
| ID | Name | Type | On screen | Motion recipe | When | Family | Needs |
|---|---|---|---|---|---|---|---|
| **P-29** | Sticker | overlay (comedy light) | One emoji, 140 px, 8 px white outline, beside the face at shoulder height (on the face only when the joke is aimed right at it; never on the device) | Pop 6 f (0 → 1.2 → 1), wobble ±3° over 10 f. z9 | The one self-aware joke that earns it: it's the only cartoon in a real-world reel, so more than one turns it into a meme page | B-11 | joke tone |
| **P-30** | Cut to Black | transition pass | Full-frame black | Hard cut to black on the last word's end (+2 f); 0–3 f of pure black before the card starts building (v01 @ 22.42) | Into the end card only | B-12 | — |
| **P-31** | Logo Plate | overlay (insert) | Another product's or company's real logo (the creator's file, else fetched from the web) on a neutral plate; `VEOS.fx.logoPlate` (the name set in type) only when no logo can be found | Built-in rise; ≤ 2.5 s; on the POV at y 200–520 or on L-device-dim | The script names a product or brand that isn't the creator's device on screen | B-9 (B-8 when rebuilt) / TC-label | the real logo, source noted |
| **P-32** | End Card | brand | §6.7: black, the wordmark, an artwork band, the CTA line | Builds in over ≈ 14 f; holds; exit smear 5 f; ≤ 5 s; hard end | CTA `end_card`, `comment_keyword`, `link_bio` | B-10 / TC-display | `kind: "end-card"` |
| **P-33** | Keyword Chip | brand | "Comment" + the keyword chip on the end card (or "Link in bio") | Pops 0.3 s after the card (7 f); ≥ 1.5 s. z6, `kind: "cta-keyword"` | CTA `comment_keyword` / `link_bio` | B-10 / TC-display | the keyword |
| **P-34** | Headline Card | overlay (insert) | The real headline: a `veos capture` of the article's headline (or the maker's page) framed on the line, else `VEOS.fx.headlineCard` with the outlet name set in type and the exact headline; a highlight bar on the spoken phrase | Built-in rise; ≤ 3 s; on L-device-dim (the A-roll dimmed behind it) | The script quotes a news story or a maker's claim | B-9 (B-8 when rebuilt) / TC-label | the real headline, word for word, source noted |

### 8.4 Line → pattern lookup
Vocabulary, not a decision table: it tells you what this style reaches for. Ask what the moment needs, then use it.

| Line type | Primary | Alternates | For example |
|---|---|---|---|
| Hook claim or question | P-01 or P-02 + P-03 → T-WHIP | P-04 | "What they don't tell you about your phone" |
| A feature, setting or button is named | P-06 | P-08, P-22 | "There's a setting called Back Tap" |
| An action on the device | P-06 / P-09 + P-26 | P-07 | "Hold the space bar" |
| A number shown on the device | P-06 with the number on screen | P-22 (with the number), P-27 | "Bursts are capped at 600" |
| A tiny on-screen detail | P-08 | P-27 | "The clock icon actually ticks" |
| A counted repetition | P-07 + P-19 | P-06 + P-19 | "Batch number five" |
| Repetitions skipped | P-20 on the cut | — | "…and seven" |
| The result / the answer | P-21 run → P-12 | P-25 | "This is twenty edits later" |
| Opinion, why it matters | P-14 | P-15 | "That's genuinely useful" |
| Reaction or joke | P-16 | P-29 | "I look like a cartoon now" |
| A comparison of two devices | P-28 + P-25 | P-06 ×2 (G-3) | "Old phone vs new phone" |
| Works / fails verdict | P-25 | — | "It failed" |
| Someone's message read out | P-23 (or B-9 `fx.shot`) | P-24 | "My friend texted me…" |
| A notification or alert | P-24 | P-06 (filmed) | "I got this notification" |
| Another product or brand named | P-31 | — | "Unlike that other brand…" |
| A news story or maker's claim | P-34 | P-31 | "The box says 1,000 watts" |
| Scene-setting (where, when) | P-13 | P-14 | "So I'm on a train" |
| CTA / end | P-30 → P-32 (+ P-33) | hard end | — |

### 8.5 Numbers and truth
- No data charts: numbers are the device's own readings, the counter, or spoken specs on a chip.
- The counter counts repetitions that happened in the footage (§8.6).
- Specs on chips are copied from the device screen or the script, with units.
- A drawn phone or a recreated screen is a fallback and looks like one (tilted, floating over the dimmed set); its screen
  furniture may use made-up but realistic values with no label, but any spec or result the reel claims is the one the
  creator said.

### 8.6 The counter (running state)
```yaml
running_state:
  vars:
    count: {type: counter, start: 0, label: "<the thing being counted>", format: "{label}: {n}", display: P-18, persist: across_cuts}
```
- **Ops** are written per beat: `state_ops: [{var: count, op: add, value: 1, at: <s>}]`, or `op: set` for a jump (P-20),
  and only on a cut frame (the digits roll 1–2 f after it, P-19; whips included: the counter stays sharp through every
  blur, v03 @ 7.9, 37.9).
- **Display rules:** one position for the whole span (cx 540, cy = caption cy − 120); it changes only on ops; it appears
  with the first op (value 1, never 0); it never decreases; it never shows a value the footage hasn't reached; it survives
  every cut (face and POV); it exits 8 f before the TURN (P-12) and never shares a frame with the title or the end card.
- **Label:** one noun, title case, ≤ 12 characters, the thing that repeats ("Reframes", "Batches", "Passes", "Drops",
  "Washes", "Tries").
- **Build:** one scene from the first op to its exit; the shown value is the last op at or before `ctx.t`; the scene
  declares an `events` entry at every op (§16).
- **Check by eye:** the shown value equals the running sum of ops at every tick frame; ops ascend; the final value equals
  the last repetition shown; the counter's rect holds still (±4 px).

### 8.7 Anchors: the ring and the tap ripple (tracked)
- **When to track:** as soon as a beat's visual puts a ring, ripple or bubble *on the device* and the device moves more
  than 20 px over the scene (a hand-held swing, a hold-up, a pan). Track only the scene's span plus 0.3 s each side (≤ 10 s
  a run):
  1. `veos track --project P --at <t_in> --look` → read the device box off `plan/tracks/look_<t>.jpg` (edit-frame px).
  2. `veos track --project P --id phone --at <t_in> --box x,y,w,h --from <t_in − 0.3> --to <t_out + 0.3>` (a fingertip
     tap: `--point x,y`). Look at `plan/tracks/phone.preview.jpg`.
- **Scene:** `anchor: {track: "phone", scale_with: true, lost: "fade"}` with `box` = the device box at `t_in` + 14 px on
  every side (corner radius + 14). The ring code draws inside that box; core moves and scales the box with the device
  (camera zooms included). Tap ripple: `anchor: {track: "tap"}` on a point track.
- **Fallback:** a clamp or a still hand (drift ≤ 20 px over the 9 f sweep) needs no track: use the static box from the look
  frame. Skip the ring when the preview shows the device lost on more than 20 % of the span (`max_lost` 0.2), when the
  device fills or leaves the frame, or when motion blur hides its outline (the H-A swing): never leave a ring on a stale
  spot.
- **The head:** a ring whose tracked rect would come within 40 px of the head (a device held next to the face) is usually
  skipped; look at the frame and decide.

### 8.8 Comedy layer (light)
- **Where:** `joke` beats, on the creator's face: a reaction shot (P-16), a self-aware line to camera (v03 @ 0:23 "I look
  like hairy Shrek").
- **What:** the reaction itself; a Z-3 snap-punch on the best reaction; the one sticker (P-29) if a joke truly earns it.
- **Never:** meme sounds, stamps, freeze-frames, marker scribbles, or anything on the device screen.

### 8.9 Assets
- Real captures first: the creator's own device, filmed by the creator (B-2), with native recordings (B-3) as backup.
- Mocks only as fallbacks (P-11), generic and unbranded.
- No stock footage, no promo renders of the device: the device on screen is always the creator's own.
- Another brand's logo, a real post, a real headline: the creator's files first, else fetched from the web, source noted
  (§12.5).
- Third-party moments: fetch the real thing (§12.5).
- Personal data on device screens is blurred (§2).

---

## §9 Transition system

### 9.1 Library
Measured at 30 fps (v02, v03 bursts). f0 = the cut frame. The reference has whips in both directions: 10 blur transitions
in the three reels, 4 face → POV, 5 POV → face, 1 hook.

| ID | Transition | Frames | Recipe | Cue role |
|---|---|---|---|---|
| **T-WHIP** | Zoom-flash whip (into the device, or back out to the face) | 10 | f−4…f−1: the outgoing shot zooms 1.0 → 1.6 **about the device point** (ease-in: ≈ +2 %, +2 %, +11 %, +16 % a frame) and brightens; a face out = camera Z-1 `zoom-through` (7 f) with `p.origin: {x, y}` = the device point, a POV out = the clip scene's own scale about the same point. f−2…f+1: footage radial blur at the device point (`amount` 0.3), the picture fully blurred. f0: stage `cut`; the incoming shot lands at 1.15 → 1.00 with a footage defocus 14 → 0 px and the flash 28 → 0 % over 3 f. Sharp on f+3. Captions hidden on the 3 peak frames. Timeline: §16 | whoosh (transitions) |
| **T-WHIP-S** | Spin whip | 7 | Built in: `{"t": <cut>, "type": "whip", "angle": 60, "frames": 7, "pre": 3, "px": 120, "travel": 880}` (diagonal smear, ≈ 620 px/f at the peak, a 2 f cross-blend, the incoming shot smears in from the other side) + Z-5 `rotation-snap` 5° in 3 f before the cut on a face out (`p.origin` the device point). No flash (v02 @ 1.30–1.57, 29.73–30.03) | whoosh (transitions) |
| **T-WHIP-L** | Linear whip | 6 | Built in: `{"t": <cut>, "type": "whip", "dir": "left", "frames": 6, "pre": 3, "px": 60, "travel": 480}` (the frame slides sideways with a horizontal smear, 160 px/f; `dir: "right"` for the reverse) + a 30 % darkening `VEOS.fx.flash({at: <cut> − 3/30, up: 3, hold: 0, decay: 3, color: "#000000", peak: 0.3, z: 6})` (under the captions); hard cut at f0; captions stay up (v02 @ 5.27–5.43, 24.37–24.50) | swish (transitions) |
| **T-CUT** | Hard cut | 0 | On the word boundary ±1 f | silent |
| **T-MATCH** | Match-motion cut | 0 | A hard cut where the A-roll hand reaching for the device meets the POV hand entering the frame (±2 f of the reach) | silent |
| **T-JUMP** | Jump cut | 0 | Inside the A-roll on a pause ≥ 150 ms; same framing | silent |
| **T-BLACK** | Cut to black | 0 + ≤ 3 black | P-30 hard cut to black, then the end card builds in (§6.7) (v01 @ 22.42) | none (the CTA cue sits on the card) |
| **T-DIM** | Dim to drawn phone | 8 | Stage `via: dim`; P-11 rises over 10 f | soft whoosh (fallback only) |

### 9.2 Grammar
| Boundary | Use | Never |
|---|---|---|
| f0 | No transition: open on live footage + the Z-4 punch and title pop (H-A) or the lunge (H-B) | A fade-in or a black first frame |
| Hook → first POV | **T-WHIP-S** (hand-held device) or **T-WHIP** (clamp) by 2.5 s | A hard cut |
| Face → POV, opening an item | a whip (change the kind from the last one) | — |
| Face → POV inside an item | T-CUT or T-MATCH | Any blur |
| POV → face, the item's result just shown | a whip-out (G-2b): T-WHIP, T-WHIP-L or T-WHIP-S | — |
| POV → face, mid-item | **T-CUT** on the first word of the sentence | A whip |
| POV → POV | T-CUT (G-3) or a P-21 step punch | Any blur |
| Repetition → repetition (RS-COUNT) | T-CUT; the finale as P-21 step punches | A whip (save it for the first repetition, a reaction exit and the TURN) |
| Into the TURN (result) | T-WHIP | — |
| Last word → end card | T-BLACK | A fade; a black tail over 0.2 s |
| CTA `none` | Hard end ≤ 6 f after the last word | — |

Two typed transitions never overlap. A POV entered by T-CUT doesn't do the whip's land (`pov(..., {land: false})`, §16).

### 9.3 Shot grammar
| ID | Rule |
|---|---|
| **R-1** | Face and device trade the screen; neither holds longer than its sentence earns. |
| **R-2** | Cut to the device on the trigger word (lead 2 f): the feature noun, the action verb, the number. |
| **R-3** | Cut back to the face on the first word of an opinion, a reaction or a joke. |
| **R-4** | Two POV takes in a row must differ (another action, angle or macro), never the same framing again. |
| **R-5** | Use T-MATCH when the A-roll hand reaches toward the device and a POV take starts with the hand entering (v03 @ 0:02.5). |
| **R-6** | Jump cuts (T-JUMP) remove every A-roll pause ≥ 150 ms; the framing stays (no punch reframes). |
| **R-7** | The TURN (result) is the longest POV of the reel (2–5 s) and is followed by a face reaction. |
| **R-8** | The reel's last shot is the face (a reaction or the last line) or the end card, never a POV mid-action. |

### 9.4 How the moves breathe
A whip is a section break: it says "new thing" or "here's what that did". It only reads that way if each one has room
around it, so two never crowd each other, and inside an item everything is a hard cut you don't notice. Change the kind
from one whip to the next (zoom-flash, spin, linear) so the reel feels alive, not looped; the zoom-flash is the loudest, so
it belongs on the hook with a clamp, the big results and the TURN. Look for the match cut: when the hand reaches for the
device and a POV take opens on a hand entering, cut there; it's the most satisfying cut in the style. The cut to black
happens once, into the end card; the dim to a drawn phone only when a fallback forces it. A list reel whips often (v02:
7 in 37 s); a count-up lets the counter carry the momentum and whips less (v03: 3 in 45 s); a story barely whips at all
(v01: none; its end card carries the motion).

---

## §10 Motion tokens, camera and zoom, layers, finishing

### 10.1 Motion tokens (30 fps)
| Token | Value |
|---|---|
| Beat lead | 2 f before the onset |
| Entries | `cubic-bezier(0.22, 1, 0.36, 1)` (expo-out) |
| Exits | `cubic-bezier(0.64, 0, 0.78, 0)`, 3–8 f |
| In-out | `cubic-bezier(0.65, 0, 0.35, 1)` |
| Title pop / swap | 2 f (scale 0.70 → 1, h-blur 12 → 0 px) / 2 f blurred crossover (new 0.85 → 1) |
| Whips | T-WHIP 4 out + 3 peak + 3 land (1.6×, flash 28 %); T-WHIP-S 7 f (5° roll); T-WHIP-L 6 f |
| Ring sweep | 9 f bottom → top, segment 45 % of the outline height, no hold |
| Tap ripple | 10 f (Ø 40 → 160), second ring +3 f |
| Counter | in 8 f; tick = odometer roll 4 f (digits up, ease-out, 1–2 f after the cut); out 8 f |
| Bubble | flies out of the device 6 f (sliver → full, h-blur 16 → 0 px), drifts with the footage (`follow_footage: true`) |
| Chip pop | 7 f; verdict stamp 5 f |
| POV push | `kenburns` 1.00 → 1.06 (standard) / 1.08 (over 2.5 s) / 1.10 (TURN) / 1.12 (macro) |
| POV snap / step | 1.00 → 1.25 in 6 f, hold (P-10b) / +6 to +23 % hard steps every 0.5 s (P-21) |
| Stage | `cut` 0 f; `dim` 8 f |
| End card | build 14 f; exit smear + zoom blur 5 f |
| Holds | Text ≥ 0.25 s per word; any element ≥ 10 f after it's built |

### 10.2 Footage camera (`zoom_policy: presets`)
| ID | Preset (engine name) | Recipe | Use |
|---|---|---|---|
| **Z-4** | `crash-zoom` | 1.0 → 1.4 over f1–f5 (ease-out: ≈ +6, +11, +10, +9, +1 % a frame; measured 1.0 → 1.43, v02 @ 0.03–0.17), held to the hook whip; the f0 frame is the motion-blurred swing | The H-A open punch on f0, and nowhere else |
| **Z-1** | `zoom-through` | 1.0 → 1.6, 7 f, ease-in, ends on the cut; pivot `p.origin` = the device point | Only inside T-WHIP (a face out) |
| **Z-5** | `rotation-snap` | 5° roll in 3 f about `p.origin` = the device point | Only inside T-WHIP-S (a face out) |
| **Z-2** | `push-drift` | 1.00 → 1.05 over the beat | Face holds over 3 s |
| **Z-3** | `snap-punch` | 1.00 → 1.15 in 3 f, motion blur f1–2, hold to the next cut | The best joke reaction; FB-3's hold-up substitute. A punch on the face is rare here, which is why it lands |
| **Z-0** | `reset` | Back to 1.0 in 4 f | Written on every return cut after a whip, so two whips are never consecutive camera events |

The camera presets move the A-roll only; POV clips move by their own `kenburns`, the P-10b snap and the P-21 steps. Whip
zooms pivot on the device point (`p.origin: {x, y}` on Z-1 / Z-5, or `"device"` with `timeline.canvas_nodes.device` when
one device position serves the reel) and the radial blur is centred there, so the read is "into the device", not "into the
face". Never two camera moves within 0.4 s; change the kind of move from one to the next. Measured: no continuous digital
push on the A-roll; its scale drifts are the presenter and the hand-held camera (live motion is the motion). The camera
only ever moves footage: there's no canvas camera in this style.

### 10.3 Layer order (back to front)
1. W-void / W-studio (z1 world)
2. POV clip scenes (z1 plates, full-bleed, under a `hidden` stage, so the whip's footage blur reaches them)
3. Drawn phone (P-11, z5 on L-device-dim) above the dimmed footage
4. A-roll footage (stage)
5. Chips, bubbles, notification, logo plate, headline card, loupe (z5)
6. Counter, verdict chips, ring, tap ripples, CTA chip (z6)
7. Captions (z7)
8. Sticker (z9)
9. Title (z10)
10. The black of P-30 (z11). Whip blur, smear and flash are drawn by core over the picture (under the captions), not as
    scenes

### 10.4 Finishing
- No grain, no vignette, no LUT.
- Glow only on the ring and the tap ripples.
- Hard shadows only on the title (the extrusion); soft shadows on captions, bubbles and chips.
- Exposure and white balance matched between the A-roll and the POV; nothing else.

---

## §11 Sound

The reference's sound couldn't be measured; this is a decision, not a measurement. Sound marks the moves: the whip, the
reveal, the count. The cuts inside an item are silent so the whips stay special.

| Line | Direction |
|---|---|
| **Where sound goes** | `hook`: one cue on the title entry or the ring (a lens-zoom click such as `camera-quick-zoom-shoot-ohmlab-camera-quick-zoom-shoot-ohmlab` on the punch). `transitions`: every whip (a flash-whoosh such as `cinematic-transition-flash-05` on T-WHIP, `hit-spin` on T-WHIP-S, `fast-swish-movement-fast-swish-movement` on T-WHIP-L); hard cuts and step punches are silent. `reveals`: the ring, the TURN result, a verdict chip (a bright ding such as `05405-shine-ding`). `list_cue`: one tick file for the counter (`digital-click`), the one sound that repeats, at most one tick cue in each `REP-n` section. `cta`: the end card |
| **Meme sounds** | None (comedy is light and lives on the face) |
| **The bed** | On; it enters on the hook whip landing |
| **Ducking** | The bed sits ≥ 18 dB under the voice while the voice speaks. POV clips are muted (the A-roll voice carries them); a POV take cut in as its own EDL segment keeps its own voice |
| **Loudness** | −14 LUFS integrated, true peak ≤ −1.5 dBTP; a hard end ≤ 6 f after the last word |

Pick each cue for its moment, so the same whoosh never turns into wallpaper; the counter tick is the deliberate repeat.

---

## §12 Footage handling

### 12.1 Setups
| Setup | Camera | Framing | Set and light | Notes |
|---|---|---|---|---|
| **A: A-roll** | Main camera on a tripod, 4K, 30 fps (or 60 conformed), vertical | Eye level or slightly low; head top y 160–320; chest and hands in frame so the device shows | Shallow depth of field (f/1.8–2.8); soft coloured practicals or a warm shelf behind, 1.5–3 m back; soft key at 45° | A lav mic is fine (visible in all three reference reels); a plain or textured top, no logos |
| **B: POV** | A second camera or a phone at chin height looking down at the device in one hand | Device screen 40–65 % of frame height, centre x 380–700, centre y 700–1000 | The same set, blurred | Muted; the A-roll voice carries it |
| **C: Clamp** | The device on a clamp or monopod at chest height; a locked-off camera on it | Screen 45–80 % of frame height | Same set | For the lean-in hook (SH-4) and repetitions (SH-5) |

### 12.2 Shots and fallbacks
| ID | Shot | Spec | Must |
|---|---|---|---|
| **SH-1** | A-roll talking head | Setup A, device in hand | must |
| **SH-2** | Hand-held device POV | Setup B, one take per feature, 2–6 s, hold still 1 s before and after the action | **must** |
| **SH-3** | Hold-up | Device swung toward the lens in ~0.3 s, held still 1.5–2 s at 30–40 cm, face soft behind, device bottom above y 1210 | optional (H-A) |
| **SH-4** | Lean-in | Device on its clamp; the presenter leans in from camera-left, face in the top half | optional (H-B) |
| **SH-5** | Clamp POV | Setup C locked off, one take per repetition, 1–3 s | optional (RS-COUNT) |
| **SH-6** | Macro detail | Icon, port, button or texture, tilted 15–25°, slow forward move 3–4 s | optional |
| **SH-7** | Screen recording | Native recording of every UI step | optional (backup) |
| **SH-8** | Wide context | Presenter using the device in the room, 3–7 s | optional (RS-STORY) |
| **SH-9** | Reaction bank | Laugh, disbelief, wince, shrug, 1–2 s each | optional |

| ID | For | What the engine does instead | Cost | Result |
|---|---|---|---|---|
| **FB-1** | SH-2 | The SH-7 screen recording inside the drawn phone (P-11), tilted −6° with a slow float, over the dimmed A-roll (L-device-dim) | No real hand or device: the POV feel and believability are lost | degraded |
| **FB-2** | SH-2 (no recording either) | A recreated generic UI (`fx.appUI`) inside the drawn phone, for one or two beats at most | The reel shows a mock, not the device | degraded |
| **FB-3** | SH-3 | SH-1 with the device in hand + the title; the whip starts after a Z-3 snap-punch toward the hand | Less depth in the hook | holds |
| **FB-4** | SH-4 | SH-1; the ring is skipped and the hook is H-A | No lean-in energy | holds |
| **FB-5** | SH-5 | SH-2 hand-held takes, one per repetition | Less consistent framing between repetitions | holds |
| **FB-6** | SH-6 | A 1.35× crop of an SH-2 take with P-08's push (more needs a 4K source) | No macro texture | degraded |
| **FB-7** | SH-8 | Skip the wide; stay on SH-1 | None worth noting | holds |
| **FB-8** | SH-9 / SH-1 extras | The nearest natural reaction in the main take | Fewer reaction beats | holds |

Say in the plan which fallbacks this reel uses (`fallback_used` per beat). When more than half the device beats run on
FB-1/FB-2, tell the creator plainly: "this look needs your POV shots; this reel will read as a screen-recording explainer".
Without a hand-held hold-up (FB-3) the hook loses its swing and reads less like this style; say so when you show the
storyboard, so the next shoot has one.

### 12.3 The POV capture checklist
Give this to the creator before the shoot.
- **C-1** Clean the screen and the lens. Peel off a glossy screen protector if it glares.
- **C-2** Do Not Disturb on, notifications hidden, a demo contact name; nothing personal on screen.
- **C-3** Screen brightness 70–85 %, auto-brightness off, night-shift/true-tone off; dark mode only if the reel is about it.
- **C-4** POV camera: the same frame rate as the A-roll; shutter 1/60 at 30 fps (1/50 in 50 Hz countries) so the screen
  doesn't band; expose for the screen (about −0.7 EV) so white UI isn't clipped; focus locked on the screen.
- **C-5** Framing: vertical 9:16, 4K if possible; the screen fills 40–65 % of frame height with its centre at x 380–700,
  y 700–1000; UI you need to read stays above y 1340 (the caption band).
- **C-6** Background: the same set as the A-roll, blurred (f/2–2.8). Hand and wrist enter from a bottom corner.
- **C-7** One feature = one take: hold the device still for 1 s, do the action at normal speed, hold 1 s on the result. Then
  do it once more, slower.
- **C-8** Count-ups: lock the POV camera on the clamped device; identical framing for every repetition; one file per
  repetition.
- **C-9** Hook hold-up: swing the device from your chest toward the lens in about 0.3 s, stop 30–40 cm away, hold 2 s; your
  face behind at f/2 so it's soft; keep the device's bottom edge above the lower third.
- **C-10** Lean-in: device on a clamp at chest height, lean in from camera-left, face in the top half of the frame.
- **C-11** Macro: tilt 15–25°, push in slowly for 3–4 s, focus on the detail.
- **C-12** Also screen-record every UI step natively (SH-7) as a backup for legibility.
- **C-13** Name files `item01_pov_a.mp4`, `item01_pov_b.mp4`, `rep07_clamp.mp4`, `hook_holdup.mp4` so logging is instant.
- **C-14** POV takes are silent inserts under the A-roll voice. If you talk while filming the POV, keep the mic on you: that
  take can be cut in as its own segment.

### 12.4 Props, the reaction bank, resolution
- **Props:** the device; a phone clamp or monopod; a second camera or phone for the POV; a glossy screen protector off.
- **Reaction bank (SH-9):** laugh, disbelief, wince, shrug.
- **No cut-out** (`matte: none`).
- **Resolution:** a 1.35× punch needs ≥ 1080 × 1920; a 2× crop (the P-27 loupe on a POV) needs a 4K POV, else use the SH-7
  recording inside the loupe; the P-10b snap stays sharp from a ≥ 1440 px wide POV.

### 12.5 Third-party inserts: fetch the real thing
The creator's own device, filmed by the creator, is creator footage, not an insert. Third-party moments in this style are
usually a message someone else sent, a notification from another service, a news story or a maker's claim, another
brand's product, another creator's video. When the creator names one, the viewer should see the real one.
1. The creator's own files in their folder come first (a friend's message is almost always theirs).
2. Otherwise search the web and fetch it: the real logo, the real headline, the maker's real page (captured and framed on
   the part that matters). Note where it came from.
3. Show it as it is with `VEOS.fx.shot` (cropped, framed, highlighted), never altered to say something it doesn't; a post
   or headline is shown word for word.
4. **Nothing usable to be found: rebuild it from its exact words** (no labels, no credit lines):

| Moment | Rebuilt as |
|---|---|
| A message | P-23 bubble (`quote_card` recipe; the exact words from the script; initials, never a photo) |
| A notification | P-24 (`recreated_ui`, the real app's name, a generic glyph) |
| A news story or a maker's claim | P-34 (`headline_card`, the exact headline) |
| Another product or brand | P-31 (`logo_plate`, the name set in type) |
| Another creator's video | `fx.appUI({kind: "video"})` on L-device-dim |
| A person | `fx.silhouette` |

### 12.6 Frame rate and audio
- 30 fps CFR out, 1080 × 1920; conform variable-frame-rate phone POVs.
- One voice: the A-roll mic (high-pass 80 Hz, de-ess, compression, −14 LUFS). POV video assets carry no sound into the mix.

---

## §13 What your plan should settle

Your `ideas.md` is a page or two, for you. In this style it has decided, before any code:
1. **The shape and the hook:** RS-LIST, RS-COUNT or RS-STORY; HA-17 H-A or H-B (or HA-02 / HA-10 / HA-14); the title (8–10
   candidates, the pick, two alternates) with its phrase timings, or the question chunks; the whip landing frame.
2. **The shot-pairing table:** every sentence → face or device, its trigger word and frame, the POV take with its in and
   out, the fallback if any.
3. **The whip map:** every section change, its kind (T-WHIP / T-WHIP-S / T-WHIP-L), its cut frame, its device point; the
   Z-1 / Z-5 and Z-0 pairs; every T-MATCH.
4. **The caption height** (rule CY: `low` 1400 or `mid` 1270) with its overlap numbers, and the counter band that follows.
5. **The count plan** (RS-COUNT): the label, every op and its frame, the jumps, the step-punch scales of the finale, the
   counter's exit frame before the TURN.
6. **The anchors:** every ring and ripple box, tracked or static, and the rings skipped.
7. **The inserts** (the creator's, fetched with their source, or rebuilt) and the fallbacks used, with the plain warning
   when FB-1/FB-2 carry more than half the device beats.
8. **The sound:** the cue moments, the list cue, the bed's entry.
9. **The moments you'll look at hardest on the storyboard:** f0 (the device + the title or first chunk), the whip
   landing, one POV beat with its caption (the UI it reads clear of the band), one face beat (the head clear, the caption
   and counter on the chest), one counter tick (RS-COUNT), the TURN, the end card.

**Beat fields this style adds:** `trigger {word, at}`, `shot_id`, `fallback_used`, `state_ops [{var: count, op: add | set,
value, at}]`, `anchor {target: object:device | region, box {x, y, w, h, r} | point, follow}`, `insert {id, origin}`,
`sponsor {id, disclosure}` (only when sponsored). Captions carry `{profile: CS-1, overrides: []}` (no emphasis in this
style).

A beat, for the shape:
```yaml
- id: 7
  section: ITEM-2                 # HOOK | ITEM-n | REP-n | TURN | END
  t0: 7.40
  t1: 10.80
  spoken: "tap the back of your phone twice"
  trigger: {word: "tap", at: 7.52}
  tone: explain                   # hype | explain | awe | win | warn | joke | cta
  line_type: action_on_device     # §8.4
  layout: L-pov                   # L-full | L-pov | L-device-dim | L-endcard
  visual: "POV: two finger taps on the back of the phone, the screenshot thumbnail flies into the corner; ripple on the second tap"
  layers: [pov-07, ripple-07]
  pattern: P-06
  transition_in: T-WHIP           # T-WHIP | T-WHIP-S | T-WHIP-L | T-CUT | T-MATCH | T-JUMP | T-BLACK | T-DIM
  camera: zoom-through            # Z preset name or null
  sfx: [{t: 7.38, id: "cinematic-transition-flash-05", beat: 7, on: "transition@7.38", why: "whip into the device"}]
  caption: {profile: CS-1, overrides: []}
  shot_id: SH-2
  fallback_used: null             # FB-n when a fallback replaced the shot
  state_ops: []                   # RS-COUNT: [{var: count, op: add, value: 1, at: 9.96}]
  anchor: {target: "region", box: {x: 380, y: 760, w: 0, h: 0}, follow: none}   # tap point for P-26
  insert: null                    # {id: I1, origin: creator | fetched | created}
```

The reel header:
```yaml
meta:
  format: F-A
  shape: RS-COUNT                 # RS-LIST | RS-COUNT | RS-STORY
  hook_archetype: HA-17           # or HA-02 | HA-10 | HA-14
  hook_variant: H-B               # H-A | H-B (HA-17 only)
  structure: list
  caption_y: mid                  # rule CY: low = 1400, mid = 1270 (written to the tokens.override.json patch)
  count: {var: count, label: "Batches", final: 20}   # RS-COUNT only
  keyword: null                   # the keyword when the CTA is comment_keyword
  cta: end_card                   # end_card | comment_keyword | link_bio | none
  fallbacks: []                   # FB ids used anywhere in the reel
```

---

## §14 Worked examples

Times are planning estimates: take the real ones from the words. They show the standard; match it, then beat it.

### 14.1 RS-LIST, HA-17 H-A, phones: "What they don't tell you about your phone"
**Footage:** SH-1 A-roll; SH-3 hold-up; SH-2 POV × 6 (space-bar trackpad, Back Tap, calculator swipe, burst counter, two
takes of the Back Tap settings); SH-6 macro of the shutter. **Caption height:** `low` (1400): every POV keeps the screen
above y 1300. **CTA:** `end_card`. **Duration:** ~34 s.

**Hook**
| t (s) | Spoken | Tone | Visual | Text | Layout / camera | Cue |
|---|---|---|---|---|---|---|
| 0.00 | "What they" | hype | SH-3 phone swinging up to the lens; Z-4 open punch 1.0 → 1.4 | P-01 "WHAT THEY" pops in f1–f2 | L-full, camera | hook |
| 0.40 | — | hype | P-03 sweep up the held phone (still from 0.3 s) | — | — | — |
| 0.50 | "don't tell you" | hype | — | "DON'T TELL YOU" | — | — |
| 1.25 | "about your phone." | hype | — | "ABOUT YOUR PHONE" | — | — |
| 2.00 | — | hype | T-WHIP-S: Z-5 roll + diagonal blur pass; the title blurs away | — | camera | transitions |
| 2.20 | "Hold the space bar" | explain | **T-WHIP-S** → P-06: thumb on the space bar, the keyboard turns into a trackpad | captions on | L-pov | — |

**Section plan**
| Section | t (s) | Spoken (gist) | Tone | Layout | Pattern | Transition in | Overlay |
|---|---|---|---|---|---|---|---|
| ITEM-1 | 2.2–4.9 | "Hold the space bar and the keyboard becomes a trackpad" | explain | L-pov | P-06 + P-10 | T-WHIP-S | P-26 ripple on the press (2.5) |
| ITEM-1 | 4.9–6.6 | "Fixing typos is so much faster" | win | L-full | P-14 | **T-WHIP-L** out (G-2b) (+ Z-0) | — |
| ITEM-2 | 6.6–7.4 | "Next one:" | hype | L-full | P-15 (holds the phone up) | — | — |
| ITEM-2 | 7.4–10.8 | "Tap the back of your phone twice… it takes a screenshot" | explain | L-pov | P-06 | T-CUT | P-26 on the 2nd tap |
| ITEM-2 | 10.8–13.0 | "You'll find it under Back Tap in the settings" | explain | L-pov | P-09 (scroll to the setting), 2nd take | T-CUT (G-3) | P-22 "Back Tap" |
| ITEM-2 | 13.0–14.6 | "I set mine to the flashlight" | joke | L-full | P-16 (a grin) | T-CUT (+ Z-0) | — |
| ITEM-3 | 14.6–17.8 | "Typed a wrong digit? Swipe the calculator display" | explain | L-pov | P-06 | **T-WHIP** | — |
| ITEM-3 | 17.8–19.4 | "No more clearing everything" | win | L-full | P-14 | T-CUT (+ Z-0) | — |
| ITEM-4 | 19.4–20.4 | "And the best one:" | hype | L-full | P-15 | T-WHIP-L at 19.4 | — |
| ITEM-4 | 20.4–23.4 | "Slide the shutter left and it shoots a burst" | explain | L-pov | P-08 macro of the shutter → | T-MATCH | P-10b snap on "burst" (22.6) |
| ITEM-4 | 23.4–27.6 | "…and it counts every photo" | awe | L-pov | P-12-style hold on the burst counter climbing (the number is on the device), 2nd take | T-CUT (G-3) | P-27 loupe on the counter (24.4) |
| END | 27.6–30.2 | "The attention to detail is wild." | win | L-full | P-16 | **T-WHIP** out (G-2b) (+ Z-0) | — |
| END | 30.2–30.6 | — | cta | — | P-30 cut to black | T-BLACK | — |
| END | 30.6–34.0 | — | cta | L-endcard | P-32 wordmark | — | — |

**Why it works:** the whips at 2.0 (spin, the hook), 4.9 (linear, out of the first result), 14.6 (zoom-flash, into a new
item), 19.4 (linear, into the best one) and 27.6 (zoom-flash, out of the result) each open or close a section, and the kind
changes every time; everything inside an item is a hard cut or the match cut at 20.4. 13 cuts in 34 s, the face on screen
a bit over a third of it. The burst moment is the longest device stretch (20.4 → 27.6), so it runs as a macro, a hand take
and a second take with the loupe, and the best item is last.

### 14.2 RS-COUNT, HA-17 H-B, kitchen gadgets: "Can a $30 blender crush ice twenty times in a row?"
**Footage:** SH-4 lean-in (blender on the counter, presenter beside it); SH-5 locked-off top-down POV into the jar, one file
per batch (20 files, 14 used); SH-1 A-roll; SH-9 reactions. **Caption height:** `mid` (1270), because the blender's control
dial sits in the low band (y 1360–1480) of the SH-5 frame (rule CY: low 61 % overlap, mid 9 %). The counter therefore sits
at cy 1150. **Counter:** `count`, label "Batches", final 20. **CTA:** `comment_keyword`, keyword BLENDER. **Duration:** ~44 s
(re-hook at 22 s).

**Hook**
| t (s) | Spoken | Tone | Visual | Text | Layout / camera | Cue |
|---|---|---|---|---|---|---|
| 0.00 | "Can a thirty-dollar blender" | hype | SH-4 lean-in; P-03 sweep up the blender at 0.3 s (still on the counter), `kind: "device"` | chunk "Can a $30 blender" | L-full | hook |
| 0.90 | "crush ice" | hype | — | chunk "crush ice" | — | — |
| 1.30 | — | hype | Hand presses the pulse button: P-26 ripple | — | — | — |
| 1.60 | "twenty times in a row?" | hype | — | chunk "twenty times in a row?" | — | — |
| 2.20 | — | hype | T-WHIP: Z-1 zoom-through about the jar + P-05 radial blur + flash lift | (hidden on the 3 peak frames) | camera | transitions |
| 2.47 | "Batch one." | explain | **T-WHIP** → P-07 top-down jar, ice shattering | chunk "Batch one." | L-pov | — |
| 3.90 | — | win | The ice turns to snow: **P-18 counter in** "Batches: 1" | — | — | list_cue |

**Section plan and state plan**
| Section | t (s) | Spoken (gist) | Layout | Pattern | Transition | State op |
|---|---|---|---|---|---|---|
| REP-1 | 2.47–5.0 | "Batch one… easy." | L-pov | P-07 | T-WHIP | set 1 @ 3.90 |
| REP-2 | 5.0–6.6 | "Two." | L-pov | P-07 | T-CUT (G-3) | add 1 → 2 @ 6.20 |
| REP-3 | 6.6–8.0 | "Three." | L-pov | P-07 | T-CUT | add 1 → 3 @ 7.60 |
| — | 8.0–10.1 | "The motor's getting warm" | L-full | P-14 (hand on the jug) | **T-WHIP** out (G-2b) (+ Z-0) | (counter stays) |
| REP-5 | 10.1–11.6 | "Five." | L-pov | P-07 | T-CUT | set 5 @ 11.20 (P-20 jump on the cut) |
| REP-6 | 11.6–13.0 | "Six, still crushing." | L-pov | P-07 | T-CUT | add 1 → 6 @ 12.70 |
| — | 13.0–15.2 | "My kitchen sounds like a building site" | L-full | P-16 + P-29 (🔨) | T-CUT | — |
| REP-10 | 15.2–17.0 | "Ten." | L-pov | P-07 | **T-WHIP** | set 10 @ 16.60 |
| REP-12 | 17.0–18.4 | "Twelve." | L-pov | P-07 | T-CUT | set 12 @ 18.00 |
| — | 18.4–22.0 | "Now let's push it all the way to twenty" (re-hook) | L-full | P-14 + Z-2 push | T-CUT (+ Z-0) | (counter stays) |
| REP-15 | 22.0–23.4 | "Fifteen." | L-pov | P-07 | T-CUT | set 15 @ 23.00 |
| REP-16 | 23.4–24.8 | "Sixteen." | L-pov | P-07 | T-CUT | add 1 → 16 @ 24.40 |
| REP-17–20 | 24.8–26.8 | "Seventeen, eighteen, nineteen… twenty." | L-pov | **P-21** step punches on one clamp take, every 0.5 s (1.00 → 1.08 → 1.16 → 1.25 → 1.40) | T-CUT | add 1 @ 24.82 / 25.32 / 25.82 / 26.32 (each a roll, P-19) |
| TURN | 26.8–31.0 | "Look at that. Snow. Every single time." | L-pov | **P-12** (jar close-up, push 1.00 → 1.10); counter out 26.6 | **T-WHIP** | — |
| TURN | 31.0–32.4 | — | L-pov | P-25 "WORKS ✓" in the counter band, on a second take | T-CUT (G-3) | — |
| END | 32.4–37.6 | "Thirty dollars. I'm genuinely impressed." | L-full | P-16 | **T-WHIP** out (G-2b) (+ Z-0) | — |
| END | 37.6–40.0 | "Comment BLENDER and I'll send you the link." | L-full | P-14 | — | — |
| END | 40.0–40.3 | — | — | P-30 | T-BLACK | — |
| END | 40.3–44.0 | — | L-endcard | P-32 + P-33 "Comment BLENDER" | — | — |

**Why it works:** every value the counter shows is a batch the viewer saw, or the jump to it on a cut; it never runs
backwards and it leaves before the snow gets the screen to itself. The counting speeds up into the step punches, so the
TURN lands like a payoff, not a pause. The joke (the building site, one hammer sticker) sits in the middle, and the counter
and the title never meet (H-B has no title).

### 14.3 RS-STORY, HA-14, phones and accessories: "My phone told me I'd left my keys at the café"
**Footage:** SH-1 A-roll (phone in hand); SH-2 POV of the tracker alert on the creator's own phone; SH-8 wide of the café
walk; the friend's message: the creator's screenshot (else a P-23 bubble rebuilt from the exact words). **Caption height:** `low`.
**CTA:** `link_bio`. **Duration:** ~29 s.

| t (s) | Spoken (gist) | Tone | Layout | Pattern | Transition | Notes |
|---|---|---|---|---|---|---|
| 0.00 | "So my phone just saved me forty minutes." | hype | L-full | P-14 + P-02 (chunk at f0), phone swinging in hand | — | HA-14: caption at f0 + moving footage |
| 0.90 | — | hype | L-full | P-15: phone held up to the lens (the strongest image by 1.0 s) | — | — |
| 2.10 | "I got this alert:" | explain | L-pov | P-06: the "left behind" alert on the creator's phone | **T-WHIP** | filmed on the creator's own device = creator footage |
| 4.6 | "'Keys left behind'" | explain | L-pov | P-27 loupe on the alert text | — | the loupe holds 1.4 s |
| 6.0 | "And then my friend texted me" | explain | L-full | P-23 bubble ("are these yours?", initials "S") in the bubble band | T-CUT (+ Z-0) | insert I1: the creator's screenshot via `fx.shot`, else rebuilt |
| 9.2 | "So I walked back" | explain | L-pov | P-13 wide of the café walk | T-CUT | — |
| 13.0 | "The map was spot on" | awe | L-pov | P-06: the map pin on the phone | **T-WHIP** | — |
| 16.4 | "Two tables from where I sat." | win | L-pov | P-12 hold on the found keys + phone | T-CUT (G-3) | the TURN |
| 19.8 | "Best ten-dollar thing I own." | win | L-full | P-16 | T-CUT (+ Z-0) | — |
| 22.5 | "The tracker's linked in my bio." | cta | L-full | P-14 | — | — |
| 24.9 | — | cta | — | P-30 → P-32 + "Link in bio" chip | T-BLACK | card ≤ 5 s |

---

## §15 Your look at the storyboard: the checklist

Watch it once as a stranger with a thumb over the next reel, then once as the editor whose name is on it. Fix what
bothers you, in one pass.

**The style (does it feel like §The feel?)**
- Frame 0: the device is there (≥ 15 % of frame height) with the title phrase or the first chunk, and something is
  already moving; at 25 % scale it still reads.
- The H-A open punch on f1–f5; the title pops phrase by phrase and rides out in the whip; the whip into the device lands
  by 2.5 s.
- At full speed it feels like holding the device: face for the thought, device for the thing, every picture full frame,
  nothing split or boxed.
- Whips only on section changes, in both directions, the kind changing from one to the next, Z-0 after each; inside an
  item, cuts you don't notice.
- Blue only in the hook, red only on the count, cyan only on the device; the POV's colours untouched.
- The best item last; RS-COUNT speeds into the step punches; the TURN is the longest device moment and is followed by the
  face.
- The humour lives on the creator's face; no meme sound anywhere.
- Start to end: you wanted the device, or wanted to try the trick, before the end card.

**Craft (by eye, in context; the framing is in §2 and §3.7)**
- The creator's face reads whenever the moment is about them: the title, counter, captions, chips and bubble sit low,
  the sticker beside the face, no top-band chip or notification on the face shot; nothing chops the head or buries the
  face by accident.
- Rings and ripples sit on the device (tracked, or a still device drifting ≤ 20 px), clear of the head.
- No text over text by accident: captions out of the way under the H-A title; the title and the counter never in one
  frame; nothing in the caption band while captions show; one overlay on a POV.
- Every device line shows the thing on the device, landing on its word; counter ticks on their result; cuts on word
  boundaries; the voice runs continuously under the POVs; nothing teleports, nothing lingers after its point.
- The counter: in on the first op at 1, rolls on every op, never goes down, its final value = the last repetition shown,
  its position constant, gone before the TURN.
- Counts, specs and numbers trace to the footage, the device screen or the script; fetched headlines and posts word for
  word; a "can it" title answered on screen; the CTA keyword readable; device, app and brand names spelt exactly.
- CS-1 as profiled: one quiet line at one height for the whole reel, off the UI being read; UI text that matters is
  legible (big on screen, or a loupe or chip).
- Personal data on device screens blurred; no fallback passed off as the real device.
- The file itself (1080 × 1920, 30 fps, −14 LUFS, the bed under the voice, the end card ≤ 5 s, a hard end) is the
  render's job; it checks it.

---

## §16 Build notes
- **Fonts:** Montserrat (900 italic), Poppins (600, 700, 800), Inter Tight (500, 600, 700), Barlow Condensed (700), all
  bundled. Pre-paint ✓, ✕, ·, $ and ₹ before first use.
- **Determinism:** every frame is a function of its index; streaks, ripples and end-card shards come from seeded noise of
  the frame number; video frames come from `ctx.videoFrame(name, seconds)` only; no CSS animation in scenes.
- **Built in, no scene:** the whip blur, smear and flash (P-05), the cut stage, the dim stage.

The scenes.js recipes for this style's signature pieces:
```js
// P-01 Title Stagger: one phrase at a time, 2 f pop-in with horizontal blur, 2 f blurred crossover, blurred away in the hook whip.
const TITLE = { cy: 1340, out: 2.00, phrases: [{ text: "WHAT THEY", at: 0.03 }, { text: "DON'T TELL YOU", at: 0.50 }, { text: "ABOUT YOUR PHONE", at: 1.25 }] };
function titleLayers(ctx, text, s, op, blur) {          // extrusion, white stroke, gradient fill: three stacked copies
  const font = `italic 900 76px/1 ${ctx.fam("display")}`, g = ctx.tokens.gradients.title.stops;
  const base = `position:absolute;left:64px;width:952px;text-align:center;top:${TITLE.cy - 38}px;font:${font};letter-spacing:.01em;text-transform:uppercase`;
  return `<div style="position:absolute;inset:0;opacity:${op};transform-origin:540px ${TITLE.cy}px;transform:scale(${s.toFixed(3)});filter:url(#hb${Math.round(blur)})">
    <div style="${base};color:${ctx.col("title_shadow")};text-shadow:2px 3px 0 ${ctx.col("title_shadow")},4px 6px 0 ${ctx.col("title_shadow")},0 8px 18px rgba(0,0,0,.35)">${ctx.esc(text)}</div>
    <div style="${base};color:${ctx.col("paper")};-webkit-text-stroke:6px ${ctx.col("paper")}">${ctx.esc(text)}</div>
    <div style="${base};background:linear-gradient(180deg,${g[0]},${g[1]} 55%,${g[2]});-webkit-background-clip:text;background-clip:text;color:transparent">${ctx.esc(text)}</div></div>`;
}
const HBLUR = `<svg width="0" height="0" style="position:absolute">${[0, 4, 8, 12].map(b => `<filter id="hb${b}" x="-10%" y="-50%" width="120%" height="200%"><feGaussianBlur stdDeviation="${b} 0"/></filter>`).join("")}</svg>`;
VEOS.scene({ id: "title", t_in: 0, t_out: TITLE.out + 4 / 30, z: 10, in: "none", out: "none", kind: "lockup", satisfies: ["question", "device"],
  text: true, text_class: "TC-display", lines: 1, roles: ["primary"], text_content: TITLE.phrases.map(p => p.text).join(" "),
  box: { x: 64, y: TITLE.cy - 60, w: 952, h: 120 }, events: TITLE.phrases.slice(1).map(p => p.at),
  render(ctx, lt) {
    const F = Math.round(lt * 30), P = TITLE.phrases, q = b => [0, 4, 8, 12].reduce((a, v) => Math.abs(v - b) < Math.abs(a - b) ? v : a, 0);
    let html = HBLUR;
    P.forEach((p, k) => {
      const a = Math.round(p.at * 30), nxt = k + 1 < P.length ? Math.round(P[k + 1].at * 30) : null, f = F - a;
      if (f < 0 || (nxt !== null && F >= nxt + 2)) return;
      const from = k === 0 ? 0.70 : 0.85, pin = ctx.ease.out(ctx.clamp((f + 1) / 2));          // sharp on its 3rd frame
      const pout = nxt !== null ? ctx.clamp((F - nxt + 1) / 2) : 0;                              // 2 f crossover
      const pw = ctx.clamp((F - Math.round(TITLE.out * 30)) / 4);                                 // blurred away in the whip
      html += titleLayers(ctx, p.text, (from + (1 - from) * pin) * (1 + 0.5 * pw), (0.5 + 0.5 * pin) * (1 - pout) * (1 - pw), q(12 * (1 - pin) + 8 * pout + 12 * pw));
    });
    return ctx.html(html);
  } });

// P-18/P-19/P-20 Counter: one scene for the whole span; value = last op at or before t; odometer roll on each op.
const OPS = [{ t: 3.90, v: 1 }, { t: 6.20, v: 2 }, { t: 7.60, v: 3 }, { t: 11.20, v: 5 } /* … from state_ops */];
const CNT = { label: "Batches", cy: 1150, out: 26.60 };
VEOS.scene({ id: "counter", t_in: OPS[0].t, t_out: CNT.out, z: 6, in: "none", out: "none", text: true, text_class: "TC-display",
  roles: ["accent"], text_content: OPS.map(o => `${CNT.label}: ${o.v}`).join(" / "), box: { x: 200, y: CNT.cy - 48, w: 680, h: 96 },
  events: OPS.slice(1).map(o => o.t - OPS[0].t),
  render(ctx, lt, dur) {
    let i = 0; OPS.forEach((o, k) => { if (ctx.t >= o.t - 1e-6) i = k; });
    const v = String(OPS[i].v), pv = i > 0 ? String(OPS[i - 1].v) : v, p = i > 0 ? ctx.ease.out(ctx.clamp((ctx.t - OPS[i].t) * 30 / 4)) : 1;
    const inP = ctx.ease.out(ctx.clamp(lt / (8 / 30))), outP = ctx.clamp((dur - lt) / (8 / 30)), H = 84;
    const st = `font:700 80px/1 ${ctx.fam("label")};font-variant-numeric:tabular-nums;color:${ctx.col("accent")};-webkit-text-stroke:3px ${ctx.col("counter_stroke")};paint-order:stroke fill;text-shadow:0 3px 8px rgba(0,0,0,.45)`;
    const W = Math.max(v.length, pv.length), a = v.padStart(W, " "), b = pv.padStart(W, " ");
    const digits = [...a].map((c, k) => c === b[k] || p >= 1 ? `<span style="display:inline-block;width:.62em;text-align:center">${c.trim()}</span>`
      : `<span style="display:inline-block;width:.62em;height:${H}px;overflow:hidden;vertical-align:bottom;position:relative"><span style="position:absolute;left:0;right:0;top:${-H * p}px">${b[k].trim()}</span><span style="position:absolute;left:0;right:0;top:${H * (1 - p)}px">${c.trim()}</span></span>`).join("");
    return ctx.html(`<div style="position:absolute;left:200px;top:${CNT.cy - 48 + 24 * (1 - inP)}px;width:680px;height:96px;display:flex;align-items:center;justify-content:center;opacity:${Math.min(inP, outP)};${st}">${ctx.esc(CNT.label)}:&nbsp;${digits}</div>`);
  } });

// P-03 Ring Sweep: box from the anchor pass (output px). A glowing segment runs bottom -> top on both sides in 9 frames.
const RING = { t: 0.30, b: { x: 600, y: 470, w: 250, h: 470, r: 46 } };
VEOS.scene({ id: "ring", t_in: RING.t, t_out: RING.t + 10 / 30, z: 6, in: "none", out: "none", kind: "device", roles: ["highlight"],
  box: { x: RING.b.x - 18, y: RING.b.y - 18, w: RING.b.w + 36, h: RING.b.h + 36 }, events: [4 / 30],
  render(ctx, lt) {
    const f = lt * 30, x = RING.b.x - 14, y = RING.b.y - 14, w = RING.b.w + 28, h = RING.b.h + 28, r = RING.b.r + 14, g = ctx.canvas();
    const head = y + h - (h + 0.3 * h) * ctx.ease.inOut(ctx.clamp(f / 9)), seg = 0.45 * h;      // head climbs past the top edge
    const grad = g.createLinearGradient(0, head, 0, head + seg);
    grad.addColorStop(0, ctx.hexA("highlight", 1)); grad.addColorStop(1, ctx.hexA("highlight", 0));
    g.save(); g.beginPath(); g.rect(x - 30, Math.max(y - 30, head - 6), w + 60, seg + 6); g.clip();
    const path = () => { g.beginPath(); g.moveTo(x + r, y); g.arcTo(x + w, y, x + w, y + h, r); g.arcTo(x + w, y + h, x, y + h, r); g.arcTo(x, y + h, x, y, r); g.arcTo(x, y, x + w, y, r); g.closePath(); };
    g.shadowColor = ctx.col("highlight"); g.shadowBlur = 40; g.lineWidth = 8; g.strokeStyle = grad; path(); g.stroke();
    g.shadowBlur = 18; g.lineWidth = 4; g.strokeStyle = "rgba(255,255,255,.95)"; path(); g.stroke(); g.restore();
    return "";
  } });

// POV clip: lands from the whip (land = true), optional P-10b snap at `snap` (clip seconds) and P-21 steps [{at, s}].
function pov(id, asset, t0, t1, povPt, { kb = [1.0, 1.06], offset = 0, land = true, snap = null, steps = [] } = {}) {
  VEOS.scene({ id, t_in: t0, t_out: t1, z: 1, in: "none", out: "none", kind: "broll", continuous: true, box: { x: 0, y: 0, w: 1080, h: 1920 }, // z1 plate: takes the footage blur
    events: [snap, ...steps.map(s => s.at)].filter(x => x != null),
    render(ctx, lt, dur) {
      const L = land ? ctx.ease.out(ctx.clamp(lt / (3 / 30))) : 1, sn = snap != null ? 1 + 0.25 * ctx.ease.out(ctx.clamp((lt - snap) / (6 / 30))) : 1;
      let st = 1; steps.forEach(s => { if (lt >= s.at) st = s.s; });                       // hard steps, no easing
      const s = (1.15 - 0.15 * L) * ctx.lerp(kb[0], kb[1], lt / dur) * sn * st;   // the land blur is the timeline.blur defocus
      return ctx.html(`<div style="position:absolute;inset:0;background:url(${ctx.videoFrame(asset, lt + offset)}) center/cover;transform-origin:${povPt.x}px ${povPt.y}px;transform:scale(${s.toFixed(4)})"></div>`);
    } });
}
```

**The timeline entries that go with a T-WHIP** at `tCut` (device point `D = {x, y}` in screen px):
`"camera": [{"t": tCut - 7/30, "preset": "zoom-through", "p": {"origin": D}}, …, {"t": <return cut>, "preset": "reset"}]`
(a face out; a POV going out zooms inside its own `pov()` about `povPt`: add a 4 f 1.0 → 1.6 ramp before `t1`),
`"blur": [{"t": tCut - 2/30, "kind": "radial", "amount": 0.3, "at": [D.x, D.y], "frames": 4, "shape": "pulse"}, {"t": tCut,
"kind": "defocus", "px": 14, "frames": 3, "shape": "decay"}]`, `"transitions": [{"t": tCut, "id": "T-WHIP", "type": "flash",
"frames": 7, "pre": 4, "peak": 0.28}, {"t": <return cut>, "id": "T-CUT"}]`, `"stage": [{"t": tCut, "layout": "L-pov", "via":
"cut"}, {"t": <return cut>, "layout": "L-full", "via": "cut"}]`. POV scenes are z1 plates, so the footage blur reaches them.
T-WHIP-S is a `whip` transition (`angle: 60`) + `rotation-snap` 3 f before the cut (`p.origin: D`); T-WHIP-L a `whip`
transition (`dir`) + the 30 % dark `fx.flash`. Never overlap two typed transitions. A POV entered by T-CUT uses
`pov(..., {land: false})`.

---

## Appendix A. Evidence map
The full map (every element → `vNN @ m:ss`), the measurements and the unverified list are in `evidence.md`. Sources: three
of Mrwhosetheboss's reels (v01 an invitation story, 27.8 s; v02 "What they don't tell you about the iPhone", 36.9 s; v03
"Can your iPhone actually see the back of your head?", 45.5 s), their frame sheets, a full-resolution fidelity audit
(6 Oct 2026) and a full-frame-rate motion audit (7 Oct 2026).

| What | Evidence |
|---|---|
| The Title Stagger: 2 f pop-in, blue gradient, white stroke, navy extrusion, cy ≈ 1340, ≈ 77 px | v02 @ 0:00.07–0:01.33 |
| Whips both ways: spin, linear, zoom-flash; the f0 open punch; the POV snap; the step punches | spin v02 @ 1.30, 29.8; linear v02 @ 5.3, 24.4; zoom-flash v02 @ 10.6, 17.9, v03 @ 2.5, 7.9, 37.9; punch v02 @ 0.03–0.17; snap v02 @ 8.2; steps v03 @ 40.2–42.8 |
| The cyan ring sweep, bottom → top | v03 @ 0:00.30–0:00.57 |
| The counter "Reframes: N", red with a dark stroke, above the captions, across cuts, jumping on cuts (5 → 7, 13 → 15 → 16 → 18 → 20) | v03 @ 0:04–0:42 |
| One-line white captions, Poppins-like 600 ≈ 56 px with a black outline, y ≈ 1607 (v02) / ≈ 1273 (v03) | v02 @ 0:02–0:36, v03 @ 0:00–0:45 |
| The message bubble flying out of the phone; the end card (black, a white condensed wordmark, artwork bands) | v01 @ 0:05–0:13; v01 @ 0:22–0:27 |

Not verifiable from the reels: the sound, the exact fonts, the speech language beyond the English burnt-in captions,
whether the backdrops were real sets, whether the POV came from a second camera.

## Appendix B. Hook-title bank
Slots in `{braces}` are filled per reel.

| # | Title phrases (or the hook question) | Hook | Shape | For example |
|---|---|---|---|---|
| 1 | WHAT THEY / DON'T TELL YOU / ABOUT YOUR {DEVICE} | HA-17 H-A | RS-LIST | WHAT THEY / DON'T TELL YOU / ABOUT YOUR PHONE |
| 2 | Can your {device} actually {do X}? | HA-17 H-B | RS-COUNT | Can your phone actually see the back of your head? |
| 3 | I PUSHED / {FEATURE} / TO THE LIMIT | HA-17 H-A | RS-COUNT | I PUSHED / THIS BLENDER / TO THE LIMIT |
| 4 | STOP USING / YOUR {DEVICE} / LIKE THIS | HA-17 H-A | RS-LIST | STOP USING / YOUR PHONE CAMERA / LIKE THIS |
| 5 | {N} {DEVICE} TRICKS / YOU NEVER USE | HA-17 H-A | RS-LIST | 4 PHONE TRICKS / YOU NEVER USE |
| 6 | YOU'VE BEEN / USING {X} / WRONG | HA-17 H-A | RS-LIST | YOU'VE BEEN / USING SCREENSHOTS / WRONG |
| 7 | THE {PRICE} {DEVICE} / THAT BEATS / {RIVAL} | HA-02 | RS-LIST | THE $20 EARBUDS / THAT BEAT / MY $250 ONES |
| 8 | THIS {RESULT} / WAS {MADE} / {N} TIMES | HA-02 | RS-COUNT | THIS PHOTO / WAS EDITED / 20 TIMES |
| 9 | "{Action}." → straight into the device | HA-10 | RS-LIST | "Hold the space bar." |
| 10 | "So my {device} just {did something}." | HA-14 | RS-STORY | "So my phone just saved me forty minutes." |
