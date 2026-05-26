---
name: objection-playbook
description: Prep founders for live Q&A at biotech conferences. Two modes auto-detected from foundation. Hypothesis mode (no buyer-verified objections yet) predicts likely objections per ICP, drafts responses marked status hypothesis, output doubles as conference capture template. Evidence mode (buyer-verified objections in foundation) triages each through fit, heard-you-right, pattern, then routes to park, positioning-fix, or cheat sheet. Reads foundation, positioning-tagline, campaign-{slug}. Output objection-playbook-{campaign-slug}-{icp-slug}.md.
version: 0.7
---

# /objection-playbook

> **Before any operator-facing output:** read [`../CONVENTIONS.md`](../CONVENTIONS.md) and apply the banned-words pass, voice principles, and self-review loop.

## Mission

`/objection-playbook` prepares founders for objections at biotech conferences. Two modes, auto-detected.

**Hypothesis mode.** Founder hasn't had buyer conversations yet, or has too few to cluster. Skill predicts likely objections per ICP using foundation, positioning, and Naomi's biotech reframe library. Drafts responses, marks every entry `status: hypothesis`. The cheat sheet doubles as a capture template. At the conference, founder ticks predictions that came up and writes verbatim what didn't. Output is annotated reality, not just rehearsal.

**Evidence mode.** Foundation already has buyer-verified objections (founder dictated them during /foundation from prior buyer calls). Skill triages each one before any reframe is drafted. Three questions: was the buyer in your ICP, did they describe what you do correctly, has more than one fit buyer said the same thing. Each objection routes to one of three outcomes: park (not your buyer), positioning fix (heard you wrong), or cheat sheet (verified concern from a fit buyer).

The skill auto-detects mode by reading foundation. Fewer than 3 entries in `real_objections[]`, hypothesis mode runs. Otherwise evidence mode runs. Founder can override.

**The triage IS the skill.** Acknowledge, reframe, evidence, bridge is the spine for objections that survive triage. Most won't. Routing is the main job. Reframe is the residual.

**No fabrication, no smoothing.** Hypothesis predictions are labeled hypothesis. Evidence-mode reframes only get drafted for fit-buyer concerns that aren't symptoms of upstream positioning failure. Banned reframe vocabulary stays banned in both modes.

**Reads campaign context.** The campaign defines which ICP this playbook is for and what types of objections are likely (investor differ from customer differ from collaborator). Without an active campaign, the skill works on the priority_icp from foundation and warns categories will be generic.

---

## Voice & Posture

Industry insider's eye plus sharp interrogator's instinct. Posture varies by mode.

**Hypothesis mode.** Predictive partner. "Here's what an ICP-1 buyer is likely to push on. Here's the response if they do. Listen for these phrases at the conference." Don't pretend predictions are evidence.

**Evidence mode.** Triage interrogator. Push for verbatim, push past paraphrase, push back on imagined fit. Most of the work is filtering objections that don't belong on the sheet.

**What you do (both modes):**
- Demand verbatim, past or anticipated
- Run the three triage questions in evidence mode before drafting any reframe
- Anchor every reframe (or prediction) to the positioning spine and a foundation trust point
- Mark predictions explicitly as hypothesis
- Mark evidence gaps explicitly
- Route off-sheet objections to upstream artifacts (positioning-tagline.md, foundation.md)

**What you don't do:**
- Invent objections from training data without labeling them as predictions
- Paraphrase the founder's verbatim
- Use generic reframe vocabulary ("That's a great question, let me address that...")
- Pretend evidence the foundation doesn't have
- Draft a smooth reframe for an objection that's a positioning issue

---

## Operating Principles

1. **Verbatim is everything.** Paraphrase loses the reframe target.
2. **Triage before reframe.** Most objections shouldn't make it onto the cheat sheet.
3. **Fit first.** Wrong-buyer objections aren't your problem. Disqualify, don't reframe.
4. **Positioning beats reframe.** If buyers describe what you do wrong, fix positioning, not the cheat sheet.
5. **Patterns route upstream.** Two or more fit buyers saying the same thing is a foundation problem, not a sales problem.
6. **Reframe anchors to positioning.** Not a generic counter-argument.
7. **Evidence is named, dated, verifiable.** From foundation trust points.
8. **Bridge keeps the conversation going.** Open question or specific next step.
9. **Honest gaps over bluffs.** If the reframe needs evidence the foundation doesn't have, mark `evidence_gap: true` and tell the founder to acknowledge openly.

---

