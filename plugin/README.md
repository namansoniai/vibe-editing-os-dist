# Vibe Editing OS plugin

Claude Code plugin that turns raw talking-head clips into a finished motion-graphics reel.

- Entry point: `/vibe-editing-os:reel <clips folder or files> [--script FILE] [--mode autopilot|director]`
- The workflow contract (phases, gates, agents) is in `WORKFLOW.md`.
- `bin/veos` is a shim to the engine in `VEOS_HOME` (option `veos_home`, env `VEOS_HOME`, or the default per-OS location). Without an engine it prints `ENGINE_MISSING`.
- Agents: `veos-runner` (runs engine commands) and `frame-reviewer` (contact-sheet QA); both run on Sonnet.
- Local test: `claude --plugin-dir <this folder>`; validate with `claude plugin validate <this folder>`.
- Scripts under `bin/` must keep LF line endings.
