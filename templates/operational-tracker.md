# Operational Tracker v1.0: structure

> Markdown specification of `CosmediSites_Redesign_Operational_Tracker_v1.0.xlsx`, generated from the
> workbook so its structure can be reviewed and versioned in Git. The workbook itself is a
> **GitHub Release asset**, not committed. To change the tracker, change the workbook, regenerate
> this page and open a PR.

## How the tracker is used with Chirply

One copy per project, as a **Google Sheet** in the project Drive folder (`00_Admin/`), linked from the Chirply deal.
To avoid keeping the same fact in two places, each tab has one live home:

| Tab | Live home when Chirply is the front end | Why |
|---|---|---|
| Lists | Sheet | Status vocabularies. Chirply uses the same values |
| Dashboard | **Chirply** (pipeline + weekly digest) | Retire in project copies, or keep as read-only |
| Stage Tracker | **Chirply** (deal stage + stage tasks) | Stage status is Chirply's job; the tab stays the reference for owners/DoD |
| Approvals | **Chirply** (Approval Record object, same columns) | Drives approval automations |
| Content Inputs | **Sheet** | Tabular; drives overdue reminders |
| Proof Inventory | **Sheet** | Tabular evidence log |
| QA | **Sheet** (check-level); Chirply holds gate sign-off | Tabular; three gates |
| Measurement | **Sheet** | Numbers over time |

If the Option B fallback is used, or for a small project run without Chirply, the whole workbook is used as designed.

## Lists

| Stage Status | Approval Status | Input Status | QA Status |
|---|---|---|---|
| Not Started | Pending | Not Requested | Not Checked |
| In Progress | Approved | Requested | Pass |
| Blocked | Changes Requested | Received | Fix |
| Ready for Review | Locked | Verified | N/A |
| Complete | N/A | N/A |  |
| N/A |  |  |  |

## Dashboard

- COSMEDISITES WEBSITE REDESIGN — PROJECT CONTROL
- Client · [[Client]] · KPI · Value
- Domain · [[Domain]] · Stages Complete · =COUNTIF('Stage Tracker'!G2:G16,"Complete")
- Project Lead · [[Name]] · Open Inputs · =COUNTIFS('Content Inputs'!E2:E200,"<>Verified",'Content Inputs'!E2:E200,"<>N/A",'Content Inputs'!A2:A200,"<>")
- Target Launch · [[Date]] · QA Fixes Open · =COUNTIF(QA!D2:D100,"Fix")
- Current Phase · [[Phase]]
- Operating rule: move stages only when Definition of Done is met.

## Stage Tracker

