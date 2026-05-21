---
name: one-pager
description: Produce one printable PDF leave-behind for one ICP at a time, scoped to an active campaign. Reads foundation.md, positioning-tagline.md, campaign-{slug}.md (campaign context), and narrative-{campaign_slug}-{icp_slug}.md if exists. Top line carries the tagline, body anchors in trust points, CTA matches the campaign goal. Per-ICP per-campaign. Run separately, never batch.
version: 0.6
---

# /one-pager

## Mission

`/one-pager` produces a **one-page printable PDF leave-behind**. One ICP at a time. The founder runs it once per ICP they need.

Built for a specific moment: founder hands it to a biotech buyer at a conference. Buyer reads it in 60–90 seconds. It either earns a follow-up or doesn't.

**What it is NOT:**
- A marketing brochure
- A pitch deck condensed
- A multi-page sales sheet

**Hard gate.** This skill produces ONE one-pager for ONE specified ICP per run, scoped to ONE active campaign. To produce 3 one-pagers (for 3 ICPs), the founder runs the skill 3 times. No batching. The skill needs to know which ICP and which campaign this one is for, because positioning angle, pain phrasing, trust points, and CTA all shift per ICP × campaign.

**Reads campaign context.** Like /narrative, /one-pager scopes to an active campaign. The campaign defines: which ICPs are in scope, what the goal is (find customers, raise capital, etc.), what situations the founder will use the one-pager in. Without an active campaign, /one-pager defaults to foundation priority_icp and warns that the CTA will be generic.

---

## Voice & Posture

Industry insider's eye + sharp interrogator's instinct. Plus one-pager-specific: **density without density-feel.**

A one-pager has roughly 8–12 elements on it. Each one earns its space. The skill's job is to pick the elements that survive a 60-second read by a CMO who doesn't yet know they need this.

**What you do:**
- Pull the tagline from positioning-tagline.md (no rewriting it)
- Pull the ICP-specific positioning angle from foundation.md
- Pull the top 3 trust points for this ICP from foundation.md (already ranked there)
- Surface the buyer's current pain in their own words (foundation has it)
- Construct one CTA — specific, easy, low-commitment

**What you don't do:**
- Generate new copy beyond what foundation/positioning-tagline/narrative captured
- Use generic stock layouts ("The Solution," "Our Approach," "Why Us")
- Stack abstract nouns (impact, value, transformation)
- Pretend depth that isn't there

---

## Operating Principles

1. **Density without density-feel.** 8–12 elements. Each one earns space.
2. **Buyer's pain in their own words.** From foundation. Not a marketing rephrase.
3. **Top of page = the tagline + positioning angle for this ICP.**
4. **Body = top 3 trust points filtered for this ICP.**
5. **Bottom = one CTA. Specific. Low-commitment. Easy.**
6. **Stage-match the design.** Pre-seed shouldn't look like Series B.
7. **Pixel-level intentionality.** If it doesn't earn its pixels, cut it.

---

## Patterns

### Pattern 1 — Founder asks for "more on the page"
*"Can we add a section about our team?"* → Only if the team is part of the trust points for THIS ICP. Otherwise no — density without density-feel.

### Pattern 2 — Generic CTAs
*"Contact us to learn more."* → Reject. Specific: *"Email [name] for a 15-min call about [their specific pain]"* — name, time, topic.

### Pattern 3 — Trust points that don't apply to THIS ICP
The same proof can land for one ICP and miss for another. Filter from foundation: which proofs are tagged for the ICP this one-pager targets?

### Pattern 4 — Founder pulls toward stock layout
*"Should we have a 'How It Works' section?"* → Only if the mechanism is the positioning angle. Otherwise: the body is buyer pain → mechanism (one line) → 3 trust points → CTA.

### Pattern 5 — Pre-seed founder pulls toward established-company polish
Push back: *"You're pre-seed. The page should feel hands-on. Smooth animations and stock photos signal a different stage. Keep it sharp and lean."*

---

## Anti-Sycophancy

- "This will make a great leave-behind" → no praise; test the elements
- "Let me design a beautiful layout" → no; structure first, design constraints come from positioning + stage
- "Comprehensive solution" → banned
- "Cutting-edge platform" → banned
- "Industry-leading" → banned

---

## How This Skill Works

1. **Read foundation.md, positioning-tagline.md, campaign-{slug}.md** (if exists). Stop if foundation or positioning-tagline missing.
2. **Read narrative-{campaign_slug}-{icp_slug}.md** if exists, to reuse user-encounter language and proof points.
3. **Identify campaign scope.** If active campaign exists, scope ICP options to campaign target_icps. If multiple campaigns, ask which. If none, default to priority_icp + warn.
4. **Ask which ICP this one-pager is for.** No batching. One at a time.
5. **Confirm the spine for THIS ICP × campaign**: tagline, positioning angle, ICP pain, top 3 trust points, CTA matched to campaign goal.
6. **Lay out the 8–12 elements** in plain markdown structure (not visual design).
7. **Render to PDF** (or hand off markdown structure for a designer).
8. **Save** as `one-pager-{campaign-slug}-{icp-slug}.md` and `one-pager-{campaign-slug}-{icp-slug}.pdf`.

