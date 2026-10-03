# Stage 12 — Compliance + Strategy + Technical QA

**Purpose:** Run separate regulated-content, strategy/UX and technical/SEO sign-offs so one type of QA cannot hide another.

## 12A — Compliance QA

**Use when:** Before launch candidate approval.  
**Inputs:** Staging content; Proof Inventory; compliance constraints; consent records.  
**Produces:** Compliance QA report.

```text
Run the CosmediSites compliance content review.

Check each relevant page for:
- unsupported claims;
- inaccurate practitioner titles;
- qualification / registration presentation;
- treatment terminology;
- before/after presentation;
- patient consent;
- testimonial wording/source;
- promotional superlatives;
- pricing / offer claims;
- guarantees / outcome language;
- safety / pain / downtime claims;
- clinical reviewer attribution.

For every issue record:
URL
COPY / COMPONENT
ISSUE
EVIDENCE / RULE SOURCE if supplied
SEVERITY: BLOCKER / HIGH / MEDIUM / LOW
FIX REQUIRED
OWNER

If no jurisdiction-specific rule has been supplied, do not invent legal advice. Mark the item for appropriate human/compliance review.
```

## 12B — Strategy / UX QA

**Use when:** Before launch.  
**Inputs:** Staging site; Positioning Thesis; IA; approved deck/screens.  
**Produces:** Strategy/UX QA report.

```text
Audit the staging site against the approved strategy, not just against Figma.

Check:
- three-second perception;
- wrong-category avoidance;
- trust visible early enough;
- priority services visible;
- patient discovery routes;
- clinic vs practitioner hierarchy;
- proof quality;
- CTA clarity;
- booking friction;
- mobile hierarchy;
- results/reviews presentation;
- scalability;
- approved brand ideas visible without repetition becoming forced.

For each return:
PASS / FIX / NOT TESTABLE
Evidence
Impact
Required fix

Then run the 60-second test:
What kind of clinic/business is this?
What makes it different?
What should a user do next?
What makes it credible?
How does a user find the right service?
Does it feel specific to this client?
```

## 12C — Technical / SEO QA

**Use when:** Before launch.  
**Inputs:** Staging site; sitemap; redirect map; tracking plan.  
**Produces:** Technical/SEO QA report.

```text
Run the technical / SEO launch QA using supplied technical evidence.

Check where testable:
- correct production URLs;
- indexability directives;
- canonicals;
- title/meta fields;
- headings;
- XML sitemap;
- robots;
- redirects / chains;
- internal links;
- broken links;
- schema based on real content;
- images / alt treatment where relevant;
- performance / Core Web Vitals evidence if supplied;
- mobile rendering;
- forms;
- booking links;
- analytics / conversions;
- consent/cookie implementation;
- 404 behaviour.

For each issue:
URL / scope
Check
Status
Severity
Fix
Owner
Retest required

Do not mark an item PASS if it was not actually tested; use NOT TESTED.
```

## 12D — Consolidated QA Triage

**Use when:** When the three QA streams are complete.  
**Inputs:** Compliance QA; Strategy/UX QA; Technical/SEO QA.  
**Produces:** Single prioritised launch issue list.

```text
Combine the three QA reports without losing the source gate.

Prioritise:
P0 LAUNCH BLOCKER
P1 FIX BEFORE LAUNCH
P2 FIX IMMEDIATELY AFTER LAUNCH IF NECESSARY
P3 BACKLOG / POLISH

For each item include:
Source gate
Issue
Impact
Owner
Fix status
Retest owner

Resolve duplicates but preserve the strictest severity.

Finish:
Total P0
Total P1
Outstanding compliance blockers
Outstanding technical blockers
Outstanding strategy/UX blockers
Recommended launch status: GO / NO-GO / CONDITIONAL
```

## 12E — Launch Blocker Decision

**Use when:** When someone wants to launch with open QA items.  
**Inputs:** Consolidated QA list; deadline/business context.  
**Produces:** GO/NO-GO decision memo.

```text
Assess whether the site should launch with the remaining open issues.

For each unresolved P0/P1 item state:
Impact if we launch
Impact if we delay
Workaround
Rollback/recovery difficulty
Compliance/search/data risk

Then choose:
GO
NO-GO
CONDITIONAL GO

A deadline alone is not a reason to downgrade a compliance, tracking, migration or critical conversion blocker.

If CONDITIONAL GO, state:
- exact conditions;
- owner;
- deadline;
- rollback trigger.
```

