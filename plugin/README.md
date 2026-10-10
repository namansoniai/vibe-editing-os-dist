# Vibe Editing OS plugin

Claude Code plugin that turns raw talking-head clips (or a voice-over) into a finished motion-graphics reel in the
creator's own style.

- Entry point: `/vibe-editing-os:reel <clips folder or files> [--script FILE]`. Two stops per reel: the cut (a video) and
  the storyboard.
- Skills: `setup`, `playbook`, `reel`, `edit`, `render`. The flow, phases and commands are in `WORKFLOW.md`.
- Models: every skill except `setup` runs on Opus 5.5 at high effort (`model: claude-opus-5-5`, `effort: high`); setup
  runs on the user's own model. There are no agents: the editor does every step itself.
- Works with PowerShell only (Claude Desktop on Windows), Bash only, or both.
- `bin/veos` / `bin/veos.cmd` wrap the engine in `VEOS_HOME` (option `veos_home`, env `VEOS_HOME`, or the default per-OS
  location). Without an engine they print `ENGINE_MISSING`.
- Licence: `/vibe-editing-os:setup` asks for the key from the purchase email and activates it (max 2 computers per key;
  `setup move` frees this computer). Every engine command except `doctor`, `licence` and `paths` needs an active licence
  (`LICENCE_REQUIRED` otherwise); 7 days offline grace. Developers: `VEOS_DEV=1` or the dev venv skip it.
- `skills/edit/SOUNDS.md` is generated from `assets/sfx/catalog.json` by `tools/sounds_list.py`.
- Local test: `claude --plugin-dir <this folder>`; validate with `claude plugin validate <this folder>`.
- Scripts under `bin/` keep their line endings (`veos` LF, `veos.cmd` CRLF).
