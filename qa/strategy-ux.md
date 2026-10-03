# QA Gate — Strategy / UX QA

> One of the three separate Stage 12 checks. **Treat these as three separate checks** (SOP Stage 12),
> so one type of QA cannot hide another.

| | |
|---|---|
| Owner | **Independent QA Reviewer (SOP: "Independent reviewer")** (SOP Stage 12 B) |
| Run with | Prompt [12B](../workflows/stage-12-qa/prompts.md) → [12D Consolidated QA Triage](../workflows/stage-12-qa/prompts.md) |
| Record in | Project Tracker **QA** tab (Google Sheet in the project Drive folder) and [Template 15](../templates/compliance-launch-qa.md) |
| Status values | Not Checked · Pass · Fix · N/A (Tracker v1.0) |
| Method | [Playbook 23. Internal Quality Test](../playbook/website-strategy-playbook.md#23-internal-quality-test) |

## Rules

- Audit the staging site against the approved strategy, not just against Figma. (Prompt 12B)
- Run the 60-second internal quality test with someone who did not work deeply on the design. (Playbook §23)

## Checks (SOP Stage 12, verbatim)

| Check | Owner | Status | Issue / fix | Sign-off / date |
|---|---|---|---|---|
| Positioning survives implementation | | Not Checked | | |
| Trust appears early enough | | Not Checked | | |
| User journeys work | | Not Checked | | |
| Clinic/practitioner hierarchy is correct | | Not Checked | | |
| CTAs are clear | | Not Checked | | |
| Mobile experience works | | Not Checked | | |
| Future scalability remains intact | | Not Checked | | |

> The prompt checks more detail than this list. Record extra findings in the issue/fix column against the closest SOP check.

## Gate sign-off

- [ ] Every check is Pass or N/A, or the Fix is explicitly accepted (SOP Stage 12 DoD: "Blocking issues resolved or explicitly accepted")
- Signed off by:
- Date:
