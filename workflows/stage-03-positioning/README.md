# STAGE 03 — POSITIONING

<!-- GENERATED from ops/stages.yaml by scripts/build.py. Do not edit by hand. -->

> This is the stage card: what you need to work this stage. Day-to-day status lives in the
> operational tool (Chirply); this card and the files it links to are the source.

| Status | Owner | Reviewer | Deadline |
|---|---|---|---|
| *set per project* | Strategist *(default role)* | Project Lead *(default role)* | *set per project* |

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

**Positioning Thesis + Brand Architecture**

- Template 04 — [Positioning Thesis](../../templates/positioning-thesis.md)

## Definition of Done

> **Interim.** This list is compiled from this stage's validator prompt(s) in the AI Workflow
> Pack v1.0. The Website Redesign SOP v1.0 Definition of Done is authoritative. Reconcile
> it when the SOP is imported ([sop/](../../sop/website-redesign-sop.md)).

- [ ] Three-second perception
- [ ] Wrong perception
- [ ] Positioning thesis (25 words or fewer)
- [ ] Priority services
- [ ] Brand architecture
- [ ] 3D validator returns PASS on every test
- [ ] Client strategic approval recorded
- [ ] Positioning added to LOCKED DECISIONS in the Master Project Context

Do not move stage until every item passes, or an authorised exception is recorded.

## Approval

- Gate: **Client strategic approval**
- Required: client approval
- On approval, lock: **Positioning** (add to LOCKED DECISIONS in the Master Project Context)

## Handoffs and client communication

- [H02 — Strategist → SEO Lead](../../prompts/team-handoffs/role-handoff-prompts.md#h02--strategist--seo-lead)
- [H03 — Strategist → Designer](../../prompts/team-handoffs/role-handoff-prompts.md#h03--strategist--designer)

## Next

[Stage 04 — IA + SEO](../stage-04-ia-seo/README.md)
