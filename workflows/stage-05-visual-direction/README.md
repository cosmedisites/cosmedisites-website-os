# STAGE 05 — VISUAL DIRECTION

<!-- GENERATED from ops/stages.yaml by scripts/build.py. Do not edit by hand. -->

> This is the stage card: what you need to work this stage. Day-to-day status lives in the
> operational tool (Chirply); this card and the files it links to are the source.

| Status | Owner | Reviewer | Deadline |
|---|---|---|---|
| *set per project* | Designer *(default role)* | Strategist *(default role)* | *set per project* |

## Objective

Translate approved positioning into a coherent, defensible visual system without allowing aesthetic preference to rewrite strategy.

## Inputs

- Master Project Context for this project (in the project's Drive folder)
- [AI Operating Rules](../00-ai-operating-rules.md)
- Positioning Thesis
- Strategic Diagnosis
- Current → Proposed
- Brand assets
- Current-site evidence
- Approved visual principles
- Master Project Context
- IA
- Visual principles

## Run

Route: **5A → 5B + 5C → 5D**

- **[5A — Strategy → Visual Principles](prompts.md#5a--strategy--visual-principles)** — Before the designer produces the style direction. → *Visual principles brief.*
- **[5B — Current → Proposed Generator](prompts.md#5b--current--proposed-generator)** — When preparing the visual direction or client deck. → *Client-friendly comparison table.*
- **[5C — Designer Execution Prompt](prompts.md#5c--designer-execution-prompt)** — When handing approved strategy to a designer or design model. → *Design brief for homepage + system exploration.*

## Validate

- **[5D — Visual Direction Validator](prompts.md#5d--visual-direction-validator)** — Before client visual approval. → *Visual strategy QA.*

## Output

**Visual Direction**

- Template 07 — [Visual Direction](../../templates/visual-direction.md)
- Template 05 — [Current → Proposed Summary](../../templates/current-proposed-summary.md)

## Definition of Done

> **Interim.** This list is compiled from this stage's validator prompt(s) in the AI Workflow
> Pack v1.0. The Website Redesign SOP v1.0 Definition of Done is authoritative. Reconcile
> it when the SOP is imported ([sop/](../../sop/website-redesign-sop.md)).

- [ ] Every visual principle traces back to positioning or user behaviour
- [ ] Current → Proposed comparison complete
- [ ] Desired category perception achieved; wrong category avoided
- [ ] No Level 5 visual choice undermines a Level 1–4 decision
- [ ] No placeholder mistaken for proof
- [ ] 5D validator returns PASS
- [ ] Client approval recorded

Do not move stage until every item passes, or an authorised exception is recorded.

## Approval

- Gate: **Client approval**
- Required: client approval

## Next

[Stage 06 — Page + Component System](../stage-06-page-system/README.md)
