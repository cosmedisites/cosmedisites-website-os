# CosmediSites AI Workflow Index

## Fast operating rule

1. Open **00-master-project-context.md** and keep it current.
2. Read **00-ai-operating-rules.md** once per project/workspace.
3. Find the current stage below.
4. Run the prompts in the recommended order.
5. Produce the mapped artefact.
6. Run the validator / Definition of Done.
7. Do not move stage until PASS or an authorised exception is recorded.

## Stage router

| Stage | Phase | Prompt route | Output | Template | Gate |
|---|---|---|---|---|---|
| 0 | Commercial Brief | 0A → 0B → 0C; use 0D if blocked | Project Strategy Brief | Template 01 | Client factual confirmation |
| 1 | Evidence | 1A + 1B → 1C → 1D | Evidence Pack | Template 02 | Internal |
| 2 | Strategic Diagnosis | 2A → 2B → 2C | Strategic Diagnosis | Template 03 | Internal |
| 3 | Positioning | 3A → 3B + 3C → 3D → 3E | Positioning Thesis + Brand Architecture | Template 04 | Client strategic approval |
| 4 | IA + SEO | 4A → 4B + 4C → 4D → 4E | Sitemap / SEO Architecture | Template 06 | Conditional client approval |
| 5 | Visual Direction | 5A → 5B + 5C → 5D | Visual Direction | Template 07 | Client approval |
| 6 | Page + Component System | 6A + 6B + 6C + 6D → 6E | Page / Component System | Template 08 | Internal / included in review |
| 7 | Proof + Content + Photography | 7A + 7B + 7C → 7D + 7E | Proof Inventory + Photography Brief + content gaps | Templates 09–10 | Client supplies inputs |
| 8 | Client Strategy Review | 8A → 8B → 8C → 8D | Client Strategy Deck | Template 11 | Review meeting |
| 9 | Approval Gate | 9A + 9B → 9C + 9D; use 9E for reopened decisions | Approval Record + revision plan | Template 12 | Client sign-off |
| 10 | Production Inputs | 10A → 10B/10C → 10D | Content / Input Tracker + build readiness | Template 13 | Internal gate |
| 11 | Build | 11A + 11B + 11C → 11D | Build Handoff + implementation variance | Template 14 | Internal |
| 12 | QA | 12A + 12B + 12C → 12D → 12E | Compliance / Strategy / Technical QA | Template 15 | Internal sign-off |
| 13 | Launch | 13A → 13B → 13C + 13D; 13E as needed | Launch runbook + baseline | Template 16 | Launch sign-off |
| 14 | 30/60/90 Measurement | 14A → 14B → 14C → 14D → 14E | Post-launch review + learning | Template 17 | Internal / client review |


## Prompt-use pattern

For every stage:

**Research / Input → Strategy / Execution → Validation → Handoff**

Not every stage needs all four as separate prompts, but the logic remains the same.

## What to paste into a new AI conversation

Minimum context:
1. AI Operating Rules
2. Master Project Context
3. Current-stage prompt
4. Relevant source artefacts/files only

Do **not** paste the entire project archive into every prompt if it is not relevant.

## When to start a fresh conversation

Start a fresh workspace/thread when:
- moving into a different role with lots of unrelated context;
- the model begins re-litigating LOCKED decisions;
- the source set becomes too large/noisy;
- a client/project changes.

Carry across:
- Master Project Context
- current artefact
- current-stage prompt
- relevant source files

## Quick routing by job

- “I need to understand the client” → 0A/0B
- “Audit the existing site before design” → 1A–1D
- “What is actually wrong strategically?” → 2A–2C
- “What should this clinic be known for?” → 3A–3E
- “Build the sitemap without killing SEO” → 4A–4E
- “Turn strategy into art direction” → 5A–5D
- “Design reusable pages/components” → 6A–6E
- “Get proof/content/photos together” → 7A–7E
- “Build the client presentation” → 8A–8D
- “Handle client comments/approval” → 9A–9E
- “Chase and verify production inputs” → 10A–10D
- “Hand to dev/build correctly” → 11A–11D
- “QA before launch” → 12A–12E
- “Launch safely” → 13A–13E
- “Review 30/60/90 performance” → 14A–14E
- “Write client comms” → C01–C09
- “Handoff between team roles” → H01–H08
