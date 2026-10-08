# Workflow contract v1: the `vibe-editing-os` plugin

**Owner:** Opus. This turns the manual Reel 7 run into skills. **The phase list below is exactly the sequence that produced Reel 7.**

## 1. User experience
```
/vibe-editing-os:reel <clips folder or files> [--script FILE] [--mode autopilot|director]
   → (workspace playbook) → prep (automatic) → rough cut → ⛔ approve the cut → captions → inputs → plan → storyboard → ⛔ approve → render → final.mp4
/vibe-editing-os:reel            (no args) → resume the most recent project from where it stopped
"approve" / "hook thoda fast karo"  → continue / revise
```

**Gates:**
- **Autopilot (default):** the cut gate (after the rough cut, before captions) and the storyboard gate.
- **Director:** the cut gate, a concept gate after the plan check (before any scene code), the storyboard gate, and a final review.

**Project folder:** `<clips folder>/vibe-edit/`. If the clips are scattered, use the folder of the first clip.

## 2. Plugin layout
```
plugin/
  .claude-plugin/plugin.json      name "vibe-editing-os"; userConfig: veos_home (directory, optional)
  bin/veos  bin/veos.cmd          shim → VEOS_HOME python -m veos (VEOS_HOME/venv, else VEOS_HOME/dev-venv)
  hooks/hooks.json                SessionStart(startup|resume) → `veos doctor --quick` (one status line)
  agents/veos-runner.md           model: claude-sonnet-5-5, effort high. Runs engine commands, waits, returns ONLY the JSON summaries
  agents/frame-reviewer.md        model: claude-sonnet-5-5, effort high. Reads contact sheets against a checklist, returns failures only
  agents/frame-looker.md          model: claude-sonnet-5-5, effort high. Reads the `veos look` sheets + look.json, writes plan/look.md (what is on screen)
  agents/rough-cutter.md          model: claude-sonnet-5-5, effort high. Reads `veos roughcut-candidates`, decides the takes, writes edl.json, runs veos cut
  agents/scene-coder.md           model: claude-sonnet-5-5, effort high. Writes plan/scenes.js from the planner's plan (scenes.plan.json + scene-briefs.md) until validate passes (V-PLAN included)
  skills/reel/SKILL.md            orchestrator (state machine, gates, resume)
  skills/reel-prep/SKILL.md       ingest → conform → transcribe → faces (delegates to veos-runner); the person cut-out waits for the plan
  skills/reel-roughcut/SKILL.md   delegates to rough-cutter: takes, flubs, dead air → edl.json → veos cut → the cut gate (user approves / asks for changes)
  skills/reel-captions/SKILL.md   Claude romanises / fixes caption text → veos captions apply
  skills/reel-plan/SKILL.md       Opus writes the plan (timeline.json + scenes.plan.json + scene-briefs.md) → validate --plan → scene-coder writes scenes.js (validate loop) → veos stills → frame-reviewer against the briefs
  skills/reel-storyboard/SKILL.md tokens → prep-frames → bundle → storyboard → open → gate
  skills/reel-render/SKILL.md     render → mix → assemble → qa → side-by-side (optional) → report
```

**Path rule:** skills reference repo assets through the engine (`veos paths` prints the playbooks, renderer player/core and veos_home paths as JSON). **Skills never hard-code paths.** In dev, the engine resolves the repo root from its own location; in the product it resolves `VEOS_HOME/app/`.

