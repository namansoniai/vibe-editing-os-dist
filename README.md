# Vibe Editing OS

Turn raw talking-head clips into finished short-form reels, edited in **your** style, inside the Claude desktop app.

## Install (no Terminal needed), version 0.3.0
1. Install the **Claude desktop app**, open the **Code** tab, and start a **local** session in any folder.
2. Paste this message and send it:

> Please set up the Vibe Editing OS plugin for me. In my user settings file `~/.claude/settings.json` (create it if missing, keep everything already in it), add the marketplace `"vibe-editing-os": {"source": {"source": "url", "url": "https://raw.githubusercontent.com/namansoniai/vibe-editing-os-dist/main/.claude-plugin/marketplace.json"}}` under `extraKnownMarketplaces`, and add `"vibe-editing-os@vibe-editing-os": true` under `enabledPlugins`. Then tell me to start a new session.

3. Start a **new session**. If the plugin isn't active yet, open **+ → Plugins → Add plugin** and install **vibe-editing-os**.
4. Type `/vibe-editing-os:setup`. This one-time install takes 15–20 min (~3.6 GB).
5. Type `/vibe-editing-os:playbook` to build your editing playbook.
6. Type `/vibe-editing-os:reel` and give it the folder with your raw clips.
