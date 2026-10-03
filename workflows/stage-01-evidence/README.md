# STAGE 01 — EVIDENCE

<!-- GENERATED from ops/stages.yaml by scripts/build.py. Do not edit by hand. -->

> This is the stage card: what you need to work this stage. Day-to-day status lives in the
> operational tool (Chirply); this card and the files it links to are the source.

| Status | Owner | Reviewer | Deadline |
|---|---|---|---|
| *set per project* | Strategist *(default role)* | Project Lead *(default role)* | *set per project* |

## Objective

Build a factual picture of the current site, competitors and available performance evidence before prescribing solutions.

## Inputs

- Master Project Context for this project (in the project's Drive folder)
- [AI Operating Rules](../00-ai-operating-rules.md)
- Website/screenshots/analytics/search data
- Project Strategy Brief
- 3–5 competitors
- Current-site evidence
- Evidence notes
- Competitor matrix

## Run

Route: **1A + 1B → 1C → 1D**

- **[1A — Current Site Evidence Extraction](prompts.md#1a--current-site-evidence-extraction)** — At the start of the audit/evidence stage. → *Structured evidence notes.*
- **[1B — Competitor Evidence Comparison](prompts.md#1b--competitor-evidence-comparison)** — When competitor sites or screenshots are available. → *Competitor evidence matrix and opportunity gaps.*
- **[1C — KEEP / CHANGE / MISSING / UNCERTAIN](prompts.md#1c--keep--change--missing--uncertain)** — After current-site and competitor evidence has been collected. → *Evidence Pack core classification.*

## Validate

- **[1D — Evidence Pack Validator](prompts.md#1d--evidence-pack-validator)** — Before Stage 1 is complete. → *Validation report and missing evidence list.*

## Output

**Evidence Pack**

- Template 02 — [Evidence Pack](../../templates/evidence-pack.md)

## Definition of Done

> **Interim.** This list is compiled from this stage's validator prompt(s) in the AI Workflow
> Pack v1.0. The Website Redesign SOP v1.0 Definition of Done is authoritative. Reconcile
> it when the SOP is imported ([sop/](../../sop/website-redesign-sop.md)).

- [ ] Current desktop site reviewed
- [ ] Mobile reviewed
- [ ] Key page types reviewed
- [ ] Competitor set reviewed
- [ ] KEEP / CHANGE / MISSING / UNCERTAIN all used appropriately
- [ ] Main revenue services and growth priorities considered
- [ ] Proof inventory started
- [ ] Booking journey considered
- [ ] Brand architecture / future growth considered
- [ ] Evidence separated from inference
- [ ] Summary diagnosis supported by the evidence
- [ ] 1D validator returns PASS

Do not move stage until every item passes, or an authorised exception is recorded.

## Approval

- Gate: **Internal**
- Internal sign-off only

## Next

[Stage 02 — Strategic Diagnosis](../stage-02-diagnosis/README.md)
