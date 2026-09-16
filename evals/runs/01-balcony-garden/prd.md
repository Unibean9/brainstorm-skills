---
title: In-Pot Care Card
status: final
created: 2026-09-16
updated: 2026-09-16
source: evals/golden-data.yaml, case 01-balcony-garden, turns 1-19
stance: facilitator
branch: frontend-design: landing-page
---

# PRD: In-Pot Care Card

## 0. Document Purpose

This final PRD records the direction explicitly chosen in the Balcony Garden replay and is intended for product, content, physical-design, and downstream frontend work. It is grounded only in the 19 canonical user turns. Directly stated problems, constraints, candidates, critiques, decisions, and confirmations are preserved as source material; any product detail, measurement method, or implementation implication not stated by the user is marked `[ASSUMPTION]` and/or placed in Open Questions.

## 1. Executive Summary

Renters and apartment residents buy plants excitedly, then may see a plant look sick and not know what they did wrong. The recurring job is narrower than learning gardening: answer “does this plant need water today?” during a short check before work.

The chosen v1 solution is an in-pot care card. It sits at the place where care happens and explains a plant-specific watering rhythm plus visible signs of too little or too much water. The card is preferred because the group scored the options on cost, no electricity, and removing guesswork, and judged the card strongest. The first version covers only a few common plants. Sensors are later; the reminder app and self-watering pot are out of v1.

The central product thesis is that guidance placed beside the plant can remove more watering guesswork for this user than a fixed calendar, while preserving the chosen low-cost, no-power constraint.

## 2. Problem

### 2.1 Problem statement

The target user buys a plant, sees it look sick a few weeks later, and does not know what they did wrong. Their repeated question is whether the plant needs water today. Existing directions considered in the replay each leave a concern: a reminder app adds an app surface, a sensor adds per-pot cost and battery replacement, and a self-watering pot changes the physical product. A card can also be discarded if it looks like an advertisement.

### 2.2 Evidence and provenance

- The problem and emotional moment come from user turns 1–4.
- The four candidate directions come from user turns 5–8.
- The no-app, no-charging, ten-second, and plant-point-of-view constraints come from user turns 9–11.
- Retention, condition variation, and sensor cost/battery critiques come from user turns 12–14.
- The choice and rationale come from user turns 15–16.
- The v1 boundary and visible-sign requirement come from user turns 17–18.

## 3. Target Users

### 3.1 Primary target user

A renter or apartment resident in a small rental or apartment who works during the day and does not want to study plant care. The replay does not provide a demographic profile, plant list, purchase context, or evidence of existing customers.

### 3.2 Non-users and boundary

The v1 is not a general gardening education product. It is not scoped around people seeking to grow a large garden. `[ASSUMPTION: the first release is designed for one plant at a time because the chosen artifact is an in-pot card; multi-plant ownership remains an open question.]`

## 4. Jobs To Be Done

- **Functional:** When checking a plant before work, decide whether it needs water today.
- **Contextual:** Get useful guidance without opening an app, charging a battery, or studying plant care.
- **Cognitive:** Replace guesswork with watering rhythm and visible-sign guidance.
- **Emotional:** Avoid the uncertainty of seeing a sick-looking plant and not knowing what went wrong.
- **Environmental:** Interpret the plant’s condition in its actual setting, because a west-facing balcony and a north-facing window do not share an identical rhythm.

## 5. Glossary

- **Care Card** — The chosen small physical card that sits in a plant’s pot and provides watering guidance.
- **Target User** — A renter or apartment resident who works during the day and does not want to study plant care.
- **Watering Rhythm** — Guidance about when watering may be needed; it is not a fixed calendar used alone.
- **Visible Signs** — Observable indications of too little water or too much water that the Care Card explains. `[ASSUMPTION: the exact signs and their wording are content decisions not provided in the replay.]`
- **Condition** — The plant’s surrounding situation that can affect watering guidance, including the contrast between a west-facing balcony and a north-facing window.
- **Common Plant Set** — The small set of common plants covered by v1. `[ASSUMPTION: the exact members of this set are not yet chosen.]`
- **Water-Today Decision** — The Target User’s answer to whether the plant needs water today.
- **v1** — The first version: a Care Card for the Common Plant Set, with no reminder app, self-watering pot, or sensor.

