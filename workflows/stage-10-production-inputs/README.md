# STAGE 10 — PRODUCTION INPUTS

<!-- GENERATED from ops/stages.yaml by scripts/build.py. Do not edit by hand. -->

> This is the stage card: what you need to work this stage. Day-to-day status lives in the
> operational tool (Chirply); this card and the files it links to are the source.

| Status | Owner | Reviewer | Deadline |
|---|---|---|---|
| *set per project* | Project Lead *(default role)* | Strategist *(default role)* | *set per project* |

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

**Content / Input Tracker + build readiness**

- Template 13 — [Content / Input Tracker](../../templates/content-input-tracker.md)

## Definition of Done

> **Interim.** This list is compiled from this stage's validator prompt(s) in the AI Workflow
> Pack v1.0. The Website Redesign SOP v1.0 Definition of Done is authoritative. Reconcile
> it when the SOP is imported ([sop/](../../sop/website-redesign-sop.md)).

- [ ] Strategic approvals recorded
- [ ] Required screens approved
- [ ] Mobile states defined
- [ ] Sitemap / URL map approved
- [ ] Redirect requirements known
- [ ] Primary copy approved or clearly owned
- [ ] Practitioner facts verified
- [ ] Proof required by the design is available
- [ ] Photography final, or placeholders explicitly controlled
- [ ] Booking / contact details known
- [ ] Tracking requirements known
- [ ] Compliance-critical unknowns resolved
- [ ] Open items have owners and do not block build
- [ ] 10D Build Readiness Gate returns PASS

Do not move stage until every item passes, or an authorised exception is recorded.

## Approval

- Gate: **Internal gate**
- Internal sign-off only

## Next

[Stage 11 — Build](../stage-11-build/README.md)
