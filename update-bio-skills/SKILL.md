---
name: update-bio-skills
description: Update the bio-skills bundle to the latest GitHub release. Pulls changes, summarizes the CHANGELOG diff in plain language, tells the founder to restart Claude Code if new skills landed. Plumbing skill — not part of the methodology workflow.
version: 0.1.0
---

# /update-bio-skills

## Mission

Pull the latest bio-skills from GitHub without making the founder leave Claude Code. Surface what changed in plain language. Tell them when a restart is needed.

This skill is infrastructure. It does not produce founder-facing artifacts. It does not write to `foundation.md` or any other artifact file. If the founder runs `/update-bio-skills` expecting methodology output, redirect them to `/foundation` or whichever skill they meant.

---

## Voice & Posture

Short, factual, no marketing. The founder ran a maintenance command. Tell them what happened, what changed, what to do next. No praise, no filler.

---

## How this skill works

Bundle directory: `~/.claude/skills/bio-skills`

1. Capture the local version from `~/.claude/skills/bio-skills/VERSION`.
2. Run `cd ~/.claude/skills/bio-skills && git pull --ff-only` via Bash.
3. Capture the new version from the same VERSION file (may be unchanged).
4. If the pull reported "Already up to date" — tell the founder: *"Already on the latest version (v[X]). No changes."* Stop.
5. If the pull reported merge conflicts or any non-fast-forward error — surface the error verbatim, suggest the founder run `cd ~/.claude/skills/bio-skills && git status` and resolve manually. Do not attempt destructive recovery.
6. If the pull succeeded with new commits:
   a. Read `~/.claude/skills/bio-skills/CHANGELOG.md`.
   b. Extract the entries between the old version and the new version.
   c. Summarize each entry in one plain-language sentence per bullet — no jargon, no internal skill terms (apply `CONVENTIONS.md` glossary translation if it exists).
   d. Tell the founder: *"Updated bio-skills from v[OLD] to v[NEW]. Changes: [bullets]. Restart Claude Code (or start a new chat) to load the updates."*

---

## Output shape

**Up to date:**
> Already on the latest version (v0.1.0).

**Updated successfully:**
> Updated bio-skills from v0.1.0 to v0.2.0.
>
> Changes:
> - [plain-language summary of CHANGELOG bullet 1]
> - [plain-language summary of CHANGELOG bullet 2]
>
> Restart Claude Code (or start a new chat) so the updates load.

**Pull failed:**
> Update failed: [verbatim error].
>
> Run `cd ~/.claude/skills/bio-skills && git status` to see what's wrong. Common causes: local edits in the bundle dir, no network, conflicting changes upstream.

---

## Edge cases

- **Local edits in the bundle dir:** git pull --ff-only refuses. Surface the refusal verbatim. Don't offer to stash or discard — the founder may have intentionally edited a skill.
- **No network:** git pull errors out. Report the network failure honestly. Don't pretend the update worked.
- **Bundle dir missing:** the install is broken. Tell the founder to re-run the install line from the README.
- **CHANGELOG.md missing:** report the version change without bullets. *"Updated to v[NEW]. CHANGELOG missing — check the repo on GitHub for details."*
- **Founder asks the skill to also update something else (CLAUDE.md, settings):** out of scope. Decline politely.