## 3. Phase state machine (`work/../project.json`, managed ONLY via `veos project`)
| Phase | Done when | Skill | Model |
|---|---|---|---|
| `init` | project.json exists | reel | main |
| `prep` | sources.json, src/, audio/, words/, face/ exist for every talking-head source (no matte: `veos matte --if-needed` runs after the plan check, only on the kept frames) | reel-prep | veos-runner (sonnet) |
| `roughcut` | edl.json + cutmap.json + words.edit.json, **and the user approved the cut** (cut_proxy.mp4 opened; changes go back to the rough-cutter as `CHANGES:` notes) | reel-roughcut | rough-cutter (sonnet) + main (the gate) |
| `captions` | every word in words.edit.json has a `caption` field | reel-captions | **main** (or sonnet if no Devanagari / no fixes) |
| `inputs` | the creator's per-reel inputs are collected (screen recordings via `veos asset add`, links, numbers) and stored with `veos project set inputs=@file.json` (may be `{}`) | reel-inputs | **main** |
| `plan` | `veos validate` passes (V-PLAN included) and the stills review is clean | reel-plan (look → index → ideas → plan → plan check → scene code → stills review) | **main (Opus)** plans + frame-looker, scene-coder, frame-reviewer (sonnet) |
| `storyboard` | review/mockup.html built | reel-storyboard | veos-runner + frame-reviewer |
| `approved` | the user approved (autopilot gate) | reel | main |
| `render` | out/final.mp4 + qa all_pass | reel-render | veos-runner |
| `done` | reported | reel | main |

**Faceless branch (`source_type: voiceover_only`, E-12).** Chosen at `project init` (a voice-over file, the creator says "voice-over only", or a voice-over playbook). Same phases, different steps:
| Phase | Voice-over step |
|---|---|
| `prep` | `ingest` (VO = source `V`, picture ignored) → `conform` (audio only) → `transcribe` (aligned to the script) → no matte. Done when `sources.json` (source_type `voiceover_only`), `audio/V.wav`, `words/V.json` exist |
| `roughcut` | `veos cut --identity [--tighten]`: the VO is the timeline; retakes or flubs in the VO can still be cut with a planner EDL |
| `inputs` | the creator's own B-roll, screen recordings, photos to layer over the VO (`veos asset add`), plus third-party moments via ask-then-create |
| `plan` | stage `hidden` throughout; one scene per sentence, no gaps; kinetic type, diagrams + `canvas_camera`, cards, morph hand-offs, ambient worlds (`VEOS.fx`, SCENES-API §10); V-CANVAS |
| `storyboard` / `render` | unchanged (`prep-frames` writes nothing; `voice` builds the VO track) |

- Each phase is **idempotent and resumable**. Re-running a phase re-uses cached outputs.
- `veos project set phase=<x>` is called **after** a phase's done-condition is verified, never before.
- A failure records `last_error` and stops with a plain-language message.