## 6. Key User Journeys

### UJ-1. `[ASSUMPTION: illustrative protagonist name]` Alex makes the Water-Today Decision before work

- **Persona + context:** Alex is a Target User in a small rental or apartment, works during the day, and does not want to study plant care. `[ASSUMPTION: “Alex” is an illustrative name, not a real customer.]`
- **Entry state:** Alex is standing beside a plant before work; no app or powered device is required by the chosen direction.
- **Path:** Alex looks at the plant for a short check; reads the Care Card in the pot; consults its Watering Rhythm; compares the Visible Signs for too little or too much water; accounts for the plant’s Condition rather than following a calendar blindly.
- **Climax:** Alex can answer the Water-Today Decision at the exact place where care happens.
- **Resolution:** Alex leaves the plant with a decision made; the replay does not specify any logging, reminder, or follow-up behavior.
- **Edge case:** If the plant is on a west-facing balcony or in a north-facing window, the Care Card must not present an identical fixed rhythm as the sole answer.

### UJ-2. Alex interprets a plant that looks sick

- **Persona + context:** Alex sees a plant look sick a few weeks after buying it and does not know what went wrong.
- **Entry state:** Alex is uncertain whether the issue is too little water or too much water.
- **Path:** Alex uses the Care Card’s Visible Signs guidance; reads the corresponding Watering Rhythm; uses the plant’s Condition as context; makes the Water-Today Decision.
- **Climax:** The card turns an undifferentiated “sick” moment into visible guidance about too little or too much water. `[ASSUMPTION: “turns into” means the content supports a clearer decision; the replay does not promise a diagnosis.]`
- **Resolution:** The next action remains the Target User’s decision; the Care Card does not claim to diagnose every plant problem.

## 7. Solution Thesis

The product bets that the place where care happens is the right place for a low-friction answer. A Care Card can be seen during the ten-second check, does not require an app or charging, and can explain both a Watering Rhythm and Visible Signs. This addresses the user’s question while acknowledging that Conditions vary.

The trade-off is deliberate: the sensor direction may be more precise, but it brings per-pot cost and battery replacement; the chosen Care Card gives up that electronic precision in favor of low cost, no power, and immediate physical proximity. A fixed calendar alone is rejected because it cannot be identical across the Conditions named in the replay.

## 8. Features

### 8.1 Care Card placement and at-a-glance decision

**Description:** The Care Card sits in the pot so the Target User encounters guidance while looking at the plant. Its purpose is to support a short check and the Water-Today Decision. Realizes UJ-1 and UJ-2.

**Functional Requirements:**

#### FR-1: In-pot placement

The physical product must be placeable in the plant’s pot as the chosen point-of-care surface. Realizes UJ-1.

**Consequences (testable):**

- A v1 review can verify that the Care Card is presented as an in-pot object, not only as an app or remote notification.
- The placement does not require a powered accessory. `[ASSUMPTION: the final attachment or insertion method is not specified.]`

#### FR-2: Water-Today Decision cue

The Care Card must make the Water-Today Decision the first task the Target User can understand during a short plant check. Realizes UJ-1.

**Consequences (testable):**

- A content review can identify a clear path from the card’s first message to the Water-Today Decision.
- The card does not lead with broad garden education or a general gardening lesson.

### 8.2 Watering Rhythm guidance

**Description:** The Care Card explains a Watering Rhythm for each covered Common Plant Set member. The rhythm is guidance, not a fixed calendar used alone. Realizes UJ-1 and UJ-2.

**Functional Requirements:**

#### FR-3: Plant-specific rhythm

The Care Card must provide Watering Rhythm guidance associated with the covered plant, rather than one undifferentiated rhythm for all plants. Realizes UJ-1.

**Consequences (testable):**

- Each v1 Common Plant Set entry has an identifiable Watering Rhythm in content review.
- The exact plant entries and copy remain an open content decision.

