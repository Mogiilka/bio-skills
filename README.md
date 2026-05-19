# bio-skills

9 skills to draft your sales materials before BIO, then sharpen them
with what you hear there. Built for scientist-founders. Free.

## What's inside

| Skill | What it does |
|---|---|
| `/foundation` | Captures product, buyers, evidence. Reusable across campaigns. |
| `/campaign` | Sets up materials for a specific event. |
| `/positioning-tagline` | Extracts your tagline from real buyer language. |
| `/narrative` | 30-sec, 2-min, 5-min versions of your pitch. |
| `/objection-playbook` | Predicts likely objections. |
| `/one-pager` | Printable leave-behind for one buyer profile. |
| `/sales-deck` | 15-20 slide outline for booth, investor, or customer call. |
| `/validation-prep` | Question sheet for buyer conversations. Built on Mom Test. |
| `/validation-debrief` | After the conference: extract quotes, detect patterns. |

All skills share a single `CONVENTIONS.md` that translates internal terms
to plain language before any output reaches a buyer.

---

## Quick reference

Two ways to install, depending on your tool:

- **Claude Code** (CLI, or the Code tab in Claude Desktop, or the VS Code /
  JetBrains plugin): clone this repo, run one script. Skills become real
  slash commands. Steps below.
- **Chat interface** (Claude.ai web, ChatGPT, Claude Desktop main chat):
  use Projects. No install. See further down in this README, or the
  [visual guide on our landing page](https://landing-page-peach-mu-27.vercel.app/).

---

## Install — Claude Code (GitHub)

Skills become native slash commands: `/foundation`, `/campaign`, and so on.
The install script symlinks each skill into `~/.claude/skills/` and registers
a once-per-day update check that flags new releases inside Claude Code.

### Prerequisites

- [**Claude Code**](https://claude.com/product/claude-code) installed and
  opened at least once (so `~/.claude/` exists)
- **Git**
- **macOS or Linux.** Windows: use WSL, or use the ChatGPT Projects path
  below — `./install` relies on Unix symlinks.

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
   GitHub once per day for a new version (silent unless there's news)

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

## Install — Chat interface (Projects)

For Claude Desktop's Chat tab, Claude.ai web, ChatGPT, or any chat-based
AI tool. No install required.

1. Download the zip:
   [bio-skills.zip](https://github.com/norml-studio/bio-skills/archive/refs/heads/main.zip)
2. Unzip it
3. Open Claude.ai or chatgpt.com → create a new Project
4. Upload the `.claude/skills/` folder from inside the unzip to the
   Project
5. In a new conversation, type:

   > Follow the instructions in `foundation/SKILL.md` to start.

Run the skills in sequence within the same conversation. Each skill
references the output of the previous one. If you start a new
conversation, upload your latest output files (like `foundation.md`)
to the Project first so the next skill can read them.

**Prerequisite:** ChatGPT Plus, or any Claude.ai account (Projects is free).

---

## How to use

1. `/foundation` first. Capture product, buyer profile, evidence.
2. `/campaign` next. Name your event.
3. Run any of these for your campaign: `/positioning-tagline`,
   `/narrative`, `/objection-playbook`, `/one-pager`, `/sales-deck`.
4. `/validation-prep` before the conference.
5. `/validation-debrief` after. Sharpens materials with what you heard.

In the chat-interface path, refer to skills by file name instead of
slash commands: "follow `foundation/SKILL.md`."

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
