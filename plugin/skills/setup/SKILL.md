---
name: setup
description: One-time install of the Vibe Editing OS engine on this computer (licence key, Python, ffmpeg, browser, AI models), or update it with "update". Also activates or checks the licence ("activate my licence", "licence status") and moves it to another computer ("move my licence", "new laptop", "deactivate this computer"). Run this first after installing the plugin.
argument-hint: "[update | licence | move]"
user-invocable: true
---
# setup

Installs everything the plugin needs into one folder (`VEOS_HOME`; Windows `%LOCALAPPDATA%\VibeEditingOS`, macOS `~/Library/Application Support/VibeEditingOS`). No admin rights, nothing else on the computer is changed.

Vibe Editing OS needs a **licence key** from the purchase email (it looks like `VEOS-XXXX-XXXX-XXXX-XXXX`). One key works on **2 computers**. The engine checks it online about once a day and keeps working **offline for 7 days**. Only the key, an anonymous computer id and the computer's name are sent.

**Which part to run:**
- argument empty → **Install**
- argument `update` → **Update**
- argument `licence`, "activate my licence", or any engine command answered `LICENCE_REQUIRED` → **Activate the licence**
- argument `move`, "move my licence", "new laptop", "deactivate this computer", "free up a device" → **Move my licence**
- "licence status", "which plan am I on" → run `veos licence status` and say its `line` in plain words (plan, computers used, last check).

## Install (argument empty)

1. Check whether it is already installed: run `veos doctor --quick`.
   - `ready: true`: say it's ready and stop (offer `/vibe-editing-os:setup update`).
   - `machine_ready: true` but `licence_ok: false`: the engine is installed, only the licence is missing: go to **Activate the licence**.
2. Tell the user in plain words:
   - It downloads about 3 GB: the editing engine with its own Python, the video tool ffmpeg, a rendering browser, and three AI models (speech-to-text, background removal, face detection).
   - It takes 10 to 20 minutes depending on the connection, and can be safely re-run or resumed if it stops.
   - It needs about 4 GB to install, plus about 1 GB of free space per minute of video while you edit.
3. Ask with **one AskUserQuestion call, two questions**:
   - **"Ready to install now?"** Options: "Yes, install now", "Not now".
   - **"Your licence key (from your purchase email)"**: "Pick *Other* and paste the key. It looks like VEOS-XXXX-XXXX-XXXX-XXXX." Options: "I can't find my key", "I haven't bought it yet".
   Then:
   - "Not now": stop politely.
   - "I can't find my key": say "Search your inbox for 'Vibe Editing OS'. Or open https://veos-licence.shipwithoutcode.workers.dev/find-key and enter your payment ID (it starts with `pay_`, it's in the Razorpay receipt email) and the email you paid with." Ask for the key again (same question alone).
   - "I haven't bought it yet": say a licence is needed to use Vibe Editing OS, and stop.
   - A pasted key: keep only its letters, digits and dashes (the engine fixes case, spaces and look-alike characters). **Never repeat the full key back**; say "the key ending …XXXX".
4. Run the installer for the OS **in the background** with the key in the environment (it can exceed 10 minutes). Detect the OS with Bash `uname -s` (Darwin = macOS; otherwise Windows).
   - Windows: `VEOS_LICENCE_KEY='<key>' powershell -NoProfile -ExecutionPolicy Bypass -File "${CLAUDE_PLUGIN_ROOT}/setup/install.ps1"`
   - macOS: `VEOS_LICENCE_KEY='<key>' bash "${CLAUDE_PLUGIN_ROOT}/setup/install.sh"`
   Use Bash with `run_in_background: true` and `timeout: 600000`. The installer activates the licence right after it installs the engine (step 5), **before** the big downloads, so a wrong key is caught in the first few minutes.
5. Poll the output every minute or two (read the background output file, or `tail -n 5` of `install.log` in VEOS_HOME). The lines look like `[5/10] Installing the veos engine...`. Give the user one short progress line each time the step number changes, not the raw log. When "activating your licence" passes, say "Licence activated" once.
6. When it ends, the last line is JSON.
   - `"ok":true`: run `veos doctor` and report plainly: ready or not, its `licence` line, and any failing check with its hint. If `doctor_ready` is false, name the missing piece and offer to re-run setup.
   - `"ok":false` with `"step":"licence"`: the key was not accepted. Handle `licence_error` with **Licence answers** below, ask for the key again if that helps, and re-run the installer with the new key (it resumes; everything already done is skipped).
   - `"ok":false` (other steps): tell the user which step failed (`step`), the `error` in one sentence, and the `hint`. Common causes: no internet or a proxy (`download failed`), a private repository without a signed-in git (`step: app`), a full disk. Offer to re-run: it resumes and skips what is already done.
