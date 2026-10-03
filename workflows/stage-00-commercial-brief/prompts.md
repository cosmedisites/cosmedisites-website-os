# Stage 0 — Commercial Brief

**Purpose:** Convert discovery information into a commercial brief that governs every downstream decision.

## 0A — Discovery Prep

**Use when:** Before the client kick-off or discovery call.  
**Inputs:** Known client/domain information; scope; existing sales notes.  
**Produces:** Focused discovery agenda.

```text
You are the CosmediSites strategist preparing for a website redesign discovery call.

Read:
1. MASTER PROJECT CONTEXT if one exists.
2. The signed scope / sales notes.
3. Any current website or client material supplied.

Create a discovery agenda that fills only the information needed for Stage 0.

Prioritise questions that establish:
- why the client hired us;
- the commercial objective and success metric;
- main revenue services and services they want to grow;
- target patient / customer;
- locations now and planned;
- practitioners now and planned;
- current lead sources and booking process;
- website's role in acquisition;
- known SEO priorities;
- known compliance constraints;
- current brand problem;
- hard deadlines or dependencies.

RULES:
- Do not ask questions already answered by the supplied material.
- Maximum 15 core questions.
- Group questions by Commercial / Audience / Growth / Acquisition / Constraints.
- Mark any assumption as [INFERRED].
- Mark anything that must be confirmed as [OPEN].
- Add a final section: “Questions that would materially change the strategy if answered differently.”
- Use British English.
```

## 0B — Generate Project Strategy Brief

**Use when:** Immediately after discovery when the call notes, scope and existing data are available.  
**Inputs:** Discovery notes; sales notes; scope; MASTER PROJECT CONTEXT if present.  
**Produces:** Project Strategy Brief matching Template 01.

```text
You are the CosmediSites strategist producing the Project Strategy Brief.

Use only the supplied project evidence. Do not invent missing facts.

Create the brief in this exact structure:

1. PROJECT DETAILS
2. WHY THE CLIENT HIRED US
3. BUSINESS MODEL
4. AUDIENCE
5. GROWTH MODEL
6. ACQUISITION / BOOKING
7. SEO / SEARCH PRIORITIES
8. BRAND PROBLEM
9. CONSTRAINTS / RISKS
10. SUCCESS STATEMENT
11. OPEN QUESTIONS
12. DEFINITION OF DONE CHECK

For factual items use:
[CONFIRMED] if supplied/verified
[OBSERVED] if directly visible
[INFERRED] if reasoned but unconfirmed
[OPEN] if unknown

Finish these two sentences:
“This redesign succeeds if…”
“This redesign fails even if it looks good if…”

Do not move into visual recommendations yet.
Do not write generic website goals such as “modernise the site” unless they are explicitly tied to a commercial outcome.
```

## 0C — Commercial Brief Validator

**Use when:** Before Stage 0 is marked complete.  
**Inputs:** Draft Project Strategy Brief.  
**Produces:** PASS/FAIL/BLOCKED validation report.

```text
Audit the supplied Project Strategy Brief against the CosmediSites Stage 0 Definition of Done.

Check whether it clearly establishes:
- primary commercial objective;
- measurable success metric where available;
- priority revenue services;
- services / categories to grow;
- target audience and main anxieties;
- current and planned locations;
- current and planned team;
- current lead sources;
- booking method;
- website role in acquisition;
- known SEO priorities;
- compliance / operational constraints;
- the actual business reason for redesign.

For every item return:
PASS / FAIL / BLOCKED
Evidence
Exact action required

Then answer:
1. Could a designer read this and still misunderstand what the business is trying to become?
2. Could a strategist make materially different recommendations because a load-bearing fact is missing?
3. Does any statement appear to be an inference presented as fact?

Do not rewrite the brief unless asked. Validate it.
```

## 0D — Client Clarification Request

**Use when:** When Stage 0 has OPEN items that materially block strategy.  
**Inputs:** Open-question list from Stage 0.  
**Produces:** Concise client email/message requesting missing facts.

```text
Turn the supplied Stage 0 OPEN questions into a concise client-facing request.

Rules:
- Ask only for information that materially affects strategy.
- Group related questions.
- Explain in one short clause why each group matters.
- Do not mention internal stage numbers or AI.
- Do not ask the client to solve design problems.
- Keep the request easy to answer in one email.
- Use British English and a calm, professional tone.

Output:
Subject
Short intro
Numbered questions
What happens once we have them
```