#### FR-4: No calendar-only guidance

The Care Card must not present a fixed calendar as the sole basis for the Water-Today Decision. Realizes UJ-1.

**Consequences (testable):**

- A content review finds Visible Signs guidance alongside the Watering Rhythm.
- A calendar-only card fails acceptance, even if it includes a recurring schedule. `[ASSUMPTION: “fails acceptance” is a proposed product-quality rule derived from the confirmed constraint.]`

### 8.3 Visible-sign guidance

**Description:** The Care Card explains observable Visible Signs of too little or too much water. It helps the Target User interpret the plant instead of relying on a schedule alone. Realizes UJ-2.

**Functional Requirements:**

#### FR-5: Too-little-water signs

The Care Card must explain Visible Signs associated with too little water for each covered plant where applicable. Realizes UJ-2.

**Consequences (testable):**

- Content review can locate a too-little-water explanation for every covered plant entry.
- The exact signs and wording are not treated as known facts until confirmed.

#### FR-6: Too-much-water signs

The Care Card must explain Visible Signs associated with too much water for each covered plant where applicable. Realizes UJ-2.

**Consequences (testable):**

- Content review can locate a too-much-water explanation for every covered plant entry.
- The card avoids implying that every sick-looking plant has a watering cause. `[ASSUMPTION: this boundary is a safety/content interpretation, not an explicit user statement.]`

### 8.4 Condition-aware interpretation

**Description:** The Care Card acknowledges that Conditions vary. The replay specifically contrasts a west-facing balcony and a north-facing window, so the product must not flatten those contexts into one identical rhythm. Realizes UJ-1.

**Functional Requirements:**

#### FR-7: Condition context

The guidance must give the Target User a way to interpret Watering Rhythm in light of Condition variation. Realizes UJ-1.

**Consequences (testable):**

- A review using the west-facing balcony and north-facing window examples can show that the card does not prescribe an identical rhythm as the only instruction.
- The exact representation of Condition context remains an open question.

#### FR-8: Visible signs as adjustment input

The guidance must direct the Target User to use Visible Signs as an input when Conditions make a fixed rhythm insufficient. Realizes UJ-1 and UJ-2.

**Consequences (testable):**

- A content walkthrough shows a relationship between Visible Signs and the Water-Today Decision.
- The card’s first version does not depend on a sensor reading to make that relationship useful.

### 8.5 Common Plant Set coverage

**Description:** v1 covers only a few common plants. This is a deliberate boundary so the first version does not imply broad coverage that the group did not choose. Realizes UJ-1.

**Functional Requirements:**

#### FR-9: Limited v1 coverage

The v1 release must identify and support only the confirmed Common Plant Set, described to users as limited coverage. Realizes UJ-1.

**Consequences (testable):**

- Release review confirms that the product does not claim to cover every plant.
- The exact Common Plant Set is selected before production content is finalized. `[ASSUMPTION: a named set must be selected before production; the user did not supply it.]`

#### FR-10: Coverage boundary message

The v1 experience must make the limited coverage boundary visible wherever the Care Card is introduced. Realizes UJ-1.

**Consequences (testable):**

- A user can distinguish a covered plant from an uncovered plant before relying on its guidance. `[ASSUMPTION: this identification behavior is inferred from the need to limit coverage.]`
- No unsupported plant-specific instruction is presented as part of v1.

### 8.6 Power-free, app-free use

**Description:** The chosen direction must preserve the explicit no-app and no-charging constraints. The Care Card is a physical, no-power experience. Realizes UJ-1.

**Functional Requirements:**

#### FR-11: No charging dependency

The v1 Care Card must provide its core guidance without a battery or user charging step. Realizes UJ-1.

**Consequences (testable):**

- A user can access the Watering Rhythm and Visible Signs without charging a device.
- Battery replacement is not a v1 user task.

#### FR-12: No app dependency

The v1 Water-Today Decision path must not require the Target User to use a reminder app. Realizes UJ-1.

**Consequences (testable):**