7. If the JSON says `repository not configured`, ask the user for the GitHub repo URL and re-run with env `VEOS_REPO=<url>` as well.

## Update (argument `update`)

Run the same script with the update flag (`-Update` on Windows, `--update` on macOS), no key needed. It pulls the newest app version and reinstalls the engine packages only if the engine changed; models, browser and ffmpeg that exist are kept, and the user's own playbooks in `VEOS_HOME/playbooks` are never touched. Then run `veos doctor` and report as above (if `licence_ok` is false, continue with **Activate the licence**).

## Activate the licence (argument `licence`, or after `LICENCE_REQUIRED`)

1. Run `veos licence status`. If `active: true`, say "Your licence is active: <plan> plan, <n> of 2 computers" and stop, unless they want a different key.
2. Ask with AskUserQuestion, the licence-key question from Install step 3 (alone).
3. Run `veos licence activate --key '<key>'`.
   - ok: say its `message` in plain words ("Licence activated: Studio plan, this computer is 1 of 2."). If it says `replaced_key`, mention the old key on this computer was replaced.
   - not ok: **Licence answers** below.

## Move my licence (argument `move`)

This frees **this** computer's slot so the key can be activated on another computer.
1. Run `veos licence status`. If nothing is active here, say "This computer doesn't use a licence slot, so there is nothing to free. If your key says it's already on 2 computers, run this on one of those, or contact support." and stop.
2. Ask with AskUserQuestion: "Free this computer's licence slot? Vibe Editing OS stops working here until you activate it again." Options: "Yes, free it", "No, keep it".
3. Yes: run `veos licence deactivate`. Say its `message`: this computer is freed and the key is now on N of 2 computers. On the new computer: install the plugin, run `/vibe-editing-os:setup`, and paste the same key.
4. `LICENCE_OFFLINE`: "I couldn't reach the licence server, so this computer still counts. Check your internet and try again."
5. The old computer is lost or broken (they can't run this there): "Contact support at enquiry@deccansoft.com, and we'll free the old computer's slot."

## Licence answers (error code → what to say, then the next step)

Never show the code or raw JSON. Use the `message` and `hint` from the engine, in plain words:
- `KEY_INVALID`: "That key doesn't look right. Copy it from the purchase email (copy and paste works best); it looks like VEOS-XXXX-XXXX-XXXX-XXXX." Offer the find-key page (Install step 3). Ask again.
- `KEY_DISABLED`: "This key has been switched off. Please contact support at enquiry@deccansoft.com." Stop.
- `DEVICE_LIMIT`: "Your licence is already active on 2 computers. To use it here, free one of them: on the old computer, ask me to **move my licence**. If you can't use that computer any more, contact support at enquiry@deccansoft.com and we'll free the slot." Stop.
- `LICENCE_OFFLINE`: "I couldn't reach the licence server. Check your internet connection and try again. Once activated, you can keep working offline for 7 days." Offer to retry.
- `DEVICE_NOT_REGISTERED` or `LICENCE_REQUIRED`: "This computer isn't activated (or was moved to another computer)." Go to **Activate the licence**.
- anything else: say the `message` and `hint` in one sentence each.

## Notes
- Faceless (voice-over) reels need the speech model, the browser and ffmpeg, but not the background-removal or face models: if only those failed, say faceless reels already work and offer to re-run setup for talking-head reels.
- `veos` is on PATH while the plugin is enabled; before the first install it prints `ENGINE_MISSING`, which means: run this skill.
- Every engine command except `veos doctor`, `veos licence …` and `veos paths` needs an active licence; without one it answers `LICENCE_REQUIRED` ("activate your licence first": the **Activate the licence** section).
- Never delete `VEOS_HOME`. To uninstall, the user first runs **Move my licence** (to free the slot), then deletes that folder.
- Never edit, copy or create `VEOS_HOME/licence.json` by hand: it is signed and tied to this computer.

**Never patch, downgrade or edit the engine, and never ask the user to pick an engine fix.** Report the failing step plainly and suggest `/vibe-editing-os:setup update`.
