# Stage 2 — Strategic Diagnosis

**Purpose:** Turn evidence into a prioritised explanation of what is suppressing the business outcome, without jumping prematurely to visual solutions.

## 2A — Evidence → Strategic Diagnosis

**Use when:** Once the Evidence Pack is complete.  
**Inputs:** Project Strategy Brief; Evidence Pack.  
**Produces:** Draft Strategic Diagnosis.

```text
You are the CosmediSites strategist.

Using the Project Strategy Brief and Evidence Pack, write the Strategic Diagnosis.

Structure:

1. CURRENT PERCEPTION
2. DESIRED PERCEPTION
3. COMMERCIAL WEAKNESSES
4. TRUST WEAKNESSES
5. UX / DISCOVERY WEAKNESSES
6. BRAND ARCHITECTURE WEAKNESSES
7. SEARCH / INFORMATION ARCHITECTURE RISKS
8. SCALABILITY RISKS
9. PRIORITY OPPORTUNITIES
10. DIAGNOSIS IN ONE SENTENCE
11. DEFINITION OF DONE CHECK

For each weakness state:
- evidence;
- patient/business consequence;
- priority;
- confidence.

Rules:
- Do not prescribe colours, typography or UI styling.
- Explain cause and consequence.
- Separate “looks dated” from the actual commercial effect.
- Make the diagnosis specific enough that it could not be pasted unchanged onto another clinic.
```

## 2B — Priority Stack

**Use when:** When the diagnosis contains too many issues.  
**Inputs:** Strategic Diagnosis; Project Strategy Brief.  
**Produces:** Prioritised issue stack.

```text
Prioritise the supplied diagnosis using this order:

1. Revenue / lead impact
2. Trust / credibility impact
3. Ability for users to understand and choose
4. Search / discoverability risk
5. Scalability
6. Ease / cost to fix

Create:
P0 — must be solved for redesign to succeed
P1 — high-value, should be solved in core build
P2 — useful, can follow after launch
P3 — cosmetic / optional

For each issue state:
Issue | Why it matters | Evidence | Priority | What later stage must solve it

Do not promote a low-impact visual preference above a high-impact structural problem.
```

## 2C — Strategic Diagnosis Red Team

**Use when:** Before moving to positioning.  
**Inputs:** Draft diagnosis and priority stack.  
**Produces:** Red-team report.

```text
Red-team the Strategic Diagnosis.

Try to disprove it.

Ask:
- Which conclusions are directly evidenced?
- Which are inference?
- Which are aesthetic opinion disguised as strategy?
- Is the diagnosis solving the client’s commercial brief or merely the existing website?
- Does it account for planned locations / practitioners / services?
- Does it confuse low visibility with low demand?
- Does it assume a patient journey without evidence?
- Does it preserve valuable existing assets?
- Would a different strategist reach a materially different conclusion because of missing facts?

Output:
SUPPORTED
WEAK / NEEDS MORE EVIDENCE
CONTRADICTED
OPEN

Then state whether Stage 2 is PASS / FAIL / BLOCKED and why.
```

