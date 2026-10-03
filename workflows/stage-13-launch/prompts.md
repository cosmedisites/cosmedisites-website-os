# Stage 13 — Launch

**Purpose:** Launch in a controlled way, verify acquisition/measurement systems and capture the baseline required for post-launch learning.

## 13A — Launch Plan

**Use when:** Once QA is near complete.  
**Inputs:** QA report; technical handoff; launch date; hosting/domain context.  
**Produces:** Launch plan.

```text
Create the project-specific launch plan.

Structure:
PRE-LAUNCH T-7 TO T-1
LAUNCH WINDOW
IMMEDIATE POST-LAUNCH 0–2 HOURS
DAY 1
WEEK 1
ROLLBACK TRIGGERS
OWNERS / CONTACTS

Include where relevant:
backup;
DNS/domain;
deployment;
redirects;
robots/indexation;
sitemap;
forms/booking;
analytics;
conversion tracking;
cookie/consent;
critical page smoke tests;
mobile;
payments if applicable;
GBP/site links if relevant;
client notification.

Do not include generic technical steps that do not apply to the project.
```

## 13B — Launch-Day Runbook

**Use when:** On launch day.  
**Inputs:** Approved Launch Plan.  
**Produces:** Tick-box launch sequence.

```text
Convert the Launch Plan into a concise launch-day runbook.

For each step output:
ORDER
ACTION
OWNER
EXPECTED RESULT
PASS / FAIL FIELD
ROLLBACK / ESCALATION IF FAIL

Separate:
BEFORE DEPLOY
DEPLOY
5-MINUTE CHECKS
30-MINUTE CHECKS
2-HOUR CHECKS

Put revenue/lead-critical and indexation-critical checks first.
```

## 13C — Client Launch Notification

**Use when:** After launch checks pass.  
**Inputs:** Launch status; known caveats; support process.  
**Produces:** Client launch email.

```text
Draft the client launch message.

Include:
- confirmation the site is live;
- concise summary of what has changed;
- what has been checked;
- any transparent non-blocking items still being monitored;
- what the client should do / avoid immediately after launch;
- 30-day review expectation.

Do not overclaim performance gains before data exists.
Do not say the project is “finished” if monitoring/migration work remains.
```

## 13D — Measurement Baseline Capture

**Use when:** At or immediately before launch.  
**Inputs:** Analytics/GSC/GBP/booking/call data available.  
**Produces:** Baseline record matching Template 16.

```text
Create the launch measurement baseline.

Record the comparison window and launch date.

Capture where available:
- total and organic sessions;
- priority landing-page clicks / impressions;
- booking starts;
- booking completions;
- calls;
- forms / enquiries;
- conversion rate;
- mobile share and mobile conversion;
- priority service performance;
- local / GBP actions;
- priority rankings if the project tracks them.

For every metric include:
SOURCE
BASELINE PERIOD
VALUE
TRACKING CONFIDENCE
KNOWN CHANGE AT LAUNCH

If tracking is unavailable, record that as a measurement gap rather than inventing a baseline.
```

## 13E — Post-Launch Issue Triage

**Use when:** During the first 7 days.  
**Inputs:** Issue reports; analytics; QA; client feedback.  
**Produces:** Prioritised post-launch issue list.

```text
Triage post-launch issues.

Classify:
P0 — revenue/compliance/site availability/data loss/search migration blocker
P1 — serious UX/booking/SEO issue
P2 — non-critical defect
P3 — polish/request

For each:
Issue
Evidence
Affected users/pages
Severity
Owner
Fix
Retest
Does this reflect a strategy flaw or implementation defect?

Do not reopen design strategy because of isolated preference feedback during launch week.
```

