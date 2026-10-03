# STAGE 14 — 30 / 60 / 90 MEASUREMENT

<!-- GENERATED from ops/stages.yaml by scripts/build.py. Do not edit by hand. -->

> This is the stage card: what you need to work this stage. Day-to-day status lives in the
> operational tool (Chirply); this card and the files it links to are the source.

| Status | Owner | Reviewer | Deadline |
|---|---|---|---|
| *set per project* | Strategist *(default role)* | Project Lead *(default role)* | *set per project* |

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

**Post-launch review + learning**

- Template 17 — [30/60/90 Day Review](../../templates/30-60-90-review.md)

## Definition of Done

> **Interim.** This list is compiled from this stage's validator prompt(s) in the AI Workflow
> Pack v1.0. The Website Redesign SOP v1.0 Definition of Done is authoritative. Reconcile
> it when the SOP is imported ([sop/](../../sop/website-redesign-sop.md)).

- [ ] 30-day review complete
- [ ] 60-day review complete
- [ ] 90-day review complete
- [ ] KEEP / IMPROVE / TEST / SCALE plan agreed
- [ ] Learning captured (14E); OS improvement issues logged in GitHub

Do not move stage until every item passes, or an authorised exception is recorded.

## Approval

- Gate: **Internal / client review**
- Internal sign-off only

## Handoffs and client communication

- [C09 — 30/60/90 Review Summary](../../prompts/client-communications/client-communication-prompts.md#c09--306090-review-summary)

## Next

End of workflow. Log OS improvements found in 14E as GitHub Issues.
