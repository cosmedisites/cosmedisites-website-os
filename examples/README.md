# Examples — what good actually looks like

For each important artefact the OS aims to provide three things:

| | Answers | Lives in |
|---|---|---|
| **Template** | What must be completed | [`templates/`](../templates/) |
| **SOP** | How to complete it | [`sop/`](../sop/website-redesign-sop.md) and the [stage cards](../workflows/00-workflow-index.md) |
| **Example** | What good actually looks like | here |

Examples are added over time from real projects, **only after anonymisation**. There are none
yet. The first ones should come from the Phase 6 pilot project.

## Priority order for first examples

1. Project Strategy Brief (Template 01)
2. Positioning Thesis (Template 04)
3. Approval Record (Template 12)
4. Strategist → Designer handoff (H03)
5. Build Readiness Gate result (10D)

## Anonymisation rules (mandatory)

An example may enter this repository only when **every** box is ticked by the author **and** by a reviewer in the PR:

- [ ] Client, clinic, brand and domain names replaced (for example "Clinic A", `example-clinic.co.uk`)
- [ ] Practitioner names, titles, registration numbers and photos removed
- [ ] Locations generalised to region level at most (for example "a market town in the South East")
- [ ] No patient information of any kind: names, cases, ages, conditions, images, testimonials or review text
- [ ] No before/after images, consent forms or clinical notes
- [ ] Prices, revenue, lead volumes and analytics figures removed, or replaced by ranges/indices that cannot identify the client
- [ ] Unique positioning lines or brand ideas paraphrased so they cannot be traced back to the client
- [ ] Screenshots: none. Describe the layout in text instead.
- [ ] No content the client would recognise as their confidential commercial information
- [ ] Note in the example header: source stage, OS version, and "Anonymised: yes, reviewed by <name>"

If an example cannot be anonymised without losing what made it good, do not add it.
Describe the *pattern* in the SOP instead.

## Structure

```
examples/
└── anonymised-example-project/
    ├── README.md                 project summary (anonymised) + which OS version it ran on
    ├── 01-project-strategy-brief.md
    ├── 04-positioning-thesis.md
    └── …                         one file per artefact, named after the template number
```
