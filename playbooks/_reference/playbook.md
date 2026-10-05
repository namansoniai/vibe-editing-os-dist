# Aria Mehta Reel Editing Playbook (v1, "Sage Motion")

**Purpose:** you (Claude) receive talking-head clips of Aria (@fitwitharia) plus her exercise demo clips. Use this document to **ideate and build** every hook, banner, caption, motion graphic, zoom, sound and transition so that the reel **stops a tired desk worker's thumb at frame 0**, shows correct form beyond doubt, and leaves the viewer thinking *"I can do this today."*

**What "Sage Motion" is:** the dense, on-the-word motion-graphics language of her inspiration reel (step rail, clean cards, serif titles, evolving cards, edge labels, bubble, slide-aside) rebuilt **calm and premium-wellness**: soft colours, soft shadows, eased transitions of 8–16 frames, no meme moments, no alarm red. Dense information, quiet delivery. Source answers and the inspiration analysis (rules I1–I19) are in `profile.md`.

**Visual preview** (14 animated frames): `preview/index.html`.

### Creator directives (non-negotiable)
| # | Directive | Where it lives |
|---|---|---|
| D1 | **"I can do this today."** Every reel ends with something the viewer can do now: a move, a swap, a habit. Show how small it is (5 minutes, a chair, no equipment) | §6.2, §7.2, P-17, P-18 |
| D2 | **Trust in correct form.** Every exercise she names is shown in **her own demo clip**, with the form cue drawn on the body (spine line, cue chips, angle arcs). Wrong form is only ever shown as **her own deliberate demo of the mistake**, clearly marked | §8.3 P-01…P-13, §2 M8 |
| D3 | **No gym-bro vibe.** No shouting type, no shakes, no flexing stock footage, no "beast mode" language, no aggressive red. Calm voice, crisp edits | §2 N-list, §4, §9 banned list, §10.2 |
| D4 | **Dense on-the-word motion graphics** (what she loved in the inspiration): every exercise, body part, food, number and step gets its visual 2 f before the word | §2 M6, M7, §8 |
| D5 | **Calmer and premium-wellness:** sage, coral, linen, deep forest; soft shadows; smooth 8–16 f transitions; at most 2 gentle tease beats per reel, never meme sounds | §4, §9, §10, §11 |
| D6 | **Step markers and clean cards** are the signature: the Sage rail + Eucalyptus numeral tile at every item, and evolving rounded cards | §7.1, §8.3 P-35…P-37 |
| D7 | **Truth only:** no fake transformations, no calorie or gram numbers she didn't say, client results only with real data and consent | §2 M14, §8.5, §8.7 |
| D8 | **Two CTAs, always the same:** "comment **PLAN** and I'll DM you the free 7-day plan" + "follow for daily 5-minute fixes" | §6.8, P-43…P-45 |

### Quick index
| § | What |
|---|---|
| §1 | Procedure (do this in order, incl. demo sync, nutrition and consent checks) |
| §2 | Hard rules (MUST / NEVER) |
| §3 | Worlds (Studio, Linen, Forest), screen modes, stage moves, layout, safe zones |
| §4 | Colour system (Sage + Coral, one job per hue, contrast pairs) |
| §5 | Type tokens: Forest Card banner, keyword captions, subtitles, serif titles, hero numbers, tease tags |
| §6 | Hook system: stopper test, Mirror → Fix, result pairs per topic, banner writing, CTA |
| §7 | Structure: Sage rail + numeral tile, item ritual, open loops, calm-crisp rhythm |
| §8 | B-roll & motion graphics: families, 50 patterns P-01…P-50, line → pattern lookup, data rules, assets |
| §9 | Transitions T-01…T-15, grammar, budget, banned list |
| §10 | Motion tokens, zoom system Z-1…Z-7, layers, finishing |
| §11 | Sound: voice-first, optional licensed bed, future soft-SFX pools, ledger, mix |
| §12 | Footage handling (studio tripod, gym selfie, demo camera) |
| §13 | Output contract: beat-sheet schema + checkpoint |
| §14 | Worked examples: desk stretches, belly-fat myth, 8 kg client story |
| §15 | QA checklist |
| App. | Banner bank (10) |

---

## §1 Procedure (follow in order)

