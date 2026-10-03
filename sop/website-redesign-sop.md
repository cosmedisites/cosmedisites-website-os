# CosmediSites Website Redesign SOP v1.0

> **Status: AWAITING IMPORT.** The SOP was not in the material supplied when this repository was
> set up. Until it is imported:
> - each [stage card](../workflows/00-workflow-index.md) carries an **interim Definition of Done**
>   compiled from that stage's validator prompt in the AI Workflow Pack v1.0;
> - default owner/reviewer roles are **inferred** from prompt wording and the handoff prompts.
>
> When the SOP is imported, its Definitions of Done and owners are authoritative. Update
> `ops/stages.yaml` to match it, then run `python3 scripts/build.py`.

## Expected structure after import

Keep one `##` heading per stage so stage cards and the operational tool can deep-link:

```
## Stage 00 — Commercial Brief
### Owner / reviewer
### Inputs
### Actions
### Output
### Definition of Done
### Approval
```

…repeated for Stages 01–14.

## Import procedure (one pull request)

1. Convert: `pandoc -f docx -t gfm --wrap=none SOP_v1.0.docx -o sop/website-redesign-sop.md`
2. Normalise stage headings to the structure above.
3. Diff each stage's SOP Definition of Done against `ops/stages.yaml` → `dod:`. **The SOP wins.**
   Record any genuine conflict between the SOP and the AI Workflow Pack validators in the PR
   description. Do not quietly pick one.
4. Replace `owner_role` / `reviewer_role` in `ops/stages.yaml` with the SOP's owners.
5. Run `python3 scripts/build.py`, commit the regenerated stage cards, and open a PR labelled `methodology`.
6. Attach the original DOCX to the release. Add a CHANGELOG entry.
