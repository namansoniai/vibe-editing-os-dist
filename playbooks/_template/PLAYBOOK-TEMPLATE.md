# Editing playbook template (the v2 format every creator's playbook follows)

**Reference example:** the reference playbook (`reference_playbook` from `veos paths`), a complete playbook written in
this exact structure. It is the quality bar: match its **depth, specificity and decisiveness**, never its content.
**Every section below is required.** Write concrete numbers where the craft needs them (px, frames, seconds, hex values,
font names), concrete examples drawn from the creator's own topics, and decided rules. **Never write menus or "you
could…".**

The playbook is written for the Director (Claude), who reads it **end to end before every reel** and treats it as the
creator's taste: on taste it outranks every generic rule. So write it the way a great creative director briefs a
brilliant editor: say what you want and why, set a very high bar, and leave the how to the editor. Use tables. Use IDs
(D1…, M1…, N1…, P-…, T-…, Z-…, G-…, SM-…, VS-…, HF-…) so the Director can cite them.

**Taste is direction; craft is exact.**
- Rhythm and taste are described by feel: tension and release, holds before reveals, build-ups, escalation, the last
  item biggest, contrast (loud against quiet, dense against empty). Never as counts: no change quotas, no shares of
  runtime, no per-reel budgets, no "never the same X twice in a row". A measured value from the inspiration may appear as
  a reference for the feel ("the hooks that worked changed something about every second"), never as a quota.
- Craft is exact: positions, sizes, frames, colours, sync, numbers, spelling. The person's face and head are judged in
  context, by eye: kept clear when the moment is about them, never cropped by accident.

**The editing directions come first.** `playbooks/_global/GLOBAL-RULES.md` applies to every playbook: show the thing not
the word, hooks that promise, seamless and powerful and less cluttered, rhythm by feel, sound that marks what the viewer
sees, the person judged in context, say what was said, fetch what the reel needs, the style decides the look. Only a build
that doesn't run blocks.
- Restate them in §2 first: "The editing rules apply; see GLOBAL-RULES.md." Write this playbook's own rules the same way:
  directions with the creator's reasons, not hard caps.
- **Never write a rule that conflicts with them.** Settled for every style: illustrations carry no labels or credit
  lines (made-up but realistic numbers are fine in an illustration), flashes have no cap, and text may sit behind the
  speaker. A dense style is still clean: dense in *time* (many changes), not dense in *space* (many things at once).

---

## Title and purpose
- **Title:** `<Creator> Reel Editing Playbook (v1, "<style name>")`.
- **Purpose:** 2–3 lines on what this playbook makes the editor do, and what the viewer must feel by the last frame.
- Optionally one line on where the style came from (the inspiration it was pulled from, or the niche it was invented
  for) and a pointer to the preview.

## The feel (the first section)
About 400 tokens of conviction: the soul of the style, written so a director could direct a whole reel from this
paragraph alone.
- What the viewer sees at frame 0 and why they stop. The promise the reel makes, and how the viewer gets to *watch* it
  happen.
- How it moves after the hook: what it never does, what it always does, how one picture becomes the next.
- Where the creator is and why (people come for the person, not the slides), or, faceless, what carries the voice.
- How the tones feel different: the joke, the explanation, the reveal. Never mixed.
- How it breathes: where it rushes, where it holds, how it builds, the last item biggest.
- The colour that leads every frame, and what the style refuses.
- **End with a one-line test of the style.** "If a frame could belong to any other creator's reel, it's wrong." or a
  sharper one specific to this creator.

Write it in the second person or as a director's voice-over, present tense, specific to this creator's niche, worlds,
colours and devices. No lists, no hedging, no generic adjectives that could describe anyone's reel.

## Creator directives and quick index
- **Creator directives (non-negotiable), D1…D8:** the 5–8 things the creator cares most about, in their own words
  translated into editing direction. Each points to the section that implements it.
- **Quick index** of the sections.

## §1 Procedure (follow in order)
The per-reel procedure for this creator. Keep the engine's standard steps:
1. inventory
2. matte
3. transcribe
4. segment
5. read every line for what the viewer should see, and its trigger word
6. tone tags
7. result pair
8. banners/hooks
9. data or visual story
10. beat sheet
11. SFX ledger
12. checkpoint
13. build

