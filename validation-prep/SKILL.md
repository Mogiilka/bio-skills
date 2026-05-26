---
name: validation-prep
description: Pre-campaign prep for a batch of buyer conversations (conference, warm-intro run, outreach push). Reads foundation + positioning-tagline + campaign. Produces ONE reusable prep sheet covering all meetings in the campaign block. Question bank wired to foundation claims, scannable reading-the-answer guide per question, capture mechanics for two conversation rhythms. Runs once per campaign, not per meeting.
version: 0.3
---

# /validation-prep

> **Before any operator-facing output:** read [`../CONVENTIONS.md`](../CONVENTIONS.md) and apply the banned-words pass, voice principles, and self-review loop.

## Mission

`/validation-prep` produces a single prep sheet the founder uses across an entire campaign block (a conference, a warm-intro run, an outreach push). Run once before the block starts. The same sheet supports every conversation in the block. Capture rows on the back.

**The job is positioning validation, not product validation.** Foundation already captured what the product IS. This skill tests whether the positioning of it survives contact with buyers. Does their category match yours? Do they describe the value the way you describe it, or differently? Do they put you next to the competitors you expect?

**Run once per campaign.** Same sheet across all meetings in the block. Improvising per buyer kills cross-row comparability.

**Refuses to run without foundation, positioning-tagline, and campaign.** All three are required. If any is missing, the skill stops.

---

## Voice & Posture

Industry insider's eye plus sharp interrogator's instinct. Push the founder away from pitching, toward listening.

**What you do:**
- Confirm priority target profile(s) from foundation
- Force a countable campaign goal (follow-ups booked, references gathered, pilots scoped)
- Force a concrete disqualify signal
- Generate questions wired to the founder's foundation claims, with question shape matched to failure mode
- State the design logic out loud so the founder sees what each question is measuring
- Bake meeting-flow transitions between questions
- Set up capture mechanics for two conversation rhythms (scheduled meeting + booth drop-by)
- Output one prep sheet with capture rows

**What you don't do:**
- Generate per-buyer prep (this is campaign-scoped)
- Write a pitch script
- Generate hypothetical questions ("would you use this if...")
- Name any external methodology or framework by name
- Test whether the product or problem exists (foundation already did that)
- Promise time estimates anywhere in the prep sheet or the skill flow

---

## Operating Principles

1. **Past behavior beats opinion.** "Tell me about the last time you tried X" beats "would you use X."
2. **The buyer's words beat the founder's description.** How they describe what you do is the test. Your description is the hypothesis.
3. **Specific commitments are signal.** Calendar slot, money paid, intro offered, public reference. Compliments and vague future-tense are noise.
4. **Indirect probes beat head-on evaluation.** The skill never asks the buyer to evaluate a claim ("is our category right?"). Polite-sycophantic answers contaminate the data. Ask about the buyer's world; let claim-test signals fall out of their answers.
5. **Cross-row patterns are the test, not single conversations.** One buyer breaking a claim is a data point. 18 of 30 breaking the same claim is a finding.
6. **Disqualify-out is a valid outcome.** Not every conversation should end with a follow-up. Define the disqualify signal before walking in.

---

## Patterns

### Pattern 1, Founder writes a pitch question
*"I want to ask if they'd find our analysis layer valuable."* → Banned. Hypothetical, leading. Convert to past-behavior probe: *"Tell me about the last time you had to explain your technical detail to a non-scientist buyer. What did you try, what worked, what didn't?"*

### Pattern 2, Founder writes a product-existence question
*"I want to find out if biotechs even need this."* → Wrong layer. Foundation already captured the product. This skill validates positioning.

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
- Never name a methodology in the prompts. Use the principles directly.

---

## How This Skill Works

1. **Read foundation.md, positioning-tagline.md, campaign-{slug}.md.** Stop if any missing.
2. **Open with frame** (what produces / how it goes / what you end with).
3. **Step 1: Lock priority target profile** from foundation.
4. **Step 2: Force countable goal + disqualify signal.**
5. **Step 3: Generate question bank wired to foundation claims.** Name the claims, state the design logic, map question shape to failure mode, output 5 questions in meeting order with reading guide per question, bake transitions.
6. **Step 4: Set up capture mode.** Two rhythms (scheduled + booth fallback). Capture founder's existing tools.
7. **Step 5: Save** as `validation-prep-{campaign-slug}.md`.

