#!/usr/bin/env python3
"""Register the SessionStart update-check hook in ~/.claude/settings.json.

Idempotent: re-running won't duplicate the entry. Preserves any other hooks
or settings the user already has.
"""
import json
import pathlib

HOME = pathlib.Path.home()
SETTINGS = HOME / ".claude" / "settings.json"
HOOK_CMD = "bash ~/.claude/skills/bio-skills/scripts/check-update.sh 2>/dev/null || true"

SETTINGS.parent.mkdir(parents=True, exist_ok=True)
data = json.loads(SETTINGS.read_text()) if SETTINGS.exists() else {}

hooks = data.setdefault("hooks", {})
sessionstart = hooks.setdefault("SessionStart", [])

already_present = any(
    h.get("command") == HOOK_CMD
    for entry in sessionstart
    for h in entry.get("hooks", [])
)

if not already_present:
    sessionstart.append({
        "hooks": [{"type": "command", "command": HOOK_CMD, "timeout": 5}]
    })
    SETTINGS.write_text(json.dumps(data, indent=2) + "\n")
