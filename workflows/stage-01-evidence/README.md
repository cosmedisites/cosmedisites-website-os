# STAGE 01 — EVIDENCE

<!-- GENERATED from ops/stages.yaml by scripts/build.py. Do not edit by hand. -->

> This is the stage card: what you need to work this stage. Day-to-day status lives in the
> operational tool (Chirply). This card and the files it links to are the source.

| Status | Owner | Reviewer | Client involved | Deadline |
|---|---|---|---|---|
| *set per project* | Strategist | Project Lead | No | *set per project* |

Status values: Not Started · In Progress · Blocked · Ready for Review · Complete · N/A.

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

*Source: SOP v1.0, Stage 1 — Evidence Pack*

- [ ] Website reviewed.
- [ ] Mobile reviewed.
- [ ] Competitors reviewed.
- [ ] Existing assets classified.
- [ ] Revenue-driving services identified.
- [ ] Growth priorities identified.
- [ ] Proof inventory started.
- [ ] Key unknowns identified.
- [ ] Strategic diagnosis drafted.

**Also required before moving stage:**

- [ ] Diagnostic sentence written: “The existing site currently communicates X. The business needs to become Y. The primary barriers are A, B and C.” *(SOP Stage 1)*
- [ ] 1D validator returns PASS *(Workflow Index step 7)*

> Never move to the next stage because the previous one feels approximately finished.
> Move when its Definition of Done has been met, or an authorised exception is recorded.

## Approval

- Approval required: **No**
- Gate: Internal

## Method

- SOP: [Stage 1 — Evidence Pack](../../sop/website-redesign-sop.md#stage-1--evidence-pack)
- Playbook: [3. Evidence Before Preference](../../playbook/website-strategy-playbook.md#3-evidence-before-preference)

## Next

[Stage 02 — Strategic Diagnosis](../stage-02-diagnosis/README.md)
