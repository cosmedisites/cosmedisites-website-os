# Stage 05T: Creative Translation

**Website OS v1.1.** Sits between Stage 05 (Brand + Visual Direction) and Stage 05V (Creative Validation).

## Why this stage exists

The repeatable failure mode in clinic redesigns: strategy is solved, IA is solved, CRO and SEO are protected, and then the design is translated into a safe component system too early. The result is a technically good clinic website that looks generic.

This stage closes that gap. **Create the memorable experience first, then reverse-engineer the reusable system from it.** The Elementor system is the industrialisation of the approved creative direction, not the source of it.

> CRO and SEO define the constraints. They do not define the aesthetic.

## Objective

Produce 3 to 4 high-fidelity keyframes using real client assets that show what the brand should feel like at its best, at the top end of what the build stack can support, scaled to the project's Creative Intensity.

## Inputs

- Stage 00: Creative Intensity rating and the LOCKED list of strategic invariants.
- Stage 05: Brand DNA, MATCH / BEAT / AVOID board, creative thesis with 3 to 5 principles and anti-goals, asset matrix (USE / SHOOT / SOURCE / DO NOT FAKE).
- Real client assets (premises, people, treatments, training, social content). Placeholders are allowed only where the asset matrix says SHOOT, and they must not dictate the layout.

## Owner and review

- **Owner:** Designer / Creative Lead
- **Reviewer:** Strategist + Project Lead
- **Approval:** internal here; the client sees the keyframes at Stage 05V.

## Route

`keyframes → Brand Swap Test → generic-design red team` (iterate until both pass)

### 1. Keyframes

Design 3 to 4 moments, not the whole website. Usually:

1. Hero / first viewport
2. Discovery / commerce (treatment and concern discovery)
3. Proof / results
4. People / brand / education

Desktop and mobile for each. Use the client's real photography and video wherever it exists.

**The creative ceiling question.** Do not ask "what can Elementor do?" Ask "what should this experience be, and how do we build that intelligently in Elementor?" With Elementor Atomic, the MCP, modern CSS, video, sliders, controlled motion, responsive media and reusable global systems, the ceiling is far beyond standard templates. Explore it deliberately, then scale to the Creative Intensity rating:

| Creative Intensity | What the keyframes should explore |
|---|---|
| Conservative | Clean, credible, clear hierarchy; restrained motion; strong photography still required |
| Elevated | Distinct brand moments, editorial layout, purposeful motion, visual discovery |
| High-expression | Cinematic hero (video or motion), asymmetric editorial layouts, visual treatment and results discovery, personality-led people, social-native modules |

**Do not start a component library in this stage.** No "hero component", "card component" or "CTA component" thinking until Stage 06. Thinking in components too early produces a site that looks like a component library.

### 2. Brand Swap Test

Hide the logo and business name. Ask:

1. Could this reasonably be five other clinics? If yes, it fails.
2. What makes this recognisably this clinic? Name it: architecture, photography, people, typography, motion, colour, a proprietary framework, unusual layout behaviour, treatment or results presentation, distinctive copy, the physical environment, founder personality.

It does not need to be weird. It needs to be specific.

### 3. Generic-design red team

Reject and iterate if any of these dominate:

- beige / black luxury clichés
- identical card grids
- serif-heavy typography used as a substitute for identity
- meaningless whitespace
- generic claims
- over-systemised symmetry
- placeholder imagery dictating the layout

## Definition of Done

- [ ] 3 to 4 high-fidelity keyframes built with real client assets, desktop and mobile.
- [ ] Creative ceiling explored and scaled to the Creative Intensity rating.
- [ ] Brand Swap Test passed, with the distinctive elements named.
- [ ] Generic-design red team passed.
- [ ] The keyframes answer "would the target customer actually want this brand?"
- [ ] No fabricated proof, no AI-generated before/after, no placeholder dictating the aesthetic.
- [ ] No component library started. Keyframes saved to `S05T_Creative-Translation` in the project Drive folder and linked on the Chirply task.

## Output

Keyframes (an HTML prototype is the default format), plus a short note recording the Brand Swap Test answer and the red-team result.

## Next

Stage 05V: Creative Validation.

## Reference case

HAUS of DRA (October 2026). See `case-studies/haus-of-dra-creative-translation.md`.
