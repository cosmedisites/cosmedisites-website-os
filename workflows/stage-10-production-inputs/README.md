# STAGE 10 — PRODUCTION INPUTS

<!-- GENERATED from ops/stages.yaml by scripts/build.py. Do not edit by hand. -->

> This is the stage card: what you need to work this stage. Day-to-day status lives in the
> operational tool (Chirply). This card and the files it links to are the source.

| Status | Owner | Reviewer | Client involved | Deadline |
|---|---|---|---|---|
| *set per project* | Project Lead / Content Lead | Project Lead | Yes | *set per project* |

Status values: Not Started · In Progress · Blocked · Ready for Review · Complete · N/A.

## Objective

Get every approved content, evidence and technical input into a verified state before full production/build depends on it.

## Inputs

- Master Project Context for this project (in the project's Drive folder)
- [AI Operating Rules](../00-ai-operating-rules.md)
- Approved page system
- Content gaps
- Proof gaps
- Build requirements
- New inputs
- Existing tracker
- Proof Inventory

## Run

Route: **10A → 10B/10C → 10D**

- **[10A — Input Tracker Generator](prompts.md#10a--input-tracker-generator)** — After strategy approval. → *Populated Content/Input Tracker.*
- **[10B — Missing Inputs Follow-Up](prompts.md#10b--missing-inputs-follow-up)** — When client inputs are overdue or incomplete. → *Client-facing follow-up prioritised by blockage.* `CLIENT-FACING`
- **[10C — Input Verification](prompts.md#10c--input-verification)** — When client sends a batch of information/assets. → *Verification and tracker update instructions.*

## Validate

- **[10D — Build Readiness Gate](prompts.md#10d--build-readiness-gate)** — Before development begins in full. → *PASS/FAIL/BLOCKED build-readiness report.*

## Output

**Content & Input Tracker**

- Template 13 — [Content / Input Tracker](../../templates/content-input-tracker.md)
- Project Tracker tab(s): Content Inputs ([structure](../../templates/operational-tracker.md))

## Definition of Done

*Source: SOP, Stage 10 — Production Inputs*

- [ ] Every required input has an owner.
- [ ] Every input has a status.
- [ ] Pending items have a deadline.
- [ ] Received information is verified before publication.

**Also required before moving stage:**

- [ ] 10D Build Readiness Gate returns PASS *(Workflow Index step 7)*

> Never move to the next stage because the previous one feels approximately finished.
> Move when its Definition of Done has been met, or an authorised exception is recorded.

## Approval

- Approval required: **No**
- Gate: Internal gate

## Method

- SOP: [Stage 10 — Production Inputs](../../sop/website-redesign-sop.md#stage-10--production-inputs)

## Next

[Stage 11 — Build](../stage-11-build/README.md)
