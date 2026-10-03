# STAGE 13 — LAUNCH

<!-- GENERATED from ops/stages.yaml by scripts/build.py. Do not edit by hand. -->

> This is the stage card: what you need to work this stage. Day-to-day status lives in the
> operational tool (Chirply); this card and the files it links to are the source.

| Status | Owner | Reviewer | Deadline |
|---|---|---|---|
| *set per project* | Developer *(default role)* | Project Lead *(default role)* | *set per project* |

## Objective

Launch in a controlled way, verify acquisition/measurement systems and capture the baseline required for post-launch learning.

## Inputs

- Master Project Context for this project (in the project's Drive folder)
- [AI Operating Rules](../00-ai-operating-rules.md)
- QA report
- Technical handoff
- Launch date
- Hosting/domain context
- Approved Launch Plan
- Analytics/GSC/GBP/booking/call data available
- Issue reports
- Analytics
- QA
- Client feedback

## Run

Route: **13A → 13B → 13C + 13D; 13E as needed**

- **[13A — Launch Plan](prompts.md#13a--launch-plan)** — Once QA is near complete. → *Launch plan.*
- **[13B — Launch-Day Runbook](prompts.md#13b--launch-day-runbook)** — On launch day. → *Tick-box launch sequence.*
- **[13C — Client Launch Notification](prompts.md#13c--client-launch-notification)** — After launch checks pass. → *Client launch email.* `CLIENT-FACING`
- **[13D — Measurement Baseline Capture](prompts.md#13d--measurement-baseline-capture)** — At or immediately before launch. → *Baseline record matching Template 16.*
- **[13E — Post-Launch Issue Triage](prompts.md#13e--post-launch-issue-triage)** *(first 7 days)* — During the first 7 days. → *Prioritised post-launch issue list.*

## Validate

The AI Workflow Pack has no Stage 13 validator. The 13B runbook's PASS/FAIL fields are the check.

## Output

**Launch runbook + baseline**

- Template 16 — [Post-Launch Measurement Baseline](../../templates/measurement-baseline.md)

## Definition of Done

> **Interim.** This list is compiled from this stage's validator prompt(s) in the AI Workflow
> Pack v1.0. The Website Redesign SOP v1.0 Definition of Done is authoritative. Reconcile
> it when the SOP is imported ([sop/](../../sop/website-redesign-sop.md)).

- [ ] Launch plan approved
- [ ] Runbook executed, with a PASS / FAIL recorded for every step
- [ ] Measurement baseline captured, with gaps recorded as gaps
- [ ] Client launch notification sent
- [ ] 30 / 60 / 90-day reviews scheduled

Do not move stage until every item passes, or an authorised exception is recorded.

## Approval

- Gate: **Launch sign-off**
- Internal sign-off only

## Handoffs and client communication

- [C08 — Launch Notification](../../prompts/client-communications/client-communication-prompts.md#c08--launch-notification)

## Next

[Stage 14 — 30 / 60 / 90 Measurement](../stage-14-measurement/README.md)