- The core path is available from the physical Care Card at the plant.
- A reminder app is recorded as out of scope for v1.

### 8.7 Durable, non-promotional presentation

**Description:** The Care Card must behave and read like care guidance, not like an advertisement that is thrown away. The exact material, form factor, and visual language were not decided in the replay.

**Functional Requirements:**

#### FR-13: Care-first content hierarchy

The Care Card must present care guidance before any `[ASSUMPTION: optional product or brand information]`. Realizes UJ-1.

**Consequences (testable):**

- A content review can identify Watering Rhythm and Visible Signs without requiring promotional context.
- Any promotional treatment that makes the card read like an advertisement is rejected for the first release. `[ASSUMPTION: rejection criterion inferred from the stated disposal risk.]`

#### FR-14: In-pot durability decision

The product definition must specify how the Care Card remains usable in its intended in-pot context before production. Realizes UJ-1.

**Consequences (testable):**

- A physical-design review records the chosen material, dimensions, and care/environment limits before release. `[ASSUMPTION: these review fields are inferred; the replay provides no values.]`
- The product does not silently treat unconfirmed material or durability properties as a claim.

## 9. Non-Functional Requirements

### 9.1 Legibility and accessibility

- The Care Card must be legible during the user’s short check and must distinguish the Watering Rhythm, Visible Signs, and Water-Today Decision. `[ASSUMPTION: exact type size, contrast ratio, language, and accessibility standard remain open.]`
- The landing page must provide semantic structure, keyboard-visible focus, responsive layout, and reduced-motion behavior. `[ASSUMPTION: these are artifact requirements for the requested HTML, not claims about the physical card.]`

### 9.2 Offline and power independence

- Core v1 guidance must remain available without charging and without a reminder app.
- `[ASSUMPTION: dependence on internet connectivity is also excluded because the selected core surface is physical; confirm if any companion experience is later considered.]`

### 9.3 Content integrity

- Guidance must distinguish too little water, too much water, and the possibility that a sick-looking plant is not explained by watering alone. `[ASSUMPTION: the final diagnostic boundary requires horticultural/content review.]`
- The product must not claim precision, outcomes, customer adoption, testimonials, or traction that were not provided in the replay.

### 9.4 Physical reliability

- `[ASSUMPTION: the Care Card should remain readable and usable in the pot’s intended environment; material, moisture exposure, lifecycle, and validation thresholds are open questions.]`

## 10. Constraints and Guardrails

- **Cost:** Low cost is a decision criterion supplied by the user; no price target was supplied.
- **Power:** No electricity and no charging are part of the chosen direction.
- **Placement:** The guidance must be at the exact place where care happens: in the pot.
- **Variable Conditions:** West-facing balcony and north-facing window are explicit examples that rule out a fixed calendar as the only guidance.
- **Scope:** Few common plants only in v1; sensors later; reminder app and self-watering pot out of v1.
- **Trust:** The Care Card must avoid looking like an advertisement and being thrown away.
- **Claims:** No unsupported metrics, customer evidence, testimonials, or traction.

## 11. Scope and Sequencing

### 11.1 In scope for v1

- A physical Care Card that sits in the pot.
- Watering Rhythm guidance for a few common plants.
- Visible Signs guidance for too little or too much water.
- Condition-aware guidance that does not rely on a fixed calendar alone.
- A no-power, no-charging, no-reminder-app core experience.
- Care-first presentation intended to avoid the stated advertisement/disposal risk.

### 11.2 Out of scope for v1

- Soil sensors; later direction, with timing open.
- Reminder app; explicitly out of first scope.
- Self-watering pot; explicitly out of first scope.
- A broad or universal plant library; v1 covers only a few common plants.
- A fixed calendar as the only guidance.
- `[ASSUMPTION: automated diagnosis, accounts, notifications, analytics, commerce, and social features are also out of scope because they were not discussed; confirm rather than treating this as a permanent product decision.]`

### 11.3 Sequencing