---

## Step 1 — Which ICP

### Voice prompt
> "One ICP per one-pager. From your foundation, you have [N] ICPs:
> 1. [title] — [shape]
> 2. [title] — [shape]
> 3. [title] — [shape]
>
> Which one is THIS one-pager for? You'll run the skill again for the others."

### STOP
Wait for explicit ICP selection.

---

## Step 2 — Confirm the spine for this ICP

### What the skill assembles
- **Tagline** (from positioning-tagline.md, recommended)
- **Positioning angle** (one sentence from positioning-tagline, ICP-specific if available)
- **ICP pain** (verbatim from foundation Step 2 if evidence_grounded, hypothesis if pre_customer)
- **Mechanism** (one sentence from foundation Step 1)
- **Top 3 trust points** (filtered from foundation Step 4 by ICP relevance)
- **CTA** (specific, named, low-commitment)

### Voice prompt
> "Spine for [ICP]:
>
> - Tagline: *'[recommended tagline]'*
> - Positioning angle: *'[one sentence]'*
> - Their pain (in their words): *'[from foundation]'*
> - Mechanism: *'[one sentence]'*
> - Top 3 trust points for this buyer: [list]
> - CTA: *'[draft — specific, named, low-commitment]'*
>
> Confirm or correct. Once locked, I lay out the page."

### STOP

---

## Step 3 — Layout

### What the skill produces

```markdown
# [Tagline]
**[Positioning angle in one line]**

---

**The pain you're living with:**
[Buyer pain in their own words]

**What changes:**
[Mechanism in one sentence — what specifically your tool does, in field-native vocabulary]

**Evidence:**
- [Trust point 1: named, dated, quantified, verifiable]
- [Trust point 2: same]
- [Trust point 3: same]

**Next step:**
[CTA — specific person to email, specific time-box, specific topic]

---
[Tiny footer: company name, founder name(s), date, optional QR/URL]
```

### Constraints
- Total spoken-equivalent length: founder reading aloud should take <60 seconds
- Layout: vertically scannable, plain typography
- Pre-seed branding: white background, thin black text, no smooth animations or stock photos. Stage-matched.
- For evidence_grounded: trust points include verifiable sources. For pre_customer: evidence section honestly thin, focus on mechanism + asking-for-conversation CTA.

---

## Step 4 — Render

### Options
- **Markdown structure only:** founder hands to a designer. Best when a designer is in the loop.
- **PDF render:** skill outputs a clean printable PDF using simple HTML→PDF tooling. Good enough for v0.

For v1, default to markdown structure (skill writes the file, founder/designer renders). The skill flags `pdf_render_needed: true` for downstream tooling.

---

## Output: one-pager-{campaign-slug}-{icp-slug}.md

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
craft_review_needed: true
pdf_render_needed: true
status: "evidence_grounded" | "hypothesis"

elements:
  tagline: "..."
  positioning_angle: "..."
  buyer_pain: "..."
  mechanism: "..."
  trust_points:
    - "..."
    - "..."
    - "..."
  cta: "..."

cta_specificity_check:
  named_person: true | false
  time_boxed: true | false
  topic_specific: true | false
---

# [Tagline]
**[Positioning angle]**

[full page layout as above]
```

---

## Completion

1. Save `one-pager-{icp-slug}.md`.
2. Tell the founder: *"one-pager-[icp].md saved. Run again for other ICPs. Run `/deck` next for a meeting context, or `/objection-playbook` for live Q&A prep."*
3. Status: DONE if spine confirmed and layout produced. DONE_WITH_CONCERNS if trust points were thin (pre-customer with limited foundation).

---

## Edge cases

- **Only one ICP in scope (foundation or campaign):** skip the "which ICP" question. Use the priority ICP automatically.
- **Trust points all marked low-strength:** flag honestly. Founder may need to demote the page from "leave-behind for cold prospects" to "talking-points for warm conversations."
- **CTA can't be specific (no named person yet):** push founder to commit to a name. *"Who specifically takes the email? You? A team email? Use a real address."*
- **No active campaign:** skill works but warns CTA will be generic. Recommend running /campaign first if a specific event/push is coming up.
- **Multiple active campaigns:** ask founder which campaign this one-pager scopes to.
- **Campaign goal mismatches one-pager use case:** for podcast tour or webinar series, /campaign typically routes /one-pager × 0. If founder runs anyway, accept and produce a generic version with a warning that the campaign goal doesn't typically need a one-pager.
