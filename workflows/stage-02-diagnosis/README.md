# STAGE 02 — STRATEGIC DIAGNOSIS

<!-- GENERATED from ops/stages.yaml by scripts/build.py. Do not edit by hand. -->

> This is the stage card: what you need to work this stage. Day-to-day status lives in the
> operational tool (Chirply). This card and the files it links to are the source.

| Status | Owner | Reviewer | Client involved | Deadline |
|---|---|---|---|---|
| *set per project* | Strategist | Project Lead | No | *set per project* |

Status values: Not Started · In Progress · Blocked · Ready for Review · Complete · N/A.

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

*Source: SOP, Stage 2 — Strategic Diagnosis*

- [ ] Diagnosis can be understood without discussing colours/fonts.
- [ ] Commercial, trust, UX and scalability issues are separated.
- [ ] Top three opportunities are prioritised.
- [ ] Every major conclusion traces back to evidence.

**Also required before moving stage:**

- [ ] 2C red team returns PASS *(Workflow Index step 7)*

> Never move to the next stage because the previous one feels approximately finished.
> Move when its Definition of Done has been met, or an authorised exception is recorded.

## Approval

- Approval required: **No**
- Gate: Internal

## Method

- SOP: [Stage 2 — Strategic Diagnosis](../../sop/website-redesign-sop.md#stage-2--strategic-diagnosis)
- Playbook: [2. Rule Zero: Diagnose Before Designing](../../playbook/website-strategy-playbook.md#2-rule-zero-diagnose-before-designing)

## Next

[Stage 03 — Positioning](../stage-03-positioning/README.md)