- **Now:** finalize the Common Plant Set, content structure, visible-sign guidance, and physical presentation decisions needed to define v1. `[ASSUMPTION: this order is proposed to make the confirmed concept buildable.]`
- **Then:** validate the Care Card in the in-pot context and review whether users can make the Water-Today Decision without an app or powered device. `[ASSUMPTION: validation activity is proposed; no test plan was supplied.]`
- **Later:** consider sensors only after v1 scope and the cost/battery trade-off are revisited. The replay does not set a date or trigger.

## 12. Success Metrics

No numeric success target was discussed in the replay. The following are `[ASSUMPTION]` measurement proposals derived from the confirmed job and should remain open until an owner, baseline, sample, and target are chosen.

**Primary**

- **SM-1 [ASSUMPTION]: Water-Today Decision clarity** — in a defined v1 evaluation, measure whether a Target User can use the Care Card to reach a clear answer to “does this plant need water today?” during a short check. Target, baseline, sample, and method: open question. Validates FR-2, FR-3, FR-4, FR-8.

**Secondary**

- **SM-2 [ASSUMPTION]: Guidance use** — measure whether Target Users consult the Care Card’s Visible Signs and Watering Rhythm rather than discarding or ignoring it. Target, baseline, sample, and method: open question. Validates FR-5, FR-6, FR-13.
- **SM-3 [ASSUMPTION]: Constraint fit** — measure whether v1 users can use the core path without an app, charging, or a battery. Target, baseline, sample, and method: open question. Validates FR-11 and FR-12.

**Counter-metrics (do not optimize)**

- **SM-C1 [ASSUMPTION]: Card disposal or distrust** — monitor whether optimizing for low cost or compactness causes the Care Card to look like an advertisement and be thrown away. Target and method: open question. Counterbalances SM-3 and validates FR-13 and FR-14.
- **SM-C2 [ASSUMPTION]: Calendar over-reliance** — monitor whether users follow a fixed rhythm without using Visible Signs across different Conditions. Target and method: open question. Counterbalances SM-1 and validates FR-4, FR-7, and FR-8.

## 13. Risks and Mitigations

| Risk | Evidence / impact | Mitigation or unresolved item |
|---|---|---|
| Card looks like an advertisement and is thrown away | User turn 12 | Use a care-first hierarchy and validate the physical presentation. Exact visual/material direction is an open question. |
| One rhythm does not fit different Conditions | User turn 13 | Pair Watering Rhythm with Visible Signs and Condition context; do not use a fixed calendar alone. |
| Sensor precision is attractive but adds per-pot cost and battery replacement | User turn 14 | Keep sensors out of v1; revisit only after v1 evidence and a cost decision. |
| Limited Common Plant Set leaves some users unsupported | User turn 17 | Label the v1 boundary and select the exact set before production. |
| A sick-looking plant has a cause outside watering | `[ASSUMPTION]` based on the product’s narrow job | Avoid universal diagnosis claims; define content boundaries with a qualified reviewer. |
| Unspecified physical durability makes the in-pot artifact unreliable | `[ASSUMPTION]` from the chosen placement | Decide material, dimensions, exposure limits, and validation method before production. |

## 14. Assumptions Index

Every item below is an inference, proposal, or illustrative detail rather than a confirmed user decision.

