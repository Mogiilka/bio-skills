# bio-skills

9 skills to draft your sales materials before BIO, then sharpen them
with what you hear there. Plus an auto-updater that flags new versions.
Built for scientist-founders. Free.

## What's inside

| Skill | What it does |
|---|---|
| `/foundation` | Captures your product, buyers, what makes you different, your evidence. Shapes it into a structured file that every other skill reads from. Reusable across campaigns. |
| `/campaign` | Sets up for a specific event like BIO, JPM, or investor week. Pulls in what's happening there and adapts your intro and pitch deck for that context. |
| `/positioning-tagline` | Extracts your tagline from real buyer language. Marks it as a guess if you haven't had buyer conversations yet. Updates as you collect more language. |
| `/narrative` | Three versions of your pitch for every buyer profile: thirty seconds, two minutes, and five minutes. For different occasions and levels of attention. |
| `/objection-playbook` | Predicts the objections you're most likely to hear from this buyer. Drafts a response for each one so you're not caught off guard at the booth. |
| `/one-pager` | A printable, one-page handout for every buyer profile. Hand it out at the booth or give it to the person who wants to think about it later. |
| `/deck` | A 15 to 20 slide outline for every buyer profile and one setting: booth, investor meeting, or customer call. Raw copy to paste into any deck tool. |
| `/validation-prep` | A question sheet for buyer conversations. Built on the Mom Test to get past polite feedback. Points your attention to the signals worth following up on. |
| `/validation-debrief` | After the conference, pulls exact buyer quotes and finds patterns across multiple conversations. Routes the findings back into your `/foundation` file for the next round. |

All skills share a single `CONVENTIONS.md` that translates internal terms
to plain language before any output reaches a buyer.

Not a terminal user? See the [visual guide on our landing page](https://bio.norml.studio/)
for the Claude Desktop and ChatGPT install paths.

---

## Install

Skills become native slash commands: `/foundation`, `/campaign`, and so on.
The install script symlinks each skill into `~/.claude/skills/` and registers
a per-session update check that flags new releases inside Claude Code.

### Prerequisites

- [**Claude Code**](https://claude.com/product/claude-code) installed and
  opened at least once (so `~/.claude/` exists)
- **Git**
- **macOS or Linux.** Windows: use WSL — `./install` relies on Unix
  symlinks.

### Install — one line

Paste this in your terminal:

```bash
git clone --depth 1 --single-branch https://github.com/Mogiilka/bio-skills.git ~/.claude/skills/bio-skills && cd ~/.claude/skills/bio-skills && ./install
```

What it does:

1. Clones the repo into `~/.claude/skills/bio-skills/`
2. Symlinks each of the 9 skills into `~/.claude/skills/` so Claude Code
   discovers them as slash commands
3. Registers a SessionStart hook in `~/.claude/settings.json` that checks
   GitHub once per session for a new version (silent unless there's news)

If a skill name in `~/.claude/skills/` already collides with an existing
skill on your machine, `./install` refuses to overwrite and tells you which
ones to move first.

Restart Claude Code (or start a new chat), then type `/foundation` to start.

### Updates

Bio-skills checks GitHub at most once per session. When a new version ships,
your next response in Claude Code starts with a line like:

> bio-skills update check: local v0.1.0, latest v0.2.0. Type
> /update-bio-skills to sync.

Type `/update-bio-skills` in any Claude Code chat. The skill pulls the
latest version, summarizes the changes in plain language, and tells you
whether a restart is needed.

To check manually:

```bash
cd ~/.claude/skills/bio-skills && git pull
```

### Uninstall

```bash
cd ~/.claude/skills/bio-skills && ./uninstall
```

Removes the 9 skill symlinks and the update-check hook. The bundle
directory itself is left in place — `rm -rf ~/.claude/skills/bio-skills`
if you want it fully gone.

### Other AI CLIs (Codex, Cursor, etc.)

The skills are written in Claude Code's SKILL.md format. The instructions
inside each SKILL.md are tool-agnostic — they describe what to do, not
which CLI to call — so a moderately capable AI in any environment can
follow them. Auto-discovery and the update notifier are Claude Code only;
other CLIs need their own discovery convention.

---

## How to use

1. `/foundation` first. Capture product, buyer profile, evidence.
2. `/campaign` next. Name your event.
3. Run any of these for your campaign: `/positioning-tagline`,
   `/narrative`, `/objection-playbook`, `/one-pager`, `/deck`.
4. `/validation-prep` before the conference.
5. `/validation-debrief` after. Sharpens materials with what you heard.

## A note on safety

Markdown files from the internet can carry hidden instructions for an AI.
Before installing any skill — ours or anyone else's — open the folder,
paste the SKILL.md files into a chat, and ask the AI to flag anything
suspicious. Trust but verify.

## Stuck?

Email mogiilka@norml.studio.

## Built by

[Norml Studio](https://norml.studio). A brand and messaging studio
working with scientist-founders and technical teams on positioning,
messaging systems, and websites. These skills are the methodology we
use on real engagements, packaged so you can run a draft pass yourself.

If you want the version that ships, talk to us: go@norml.studio

## License

MIT. See [LICENSE](LICENSE).

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
