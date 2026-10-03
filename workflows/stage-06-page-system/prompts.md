# Stage 6 — Page + Component System

**Purpose:** Create reusable page and component patterns that scale across treatments, concerns, practitioners, locations and future growth.

## 6A — Homepage Architecture

**Use when:** After IA and visual direction are approved.  
**Inputs:** Positioning Thesis; sitemap; proof inventory; visual principles.  
**Produces:** Homepage section architecture.

```text
Build the homepage architecture before writing detailed copy.

For each section output:
SECTION NAME
JOB
PRIMARY MESSAGE
PROOF / CONTENT REQUIRED
PRIMARY CTA
LINKS TO
MOBILE NOTE
WHY IT EXISTS

Order sections by:
1. Immediate understanding
2. Trust
3. Discovery
4. Differentiation
5. Proof
6. Conversion

The homepage must:
- communicate the three-second perception quickly;
- expose enough proof early;
- let users browse by the way they think;
- surface priority commercial categories;
- reinforce the clinic brand;
- make the primary CTA obvious.

Do not turn the homepage into a complete treatment catalogue.
```

## 6B — Page Template Generator

**Use when:** When defining treatment, concern, practitioner, result and other core templates.  
**Inputs:** Approved IA; Brand Architecture; proof requirements.  
**Produces:** Reusable page-template specifications.

```text
Define reusable templates for the requested page types.

For each template provide:
PAGE JOB
WHO ARRIVES HERE
PRIMARY QUESTION TO ANSWER
REQUIRED SECTIONS IN ORDER
OPTIONAL SECTIONS
PROOF REQUIRED
INTERNAL LINKS
PRIMARY CTA
SECONDARY CTA
SEO / CONTENT NOTES
MOBILE BEHAVIOUR
EMPTY-STATE RULES

Page types may include:
Treatment / service
Concern
Practitioner
Result / case
Location
About / team
Booking / contact

Rules:
- Each page type must have a distinct job.
- Do not create a universal template with headings swapped.
- Respect clinic vs practitioner ownership.
- Hide optional sections when there is no real content.
```

## 6C — Component Library Specification

**Use when:** Once page templates are known.  
**Inputs:** Page templates; visual system.  
**Produces:** Component inventory and rules.

```text
Create the reusable component library required by the approved page system.

For each component state:
NAME
PURPOSE
USED ON
REQUIRED FIELDS
OPTIONAL FIELDS
VARIANTS
INTERACTION
MOBILE BEHAVIOUR
EMPTY / MISSING DATA BEHAVIOUR
ACCESSIBILITY / SEMANTIC NOTE

Consider:
Hero
Evidence strip
Treatment card
Concern card
Practitioner card
Result/case module
Review/testimonial
Facts/pricing block
FAQ
CTA block
Author/reviewer
Related content
Location/contact
Mega-menu / navigation

Avoid components that exist only because a single mockup needed decoration.
```

## 6D — Mobile Adaptation

**Use when:** Before approving page systems.  
**Inputs:** Desktop page architecture / mockups; conversion priorities.  
**Produces:** Mobile UX specification.

```text
Translate the approved page system to mobile deliberately.

For each key page/component define:
- what appears first;
- what can collapse;
- what must never be hidden;
- CTA position;
- sticky actions if appropriate;
- image crop / ratio;
- text size / density principle;
- card stacking;
- table / evidence behaviour;
- form behaviour.

Specifically check:
Hero
Primary navigation
Treatment discovery
Trust / proof
Practitioner cards
Before / after
Forms
Final CTA

Do not merely say “stack vertically”.
Explain the mobile decision and its conversion consequence.
```

## 6E — Scalability Validator

**Use when:** Before Stage 6 is marked complete.  
**Inputs:** Page templates; component library; growth model.  
**Produces:** Scalability QA.

```text
Stress-test the design system against future growth.

Simulate:
- 2 additional practitioners;
- 10 additional treatments;
- a second location;
- a new high-priority category;
- missing photography on one practitioner;
- a treatment with no results yet;
- a practitioner with extensive media / article content.

For each scenario answer:
Does the current system accommodate it?
What changes?
Does the clinic/practitioner hierarchy remain intact?
Does navigation still work?
Does mobile still work?

Return:
PASS
NEEDS COMPONENT VARIANT
REQUIRES ARCHITECTURE CHANGE

Any scenario requiring a new design concept for routine growth is a Stage 6 warning.
```

