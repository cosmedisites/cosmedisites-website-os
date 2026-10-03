# STAGE 07 — PROOF + CONTENT + PHOTOGRAPHY

<!-- GENERATED from ops/stages.yaml by scripts/build.py. Do not edit by hand. -->

> This is the stage card: what you need to work this stage. Day-to-day status lives in the
> operational tool (Chirply); this card and the files it links to are the source.

| Status | Owner | Reviewer | Deadline |
|---|---|---|---|
| *set per project* | Content Lead *(default role)* | Compliance Reviewer *(default role)* | *set per project* |

## Objective

Build the evidence, content and image inputs needed to make the strategy believable without fabricating authority.

## Inputs

- Master Project Context for this project (in the project's Drive folder)
- [AI Operating Rules](../00-ai-operating-rules.md)
- Existing client materials
- Site
- Reviews
- Credentials
- Result assets
- Page templates
- Proof Inventory
- Current copy
- Visual Direction
- Page System
- Current photography
- Clinic details

## Run

Route: **7A + 7B + 7C → 7D + 7E**

- **[7A — Proof Inventory Builder](prompts.md#7a--proof-inventory-builder)** — Once positioning and page needs are clear. → *Structured Proof Inventory.*
- **[7B — Content Gap Plan](prompts.md#7b--content-gap-plan)** — When page templates are known but content is incomplete. → *Prioritised content gap list.*
- **[7C — Photography Brief Generator](prompts.md#7c--photography-brief-generator)** — Before photography is booked or final design is populated. → *Shoot brief and shot list.*
- **[7E — Client Input Request Generator](prompts.md#7e--client-input-request-generator)** — When content/proof/photography gaps need client action. → *Prioritised client input request.* `CLIENT-FACING`

## Validate

- **[7D — Claims + Content Evidence Validator](prompts.md#7d--claims--content-evidence-validator)** — Before client copy enters design/build. → *Claim validation report.*

## Output

**Proof Inventory + Photography Brief + content gaps**

- Template 09 — [Proof Inventory](../../templates/proof-inventory.md)
- Template 10 — [Photography Brief](../../templates/photography-brief.md)

## Definition of Done

> **Interim.** This list is compiled from this stage's validator prompt(s) in the AI Workflow
> Pack v1.0. The Website Redesign SOP v1.0 Definition of Done is authoritative. Reconcile
> it when the SOP is imported ([sop/](../../sop/website-redesign-sop.md)).

- [ ] Proof Inventory built, with verification and consent status on every item
- [ ] Content gap plan prioritised P0–P3
- [ ] Photography brief and shot list complete
- [ ] Claims validated (7D); no UNSUPPORTED claim remains in client copy
- [ ] Client input request sent (7E)

Do not move stage until every item passes, or an authorised exception is recorded.

## Approval

- Gate: **Client supplies inputs**
- Client must supply inputs; no strategic sign-off at this stage

## Handoffs and client communication

- [H06 — Content Lead → Compliance Reviewer](../../prompts/team-handoffs/role-handoff-prompts.md#h06--content-lead--compliance-reviewer)
- [C05 — Content / Photography Request](../../prompts/client-communications/client-communication-prompts.md#c05--content--photography-request)

## Next

[Stage 08 — Client Strategy Review](../stage-08-client-review/README.md)