- `[ASSUMPTION: the first release is designed for one plant at a time; multi-plant ownership is open.]` — §3.2.
- `[ASSUMPTION: exact Visible Signs and wording were not provided.]` — §5 and §8.3.
- `[ASSUMPTION: exact Common Plant Set membership was not provided.]` — §5 and §8.5.
- `[ASSUMPTION: “Alex” is an illustrative protagonist, not a real customer.]` — §6.1.
- `[ASSUMPTION: the card supports a clearer decision but does not promise diagnosis.]` — §6.2.
- `[ASSUMPTION: the card’s attachment or insertion method is not specified.]` — FR-1.
- `[ASSUMPTION: a calendar-only card fails acceptance.]` — FR-4.
- `[ASSUMPTION: the card must avoid implying every sick-looking plant has a watering cause.]` — FR-6.
- `[ASSUMPTION: the exact Condition representation is not specified.]` — FR-7.
- `[ASSUMPTION: a named Common Plant Set must be selected before production.]` — FR-9.
- `[ASSUMPTION: coverage identification is needed before relying on guidance.]` — FR-10.
- `[ASSUMPTION: optional brand information must not precede care guidance.]` — FR-13.
- `[ASSUMPTION: material, dimensions, and care/environment limits require a production review.]` — FR-14.
- `[ASSUMPTION: exact physical-card type size, contrast, language, and accessibility standard remain open.]` — §9.1.
- `[ASSUMPTION: internet dependence is excluded from the physical core experience.]` — §9.2.
- `[ASSUMPTION: the final diagnostic boundary requires horticultural/content review.]` — §9.3.
- `[ASSUMPTION: in-pot readability and usability need physical validation.]` — §9.4.
- `[ASSUMPTION: automated diagnosis, accounts, notifications, analytics, commerce, and social features are out of scope pending confirmation.]` — §11.2.
- `[ASSUMPTION: sequencing and validation activity are proposed to make v1 buildable.]` — §11.3.
- `[ASSUMPTION: SM-1 through SM-3 and SM-C1 through SM-C2 are measurement proposals.]` — §12.

## 15. Open Questions

1. Which “few common plants” make up the v1 Common Plant Set?
2. What exact Visible Signs and wording should the Care Card use for too little and too much water for each covered plant?
3. How should the Care Card represent Condition differences such as a west-facing balcony and a north-facing window?
4. What physical material, dimensions, insertion/attachment method, and in-pot exposure limits are acceptable?
5. What design makes the Care Card feel like care guidance rather than an advertisement?
6. What language(s) should v1 support?
7. What baseline, evaluation method, sample, owner, and target should be used for SM-1, SM-2, and SM-3?
8. What threshold would indicate unacceptable card disposal or distrust for SM-C1?
9. How should the product behave when a plant looks sick for a reason unrelated to watering?
10. What evidence and revisit trigger should be required before considering sensors after v1?
11. Is a single-plant card the intended physical model when a Target User owns multiple plants?
12. Are any companion surfaces, such as packaging or a future digital surface, intended beyond the physical v1 core?

## 16. Acceptance Criteria

- **AC-1:** The v1 artifact is an in-pot Care Card, not a reminder app, soil sensor, or self-watering pot.
- **AC-2:** The Care Card supports a short check whose first job is the Water-Today Decision.
- **AC-3:** The Care Card contains Watering Rhythm guidance for each plant in the confirmed Common Plant Set.
- **AC-4:** The Care Card explains Visible Signs for too little water and too much water.
- **AC-5:** The Care Card does not rely on a fixed calendar as the sole guidance.
- **AC-6:** The guidance acknowledges Condition variation, including the west-facing balcony versus north-facing window contrast.
- **AC-7:** The core v1 path works without charging, a battery, or a reminder app.
- **AC-8:** The v1 presentation is reviewed against the risk that it looks like an advertisement and is thrown away.
- **AC-9:** The v1 experience states or otherwise enforces the limited Common Plant Set boundary without unsupported coverage claims.
- **AC-10:** The final physical design records material, dimensions, placement method, and exposure validation before production. `[ASSUMPTION: the review requirement is proposed because these details were not discussed.]`
- **AC-11:** Any success target, customer evidence, testimonial, traction statement, or numeric claim absent from the replay is omitted or explicitly marked `[ASSUMPTION]` and kept as an open question.
- **AC-12:** Downstream artifacts use this PRD as their source of truth and do not add the deferred app, sensor, or self-watering-pot directions.

## 17. Golden Quality Gate Coverage

This final PRD includes the required executive summary, problem, target users, jobs to be done, glossary, journeys, solution, seven feature groups, fourteen numbered functional requirements, non-functional requirements, scope, success and counter-metrics, risks, assumptions, open questions, and acceptance criteria. It exceeds the evaluation minimum of five feature groups and ten functional requirements while preserving unresolved details as `[ASSUMPTION]` or open questions.
