# STAGE 13 — LAUNCH

<!-- GENERATED from ops/stages.yaml by scripts/build.py. Do not edit by hand. -->

> This is the stage card: what you need to work this stage. Day-to-day status lives in the
> operational tool (Chirply). This card and the files it links to are the source.

| Status | Owner | Reviewer | Client involved | Deadline |
|---|---|---|---|---|
| *set per project* | Project Lead (technical owner: Developer) | Developer / SEO | Client informed | *set per project* |

Status values: Not Started · In Progress · Blocked · Ready for Review · Complete · N/A.

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

**Launch Record + Measurement Baseline**

- Template 16 — [Post-Launch Measurement Baseline](../../templates/measurement-baseline.md)
- Project Tracker tab(s): Measurement ([structure](../../templates/operational-tracker.md))

## Definition of Done

*Source: SOP, Stage 13 — Launch*

- [ ] Launch date and comparison period are recorded.
- [ ] Commercial conversion baseline exists where tracking permits.
- [ ] Priority search and landing-page baseline exists.
- [ ] Known tracking limitations are documented.

**Also required before moving stage:**

- [ ] Launch only after QA sign-off. *(SOP Stage 13)*
- [ ] Launch completed; tracking verified; baseline captured. *(Tracker (Stage Tracker))*

> Never move to the next stage because the previous one feels approximately finished.
> Move when its Definition of Done has been met, or an authorised exception is recorded.

## Approval

- Approval required: **Launch sign-off**
- Gate: Launch sign-off

## Method

- SOP: [Stage 13 — Launch](../../sop/website-redesign-sop.md#stage-13--launch)
- Playbook: [15. Business Outcomes](../../playbook/website-strategy-playbook.md#15-business-outcomes)

## Handoffs and client communication

- [C08 — Launch Notification](../../prompts/client-communications/client-communication-prompts.md#c08--launch-notification)

## Next

[Stage 14 — 30 / 60 / 90 Measurement](../stage-14-measurement/README.md)
