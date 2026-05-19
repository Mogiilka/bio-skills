#!/bin/sh
# SessionStart hook — fetches remote VERSION at most once per 24h.
# Prints a one-line banner if local and remote disagree. Silent otherwise.
# Stdout from a SessionStart hook is injected as session context, which is
# how Claude Code surfaces the banner to the founder.

BUNDLE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
VERSION_FILE="$BUNDLE_DIR/VERSION"
STAMP_FILE="$BUNDLE_DIR/.last-checked"
REMOTE_URL="https://raw.githubusercontent.com/Mogiilka/bio-skills/main/VERSION"

[ -f "$VERSION_FILE" ] || exit 0

if [ -f "$STAMP_FILE" ]; then
  last=$(cat "$STAMP_FILE" 2>/dev/null || echo 0)
  now=$(date +%s)
  if [ $((now - last)) -lt 86400 ]; then
    exit 0
  fi
fi

remote=$(curl -fsSL --max-time 3 "$REMOTE_URL" 2>/dev/null | tr -d '[:space:]')
[ -n "$remote" ] || exit 0

local_version=$(tr -d '[:space:]' < "$VERSION_FILE")

date +%s > "$STAMP_FILE" 2>/dev/null || true

if [ "$remote" != "$local_version" ]; then
  echo "bio-skills update check: local v$local_version, latest v$remote. Type /update-bio-skills to sync."
fi
