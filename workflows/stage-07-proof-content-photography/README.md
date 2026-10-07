# STAGE 07 — PROOF + CONTENT + PHOTOGRAPHY

<!-- GENERATED from ops/stages.yaml by scripts/build.py. Do not edit by hand. -->

> This is the stage card: what you need to work this stage. Day-to-day status lives in the
> operational tool (Chirply). This card and the files it links to are the source.

| Status | Owner | Reviewer | Client involved | Deadline |
|---|---|---|---|---|
| *set per project* | Content Lead | Strategist / Compliance Reviewer | Client supplies inputs | *set per project* |

Status values: Not Started · In Progress · Blocked · Ready for Review · Complete · N/A.

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

**Proof Inventory + Content/Input Tracker + Photography Brief**

- Template 09 — [Proof Inventory](../../templates/proof-inventory.md)
- Template 13 — [Content / Input Tracker](../../templates/content-input-tracker.md)
- Template 10 — [Photography Brief](../../templates/photography-brief.md)
- Project Tracker tab(s): Proof Inventory, Content Inputs ([structure](../../templates/operational-tracker.md))

## Definition of Done

*Source: SOP v1.0, Stage 7 — Proof + Content + Photography*

- [ ] Proof gaps are known.
- [ ] Each missing input has an owner.
- [ ] Photography requirements are defined.
- [ ] Patient/model consent requirements are identified.
- [ ] Design does not depend on evidence nobody can supply.
- [ ] The shoot brief derives from the Stage 05 asset matrix; every SHOOT item has a date and owner; nothing marked DO NOT FAKE is substituted.

**Also required before moving stage:**

- [ ] 7D claims validator shows no UNSUPPORTED claim left in client copy *(Workflow Index step 7 / prompt 7D)*

> Never move to the next stage because the previous one feels approximately finished.
> Move when its Definition of Done has been met, or an authorised exception is recorded.

## Approval

- Approval required: **No**
- Gate: Client supplies inputs

## Method

- SOP: [Stage 7 — Proof + Content + Photography](../../sop/website-redesign-sop.md#stage-7--proof--content--photography)
- Playbook: [12. Trust & Proof System](../../playbook/website-strategy-playbook.md#12-trust--proof-system)
- Playbook: [13. Photography System](../../playbook/website-strategy-playbook.md#13-photography-system)

## Handoffs and client communication

- [H06 — Content Lead → Compliance Reviewer](../../prompts/team-handoffs/role-handoff-prompts.md#h06--content-lead--compliance-reviewer)
- [C05 — Content / Photography Request](../../prompts/client-communications/client-communication-prompts.md#c05--content--photography-request)

## Next

[Stage 08 — Client Strategy Review](../stage-08-client-review/README.md)
