# Vibe Editing OS plugin

Claude Code plugin that turns raw talking-head clips into a finished motion-graphics reel.

- Entry point: `/vibe-editing-os:reel <clips folder or files> [--script FILE] [--mode autopilot|director]`
- The workflow contract (phases, gates, agents) is in `WORKFLOW.md`.
- `bin/veos` is a shim to the engine in `VEOS_HOME` (option `veos_home`, env `VEOS_HOME`, or the default per-OS location). Without an engine it prints `ENGINE_MISSING`.
- Licence: `/vibe-editing-os:setup` asks for the key from the purchase email and activates it (max 2 computers per key; `setup move` frees this computer). Every engine command except `doctor`, `licence` and `paths` needs an active licence (`LICENCE_REQUIRED` otherwise); 7 days offline grace. Developers: `VEOS_DEV=1` or the dev venv skip it. Details: `WORKFLOW.md` section 4, `engine/src/veos/licence.py`.
- Models: every reel skill and the playbook skill run the Director on Opus 5.5 at high effort (`model: claude-opus-5-5`, `effort: high`; setup runs on the user's own model). Agents (all on Sonnet 5.5, high effort): `veos-runner` (runs engine commands), `frame-reviewer` (contact-sheet QA), `frame-looker` (describes the cut from the `veos look` sheets → plan/look.md), `rough-cutter` (decides the takes → edl.json) and `scene-coder` (writes plan/scenes.js from the planner's scene plan and briefs).
- Local test: `claude --plugin-dir <this folder>`; validate with `claude plugin validate <this folder>`.
- Scripts under `bin/` must keep LF line endings.
