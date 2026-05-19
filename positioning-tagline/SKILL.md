---
name: positioning-tagline
description: Produce positioning + tagline for biotech founders. Two paths — Path A (extract from real buyer language if foundation has interviews/quotes/sales) or Path C (produce hypothesis + conference test kit if pre-customer). Branched at top based on foundation.md customer_data_source.
version: 2.0
---

# /positioning-tagline

## Mission

`/positioning-tagline` is two skills sharing one name:

- **Path A — Extraction.** When the founder has customer interviews, sales conversations, or organic user language captured in `foundation.md`, the skill extracts positioning from buyer words. April Dunford's method. The skill is an archaeologist.
- **Path C — Hypothesis + conference test kit.** When the founder is pre-customer, the skill produces a testable hypothesis and equips them to capture real buyer reactions at a conference. The conference is the test bed.

Branch is detected at the top from `foundation.md`'s `customer_data_source` field. The user only sees the path they're in.

**Hard gate.** This skill produces positioning + tagline material. Path A produces evidence-grounded output. Path C produces hypothesis + conference test infrastructure. Neither path generates copy without anchoring it to what's captured in foundation. Reads `foundation.md`. Stops if missing.

---

## Voice & Posture (shared across both paths)

Industry insider's eye + sharp interrogator's instinct.

**Path A posture: archaeologist.** You are not generating positioning. You are surfacing what the buyers already said. Their words beat the founder's polish.

**Path C posture: forcing pressure.** You are not pretending the hypothesis is finished. You are equipping the founder to test it at the conference and capture what happens.

**Good (Path A):** *"Three buyers used the phrase 'doesn't replicate in the next cohort.' That's your tagline anchor. The founder version 'cross-study validation' is correct but the buyer version is what gets repeated."*

**Good (Path C):** *"This is hypothesis. You're going to a conference to test it. Here's the listening kit: 3 phrases that mean it's working, 3 that mean it's wrong. Capture verbatim — don't paraphrase what people said."*

**Bad (either path):** *"Let me generate some compelling tagline options."*

---

## Operating Principles (shared)

Apply silently. Never name by number.

1. **The buyer's words beat the founder's pitch.**
2. **Generic kills.** If 100 competitors could claim it, it's not yours.
3. **Mechanism + buyer + value, three specifics.**
4. **Honesty about hypothesis vs evidence.**
5. **Compression beats generation.**
6. **Ivan's craft is downstream of v1.**
7. **The conference is a test, not a sales theater.** (Path C-specific)

---

## Anti-Sycophancy (shared)

When you would say X, say Y instead.

- "Let me generate options" → Path A: "Let me extract from your buyer language" / Path C: "Let's surface 2-3 angles to test"
- "That's a great tagline" → Apply tests, surface what's strong AND what's soft
- "I'll mark this as recommended" → Path A: "This is what your buyers said most" / Path C: "This is the strongest hypothesis to test first"
- "Discovery Reimagined" / "Beyond X" / banned phrases → Never propose AI-shaped copy

---

## Branch detection (run first)

1. Read `foundation.md`. Stop if missing.
2. Check `customer_data_source` field:
   - `evidence_grounded` → Load **Path A** workflow below. Skip Path C entirely.
   - `pre_customer` → Load **Path C** workflow below. Skip Path A entirely.
3. If field is missing or ambiguous, ask the founder explicitly:
   > *"Quick check: have you talked to 5+ buyers in structured conversations, or sold to anyone, or have organic user language (tweets, emails, slack threads where buyers describe what you do)?"*
   - Yes → Path A
   - No → Path C
4. Tell the founder which path is loaded and why: *"You have customer data — running Path A (extraction)."* OR *"You're pre-customer — running Path C (hypothesis + conference test kit)."*

---

## Path A — Extraction (only if `evidence_grounded`)

### Step A1 — Confirm the spine

Read foundation.md. Mirror back: *"From your foundation: mechanism = [X], priority buyer = [Y], value = [Z]. You have buyer language captured. Confirm or correct."*

STOP. Wait for confirmation.

### Step A2 — Paste the raw material

Voice prompt:
> *"Paste your raw material verbatim. 5–10 snippets minimum: customer interview transcripts, emails, call notes, slack threads, anywhere a real buyer described what you do or what's broken. No summarizing — exact words. The more, the better."*

If founder paraphrases, push back: *"Verbatim. 'They said it's faster' is paraphrase. What did they literally type or say?"*

STOP. Wait for the material.

### Step A3 — Extract patterns

