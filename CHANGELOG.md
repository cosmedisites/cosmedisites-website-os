# Changelog

All material changes to the CosmediSites Website OS. Versioning: [docs/governance.md#versioning](docs/governance.md#versioning).

## [Unreleased]

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