---

## Opening frame

Before the first question:

> **What this produces.** One prep sheet for every conversation in your {campaign_name} block. Sized to test whether buyers describe your category, problem, and differentiation the same way your foundation does.
>
> **How it goes.** Lock priority target profile, set countable goal and disqualify signal, generate questions wired to your foundation, set up capture.
>
> **What you end with.** One printable file.

Then Step 1.

---

## Step 1, Target profile scope

Voice prompt:
> "Foundation has [N] target profiles. Which is the priority for {campaign_name}?"
>
> [List each target profile by its descriptive name from foundation, not by code.]

If foundation has only 1 target profile, skip this step and use it.

If founder picks one, prep generates one bank tuned to it.
If founder picks multiple, prep generates a bank per profile. Each profile's rows tagged separately so debrief can read patterns within each profile, not mixed.

Capture: `priority_target_profile_id`, `secondary_target_profile_ids`.

---

## Step 2, Goal + disqualify

Voice prompt:
> "Goal at end of week, in countable terms? Examples: 6 follow-up calls booked, 2 pilot conversations, 1 reference customer."

If founder hedges:
> "Vague goal means vague debrief. Pick a number you'll count, not feel."

Then:
> "Disqualify signal. What kills a meeting mid-conversation? Examples: no decision-maker in the room, budget below X, company stage too early, procurement requires an MSA they can't sign."

Capture: `campaign_goal`, `disqualify_signal` in the founder's own wording.

### STOP
Failure mode: skill races past goal-setting. Force concrete or stop.

---

## Step 3, Generate the question bank

### 3a, Name the testable claims

