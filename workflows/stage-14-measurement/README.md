# STAGE 14 — 30 / 60 / 90 MEASUREMENT

<!-- GENERATED from ops/stages.yaml by scripts/build.py. Do not edit by hand. -->

> This is the stage card: what you need to work this stage. Day-to-day status lives in the
> operational tool (Chirply). This card and the files it links to are the source.

| Status | Owner | Reviewer | Client involved | Deadline |
|---|---|---|---|---|
| *set per project* | Strategist / Project Lead | Project Lead | Review as needed | *set per project* |

Status values: Not Started · In Progress · Blocked · Ready for Review · Complete · N/A.

## Objective

Use live behaviour and commercial/search data to decide what to keep, improve, test or scale after launch.

## Inputs

- Master Project Context for this project (in the project's Drive folder)
- [AI Operating Rules](../00-ai-operating-rules.md)
- Baseline
- Analytics
- Search data
- Issues
- Client feedback
- 30-day review
- Behavioural data
- 30/60 reviews
- Commercial and search data
- Review findings
- Strategy, launch baseline, post-launch results

## Run

Route: **14A → 14B → 14C → 14D → 14E**

- **[14A — 30-Day Review](prompts.md#14a--30-day-review)** *(day 30)* — At 30 days post-launch. → *30-day implementation review.*
- **[14B — 60-Day Review](prompts.md#14b--60-day-review)** *(day 60)* — At 60 days post-launch. → *60-day behaviour/content review.*
- **[14C — 90-Day Commercial / Search Review](prompts.md#14c--90-day-commercial--search-review)** *(day 90)* — At 90 days post-launch. → *90-day performance review.*
- **[14D — KEEP / IMPROVE / TEST / SCALE](prompts.md#14d--keep--improve--test--scale)** — After 60 or 90-day analysis. → *Action plan.*
- **[14E — Learning / Case Study Capture](prompts.md#14e--learning--case-study-capture)** — After the 90-day review. → *Internal learning record and optional case-study outline.*

## Validate

The AI Workflow Pack has no Stage 14 validator. The 14D decisions are reviewed by the Project Lead.

## Output

**90-Day Redesign Performance Review**

- Template 17 — [30 / 60 / 90 Day Review](../../templates/30-60-90-review.md)
- Project Tracker tab(s): Measurement ([structure](../../templates/operational-tracker.md))

## Definition of Done

*Source: SOP, Stage 14 — 30 / 60 / 90 Day Review*

- [ ] 30/60/90 reviews use the launch baseline.
- [ ] Actions are prioritised by commercial impact.
- [ ] At least one KEEP / IMPROVE / TEST / SCALE decision is recorded.
- [ ] Reusable learning is fed back into the playbook.

**Also required before moving stage:**

- [ ] Reusable learning logged as GitHub Issues (IMPROVEMENT / TEST) *(SOP Stage 14 ("Feed reusable learning back into the operating system"))*

> Never move to the next stage because the previous one feels approximately finished.
> Move when its Definition of Done has been met, or an authorised exception is recorded.

## Approval

- Approval required: **No**
- Gate: Internal / client review

## Method

- SOP: [Stage 14 — 30 / 60 / 90 Day Review](../../sop/website-redesign-sop.md#stage-14--30--60--90-day-review)
- Playbook: [24. Post-Launch Learning](../../playbook/website-strategy-playbook.md#24-post-launch-learning)
- Playbook: [15. Business Outcomes](../../playbook/website-strategy-playbook.md#15-business-outcomes)

## Handoffs and client communication

- [C09 — 30/60/90 Review Summary](../../prompts/client-communications/client-communication-prompts.md#c09--306090-review-summary)

## Next

End of workflow. Log reusable learning from 14E as GitHub Issues.