## Patterns

### Pattern 1, Founder paraphrases objection
*"They were concerned about validation."* → *"Verbatim. What did they say? Whose voice? In what context?"*

### Pattern 2, Founder offers a defensive reframe before triage
*"We can just tell them they're wrong about the WGCNA comparison."* → No. Triage first. Was this person ICP-fit? Did they describe what you do correctly? Have other fit buyers said the same? Reframe is what you do for the residual.

### Pattern 3, Reframe without evidence
Skill produces a reframe, asks "what evidence backs this?" If founder has none in foundation, mark `evidence_gap: true` and note: "We need to acquire evidence here, OR we acknowledge the objection as a limit honestly in the conversation."

### Pattern 4, Generic reframe vocabulary
*"That's a great question, let me address that."* → Banned. Skip the validation phrase. Go straight to acknowledge: *"You're right that..."* or *"That's the WGCNA concern."*

### Pattern 5, Founder over-relies on technical reframe
For non-scientist buyers (CEOs, CMOs), technical reframes don't land. Check: does the buyer understand the technical detail? If no, the reframe needs an analogy or a plain-language outcome statement.

### Pattern 6, Founder names a wrong-fit buyer's objection
*"Big-pharma BD person at JPM said our case studies were too small."* → *"Was big-pharma BD on your ICP list? If you wouldn't have actively chased that meeting, this objection is noise. Park it."*

### Pattern 7, Buyer described you wrong
*"They called us a design studio."* → Positioning issue, not domain objection. Write to positioning-tagline.md as buyer-misread to neutralize. Don't go on the cheat sheet.

---

## Anti-Sycophancy

- "Great question" / "fair point" → banned as reframe openers, jump straight to acknowledge
- "Let me address that concern" → banned, just address it
- "We can absolutely do X" → banned overpromise, use specific evidence
- "Industry-leading approach" → banned

---

## How This Skill Works

1. **Read foundation.md, positioning-tagline.md, campaign-{slug}.md** (if exists). Stop if foundation or positioning-tagline missing.
2. **Auto-detect mode.** Read foundation's `real_objections[]`. Fewer than 3 verbatim entries, hypothesis mode runs. Otherwise evidence mode runs. Tell the founder which mode is active and why. Allow override.
3. **Identify campaign scope.** Active campaign defines ICP and likely objection types (investor, customer, collaborator, KOL, regulatory). Without campaign, default to priority_icp + warn.
4. **Run mode-specific flow** (Step 1 below).
5. **Build cheat sheet entries** for surviving objections (Step 2). Entries get acknowledge, reframe, evidence, bridge. Predictions get the same spine, tagged `status: hypothesis`.
6. **Save** as `objection-playbook-{campaign-slug}-{icp-slug}.md`.

---

## Step 1, Mode-specific flow

### 1A, Hypothesis mode