Add any steps this creator needs: product shots, a screen-recording step, a recipe-ingredient step, chart-data checks…

## §2 Hard rules (MUST / NEVER)
- **Starts with:** "The editing rules apply; see GLOBAL-RULES.md", then the craft in this style's terms: where the
  person's face and head stay clear and where this style lets things cross them, nothing overlapping by accident, literal on-the-word visuals in sync, numbers and quotes as said, spelling, audio
  targets (−14 LUFS, TP ≤ −1.5), deterministic frame-based animation.
- **Then this creator's musts, as directions with their reasons:** the frame-0 stopper, how soon the result shows, the
  banner/title shape, zero dead air in the cut, promise integrity, what they never claim.
- **NEVER list:** this niche's clichés the style refuses (e.g. fitness: stock gym footage, fake before/after; finance:
  fake returns presented as real; food: stock food shots), contrast failures, fake results or testimonials presented as
  real, decorative-only visuals, and the transitions or sounds this style doesn't use. Claims (the creator's results,
  prices, client data) must be real; illustrations may use made-up but realistic numbers, unlabelled.

## §3 Worlds, screen modes, stage moves, layout, safe zones
- **Worlds:** the 2–3 visual worlds this creator's content lives in. Look, what each carries, how to enter and exit.
  Examples to think with: studio/canvas/data for tech; kitchen/recipe-card/ingredient-table for food;
  gym/form-check/progress-chart for fitness.
- **Screen modes:** what each one carries and when it takes over the reel (described, never as runtime shares).
- **Stage moves:** full, low, panel, inset, bubble, slide-aside, depth sandwich (from the renderer), and when to use each.
  How the screen splits (vertical or horizontal), how it comes back to full, how one layout becomes the next.
- **Layout diagram** with y-coordinates, and safe zones (Instagram: key text inside x 64–1016, y 110–1500).

## §4 Colour system
- **Palette:** roles → hex, each with **one job**, plus the text-on colour and contrast ratio.
- **Meanings:** the before/after or bad/good axis (red → green unless the brand forbids it), the colour that leads,
  restraint (a frame reads as one leading colour plus an accent or two), gradients. Brand colours appear only on brand
  names.
- **Must match `tokens.json`.**

## §5 Type tokens
- **Font map:** banner, captions, subtitles, titles, numbers, labels, comedy/notes. Only fonts that can be bundled
  (Google Fonts / OFL).
- **The banner/title recipe:** fill, stroke, shadow, size, word limit, chip rules, f0 behaviour, life, exit.
- **Caption systems:** big keyword captions, subtitles (language and case), glow or keyword titles, labels, kinetic
  type, hero numbers, stickers.
- **Language rules:** script (romanised Hinglish / English / Hindi / mixed), case, brand-name spelling, the glossary.

## §6 Hook system
- **Stopper test** for frame 0 and 0–3 s.
- **The default hook formula for this creator**, as a second-by-second table, plus 4–8 alternative formulas, each with
  an example **from their topics**.
- **Result pairs by topic:** a table of this creator's typical subjects → the bad state → the good state → how to show
  each. **This is the most important table for literal visuals.**
