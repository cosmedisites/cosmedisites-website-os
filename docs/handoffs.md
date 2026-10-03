# Role handoff workflow

Every handoff lets the next person work **without re-reading the whole project**.
Prompts: [prompts/team-handoffs/role-handoff-prompts.md](../prompts/team-handoffs/role-handoff-prompts.md)

## Where handoffs happen

| Handoff | Prompt | Stage | Delivered as |
|---|---|---|---|
| Project Lead → Strategist | H01 | before 00 | Comment on the S00 stage task + MPC link |
| Strategist → SEO Lead | H02 | 03 → 04 | Comment on the S04 stage task |
| **Strategist → Designer** | **H03** (+ 5C design brief) | 03/04 → 05 | Doc in Drive `05_Visual/`, linked on the S05 task |
| SEO Lead → Designer | H04 | 04 → 05/06 | Doc in Drive, linked on the S05/S06 task |
| **Designer → Developer** | **H05 + 11A + 11B + 11C** | 10 → 11 | **Build Handoff** (Template 14) in Drive, linked on the S11 task |
| Content Lead → Compliance Reviewer | H06 | 07 / 12 | Linked on the QA — Compliance task |
| QA → Project Lead | H07 | 12 → 13 | Linked on the S13 task |
| **Project Lead → Client** | **H08** + C01–C09 | any | Sent from the Chirply inbox |

When the owner changes, the **handoff is a DoD item of the outgoing stage**, not an optional extra.

## The buckets

The pack's standard buckets (AI Operating Rules §10) are used in every handoff:

| Bucket | Meaning |
|---|---|
| LOCKED | Approved decisions the next role must preserve |
| REQUIRED | Things the next role must include / solve |
| FLEXIBLE | Where judgement is encouraged |
| OPEN | Known unknowns, each with owner and next action |
| DO NOT CHANGE | Constraints that need explicit re-approval before changing |

**Designer-facing handoffs** (H03 Strategist → Designer and prompt 5C) use a variant (decision D4, v1.1):

| Bucket | Meaning |
|---|---|
| LOCKED | Approved decisions; changing them needs explicit re-approval (covers DO NOT CHANGE) |
| FLEXIBLE | Where design judgement is encouraged |
| REQUIRED | What the design must include or solve |
| AVOID | Patterns, signals and treatments the design must not use: the wrong perception, what the design must not signal (3B), wrong-category cues, fabricated or placeholder proof presented as real |
| OPEN | Unresolved items, each with owner and next action |

Source: SOP Stage 5 *Designer handoff format*; AI Operating Rules §10.

## Strategist → Designer: required contents

| Must communicate | Source in the methodology |
|---|---|
| LOCKED / FLEXIBLE / REQUIRED / AVOID / OPEN | H03, 5C; SOP Stage 5 |
| Positioning thesis | 3B / Template 04 |
| Desired (three-second) perception | 3B |
| Wrong perception | 3B |
| Priority patient journeys | H03; 4B user states |
| Priority services | 3B |
| Brand hierarchy (clinic / practitioner / location) | 3C |
| Proof requirements (trust/proof that must appear) | H03; 7A |
| SEO constraints affecting design | H03 + H04 |
| Content gaps | 7B Content Gap Plan |
| CTA hierarchy, photography direction, distinctive brand ideas | H03 |

Run H03 for the core handoff. Attach H04 and the 7B output when available.

## Designer → Developer: required contents

The authoritative list is **SOP Stage 11, "Developer receives"**, reinforced by Playbook §22
(*Build Handoff*: "The designer should not hand the developer 'some screens'"). It is captured in a
single **Build Handoff** (Template 14), assembled with three prompts:

SOP list: approved screens · responsive behaviour · component library · typography · colour tokens ·
button states · navigation behaviour · image ratios · content states · empty states · SEO architecture ·
redirect requirements · approved copy/content · tracking requirements.

| Must include | Prompt |
|---|---|
| Approved designs (screen/version links) | 11A / H05 |
| Responsive behaviour | 11A / H05 |
| Component states (buttons, empty, loading, error) | 11A / H05 |
| Typography and colour tokens | 11A |
| Image ratios / crops | 11A / H05 |
| Navigation behaviour | 11A / H05 |
| Forms | 11A / H05 |
| Content states (known content variability, optional components disappearing cleanly) | H05 / 11C |
| SEO architecture (URLs, canonicals, indexation, structured data) | 11B |
| Redirects (old → new map) | 11B (from 4D) |
| Tracking requirements (analytics, forms, booking, calls, consent) | 11B |

Rule (11A): **do not leave material UX decisions for the developer to invent.** Each OPEN item
states its owner, its deadline, and whether build can proceed without it.

## Project Lead → Client

Use **H08** for status updates and the **C01–C09** prompts for milestone communications. Send them
from Chirply so they sit on the client timeline.

Translation rules (AI Operating Rules §7 and the Quickstart client-language rule):
- "IA" → "site structure / how patients find information"; "CRO" → "booking / enquiry conversion";
  "component system" → "reusable page and design system"; no unexplained acronyms.
- Ask for **explicit decisions**, never "let us know what you think".
- Keep **approval requests separate from production-input requests**.
- Don't expose internal stage numbers, decision levels, AI use or team debate. **Don't hide a
  material blocker.**
- Don't promise numerical uplift without evidence.