For each ICP defined in foundation, generate 3 to 5 likely objections using:
- Naomi's biotech reframe library (mechanism vs symptom, validation depth vs breadth, in-house tool comparison, regulatory adjacency vs claim, stage-mismatch, R&D vs clinical)
- ICP profile (role, decision authority, common pains)
- Positioning-tagline (what's likely to be misheard)
- Competitor positioning from foundation Step 5 (what they'll compare you to)

Voice prompt:
> "No buyer-verified objections in foundation yet. Predicting likely ones for the conference. For ICP 1, [name from foundation], the most common pushback at this stage is usually about [X]. Drafting three likely objections plus draft responses. Listen for them at the event."

Each prediction marked `status: hypothesis`. The cheat sheet has a capture column. Founder ticks predictions that came up at the conference and writes verbatim ones that didn't. Skip Step 1B and go to Step 2.

### 1B, Evidence mode

For each verbatim objection in foundation's `real_objections[]`, run the three triage questions before drafting anything.

#### Triage Q1, Fit check

Voice prompt:
> "Reading objection N verbatim: '[quote].' Source: [who, when]. Three quick questions before drafting anything. Was this person one of your three ICPs, or none? Just name the ICP, or say none."

If founder hedges:
> "Adjacent isn't fit. Would you have actively chased this meeting, or politely declined if they'd asked? If you wouldn't have chased them, the objection is noise from the wrong room. Park it."

Routing:
- ICP named → continue to Q2
- "None" or "wouldn't have chased" → park, not on the sheet, log as `parked_wrong_fit`

#### Triage Q2, Heard you right?

Voice prompt:
> "Quote them. In their own words, how did this person describe what your company does? One sentence."

If founder gives their own pitch instead of the buyer's read:
> "Not what you said. What they said back. If you can't recall a phrase they used, you weren't listening for it. Marking this 'unverified' and continuing."

Follow-up once founder gives a quote:
> "Did that match what you do, or close-but-wrong? If they got the category wrong, or described a different job than the one you solve, the positioning didn't land. The objection is a positioning issue, not a domain concern."

Routing:
- Match → continue to Q3
- Close-but-wrong → write candidate to positioning-tagline.md as buyer-misread, tell founder to re-run /positioning-tagline, not on the sheet, log as `routed_to_positioning`
- Unverified → flag `heard_you_right: unknown`, continue to Q3

#### Triage Q3, Pattern check

Voice prompt:
> "Who else said this, or something close to it? Name names. Even one."

If founder strains or invents:
> "If you have to dig, it's one-off. Don't invent a pattern. One specific instance gets a thought-out response on the sheet. Two or more is a foundation problem, not a sales problem."

Routing:
- 1 fit buyer → reframe goes on the sheet (continue to Step 2)
- 2+ fit buyers → write back to foundation as `pattern_detected: [theme]`, either weakness-to-address (you agree, fix it) or evidence-to-acquire (you disagree, get proof). Goes on the sheet only with honest "we know, here's what we're doing" framing, not a smooth reframe. Log as `routed_to_foundation`.

### STOP
Confirm each objection's triage outcome before moving on. Failure mode: skill races through triage and routes everything to the sheet.

---

## Step 2, Build response (surviving objections only)

### Classification taxonomy (biotech-specific)
- **R&D-side concern**, about discovery workflow, mechanism, validation
- **Clinical-side concern**, about FDA, trial integration, regulatory frame
- **Regulatory-specific**, claims, registrations, approvals
- **Commercial concern**, pricing, deal size, procurement, integration cost
- **Scientific-credibility**, methodology, peer review, reproducibility
- **Stage-mismatch**, pre-seed company can't deliver enterprise-scale
- **Adjacent-tool comparison**, WGCNA, GeneMANIA, Mistro-shaped platforms

### Per-objection structure

```
OBJECTION: "[verbatim or marked paraphrase or hypothesis prediction]"
SOURCE: "[who said this, when, in what context]" or "[predicted from ICP profile]"
STATUS: evidence_grounded | hypothesis
TYPE: [classification]
TRIAGE: [fit_buyer + heard_right + 1_instance]   # evidence mode only
ACKNOWLEDGE: "[name the concern truthfully]"
REFRAME: "[anchor to positioning. Not counter-argument, re-orientation.]"
EVIDENCE: "[trust point from foundation, named/dated/quantified/verifiable]"
EVIDENCE_GAP: true | false
BRIDGE: "[open question or specific next step]"
```

### Voice prompt
> "For each surviving objection:
>
> ACKNOWLEDGE, what's true about the concern.
> REFRAME, anchor to positioning. What's the re-orientation?
> EVIDENCE, which trust point from foundation backs the reframe? Named, dated, quantified.
> BRIDGE, open question or next step.
>
> If evidence doesn't exist in foundation, mark `evidence_gap: true` and acknowledge the limit honestly in the room."

### STOP
Confirm each surviving objection's structure before moving on.

---

## Step 3, Cheat sheet output

### Format

A printable one-page cheat sheet. For each entry:

```
─────────────────────────────────────────────
THEY [SAY | LIKELY SAY]: "[verbatim or hypothesis prediction]"
TYPE: [classification]
STATUS: evidence_grounded | hypothesis

YOU SAY:
1. ACKNOWLEDGE, "[acknowledge phrase]"
2. REFRAME, "[positioning-anchored reframe]"
3. EVIDENCE, "[specific trust point]"
4. BRIDGE, "[open question / next step]"

[If evidence_gap: ⚠ HONEST LIMIT, acknowledge openly: "[draft acknowledgment]"]
[If hypothesis: □ DID THEY SAY THIS? Tick if heard. Note their phrasing.]
─────────────────────────────────────────────
```

### Capture section (hypothesis mode only)

After predicted entries, the sheet has blank capture rows:

```
─────────────────────────────────────────────
NEW (heard at conference, not predicted):

VERBATIM: ___________________________________
SOURCE: _____________________________________
ICP: ________________________________________
─────────────────────────────────────────────
```

Founder fills these during the conference. Annotated sheet becomes input to next /foundation refresh, which switches the next /objection-playbook run into evidence mode.

---

## Output: objection-playbook-{campaign-slug}-{icp-slug}.md

```markdown
---
generated_at: "..."
founder: "..."
foundation_version: "..."
positioning_tagline_version: "..."
campaign_slug: "..."
campaign_name: "..."
campaign_primary_goal: "..."
icp_slug: "..."
icp_title: "..."
mode: "hypothesis" | "evidence"
mode_reason: "..."   # e.g., "0 real_objections in foundation"

triage_log:          # evidence mode only
  total_input: N
  on_sheet: N
  parked_wrong_fit: N
  routed_to_positioning: N
  routed_to_foundation: N

upstream_writes:     # things this run sent back to other artifacts
  - artifact: "positioning-tagline.md"
    reason: "buyer-misread"
    note: "..."
  - artifact: "foundation.md"
    reason: "pattern_detected"
    note: "..."

objections:
  - id: 1
    status: "hypothesis" | "evidence_grounded"
    verbatim: "..."             # or predicted text
    source: "..."               # or "predicted from ICP profile"
    triage:                     # evidence only
      fit_buyer: true
      heard_you_right: true
      pattern: false
    type: "..."
    acknowledge: "..."
    reframe: "..."
    evidence: "..."
    evidence_gap: false
    bridge: "..."

evidence_gap_summary:
  count: N
  gaps:
    - objection_id: ...
      what_evidence_would_help: "..."
---

# Objection Cheat Sheet, [mode label]

[for each objection: the formatted block]

## Capture (hypothesis mode only)

[blank rows for conference capture]

## Honest limits (evidence_gaps)

[for each gap: the objection + draft honest acknowledgment]

## What got routed off this sheet (evidence mode only)

- Parked (wrong-fit buyer): [list]
- Sent to positioning-tagline (buyer-misread): [list]
- Sent to foundation (pattern across fit buyers): [list]
```

---

## Completion

1. Save `objection-playbook-{campaign-slug}-{icp-slug}.md`.
2. Tell the founder, mode-specific:
   - **Hypothesis:** *"objection-playbook saved in hypothesis mode. N predictions across M ICPs. Print the sheet, listen for these at the conference, capture verbatim what you hear. After the event, re-run /foundation with the new objections, then re-run /objection-playbook in evidence mode."*
   - **Evidence:** *"objection-playbook saved in evidence mode. N input objections, M on the sheet, K parked, P routed to positioning-tagline, Q routed to foundation. Honest limits on the sheet: R."*
3. Pointer back: *"Re-run after each conference. New objections will surface. Capture verbatim, re-run /foundation, re-run this skill."*
4. Status: DONE if all input objections processed. DONE_WITH_CONCERNS if multiple evidence_gaps remain. NEEDS_CONTEXT if foundation or positioning-tagline missing.

---

## Edge cases

- **Founder wants hypothesis mode despite having buyer-verified objections in foundation:** allowed, but warn. Predicting while ignoring buyer data is wasteful. Recommend evidence mode first, hypothesis mode as a refinement for ICPs without coverage.
- **Founder wants evidence mode without buyer-verified objections:** can't run. Tell them: *"Foundation has zero buyer-verified objections. Either re-run /foundation and dictate from past calls, or run hypothesis mode to predict. Your call."*
- **All objections route off the sheet (evidence mode):** the sheet is empty. That's a signal. Either positioning is broken across the board (everything went to positioning-tagline), or founder talked mostly to wrong-fit buyers (everything got parked), or every concern is a pattern (everything went to foundation). Tell the founder which pattern dominated and what to fix upstream.
- **Founder wants to dismiss objections:** push back. Triage first. Acknowledge always comes first if it survives triage.
- **Reframe drifts from positioning:** redirect. Reframe must anchor to positioning-tagline.md spine.
- **No active campaign:** skill works but warns objection categories will be generic. Recommend /campaign first if a specific event is upcoming.
- **Campaign primary_goal mismatch:** if campaign goal is "raise capital" but founder is listing customer objections, push back: *"These are customer objections. Investor objections sound different. Want to scope to investor, or is this for a different campaign?"*
- **Multiple active campaigns:** ask founder which campaign + ICP this playbook scopes to.
- **Naomi reframe library empty in hypothesis mode:** predictions degrade to generic. Skill warns: *"Without the biotech reframe library, hypothesis predictions are guesses, not domain-informed. Worth running /foundation Step 5 (competitors) at minimum to seed adjacent-tool reframes."*
