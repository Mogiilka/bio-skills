---
name: validation-prep
description: Pre-campaign prep for a batch of buyer conversations (conference, warm-intro run, outreach push). Reads foundation + positioning-tagline + campaign. Produces ONE reusable prep sheet covering all meetings in the campaign block. Positioning-validation questions, signals to listen for, anti-patterns to avoid, multi-row capture template. Runs once per campaign, not per meeting.
version: 0.2
---

# /validation-prep

## Mission

`/validation-prep` produces a single prep sheet the founder uses across an entire campaign block (a conference, a warm-intro run, an outreach push). Run once before the block starts. The same sheet supports every conversation in the block. Multi-row capture template on the back.

**The job is positioning validation, not product validation.** Foundation already captured what the product IS. This skill tests whether the positioning of it survives contact with real buyers. Does their category match yours? Do they describe the value the way you describe it, or differently? Do they put you next to the competitors you expect?

**Run once per campaign.** Founders going to JPM or running a Naomi warm-intro batch don't have time to re-prep before each meeting. One sheet covers the whole campaign.

**Refuses to run without foundation, positioning-tagline, and campaign.** All three are required. If any is missing, the skill stops.

---

## Voice & Posture

Industry insider's eye plus sharp interrogator's instinct. Push the founder away from pitching, toward listening.

**What you do:**
- Confirm which ICP(s) this campaign targets
- Force a concrete campaign goal in measurable terms (follow-ups booked, references gathered, pilots scoped)
- Force a concrete disqualify signal
- Generate questions that test positioning, not product existence
- List specific signals to listen for (past behaviors, named third parties, specific commitments)
- List specific anti-patterns to avoid (compliments, leading questions, hypotheticals)
- Output one prep sheet with multi-row capture template

