# Stage 05V: Creative Validation

**Website OS v1.1.** Sits between Stage 05T (Creative Translation) and Stage 06 (Page + Component System).

## Objective

Prove the creative idea survives without breaking acquisition, conversion or compliance, and that the assets to realise it exist or are commissioned, **before any production system is built**.

> SEO and CRO are constraints to design within, not excuses for generic design.

The LOCKED list from earlier stages wins every conflict: change the creative, never the invariant.

## Owner and review

- **Owner:** Strategist + SEO Lead
- **Reviewer:** Project Lead. Joe signs off anything consumer-facing, compliance-sensitive or making a regulatory claim.
- **Approval:** Yes. The client approves the keyframes. This replaces approving a mood board at Stage 05.

## Route

`CRO/SEO/compliance collision test → asset gate → client keyframe approval`

### 1. Collision test

Test every keyframe against the LOCKED invariants:

| Check | Pass condition |
|---|---|
| Crawlability | Navigation and discovery links are real, crawlable links |
| Real HTML | Core copy, headings and facts are HTML text, never inside images |
| H1 | One understandable H1; descriptive and local terms are carried by title, meta and section copy if not in the hero |
| Discovery | Users can find treatments by treatment and by concern |
| Proof | Proof sits near decisions; scopes are not combined across businesses |
| Provider clarity | Every service shows who provides it (clinic vs independent / partner) |
| Mobile | Primary choice and CTA visible in the first screen; touch targets 44px or more; labels 12px or more |
| Motion | Performant, pausable, and respects `prefers-reduced-motion` (WCAG 2.2.2) |
| Performance | Images sized and lazy-loaded below the fold; Core Web Vitals budget realistic |
| Feasibility | Each effect proven buildable in the native stack. Spike anything unproven |
| Compliance | Claims, results presentation, prescription-only medicine rules, consent |

### 2. Asset gate

This is a hard gate, not a note.

> We have the assets required to realise the design, or an approved production plan to obtain them.

Each SHOOT item in the Stage 05 asset matrix has a date and an owner. Nothing marked DO NOT FAKE is substituted.

Without this gate the loop is: placeholder design → placeholders dictate layout → component system gets built → proper photography arrives → photography doesn't fit → design gets compromised.

The correct order is: creative thesis → asset requirements → client shoot → final keyframes → systemisation.

### 3. Client keyframe approval

Present the keyframes (not mood boards) with the collision test summary. Record the decision in the Approval Record and add approved items to LOCKED DECISIONS in the Master Project Context.

## Definition of Done

- [ ] Collision test passed (or each failure fixed in the creative).
- [ ] Motion and performance feasible; unproven effects spiked in the native stack.
- [ ] Compliance check passed on the keyframes (Joe for consumer-facing content).
- [ ] **Asset gate passed.**
- [ ] Client keyframe approval recorded; LOCKED list unchanged by the creative.

## Next

Stage 06: Page + Component System, which reverse-engineers the approved keyframes.
