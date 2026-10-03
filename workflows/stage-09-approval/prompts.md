# Stage 9 — Approval Gate

**Purpose:** Convert client feedback into explicit decisions, controlled revisions and locked strategic choices.

## 9A — Meeting Notes → Approval Record

**Use when:** Immediately after the client review meeting.  
**Inputs:** Meeting notes/transcript; deck; current Approval Record.  
**Produces:** Updated Approval Record.

```text
Convert the strategy-review notes into an Approval Record.

For each decision classify:
APPROVED
CHANGES REQUESTED
PENDING
LOCKED
NOT DISCUSSED

Decisions:
Positioning
Visual direction
Navigation / user journey
Service hierarchy
Practitioner hierarchy
Homepage structure
Photography direction
Any project-specific decision

For every change request include:
CLIENT FEEDBACK
FEEDBACK TYPE
WHAT DECISION LEVEL IT AFFECTS
ACTION
OWNER
DEADLINE
DOES IT REOPEN AN APPROVED DECISION? Yes/No

Never infer approval from silence.
```

## 9B — Feedback Classifier

**Use when:** When client comments arrive by email, comments or meeting notes.  
**Inputs:** Raw client feedback; locked decisions.  
**Produces:** Classified feedback table.

```text
Classify every piece of client feedback before acting on it.

Classes:
STRATEGIC — changes business/positioning direction.
ACCURACY — factual correction.
USER / UX — concern about comprehension or behaviour.
COMPLIANCE — legal/regulatory constraint.
PREFERENCE — personal aesthetic/content preference.
NEW INFORMATION — new fact that may alter strategy.

For each comment output:
FEEDBACK
CLASS
DECISION LEVEL 1–5
CONFLICTS WITH LOCKED DECISION? Yes/No
RECOMMENDED RESPONSE
ACTION REQUIRED
OWNER

Rules:
- Accuracy and compliance corrections take priority.
- Preference does not automatically overrule approved strategy.
- If new information genuinely changes the brief, state exactly which earlier decisions must be reopened.
```

## 9C — Revision Plan

**Use when:** After feedback is classified.  
**Inputs:** Classified feedback; approved decisions; scope.  
**Produces:** Controlled revision plan.

```text
Create the next revision plan.

Group actions into:
MUST CHANGE — accuracy/compliance/approved strategic feedback.
SHOULD CHANGE — improves the agreed direction.
DO NOT CHANGE — feedback that would weaken or contradict approved strategy without new evidence.
NEEDS DECISION — unresolved trade-off requiring client choice.

For each:
Action
Reason
Owner
Affected artefact/page
Dependency
Revision round

Protect LOCKED decisions unless the brief has materially changed.
```

## 9D — Approval Follow-Up

**Use when:** After review meeting / revision round.  
**Inputs:** Approval Record; open decisions.  
**Produces:** Client email confirming decisions.

```text
Draft the client follow-up after the design/strategy review.

Include:
- thank you / concise recap;
- what is approved;
- changes we are making;
- decisions still needed;
- what is now locked;
- what we need from the client;
- next step and timing if supplied.

Do not say “let us know what you think”.
Ask for specific outstanding decisions.
Do not use internal decision-level terminology.
```

## 9E — Change-Control Evaluator

**Use when:** When someone tries to reopen an approved decision.  
**Inputs:** New request; locked decision; original rationale; new evidence.  
**Produces:** Decision on whether to reopen.

```text
Evaluate whether the new request justifies reopening an approved decision.

Test:
- Is this new factual information?
- Is it a material commercial change?
- Is it new user evidence?
- Is it a technical limitation?
- Is it a compliance requirement?
- Or is it preference?

Output:
REOPEN / DO NOT REOPEN / NEEDS MORE INFORMATION

Then state:
Original locked decision
New information/request
Why it does/does not materially change the brief
Downstream stages affected
Cost / schedule implication if known
Recommended response to client

Do not defend an old decision merely because it is old. Reopen it when the underlying facts genuinely changed.
```

