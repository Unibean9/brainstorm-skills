---
case: 01-balcony-garden
title: Balcony Garden
mode: headless replay
stance: facilitator
branch: frontend-design: landing-page
source: evals/golden-data.yaml
---

# Recorded Replay — Balcony Garden

The 19 user turns below are reproduced verbatim from `evals/golden-data.yaml`. Assistant responses are concise facilitation records; user-originated ideas and decisions remain attributed to the user.

## Opening

1. **User:** I want to help renters keep plants alive, but I do not know whether this should be an app or a physical product.

   **Assistant:** I’m capturing the desired outcome and the unresolved form-factor choice. **Question:** What is the moment when a renter most needs help keeping the plant alive?

## Framing

2. **User:** What bothers me is that people buy a plant excitedly, then a few weeks later it looks sick and they do not know what they did wrong.

   **Assistant:** The problem is a post-purchase care gap: the plant looks sick, and the owner cannot tell which action caused it. **Question:** What single decision would make that moment easier?

3. **User:** The target is someone in a small rental or apartment who works during the day and does not want to study plant care.

   **Assistant:** The target user is a renter or apartment resident with limited time and no wish to become a plant-care student. **Question:** What would this person ask repeatedly during an ordinary week?

4. **User:** The repeated question is not how to grow a big garden. It is simply: does this plant need water today?

   **Assistant:** The core job is now precise: help answer “does this plant need water today?” rather than teach gardening broadly. **Question:** What different ways could the product help answer that question?

## Diverging

5. **User:** One direction is an app that schedules watering for each plant.

   **Assistant:** I’m recording the app-and-schedule direction as one candidate. **Question:** What would the renter gain, and what would they still have to remember?

6. **User:** Another direction is a soil sensor that sends a phone notification.

   **Assistant:** I’m recording the sensor-and-notification direction as a second candidate. **Question:** What would this direction make easier at the exact place where care happens?

7. **User:** We could make a self-watering pot so the person does not need to remember.

   **Assistant:** I’m recording the self-watering-pot direction as a third candidate. **Question:** Which part of the watering decision would this direction remove, and which part would remain?

8. **User:** Or we could make a small card that sits in the pot and explains the watering rhythm and visible signs of too little or too much water.

   **Assistant:** I’m recording the in-pot care card as a fourth candidate, including watering rhythm and visible signs for too little or too much water. **Question:** What constraint would reveal which candidate fits this renter best?

## Shifting

9. **User:** If the user does not want an app and does not want to charge a battery, which direction still works?

   **Assistant:** This reframes the choice around no app and no charging. The candidates can now be considered against a power-free, low-friction use case. **Question:** What must remain useful if the product has no electronic surface?

10. **User:** If the user looks at the plant for ten seconds before work, what should the product tell them first?

   **Assistant:** The first message must serve a ten-second check before work and lead to the water-today decision. **Question:** What information must be visible before anything explanatory?

11. **User:** What would the product look like from the plant's point of view rather than the owner's point of view?

   **Assistant:** The perspective shifts from an owner’s schedule to the plant’s condition at the point of care. **Question:** What would the plant’s visible condition need the product to make legible?

## Critiquing

12. **User:** The card could look like an advertisement and be thrown away.

   **Assistant:** The care card has a retention risk: if it reads like advertising, the user may discard it before it helps. **Question:** What would make it feel like part of caring for the plant rather than promotional material?

13. **User:** A watering rhythm cannot be identical for a west-facing balcony and a north-facing window.

   **Assistant:** A fixed watering calendar is not sufficient across different light conditions; west-facing balconies and north-facing windows may need different guidance. **Question:** What should the product show alongside a rhythm so the user can adjust to conditions?

14. **User:** A sensor is more precise, but cost grows with every pot and the user has to replace batteries.

   **Assistant:** The sensor offers precision but introduces per-pot cost and battery replacement. The trade-off is now explicit: precision versus the low-cost, no-power constraint. **Question:** Which kind of guidance is valuable enough to keep if precision hardware is deferred?

## Converging

15. **User:** If we score the options on cost, no electricity, and removing guesswork, the card is strongest.

   **Assistant:** The group’s scoring criteria are cost, no electricity, and removing guesswork; the user states that the card is strongest on those criteria. This is the convergence signal.

16. **User:** The group chooses the in-pot care card because it is cheap, needs no power, and answers the question at the exact place where care happens.

   **Assistant:** Convergence is explicit: the in-pot care card is the chosen direction. The rationale is user-provided—cheap, no power, and located where care happens—and the app, sensor, and self-watering-pot options remain alternatives rather than decisions.

## Confirmation

17. **User:** The first version covers only a few common plants. Sensors are later. The reminder app and self-watering pot are out of the first scope.

   **Assistant:** Scope confirmation recorded: v1 covers a few common plants; sensors are later; the reminder app and self-watering pot are out of v1. No plant list or later timing was specified.

18. **User:** The card must explain visible signs, not just give a fixed calendar, because conditions vary.

   **Assistant:** Product behavior confirmed: the card explains visible signs and does not rely on a fixed calendar alone, because conditions vary. This constraint will govern the PRD and page.

## Handoff

19. **User:** Lock this direction, create a complete PRD, and then create one self-contained HTML landing page using prd.md. Anything we did not discuss must remain an open question or an [ASSUMPTION].

   **Assistant:** Handoff accepted. I’m locking the confirmed in-pot care card direction, creating the complete final PRD, and deriving one self-contained landing page from that PRD. Unspecified details will remain open questions or be marked `[ASSUMPTION]`.