| Stage | Phase | Owner | Reviewer | Client Involved? | Definition of Done | Status | Approval Required? | Template / Artefact | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 0 | Project Strategy Brief | Project Lead / Strategist | Project Lead | Yes | Commercial objective, growth model, priorities, audience, constraints captured. | Not Started | Client factual confirmation | 01 Project Strategy Brief |  |
| 1 | Evidence Pack | Strategist | Project Lead | No | Site/mobile/competitors reviewed; KEEP/CHANGE/MISSING/UNCERTAIN complete; diagnosis written. | Not Started | No | 02 Evidence Pack |  |
| 2 | Strategic Diagnosis | Strategist | Project Lead | No | Commercial, trust, UX and scalability issues diagnosed without visual prescription. | Not Started | No | 03 Strategic Diagnosis |  |
| 3 | Positioning | Strategist | Creative / Project Lead | Yes | Three-second perception, wrong perception, thesis, priority services and brand architecture agreed. | Not Started | Yes | 04 Positioning Thesis |  |
| 4 | IA + SEO | SEO Lead / Strategist | Project Lead | Yes if structure changes | URLs, page purposes, hierarchy, internal linking and redirect requirements defined. | Not Started | Conditional | 06 Sitemap + SEO Architecture |  |
| 5 | Visual Direction | Designer | Strategist / Creative Lead | Yes | Visual system tied to positioning; desktop/mobile direction clear. | Not Started | Yes | 07 Visual Direction |  |
| 6 | Page + Component System | Designer / UX | Strategist | No | Core page templates and reusable components defined; responsive behaviour documented. | Not Started | Internal | 08 Page + Component System |  |
| 7 | Proof + Content + Photography | Content Lead | Strategist / Compliance | Client supplies inputs | Proof inventory, input tracker and shoot brief complete; gaps owned. | Not Started | No | 09 Proof + 10 Photography |  |
| 8 | Client Strategy Review | Project Lead | Strategist / Designer | Yes | Client deck presents one coherent direction and explicit decisions. | Not Started | Review meeting | 11 Client Strategy Deck |  |
| 9 | Approval Gate | Project Lead | — | Yes | Strategic decisions explicitly approved / changes logged / locks recorded. | Not Started | Yes | 12 Approval Record |  |
| 10 | Production Inputs | Content / Project Lead | Project Lead | Yes | Every required input has owner, status and deadline. | Not Started | No | 13 Content / Input Tracker |  |
| 11 | Build | Developer | Designer | No | Approved design, content, SEO and tracking requirements implemented. | Not Started | No | 14 Build Handoff |  |
| 12 | Compliance + Strategy + Technical QA | Named QA owners | Independent reviewers | No | All three QA gates signed off and blocking issues resolved. | Not Started | Internal sign-off | 15 Compliance + Launch QA |  |
| 13 | Launch | Project Lead | Developer / SEO | Client informed | Launch completed; tracking verified; baseline captured. | Not Started | Launch sign-off | 16 Measurement Baseline |  |
| 14 | 30 / 60 / 90 Measurement | Strategist / Project Lead | Project Lead | Review as needed | Post-launch reviews completed; KEEP/IMPROVE/TEST/SCALE decisions recorded. | Not Started | No | 17 30-60-90 Review |  |

Data validation:

- `G2:G16`: "Not Started,In Progress,Blocked,Ready for Review,Complete,N/A"

## Approvals

| Decision | Level | Owner | Status | Date | Client / Approver | Feedback Classification | Notes |
|---|---|---|---|---|---|---|---|
| Positioning | L2 | Strategist | Pending |  |  | Strategic |  |
| Visual direction | L5 | Designer | Pending |  |  | Preference / Strategic |  |
| Navigation / user journey | L3 | Strategist / UX | Pending |  |  | User / UX |  |
| Service hierarchy | L1/L3 | Strategist | Pending |  |  | Strategic |  |
| Practitioner hierarchy | L1/L2 | Strategist | Pending |  |  | Strategic |  |
| Homepage structure | L3/L5 | Strategist / Designer | Pending |  |  | User / UX |  |
| Photography direction | L4/L5 | Designer / Content | Pending |  |  | Preference / Accuracy |  |

Data validation:

- `D2:D100`: "Pending,Approved,Changes Requested,Locked,N/A"
- `G2:G100`: "Strategic,Accuracy,User / UX,Compliance,Preference,New Information"

## Content Inputs

| Item | Category | Requested From | Owner | Status | Requested Date | Due Date | Source / File | Notes |
|---|---|---|---|---|---|---|---|---|
| Practitioner roles / titles | Practitioner |  |  | Not Requested |  |  |  |  |
| Registrations / numbers | Practitioner |  |  | Not Requested |  |  |  |  |
| Qualifications | Practitioner |  |  | Not Requested |  |  |  |  |
| Treatment list | Treatment |  |  | Not Requested |  |  |  |  |
| Prices / courses / downtime | Treatment |  |  | Not Requested |  |  |  |  |
| Who provides each treatment | Treatment |  |  | Not Requested |  |  |  |  |
| Review platform access / URLs | Review |  |  | Not Requested |  |  |  |  |
| Clinic photography date | Photography |  |  | Not Requested |  |  |  |  |
| Before / after cases + consent | Photography |  |  | Not Requested |  |  |  |  |
| Locations / opening hours | Business Details |  |  | Not Requested |  |  |  |  |
| Booking links / consultation status | Booking |  |  | Not Requested |  |  |  |  |
| Vector logos / brand assets | Brand |  |  | Not Requested |  |  |  |  |

