# STAGE 11 — BUILD

<!-- GENERATED from ops/stages.yaml by scripts/build.py. Do not edit by hand. -->

> This is the stage card: what you need to work this stage. Day-to-day status lives in the
> operational tool (Chirply). This card and the files it links to are the source.

| Status | Owner | Reviewer | Client involved | Deadline |
|---|---|---|---|---|
| *set per project* | Developer | Designer | No | *set per project* |

Status values: Not Started · In Progress · Blocked · Ready for Review · Complete · N/A.

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

**Implemented build**

- Template 14 — [Build Handoff](../../templates/build-handoff.md)

## Definition of Done

*Source: SOP, Stage 11 — Build*

- [ ] Developer is implementing approved decisions.
- [ ] Material UX decisions are not being invented during development.
- [ ] Desktop/mobile states are implemented.
- [ ] SEO/migration requirements are implemented.
- [ ] Tracking requirements are implemented.

**Also required before moving stage:**

- [ ] 11D shows no outstanding CRITICAL variance *(Workflow Index step 7 / prompt 11D)*

> Never move to the next stage because the previous one feels approximately finished.
> Move when its Definition of Done has been met, or an authorised exception is recorded.

## Approval

- Approval required: **No**
- Gate: Internal

## Method

- SOP: [Stage 11 — Build](../../sop/website-redesign-sop.md#stage-11--build)
- Playbook: [22. Build Handoff](../../playbook/website-strategy-playbook.md#22-build-handoff)

## Handoffs and client communication

- [H05 — Designer → Developer](../../prompts/team-handoffs/role-handoff-prompts.md#h05--designer--developer)

## Next

[Stage 12 — QA](../stage-12-qa/README.md)
