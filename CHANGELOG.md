# Changelog

All material changes to the CosmediSites Website OS. Versioning: [docs/governance.md#versioning](docs/governance.md#versioning).

## [Unreleased]

## [1.0] — proposed, not yet tagged

Initial production repository. Tag `v1.0` once this is merged to `main` and reviewed.
The Playbook and SOP will be imported in v1.1.

### Added
- Repository structure, README, CONTRIBUTING, SECURITY, CODEOWNERS, issue and PR templates.
- `ops/stages.yaml`: stage registry for Stages 00–14 (objective, route, prompts, output,
  templates, gate, default roles, interim Definition of Done).
- Generated stage cards: `workflows/stage-NN-*/README.md`.
- 17 interim template skeletons (`templates/`), built from the AI Workflow Pack output structures.
- Three QA gate checklists (`qa/`) from prompts 12A/12B/12C.
- `scripts/build.py` (generation and consistency checks) and `scripts/safety_scan.py` (secrets/PII guard).
- CI (`.github/workflows/checks.yml`) and release packaging (`.github/workflows/release.yml`).
- Operating architecture, Chirply audit, operational stage spec, Master Project Context storage,
  AI execution workflow, handoffs, automation map and implementation plan (`docs/`).

### Migrated (from CosmediSites AI Workflow Pack v1.0, content unchanged)
- AI Operating Rules, Master Project Context template, Workflow Index → `workflows/00-*.md`.
  The only edit is to filename references in the Workflow Index.
- Stage prompt files 0A–14E → `workflows/stage-NN-*/prompts.md`.
- Client communication prompts C01–C09 and role handoff prompts H01–H08 → `prompts/`.
- Prompt catalogue → `prompts/prompt-catalog.csv` (file paths updated; JSON is now generated at release).
- Quickstart DOCX → `docs/quickstart.md` (paths updated).
- `ALL_PROMPTS.md` is no longer committed. It is generated from the stage files at release, which
  removes a duplicate source of truth.

### Known gaps
- Website Strategy Playbook, Website Redesign SOP v1.0, Redesign Template Pack v1.0 and Operational
  Tracker v1.0 were not in the supplied material. Placeholders and import procedures are in place.
- Stage Definitions of Done are **interim**, compiled from the validator prompts. Default owner
  roles are **inferred**. Both must be reconciled with the SOP on import.
