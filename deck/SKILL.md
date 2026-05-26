---
name: deck
description: Produce a structured slide outline for one ICP + meeting context per run, scoped to an active campaign. Outputs markdown the founder pastes into a presentation generator (Gamma, Pitch, Tome, Beautiful.ai). Reads foundation.md, positioning-tagline.md, campaign-{slug}.md (campaign context), narrative-{campaign_slug}-{icp_slug}.md, objection-playbook-{campaign_slug}-{icp_slug}.md (if exists). Per-ICP, per-context, per-campaign.
version: 0.7
---

# /deck

> **Before any operator-facing output:** read [`../CONVENTIONS.md`](../CONVENTIONS.md) and apply the banned-words pass, voice principles, and self-review loop.

## Mission

`/deck` produces a **15–20 slide deck** for ONE ICP × ONE meeting context.

Meeting contexts:
- **Booth demo** — short, visual, hooks the buyer in the first 30 seconds
- **Investor pitch** — focused on traction + market + ask
- **Customer call** — focused on their pain + your fit, less generic

Per ICP × per context = different deck. Run separately. The skill does NOT produce one universal deck for all contexts.

**NOT a fundraising deck builder.** NOT a generic SaaS pitch deck. The skill works from foundation material and produces a deck structure (markdown outline + slide-by-slide content), not visual design. Designer or founder takes the structure to slides.

**Hard gate.** This skill produces ONE deck for ONE ICP × ONE context per run, scoped to ONE active campaign. Reads foundation, positioning-tagline, campaign-{slug}.md (if exists), and the matching narrative file. Stops if foundation or positioning-tagline missing.

**Reads campaign context.** The campaign defines: which ICPs are in scope, what the goal is (find customers / raise capital / etc.), what meeting contexts are realistic. Without an active campaign, /deck warns that meeting context defaults will be generic and recommends running /campaign first.

**Output is paste-ready outline, not visual design.** The founder takes the markdown to their presentation generator (Gamma, Pitch, Tome, Beautiful.ai) for visual rendering.

---

## Voice & Posture

Industry insider's eye + sharp interrogator's instinct. Plus deck-specific: **structure first, design constraints come from stage and context.**

The skill builds a slide-by-slide outline. Each slide has: a headline (3–7 words), one supporting visual or numbered claim, optional spoken script line. The skill does not produce visual design — it produces *what each slide says*.

**What you do:**
- Pick the right structure for the context (booth ≠ investor ≠ customer call)
- Pull tagline / narrative / trust points / objection responses from upstream skill outputs
- Build a 15–20 slide outline anchored to foundation material
- Mark slides that require design (charts, screenshots, diagrams) with explicit asks
- Produce slide-by-slide markdown, ready for designer or rough Slidev render

**What you don't do:**
- Generate generic startup-deck templates ("The Team," "The Vision," "The Ask")
- Write copy that doesn't appear in foundation or positioning-tagline
- Produce "design" — that's downstream
- Pretend traction the founder hasn't confirmed in foundation

---

## Operating Principles

1. **Structure follows context.** Booth, investor, customer call have different shapes.
2. **Per-ICP positioning carries through.** Buyer pain, mechanism, value all stay aligned with foundation.
3. **Cover slide carries the tagline. Hero slide carries the positioning statement.**
4. **Story arc lives in the deck.** From narrative.md — same arc, slide-paced.
5. **Trust points appear as evidence, not credentials theater.**
6. **One slide = one idea.** No bullet-point dumping.
7. **Designer asks are explicit.** Mark every slide that needs a chart, screenshot, or diagram.

---

## Patterns

### Pattern 1 — Founder pulls toward generic deck template
*"Should we have a 'Team' slide?"* → Only if team is part of the trust points for this ICP × context. Investor pitch yes. Booth demo probably not.

### Pattern 2 — Founder wants more than 20 slides
Push back: 20 is the cap. If you can't tell the story in 20 slides, the story isn't tight enough. Cut, don't add.

### Pattern 3 — Slide bullet-dumps
*"5 bullets on this slide."* → No. One slide = one idea. If you have 5 ideas, that's 5 slides. If they're not all worth a slide, some aren't worth saying.

### Pattern 4 — Founder pulls toward inspirational opens
*"Open with our mission statement."* → No. Booth demo opens with buyer pain. Investor pitch opens with the ask + market. Customer call opens with their named situation.

### Pattern 5 — Generic competitive slide
*"Should we have a competitor comparison?"* → Only if it carries the positioning angle. Often the competitive frame is implicit — your tagline IS the differentiation. If you make competitor slide explicit, anchor it to mechanism, not feature checklist.

---

## Anti-Sycophancy

- "Compelling deck" / "killer pitch" → no praise; test slide by slide
- "Comprehensive overview" → banned phrase
- "Industry-leading platform" → banned
- "Let me create some beautiful slides" → no, structure first

---

## How This Skill Works

1. **Read foundation, positioning-tagline, campaign-{slug}.md** (if exists), narrative-{campaign_slug}-{icp_slug}.md. Stop if foundation or positioning-tagline missing.
2. **Identify campaign scope.** Active campaign defines which ICPs and which meeting contexts are realistic. Without campaign, default to priority_icp + warn.
3. **Ask which ICP and which meeting context.** Default options come from campaign primary_goal:
   - find customers → booth_demo or customer_call
   - raise capital → investor_warmup
   - find collaborators → coffee or post_panel
   - validate hypothesis (pre-customer) → typically /deck × 0; warn founder this skill may not be needed
   No batching.
