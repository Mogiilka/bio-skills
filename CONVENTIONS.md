# Skill Conventions

Applies to all skills. Read at the start of every run, alongside upstream artifacts.

## Self-review at output time

Before emitting any draft (artifact, pitch script, one-pager, narrative, etc.):

1. Read your draft as a skeptical reader.
2. Ask: is each fact earning its place? Is it explaining, or proving credentials?
3. Check against `voice-rules.md` (if it exists in the project directory).
4. Run the glossary translation pass (see below).
5. Revise silently. Don't ask the user to confirm fixes.

## Glossary translation

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
