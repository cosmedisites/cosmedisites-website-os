# CosmediSites Website Strategy Playbook

> **Status: AWAITING IMPORT.** The Playbook is a named source document, but it was not in the
> material supplied when this repository was set up (only the AI Workflow Pack v1.0 was).
> This file is the slot it goes into. Nothing here should be read as Playbook content.

## Role in the system

| Layer | Job |
|---|---|
| **Playbook** (this file) | How CosmediSites thinks about clinic website strategy |
| [SOP](../sop/website-redesign-sop.md) | What happens next: stages, owners, gates, Definitions of Done |
| [Templates](../templates/) / [Prompts](../workflows/00-workflow-index.md) | How we execute |

## What the AI Workflow Pack already confirms about the Playbook's principles

These are taken from the AI Workflow Pack v1.0 (which says it sits *beneath* the Playbook).
They are not a substitute for the Playbook:

- **Decision hierarchy:** 1 Business strategy → 2 Positioning → 3 UX / information architecture
  → 4 Content / proof → 5 Visual expression. A lower-level preference should not casually
  overturn a higher-level decision.
- **Evidence states:** CONFIRMED · OBSERVED · INFERRED · OPEN · LOCKED.
- **Anti-generic test:** "Could this output be pasted onto another clinic unchanged?"

## How to import (one pull request)

1. Convert the master DOCX to Markdown: `pandoc -f docx -t gfm --wrap=none Playbook.docx -o playbook/website-strategy-playbook.md`
2. Tidy the headings so each chapter is a `##` heading (this gives stable deep links).
3. Delete any client names, client examples or screenshots, or anonymise them per [examples/](../examples/anonymised-example-project/README.md).
4. Open a PR labelled `documentation` and `methodology`. Methodology owner review is required.
5. Attach the original DOCX to the GitHub Release. Do not commit it.
