# Workflow contract v1: the `vibe-editing-os` plugin

**Owner:** Opus. This turns the manual Reel 7 run into skills. **The phase list below is exactly the sequence that produced Reel 7.**

## 1. User experience
```
/vibe-editing-os:reel <clips folder or files> [--script FILE] [--mode autopilot|director]
   → (workspace playbook) → prep (automatic) → rough cut → captions → inputs → plan → storyboard → ⛔ approve → render → final.mp4
/vibe-editing-os:reel            (no args) → resume the most recent project from where it stopped
"approve" / "hook thoda fast karo"  → continue / revise
```

**Gates:**
- **Autopilot (default):** only the storyboard gate.
- **Director:** a concept gate after the plan, the storyboard gate, and a final review.

**Project folder:** `<clips folder>/vibe-edit/`. If the clips are scattered, use the folder of the first clip.

## 2. Plugin layout
```
plugin/
  .claude-plugin/plugin.json      name "vibe-editing-os"; userConfig: veos_home (directory, optional)
  bin/veos  bin/veos.cmd          shim → VEOS_HOME python -m veos (VEOS_HOME/venv, else VEOS_HOME/dev-venv)
  hooks/hooks.json                SessionStart(startup|resume) → `veos doctor --quick` (one status line)
  agents/veos-runner.md           model: sonnet. Runs engine commands, waits, returns ONLY the JSON summaries
  agents/frame-reviewer.md        model: sonnet. Reads contact sheets against a checklist, returns failures only
  skills/reel/SKILL.md            orchestrator (state machine, gates, resume)
  skills/reel-prep/SKILL.md       ingest → conform → transcribe → matte (delegates to veos-runner)
  skills/reel-roughcut/SKILL.md   Claude chooses takes, removes flubs/dead air → edl.json → veos cut
  skills/reel-captions/SKILL.md   Claude romanises / fixes caption text → veos captions apply
  skills/reel-plan/SKILL.md       Claude writes plan/timeline.json + plan/scenes.js (bespoke scenes, guided by the playbook) → scenes-meta → measure → validate loop
  skills/reel-storyboard/SKILL.md tokens → prep-frames → bundle → storyboard → open → gate
  skills/reel-render/SKILL.md     render → mix → assemble → qa → side-by-side (optional) → report
```

**Path rule:** skills reference repo assets through the engine (`veos paths` prints the playbooks, renderer player/core and veos_home paths as JSON). **Skills never hard-code paths.** In dev, the engine resolves the repo root from its own location; in the product it resolves `VEOS_HOME/app/`.

## 3. Phase state machine (`work/../project.json`, managed ONLY via `veos project`)
| Phase | Done when | Skill | Model |
|---|---|---|---|
| `init` | project.json exists | reel | main |
| `prep` | sources.json, src/, audio/, words/, matte/, face/ exist for every talking-head source | reel-prep | veos-runner (sonnet) |
| `roughcut` | edl.json + cutmap.json + words.edit.json | reel-roughcut | **main (Opus)** |
| `captions` | every word in words.edit.json has a `caption` field | reel-captions | **main** (or sonnet if no Devanagari / no fixes) |
| `inputs` | the creator's per-reel inputs are collected (screen recordings via `veos asset add`, links, numbers) and stored with `veos project set inputs=@file.json` (may be `{}`) | reel-inputs | **main** |
| `plan` | plan/timeline.json validates (`passed: true`) | reel-plan | **main (Opus)** |
| `storyboard` | review/mockup.html built | reel-storyboard | veos-runner + frame-reviewer |
| `approved` | the user approved (autopilot gate) | reel | main |
| `render` | out/final.mp4 + qa all_pass | reel-render | veos-runner |
| `done` | reported | reel | main |

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
| `veos learn add\|list\|remove --playbook ID ...` | The playbook's learned feedback (`learned.md` / `learned.json`): rules from the creator that override the playbook body, never the global rules. The planner reads `learned.md` together with `playbook.md` | entries |
| `veos asset add <file> --project P [--name N]` / `veos asset list --project P` | Screen recordings (30 fps JPEG frames, `ctx.videoFrame`), images and logos (`ctx.asset`) for this reel | name, kind, frames/size |
| `veos validate --project P` | Besides the playbook rules it always runs global checks **G1 no overlap, G2 no clutter, G3 smooth motion** (needs `veos measure`; builds the per-frame motion measure itself) | passed, failures |
| `veos paths` | repo/app root, playbooks, renderer/player.html, renderer/core.js, VEOS_HOME | JSON |
| `veos bundle --out DIR` | (B-5) bundle into a chosen folder | — |

## 5. Agents
- **`veos-runner`** (`model: sonnet`, tools: Bash, Read):
  - Receives a list of `veos` commands and a project path.
  - Runs them in order, stopping at the first `"ok": false`.
  - Returns the JSON lines only, plus a one-line verdict.
  - Never edits files and never interprets creative choices.
- **`frame-reviewer`** (`model: sonnet`, tools: Read, Bash):
  - Receives contact-sheet paths, the timeline beats summary and a checklist (face covered? text overlapping text? off-screen? unreadable? empty frame > 1 s? broken glyphs or emoji?).
  - Returns a JSON list of `{frame, issue, layer_hint}` and nothing else.

## 6. What the planner reads (no style pack, no component catalogue)
- `playbooks/<id>/playbook.md`: the creator's editing playbook (how the hook, body and CTA are edited, what each tone looks like, layout rules).
- `playbooks/<id>/tokens.json`: his colours by role, fonts by slot, type, layout, motion, camera presets, budgets, tone (`veos tokens` resolves it into `work/tokens.json`; optional `plan/tokens.override.json` per reel).
- `renderer/SCENES-API.md`: the scene fields, the ctx toolkit, presets, determinism and performance rules (replaces the old component catalogue).
- `veos context`: the compact words/faces/cut context.

For every reel the planner **writes the visuals as code** (`plan/scenes.js`), exactly as the creator's original procedure did (reuse the core, write new scenes per reel). Loop: `veos scenes-meta` → `veos measure` → `veos validate` → fix → look at frames.
