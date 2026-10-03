# STAGE 12 — QA

<!-- GENERATED from ops/stages.yaml by scripts/build.py. Do not edit by hand. -->

> This is the stage card: what you need to work this stage. Day-to-day status lives in the
> operational tool (Chirply); this card and the files it links to are the source.

| Status | Owner | Reviewer | Deadline |
|---|---|---|---|
| *set per project* | Project Lead *(default role)* | Compliance Reviewer *(default role)* | *set per project* |

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

**Compliance / Strategy / Technical QA**

- Template 15 — [Compliance + Launch QA](../../templates/compliance-launch-qa.md)
- QA gate — [Compliance QA](../../qa/compliance.md) *(owner: Compliance Reviewer)*
- QA gate — [Strategy / UX QA](../../qa/strategy-ux.md) *(owner: Strategist)*
- QA gate — [Technical / SEO QA](../../qa/technical-seo.md) *(owner: SEO Lead)*

## Definition of Done

> **Interim.** This list is compiled from this stage's validator prompt(s) in the AI Workflow
> Pack v1.0. The Website Redesign SOP v1.0 Definition of Done is authoritative. Reconcile
> it when the SOP is imported ([sop/](../../sop/website-redesign-sop.md)).

- [ ] Compliance gate signed off (qa/compliance.md)
- [ ] Strategy / UX gate signed off (qa/strategy-ux.md)
- [ ] Technical / SEO gate signed off (qa/technical-seo.md)
- [ ] Consolidated triage (12D) complete
- [ ] Zero P0 items, or a 12E GO / CONDITIONAL GO decision recorded with owner and rollback trigger
- [ ] Recommended launch status recorded

Do not move stage until every item passes, or an authorised exception is recorded.

## Approval

- Gate: **Internal sign-off**
- Internal sign-off only

## Handoffs and client communication

- [H07 — QA → Project Lead](../../prompts/team-handoffs/role-handoff-prompts.md#h07--qa--project-lead)
- [C07 — Pre-Launch Approval Request](../../prompts/client-communications/client-communication-prompts.md#c07--pre-launch-approval-request)

## Next

[Stage 13 — Launch](../stage-13-launch/README.md)
