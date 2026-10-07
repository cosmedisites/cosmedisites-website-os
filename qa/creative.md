# QA Gate: Creative QA (12F)

> The fourth separate Stage 12 check, added in v1.1. **Treat these as separate checks** (SOP Stage 12),
> so one type of QA cannot hide another.

| | |
|---|---|
| Owner | **Independent reviewer who did not design the site** (SOP Stage 12 F) |
| Run with | Stage [05T](../workflows/stage-05t-creative-translation/README.md) keyframes and [05V](../workflows/stage-05v-creative-validation/README.md) validation record, then [12D Consolidated QA Triage](../workflows/stage-12-qa/prompts.md) |
| Record in | Project Tracker **QA** tab (Google Sheet in the project Drive folder) |
| Status values | Not Checked · Pass · Fix · N/A (Tracker) |

## Rules

- Audit the built staging site against the approved 05T keyframes, not against a Figma file or a template.
- The reviewer must not be the person who designed or built the site.

## Checks (SOP Stage 12 F)

| Check | Owner | Status | Issue / fix | Sign-off / date |
|---|---|---|---|---|
| Brand Swap Test still passes on the built site | | Not Checked | | |
| Built pages match the approved keyframes without flattening | | Not Checked | | |
| Real assets in place; no placeholder dictating layout | | Not Checked | | |
| Motion performant, pausable, respects reduced-motion | | Not Checked | | |
| High-value pages kept their bespoke moments | | Not Checked | | |