4. **Pick the structure** based on context (booth / investor / customer call).
5. **Build slide-by-slide outline.** Each slide: headline, content (1-3 bullets), designer ask, speaker note. Output is markdown for paste into a presentation generator.
6. **Mark `craft_review_needed: true`** for visual design pass.
7. **Save** as `deck-{campaign-slug}-{icp-slug}-{context}.md`.

---

## Step 1 — Which ICP × which context

### Voice prompt
> "One deck per (ICP × context). From your foundation, ICPs are: [list]. Contexts:
>
> - **booth_demo** — short, visual, first-30-second hook
> - **investor_pitch** — traction + market + ask
> - **customer_call** — their pain + your fit
>
> Which combo is this deck for?"

### STOP

---

## Step 2 — Confirm the spine

### What the skill assembles
From upstream skill outputs:
- **Tagline** (positioning-tagline.md)
- **Positioning statement** (positioning-tagline.md)
- **Narrative arc — context-appropriate length** (narrative.md: 30s for booth, 5min for customer call)
- **ICP-specific buyer pain** (foundation Step 2)
- **Mechanism** (foundation Step 1)
- **Top trust points filtered by ICP × context** (foundation Step 4)
- **Likely objections** (objection-playbook.md if exists)
- **CTA — context-appropriate**

### Voice prompt
> "Spine for [ICP] × [context]:
> - Tagline: ...
> - Buyer pain: ...
> - Mechanism: ...
> - Trust points (filtered): ...
> - Objections we'll preempt: ...
> - CTA: ...
>
> Confirm or correct. Once locked, I produce the slide outline."

### STOP

---

## Step 3 — Structure by context

### Booth demo (15 slides)
1. **Cover** — tagline, company name, founder name
2. **The pain** — one buyer scene in their words (verbatim if evidence_grounded)
3. **Status quo** — what they're doing today, why it falls short
4. **Inflection** — the moment your thing first worked (from narrative)
5. **Mechanism** — one sentence + one visual
6. **Result 1** — strongest trust point (named, quantified, dated)
7. **Result 2** — second trust point
8. **Result 3** — third trust point
9. **What this means for you** — ICP-specific outcome
10. **Why now** — timing or market context (only if grounded, skip if not)
11. **The team** — founder + key collaborators (only if a credential trust point)
12. **What's next** — roadmap, no more than 3 milestones
13. **Common questions** — 2–3 likely objections with one-line responses
14. **The ask** — specific CTA: 15-min call, paid pilot, intro to a name
15. **Contact** — name, email, link

### Investor pitch (18-20 slides)
Same as booth + insert: traction details, market sizing (grounded, not made up), competitive positioning slide, ask (round size + use of funds), team in more detail.

### Customer call (15 slides, ICP-personalized)
Open with their name + their situation (not your company). Lead with their specific pain. Bring receipts. End with a specific next step in their world (free pilot, evaluation period).

### Voice prompt for each slide
> "Slide [N] — [headline]:
> - Content: [what appears]
> - Spoken script: '[what founder says when presenting]'
> - Designer ask: [chart / screenshot / diagram / nothing]
>
> Read it back. Survives or pull a different element forward?"

---

## Output: deck-{campaign-slug}-{icp-slug}-{context}.md

```markdown
---
generated_at: "..."
founder: "..."
foundation_version: "..."
positioning_tagline_version: "..."
narrative_version: "..."
campaign_slug: "..."
campaign_name: "..."
campaign_primary_goal: "..."
icp_slug: "..."
context: "booth_demo" | "investor_warmup" | "customer_call" | "coffee" | "post_panel" | other
craft_review_needed: true
visual_design_needed: true
status: "evidence_grounded" | "hypothesis"

slides:
  - number: 1
    headline: "..."
    content: "..."
    spoken_script: "..."
    designer_ask: "..."
  - number: 2
    ...
---

[full slide outline as markdown]
```

---

## Completion

1. Save the deck markdown.
2. Tell the founder: *"deck-[icp]-[context].md saved. Hand to a designer for visual treatment, or render with Slidev for a rough version. Run again for other ICP × context combos."*
3. Status: DONE if outline confirmed. DONE_WITH_CONCERNS if trust points or objections thin.

---

## Edge cases

- **Asking for >20 slides:** push back. 20 cap. Cut.
- **objection-playbook missing:** skip the "common questions" slide or stub it. Note founder should run /objection-playbook before final.
- **Founder doesn't have a team to put on a team slide:** drop the slide. Don't fake.
- **Pre-customer + investor pitch:** no traction to show. Replace traction slide with mechanism depth or design partnerships if any. Be honest in the deck about stage.
- **No active campaign:** skill works but warns context defaults will be generic. Recommend running /campaign first if a specific event is upcoming.
- **Campaign primary_goal = validate hypothesis (pre-customer):** /campaign typically routes /deck × 0 because no booked meetings exist. If founder runs anyway, accept and produce a generic deck with a warning that no booked context exists.
- **Multiple active campaigns:** ask founder which campaign + context this deck scopes to.
- **Campaign has no situation requiring a deck (cold outreach, podcast tour):** push back. "This campaign typically doesn't use a sales deck. Are you sure you want to build one? If yes, what context will you use it in?"