- **Banner/title writing** with templates and banned phrasing. The hook title promises the viewer something (an
  outcome, a curiosity gap, who it's for) and is true to what the reel delivers; it need not repeat the spoken words.
  This section sets its shape (lines, sizes, word limits, case), never its voice; the Director writes 8–10 candidates,
  scores them and picks (GLOBAL-RULES: the hook decides the reel).
- **CTA formula** (their keyword/DM/link/follow habits; when they have none, how the reel lands without one).

## §7 Structure
- **Item/step markers:** pick one style per reel.
- **The item ritual.**
- **Open loops.**
- **Rhythm, by feel:** how information and entertainment trade places, where the reel holds, where it builds, the energy
  curve from hook to landing, the last item biggest. No timers.

## §8 B-roll and motion-graphics system
- **Families:** the kinds of visuals this creator needs (screen captures, product shots, their own B-roll clips, device
  mocks, data visuals, metaphor machines, kinetic type, comedy layer…), with the **assets the creator can supply** for
  each, and what the engine builds live when they have nothing.
- **Pattern specs (P-…):** a deep library (the reference has about 50) of named visual patterns, each with what's on
  screen, the motion recipe (frames at 30 fps), and when to use it. Invent patterns that fit **this niche's ideas**: a
  fitness "rep counter that fills a muscle diagram", a finance "money stack that splits into percentages", a cooking
  "ingredient drop into a bowl"…
- **Line → pattern lookup:** this creator's line types (from their actual topics) → primary pattern → alternates. It's
  vocabulary for the Director, not a decision table: it says what fits, and the Director invents when a moment needs more.
- **Picture first:** every key beat shows the thing being said (an object, a screen or app, a diagram, numbers in
  motion), in this style's own look; text supports the picture. Pointing words ("this, this and this") get a picture of
  what's meant.
- **Data rules** (if they use numbers): quantities countable, the same axes for comparisons; a number the creator says is
  shown as said; illustrations may use made-up but realistic numbers ("212 views", "1.2M views"), no label.
- **Asset rules:** real captures/footage first, generic mocks allowed only as stated, no stock clichés.

## §9 Transitions
- A library `T-01…` with frames and recipes, plus the grammar (which boundary uses which) and how the moves feel across
  the reel (which are the signature, which are rare accents). No budgets.

## §10 Motion tokens, zoom system, layers, finishing
- **Easing and timing tokens.**
- **Zoom system `Z-1…`:** recipes and tone use; zoom on meaning, never on autopilot.
- **Layer order.**
- **Finishing:** grain, vignette, regrade rules.

## §11 Sound
**The bundled SFX pack:** `veos paths` → `sfx_pack`, with tags in its `catalog.json` (role, vibe, energy, use).
- **Choose this creator's sound palette from it:** the allowed vibes, the allowed and banned roles, a short list of
  preferred sound ids per use (transition, text-pop, reveal, data, warning, success, CTA, list cue), whether meme sounds
  are allowed, whether the hook is dry, and how dense or sparse the sound feels.
- **Mirror it in `tokens.json` → `sound`:**
  ```json
  {"palette_vibes": [...], "allowed_roles": [...], "banned_roles": [...], "preferred": {"<use>": ["<id>", ...]}, "dry_hook": bool, "silence_before_cta": true}
  ```
- **Principle:** a sound only ever marks something the viewer sees happen. Restraint reads as premium.
- Tone palettes, the SFX ledger rules (no file more than 2×, one list cue), meme/comedy rules if the tone allows them,
  the music bed, silence and the outro, mix targets.
- **Only sounds the creator can legally use.** If they have no library, say so and plan voice-plus-bed.

## §12 Footage handling
- Their camera setups (selfie/tripod/desk/kitchen…), crops per mode, matte needs, reaction bank, frame rate, audio.

## §13 Output contract
- The beat-sheet fields the editor writes per beat:
  - **timing:** `id`, `section`, `t0`/`t1`, `spoken`, `trigger`
  - **classification:** `tone`, `mode`, `line_type`
  - **content:** `visual` (one sentence), scene ids, `sfx`
- The checkpoint list.

## §14 Worked examples
Two or three plans from this creator's real or typical topics: a hook table + a section-by-section pattern plan, beat by
beat. They show the standard the Director must match and then beat.

## §15 QA checklist
Grouped as stopper/hook, body, sound, truth/text/end. Craft items are exact checks; taste items are questions a director
asks of the whole reel (does it build, does each move land, would the best editor ship this), never counts.

## Appendix: banner/title bank
10 ready banners for their likely next reels.

---

## Companion files the builder also writes
- `tokens.json`: the machine-readable palette, fonts, type, layout, motion, camera presets, budgets and tone. Copy the
  schema of the `tokens.json` next to the reference playbook exactly, with this creator's values.
- `preview/index.html`: the "glimpse" page (see the `playbook` skill).
- `profile.md`: the quick preferences, what the creator volunteered, and the inspiration analysis or style decisions the
  playbook was built from (for later revisions).
