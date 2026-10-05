---
name: setup
description: One-time install of the Vibe Editing OS engine on this computer (Python, ffmpeg, browser, AI models), or update it with "update". Run this first after installing the plugin.
argument-hint: "[update]"
user-invocable: true
---
# setup

Installs everything the plugin needs into one folder (`VEOS_HOME`; Windows `%LOCALAPPDATA%\VibeEditingOS`, macOS `~/Library/Application Support/VibeEditingOS`). No admin rights, nothing else on the computer is changed.

Tell the user in plain words, then ask for an OK before running anything:
- It downloads about 3 GB: the editing engine with its own Python, the video tool ffmpeg, a rendering browser, and three AI models (speech-to-text, background removal, face detection).
- It takes 10 to 20 minutes depending on the connection, and can be safely re-run or resumed if it stops.
- It needs about 5 GB free now (and 20 GB later for renders).

## Install (argument empty)

1. Check whether it is already installed: run `veos doctor --quick`. If it says `ready: true`, say so and stop (offer `/vibe-editing-os:setup update`).
2. After the user says OK, run the installer for the OS in the background, because it can exceed 10 minutes. Detect the OS with Bash `uname -s` (Darwin = macOS; otherwise Windows).
   - Windows: `powershell -NoProfile -ExecutionPolicy Bypass -File "${CLAUDE_PLUGIN_ROOT}/setup/install.ps1"`
   - macOS: `bash "${CLAUDE_PLUGIN_ROOT}/setup/install.sh"`
   Use Bash with `run_in_background: true` and `timeout: 600000`.
3. Poll the output every minute or two (read the background output file, or `tail -n 5` of `install.log` in VEOS_HOME). The lines look like `[5/10] Installing the veos engine...`. Give the user one short progress line each time the step number changes, not the raw log.
4. When it ends, the last line is JSON.
   - `"ok":true`: run `veos doctor` and report plainly: ready or not, and any failing check with its hint. If `doctor_ready` is false, name the missing piece and offer to re-run setup.
   - `"ok":false`: tell the user which step failed (`step`), the `error` in one sentence, and the `hint`. Common causes: no internet or a proxy (`download failed`), a private repository without a signed-in git (`step: app`), a full disk. Offer to re-run: it resumes and skips what is already done.
5. If the JSON says `repository not configured`, ask the user for the GitHub repo URL and re-run with env `VEOS_REPO=<url>` (Windows PowerShell: `$env:VEOS_REPO='<url>'; powershell ...`).

## Update (argument `update`)

Run the same script with the update flag (`-Update` on Windows, `--update` on macOS). It pulls the newest app version and reinstalls the engine packages only if the engine changed; models, browser and ffmpeg that exist are kept, and the user's own playbooks in `VEOS_HOME/playbooks` are never touched. Then run `veos doctor` and report as above.

## Notes
- `veos` is on PATH while the plugin is enabled; before the first install it prints `ENGINE_MISSING`, which means: run this skill.
- Never delete `VEOS_HOME`. To uninstall, the user deletes that folder.