1. **Inventory.** `ffprobe` every clip: resolution, fps, duration, audio. Sort clips into setups (§12.1): **A** studio tripod, **B** gym selfie, **C** demo camera. Conform VFR phone footage to 30 fps CFR. Pick one voice track (the talking-head mic; demo clips are usually muted).
2. **Matte** Aria in all A/B talking-head clips (depth sandwich, bubble, cue cloud) and in demo clips used for P-02 form ghost (§12.3).
3. **Transcribe** with word timestamps. Captions are English, sentence case; keep "yaar", "bas" and other Hindi words romanised exactly as spoken. Check every exercise and food name against the glossary (§5.4).
4. **Segment** into `HOOK`, `LOOP`, `ITEM-n` (ordinal words: "first", "number two", "the last one"), `PAYOFF`, `CTA`.
5. **Classify every sentence** with a line type from §8.4 and mark its **trigger word** (the exercise, body part, food, number or verb that the visual lands on).
6. **Tone-tag every sentence:** `lift` · `calm` · `explain` · `warn` · `mock` (= gentle tease) · `awe` · `win` · `cta` (§11.1). A sentence is `mock` only when she gently teases a common mistake ("we've all done the 200-crunches-a-day thing, yaar"). Max 2 `mock` beats per reel.
7. **Demo sync (Aria-specific).** For every exercise named, find its demo clip (setup C). Log: clip, in/out, the **rep onsets** (frame of each rep's bottom/peak), the hold start/end, and whether the clip shows correct form or her **deliberate mistake** take. No demo clip → the exercise gets the P-14 line-art silhouette, and you flag it at the checkpoint ("record: seated cat-cow, side view").
8. **Truth check (Aria-specific).**
   - Numbers: list every number she says (minutes, reps, kg, weeks, grams). Only these may appear on screen. **No calorie or protein number she didn't say.**
   - Nutrition: food names and swaps exactly as she says them.
   - Client stories: real data file + consent confirmed? If not, the client pattern is P-32 "what changed" only, with no photos and no chart.
9. **Pick the result pair** for the hook (§6.4): the viewer's **current state** (slumped, stuck, doing the wrong move) and the **fixed state** (her doing it right, the posture reset, the swap made). Plan the asset for both.
10. **Write 3 banners** (§6.5) and **3 hook variants** (§6.2, §6.6). Recommend one. Run the stopper test (§6.1).
11. **Plan the visual story** for every number, comparison, food and body part (§8.5): which pattern makes the viewer *see* it.
12. **Fill the beat sheet** (§13): one beat per trigger word, an event every ≤ 1.8 s (≤ 1.0 s in the hook). Each beat gets mode, pattern, family, caption, tone, zoom, transition and SFX (empty until she has a library, §11).
13. **Transition map + budgets** (§9.3, §9.4). Sound plan: voice-first + optional bed (§11).
14. **CHECKPOINT** (§13.4), then **wait for approval.**
15. Build act by act, storyboard, QA (§15, max 3 passes), final render.

---

## §2 Hard rules

**MUST**
- M1. **Frame 0 is a thumbnail and a stopper.** It holds ≥ 3 layers: **Forest Card banner + the result pair (or the bad state) + Aria**. At least one element is moving on f0 (the card's soft settle, the spine line drawing, the demo playing). The banner is fully readable on f0.
- M2. **≥ 8 visual changes in the first 3 s** (caption steps, cue chips, a spine line, the light sweep, a card evolve, a zoom).
- M3. **The fix is visible by 2.5 s.** The viewer sees Aria's correct move / fixed state by 2.5 s, not only the problem.
- M4. **The banner obeys §5.2 / §6.5:** ≤ 9 words, ≤ 2 lines, one keyword chip, readable at 25% scale, and saying the same thing as the result pair on screen.
- M5. **Zero dead air.** At most 1 gap ≥ 150 ms per 15 s. A deliberate ≤ 0.4 s breath pause is allowed only before a reveal (it's her calm signature). Jump cuts on word boundaries ±1 f.
- M6. **Literal, on-the-word visuals.** Every exercise, body part, food, number and step gets its visual **2 f before the word** and fully on within ±5 f. Exercise demo cards land within ±2 f of the exercise name. Rep counters tick on the **rep onset in the demo**, not on a timer.
- M7. **Something changes every ≤ 1.8 s** (body) and **≤ 1.0 s** (hook). Nothing is visually static for more than 3.0 s. A calm hold (a stretch demo running with a hold timer) counts as changing only if the timer or breath cue is visibly moving.
- M8. **Form is shown, not described.** Every form cue ("ribs down", "neutral spine", "knees over toes") is drawn on her demo: P-04 spine line, P-11 cue chips, P-03 angle arc or P-02 ghost. Wrong form only from her **own deliberate mistake take**, framed in Clay with ✕ and the label "common mistake".
- M9. **Tone drives treatment.** The comedy layer (Butter tease tags, P-21; soft markup, P-46) appears only on `mock` beats, max 2 per reel, never in the hook's first 1 s and never on a form demonstration of the *correct* move. `calm` beats (stretch holds) get Z-4 or no zoom and the breath cue.
- M10. **SFX ledger is clean** once she has a licensed library: no file > 2× (the list cue may repeat per item), no file on two consecutive cues. **Until then: no SFX at all.**
- M11. **Aria stays on screen or one tap away.** Graphics live in cards, splits, the Forest stage with a panel or bubble, or the depth sandwich. A full-screen graphic **without her** lasts ≤ 3.5 s. Her own demo clip full-screen counts as "her on screen".
- M12. **The face is never covered.** The banner bottom sits ≥ 48 px above her head top. Captions at chest height. Tags and chips never on her face. On demo clips, cue chips never cover the body part they name (leader line instead).
- M13. **Promise integrity.** The banner count equals the items shown ("3 desk stretches" = 3 rail nodes = 3 items). "5 minutes" in the banner = the hold timers/plan actually add up to what she says. The CTA keyword **PLAN** is on screen ≥ 1.5 s in the CTA section.
- M14. **Facts only from her words or her records.** Numbers (kg, weeks, minutes, reps, grams) appear only if she says them. No calories she didn't say. Client data only from her real records with consent. Food labels exactly as spoken.
- M15. **Spelling:** English exact; exercise and food names per the glossary (§5.4); Hindi words romanised as spoken ("yaar", "bas", "chalo").
- M16. **Hold before you cut.** Titles and labels hold ≥ 12 f after building. On-screen text holds ≥ 0.28 s per word.
- M17. **Audio:** −14 LUFS integrated, true peak ≤ −1.5 dBTP. Hard end ≤ 6 f after the last word.
- M18. **Deterministic, frame-based animation:** breath circles, floating cards, parallax and particles come from seeded noise of the frame number.

**NEVER**
- N1. **Fake transformations:** no warped/morphed bodies, no "after" bodies that aren't real, no slimming filters, no before/after pairs with different lighting/poses presented as results. No AI-generated bodies.
- N2. **Contrast failures:** coral or sage *text* on Linen (2.2:1 / 1.5:1); paper text on Sage; light text on her white studio wall without the Forest Card or a soft shadow.
- N3. **Stock gym footage**, especially shirtless or flexing clips, stock "fit people", stock food shots. Every person on screen is Aria (or a consented client); every food shot is hers.
- N4. **Aggressive red alarm graphics:** no flashing red, no warning triangles, no siren colour, no "DANGER" type, no shakes on bad states. Bad = Clay outline + ✕, quiet.
- N5. The same zoom twice in a row; the same transition 3× in a row; the same SFX file on consecutive cues.
- N6. More than 3 bright roles in one frame (Sage + 2). Butter outside the tease layer. Coloured words inside subtitles.
- N7. **Numbers she didn't say:** calories, protein grams, body-fat %, "burns X kcal", "Y% faster". Not even as decoration.
- N8. Transitions outside T-01…T-15 or zooms outside Z-1…Z-7. **Banned outright:** shatter, zoom-blur slam, glitch, RGB split, invert flicker, whip blur, light-leak burns, camera shake, crash zoom, rotation snap, stamps.
- N9. **Meme sounds or meme visuals** (vine boom, "bruh", skulls 💀, clown 🤡, facepalm stickers). Gym-bro language in graphics ("BEAST MODE", "NO EXCUSES", "GRIND").
- N10. A black tail > 0.2 s, or an outro louder than her voice.
- N11. Text layers overlapping (subtitle under a title, chip over the banner).
- N12. Decorative-only visuals. Every graphic shows the thing being said. Medical claims she didn't make ("cures", "heals disc").
- N13. Other gym-goers' faces visible in setup B (blur them, §12.2).

---

## §3 Worlds, screen modes, stage moves, layout, safe zones

### 3.1 Three worlds
| World | Look | Carries | Enter / exit |
|---|---|---|---|
| **Studio** | Aria's footage: white walls, plants, yoga mat (A) or the gym (B). Not regraded beyond matching WB | Claims, cues, asides, gentle teases, CTA | Jump cut, T-02 rise back, zooms |
| **Linen** | `#F7F4EE` with a faint dot grid (`#E4DED3`, 2 px dots, pitch 72 px) | Exercise demo cards, steps, cue chips, swaps, plates, coach notes, myth cards | T-01 soft panel drop in; T-02 rise back or T-05 blur dissolve out |
| **Forest** | Deep Forest `#16211C`, faint sage dot grid (`#B7D3B0` at 8%, pitch 72 px), a 700 px soft radial glow (Sage 12% or Coral 10%) behind the hero element drifting ±16 px | Numbers, timelines, client results, myth → fact reveals, "what actually changed", payoffs | T-08 breath push-through or T-13 soft exposure lift in; T-02 or T-05 out |

Switching worlds is a beat; it lands on an ordinal word ("first", "number two") or a discourse word ("but", "here's the thing", "so").

### 3.2 Screen modes
| Mode | What | Share (per 60 s) |
|---|---|---|
| `HOOK` | Mirror → Fix (§6.2): Forest Card banner + result pair + Aria | 5–8 s |
| `F` | Full-frame talking head + `CAP-SUB`, with Z-1…Z-4 | 25–35% |
| `S` | Linen split: card(s) on top (demo card, swap card, plate), Aria in the panel at the bottom (`P-BLEED` top y 1135, or `P-INSET` x 12–1068, y 1008–1881) | 30–45% |
| `D` | **Demo full:** her demo clip full-frame (it's her), cue chips drawn on it, Aria-talking in the G-4 bubble when she is explaining over it | 10–20% (higher in form reels) |
| `FS` | **Forest stage** split or full: hero number, timeline, myth → fact; Aria in the panel or bubble | 5–20% (higher in client and myth reels) |
| `V` | **Versus split:** left = common mistake (Clay frame ✕), right = correct (Leaf frame ✓), identical crop and timing | ≤ 12% |
| `A` | **Slide-aside:** Aria in x 0–450, a tall card (demo, plate, checklist) on the right | ≤ 12% |
| `I` | Inset card over `F` in the top band (y 300–900) | ≤ 10% |

### 3.3 Linen split layout (`S`)
```
┌─────────────────────────┐ 0
│  (IG top UI, keep clear)│ ← y 0–110
│ ○──●──○  Sage rail      │ ← rail y 132 (nodes Ø 28), x 120–960
│   Seated cat-cow        │ ← serif title band y 190–290 (88 px italic)
│   [chair only] [2 min]  │ ← chips y 296–344
│  ╭───────────────────╮  │
│  │ DEMO CARD (4:5 or │  │ ← card zone x 40–1040, y 360–960, radius 44
│  │ 16:9 crop), cues  │  │   soft shadow 0/12/32 ink 18%
│ [2]╰─────────────────╯  │ ← numeral tile bottom-left of card (x 64, y 860), 150×180
│   ink subtitle here     │ ← CAP-SUB ink, centre y = panel top − 60 (≈1075)
│╭───────────────────────╮│ ← SPEAKER PANEL top y 1135, top radius 56
││   Aria (footage)      ││   x 12–1068, bleeds off the bottom
└┴───────────────────────┴┘ 1920
```

### 3.4 Stage moves
| ID | Move | Recipe | Use |
|---|---|---|---|
| **G-1** | **Soft panel drop** | T-01: full frame eases down into the panel in **10 f** (`ease_in_out`), Linen revealed behind, the card rises 40 px + fades in over 12 f, starting at f4 | Into every item |
| **G-2** | **Rise back** | T-02: panel → full frame, scale 0.94 → 1.02 → 1.00 over 9 f, a 3 px vertical blur on f1–3 only. Linen fades behind | Back to Aria for an opinion, cue, tease or the CTA |
| **G-3** | **Slide-aside** | T-03: the panel narrows to x 0–450 (rounded right corners 48) in **10 f**; the card grows in x 470–1050 | "Look at this", plate builder, checklist, tall demo |
| **G-4** | **Bubble** | T-04: footage → Ø 300 circle at bottom-left (centre x 210, y 1560), 6 px paper ring, soft shadow 0/10/28, in 10 f with a gentle overshoot (1.06). Reverse to return | Full-screen demo (`D`) or Forest stage while she explains |
| **G-5** | **Depth sandwich** | Aria's matte drawn **in front of** the card; she overlaps its bottom edge or corner by 60–140 px; card parallax ±10 px | Hook, hero numbers, the "fixed" reveal |
| **G-6** | **Cue cloud** | P-41: 4–6 soft-blurred exercise/food cards float behind her matte (blur 6 px, 70% opacity, drift ±10 px, 1 cycle / 6 s) | Intros of a list ("I've got three for you"), "all of these" lines |

### 3.5 Forest stage (`FS`) spec
- **Background:** `#16211C` + sage dot grid at 8%, pitch 72 px. One soft radial glow (700 px, Sage 12% or Coral 10%) behind the hero element, drifting ±16 px over 4 s.
- **Graphic zone:** x 48–1032, y 170–1060. Aria in a `P-INSET` panel or the G-4 bubble. Captions: paper `CAP-SUB` at panel top − 60.
- **Glow rule:** glow only on the hero element and the state change (week 0 → week 12). Everything else flat.
- **Honesty:** every number is from her words or her client records (M14). Same axes for any comparison.

### 3.6 Safe zones (Instagram)
- Key text within x 64–1016, y 110–1500. Bottom ≈ 380 px and right ≈ 110 px are UI-covered; only the speaker panel, bubble or her body may live there.
- **Banner:** top edge y 150 (range 140–200).
- **Captions:** centre y 1150–1450 (default 1300 in `F`).
- **Bubble:** bottom edge above y 1740.
- **Demo cue chips:** inside x 64–1016 even when the body part is near the edge; use a leader line.

---

## §4 Colour system (soft, each hue has one job)

### 4.1 Palette
| Role (tokens.json) | Name | Hex | One job | Text on it (contrast) |
|---|---|---|---|---|
| `primary` | **Sage** | `#B7D3B0` | Read this: banner keyword chip, keyword highlight swipe, rail fill, list highlights, CTA chips | `ink` (9.6:1) |
| `accent` | **Warm Coral** | `#F2896B` | Warmth and "the fix": light sweep, active rail node, PLAN key, muscle glow, underline swipe | `ink` (6.3:1). **Never as text on Linen** |
| `bad` | **Clay** | `#A94A3C` | The common mistake: ✕ frames, soft mistake outlines, "myth" tag, slumped spine line | `paper` (5.6:1); as text on Linen 5.1:1 |
| `good` | **Leaf** | `#2E7A55` | Correct form, ✓, fixed posture, "fact", completed rail nodes, real progress | `paper` (5.2:1); as text on Linen 4.75:1 |
| `data` | **Mist Blue** | `#8DB3D4` | Numbers and time: hold timers, rep rings, timelines, chart lines, breath cue | `ink` (7.0:1) |
| `concept` | **Eucalyptus** | `#2D6466` | Step numeral tiles, exercise/concept names on chips, coach-note tags | `paper` (6.7:1) |
| `comedy` | **Butter** | `#F5D77E` | **Gentle tease layer only** (P-21 tags), `mock` beats | `ink` (11:1) |
| `ink` | Forest Ink | `#1E2622` | Text, banner card fill, strokes | — |
| `paper` | Paper | `#FFFFFF` | White text, cards, chips, bubble ring | — |
| `canvas` / `grid` | Linen / Linen grid | `#F7F4EE` / `#E4DED3` | Linen world | — |
| `night` | Deep Forest | `#16211C` | Forest stage | — |

Gradients (numeral tiles, hero glows, sweep only):
- Sage `#D6E7D1 → #B7D3B0 → #86AC80`
- Coral `#F9B9A4 → #F2896B → #D9674A`
- Leaf `#6FB08C → #2E7A55 → #1F5A3E`
- Eucalyptus `#4F8C8E → #2D6466 → #1D4546`

### 4.2 Meaning
- **Sage** = read this / do this / the brand.
- **Coral** = warmth, the fix arriving, the action (PLAN).
- **Clay → Leaf** is the **mistake → correct** axis (soft red → green, never alarm red).
- **Mist Blue** = time, reps, numbers.
- **Eucalyptus** = names and steps.
- **Butter** = it's a gentle joke.

### 4.3 Rules
- Max **3 bright roles per frame** (Sage + 2). Clay and Leaf together count as 2 (versus frames).
- One hue per caption block. Subtitles are never coloured.
- On Linen, coloured *text* is only Clay, Leaf or Eucalyptus (all ≥ 4.5:1); Sage and Coral appear only as **fills** with ink text.
- On her white studio wall, every text block either sits on the Forest Card / a paper chip, or switches to `ink` text with a paper halo (the light-background rule, §5.5). Paper text with the soft shadow (0/4/16, ink 45%) is only for dark areas of the footage.
- Footage is not regraded beyond matching WB/exposure between A, B and C. Never tint her skin.
- Shadows are **soft only** (0/12/32 at 18% ink for cards, 0/4/16 at 45% for text). No hard offset shadows, no strokes on type.

---

## §5 Type tokens

### 5.1 Font map (all bundled, OFL)
| Slot (tokens) | Font | Weight | Role |
|---|---|---|---|
| `display` | **Plus Jakarta Sans** | 800 | Banner, edge labels, glow keywords |
| `chunky` | **Jost** | 600 | Keyword captions (the "big word" system; not chunky by design) |
| `body` | **Plus Jakarta Sans** | 700 | Subtitles, sentence case |
| `numeric` | **Inter Tight** | 300 (hero), 600 (tiles) | Hero numbers, numeral tiles, timers |
| `serif` | **Instrument Serif** | 400 italic | Exercise/topic titles, coach notes, quotes, emphasis lines |
| `marker` | **Instrument Serif** | 400 italic | Soft mistake notes (P-46) |
| `kinetic` | **Inter Tight** | 600 | Form-cue kinetic words ("ribs down") |
| `ui` | **Jost** | 500 / 600 | Chips, rail labels, tags, plan pills |
| `pixel` | **Jost** | 500 | Unused (no pixel type in this style) |
| `mono` | **JetBrains Mono** | 400 | Timer digits texture only ("00:30") |

### 5.2 `CAP-BANNER`: the Forest Card (first thing people read)
| Property | Spec |
|---|---|
| Card | `ink` fill at 94%, **no stroke**, soft shadow 0/12/32 ink 22%, radius 32, rotation 0. x 56–1024, top y **150**, height auto (2 lines ≈ 210 px), padding 34/40 |
| Text | `paper`, Plus Jakarta Sans 800, **60–70 px**, line height 1.08, tracking −1%, centred. ≤ 9 words, ≤ 2 lines. **Sentence case** |
| Keyword chip | 1–3 words inside the card, chip radius 18, padding 4/18. Default: `primary` Sage fill + ink text. `bad` Clay + paper (the mistake: "CRUNCHES"), `good` Leaf + paper (the fix), `data` Mist + ink (numbers: "5 MINUTES", "8 KG") |
| Emoji | ≤ 1, at a line end, calm set only: 🌿 ✨ 🧘‍♀️ 🥗 ✅. Never 🔥💀🤡💥 |
| Underline | A Coral swipe (6 px, rounded caps) wipes under the chip L → R over 10 f **when the chip word is spoken** |
| f0 | **Fully readable on frame 0** at scale 1.03 and opacity 1, settling to 1.00 by f8 (ease_entry). Shadow blur grows 16 → 32 over f0–f8 |
| Life | Chip breath (1.0 → 1.06 → 1.0 over 10 f) on the spoken keyword. **Chip flip** (T-11 mini, 8 f) at the fix beat: "CRUNCHES" (Clay) → "DEAD BUGS" (Leaf), "MYTH" → "FACT". One flip max |
| Exit | Glides up 60 px + fades over 8 f at the hook's end, or blurs out inside T-01. Never a hard pop mid-sentence |
| Duration | The hook (≥ 0.28 s per word, minimum 2.5 s, maximum 8 s) |
| Variants | **B-FIX** "Stop doing [CRUNCHES] – do this instead" (chip flips Clay → Leaf). **B-NUMBER** "[3] desk stretches for your lower back" (Mist chip). **B-MYTH** "Belly fat? It's [NOT CARDIO]" (Clay chip → Leaf flip). **B-STORY** "[8 KG] in 12 weeks: what we changed" (Mist chip) |

### 5.3 `CAP-KEY` (keyword captions: hook, list intros, CTA)
- Jost 600. Keyword line **110–130 px**; helper line **54–64 px** (Jost 500) above it.
- On footage: `paper` with the soft text shadow (or `ink` + paper halo over her white wall, see the light-background rule in §5.5); the keyword sits on a **Sage highlight swipe** (a rounded rectangle wiping in L → R behind the word over 8 f, height 70% of the cap, 85% opacity) with ink text. On Linen: ink text, same swipe.
- Left-aligned at x 72 under the hook card (inspiration I1) or centred in `F`; block y 1220–1500.
- Words append on onsets with a 6 f rise (+18 px → 0, opacity 0 → 1, ease_entry). Blocks clear with a 4 f fade, never a 1-frame pop.
- No squash, no stroke, no hard shadow.

### 5.4 Language rules and glossary
- **English captions, sentence case** ("Bas 5 minutes, yaar"). Proper nouns capitalised. The CTA keyword **PLAN** is always caps.
- Hindi words romanised exactly as spoken, never translated, never italicised in subtitles: yaar, bas, chalo, accha, thoda, roti, sabzi.
- Banner language: English, sentence case + one chip.
- **Glossary (exact spelling):** Aria Mehta · @fitwitharia · PLAN · cat-cow · seated cat-cow · thoracic extension · hip flexor stretch · figure-4 stretch · glute bridge · dead bug · bird dog · plank · crunches · paneer · tofu · dal · rajma · chana · roasted chana · moong · sprouts · curd · Greek yogurt · soya chunks · besan chilla · whey · desk workers · 7-day plan.
- Units as she says them: "8 kg" (space, lowercase kg), "12 weeks", "5 minutes", "30 seconds".

### 5.5 `CAP-SUB` (subtitles: every word of talking sections)
- Plus Jakarta Sans 700, **50–56 px**, **sentence case**, 2–4 words per card, swap with a 3 f blur dissolve.
- `paper` with soft shadow on Forest and on dark footage (gym, dark clothing); `ink` on Linen.
- **Light-background rule (her white studio wall):** measure the mean luminance of the caption box area on the footage. If it is > 0.6 (white wall, light top), use `ink` text with a paper halo (0/0/30, paper 80%) instead of paper + shadow. Applies to `CAP-SUB`, `CAP-KEY` helpers and emphasis lines. Never white text on her white wall or on her face.
- Centre y 1300 in `F`; in `S` / `FS`, at panel top − 60.
- Hidden under `CAP-KEY`, serif emphasis lines, edge labels, during T-01 / T-02 / T-08, and during the hook (the hook uses `CAP-KEY`).

### 5.6 Serif titles, edge labels, emphasis lines
- **Serif title (P-35):** Instrument Serif italic 88 px, ink on Linen / paper on Forest, typed 1 letter / 2 f with blur 8 → 0 px, above the card (y 190–290). Holds the whole item.
- **Edge labels (P-37):** Plus Jakarta Sans 800, 96 px, paper with soft shadow, on the demo card's bottom edge, swapped per spoken noun with a 6 f blur cross-swap ("hips" → "ribs" → "breath").
- **Emphasis line:** Instrument Serif italic 96–110 px, paper on footage (soft shadow), one short phrase ("it's not cardio."), fades in word by word, 8 f each. Replaces the inspiration's red kinetic "MAT BHOOLNA" (I12). Max 2 per reel.

### 5.7 Kinetic form cues (`KT-CUE`)
- Inter Tight 600, 64–80 px, ink on a paper pill (radius 999, padding 10/26) with a 2 px Leaf leader line to the body part.
- Pops in by scaling 0.92 → 1.0 + fade over 7 f (ease_entry); leader line draws over 8 f after.
- Used for "ribs down", "knees out", "chin tucked", "exhale".

### 5.8 Soft mistake note (`CAP-NOTE`, `mock` or `warn` beats)
- Instrument Serif italic 56–68 px, Clay on Linen / paper on footage, rotation −2…+2°.
- Paired with a **thin Clay outline** (4 px, rounded, drawn with `stroke-dashoffset` over 12 f) around the mistake area, plus a small ✕ in a Clay circle (Ø 44).
- Examples: "hips sagging", "neck doing the work", "we've all been here".

### 5.9 Hero numbers (`HERO-NUM`)
- Inter Tight **300**, 240–420 px, paper on Forest with a soft Sage glow (0/0/40, 35%), ink on Linen. Unit in Jost 500 at 35% of the numeral size ("8 kg", "12 weeks").
- Always counts (ease-out over 24–30 f) or ticks per real data point.
- Lands with a Z-5 settle nudge (3 px, 6 f). Only numbers she says.

### 5.10 Tease tags (`TAG-TEASE`, `mock` beats only)
- A 1–5 word Butter pill (ink text, Jost 600 52 px, radius 999) with a 1 small calm emoji max (🙈 😅 🫠), soft shadow, rotation ±3°.
- Pops 0.9 → 1.04 → 1.0 over 8 f, sways ±1.5° for 18 f.
- ≤ 1 on screen, ≤ 2 per reel, never on the face, never during a correct-form demo. Examples: "200 crunches a day 😅", "we've all done this 🙈", "cardio queen era".

---

## §6 Hook system

### 6.1 The stopper test (run it on frame 0 and on 0–3 s)
1. **Thumbnail test:** frame 0 at 25% scale still shows *what this is about*: the Forest Card is readable, and the problem (slumped spine, crunch, belly-fat myth card) plus Aria are visible.
2. **Mute test:** sound off, the first 3 s still tell the story: problem → her fix.
3. **1-second read:** the banner reads in ≤ 1.5 s (≤ 9 words).
4. **Change count:** ≥ 8 visual changes in 0–3 s and ≥ 1 moving element on f0.
5. **Feed-contrast test:** in a strip of 6 fitness reel thumbnails (mostly loud yellow/red text on gym footage), ours is the calm one that still pops: the dark Forest Card on her white wall + one Sage chip + her body in a clear posture.
6. **Bro test:** would this frame look at home on a gym-bro account? If yes, it fails (loud colour, shouting type, shaking camera, flexing).

### 6.2 Mirror → Fix (the default hook)
Spoken pattern (Aria): "*If your lower back hurts after a workday* [mirror]… *do these 3 stretches right at your desk* [fix]."

| t | Beat | Tone | Visual | Caption | Zoom / move | Sound |
|---|---|---|---|---|---|---|
| **f0** | Stopper frame | lift | **Forest Card** settled-in (B-NUMBER or B-FIX) + the **mirror state** in the top band: P-14 desk-posture silhouette slumping with a Clay spine line (or her deliberate-mistake demo in a card with a Clay ✕ frame), tilted 2° + **Aria** cut-out overlapping its bottom-right corner (G-5), already mid-sentence | — | Card settles 1.03 → 1.00 over 8 f; silhouette slumps continuously | Voice only (dry) |
| 0.1–1.2 | "If your lower back hurts after sitting all day…" | warn | **P-16 pain spot**: a soft Clay pulse at the lower back (2 slow pulses, 18 f each). **P-15 sitting clock** sweeps if she says hours | KEY "after sitting / **ALL DAY**" | Z-4 breath drift on Aria | — |
| 1.2–1.8 | "…you're not lazy, yaar" (tease, optional) | mock | P-21 Butter tag "we've all been here 🙈" beside her shoulder (once) | KEY "**not lazy**" | Z-2 glide-in (soft) | — |
| 1.8–2.5 | "…here's the fix" (pivot) | awe | **T-10 Coral light sweep** across the card: the slumped silhouette resolves into **her correct demo** (stretch in motion), spine line turns Leaf and straightens over 12 f. **Chip flip** if the banner has one | — | Z-3 pull-out reveal | Bed enters here if licensed (§11) |
| 2.5–4.5 | "…3 stretches you can do at your desk in 5 minutes" | lift | **P-17 5-minute pill** fills; **3 rail nodes** draw in at the top (preview of SM-1); P-39 badge "chair only" | KEY "**3 stretches** / at your desk" | Z-1 soft punch on "3" | — |
| 4.5–6.5 | Loop ("the third one is the one everyone skips") | lift | Third rail node pulses Coral; G-6 cue cloud of the 3 demo stills floats behind her | KEY "everyone **skips** #3" | Z-4 | — |
| ≤ 7 | Exit | — | Banner glides up; T-05 blur dissolve → T-01 soft panel drop into item 1 on "First" | — | — | — |

**Never skip the fix.** Even if the script's hook only names the problem, her correct move appears by **2.5 s** (M3). That fix-on-screen is the trust signal (D2).

### 6.3 Visual stopper devices (VS, combine 2–3 in a hook)
| ID | Device | Recipe |
|---|---|---|
| VS-1 | **Mistake card with soft markup** | Her deliberate-mistake demo in a Clay-framed card + P-46 outline + serif note ("neck doing the work") |
| VS-2 | **Depth sandwich** | Aria's matte in front of the demo card (G-5), parallax ±10 px |
| VS-3 | **Spine line morph** | P-04: Clay curve straightens into a Leaf line on her demo in 12 f |
| VS-4 | **Coral light sweep** | T-10: mistake → correct demo in 16 f |
| VS-5 | **Versus from f0** | Mode V: left mistake (Clay ✕), right correct (Leaf ✓), divider draws top → bottom on f0–10 |
| VS-6 | **Myth card on f0** | P-19 card "Myth: more cardio = less belly fat" already in place, a Clay "myth" tag pulsing; flips at the pivot |
| VS-7 | **Real number on f0** | B-STORY: "8 kg" hero number + 12-week rail (client reels only, real data) |
| VS-8 | **Body glow map** | P-05: line-art body with the target area glowing Coral on f0 |

### 6.4 Result pairs by topic (pick one per reel; the most important table)
| Topic (her reels) | Mirror / mistake state (Clay) | Fix / correct state (Leaf) | How each is shown | Pair pattern |
|---|---|---|---|---|
| **Lower back + desk stretches** (idea 1) | Desk worker slumped, rounded lower back, a Clay pain pulse | Aria doing seated cat-cow at a chair, neutral spine, Leaf spine line | Mirror: P-14 silhouette (or her slump take). Fix: her demo clip + P-04 | P-14 → T-10 → P-01 + P-04 |
| **Belly fat, not cardio** (idea 2) | Myth card "More cardio = less belly fat" with a treadmill silhouette running in place | Fact card in her words ("it's not cardio") + the things she names (e.g. strength, protein, sleep) stacking | P-19 myth card flip + P-23 balance scale | P-19 → P-23 |
| **Vegetarian protein swaps** (idea 3) | A plate/thali with only the foods she calls low-protein (e.g. plain rice + aloo) | The same plate after her swaps (e.g. dal, paneer, curd) dropping in | P-27 thali map, same plate same axes, items swap in place | P-25 swap card ×4 |
| **Stop crunches** (idea 4) | Her deliberate crunch take: neck pulled, Clay outline at the neck, Clay ✕ | Her dead bug (or whatever she names) with ribs down, Leaf ✓, cue chips | Mode V versus with identical crop and timing | P-10 + P-46 → P-11 |
| **Client 8 kg in 12 weeks** (idea 5) | Week 0 on a 12-week rail (start weight only if she gives it) | Week 12 with "8 kg" counted; **real** consented photos only, same pose and light | P-29 timeline + P-38 hero number; P-31 only with consent | P-29 + P-32 |
| Neck / "tech neck" | Head forward over a laptop, Clay angle arc at the neck | Chin tuck, ears over shoulders, Leaf vertical line | P-14 + P-03 | P-47 |
| Plank / core form | Hips sagging (Clay outline at the hips) | Straight line shoulder–hip–heel (Leaf line) | Her two takes, Mode V | P-10 + P-04 |
| Squat / knees | Knees caving (Clay arrows inward) | Knees tracking over toes (Leaf arrows) | Her two takes + P-11 "knees out" | P-10 + P-11 |
| "No time" | A packed calendar (her words) | A 5-minute block slotted in, ticked | P-17 + P-18 | P-18 |

### 6.5 Banner writing (the first thing people read)
**Formula:** `[viewer-pointed problem or promise] + [ONE CHIP] + [≤ 1 calm emoji]`, ≤ 9 words, sentence case, matching the result pair on screen.

| Template | Example |
|---|---|
| **Number + body part** (B-NUMBER, default for listicles) | "[3] desk stretches for your lower back 🌿" |
| **Stop → do** (B-FIX, form corrections) | "Stop doing [CRUNCHES]. Do this instead" (chip flips → "DEAD BUGS") |
| **Myth** (B-MYTH) | "Not losing belly fat? It's [NOT CARDIO]" |
| **Story** (B-STORY) | "[8 KG] in 12 weeks: what we actually changed" |
| **Swap** | "[4] easy protein swaps, fully veg 🥗" |
| **Time promise** | "Fix desk back pain in [5 MINUTES]" |
| **POV** | "POV: you sit 9 hours and your back [HATES YOU]" |

- **Count banners:** the validator (M13) reads the first number in the banner as the item count. When the banner's number is not the item count ("8 KG in 12 weeks"), set `meta.count` in the timeline to the real number of ITEM sections.
- **Write 3, pick by the stopper test;** the others go to Trial Reels.
- **Banned:** "NO EXCUSES", "BEAST MODE", "SHRED", "BURN FAT FAST", any calorie number, "guaranteed", more than 1 emoji, counts that don't match the items, medical claims ("cure", "heal").

### 6.6 Other hook formulas (all must show her fix by 2.5 s)
| ID | Formula | Example from her topics |
|---|---|---|
| HF-1 | **Mirror → Fix** (default, §6.2) | "If your lower back hurts after work…" → seated cat-cow |
| HF-2 | **Myth flip** | "More cardio won't fix belly fat." Myth card on f0 → flips to fact at 1.8 s (idea 2) |
| HF-3 | **Stop → Do** | "Stop doing crunches." Mode V from f0: crunch ✕ left, dead bug ✓ right (idea 4) |
| HF-4 | **Real result first** | "My client lost 8 kg in 12 weeks." Hero "8 kg" counts on f0–24 + rail (idea 5) |
| HF-5 | **Swap reveal** | "You're eating enough roti, but not enough protein." Plate → swap pill flips (idea 3) |
| HF-6 | **Gentle tease** | "200 crunches a day? Bas, yaar." Butter tag + her crunch take, fix by 2.5 s |
| HF-7 | **Time ask** | "Give me 5 minutes and your back will thank you." 5-minute pill fills while she demos |
| HF-8 | **POV desk worker** | "POV: it's 6 pm and your back is done." Silhouette slump → her stretch |

### 6.7 Hook sound
- Voice only, dry. No meme hits, no risers.
- If she supplies a licensed bed: it enters softly on the fix beat (≈2 s) at −24 dB under the voice and settles at −22 dB.
- Once she has a licensed SFX library (§11.4): ≤ 3 soft cues in the hook (a soft whoosh on the light sweep, a soft pop on the rail, a pluck on the count), each a different file.

### 6.8 CTA formula
1. **Early loop** (5–12 s, `CAP-KEY`): "the free 7-day plan is at the end" → helper "free 7-day plan" + keyword "**at the end**".
2. **End CTA:** Aria rises back (G-2) for "comment **PLAN** and I'll DM you the free 7-day plan".
   - **P-43 Plan card:** a paper card "Free 7-day plan" with 7 day pills (Mon…Sun) filling Sage one by one (3 f stagger).
   - **P-44 PLAN key:** "PLAN" on a soft Coral rounded key (radius 28, soft shadow) that presses down 8 px over 6 f and releases; a comment bubble types "PLAN" (1 letter / 2 f); the plan card then glides into a DM bubble (16 f arc).
   - PLAN is on screen ≥ 1.5 s (M13).
3. **Follow chip (P-45):** "follow for daily 5-minute fixes · @fitwitharia" paper chip in the top band, rising 8 f; holds to the end.
4. Hard end ≤ 6 f after the last word (T-14). The CTA is tone `cta`: calm, no tease.

---

## §7 Structure devices

### 7.1 Step / item markers (SM-1 + SM-2 together is the default)
| ID | Marker | Recipe |
|---|---|---|
| **SM-1** | **Sage rail** (signature, from I4) | N nodes (Ø 28, 2 px ink-40% outline, Jost 600 numerals 16 px) on a dashed line (2 px, dash 6/6) at y 132, x 120–960. **Active** node: Coral ring + scale 1.25 (8 f). **Done** node: Leaf fill + paper ✓. The connector fills solid Sage L → R over 12 f as each item starts. Visible on Linen and Forest for the whole list; a 30% ghost in `F` |
| **SM-2** | **Eucalyptus numeral tile** | 150×180 tile (radius 28, Eucalyptus gradient, soft shadow), Inter Tight 600 numeral 120 px paper, bottom-left of the card (x 64, y 860). Rises 40 px + fades in over 10 f on the ordinal word, holds ≈1.2 s, then shrinks to 70% and docks at the card corner for the rest of the item |
| SM-3 | Serif item title | The P-35 title alone is the marker (full-width demo cards) |
| SM-4 | Day pills | 7 pills (Mon–Sun) for plan/habit reels; the active day fills Sage |
| SM-5 | Swap counter | "swap 1/4" pill in the top band (Jost 600); the number ticks on the ordinal word |
| SM-6 | Week rail | 12 week dots for client stories; dots fill Leaf as the story moves (P-29) |

### 7.2 Item ritual (identical for every item)
1. **G-1 soft panel drop** (or T-08 push-through into Forest) starting 0–10 f before the ordinal word. List cue sound only if licensed.
2. **Rail:** connector fills, active node rings Coral. **Numeral tile** rises (SM-2).
3. **Serif title** types the exercise/food name **on the name** (±2 f) + chips ("chair only", "30 sec each side").
4. **Demo card** plays her correct demo (P-01). 2–4 evolving beats, one per cue: cue chips (P-11), spine line (P-04), rep ring (P-06) or hold timer (P-07), edge labels (P-37). Every ≤ 1.8 s.
5. **Rise back (G-2)** to Aria for the "why it works" or a gentle tease, with Z-1 or Z-2.
6. **"Today" tick:** the rail node turns Leaf ✓ on the item's last word.

### 7.3 Open loops
- Count loop: rail nodes visible from the hook; the viewer sees how many are left.
- "The last one is the one everyone skips" / "the swap nobody talks about".
- Deliverable loop: "free 7-day plan at the end" (paid off by P-43).
- Client loop: "and it wasn't the diet you think" (paid off by P-32).
- Every loop is paid off on screen (M13).

### 7.4 Rhythm: calm voice, crisp edits
- **Every 8–12 s a human beat:** a rise back to Aria for a warm aside, a gentle tease (max 2 per reel), or a "you can do this" line to camera. It must also carry information.
- **Never two tease beats back to back;** at least one `explain` or `win` beat between them.
- **Calm holds are allowed** during stretches: the demo runs with a moving hold timer and breath cue (P-07, P-08) for up to 3 s without a new element.
- **Energy curve:** hook (crisp) → item 1 (clear, slow enough to copy) → middle items (steady, alternate Linen ↔ Studio) → last item (the "everyone skips" one: Forest stage or Mode V, the biggest visual) → payoff ("today" checklist P-18) → CTA (warm, confident).

---

## §8 B-roll and motion-graphics system

### 8.1 Families
| ID | Family | What | Assets Aria must supply |
|---|---|---|---|
| B-1 | **Demo clip card** | Her exercise demo in a rounded card or full-frame (mode D) | Camera C: each exercise **side view + front view**, 3 clean reps or a 10 s hold, 2 s still in the start position, plain background (yoga mat, white wall), 1080×1920 or 4K landscape, 30/60 fps |
| B-2 | **Mistake take** | Her own deliberate wrong-form rep, clearly marked | Camera C: same framing as the correct take, 2 reps of the common mistake (crunch neck pull, sagging plank, rounded back) |
| B-3 | **Body line-art** | Procedural silhouettes: desk posture, muscle map, spine | Built live (no assets) |
| B-4 | **Form overlays** | Spine lines, angle arcs, cue chips, range arcs, ghosts | Built live on B-1/B-2 (needs her matte) |
| B-5 | **Timers & counters** | Hold timers, rep rings, 5-minute pills, sitting clock | Built live |
| B-6 | **Food & plate** | Her own food B-roll + line-art thali/plate | Camera C top-down: paneer, dal, curd, chana, soya chunks, tofu, sprouts, besan chilla, a typical lunch plate; 5 s each on a light surface, daylight |
| B-7 | **Myth/fact cards** | Paper cards that flip | Built live |
| B-8 | **Client story** | Week rail, real chart, consented photos, "what changed" stack, quotes | Her records (dates, weights), client written consent, photos taken same angle/light; real client quote text |
| B-9 | **Coach note card** | Paper note "Coach note:" with typed text | Built live |
| B-10 | **Chips & badges** | "chair only", "no equipment", "30 sec", Leaf ✓, Clay ✕ | Built live |
| B-11 | **Desk-life B-roll** | Her desk, chair, laptop, water bottle; "6 pm" moments | Camera C: 3–5 s each, her own desk (no brand logos) |
| B-12 | **Hero numbers & charts** | Forest stage numerals, timelines, habit grids | Built live from her real numbers |
| B-13 | **Tease layer** | Butter tags, soft mistake markup | Built live; `mock` beats only |
| B-14 | **CTA kit** | Plan card, PLAN key, DM bubble, follow chip | Built live; the plan PDF's real title |

**Family rules:** ≥ 4 families per 60 s. Same family ≤ 10 s straight (a stretch demo may run 12 s if timers move). B-1 is mandatory for every exercise named (M8). B-13 only on `mock` beats.

### 8.2 Staging choreography
Lead −2 f → land ≤ 7 f (soft entries) → read 0.8–1.8 s (something moves inside: the demo, a timer, a line drawing) → **evolve** (add a cue, draw a line, flip) or **swap** (T-06 card push). Evolve inside an item; swap between items.

### 8.3 Pattern specs (30 fps)

**Body & form (B-1, B-2, B-4)**
| ID | Pattern | What's on screen | Motion | Use when she says… |
|---|---|---|---|---|
| **P-01** | **Demo card** | Her demo clip in a rounded card (radius 44, 4:5 crop, soft shadow) in the card zone; serif title above, numeral tile docked | Card rises 40 px + fades 12 f; the clip plays from the start position on the exercise name | Any exercise name |
| **P-02** | **Form ghost** | Her correct-form matte at 30% paper tint ghosted **over** her mistake take, aligned at the hips; the gap between the two bodies is visible | Ghost fades in 10 f, then a cross-dissolve of the two **real** takes over 14 f (never a warp) | "Your back should end up here" |
| **P-03** | **Angle arc** | A thin arc (4 px) at a joint (knee, hip, neck) between two limb lines; Leaf when right, Clay when wrong; degree number only if she says it | Arc draws 10 f; limb lines draw 6 f each from the joint | "Knee at 90", "chin tucked", "hinge at the hips" |
| **P-04** | **Spine line** | A smooth 6 px line traced along her spine on the demo: Clay curve (rounded) → Leaf straight (neutral) | Draws top → bottom 12 f; morphs Clay → Leaf over 12 f on the fix word | "Neutral spine", "your back rounds", posture |
| **P-05** | **Muscle glow map** | Front/back line-art body (paper lines on Forest, ink on Linen); the named muscle fills with a Coral glow | Body draws 14 f once per reel; each muscle glows 8 f in on its name, the previous dims to 30% | "Lower back", "glutes", "hip flexors", "core" |
| **P-06** | **Rep ring** | A Mist ring around a corner badge on the demo card, filling per rep; numeral in Inter Tight 600 | Each segment fills 6 f **on the rep onset** from demo sync (§1 step 7); last rep → Leaf ✓ | "10 reps", "do 3 of these" |
| **P-07** | **Hold timer** | A Mist circular timer (Ø 180) with JetBrains Mono "00:30", counting down in real time | Ring depletes continuously; final 3 s the ring breathes 1.0 → 1.05 | "Hold for 30 seconds" |
| **P-08** | **Breath cue** | A soft Sage circle behind the word "inhale" / "exhale" (Instrument Serif italic) | Expands 1.0 → 1.35 over 4 s (inhale), contracts over 4 s (exhale), synced to her cue | "Breathe in…", "exhale as you…" |
| **P-09** | **Range arc** | A dotted Mist arc tracing the moving limb's path, start/end dots | Draws in sync with the demo's movement | "All the way up", "full range" |
| **P-10** | **Form check versus** (Mode V) | Left: mistake take, Clay frame + ✕ + "common mistake". Right: correct take, Leaf frame + ✓. Identical crop, scale and timing | Divider draws top → bottom 10 f; clips play in sync; the left desaturates 40% after its ✕ lands | "Don't do this… do this", "most people…" |
| **P-11** | **Cue chips** | 2–3 `KT-CUE` pills beside the body with Leaf leader lines ("ribs down", "knees out") | Pill 7 f + leader 8 f, 6 f stagger, on each cue word | Every form cue |
| **P-12** | **Slow-mo spotlight** | The demo slows to 50% at the key moment; a soft radial spotlight (25% ink vignette) on the joint | Speed ramp 6 f; spotlight 8 f | "This is the part people miss" |
| **P-13** | **Position steps** | The stretch frozen at its 2–3 positions as small numbered frames in a row, the live clip above | Each still pops 8 f on "first… then… then" | Multi-position stretches (cat → cow) |
| **P-40** | **Depth demo** | Her demo card behind her talking-head matte (G-5); she half-turns and points at it | Card parallax ±10 px | "Like this", "watch my hips" |
| **P-47** | **Posture pair** | Two line-art side silhouettes: head-forward (Clay angle) vs stacked (Leaf vertical line) | Left draws 10 f, right 10 f, then the Leaf line drops through ear–shoulder–hip 8 f | Tech neck, standing posture |
| **P-50** | **Bubble demo** | Demo full-frame (mode D) with Aria in the G-4 bubble explaining | Bubble shrink 10 f; the bubble breathes 1.0 → 1.04 on her stress words | Long demos while she talks |

**Desk-worker life (B-3, B-5, B-11)**
| ID | Pattern | What's on screen | Motion | Use when she says… |
|---|---|---|---|---|
| **P-14** | **Desk slump silhouette** | Line-art person at a desk (chair, laptop); the spine curves forward over time (Clay line), then resets upright (Leaf) | Slump: continuous 2 s ease; reset 12 f on the fix word | "After sitting all day", "at your desk" |
| **P-15** | **Sitting clock** | A minimal clock face; the hand sweeps the hours she says; a chair icon under it | Sweep 24 f; the arc fills Mist | "8 hours", "9 to 6" (her numbers) |
| **P-16** | **Pain spot pulse** | A soft Clay radial pulse at the named area on the silhouette or her demo | 2 pulses, 18 f each, 40% → 0% | "Lower back hurts", "stiff neck" |
| **P-17** | **5-minute pill** | A Sage pill "5 minutes" with a fill bar; one segment per stretch | Fills L → R 20 f; segments light per item | "5 minutes", "less than a coffee break" |
| **P-18** | **Today checklist** | A paper card "Today" with the 3–4 things she said, each with a round box | Each ticks Leaf ✓ (8 f) on its word; the card glints once | Payoff, recap, "you can do this today" |
| **P-39** | **Equipment badges** | Chips "chair only", "no equipment", "at your desk", "2 min" with line icons | Pop 7 f, 4 f stagger | "No gym needed", "just a chair" |

**Myth-busting (B-7)**
| ID | Pattern | What's on screen | Motion | Use when she says… |
|---|---|---|---|---|
| **P-19** | **Myth card flip** | Paper card: Clay "myth" tag + the myth in serif ("More cardio = less belly fat"). Back: Leaf "fact" tag + her fact in her words | rotateY 0 → 180° over 14 f (ease_in_out), lift 1.04; the tag swaps at 90° | "Most people think…", "that's a myth" |
| **P-20** | **Soft strike** | A 5 px ink line strikes through the myth phrase; the phrase fades to 40% | Line draws L → R 12 f | "It's not about X" |
| **P-22** | **Spot-reduction demo** | Line-art body; arrows from "crunches" point at the belly, which stays unchanged, while a soft whole-body Sage wash fills on her real reason | Arrows 8 f; wash 20 f bottom → top | "You can't target belly fat" (only if she says it) |
| **P-23** | **Balance scale** | A minimal scale: left pan "cardio", right pan the items she names (e.g. "strength", "protein", "sleep") dropping in; the scale tips | Each item drops 10 f with a soft bounce; tilt 14 f | "It's not X, it's Y + Z" |
| **P-42** | **Banner chip flip** | The banner chip flips "MYTH" → "FACT" or "CRUNCHES" → "DEAD BUGS" | 8 f X-axis flip; Clay → Leaf at 90° | The fix word, once per reel |
| **P-48** | **Lanes** | Two lanes on the same axis: what she says doesn't work vs what works, as labelled tracks; her words only | Both fill in sync over 24 f; the left greys 40% | Comparisons she makes |

**Nutrition (B-6)**
| ID | Pattern | What's on screen | Motion | Use when she says… |
|---|---|---|---|---|
| **P-24** | **Plate builder** | A top-down plate (her food shot or line art); foods drop in as named with a Jost label chip each | Each food drops 10 f (scale 1.1 → 1.0, shadow grows); label 6 f | Building a meal |
| **P-25** | **Swap card** | "swap n/4" pill + two food pills: from (40% opacity) → to (Leaf outline), with an arrow; the to-food shot fills the card | Arrow draws 8 f; from-pill slides out left, to-pill slides in 10 f | Each protein swap |
| **P-26** | **Protein bars** | Bars on one shared axis for foods she compares; values **only as she says them** ("about 20 grams") | Bars grow 18 f, 6 f stagger; labels 6 f after | When she gives numbers |
| **P-27** | **Thali map** | A steel-thali outline with 4–5 katoris; each fills with a food label as named | Katori fills 10 f each | Indian meals, "a normal lunch" |
| **P-28** | **Grocery shelf** | A line shelf; food chips slide onto it in order | Slide 8 f, 4 f stagger | "Add these to your list" |

**Client stories (B-8, B-12)**
| ID | Pattern | What's on screen | Motion | Use when she says… |
|---|---|---|---|---|
| **P-29** | **12-week rail** | On Forest: 12 week dots on a line; milestones she names land as Jost labels ("week 4: walks after dinner") | Dots fill Leaf L → R synced to her words; label 8 f each | "In 12 weeks", "by week 4" |
| **P-30** | **Real chart** | A line chart of **real** recorded weights (her data file), Mist line, Leaf end dot, labelled axes | Line draws 30 f; end dot pulses once | Only with her real data |
| **P-31** | **Consented photo pair** | Two real client photos, same size, "week 0" / "week 12" labels, small "shared with consent" chip | Left fades in 8 f, right 8 f later; no warping, no filters | Only with written consent |
| **P-32** | **What-changed stack** | Paper cards stacking with a line icon each: the changes she names ("protein at breakfast", "3 strength days", "8k steps") | Each card slides up 10 f and stacks with a 12 px offset | "What we actually changed" |
| **P-33** | **Habit grid** | 12×7 grid of day dots filling Sage (consistency), a few left empty (honest) | Fills 2 f per week | "Consistent, not perfect" |
| **P-34** | **Quote card** | Real client quote in Instrument Serif italic on paper, first name/initial only | Words fade in, 4 f stagger | Real quotes only |
| **P-38** | **Hero number** | Inter Tight 300 numeral + unit ("8 kg", "12 weeks") on Forest with a soft Sage glow | Counts 24–30 f ease-out; Z-5 settle on landing | Every number she says that matters |

**Structure, text, CTA (B-9, B-10, B-14)**
| ID | Pattern | What's on screen | Motion | Use when she says… |
|---|---|---|---|---|
| **P-35** | **Serif title** | Exercise/topic name in Instrument Serif italic 88 px above the card | 1 letter / 2 f, blur 8 → 0 | Every item name |
| **P-36** | **Keyword chips** | 1–3 Jost chips under the title ("for desk workers", "30 sec each side") | Pop 7 f, 4 f stagger | Qualifiers |
| **P-37** | **Edge labels** | Big words on the card's bottom edge, swapped per noun | 6 f blur cross-swap | Lists of body parts/foods in one sentence |
| **P-41** | **Cue cloud** (G-6) | 4–6 blurred cards of the coming exercises/foods floating behind her matte | Drift ±10 px, 6 s cycle | List intros |
| **P-43** | **Plan card** | Paper card "Free 7-day plan" + 7 day pills | Pills fill Sage, 3 f stagger; the card glides into a DM bubble over 16 f | CTA |
| **P-44** | **PLAN key** | Coral rounded key "PLAN" + a comment bubble typing "PLAN" | Key press 6 f down, 6 f up; typing 1 letter / 2 f | "Comment PLAN" |
| **P-45** | **Follow chip** | "follow for daily 5-minute fixes · @fitwitharia" | Rises 8 f, holds | "Follow for…" |
| **P-49** | **Coach note** | Paper note card, Eucalyptus "Coach note:" tag, typed text (her words) | Typewriter 1 word / 3 f, caret blink | Tips, rules of thumb |

**Gentle tease (B-13, `mock` only)**
| ID | Pattern | What's on screen | Motion | Use when she says… |
|---|---|---|---|---|
| **P-21** | **Tease tag** | Butter pill near the subject (not the face): "200 crunches a day 😅" | Pop 8 f, sway 18 f | Gentle teasing of a habit |
| **P-46** | **Soft mistake markup** | Thin Clay outline around the mistake + serif note ("neck doing the work") + small ✕ | Outline 12 f, note 10 f, ✕ 6 f | Pointing out the common mistake |

### 8.4 Line → pattern lookup (classify every sentence with this)
| Line type (her words) | Primary | Alternates |
|---|---|---|
| "If your lower back hurts after sitting all day" (mirror) | P-14 + P-16 | P-15, her slump take |
| "Here's the fix / try this" | T-10 → P-01 + P-04 | P-40 |
| Exercise name ("seated cat-cow") | P-35 + P-01 (+ SM-1/SM-2 at an item start) | P-40, P-50 |
| Form cue ("ribs down", "chin tucked") | P-11 | P-03, P-04 |
| "Your back should be straight / neutral" | P-04 | P-02 |
| "Most people do it like this" (mistake) | P-10 (her mistake take) | P-46, P-02 |
| Reps ("10 reps", "3 rounds") | P-06 | P-37 |
| Hold ("hold 30 seconds") | P-07 (+ P-08 if she cues breath) | — |
| Breath cue | P-08 | — |
| Muscle / body part named | P-05 | P-16 (pain), P-37 |
| Positions ("start here… then…") | P-13 | P-09 |
| "No equipment / just a chair / at your desk" | P-39 | P-17 |
| "5 minutes / quick / coffee break" | P-17 | P-07 |
| "Sitting 8 hours" | P-15 | P-14 |
| Myth statement ("most people think…") | P-19 | P-20 |
| "It's not X, it's Y" | P-19 flip + P-23 | P-48, P-42 |
| "You can't spot-reduce" | P-22 | P-05 |
| Food named | P-24 | P-27, P-28, P-37 |
| Swap ("instead of X, have Y") | P-25 | P-24 |
| Protein grams she states | P-26 | P-38 |
| "A normal Indian lunch" | P-27 | P-24 |
| Client result number ("8 kg", "12 weeks") | P-38 + P-29 | P-30 (real data) |
| "What we changed" | P-32 | P-33 |
| "She was consistent, not perfect" | P-33 | P-29 |
| Client quote | P-34 | — |
| Before/after photos | P-31 (**consent only**) | P-32 instead |
| Gentle tease of a habit | P-21 + Z-2 | P-46 |
| Tip / rule of thumb | P-49 | P-36 |
| List intro ("I've got 3 for you") | P-41 + SM-1 draw-in | P-17 |
| Recap / payoff | P-18 | P-17 |
| "You can do this today" | P-18 | emphasis line (§5.6) |
| "Comment PLAN" | P-44 + P-43 | — |
| "Follow for daily fixes" | P-45 | — |

### 8.5 Data and truth rules (D7)
1. **Only her numbers.** Every number on screen appears in her transcript or her client records. No calories, macros, body-fat % or "burns X" she didn't say (N7).
2. **Same axes.** Comparisons (P-10, P-26, P-48, P-31) use identical frames, crops, scales and timing; only the variable changes.
3. **Show the body, not the jargon.** "Neutral spine" is a line on her spine; "hip hinge" is an angle arc at her hips. The label names it once (`KT-CUE`), then the overlay runs.
4. **Mistake → correct = Clay → Leaf,** landing on the spoken fix word. Never a warning flash.
5. **One idea per screen.** Max 3 animated groups at once; the rest dims to 40%.
6. **Sync to the body:** rep segments fill on rep onsets; spine lines straighten when *she* straightens in the demo.
7. **Client honesty:** real data + written consent, or no chart/photos (P-32 only). A small "real client · shared with consent" chip on P-30/P-31.
8. **Escalate:** the last item gets the biggest visual (Mode V, Forest stage, or the P-02 ghost).

### 8.6 Density and variety
- An event every 0.8–1.8 s (calm holds ≤ 3 s allowed during stretches, §7.4).
- ≥ 8 different patterns and ≥ 4 families per 60 s.
- The same pattern at most 2 beats in a row (the item ritual excepted).

### 8.7 Asset rules
- **Her footage first:** every exercise is her demo (B-1/B-2); every food shot is hers (B-6); every desk shot is hers (B-11).
- **Built-live line art** (silhouettes, body maps, plates, thali, scales) is allowed for concepts, and for any exercise without a demo (flag it at the checkpoint).
- **No stock** people, gyms, food or bodies. No AI-generated bodies or faces.
- **Client material:** real, consented, unretouched, same angle and light; first name/initial only.
- No brand logos on supplements, apparel or equipment unless she names the brand. Blur gym strangers (N13).
- **Shot list to request when a reel lacks assets:** "side view, 3 reps, 2 s start position" per exercise; "deliberate mistake take, same framing"; "top-down 5 s" per food.

---

## §9 Transitions (`T`)

### 9.1 Library (30 fps; smooth by design)
| ID | Transition | Frames | Recipe | Sound role (if licensed) |
|---|---|---|---|---|
| **T-01** | **Soft panel drop** (G-1) | 10 (+ card 12) | Full frame eases down into the panel (`ease_in_out`); Linen/Forest revealed; the card rises 40 px + fades from f4 | Soft whoosh |
| **T-02** | **Rise back** (G-2) | 9 | Panel → full: scale 0.94 → 1.02 → 1.00, 3 px vertical blur on f1–3; the stage fades behind | Soft swish up |
| **T-03** | **Slide-aside** (G-3) | 10 | Panel narrows to x 0–450 (rounded right corners 48); the card grows in x 470–1050 | Paper slide |
| **T-04** | **Bubble shrink / grow** (G-4) | 10 | Footage ↔ Ø 300 circle at bottom-left, overshoot 1.06 | Soft pop / swish |
| **T-05** | **Blur dissolve** | 8 | Gaussian blur 0 → 24 px on the outgoing (f0–4), cross-fade, 24 → 0 on the incoming (f4–8). Replaces the inspiration's zoom-blur slam (I3) | Air |
| **T-06** | **Card push swap** | 8 | Outgoing card slides left 120 px + fades; the incoming slides in from the right 120 px, overlapping 3 f | Paper slide |
| **T-07** | **Card evolve** | 12 | The card morphs in place (size, radius, content cross-fade); no exit | — |
| **T-08** | **Breath push-through** | 14 | The camera pushes into a card or her demo's body area: 1 → 3× (ease_in), blur 0 → 12 px on the last 4 f; the target's colour becomes the next scene's background (e.g. → Forest) | Soft whoosh |
| **T-09** | **Sage wipe** | 12 | A soft-edged Sage band (feather 80 px) sweeps diagonally 20° top-left → bottom-right, revealing the next scene | Soft whoosh |
| **T-10** | **Coral light sweep** (the fix reveal) | 16 | A Coral light bar (140 px, white core 20 px, feather 60 px) sweeps L → R at 15°; behind it the correct state resolves from blur 16 → 0 and opacity 0 → 1; a soft bloom on exit | Shimmer |
| **T-11** | **Myth flip** | 14 | Card rotateY 0 → 180° (perspective 1400 px); lift 1.04; the content swaps at 90° | Page turn |
| **T-12** | **Jump cut** | 0 | Word-boundary cut inside the same setup; alternate with Z-1 / plain | — |
| **T-13** | **Soft exposure lift** | 6 | +0.35 EV bloom over 3 f, cut on f3, settle 3 f. For world changes Studio → Linen/Forest | Air |
| **T-14** | **Hard end** | 0 | Cut to the end ≤ 6 f after the last word | — |
| **T-15** | **Match cut** | 0 | Cut from her talking-head pose to the same pose in the demo clip (e.g. seated → seated stretch), aligned on her hips ±20 px | — |

**Banned (N8):** shatter, zoom-blur slam, glitch, RGB split, invert flicker, whip blur, light-leak burns, film burns, shakes, crash zooms, rotation snaps, spin transitions.

### 9.2 Grammar
| Boundary | Use | Never |
|---|---|---|
| Frame 0 | Forest Card settle + a moving result pair (VS devices) | A static or fade-from-black frame |
| Mistake → fix (hook) | **T-10 Coral light sweep** (+ P-42 chip flip) | Hard cut, shatter |
| Myth → fact | **T-11 Myth flip** | Crossfade |
| Hook → item 1 | T-05 → T-01 | Hard cut |
| New item | T-01 (Linen) or T-08 (into Forest) + SM-1/SM-2 on the ordinal word | Hard cut |
| Item → Aria (opinion, tease) | **T-02 Rise back** | — |
| Aria → full-screen demo while she keeps talking | T-04 bubble | — |
| Talking pose → same pose in the demo | T-15 match cut | — |
| Comparison | T-03 slide-aside or Mode V divider | — |
| Card → card (same item) | T-07 evolve or T-06 push | A still jump |
| Number lands | Z-5 settle | Shake |
| Last word | T-14 | Black tail |

### 9.3 Transition map (part of the plan)
```yaml
transitions:
  - {t: 0.00, id: VS-1+G-5, to: HOOK, sfx: null}
  - {t: 1.85, id: T-10, from: mistake, to: fix, sfx: null}
  - {t: 1.90, id: P-42, note: "chip flip CRUNCHES -> DEAD BUGS", sfx: null}
  - {t: 6.60, id: T-05+T-01, from: HOOK, to: S, note: "on 'First'", sfx: null}
  - {t: 14.2, id: T-02, from: S, to: F, sfx: null}
```
(`sfx` stays `null` until she has a licensed library, §11.)

### 9.4 Budget (per 60 s)
- T-01 / T-08: one per item.
- T-10: once in the hook, plus once more only for the payoff.
- T-11: ≤ 2. T-04: ≤ 3. T-09: ≤ 2. T-13: ≤ 2.
- **The same transition never 3× in a row** (except the item-entry ritual).
- Cuts within ±1 f of word boundaries; audio never offset.

---

## §10 Motion tokens, zoom system, layers, finishing

### 10.1 Motion tokens (30 fps)
| Token | Value |
|---|---|
| Beat lead | 2 f before the onset |
| Entries | `cubic-bezier(0.16, 1, 0.3, 1)` (soft expo-out), 7–12 f |
| Exits | `cubic-bezier(0.7, 0, 0.84, 0)`, 6–8 f |
| In-out (panels, flips) | `cubic-bezier(0.65, 0, 0.35, 1)` |
| Gentle overshoot (bubble, tiles) | `cubic-bezier(0.34, 1.28, 0.64, 1)`, 10 f |
| Pop (chips, tags) | Scale 0.92 → 1.04 → 1.0 over 7–8 f, opacity 0 → 1 in 4 f. **No squash** |
| Line draw (spine, outlines, arcs) | 10–12 f via `stroke-dashoffset`, round caps |
| Typewriter (serif titles) | 1 letter / 2 f, blur 8 → 0 |
| Typewriter (coach note) | 1 word / 3 f |
| Counter | 24–30 f ease-out |
| Settle nudge (Z-5) | ±3 px, 6 f, bump 1.02, seeded, decaying |
| Drift (cue cloud, glows) | ±10–16 px over 4–6 s, seeded sine |
| Breath (P-08) | 4 s in / 4 s out |
| Hold | Titles ≥ 12 f after complete; text ≥ 0.28 s / word |

### 10.2 Zoom system (`Z`): soft, always on meaning
| ID | Preset (tokens) | Recipe | Tone / use |
|---|---|---|---|
| **Z-1** | `soft-punch` | 1.00 → 1.10 (selfie) / 1.15 (tripod) in **6 f**, light motion blur, hold until the next cut | `lift` / `win` emphasis word |
| **Z-2** | `glide-in` | 1.00 → 1.25 toward her face in **10 f**, hold 20–40 f, ease back 8 f | `mock` (gentle tease) and "listen to this" moments; ≤ 3 per reel |
| **Z-3** | `pull-out` | 1.15 → 1.00 in 8 f | Reveal a graphic beside her; the fix reveal |
| **Z-4** | `push-drift` | 1.00 → 1.05 over the beat | `calm`, `explain`, `awe` |
| **Z-5** | `shake` (settle nudge) | ±3 px 6 f + 1.02 bump | Hero numbers landing; never on bad states |
| **Z-6** | `zoom-through` | = T-08 (1 → 3×, 14 f) | World changes |
| **Z-7** | `form-focus` | On demo footage only: 1.00 → 1.40 toward the named joint in 12 f, hold 20–40 f | "Watch my hips", P-12 moments; ≤ 3 per reel |

**Zoom rules:**
- In Mode F, a zoom event every **3.5–6 s**.
- **Never the same Z twice in a row** (validator N5-zoom).
- Zoom on meaning (emphasis, tease, reveal, form), not on every cut. Tripod jump cuts alternate: plain → Z-1 → plain → Z-4…
- Zooms never push her face out of the safe frame or under the banner; Z-7 never crops the body part being discussed.

### 10.3 Layer order (back to front)
1. Background (footage / Linen / Forest)
2. Glow (Forest radial, breath circle)
3. Cue cloud (G-6)
4. Card(s), demo cards, line-art, charts
5. **Aria matte (depth sandwich)** *or* the speaker panel / bubble
6. Form overlays on demos (spine, arcs, outlines, cue chips)
7. Edge labels, serif titles
8. Rail + numeral tile
9. `CAP-SUB`
10. `CAP-KEY` / emphasis line
11. Tease layer (P-21)
12. Banner (Forest Card)
13. Light passes (T-10 sweep, T-13 lift)

### 10.4 Finishing
- No grain, no vignette (except the P-12 spotlight). Soft glows only on Forest hero elements, the breath cue and the T-10 sweep.
- Footage: match WB/exposure between setups A, B, C only; keep her skin tones natural; no beauty or slimming filters (N1).
- Card radius 28–48 (default 44). **Soft shadows only:** cards 0/12/32 ink 18%; chips 0/6/16 ink 14%; text 0/4/16 ink 45%.

---

## §11 Sound

### 11.1 Tone palettes
| Tone | Colour role | Zoom | Treatment | Sound (once licensed) |
|---|---|---|---|---|
| `lift` | Sage | Z-1 | Hook energy, counts, list intros | Soft whoosh, soft pop |
| `calm` | Sage / Mist | Z-4 or none | Stretch holds, breath cues | None (voice + bed) |
| `explain` | Mist / Eucalyptus | Z-4 | Cues, mechanisms, swaps | Paper slide, soft tick |
| `warn` | Clay (quiet) | none | Mistakes, myths | A low soft thud (never an alarm) |
| `mock` | Butter | Z-2 | Gentle tease, ≤ 2 per reel | **None** (no meme sounds, ever) |
| `awe` | Coral | Z-3 / Z-4 | The fix reveal, the client result | Shimmer |
| `win` | Leaf | Z-1 | ✓ ticks, completed items, payoff | Soft chime |
| `cta` | Sage + Coral key | Z-3 | PLAN, follow | Soft key click |

### 11.2 Current state: voice-first
- **She has no sound-effects library.** Until she supplies a licensed one, **no SFX are added**; `sfx` fields stay empty and the ledger is empty.
- **Bed (optional):** only a track she has the licence for (her own purchase / a royalty-free library she subscribes to). Calm acoustic, soft lo-fi or minimal piano, 70–100 BPM, ducked 22 dB under the voice, entering on the fix beat (≈2 s). If she has none, export **voice only** and she adds Instagram in-app music at upload (keep it ≥ 20 dB under her voice).
- **Never** copyrighted songs baked into the file, meme sounds, gym-hype tracks, heavy bass drops.

### 11.3 SFX ledger rules (apply as soon as a library exists)
- Any file ≤ 2 uses. One file may be the **list cue** (one per item).
- No file on two consecutive cues. Rotate variants inside a pool.
- Density: ≤ 1 cue per 2 s on average (calmer than the inspiration). Never 2 overlapping. Never under a trigger word's consonant (shift ±2 f).
- Levels: −24…−30 dB under the voice. Sounds should be *felt*, not noticed.
- `meme_max_per_reel` = 0 in `tokens.json`: any meme cue fails validation (M9).

### 11.4 Pools to source (when she buys a licensed pack)
| Role | What to look for |
|---|---|
| Soft whoosh / air | Short airy whooshes, no sub hits |
| Paper slide | Card/paper slides for T-03, T-06 |
| Soft pop | Rounded UI pops for chips and rail nodes (list cue candidate) |
| Wood tick | Soft wooden clicks for rep counters |
| Shimmer | Gentle bell/shimmer for T-10 |
| Soft chime | Single-note chimes for ✓ |
| Key click | A soft keyboard key for P-44 |
| Page turn | For T-11 myth flips |

### 11.5 Silence, outro, mix
- **Breath pause:** ≤ 0.4 s of near-silence before a reveal is allowed (M5); it's part of her calm delivery.
- **Bed drop-out:** if a bed is used, it dips for 0.5–1 s before the fix reveal / client number and returns under it.
- **Outro:** hard stop ≤ 6 f after the last word.
- **Mix:** voice chain (high-pass 80 Hz, gentle de-ess, light compression, room-tone noise reduction for the home studio) → **−14 LUFS integrated, true peak ≤ −1.5 dBTP**. Gym selfie clips: extra noise reduction for gym music; if the gym music is copyrighted and audible, flag the clip.

---

## §12 Footage handling

### 12.1 Setups
| Setup | Description | Use | Framing target |
|---|---|---|---|
| **A: Studio tripod** | Home studio, white walls, plants, yoga mat; standing or seated on the mat/chair | Main talking head, panel and full | Eyes at y ≈ 620–700 when standing medium shot; head top ≥ 48 px below the banner bottom (≈ y 420) |
| **B: Gym selfie** | Handheld front cam in the gym | Occasional asides, "real life" moments, teases | Face centred x 400–680; stabilise; blur strangers |
| **C: Demo camera** | Separate camera, her exercise demos | All B-1/B-2 demo cards, Mode D, P-02/P-10 | Whole body in frame with 8% margin; side view for spine/hinge cues, front view for knees/shoulders |

### 12.2 Crops
- `F`: as shot, with Z-zooms.
- `S` / `FS` panel: head top = panel top + 60…110, face x 340–740.
- **Bubble (G-4):** face centred, scaled so the face fills 70% of Ø 300.
- **Slide-aside (G-3):** face centred in x 0–450.
- **Depth sandwich (G-5):** matte placed so the head top is ≥ 48 px below the banner bottom and a hand or shoulder overlaps the card corner by 60–140 px.
- **Demo cards:** 4:5 crop centred on the body's midpoint (hips); never crop hands/feet that the cue is about. For Mode V, both takes use the same crop box.
- **Gym (B):** blur any other person's face (Gaussian 24 px, tracked) (N13).

### 12.3 Matte
- Required for A/B talking heads (depth sandwich, bubble, cue cloud) and for demo clips used in P-02.
- RobustVideoMatting / Resolve Magic Mask (Person); feather 2 px, choke 1 px, temporal smoothing. Check hair and plant leaves at 200% (her plants sit close to her head).

### 12.4 Demo sync log (per reel)
```yaml
demos:
  - exercise: "seated cat-cow"
    clip: raw/C_0012.mp4
    take: correct            # correct | mistake
    view: side
    in_s: 2.10
    out_s: 9.80
    rep_onsets_s: [3.0, 4.6, 6.2]
    hold: null
```

### 12.5 Reaction / warmth bank (ask at the shoot)
2–3 s each, for rise-backs, bubbles and tease beats:
- a warm smile to camera
- a knowing "we've all done this" laugh
- a slow nod
- pointing down at the demo area ("like this")
- an exhale with shoulders dropping (for calm beats)
- a playful eyebrow raise (for teases)

### 12.6 Frame rate & audio
- 30 fps CFR (conform VFR; 60 fps demo clips may be used for P-12 slow-mo at 50%). 1080×1920, BT.709.
- One voice track: high-pass, de-ess, compression, noise reduction, −14 LUFS.

---

## §13 Output contract

### 13.1 Beat sheet schema (the first ```yaml``` block of the edit brief)
```yaml
- id: 4
  section: HOOK                  # HOOK | LOOP | ITEM-n | PAYOFF | CTA
  spoken: "here's what actually fixes it"
  trigger: "fixes"
  onset_s: 1.92
  start_s: 1.85
  t0: 1.85
  t1: 2.60
  tone: awe                      # lift | calm | explain | warn | mock | awe | win | cta
  mode: HOOK                     # HOOK | F | S | D | FS | V | A | I
  line_type: "the fix"           # §8.4
  stage_move: G-5                # G-1…G-6 or null
  family: B-1
  pattern: P-04                  # §8.3
  visual: "Coral light sweep turns the slumped silhouette into Aria's seated cat-cow demo; spine line Clay -> Leaf"
  on_screen_text: ["DEAD BUGS"]
  caption: {style: CAP-KEY, text: ["here's the", "FIX"], highlight: primary}
  banner: {text: "Stop doing CRUNCHES. Do this instead", chip_state: "DEAD BUGS"}
  zoom: Z-3                      # Z-1…Z-7 or null
  transition_in: T-10
  transition_out: evolve
  demo: {clip: raw/C_0007.mp4, take: correct, in_s: 1.2}
  numbers_said: []               # every number on screen must be listed here (M14)
  sfx: []                        # empty until a licensed library exists (§11.2)
  assets: [raw/C_0007.mp4]
```

### 13.2 SFX ledger
```yaml
sfx_ledger: {}                   # voice-first; fill only with licensed files (§11.3)
bed: null                        # or {file: "<licensed track>", licence: "<source>", level_db: -22, in_s: 1.9}
```

### 13.3 Hook proposal format (3 required)
```yaml
- name: "Stop -> Do: crunch vs dead bug"
  formula: HF-3
  banner: "Stop doing CRUNCHES. Do this instead"
  result_pair: {mistake: "Aria's deliberate crunch take, neck pulled", fix: "Aria's dead bug, ribs down"}
  stoppers: [VS-5, VS-1, VS-4]
  captions: {style: CAP-KEY, cards: ["stop doing / CRUNCHES", "do / THIS", "ribs / DOWN"]}
  storyboard: "f0 Forest Card + Mode V divider drawing + Aria cut-out | 0.4 Clay outline at neck + note | 1.2 tease tag | 1.9 chip flip + Leaf frame | 2.4 cue chips"
  sound: "voice only"
  stopper_test: {thumbnail: pass, mute: pass, read_s: 1.1, changes_3s: 10, bro_test: pass}
```

### 13.4 Checkpoint (before building)
Send:
1. 3 hooks with banners + the stopper test results.
2. The result pair and how both states are produced (which demo takes; any line-art fallback).
3. The beat sheet with tones, the transition map and the sound plan (voice-only or licensed bed).
4. **The truth list:** every number on screen and where she said it; client data source + consent status.
5. **The demo sync log** (§12.4) and the **missing-asset shot list** (§8.7).
6. Style stills: f0 (thumbnail), the fix reveal, one item ritual (rail + tile + title + demo), one form overlay, one rise-back, the CTA (PLAN key).

**Wait for approval.** The storyboard page is gate 2.

---

## §14 Worked examples

### 14.1 Idea 1: "3 desk stretches that fix your lower back in 5 minutes" (HF-1 Mirror → Fix, keyword PLAN)
**Banner:** "[3] desk stretches for your lower back 🌿" (Mist chip "3").

| t | Spoken (typical) | Tone | Mode | Visual | Zoom | Transition |
|---|---|---|---|---|---|---|
| f0 | — | lift | HOOK | Forest Card + P-14 slump silhouette (Clay spine) in the top band + Aria cut-out at its corner (G-5) | — | — |
| 0.1 | "If your lower back hurts after sitting all day…" | warn | HOOK | P-16 Clay pulse at the lower back ×2; KEY "after sitting / ALL DAY" | Z-4 | — |
| 1.3 | "…you're not broken, yaar." | mock | HOOK | P-21 tag "we've all been here 🙈" | Z-2 | — |
| 1.9 | "Try this." | awe | HOOK | T-10 sweep → her seated cat-cow demo; P-04 spine Clay → Leaf | Z-3 | T-10 |
| 2.6 | "3 stretches, at your desk, 5 minutes." | lift | HOOK | P-17 5-minute pill (3 segments); rail draws 3 nodes; P-39 "chair only" | Z-1 | — |
| 4.6 | "And the free 7-day plan is at the end." | lift | HOOK | KEY "free 7-day plan / AT THE END"; P-41 cue cloud | Z-4 | — |
| 6.6 | "First: seated cat-cow." | explain | S | T-05 → T-01; rail node 1 Coral; SM-2 "1"; P-35 "Seated cat-cow"; P-01 demo (side view) | — | T-01 |
| 8.0 | "Round your back as you exhale… arch as you inhale." | calm | S | P-08 breath cue; P-04 spine line follows; P-11 "exhale, round" → "inhale, arch" | — | evolve |
| 11.0 | "Do it 5 times, slowly." | explain | S | P-06 rep ring on rep onsets | — | — |
| 13.0 | "Your spine has been frozen in one shape all day." | explain | F | T-02 rise back; KEY "frozen in / ONE SHAPE" | Z-1 | T-02 |
| 15.5 | "Second: seated figure-4." | explain | S | T-01; node 1 → Leaf ✓, node 2 Coral; SM-2 "2"; P-35; P-01 front view; P-05 glutes glow (inset) | — | T-01 |
| 18.0 | "Hold 30 seconds each side." | calm | D | T-04 bubble; demo full; P-07 hold timer; P-11 "sit tall" | Z-7 on the hip | T-04 |
| 22.0 | "The last one is the one everyone skips…" | lift | F | T-04 grow back; node 3 pulses | Z-2 | T-04 |
| 23.5 | "Thoracic extension over your chair." | explain | FS → S | T-08 push-through; Forest stage, P-47 posture pair → P-01 demo; SM-2 "3" | — | T-08 |
| 28.0 | "Hands behind your head, open your chest." | explain | S | P-11 "elbows wide", "ribs down"; P-37 edge labels "chest" → "upper back" | — | evolve |
| 31.0 | "That's it. Do it today, at 4 pm." | win | S | P-18 Today checklist: 3 ticks on each name; node 3 → Leaf ✓ (rail complete) | Z-1 | T-07 |
| 34.0 | "Comment PLAN and I'll DM you the free 7-day plan." | cta | F | T-02 rise back; P-43 plan card + P-44 PLAN key + DM | Z-3 | T-02 |
| 37.5 | "Follow for daily 5-minute fixes." | cta | F | P-45 follow chip | — | T-14 |

### 14.2 Idea 2: "Why you're not losing belly fat (it's not cardio)" (HF-2 Myth flip)
**Banner:** "Not losing belly fat? It's [NOT CARDIO]" (Clay chip → flips Leaf "FACT").
- **HOOK (0–6 s):** f0 = Forest Card + P-19 myth card ("More cardio = less belly fat", Clay "myth" tag) in the top band + Aria (G-5). 0.3 s: treadmill line-art silhouette runs in place inside the card (warn). 1.0 s: P-21 tag "cardio queen era 😅" (mock, once). 1.8 s: **T-11 myth flip** → "fact" side in her words + P-42 chip flip. 2.5 s: P-23 scale starts filling with the first thing she names.
- **ITEMS (each thing she names, e.g. strength / protein / sleep):** SM-1 rail with N nodes; per item: T-01 → SM-2 tile → P-35 title → B-1 demo (strength: her squat demo with P-11 cues) or P-24 plate (protein: her food B-roll) or P-49 coach note (sleep tip) → T-02 rise back for "why".
- **"You can't spot-reduce" (if said):** P-22 on Forest.
- **PAYOFF:** P-23 scale fully tipped toward her items + P-18 Today checklist ("1 strength session", "protein at breakfast", her words).
- **CTA:** P-43 + P-44 + P-45. **Truth check:** no calories, no "burns X", no body-fat %.

### 14.3 Idea 5: "My client lost 8 kg in 12 weeks: what we actually changed" (HF-4 Real result first)
**Banner:** "[8 KG] in 12 weeks: what we actually changed" (Mist chip).
- **Pre-check:** her records file + written consent. No consent → no photos (P-31) and no chart (P-30); use P-32/P-33 only. The number "8 kg" and "12 weeks" must be spoken.
- **HOOK (0–6 s):** f0 = Forest Card + Forest stage: P-38 "8 kg" counting 0 → 8 (f0–f26) + P-29 12-week rail filling + Aria in the panel. 1.5 s: "and it wasn't a crash diet" → P-20 soft strike on "crash diet". 2.4 s: first P-32 card slides up ("what changed").
- **BODY:** SM-6 week rail as the marker. Each change she names = one P-32 card + its proof visual: steps (P-15-style step ring, her number only), protein (P-24 plate with her food shots), strength (her demo), sleep (P-49 coach note). P-33 habit grid on "she wasn't perfect" (honest gaps). P-34 quote if a real quote exists.
- **PAYOFF:** P-30 real chart (consent) or P-38 "8 kg" again + "12 weeks" → T-10 sweep to Aria: "you can start with one of these today" → P-18.
- **CTA:** P-43 + P-44 + P-45. Chip "real client · shared with consent" on any client visual.

### 14.4 Idea 4 hook in one line
"Stop doing crunches" → Mode V from f0 (her crunch take ✕ / her dead bug ✓), P-46 outline at her neck + note "neck doing the work", P-21 tag "200 a day? 😅", chip flip CRUNCHES → DEAD BUGS at 1.9 s, P-11 "ribs down" at 2.4 s.

### 14.5 Idea 3 structure in one line
SM-5 swap counter (1/4…4/4) + P-27 thali map that stays on screen as the spine; each swap = P-25 card with her food B-roll, grams only via P-26 when she says them; payoff P-28 grocery shelf with all 4.

---

## §15 QA checklist

**Stopper / hook**
- [ ] f0 has Forest Card + result pair + Aria; banner readable at 25%; one element moving.
- [ ] ≥ 8 changes in 0–3 s; the fix visible by 2.5 s.
- [ ] Banner ≤ 9 words, ≤ 2 lines, one chip, ≤ 1 calm emoji, matches the visuals.
- [ ] Bro test passed: no loud colour, no shake, no shouting type.

**Body**
- [ ] Every exercise named has her demo (or a flagged line-art fallback).
- [ ] Every form cue is drawn on the body (P-04/P-11/P-03/P-02).
- [ ] Mistakes come only from her deliberate mistake take, Clay-framed, labelled.
- [ ] Rail + numeral tile at every item; count = banner count.
- [ ] Event every ≤ 1.8 s; nothing static > 3 s (stretch holds have moving timers).
- [ ] ≥ 8 patterns, ≥ 4 families per 60 s; same Z never twice in a row; same T never 3× in a row.
- [ ] ≤ 3 bright roles per frame; subtitles never coloured; coral/sage never as text on Linen.
- [ ] No white text over her white wall or her face (light-background rule, §5.5).
- [ ] Face never covered; captions at chest height; chips never on the body part they name.
- [ ] ≤ 2 tease beats, only on `mock`; never during a correct-form demo.

**Sound**
- [ ] No SFX unless licensed; ledger clean if used; zero meme sounds.
- [ ] Bed licensed (or none); ducked ≥ 22 dB; no copyrighted songs.
- [ ] −14 LUFS, TP ≤ −1.5 dBTP; hard end ≤ 6 f after the last word.

**Truth / text / end**
- [ ] Every on-screen number is in `numbers_said` or her client records. No calories she didn't say.
- [ ] Client visuals: real data, consent chip, no warping/filters; no fake transformations.
- [ ] No stock people/gyms/food; gym strangers blurred.
- [ ] Glossary spellings; sentence-case subtitles; Hindi words as spoken.
- [ ] PLAN on screen ≥ 1.5 s; plan card + follow chip present; every open loop paid off.

---

## Appendix: banner bank (next reels)
| # | Banner (chip in [ ]) | Hook formula | Result pair |
|---|---|---|---|
| 1 | "[3] desk stretches for your lower back 🌿" | HF-1 | Slump silhouette → seated cat-cow |
| 2 | "Not losing belly fat? It's [NOT CARDIO]" | HF-2 | Myth card → fact + scale |
| 3 | "[4] easy protein swaps, fully veg 🥗" | HF-5 | Low-protein thali → swapped thali |
| 4 | "Stop doing [CRUNCHES]. Do this instead" | HF-3 | Crunch ✕ → dead bug ✓ |
| 5 | "[8 KG] in 12 weeks: what we actually changed" | HF-4 | Week 0 → week 12 rail + what-changed stack |
| 6 | "Fix desk back pain in [5 MINUTES]" | HF-7 | Slump → 3-stretch timer |
| 7 | "Your neck isn't stiff. It's [TECH NECK]" | HF-2 | Head-forward → stacked posture (P-47) |
| 8 | "Your plank is lying to you: [HIPS]" | HF-3 | Sagging hips ✕ → straight line ✓ |
| 9 | "POV: you sit 9 hours and your back [HATES YOU]" | HF-8 | Slump timelapse → her reset stretch |
| 10 | "No gym? Bas, [ONE CHAIR] is enough" | HF-1 | Packed gym icon → her chair workout |

Banners are drafts: verify every number and claim against each reel's script before use (M14).
