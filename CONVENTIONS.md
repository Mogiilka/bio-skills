# Skill Conventions

Applies to all skills. Read at the start of every run, alongside upstream artifacts.

## Self-review at output time

Before emitting any draft (artifact, pitch script, one-pager, narrative, etc.):

1. Read your draft as a skeptical reader.
2. Ask: is each fact earning its place? Is it explaining, or proving credentials?
3. Check against `voice-rules.md` (if it exists in the project directory).
4. Run the glossary swap (see below).
5. Revise silently. Don't ask the user to confirm fixes.

## Glossary swap

When emitting operator-facing or buyer-facing prose, swap internal skill terms for plain language. Internal terms can stay in YAML, schema fields, and skill notes; they should not appear in pitch scripts, one-pagers, websites, emails, or any text the operator might paste to a buyer.

| Internal term | Plain-language swap |
|---|---|
| onliness / onliness statement | what makes us different / what we're the only ones doing |
| Master Messaging spreadsheet / MMS | messaging system you keep / messaging reference |
| ICP / ICP atlas | buyer profile / target customer / who this is for |
| differentiation playbook | how we stand apart / where we sit vs others |
| validation-prep | call prep |
| validation-debrief | call notes review |
| named_buyer_gap | no real buyer named yet |
| onliness_weakness_held | we're not yet uniquely positioned |
| single_case_warning | only one case shipped so far |

**Apply at output time, not at storage time.** The flag/term stays in YAML for downstream skills to read. The prose-facing swap happens in the self-review pass before emit.

If an operator-facing sentence still feels slop-y after swap, find a synonym that fits the context. Don't ship the internal term.

## Banned words

These words and constructions are AI tells. They contaminate operator-facing prompts and outputs. Strip them on every emit.

- **actual / actually** — adds emphasis without adding information. The sentence is usually stronger without it.
- **real / really** — same pattern.
- **artifact** — wrong noun for what these skills produce. Use "piece of collateral," "concrete message," or the specific artifact name (one-pager, deck, prep sheet, etc.).
- **translate / translation (verb form)** — burned word in biotech. Use "rewrite in plain language," "convert," "describe," or the specific action.
- **"not X, it's Y" constructions** — over-corrects via contrast and reads as a trained rhetorical move. Say the positive thing directly.

Apply at output time, alongside the glossary swap. Internal skill notes and YAML keys can keep these words if needed. Operator-facing text cannot.

## Voice principles

These apply to every skill's operator-facing output.

- **Use "target profile" not "ICP"** (or "buyer profile," or "who you're trying to reach"). Schema keys can stay coded (`icp_id`, `target_profile_id`); operator-facing labels cannot.
- **No advisor name attribution.** Don't say "our advisor said X" or quote a named person. State principles directly, without source. The skills ship to all founders; named advisors don't belong in the dialogue.
- **No time estimates.** No "~20 min," "takes ~X min," or process-duration claims anywhere. Describe what the skill does, not how long it takes.
- **No letter-number abbreviations.** Don't refer to claims as "C1," "C2," or target profiles as "T1," "T2." Use plain words: "category," "problem," "target," "first target profile."
- **Lead with problem, not rules.** When introducing a new step (capture, recording, behavior change), name the founder's situation first ("you'll talk to a stack of people; by Friday you'll remember a few clearly and the rest as blur"), then offer the response. Parental safety reminders demote into trade-off footnotes, not opening lines.

## Standard opening pattern

Every skill opens with three things before its first question:

1. **What this produces.** One concrete sentence about the output.
2. **How it goes.** Brief sequence of what the skill will do.
3. **What you end with.** One concrete sentence about the artifact the founder walks away with.

Then the first question. Don't dive in cold.

Example:

```
**What this produces.** One prep sheet for every conversation in your BIO 2026 block.

**How it goes.** Lock priority target profile, set countable goal and disqualify signal, generate questions wired to your foundation, set up capture.

**What you end with.** One printable file.

Which is the priority for BIO 2026?
```

## Silent voice-rules capture

Maintain `voice-rules.md` in the project directory.

**Trigger:** the moment the user corrects something you produced.

Corrections look like:
- "this sounds cheap"
- "cut this"
- "no, rewrite without X"
- specific complaint after seeing output

NOT corrections:
- Iteration ("make it shorter," "add more X")
- Acceptance ("ok," "looks fine")
- Questions about the draft

**On trigger, capture:**
- The original content you produced
- The user's reaction, verbatim
- Severity inferred from their language

**Severity tiers:**
- Critical: strong reaction, whole section cut, "never do this" → applies immediately as a rule
- Medium: moderate cut, neutral language → applies after 2+ observations on same pattern
- Low: small edit, polish → applies after 3+ clustering observations

Promotion is automatic. No questions to the user.

**voice-rules.md format:**

```yaml
- pattern: short description of what to avoid or do
  context: spoken pitch | written intro | one-pager | etc.
  severity: critical | medium | low
  example: "original phrase" cut on YYYY-MM-DD ("user reaction")
```

## Cap and pruning

~15-20 rules max. If more accumulate, propose consolidation. Auto-prune rules that haven't triggered in 5 sessions.

## Workflow integration

Each skill run:

1. Read upstream artifacts + `voice-rules.md`
2. Gather context (questions, evidence, materials)
3. Generate draft internally
4. Self-review and revise silently
5. Emit final version
6. If user corrects: log observation silently, promote to rule per severity
7. Write artifact

User never sees voice-rules unless they open the file themselves.