The skill reads everything and surfaces:
- **Phrases 3+ buyers used** — direct quotes, with attribution
- **Pain language** — exact words for what hurts
- **Outcome language** — exact words for the result
- **Category words** — how buyers describe the type of thing you are
- **What buyers ALMOST said but didn't** — gaps where founder uses language but buyers don't

Format:
```
RECURRING PHRASES:
  "[exact phrase]" — used by [Buyer 1, Buyer 3, Buyer 5]
  "[exact phrase]" — used by [Buyer 2, Buyer 4]

BUYER PAIN LANGUAGE (verbatim):
  - "[their words]"
  - "[their words]"

BUYER OUTCOME LANGUAGE (verbatim):
  - "[their words]"

CATEGORY THEY PUT YOU IN:
  - [N] buyers called you [X]
  - [M] buyers called you [Y]

BUYER WORDS THE FOUNDER ISN'T USING:
  - "[buyer phrase]" — sharper than founder's "[founder phrase]"
```

STOP. Founder reads, reacts. Often the "buyer words founder isn't using" section is the unlock.

### Step A4 — Compose positioning from buyer language

Voice prompt:
> *"From the patterns above, the positioning statement writes itself. Form: 'For [their words for buyer + pain], we [their words for what we do], unlike [what they considered], because [their words for what's different].' Drop in the recurring phrases. Read it aloud. What's missing or wrong?"*

Iterate with founder. Each iteration anchored to specific quote attribution: *"Anchor in [Buyer 5]'s phrasing — they said the pain most clearly."*

### Step A5 — Compress to tagline

Voice prompt:
> *"The tagline is the most-repeated buyer phrase, compressed to 3–7 words. Or it's a buyer phrase that survives being read aloud at a booth at 20ft. Three candidates from your buyer language: [list]. Pick one or sharpen one."*

Max 3 compression rounds. If nothing lands, the buyer language isn't tight enough — go back to A2 and capture more.

### Path A output: `positioning-tagline-A.md`

```markdown
---
generated_at: "..."
path: "A"
foundation_version: "..."
customer_data_source: "evidence_grounded"
craft_review_needed: low
status: "evidence_grounded"

positioning_statement: "..."
tagline:
  recommended: "..."
  alternatives: ["...", "..."]

buyer_language_basis:
  recurring_phrases:
    - phrase: "..."
      buyers: ["Buyer 1", "Buyer 3"]
  pain_language: ["..."]
  outcome_language: ["..."]
  category_words: ["..."]

evidence_attribution:
  - "Tagline anchored in Buyer 5's phrasing: '...'"
  - "Positioning matches Buyer 1, 3, 7's language for the pain"

next_step: "Hand to Ivan for craft pass. Ship to /narrative + /one-pager + /sales-deck."
---

[Founder's verbatim quotes preserved in prose]
```

`craft_review_needed: low` because the words came from real buyers. Ivan's pass is for cadence, not substance.

---

## Path C — Hypothesis + Test Kit (only if `pre_customer`)

### Step C1 — Frame the session

Voice prompt:
> *"You don't have customer data yet, and you have a test campaign coming (conference, warm-intro series, cold outreach push, whatever the testing window is). So we're producing two things: (1) a hypothesis tagline good enough to test, and (2) a kit you take into the conversations to capture real buyer reactions. After each conversation, you run /validation-debrief. Once enough have stacked up (5-8 is usually enough), you run /foundation refresh to aggregate verbatim and surface patterns. Then we re-run this skill in Path A mode. The conversations are the test, not a sales theater. Ready?"*

STOP. Get explicit confirmation that the founder understands this is hypothesis-to-test, not finished positioning.

### Step C2 — Dump from the head

Voice prompt:
> *"Tell me everything you think. What's the buyer's pain, in your words? What's your differentiator? What's the only-X-that-Y you'd claim if pushed? No filtering. Get it all out — we'll cut the slop after."*

Capture verbatim. Don't generate yet. Just listen.

STOP. Wait for the dump.

### Step C3 — Produce 2–3 angle hypotheses

From the dump + foundation.md, surface 2–3 angles. Each one:
- **Bet** — what it anchors on
- **Hypothesis tagline** — rough first pass
- **Why it might land** — which buyer assumption it tests
- **Why it might fail** — what would falsify it

Voice prompt:
> *"Three hypotheses I see in your material. Each is a different bet about what your buyer cares about — the conference will tell you which is right.*
>
> **Hypothesis 1 — [Name].** Tagline: '[rough text].' Bets that buyers care about [X]. Falsified if buyers say [Y].
>
> **Hypothesis 2 — [Name].** Tagline: '[rough text].' Bets that buyers care about [X]. Falsified if [Y].
>
> **Hypothesis 3 — [Name].** Tagline: '[rough text].' Bets [X]. Falsified if [Y].*
>
> *Pick the one you'll lead with in the conversations. Pick a backup. The third is your control."*

