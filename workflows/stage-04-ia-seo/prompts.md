# Stage 4 — Information Architecture + SEO

**Purpose:** Protect valuable search equity while structuring the site around patient intent, commercial priorities and future growth.

## 4A — Existing URL Preservation Audit

**Use when:** Before approving a new sitemap.  
**Inputs:** Existing URL export; GSC/analytics if available; current sitemap; links/rankings if supplied.  
**Produces:** Retain / improve / merge / remove / redirect inventory.

```text
Review the supplied current URL inventory before designing the new architecture.

For each URL classify:
RETAIN
IMPROVE
MERGE
REMOVE
REDIRECT
UNKNOWN

Record:
URL
Current page type
Observed / supplied search value
Commercial value
Content uniqueness
Proposed destination
Decision
Reason
Risk if changed
Confidence

Rules:
- Do not delete or consolidate solely because two pages look similar.
- Protect pages with demonstrated search, link or conversion value unless there is a strong reason not to.
- Mark missing performance data as OPEN rather than assuming no value.
- Identify high-risk migration URLs separately.
```

## 4B — Build Sitemap / IA

**Use when:** After positioning and URL preservation review.  
**Inputs:** Positioning Thesis; commercial priorities; user journeys; URL inventory.  
**Produces:** Proposed sitemap and navigation model.

```text
Build the proposed CosmediSites information architecture.

Design for three common user states where relevant:
1. “I know the treatment I want.”
2. “I know the problem I want solved.”
3. “I don’t know what I need yet.”

Define:
- primary navigation;
- treatment/service hierarchy;
- concern hierarchy;
- location structure;
- practitioner structure;
- results/case-study structure;
- about/trust content;
- supporting informational content;
- booking/contact route.

For every page include:
Proposed URL
Page purpose
Primary user intent
Commercial role
Parent
Primary CTA
Related page types
Existing URL mapping if applicable

Do not create pages solely to fill a sitemap.
Prevent obvious cannibalisation by giving each page a distinct job.
```

## 4C — Internal Linking + Ownership Rules

**Use when:** Once sitemap exists.  
**Inputs:** Approved sitemap; Brand Architecture.  
**Produces:** Internal-linking rules.

```text
Create the internal-linking model for the proposed site.

Define directional rules for:
- treatment → concern;
- concern → treatment;
- treatment → practitioner;
- practitioner → treatment;
- result/case → treatment;
- result/case → practitioner;
- informational article → commercial page;
- location → treatment;
- treatment → location where relevant.

For each rule state:
SOURCE PAGE TYPE
DESTINATION PAGE TYPE
WHY THE LINK EXISTS
ANCHOR / LABEL GUIDANCE
WHEN NOT TO LINK

Respect the approved brand architecture.
Do not fragment treatment ownership across practitioners if the clinic brand is meant to own treatments.
```

## 4D — Migration / Redirect Map

**Use when:** When URLs will change.  
**Inputs:** Existing URL inventory; approved sitemap.  
**Produces:** Redirect and migration map.

```text
Create a migration map.

For each changed or removed URL output:
OLD URL
STATUS / CURRENT ROLE
NEW URL
ACTION: 301 / retain / canonical / remove
REASON
CONTENT MERGE REQUIRED?
INTERNAL LINKS TO UPDATE?
RISK
QA CHECK

Flag:
- many-to-one redirects;
- homepage redirects;
- chains;
- high-value URLs;
- pages with no appropriate destination;
- parameter / trailing slash / protocol patterns if relevant.

Do not redirect unrelated retired pages to the homepage merely to avoid a 404.
```

## 4E — IA + SEO Validator

**Use when:** Before design locks navigation/page system.  
**Inputs:** Proposed sitemap; URL decisions; internal-link model; migration map.  
**Produces:** PASS/FAIL/BLOCKED IA report.

```text
Validate the proposed information architecture.

Check:
- every primary page has a distinct purpose;
- priority commercial services have appropriate landing pages;
- concern pages are genuinely useful rather than thin duplicates;
- practitioner pages fit the brand architecture;
- locations are structured consistently;
- valuable existing URLs are protected;
- removed URLs have sensible decisions;
- internal links support patient journeys;
- navigation is understandable without industry knowledge;
- future practitioners / treatments / locations can be added;
- obvious cannibalisation risks are identified;
- redirects are known before build.

Return PASS / FAIL / BLOCKED for each and list all launch-critical SEO risks.
```

