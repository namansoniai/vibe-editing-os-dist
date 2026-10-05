# Editing playbook template (structure every creator's playbook must follow)

**Reference example:** the reference playbook (`reference_playbook` from `veos paths`), a complete playbook written in this exact structure. It is the quality bar: match its **depth, specificity and decisiveness**, not its content. **Every section below is required.** Write concrete numbers (px, frames, seconds, hex values, font names), concrete examples drawn from the creator's own topics, and decided rules. **Never write menus or "you could…".**

The playbook is written for an AI editor (Claude), who reads it section by section while editing. Use tables. Use IDs (D1…, M1…, N1…, P-…, T-…, Z-…) so the editor can cite rules.

**Global rules come first.** `playbooks/_global/GLOBAL-RULES.md` (G1 no overlapping, G2 no clutter, G3 smooth motion, G4 high quality) applies to every playbook.
- Restate them in §2 as the first hard rules: "G1–G4 apply; see the global rules."
- **Never write a rule that conflicts with them.** A dense style is still clean: dense in *time* (many changes), not dense in *space* (many things at once).

---

## Header
- **Title:** `<Creator> Reel Editing Playbook (v1, "<style name>")`.
- **Purpose:** 3 lines on what this playbook makes the editor do.
- **Creator directives (non-negotiable), D1…D8:** the 5–8 things the creator cares most about, in their own words translated into editing rules. Each points to the section that implements it.
- **Quick index** of the sections.

## §1 Procedure (follow in order)
The per-reel procedure for this creator. Keep the engine's standard steps:
1. inventory
2. matte
3. transcribe
4. segment
5. classify lines + trigger words
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
- **Must include:** frame-0 stopper, visual-change cadence, the result by N seconds, banner/title limits, zero dead air, literal on-the-word visuals, the face never covered, promise integrity, facts only from the footage/script, spelling, audio targets (−14 LUFS, TP ≤ −1.5), and deterministic frame-based animation.
- **NEVER list:** this niche's clichés to avoid (e.g. fitness: stock gym footage, fake before/after; finance: fake charts or returns; food: stock food shots), contrast failures, fake UIs/metrics, decorative-only visuals, and banned transitions or sounds.

## §3 Worlds, screen modes, stage moves, layout, safe zones
- **Worlds:** the 2–3 visual worlds this creator's content lives in. Look, what each carries, how to enter and exit. Examples: studio/canvas/data for tech; kitchen/recipe-card/ingredient-table for food; gym/form-check/progress-chart for fitness.
- **Screen modes** with share-of-runtime targets.
- **Stage moves:** full, low, panel, inset, bubble, slide-aside, depth sandwich (from the renderer), and when to use each.
- **Layout diagram** with y-coordinates, and safe zones (Instagram: key text inside x 64–1016, y 110–1500).

## §4 Colour system
- **Palette:** roles → hex, each with **one job**, plus the text-on colour and contrast ratio.
- **Meanings:** before/after or bad/good axis (red → green unless the brand forbids it), max bright colours per frame, gradients. Brand colours appear only on brand names.
- **Must match `tokens.json`.**

## §5 Type tokens
- **Font map:** banner, captions, subtitles, titles, numbers, labels, comedy/notes. Only fonts that can be bundled (Google Fonts / OFL).
- **The banner/title recipe:** fill, stroke, shadow, size, word limit, chip rules, f0 behaviour, life, exit.
- **Caption systems:** big keyword captions, subtitles (language and case), glow or keyword titles, labels, kinetic type, hero numbers, stickers.
- **Language rules:** script (romanised Hinglish / English / Hindi / mixed), case, brand-name spelling, the glossary.

## §6 Hook system
- **Stopper test** for frame 0 and 0–3 s.
- **The default hook formula for this creator**, as a second-by-second table, plus 4–8 alternative formulas, each with an example **from their topics**.
- **Result pairs by topic:** a table of this creator's typical subjects → the bad state → the good state → how to show each. **This is the most important table for literal visuals.**
- **Banner/title writing** with templates and banned phrasing.
- **CTA formula** (their keyword/DM/link/follow habits).

## §7 Structure
- **Item/step markers:** pick one style per reel.
- **The item ritual.**
- **Open loops.**
- **Rhythm:** information vs entertainment beats, the energy curve.

## §8 B-roll and motion-graphics system
- **Families:** the kinds of visuals this creator needs (screen captures, product shots, their own B-roll clips, device mocks, data visuals, metaphor machines, kinetic type, comedy layer…), with the **assets the creator must supply** for each.
- **Pattern specs (P-…):** 20–60 named visual patterns, each with what's on screen, the motion recipe (frames at 30 fps), and when to use it. Invent patterns that fit **this niche's ideas**: a fitness "rep counter that fills a muscle diagram", a finance "money stack that splits into percentages", a cooking "ingredient drop into a bowl"…
- **Line → pattern lookup:** this creator's line types (from their actual topics) → primary pattern → alternates. **The editor classifies every sentence with this table.**
- **Data rules** (if they use numbers): quantities countable, the same axes for comparisons, real numbers only.
- **Asset rules:** real captures/footage first, generic mocks allowed only as stated, no stock clichés.

## §9 Transitions
- A library `T-01…` with frames and recipes, plus the grammar (which boundary uses which) and a budget per 60 s.

## §10 Motion tokens, zoom system, layers, finishing
- **Easing and timing tokens.**
- **Zoom system `Z-1…`:** recipes and tone use.
- **Layer order.**
- **Finishing:** grain, vignette, regrade rules.

## §11 Sound
**The bundled SFX pack:** `veos paths` → `sfx_pack`, with tags in its `catalog.json` (role, vibe, energy, use).
- **Choose this creator's sound palette from it:** the allowed vibes, the allowed and banned roles, a short list of preferred sound ids per use (transition, text-pop, reveal, data, warning, success, CTA, list cue), whether meme sounds are allowed, whether the hook is dry, and density (sounds per 10 s).
- **Mirror it in `tokens.json` → `sound`:**
  ```json
  {"palette_vibes": [...], "allowed_roles": [...], "banned_roles": [...], "preferred": {"<use>": ["<id>", ...]}, "dry_hook": bool, "silence_before_cta": true}
  ```
  plus `budgets.sfx_per_10s`.
- **Principle:** a sound only ever marks something the viewer sees happen. Restraint reads as premium.
- Tone palettes, the SFX ledger rules (no file more than 2×, one list cue), meme/comedy rules if the tone allows them, the music bed, silence and the outro, mix targets.
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
Two or three plans from this creator's real or typical topics: a hook table + a section-by-section pattern plan.

## §15 QA checklist
Grouped as stopper/hook, body, sound, truth/text/end.

## Appendix: banner/title bank
10 ready banners for their likely next reels.

---

## Companion files the builder also writes
- `tokens.json`: the machine-readable palette, fonts, type, layout, motion, camera presets, budgets and tone. Copy the schema of the `tokens.json` next to the reference playbook exactly, with this creator's values.
- `preview/index.html`: the "glimpse" page (see the `playbook` skill).
- `profile.md`: the interview answers and the inspiration analysis the playbook was built from (for later revisions).
