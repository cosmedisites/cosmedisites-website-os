# QA Gate — Technical / SEO QA

> One of the three separate Stage 12 checks. **Treat these as three separate checks** (SOP Stage 12),
> so one type of QA cannot hide another.

| | |
|---|---|
| Owner | **Developer + SEO Lead** (SOP Stage 12 C) |
| Run with | Prompt [12C](../workflows/stage-12-qa/prompts.md) → [12D Consolidated QA Triage](../workflows/stage-12-qa/prompts.md) |
| Record in | Project Tracker **QA** tab (Google Sheet in the project Drive folder) and [Template 15](../templates/compliance-launch-qa.md) |
| Status values | Not Checked · Pass · Fix · N/A (Tracker v1.0) |
| Method | [Playbook 21. SEO Architecture Before Final Design](../playbook/website-strategy-playbook.md#21-seo-architecture-before-final-design) |

## Rules

- Never mark an item Pass unless it was actually tested. (Prompt 12C: use NOT TESTED)
- Check redirects against the Stage 04 migration map (prompt 4D).

## Checks (SOP Stage 12, verbatim)

| Check | Owner | Status | Issue / fix | Sign-off / date |
|---|---|---|---|---|
| Indexability | | Not Checked | | |
| Metadata | | Not Checked | | |
| Canonicals | | Not Checked | | |
| Redirects | | Not Checked | | |
| Schema | | Not Checked | | |
| Internal links | | Not Checked | | |
| Performance | | Not Checked | | |
| Forms | | Not Checked | | |
| Tracking | | Not Checked | | |
| Responsive behaviour | | Not Checked | | |
| Broken links | | Not Checked | | |
| Consent/cookie implementation where applicable | | Not Checked | | |

> The prompt checks more detail than this list. Record extra findings in the issue/fix column against the closest SOP check.

## Gate sign-off

- [ ] Every check is Pass or N/A, or the Fix is explicitly accepted (SOP Stage 12 DoD: "Blocking issues resolved or explicitly accepted")
- Signed off by:
- Date:
