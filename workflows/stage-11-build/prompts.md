# Stage 11 — Build

**Purpose:** Translate approved strategy, design, content and SEO requirements into an implementation package with minimal ambiguity.

## 11A — Designer → Developer Handoff

**Use when:** Immediately before development starts.  
**Inputs:** Approved screens; component system; visual tokens; mobile behaviour.  
**Produces:** Developer handoff.

```text
Create the designer-to-developer handoff.

Separate into:
LOCKED
REQUIRED
FLEXIBLE
OPEN
DO NOT CHANGE

Document:
- approved screen/version links;
- component list;
- responsive behaviour;
- typography and colour tokens;
- spacing principles;
- button states;
- navigation behaviour;
- form interactions;
- image ratios/crops;
- empty states;
- loading/error states where relevant;
- accessibility/semantic notes;
- animation rules.

For each OPEN item state:
Owner
Deadline
Whether build can proceed without it

Do not leave material UX decisions for the developer to invent.
```

## 11B — SEO → Developer Handoff

**Use when:** Before build or migration implementation.  
**Inputs:** Approved sitemap; URL map; redirects; schema/content requirements; tracking.  
**Produces:** SEO implementation handoff.

```text
Create the SEO-to-developer implementation handoff.

Include:

URLS
- approved URL structure;
- URLs that must not change;
- old → new redirect map;
- canonical rules.

CRAWL / INDEXATION
- indexable page types;
- noindex / utility pages;
- robots / sitemap requirements if project-specific.

ON-PAGE / STRUCTURE
- heading/template constraints;
- editable metadata fields;
- breadcrumb requirements;
- internal-link modules;
- practitioner/author relationships.

STRUCTURED DATA
- schema types required where supported by real content;
- data dependencies;
- do not invent fields merely to satisfy schema.

TRACKING
- analytics;
- forms;
- booking;
- calls;
- consent requirements.

QA
- launch tests.

Mark every item:
MUST
SHOULD
N/A
OPEN
```

## 11C — Content → Build Mapping

**Use when:** When approved copy/content needs mapping to templates.  
**Inputs:** Approved page copy; page templates; input tracker.  
**Produces:** Page/content implementation map.

```text
Map approved content to the build.

For each page:
URL
PAGE TEMPLATE
H1 / HERO COPY
PRIMARY CTA
SECTION ORDER
CONTENT SOURCE
PROOF COMPONENTS
PRACTITIONER / REVIEWER
RESULTS / REVIEWS
FAQ
RELATED LINKS
SEO NOTES
OPEN ITEMS

Rules:
- Do not make factual copy changes during mapping.
- Flag copy that no longer fits the approved component rather than truncating away meaning.
- Ensure optional components disappear cleanly when no verified content exists.
```

## 11D — Build Implementation Validator

**Use when:** During staging before formal QA.  
**Inputs:** Staging site/screens; approved designs; handoffs.  
**Produces:** Implementation variance report.

```text
Compare the staging build against approved design, UX, SEO and content requirements.

Classify variances:
CRITICAL — changes strategy, conversion, compliance, URL/search behaviour or core UX.
MAJOR — visibly undermines approved design/system.
MINOR — polish.
ACCEPTABLE VARIATION — technically necessary or equivalent implementation.

Check:
- hierarchy;
- CTAs;
- navigation;
- responsive behaviour;
- evidence/proof placement;
- content accuracy;
- image crops;
- component consistency;
- URLs;
- internal links;
- metadata/editability;
- performance-impacting implementation where visible.

Output:
Page/component
Variance
Classification
Approved reference
Required fix
Owner
```

