# Role Handoff Prompts

Every handoff must separate LOCKED / REQUIRED / FLEXIBLE / OPEN / DO NOT CHANGE.
Designer-facing handoffs (H03, and prompt 5C) use LOCKED / FLEXIBLE / REQUIRED / AVOID / OPEN (AI Operating Rules §10).

## H01 — Project Lead → Strategist

**Use when:** At the named role transition.  
**Inputs:** Current artefacts and Master Project Context.  
**Produces:** Role-specific handoff.

```text
Create the strategist handoff from onboarding.

Include:
LOCKED — signed scope, commercial commitments, dates, explicit client constraints.
REQUIRED — questions the strategy must answer.
FLEXIBLE — areas not yet decided.
OPEN — facts still missing.
DO NOT CHANGE — promises/scope boundaries that require project-lead approval.

Also include:
client objective;
key stakeholders;
main sensitivities;
access/data available;
known previous decisions.
```

## H02 — Strategist → SEO Lead

**Use when:** At the named role transition.  
**Inputs:** Current artefacts and Master Project Context.  
**Produces:** Role-specific handoff.

```text
Create the strategist-to-SEO handoff.

Include:
commercial objective;
priority services/categories;
approved positioning;
desired user journeys;
growth model;
clinic/practitioner/location architecture;
current search concerns;
pages/services that must be protected;
known SEO data gaps.

Separate:
LOCKED
REQUIRED
FLEXIBLE
OPEN
DO NOT CHANGE

The SEO lead should be able to build the sitemap/URL plan without re-deriving the business strategy.
```

## H03 — Strategist → Designer

**Use when:** At the named role transition.  
**Inputs:** Current artefacts and Master Project Context.  
**Produces:** Role-specific handoff.

```text
Create the strategist-to-designer handoff.

Include:
positioning thesis;
three-second perception;
wrong perception;
priority patient journeys;
priority services;
clinic/practitioner hierarchy;
distinctive brand ideas;
trust/proof that must appear;
CTA hierarchy;
photography direction;
search/architecture constraints that affect design;
content gaps (from the 7B Content Gap Plan where available).

Separate:
LOCKED — approved decisions; changing them needs explicit re-approval
FLEXIBLE — where design judgement is encouraged
REQUIRED — what the design must include or solve
AVOID — patterns, signals and treatments the design must not use: the wrong perception,
  what the design must not signal (3B), wrong-category cues, fabricated or placeholder
  proof presented as real
OPEN — unresolved items, each with owner and next action

Do not prescribe visual details that are genuinely the designer’s job.
```

## H04 — SEO Lead → Designer

**Use when:** At the named role transition.  
**Inputs:** Current artefacts and Master Project Context.  
**Produces:** Role-specific handoff.

```text
Create the SEO-to-designer handoff.

Only include SEO requirements that materially affect UX/layout:
navigation hierarchy;
page types;
 breadcrumb requirements;
internal-link modules;
 treatment/concern relationships;
 practitioner/location relationships;
 required editable fields;
 content depth/section needs;
 migration constraints relevant to slugs/links.

Separate:
MUST SUPPORT
SHOULD SUPPORT
FLEXIBLE
OPEN

Do not dump an SEO audit onto the designer.
```

## H05 — Designer → Developer

**Use when:** At the named role transition.  
**Inputs:** Current artefacts and Master Project Context.  
**Produces:** Role-specific handoff.

```text
Create the designer-to-developer handoff using the approved component/page system.

Separate:
LOCKED
REQUIRED
FLEXIBLE
OPEN
DO NOT CHANGE

Include:
design version;
responsive behaviour;
component states;
navigation;
forms;
image ratios;
animations;
empty/error states;
accessibility/semantic notes;
known content variability.

Highlight any component that must support future practitioners, treatments, locations or results.
```

## H06 — Content Lead → Compliance Reviewer

**Use when:** At the named role transition.  
**Inputs:** Current artefacts and Master Project Context.  
**Produces:** Role-specific handoff.

```text
Create the content-to-compliance handoff.

Include:
pages/copy requiring review;
new or changed claims;
practitioner titles/credentials;
treatment claims;
before/after usage;
testimonials;
pricing/promotions;
results/outcomes language;
proof sources;
consent status;
open questions.

For each claim, link to or identify the proof source.
Do not ask the compliance reviewer to infer where claims came from.
```

## H07 — QA → Project Lead

**Use when:** At the named role transition.  
**Inputs:** Current artefacts and Master Project Context.  
**Produces:** Role-specific handoff.

```text
Create the QA-to-project-lead handoff.

Summarise:
P0 blockers;
P1 before-launch issues;
P2 post-launch issues;
compliance status;
strategy/UX status;
technical/SEO status;
items waiting on client;
items waiting on team;
recommended launch status.

Separate implementation defects from new client preferences.
State exactly what must be true before GO.
```

## H08 — Project Lead → Client

**Use when:** At the named role transition.  
**Inputs:** Current artefacts and Master Project Context.  
**Produces:** Role-specific handoff.

```text
Translate the current internal project state into a concise client update.

Include:
what is complete;
what is currently happening;
what decisions/inputs are needed from the client;
what is blocked, if anything;
what happens next;
dates if confirmed.

Do not expose internal jargon, uncertainty that does not affect the client, or team debate.
Do not hide a material blocker.
```

