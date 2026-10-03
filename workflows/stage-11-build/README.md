# STAGE 11 — BUILD

<!-- GENERATED from ops/stages.yaml by scripts/build.py. Do not edit by hand. -->

> This is the stage card: what you need to work this stage. Day-to-day status lives in the
> operational tool (Chirply); this card and the files it links to are the source.

| Status | Owner | Reviewer | Deadline |
|---|---|---|---|
| *set per project* | Developer *(default role)* | Designer *(default role)* | *set per project* |

## Objective

Translate approved strategy, design, content and SEO requirements into an implementation package with minimal ambiguity.

## Inputs

- Master Project Context for this project (in the project's Drive folder)
- [AI Operating Rules](../00-ai-operating-rules.md)
- Approved screens
- Component system
- Visual tokens
- Mobile behaviour
- Approved sitemap
- URL map
- Redirects
- Schema/content requirements
- Tracking
- Approved page copy
- Page templates
- Input tracker

## Run

Route: **11A + 11B + 11C → 11D**

- **[11A — Designer → Developer Handoff](prompts.md#11a--designer--developer-handoff)** — Immediately before development starts. → *Developer handoff.*
- **[11B — SEO → Developer Handoff](prompts.md#11b--seo--developer-handoff)** — Before build or migration implementation. → *SEO implementation handoff.*
- **[11C — Content → Build Mapping](prompts.md#11c--content--build-mapping)** — When approved copy/content needs mapping to templates. → *Page/content implementation map.*

## Validate

- **[11D — Build Implementation Validator](prompts.md#11d--build-implementation-validator)** — During staging before formal QA. → *Implementation variance report.*

## Output

**Build Handoff + implementation variance**

- Template 14 — [Build Handoff](../../templates/build-handoff.md)

## Definition of Done

> **Interim.** This list is compiled from this stage's validator prompt(s) in the AI Workflow
> Pack v1.0. The Website Redesign SOP v1.0 Definition of Done is authoritative. Reconcile
> it when the SOP is imported ([sop/](../../sop/website-redesign-sop.md)).

- [ ] Designer → Developer handoff complete, with no material UX decision left to the developer
- [ ] SEO → Developer handoff complete, with every MUST item addressed
- [ ] Content mapped to templates without factual changes
- [ ] 11D shows no outstanding CRITICAL variance

Do not move stage until every item passes, or an authorised exception is recorded.

## Approval

- Gate: **Internal**
- Internal sign-off only

## Handoffs and client communication

- [H05 — Designer → Developer](../../prompts/team-handoffs/role-handoff-prompts.md#h05--designer--developer)

## Next

[Stage 12 — QA](../stage-12-qa/README.md)
