# Changelog

All material changes to the CosmediSites Website OS. Versioning: [docs/governance.md#versioning](docs/governance.md#versioning).

## v1.1 (7 October 2026): Creative Translation layer

**Why.** The HAUS of DRA redesign exposed a repeatable failure mode: strategy, IA, CRO and SEO were solved, then the design was translated into a safe component system too early. The site was technically good and visually generic. The fix is a formal creative layer between visual direction and the component system.

**Added**
- Stage 05T Creative Translation: 3 to 4 high-fidelity keyframes with real client assets; Brand Swap Test; generic-design red team.
- Stage 05V Creative Validation: CRO/SEO/compliance/mobile/motion/performance collision test; hard asset gate; client approves keyframes, not mood boards.
- Creative Intensity rating at Stage 00 (Conservative / Elevated / High-expression) and a LOCKED list of strategic invariants.
- Brand reality audit, MATCH / BEAT / AVOID benchmark, asset matrix (USE / SHOOT / SOURCE / DO NOT FAKE) and creative thesis at Stage 05 (renamed Brand + Visual Direction).
- Stage 06 is now derived from the approved keyframes, with a DoD line forbidding visual flattening.
- Native implementation pilot at Stage 11 before roll-out.
- Fourth independent QA gate, 12F Creative.
- Principles: "The design system follows the creative direction, not the other way around." and "SEO and CRO are constraints to design within, not excuses for generic design."

**Unchanged**
- Stage numbers 06 to 14 (new stages are 05T and 05V), so v1.0 projects, Drive folders and pipeline columns remain valid.

**Where it is applied**
- Chirply (CosmediSites): project template "Website Redesign (OS v1.1)"; the Website Redesign deal template now creates projects from it (`os_version: v1.1`); pipeline columns 05 Brand + Visual Direction, 05T, 05V. The v1.0 template is kept for projects already running.
- Drive (`_Website OS`): template folder renamed to OS v1.1 with S05T and S05V subfolders; tracker, README and Master Project Context v1.1; v1.0 originals in `_Archive – Website OS v1.0`.

## [Unreleased]

### Operational design (Chirply; no SOP change)
- 2026-10-04: Chirply shipped project templates (auto-created from a deal template), native task
  reviewers with request/approve review, task comments and links, custom board columns, tags,
  team-member fields and project-task workflow triggers/actions. Updated the Chirply audit,
  operational stage spec, automation map and pilot set-up to use them.

## [1.0] — proposed, not yet tagged

Initial production repository, built from **CosmediSites Website OS Source Pack v1.0**.
Tag `v1.0` once this is merged to `main` and reviewed.

### Added: source methodology (verbatim from Source Pack v1.0)
- Website Strategy Playbook v1.0 → `playbook/website-strategy-playbook.md`
- Website Redesign SOP v1.0 → `sop/website-redesign-sop.md`
- Redesign Template Pack v1.0, 17 templates → `templates/*.md` (files renamed to kebab-case; content unchanged)
- AI Workflow Pack v1.0:
  - AI Operating Rules, Master Project Context template, Workflow Index → `workflows/00-*.md`
  - stage prompts 0A–14E → `workflows/stage-NN-*/prompts.md`
  - C01–C09 and H01–H08 → `prompts/`
  - catalogue → `prompts/prompt-catalog.csv`
  - Quickstart → `docs/quickstart.md`
- Operational Tracker v1.0 → `templates/operational-tracker.md`. This is a structure spec generated
  from the workbook; the XLSX itself is a release asset.

Repository-only edits to source material: filename references in the Workflow Index, file paths in
the prompt catalogue and Quickstart, and an added "Using these templates in the Website OS" section
at the end of `templates/README.md`. `ALL_PROMPTS.md` and `PROMPT_CATALOG.json` are now generated at
release rather than committed, which removes duplicate sources of truth.

### Added: operating-system infrastructure
- `ops/stages.yaml`: stage registry reconciling the SOP (owners, outputs, Definitions of Done), the
  Tracker (approval requirement, client involvement, status lists) and the AI pack (objective,
  prompt route, gate). Every field records its source.
- Generated stage cards (`workflows/stage-NN-*/README.md`), the README stage table and the Chirply
  payload (`stage-config.json`), all from the registry.
- QA gates (`qa/`) from SOP Stage 12, with SOP owners.
- `scripts/build.py` (generation and consistency checks) and `scripts/safety_scan.py` (secrets/PII guard).
- CI (`checks.yml`) and release packaging (`release.yml`).
- README, CONTRIBUTING, SECURITY, CODEOWNERS, issue and PR templates.
- `docs/`: Chirply audit and decision matrix, operating architecture, operational stage spec, Master
  Project Context storage, AI execution workflow, handoffs, automation map, governance,
  implementation plan.

### Known gaps (logged as open questions)
- The SOP has no Definition of Done checklist for Stages 9, 13 and 14; the stage cards use Templates 12, 16 and 17.
- The "Creative / Creative Lead" reviewer named in SOP Stages 3 and 5 is not in the SOP role table.
- The Chirply audit was run against a non-CosmediSites workspace; verification tests V1–V10 are pending.