Data validation:

- `E2:E200`: "Not Requested,Requested,Received,Verified,N/A"

## Proof Inventory

| Type | Claim / Evidence | Source / URL | Applies To | Verified? | Consent / Permission | Owner | Deadline | Notes |
|---|---|---|---|---|---|---|---|---|

Data validation:

- `A2:A200`: "Qualification,Registration,Membership,Award,Review,Result,Media,Teaching,Other"
- `D2:D200`: "Clinic,Practitioner,Treatment,Location,Multiple"
- `E2:E200`: "Yes,No,Pending"
- `F2:F200`: "Confirmed,Pending,N/A"

## QA

| Gate | Check | Owner | Status | Issue / Fix | Sign-off / Date |
|---|---|---|---|---|---|
| Compliance | Claims |  | Not Checked |  |  |
| Compliance | Credentials |  | Not Checked |  |  |
| Compliance | Practitioner titles |  | Not Checked |  |  |
| Compliance | Treatment terminology |  | Not Checked |  |  |
| Compliance | Before/after usage |  | Not Checked |  |  |
| Compliance | Testimonials |  | Not Checked |  |  |
| Compliance | Promotional language |  | Not Checked |  |  |
| Compliance | Pricing claims |  | Not Checked |  |  |
| Compliance | Guarantees / outcome language |  | Not Checked |  |  |
| Compliance | Patient consent |  | Not Checked |  |  |
| Strategy / UX | Positioning survives implementation |  | Not Checked |  |  |
| Strategy / UX | Trust appears early enough |  | Not Checked |  |  |
| Strategy / UX | User journeys work |  | Not Checked |  |  |
| Strategy / UX | Clinic/practitioner hierarchy correct |  | Not Checked |  |  |
| Strategy / UX | CTAs clear |  | Not Checked |  |  |
| Strategy / UX | Mobile works |  | Not Checked |  |  |
| Strategy / UX | Scalability preserved |  | Not Checked |  |  |
| Technical / SEO | Indexability |  | Not Checked |  |  |
| Technical / SEO | Metadata |  | Not Checked |  |  |
| Technical / SEO | Canonicals |  | Not Checked |  |  |
| Technical / SEO | Redirects |  | Not Checked |  |  |
| Technical / SEO | Schema |  | Not Checked |  |  |
| Technical / SEO | Internal links |  | Not Checked |  |  |
| Technical / SEO | Performance |  | Not Checked |  |  |
| Technical / SEO | Forms / booking |  | Not Checked |  |  |
| Technical / SEO | Tracking |  | Not Checked |  |  |
| Technical / SEO | Responsive behaviour |  | Not Checked |  |  |
| Technical / SEO | Broken links |  | Not Checked |  |  |
| Technical / SEO | Consent implementation |  | Not Checked |  |  |

Data validation:

- `D2:D30`: "Not Checked,Pass,Fix,N/A"

## Measurement

| Metric | Baseline | 30 Days | 60 Days | 90 Days | Direction / Note | Action |
|---|---|---|---|---|---|---|
| Organic sessions |  |  |  |  |  |  |
| Priority landing-page clicks |  |  |  |  |  |  |
| Booking starts |  |  |  |  |  |  |
| Booking completions |  |  |  |  |  |  |
| Calls |  |  |  |  |  |  |
| Forms / enquiries |  |  |  |  |  |  |
| Conversion rate |  |  |  |  |  |  |
| Mobile conversion |  |  |  |  |  |  |
| Priority service performance |  |  |  |  |  |  |
| GBP / local actions |  |  |  |  |  |  |
| Decision | KEEP | IMPROVE | TEST | SCALE | Owner | Deadline |
| [[Item]] |  |  |  |  |  |  |
| [[Item]] |  |  |  |  |  |  |
| [[Item]] |  |  |  |  |  |  |
| [[Item]] |  |  |  |  |  |  |
| [[Item]] |  |  |  |  |  |  |
| [[Item]] |  |  |  |  |  |  |
| [[Item]] |  |  |  |  |  |  |

