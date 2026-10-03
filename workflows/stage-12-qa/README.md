# STAGE 12 — QA

<!-- GENERATED from ops/stages.yaml by scripts/build.py. Do not edit by hand. -->

> This is the stage card: what you need to work this stage. Day-to-day status lives in the
> operational tool (Chirply). This card and the files it links to are the source.

| Status | Owner | Reviewer | Client involved | Deadline |
|---|---|---|---|---|
| *set per project* | Named QA owners (see gates) | Independent reviewers | No | *set per project* |

Status values: Not Started · In Progress · Blocked · Ready for Review · Complete · N/A.

## Objective

Run separate regulated-content, strategy/UX and technical/SEO sign-offs so one type of QA cannot hide another.

## Inputs

- Master Project Context for this project (in the project's Drive folder)
- [AI Operating Rules](../00-ai-operating-rules.md)
- Staging content
- Proof Inventory
- Compliance constraints
- Consent records
- Staging site
- Positioning Thesis
- IA
- Approved deck/screens
- Sitemap
- Redirect map
- Tracking plan

## Run

Route: **12A + 12B + 12C → 12D → 12E**

- **[12A — Compliance QA](prompts.md#12a--compliance-qa)** *(Compliance gate)* — Before launch candidate approval. → *Compliance QA report.*
- **[12B — Strategy / UX QA](prompts.md#12b--strategy--ux-qa)** *(Strategy / UX gate)* — Before launch. → *Strategy/UX QA report.*
- **[12C — Technical / SEO QA](prompts.md#12c--technical--seo-qa)** *(Technical / SEO gate)* — Before launch. → *Technical/SEO QA report.*

## Validate

- **[12D — Consolidated QA Triage](prompts.md#12d--consolidated-qa-triage)** — When the three QA streams are complete. → *Single prioritised launch issue list.*
- **[12E — Launch Blocker Decision](prompts.md#12e--launch-blocker-decision)** *(only if launching with open P0/P1 items)* — When someone wants to launch with open QA items. → *GO/NO-GO decision memo.*

## Output

**Compliance + Strategy + Technical QA sign-off**

- Template 15 — [Compliance + Launch QA](../../templates/compliance-launch-qa.md)
- QA gate — [Compliance Review](../../qa/compliance.md) *(owner: Compliance Reviewer)*
- QA gate — [Strategy / UX QA](../../qa/strategy-ux.md) *(owner: Independent QA Reviewer)*
- QA gate — [Technical / SEO QA](../../qa/technical-seo.md) *(owner: Developer + SEO Lead)*
- Project Tracker tab(s): QA ([structure](../../templates/operational-tracker.md))

## Definition of Done

*Source: SOP v1.0, Stage 12 — Compliance + Strategy + Technical QA*

- [ ] Compliance gate signed off.
- [ ] Strategy/UX gate signed off.
- [ ] Technical/SEO gate signed off.
- [ ] Blocking issues resolved or explicitly accepted.

**Also required before moving stage:**

- [ ] 12D consolidated triage complete; any open P0 has a 12E GO / CONDITIONAL GO decision recorded with owner and rollback trigger *(Workflow Index step 7 / prompts 12D–12E)*

> Never move to the next stage because the previous one feels approximately finished.
> Move when its Definition of Done has been met, or an authorised exception is recorded.

## Approval

- Approval required: **Internal sign-off**
- Gate: Internal sign-off

## Method

- SOP: [Stage 12 — Compliance + Strategy + Technical QA](../../sop/website-redesign-sop.md#stage-12--compliance--strategy--technical-qa)
- Playbook: [20. Compliance as a Dedicated Gate](../../playbook/website-strategy-playbook.md#20-compliance-as-a-dedicated-gate)
- Playbook: [23. Internal Quality Test](../../playbook/website-strategy-playbook.md#23-internal-quality-test)

## Handoffs and client communication

- [H07 — QA → Project Lead](../../prompts/team-handoffs/role-handoff-prompts.md#h07--qa--project-lead)
- [C07 — Pre-Launch Approval Request](../../prompts/client-communications/client-communication-prompts.md#c07--pre-launch-approval-request)

## Next

[Stage 13 — Launch](../stage-13-launch/README.md)