## 4. New engine commands (Phase W1)
| Command | Purpose | Output (stdout JSON, small) |
|---|---|---|
| `veos project init <clips…> --project P [--script F] [--mode autopilot\|director] [--playbook ID]` | Create project.json: sources list, script path, mode, playbook (from the folder's workspace; no silent default), phase=init, created | path, phase |
| `veos project show --project P` / `veos project set --project P key=value …` | Read/update state (`phase`, `approved_at`, `last_error`, `notes`…) | the state |
| `veos project latest` | The most recently modified project (projects registered in `VEOS_HOME/projects.json`) | path, phase |
| `veos context --project P [--part sources\|words\|faces\|all]` | **Compact planning context for Claude:** sources with setups and durations; face ranges per setup (x, y, w, h min/median/max + head-top estimate); the word list as `i:word@t` lines (edit time if cut exists, else per source) with low-confidence marks and pauses ≥ 0.3 s; script excerpt; gaps | text-ish JSON designed to be read by the model (≤ ~3k tokens per minute of speech) |
| `veos captions apply <map.json> --project P` | map = `{"<i>": "caption text", …}` (edit-time word indices). Writes the `caption` field; `""` hides the word; validates that every index exists | applied, missing |
| `veos scenes-meta --project P` | Load `plan/scenes.js` headless; write `plan/scenes.meta.json`; registration errors name the scene id | scene ids |
| `veos measure --project P [--every 10]` | Render sampled frames headless; write `plan/measure.json` (rendered rect per scene per frame) | frames sampled, ms/frame |
| `veos workspace get [--dir D]` / `veos workspace set --playbook ID [--dir D]` | A folder remembers its playbook (`.vibe-editing-os.json`, found by walking up). `get` also lists the available playbooks. `project init` takes the playbook from it; with none it fails `PLAYBOOK_REQUIRED` ("choose a playbook first") | found, dir, playbook, playbooks[] |
| `veos playbook new-id --name "Aria Mehta" [--handle @x]` | Unique kebab id for a new playbook; setup never overwrites an existing one | id, path |
| `veos learn add\|list\|remove --playbook ID ...` | The playbook's learned feedback (`learned.md` / `learned.json`): rules from the creator that override the playbook body, never the global rules. The planner reads `learned.md` together with `playbook.md`. On a template copy, `add --change PATH=VALUE` is classified against the copy's `locks` and applied (VAR/TUNE → `tuned`; DNA or out-of-range TUNE → applied and logged as DV-n, no confirmation or warning; only NC is refused, in one line with the nearest option; `--nc NC-n` for prose) | entries; status, class, message, alternative |
| `veos templates list [--all]` / `gallery [--out F] [--faceless-first]` / `copy <id> [--name] [--handle] [--colors] [--language] [--cta] [--id]` / `check [ID…]` | Path A of the `playbook` skill: the shipped style templates (`playbooks/_styles/<id>/`, TEMPLATE-PACKAGE.md; hidden when an engine capability is missing), the picker page, the buyer's branded copy (`kind: style_copy` + `lineage` + `profile.md`; link it with `workspace set`), and the package checker for template authors | templates[], hidden; out, cards; id, title, nudge_line, notes; results |
| `veos asset add <file> --project P [--name N]` / `veos asset list --project P` | Screen recordings (30 fps JPEG frames, `ctx.videoFrame`), images and logos (`ctx.asset`) for this reel | name, kind, frames/size |
| `veos validate --project P` | Besides the playbook rules it always runs global checks **G1 no overlap, G2 no clutter, G3 smooth motion** (needs `veos measure`; builds the per-frame motion measure itself) | passed, failures |
| `veos licence activate --key K` / `status` / `validate` / `deactivate` | The buyer's licence (`engine/src/veos/licence.py`, server `veos-licence.shipwithoutcode.workers.dev`). `activate` normalises the key, registers this computer (device id = hash of machine id + OS user; max 2 per key) and saves the signed `VEOS_HOME/licence.json`; `status` is local; `validate` re-checks online (offline grace 7 days since the last successful check); `deactivate` frees this computer ("move my licence"). Errors: `KEY_INVALID`, `KEY_DISABLED`, `DEVICE_LIMIT`, `DEVICE_NOT_REGISTERED`, `LICENCE_OFFLINE` (each with a plain hint) | tier, tier_name, devices_used, max_devices, last_validated, offline_days_left, message / line |
| **licence gate** | Every command except `doctor`, `licence` and `paths` first checks the licence: no network while the last check is < 24 h old, then one online re-check; offline it keeps working until 7 days after the last successful check. Otherwise `LICENCE_REQUIRED`, which skills turn into "activate your licence first" (`/vibe-editing-os:setup licence`). Dev bypass: env `VEOS_DEV=1` or the dev venv (`VEOS_HOME/dev-venv`); `VEOS_DEV=0` forces the gate on. Template tiers: Raw = own playbook only (path B), Rough Cut = `tier: core` templates, Studio / Director's Cut = all; the rest appear in `templates list` → `locked` and in the gallery as "Upgrade to … to unlock"; `copy` refuses them (`TEMPLATE_LOCKED`) | — |
| `veos paths` | repo/app root, playbooks, renderer/player.html, renderer/core.js, VEOS_HOME, `sfx_pack` (local download cache, `VEOS_HOME/sfx`), `sfx_catalog` (shipped `assets/sfx/catalog.json`) | JSON |
| `veos sfx catalog [--pack DIR] [--descriptions CSV] [--draft] [--update]` / `veos sfx tag [--pack DIR] tags.json` | Pack owner only, once per pack: build the catalogue from the owner's `SFX_Descriptions.csv` (works without audio; with `--pack` it also measures; Category gives default roles; duplicates, songs and do-not-use rows are `excluded`). Claude reviews the guesses and merges corrections (`{id: {role, vibe, energy, use}}`, marked `reviewed`). Only `assets/sfx/catalog.json` ships; `tools/publish_sfx.py PACK_DIR` uploads the audio to the public sfx repo | sounds, excluded_by_reason, by_role / tagged |
| `veos sfx fetch --ids a,b \| --playbook ID \| --project P` | Download only the missing sounds into `VEOS_HOME/sfx` (3 tries, size check). `veos sfx --project P` does this automatically for its cues | requested, downloaded, mb_downloaded |
| `veos sfx --project P` | Fetch missing sounds, then build `work/sfx.wav` from `timeline.sfx` + the catalogue (anchors, default dB by role, voice-relative level). Then `veos mix <voice> <out> --dur D --sfx work/sfx.wav`; the mix fails (`SFX_TOO_LOUD`) if the SFX are not >= 20 dB under the voice (median) or any non-sub cue is within 6 dB of speech | cues, bus peak |
| sound rules | `veos validate` always checks cues with a catalogue `id`: S1 tied to a visual event (+-3 frames), S2 vibe/beat-tone match, S3 palette, S4 restraint, S5 ledger, S6 catalogue (`engine/SPEC.md` section 6). The storyboard lists sounds as `id - why` and its animatic voice includes them | failures |
| `veos bundle --out DIR` | (B-5) bundle into a chosen folder | — |

## 5. Agents
- **`veos-runner`** (`model: claude-sonnet-5-5`, `effort: high`, tools: Bash, Read):
  - Receives a list of `veos` commands and a project path.
  - Runs them in order, stopping at the first `"ok": false`.
  - Returns the JSON lines only, plus a one-line verdict.
  - Never edits files and never interprets creative choices.
- **`frame-reviewer`** (`model: claude-sonnet-5-5`, `effort: high`, tools: Read, Bash):
  - Receives contact-sheet paths, the timeline beats summary and a checklist (face covered? text overlapping text? off-screen? unreadable? empty frame > 1 s? broken glyphs or emoji?).
  - Returns a JSON list of `{frame, issue, layer_hint}` and nothing else.
- **`frame-looker`** (`model: claude-sonnet-5-5`, `effort: high`, tools: Read, Bash):
  - Reads the `veos look` sheets and `look.json` of the cut; writes `plan/look.md` (setup, a timecoded timeline of moments, free space, flags), ≤ ~45 lines per minute.
  - Describes, never measures or advises; frame-left / frame-right only; "unclear" rather than a guess.
- **`rough-cutter`** (`model: claude-sonnet-5-5`, `effort: high`, tools: Read, Bash, Write):
  - Reads `veos roughcut-candidates` (sentences, take groups, false starts, pauses, fillers, a suggested EDL); decides the takes by the rough-cut rules, compares frames (`veos look --src --at`) only when a line has 2+ takes.
  - Writes `work/edl.json`, runs `veos cut`, returns one `CUT:` line and a verdict.

## 6. What the planner reads (no style pack, no component catalogue)
- `playbooks/<id>/playbook.md`: the creator's editing playbook (how the hook, body and CTA are edited, what each tone looks like, layout rules).
- `playbooks/<id>/tokens.json`: his colours by role, fonts by slot, type, layout, motion, camera presets, budgets, tone (`veos tokens` resolves it into `work/tokens.json`; optional `plan/tokens.override.json` per reel).
- `renderer/SCENES-API.md`: the scene fields, the ctx toolkit, presets, determinism and performance rules (replaces the old component catalogue).
- `veos context`: the compact words/faces/cut context.

For every reel the planner **writes the visuals as code** (`plan/scenes.js`), exactly as the creator's original procedure did (reuse the core, write new scenes per reel). Loop: `veos scenes-meta` → `veos measure` → `veos validate` → fix → look at frames.
