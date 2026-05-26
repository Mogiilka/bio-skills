# Changelog

All notable changes to bio-skills will be documented in this file.

## [0.3.0] — 2026-05-26

### Added
- `CONVENTIONS.md` gains three new sections: **banned words** list (`actual`, `actually`, `real`, `really`, `artifact`, `translate`/`translation` verb, "not X, it's Y" constructions), **voice principles** (use "target profile" not "ICP", no advisor name attribution, no time estimates, no letter-number abbreviations, lead with problem not rules), and **standard opening pattern** (what produces / how it goes / what you end with, then first question).
- Wired `CONVENTIONS.md` into all 9 founder-facing `SKILL.md` files. Each now reads it before any operator-facing output. Previously the file claimed "applies to all skills" but no skill referenced it.

### Changed
- **`/validation-prep` major refactor** (skill version 0.2 → 0.3). New opening frame. Question bank now wired to foundation's 5 testable claims (category, problem, target, differentiation, mechanism) with question-shape-vs-failure-mode mapping made visible. Smoother conversational wording. Transitions baked into the prep sheet output. Q-recommend Part 1 ("how would you describe us to a colleague") explicitly labeled as the message test. Reading-the-answer bullets per question. New Step 4 (Capture mode) covering scheduled-meeting recording opener and booth voice-memo fallback. Founder's existing capture tools captured upfront. Output structure: page 1 pocket card with opener + transitions, page 2 questions with claim labels visible, pages 3+ capture rows with new slots (`capture_mode`, `recording_y_n`, vocabulary echo per row). Removed: the original Q1 "what did you think we were", Q-buying-group, and "what would have to be true" questions, replaced by Q-recommend's two-beat structure that surfaces target signals more naturally.
- **README.md sync** to match the live landing page. Dropped Mom Test reference from `/validation-prep` description, fixed `/deck` "every buyer profile and one setting" wording, ported the "fluff detector / pushes back on weak claims" framing into `/foundation` description, rewrote "translates internal terms" without the verb, swapped "real engagements" for "paid engagements" in the Built By block.
- **`CONVENTIONS.md` section rename:** "Glossary translation" → "Glossary swap" (with matching update in `update-bio-skills`) to remove the `translate` verb root everywhere.
- **AI-tell scrub across all 9 skills.** Removed instances of `actually`, `real`, `really`, and `artifact` from user-facing prompts and example dialogue where the words added emphasis without information. Foundation and narrative were heaviest. Schema labels (e.g., `real-evidence` in narrative, YAML `artifact:` references) and intentional bad-example founder dialogue preserved as illustrative.

### Fixed
- `validation-prep/SKILL.md` Pattern 1 example phrasing: "translation work" → "analysis layer" (translate is on the biotech no-go list).
- `objection-playbook/SKILL.md` reframe guidance: "outcome-translation" → "plain-language outcome statement".

### Migration
- After `git pull`, restart Claude Code (or start a new chat) to pick up the refreshed `SKILL.md` content.
- No data migration needed. Existing `foundation.md`, `positioning-tagline.md`, and other operator-facing files keep working.
- Running `/validation-prep` after this update produces a sheet with the new structure (claim labels visible, capture-mode step, expanded row slots). In-flight prep sheets from prior runs remain valid for any campaign already underway.

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