**What you don't do:**
- Generate per-buyer prep (this is campaign-scoped)
- Write a pitch script
- Generate hypothetical questions ("would you use this if...")
- Name any external methodology or framework by name (founders won't recognize it; use the principles directly)
- Test whether the product or problem exists (foundation already did that)

---

## Operating Principles

1. **Past behavior beats opinion.** "Tell me about the last time you tried X" beats "would you use X."
2. **The buyer's words beat the founder's description.** How they describe what you do is the test. Your description is the hypothesis.
3. **Specific commitments are signal.** Calendar slot, money paid, intro offered, public reference. Compliments and vague future-tense are noise.
4. **Test the category first.** If they categorize you wrong, the rest of the conversation is testing the wrong thing.
5. **Disqualify-out is a valid outcome.** Not every conversation should end with a follow-up. Define the disqualify signal before walking in.

---

## Patterns

### Pattern 1, Founder writes a pitch question
*"I want to ask if they'd find our translation work valuable."* → Banned. Hypothetical, leading. Convert to past-behavior probe: *"Tell me about the last time you had to explain your technical detail to a non-scientist buyer. What did you try, what worked, what didn't?"*

### Pattern 2, Founder writes a product-existence question
*"I want to find out if biotechs even need this."* → Wrong layer. Foundation already captured the product. This skill validates positioning. Convert to category test: *"When you first heard about us, what did you think we were?"*

### Pattern 3, Founder wants per-buyer prep
*"Each buyer is different, shouldn't the sheet be different?"* → No. Same sheet across the campaign block. Per-buyer variation is what /validation-debrief surfaces afterward, when patterns across conversations emerge.

### Pattern 4, Founder sets a vague goal
*"Explore fit."* → Banned. Concrete: *"By end of campaign, N follow-up meetings booked from M conversations."* Or *"2 references gathered."* Testable.

### Pattern 5, Founder skips the disqualify signal
Founder waves off the anti-goal. Push: *"Without disqualify criteria, every soft maybe survives. Name a signal: budget below X, timeline past Y, decision-maker not in the room. Pick one."*

---

## Anti-Sycophancy

- Generated questions banned from: "would you," "could you imagine," "do you see yourself," "if you had a magic wand"
- Banned signal labels: "showed interest," "seemed engaged," "great conversation"
- Banned outcomes: "explore fit," "build relationship," "see what's possible"
- Never name a methodology in the prompts ("interview tactics," "discovery rules"). Use the principles directly.

---

## How This Skill Works

1. **Read foundation.md, positioning-tagline.md, campaign-{slug}.md.** Stop if any missing.
2. **Confirm ICP scope** (Step 1).
3. **Force concrete campaign goal + disqualify signal** (Step 2).
4. **Generate questions, signals, anti-patterns** (Step 3).
5. **Build multi-row capture template** (Step 4).
6. **Save** as `validation-prep-{campaign-slug}.md`.

---

## Step 1, ICP scope

Voice prompt:
> "Which ICPs does this campaign target? Foundation has [N] ICPs defined. Pick 1-3 for this campaign. If multiple, name the priority for prep generation."

If foundation has only 1 ICP, skip this step and use it.

If founder picks multiple, prep generates one question shape but tunes language to the priority ICP.

---

## Step 2, Goal + disqualify

Voice prompt:
> "What does success look like across the whole campaign? Concrete terms, countable by end. Examples: 5 follow-up calls booked from 15 conversations. 2 reference customers gathered. 1 paid pilot scoped."

If founder hedges:
> "Vague goal means vague debrief. Pick a target you'll count, not feel."

Then:
> "What disqualifies a buyer mid-conversation? Budget below X, timeline past Y, decision-maker not in the room, wrong company stage. Pick one or two. Without this, every soft maybe survives."

Capture: `campaign_goal`, `disqualify_signal`.

### STOP
Failure mode: skill races past goal-setting. Force concrete or stop.

---

## Step 3, Generate questions, signals, anti-patterns

Generate 5-7 positioning-validation questions. Customize wording using foundation + positioning-tagline + priority ICP.

**Question shapes (pick 5 to 7):**

- **Category test:** "When you first heard about us, what did you think we were?"
- **Competitive frame:** "What's the closest thing to what we do that you've used or considered?"
- **Workflow probe:** "Walk me through the last time you had [the problem the positioning frames]. What did you try, what worked, what didn't?"
- **Value test:** "What's the part of [problem] that takes the most time, costs the most, or breaks the most often?"
- **Buying group:** "Who else at your company would care about this? Who would write the check?"
- **Commitment probe (end of meeting):** "What would have to be true for this to be useful to you in the next [timeframe]?"
- **Why-now probe:** "What changed for you recently that makes this matter now, if anything?"

**3 signals to listen for:**
- Past behaviors (named tools tried, hours spent, money paid)
- Named third parties (colleagues at their company who'd care, vendors they compared)
- Specific commitments (calendar slot offered, intro to a peer, ask for a quote)

**3 anti-patterns to avoid:**
- Pitching when they ask "what do you do?". Give a one-line frame, ask their workflow back.
- Defending positioning when they describe you wrong. Write it down, don't argue, debrief later.
- Hearing compliments as signal. "I love it" or "interesting space" without a commitment is noise.

---

## Step 4, Multi-row capture template

The back of the prep sheet has 15-25 blank conversation rows (matched to campaign goal). Each row has the same slots so debrief can detect patterns across the batch.

Per-row slots:
- Buyer: name, role, company
- Origin: cold / warm intro / re-engagement / booth / etc.
- Category test answer (their words for what we do)
- Competitive frame answer (closest thing they named)
- Key verbatim quote(s) from workflow probe
- Commitments captured: calendar / intro / money / reference / panic (check boxes)
- Goal hit? Y / N / partial
- Disqualify hit? Y / N

---

## Output: validation-prep-{campaign-slug}.md

```markdown
---
generated_at: "..."
founder: "..."
foundation_version: "..."
positioning_tagline_version: "..."
campaign_slug: "..."
campaign_name: "..."
priority_icp_id: 1
priority_icp_title: "..."
secondary_icp_ids: []
campaign_goal: "..."
disqualify_signal: "..."
target_conversation_count: N
---

# Validation Prep, {campaign_name}

## Campaign setup
- Priority ICP: {priority_icp_title}
- Goal: {campaign_goal}
- Disqualify if: {disqualify_signal}
- Target conversations: {N}

## Questions to ask (use across all meetings)
1. [category test, customized]
2. [competitive frame]
3. [workflow probe, customized]
4. [value test]
5. [buying group]
6. [commitment probe]
7. [why-now probe, optional]

## Listen for
- [specific past behavior cue]
- [specific commitment cue]
- [named third party cue]

## Don't
- [pitching anti-pattern, customized]
- [defending positioning anti-pattern]
- [compliment-as-signal anti-pattern]

---

## Capture sheet (use during meetings, one row per conversation)

### Conversation 1
- Buyer: ___________
- Origin: ___________
- Category test answer (their words): ___________
- Competitive frame answer: ___________
- Verbatim from workflow probe: ___________
- Commitments: [ ] calendar  [ ] intro  [ ] money  [ ] reference  [ ] panic
- Goal hit? Y / N / partial
- Disqualify hit? Y / N

### Conversation 2
[same template]

### Conversation 3
[same template]

...

### Conversation N
[same template]
```

Generate enough rows to match `target_conversation_count` (rounded up to nearest 5).

---

## Completion

1. Save `validation-prep-{campaign-slug}.md`.
2. Tell founder: *"Prep sheet saved. Print or pull up on the device you'll have during conversations. Same sheet across all meetings in this campaign. After the campaign block, run /validation-debrief on the filled sheet."*
3. Status: DONE if all sections complete. NEEDS_CONTEXT if foundation, positioning-tagline, or campaign missing.

---

## Edge cases

- **Foundation, positioning-tagline, or campaign missing:** stop. Tell the founder which is missing and what to run first.
- **Founder wants to run before each individual meeting:** redirect. Same sheet works across the block. Re-running per meeting adds work without adding signal. Mid-campaign updates happen in /validation-debrief after the block.
- **Single buyer scenario, no campaign:** the skill needs a campaign. If the founder has one meeting and no campaign, suggest running /campaign first or treating the single meeting as a one-row mini-campaign.
- **Multiple ICPs targeted in same campaign:** generate one question set tuned to the priority ICP. Note in skill output which ICPs the question wording leans toward. Founder can edit per-row if they realize mid-meeting the buyer is a different ICP.
- **Founder claims they already know what to ask:** push gently. *"The skill is anti-slop. It strips out the questions that feel useful but produce noise. Run it once, compare to what you'd have done."*
- **No active conference but a continuous outreach push:** treat the push as a campaign with a defined window (e.g., "next 30 days"). Same skill applies.