Read foundation. Extract the testable claims:
- **Category** (what kind of thing the company is)
- **Problem** (what's broken that they fix)
- **Target** (who has the problem)
- **Differentiation** (how they're different from alternatives)
- **Mechanism** (the technical or methodological how)

State them to the founder in plain words, using nouns and verbs from their foundation:

> "Your foundation makes 5 testable claims:
> - **Category:** {category claim from foundation}
> - **Problem:** {problem claim from foundation}
> - **Target:** {target claim from foundation}
> - **Differentiation:** {differentiation claim from foundation}
> - **Mechanism:** {mechanism claim from foundation}"

### 3b, State the design logic

> "Each question probes one claim indirectly. The skill never asks the buyer to evaluate a claim head-on, because polite-sycophantic answers contaminate the data. Instead the questions ask about the buyer's world. Mismatches across multiple buyers mean a claim is failing in the market.
>
> Question shape matches failure mode:
> - **Category** fails through misattribution. Ask what they compare you to. Hear which category they reach for.
> - **Problem** fails through non-existence. Ask about their last attempt. Hear whether there was one.
> - **Differentiation** fails through wrong pain layer. Ask what breaks most. Hear whether your axis is the answer, or something else.
> - **Target** fails through wrong role. Surfaced via the recommend question's second beat (who's a fit) and from buying-group signals captured during the workflow probe.
> - **The message itself** is tested at the close. Ask the buyer to describe you to a colleague. Hear which words they pick."

### 3c, Generate the question bank

Five questions plus transitions, in meeting order. Wording is conversational, not discovery-script.

#### 1. Q-opener (before pitch)

> "What made you want to take this meeting?"

**Tests:** the hook in your outreach.

**Reading:**
- "I read your blurb on {claim phrase}" → positioning hook landed
- "My admin booked it" → outreach didn't carry a hook
- "I thought you were a {wrong category}" → prior category framing is failing

**Transition to pitch:** "Got it. Let me tell you what we do, then I want to hear about your side."

#### 2. Q-workflow (after pitch)

> "When's the last time you were working on {problem from foundation}? Tell me what you tried."

**Tests:** whether the problem exists for this buyer, in their words.

**Reading:**
- Concrete past-attempt story → problem present for them
- "We don't do that" → wrong target or wrong problem framing
- "We tried but blocker was {X}" → problem exists, differentiation may be wrong layer

**Transition:** "When you were trying that, what did you reach for?"

#### 3. Q-competitive

> "Any tools, vendors, anyone you talked to?"

**Tests:** which category the market puts you in.

**Reading:**
- Software / tool names → market sees you as software
- Service / agency / CRO names → market shelves you with services
- "Nothing, we don't have a solution" → either differentiated or invisible; Q-workflow disambiguates

**Transition:** "And in that whole process, where does it usually break?"

#### 4. Q-pain

> "Where does that usually go wrong? Time, cost, something else?"

**Tests:** whether your differentiation sits on the buyer's top pain.

**Reading:**
- Aligns with your differentiation axis → claim lands
- Different pain layer → differentiation is wrong layer; reposition or extend
- A pain layer not in your foundation → opportunity to capture for next-round repositioning

**Transition:** "Last thing. If our conversation came up later with a colleague..."

#### 5. Q-recommend (close)

Two beats.

**Beat 1:**
> "If our conversation came up later with a colleague, how would you describe us to them?"

**Beat 2 (after their answer, capture verbatim first):**
> "And who do you think would be a great fit for this?"

**This is the message test.** The buyer's description in Beat 1 IS your message coming back in their words.

**Reading Beat 1 (the message test):**
- They use your phrasing → message landed verbatim
- They rewrite it better → lift their phrasing into next-round copy
- They describe you in a different category than yours → message didn't carry the category claim
- They can't describe you cleanly → message was too abstract

**Reading Beat 2 (target validation):**
- Peer-target-profile name with reason → category and target landing
- Wrong-category referral → category still dragging in market
- "Anyone in {industry}, I guess" → polite filler, didn't land

### 3d, Cross-row note

State to founder:

> "One buyer breaking a claim is a data point. 18 of 30 breaking the same claim is a finding. The sheet is designed for that pattern read in /validation-debrief."

### 3e, Confirm or edit

> "Edits?"

If founder tries to add a hypothetical or pitch question, convert it to a past-behavior probe per Pattern 1.

---

## Step 4, Capture mode

Lead with the problem the founder faces, not safety rules.

Voice:

> "You'll talk to a stack of people across {campaign_name}. Without a capture system, by Friday you remember a few clearly and the rest as blur. Verbatim is what makes /validation-debrief readable.
>
> Two rhythms because {campaign_name} has two.
>
> **Scheduled meetings.** Open with 'Mind if I record this? Just for my notes.' Most say yes. If they say no, fall back to notes.
>
> **Booth drop-bys** (or other bursty contexts). No time for a sheet. Don't try live capture. Right after the buyer walks away, fire phone voice memo. Their words: 'Just talked to [name], they asked [X], their pain was [phrase].'"

Then:

> "What tools do you already use?"

Capture the founder's tools (named transcription tool, phone voice memo, etc.) and bake them into the sheet output.

Then the trade-off footnote, not a commandment:

> "One trade-off worth knowing: recording without asking is what backfires. Asked-and-recording or not-recording both work. If you forget the opener and realize mid-conversation, pause and ask."

Capture: `capture_tools_scheduled`, `capture_tools_booth`, `recording_opener_phrase`.

---

## Step 5, Save and hand off

Save the prep sheet (see Output template below).

Tell founder:

> "Saved validation-prep-{campaign-slug}.md.
>
> Page 1: opener phrase, transitions, frame for your pocket.
> Page 2: questions with claim labels visible.
> Pages 3+: capture rows.
>
> After {campaign_name}, run /validation-debrief on the filled sheet plus your {named tools} transcripts and voice memos."

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
priority_target_profile_id: 1
priority_target_profile_title: "..."
secondary_target_profile_ids: []
campaign_goal: "..."
disqualify_signal: "..."
target_conversation_count: N
capture_tools_scheduled: "..."
capture_tools_booth: "..."
---

# Validation Prep, {campaign_name}

## Page 1, Pocket card

**Campaign setup:**
- Priority target profile: {priority_target_profile_title}
- Goal: {campaign_goal}
- Disqualify if: {disqualify_signal}

**Recording opener for scheduled meetings:**
> "Mind if I record this? Just for my notes."

**Booth fallback (right after the buyer walks away):**
> "Just talked to [name], they asked [X], their pain was [phrase]."

**Transitions between questions:**
- After Q-opener → "Got it. Let me tell you what we do, then I want to hear about your side."
- After your pitch → "When's the last time you were working on {problem}..."
- After Q-workflow → "When you were trying that, what did you reach for?"
- After Q-competitive → "And in that whole process, where does it usually break?"
- After Q-pain → "Last thing. If our conversation came up later with a colleague..."

---

## Page 2, Questions with claim labels

### Your foundation claims (the test targets):
- **Category:** {category claim}
- **Problem:** {problem claim}
- **Target:** {target claim}
- **Differentiation:** {differentiation claim}
- **Mechanism:** {mechanism claim}

### 1. Q-opener (before pitch) — tests outreach hook
"What made you want to take this meeting?"

### 2. Q-workflow (after pitch) — tests problem + target
"When's the last time you were working on {problem}? Tell me what you tried."

### 3. Q-competitive — tests category + differentiation
"Any tools, vendors, anyone you talked to?"

### 4. Q-pain — tests differentiation pain layer
"Where does that usually go wrong? Time, cost, something else?"

### 5. Q-recommend (close, two beats) — tests message + target
- Beat 1: "If our conversation came up later with a colleague, how would you describe us to them?"
- Beat 2: "And who do you think would be a great fit for this?"

**Listening cue throughout:** note which of YOUR words the buyer uses spontaneously later in the conversation. That phrase landed.

---

## Pages 3+, Capture rows (one row per conversation)

### Conversation 1
- Buyer: ___________
- Capture mode: [ ] meeting  [ ] booth
- Recording: [ ] Y  [ ] N
- Q-opener answer (verbatim): ___________
- Q-workflow (verbatim phrases): ___________
- Q-competitive (specific names): ___________
- Q-pain (their word for pain): ___________
- Q-recommend Beat 1, their description (verbatim): ___________
- Q-recommend Beat 2, who's a fit (names): ___________
- Vocabulary echo (their use of your words later): ___________
- Commitments: [ ] calendar  [ ] intro  [ ] money  [ ] reference
- Goal hit? Y / N / partial
- Disqualify hit? Y / N

### Conversation 2
[same template]

...

### Conversation N
[same template]
```

Generate enough rows to match `target_conversation_count` plus a buffer for booth drop-bys (round up to nearest 5).

---

## Completion

1. Save `validation-prep-{campaign-slug}.md`.
2. Tell founder per Step 5 voice block.
3. Status: DONE if all sections complete. NEEDS_CONTEXT if foundation, positioning-tagline, or campaign missing.

---

## Edge cases

- **Foundation, positioning-tagline, or campaign missing:** stop. Tell the founder which is missing and what to run first.
- **Foundation has no testable claims (all hypothesis-flagged with no specificity):** stop. The question bank can't test claims that aren't specified. Suggest re-running /foundation to sharpen.
- **Founder wants to run before each individual meeting:** redirect. Same sheet works across the block. Re-running per meeting adds work without adding signal.
- **Single buyer scenario, no campaign:** the skill needs a campaign. Suggest running /campaign first or treating the single meeting as a one-row mini-campaign.
- **Multiple target profiles targeted in same campaign:** generate one bank per profile, tagged on its own rows. Founder picks per-row which profile a buyer fits when filling.
- **Founder claims they already know what to ask:** push gently. *"The skill is anti-slop. It strips out questions that feel useful but produce noise. Run it once, compare to what you'd have done."*
- **No active conference but a continuous outreach push:** treat the push as a campaign with a defined window. Same skill applies.
- **Founder declines the recording opener:** still output it in the prep sheet but mark it optional. Add a header note: "Without verbatim, debrief works from paraphrasing, which loses buyer-specific phrasing. Highest-cost trade in this skill."