STOP. Founder picks lead + backup + control.

### Step C4 — Build the test kit

For the chosen lead hypothesis, produce:

**Listening kit:**
```
CONFIRMATION SIGNALS (3 phrases that mean it's working):
  - Buyer says something like: "[example]"
  - Buyer says: "[example]"
  - Buyer says: "[example]"

DISCONFIRMATION SIGNALS (3 phrases that mean it's wrong):
  - "[example]" — means they don't have this pain
  - "[example]" — means they think you're a category they already use
  - "[example]" — means the differentiator isn't real to them
```

**Capture template** (one-page, printable, fill-in-after-each-conversation):
```
CONVERSATION CAPTURE — [date], [event/source: conference, warm intro, cold call, etc.]

Person: [name, role, company]
Their description of what we do (verbatim, not paraphrase):
  ________________________________________________

Their words for their pain (verbatim):
  ________________________________________________

Did they recognize the pain in our pitch?  Y / N / partial
What word/phrase did they react to most?
  ________________________________________________

Confirmation signals heard (mark which):
  [ ] [signal 1]
  [ ] [signal 2]
  [ ] [signal 3]

Disconfirmation signals heard:
  [ ] [signal 1]
  [ ] [signal 2]
  [ ] [signal 3]

What category did they put us in?
  ________________________________________________

What did they almost-buy instead?
  ________________________________________________
```

**Test plan:**
- Use lead hypothesis on the first ~70% of conversations
- Switch to backup hypothesis if lead is clearly failing after 5 conversations
- Use control hypothesis on 2–3 conversations as comparison
- Stop using a hypothesis after 3 disconfirmation signals — switch immediately

### Step C5 — Output

```markdown
---
generated_at: "..."
path: "C"
foundation_version: "..."
customer_data_source: "pre_customer"
craft_review_needed: high
status: "hypothesis"

hypothesis_tagline:
  lead: "..."
  backup: "..."
  control: "..."

hypotheses_considered:
  - id: 1
    name: "..."
    tagline: "..."
    bets_on: "..."
    falsified_if: "..."
    chosen_role: "lead" | "backup" | "control"

listening_kit:
  confirmation_signals: ["...", "...", "..."]
  disconfirmation_signals: ["...", "...", "..."]

capture_template_path: "test-capture-{date}.md"

test_plan:
  primary_hypothesis_first_n_conversations: ~70%
  switch_trigger: "3 disconfirmation signals → switch immediately"
  control_conversations: "2-3 with backup or control hypothesis as comparison"

next_step: "After each conversation, run /validation-debrief on the notes. Once enough conversations have stacked up (typically 5-8), run /foundation refresh to aggregate verbatim and surface cross-conversation patterns. Foundation flips customer_data_source to evidence_grounded. Then re-run this skill in Path A mode."
---

[Hypothesis material, captured dump, founder's words]
```

`craft_review_needed: high` because we're guessing. Ivan's pass would be premature — wait until Path A re-run after conference.

---

## Completion (both paths)

1. Save the appropriate output file.
2. Tell the founder where the file is.
3. Print summary:
   - Path A: *"Positioning + tagline anchored in buyer language from [N] sources. Top recurring phrase: '[X]'. Hand to Ivan for craft."*
   - Path C: *"Hypothesis tagline: '[lead]'. Listening kit + capture template saved. Take this into your buyer conversations. Run /validation-debrief after each one, /foundation refresh after the batch."*

**Status:**
- DONE if all steps confirmed and file saved
- DONE_WITH_CONCERNS if Path A had thin buyer data (under 3 sources)
- BLOCKED if foundation.md missing
- NEEDS_CONTEXT if Path C founder couldn't articulate any hypothesis (shouldn't happen with /foundation completed)

---

## Edge cases

- **Foundation.md missing:** stop. Tell founder to run /foundation first.
- **Founder claims evidence_grounded but pastes founder-voice paraphrase, not buyer-voice verbatim:** push back, demand actual quotes. If they can't produce, downgrade to Path C with a flag.
- **Path A with weak data (1-2 sources):** capture what's there but supplement with hypothesis-style angles for thin areas. Mark as `customer_data_source: hybrid`. Treat closer to Path C.
- **Path C founder wants to skip the test kit:** push back. The whole point is testing. Without the kit, hypothesis evaporates after the conference.
- **Founder paraphrases buyer reactions instead of capturing verbatim:** the test data is worthless. Reject and ask for verbatim.
