# Changelog

All notable changes to bio-skills will be documented in this file.

## [0.2.0] — 2026-05-20

### Changed
- Renamed `/sales-deck` → `/deck`. Folder, slash command, output filename
  pattern (`sales-deck-{...}.md` → `deck-{...}.md`), and cross-references in
  other skills updated.

### Migration
- After `git pull`, re-run `./install`. The installer now cleans up the
  stale `~/.claude/skills/sales-deck` symlink automatically.
- Existing output files named `sales-deck-{...}.md` keep working — they're
  just markdown. New runs save as `deck-{...}.md`.

## [0.1.0] — 2026-05-19

### Added
- Initial release: 9 skills for drafting and validating biotech sales materials before BIO 2026
- `/foundation`, `/campaign`, `/positioning-tagline`, `/narrative`,
  `/objection-playbook`, `/one-pager`, `/sales-deck`, `/validation-prep`,
  `/validation-debrief`
- `/update-bio-skills` auto-updater + SessionStart hook that flags new releases
- `CONVENTIONS.md` shared rules for plain-language output
- `install` / `uninstall` scripts (POSIX sh, macOS/Linux)
- Install paths for Claude Code (GitHub clone) and ChatGPT Projects (file upload)
