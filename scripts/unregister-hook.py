#!/usr/bin/env python3
"""Remove the bio-skills SessionStart hook from ~/.claude/settings.json.

Leaves other hooks and settings untouched. Cleans up empty containers so
settings.json doesn't accumulate dangling keys.
"""
import json
import pathlib

HOME = pathlib.Path.home()
SETTINGS = HOME / ".claude" / "settings.json"
HOOK_CMD = "bash ~/.claude/skills/bio-skills/scripts/check-update.sh 2>/dev/null || true"

if not SETTINGS.exists():
    raise SystemExit(0)

data = json.loads(SETTINGS.read_text())
hooks = data.get("hooks", {})
sessionstart = hooks.get("SessionStart", [])

cleaned = []
for entry in sessionstart:
    remaining = [h for h in entry.get("hooks", []) if h.get("command") != HOOK_CMD]
    if remaining:
        entry["hooks"] = remaining
        cleaned.append(entry)

if cleaned:
    hooks["SessionStart"] = cleaned
elif "SessionStart" in hooks:
    del hooks["SessionStart"]

if not hooks:
    data.pop("hooks", None)

SETTINGS.write_text(json.dumps(data, indent=2) + "\n")
