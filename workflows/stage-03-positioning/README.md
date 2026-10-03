# STAGE 03 — POSITIONING

<!-- GENERATED from ops/stages.yaml by scripts/build.py. Do not edit by hand. -->

> This is the stage card: what you need to work this stage. Day-to-day status lives in the
> operational tool (Chirply). This card and the files it links to are the source.

| Status | Owner | Reviewer | Client involved | Deadline |
|---|---|---|---|---|
| *set per project* | Strategist | Creative Lead / Project Lead | Strategic approval | *set per project* |

Status values: Not Started · In Progress · Blocked · Ready for Review · Complete · N/A.

## Objective

Define the market perception, brand architecture and strategic ideas the new website must make obvious.

## Inputs

- Master Project Context for this project (in the project's Drive folder)
- [AI Operating Rules](../00-ai-operating-rules.md)
- Project Strategy Brief
- Evidence Pack
- Strategic Diagnosis
- Candidate directions
- Positioning Thesis
- Growth model
- Current team
- Service ownership

## Run

Route: **3A → 3B + 3C → 3D → 3E**

- **[3A — Generate Positioning Directions](prompts.md#3a--generate-positioning-directions)** — After Strategic Diagnosis is approved internally. → *Up to 3 evidence-based positioning directions.*
- **[3B — Select and Sharpen Positioning](prompts.md#3b--select-and-sharpen-positioning)** — When candidate directions exist. → *Recommended Positioning Thesis.*
- **[3C — Brand Architecture](prompts.md#3c--brand-architecture)** — When the business has founders, multiple practitioners, locations or expansion plans. → *Brand architecture rules.*
- **[3E — Client-Facing Positioning Explanation](prompts.md#3e--client-facing-positioning-explanation)** — When preparing the client deck or strategy review. → *Client-facing explanation.* `CLIENT-FACING`

## Validate

- **[3D — Positioning Validator](prompts.md#3d--positioning-validator)** — Before client-facing positioning approval. → *PASS/FAIL validation.*

## Output

**Positioning Thesis**

- Template 04 — [Positioning Thesis](../../templates/positioning-thesis.md)

## Definition of Done

*Source: SOP, Stage 3 — Positioning*

- [ ] Desired perception written.
- [ ] Wrong perception written.
- [ ] Positioning thesis agreed internally.
- [ ] Priority services/categories identified.
- [ ] Clinic/practitioner relationship defined.
- [ ] Future growth test passed.

**Also required before moving stage:**

- [ ] No visual design begins until this is internally approved. *(SOP Stage 3)*
- [ ] 3D validator returns PASS *(Workflow Index step 7)*
- [ ] Client strategic approval recorded in the Approval Record *(SOP Stage 3 / Tracker)*
- [ ] Approved positioning added to LOCKED DECISIONS in the Master Project Context *(Deployment Guide (Version control))*

> Never move to the next stage because the previous one feels approximately finished.
> Move when its Definition of Done has been met, or an authorised exception is recorded.

## Approval

- Approval required: **Yes**
- Gate: Client strategic approval
- On approval, lock: **Positioning**. Add it to LOCKED DECISIONS in the Master Project Context.

## Method

- SOP: [Stage 3 — Positioning](../../sop/website-redesign-sop.md#stage-3--positioning)
- Playbook: [4. Positioning Thesis](../../playbook/website-strategy-playbook.md#4-positioning-thesis)
- Playbook: [11. Brand Architecture](../../playbook/website-strategy-playbook.md#11-brand-architecture)

## Handoffs and client communication

- [H02 — Strategist → SEO Lead](../../prompts/team-handoffs/role-handoff-prompts.md#h02--strategist--seo-lead)
- [H03 — Strategist → Designer](../../prompts/team-handoffs/role-handoff-prompts.md#h03--strategist--designer)

## Next

[Stage 04 — IA + SEO](../stage-04-ia-seo/README.md)
