# Stage 10 — Production Inputs

**Purpose:** Get every approved content, evidence and technical input into a verified state before full production/build depends on it.

## 10A — Input Tracker Generator

**Use when:** After strategy approval.  
**Inputs:** Approved page system; content gaps; proof gaps; build requirements.  
**Produces:** Populated Content/Input Tracker.

```text
Create the production input tracker.

For each required item record:
ITEM
CATEGORY
REQUESTED FROM
INTERNAL OWNER
STATUS
REQUESTED DATE if known
DUE DATE if known
SOURCE / FILE
VERIFICATION REQUIRED?
BLOCKS WHAT?
NOTES

Categories:
Practitioner
Treatment
Pricing
Review
Photography
Results / consent
Location
Booking
Brand
Legal / compliance
Technical
Other

Statuses:
Not Requested
Requested
Received
Verified
N/A

Only create inputs that the approved project actually needs.
```

## 10B — Missing Inputs Follow-Up

**Use when:** When client inputs are overdue or incomplete.  
**Inputs:** Current input tracker.  
**Produces:** Client-facing follow-up prioritised by blockage.

```text
Draft a concise missing-input follow-up.

Group items into:
BLOCKING NOW
NEEDED BEFORE LAUNCH
CAN FOLLOW AFTER LAUNCH

For every blocking item explain in plain language what work cannot proceed without it.

Do not send the client a giant tracker dump.
Do not chase N/A or already received items.
Keep the request skimmable and specific.
```

## 10C — Input Verification

**Use when:** When client sends a batch of information/assets.  
**Inputs:** New inputs; existing tracker; Proof Inventory.  
**Produces:** Verification and tracker update instructions.

```text
Review the newly supplied production inputs.

For each item:
MATCHED TRACKER ITEM
RECEIVED?
COMPLETE?
FACTUALLY CONSISTENT WITH EXISTING CONTEXT?
PROOF / SOURCE PRESENT?
COMPLIANCE REVIEW NEEDED?
STATUS: Received / Verified / Still Incomplete
NOTES

Flag contradictions with previously confirmed facts.
Do not silently overwrite earlier data; state the conflict and request resolution if material.
```

## 10D — Build Readiness Gate

**Use when:** Before development begins in full.  
**Inputs:** Approved strategy; inputs; designs; sitemap; handoff artefacts.  
**Produces:** PASS/FAIL/BLOCKED build-readiness report.

```text
Run the CosmediSites Build Readiness Gate.

Check:
- strategic approvals recorded;
- required screens approved;
- mobile states defined;
- sitemap / URL map approved;
- redirect requirements known;
- primary copy approved or clearly owned;
- practitioner facts verified;
- proof required by design is available;
- photography final or placeholders explicitly controlled;
- booking/contact details known;
- tracking requirements known;
- compliance-critical unknowns resolved;
- open items have owners and do not block build.

Return PASS / FAIL / BLOCKED for each.
List BLOCKERS first.
Do not declare the project ready merely because design is complete.
```

