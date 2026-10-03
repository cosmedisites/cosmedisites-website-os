# STAGE 02 — STRATEGIC DIAGNOSIS

<!-- GENERATED from ops/stages.yaml by scripts/build.py. Do not edit by hand. -->

> This is the stage card: what you need to work this stage. Day-to-day status lives in the
> operational tool (Chirply); this card and the files it links to are the source.

| Status | Owner | Reviewer | Deadline |
|---|---|---|---|
| *set per project* | Strategist *(default role)* | Project Lead *(default role)* | *set per project* |

## Objective

Turn evidence into a prioritised explanation of what is suppressing the business outcome, without jumping prematurely to visual solutions.

## Inputs

- Master Project Context for this project (in the project's Drive folder)
- [AI Operating Rules](../00-ai-operating-rules.md)
- Project Strategy Brief
- Evidence Pack
- Strategic Diagnosis

## Run

Route: **2A → 2B → 2C**

- **[2A — Evidence → Strategic Diagnosis](prompts.md#2a--evidence--strategic-diagnosis)** — Once the Evidence Pack is complete. → *Draft Strategic Diagnosis.*
- **[2B — Priority Stack](prompts.md#2b--priority-stack)** — When the diagnosis contains too many issues. → *Prioritised issue stack.*

## Validate

- **[2C — Strategic Diagnosis Red Team](prompts.md#2c--strategic-diagnosis-red-team)** — Before moving to positioning. → *Red-team report.*

## Output

**Strategic Diagnosis**

- Template 03 — [Strategic Diagnosis](../../templates/strategic-diagnosis.md)

## Definition of Done

> **Interim.** This list is compiled from this stage's validator prompt(s) in the AI Workflow
> Pack v1.0. The Website Redesign SOP v1.0 Definition of Done is authoritative. Reconcile
> it when the SOP is imported ([sop/](../../sop/website-redesign-sop.md)).

- [ ] Current and desired perception stated
- [ ] Every weakness has evidence, consequence, priority and confidence
- [ ] Issues prioritised P0–P3 (2B)
- [ ] Diagnosis stated in one sentence
- [ ] Diagnosis could not be pasted unchanged onto another clinic
- [ ] No visual prescriptions (colour, type, UI styling)
- [ ] Red team (2C) returns PASS

Do not move stage until every item passes, or an authorised exception is recorded.

## Approval

- Gate: **Internal**
- Internal sign-off only

## Next

[Stage 03 — Positioning](../stage-03-positioning/README.md)
