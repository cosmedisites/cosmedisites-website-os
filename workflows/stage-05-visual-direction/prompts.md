# Stage 5 — Visual Direction

**Purpose:** Translate approved positioning into a coherent, defensible visual system without allowing aesthetic preference to rewrite strategy.

## 5A — Strategy → Visual Principles

**Use when:** Before the designer produces the style direction.  
**Inputs:** Positioning Thesis; Strategic Diagnosis; Current → Proposed; brand assets.  
**Produces:** Visual principles brief.

```text
Translate the approved strategy into visual principles.

For each area define:
- what it needs to communicate;
- recommended visual behaviour;
- what to avoid;
- strategic reason.

Areas:
Palette / contrast
Typography
Spacing / density
Photography
Buttons / CTA hierarchy
Cards / containers
Iconography
Motion
Evidence / data presentation
Dark / light section use

Rules:
- Do not prescribe arbitrary pixel values unless required.
- Every recommendation must trace back to positioning or user behaviour.
- Preserve approved brand assets where the strategy says to preserve them.
- Distinguish category expectation from client-specific differentiation.
```

## 5B — Current → Proposed Generator

**Use when:** When preparing the visual direction or client deck.  
**Inputs:** Current-site evidence; approved visual principles.  
**Produces:** Client-friendly comparison table.

```text
Create a Current → Proposed comparison for the redesign.

Use these rows where relevant:
Brand perception
Colour / contrast
Typography
Photography
Navigation
Treatment / service discovery
Credibility / proof
CTA / booking
Practitioner positioning
Mobile experience

For each row:
CURRENT — factual, non-insulting description.
PROPOSED — concise strategic shift.
WHY — one clause linking the change to business/user outcome.

Avoid subjective phrases like “looks better” or “more premium” unless you explain what changes the perception.
```

## 5C — Designer Execution Prompt

**Use when:** When handing approved strategy to a designer or design model.  
**Inputs:** Master Project Context; Positioning Thesis; IA; visual principles.  
**Produces:** Design brief for homepage + system exploration.

```text
You are designing within an approved CosmediSites strategy.

First separate the brief into:

LOCKED
- business / positioning / architecture decisions that cannot be changed through styling.

FLEXIBLE
- areas where design judgement is encouraged.

REQUIRED
- content, proof, UX or conversion elements that must appear.

AVOID
- patterns, signals and treatments that would contradict the approved strategy, including
  wrong-category cues and placeholder proof presented as real.

OPEN
- unresolved content/assets that require labelled placeholders.

Then design the requested page/system.

Your output must explain:
1. Page hierarchy.
2. Visual hierarchy.
3. Primary and secondary CTA treatment.
4. Photography role and crop.
5. Evidence / trust placement.
6. Responsive behaviour.
7. How the design remains scalable.

Do not create fake credentials, ratings, patient results or practitioner identities to make the mockup look complete.
```

## 5D — Visual Direction Validator

**Use when:** Before client visual approval.  
**Inputs:** Visual direction / mockups; Positioning Thesis; IA.  
**Produces:** Visual strategy QA.

```text
Review the proposed visual direction against the approved strategy.

Score only as a diagnostic, not as client-facing ratings:
- desired category perception;
- wrong-category avoidance;
- clinical credibility;
- trust visibility;
- CTA clarity;
- photography fit;
- hierarchy;
- mobile plausibility;
- scalability;
- distinctiveness to this client.

Then answer:
- Which design choices directly support the positioning?
- Which are merely fashionable?
- What would make the site look like a generic template?
- Has any Level 5 visual choice undermined a Level 1–4 decision?
- Is any placeholder being mistaken for proof?

Return KEEP / CHANGE / OPEN.
Finish with PASS / FAIL / BLOCKED for Stage 5.
```

