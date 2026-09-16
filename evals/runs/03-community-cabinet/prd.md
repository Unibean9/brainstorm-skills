---
title: Community Cabinet
status: final
created: 2026-09-16
updated: 2026-09-16
---

# PRD: Community Cabinet

## 0. Document Purpose

This PRD translates the canonical facilitator replay into a buildable pilot brief for the building committee and the team responsible for the first neighborhood cabinet. It uses the recorded user turns as the source of product decisions, groups capabilities into feature groups, numbers functional requirements globally, and marks every inference as `[ASSUMPTION]`. It is intentionally explicit about what is not promised: this is a one-neighborhood pilot, not a citywide network or open marketplace.

## 1. Executive Summary

Community Cabinet is a shared physical cabinet for household tools that are used only a few times a year. Residents can discover what is available, borrow it, return it, and leave a condition history without relying on an open marketplace conversation. QR codes connect the physical cabinet to the item and its current borrowing record. One neighborhood steward coordinates the operating loop.

The product responds to two linked problems: residents do not know whom to ask and feel awkward bothering a neighbor; owners worry about damage, loss, and nobody being responsible. The MVP therefore makes custody visible and repeatable: item registration, borrow and return, condition history, and a clear damage rule.

The first pilot is one neighborhood. Numeric success targets are intentionally not set yet. The first signals are whether lenders come back and whether items return on time.

## 2. Problem

Households own drills, ladders, vacuums, and camping items that may be used only a few times a year. Nearby supply exists, but access is socially and operationally unclear. A resident who needs an item may not know whom to ask and may avoid asking because the request feels awkward. The prospective lender faces the opposite risk: damage, loss, and no clear responsible person.

The brainstorm explored four directions: an open marketplace app, a smart locker, a paper board with QR codes and a steward, and rental plus local delivery. The group rejected an open marketplace because it could create too many messages and unclear availability. It rejected a smart locker because it is expensive and a power outage could block access. It recognized that a paper board is cheap but still needs someone to update availability and inspect returns. The chosen direction is a physical cabinet with QR codes and one neighborhood steward; it does not start as an open marketplace.

## 3. Target Users

### 3.1 Primary users

- **Borrower:** a neighborhood resident who needs an occasional household tool and wants a clear way to find, borrow, and return it.
- **Lender:** a neighborhood resident who makes a household tool available and needs custody, condition, and damage handling to be visible enough to lend again.
- **Steward:** the one designated neighborhood role that maintains the cabinet's operating loop, including availability upkeep and returned-item inspection.
- **Building committee:** the decision-making audience for the pilot, responsible for approving the bounded experiment and its operating rules.

### 3.2 Jobs To Be Done

- Functional: when I need a rarely used household tool, I want to discover whether one is available nearby and complete a borrow/return handoff with a known record.
- Functional: when I lend an item, I want its custody, return state, and damage rule to be clear enough that I can decide whether to lend again.
- Social: when I need something, I want to avoid an awkward broadcast request to neighbors.
- Emotional: when I hand over an item, I want confidence that someone is responsible for the next state of it.
- Operational: when I steward the cabinet, I want a small, legible routine that does not depend on a support team.

### 3.3 Non-Users in v1

- Residents outside the first pilot neighborhood.
- A public marketplace of unrelated lenders and borrowers.
- A local-store rental and delivery service.
- A smart-locker operator or power-dependent access system.

## 4. Key User Journeys

The turns do not provide real names. The names below are `[ASSUMPTION: narrative placeholders used to make the journeys testable; they are not customer claims or testimonials]`.

- **UJ-1. Alex finds and borrows an item without an awkward group request.**
  - **Persona + context:** Alex, a resident in the pilot neighborhood, needs an occasional household tool and does not know whom to ask.
  - **Entry state:** Alex is at the physical cabinet and sees the cabinet/item QR code.
  - **Path:** Alex scans the QR code; reviews the item's identity, current availability, and borrow instructions; records the borrow against the item; takes the item; and sees the expected return step.
  - **Climax:** Alex can tell that the item is in Alex's custody and what action closes that custody.
  - **Resolution:** The item is marked borrowed until Alex completes the return flow; the steward can see the same status.
  - **Edge case:** If the item is not available, Alex sees that state rather than sending an unclear message to neighbors.

- **UJ-2. Sam returns an item and records its condition.**
  - **Persona + context:** Sam, a resident borrower, is ready to return a tool to the physical cabinet.
  - **Entry state:** Sam has the borrowed item and its QR code or cabinet location.
  - **Path:** Sam scans the item; opens the return flow; records that the item is being returned; confirms its condition against the prior record; and places it in the cabinet for steward inspection.
  - **Climax:** The return is visible as a new custody event and the condition history is preserved rather than overwritten.
  - **Resolution:** The item is available only according to the return rule and steward inspection state; the steward has an actionable inspection record.
  - **Edge case:** If Sam reports damage, the damage rule routes the item to the appropriate review state instead of silently returning it to availability.

- **UJ-3. Jordan lends again because custody is legible.**
  - **Persona + context:** Jordan, a lender, is deciding whether a household item can be registered in the pilot.
  - **Entry state:** Jordan has the item and can reach the cabinet's registration flow or the steward.
  - **Path:** Jordan registers the item; records its starting condition; reviews the borrow/return expectation and damage rule; places the item in the cabinet; and later reviews its condition history.
  - **Climax:** Jordan can see who or what state currently holds custody and what happens if an item returns damaged.
  - **Resolution:** Jordan either keeps the item in the cabinet for future borrowing or withdraws it through the steward's operating flow.
  - **Edge case:** If Jordan does not accept the damage rule, the item is not treated as an active cabinet item until the disagreement is resolved.

- **UJ-4. Riley stewards the cabinet through a small pilot.**
  - **Persona + context:** Riley, the one neighborhood steward, maintains availability and inspects returned items without a support team.
  - **Entry state:** Riley can access the cabinet and its item records.
  - **Path:** Riley checks items marked returned; inspects the physical item; updates availability and condition; flags damage or loss; and communicates the rule-based next state to the relevant parties.
  - **Climax:** The physical cabinet and its records agree about whether an item is available, borrowed, under inspection, damaged, or lost.
  - **Resolution:** Riley leaves a clear next action and the pilot has a traceable custody history.

## 5. Glossary

- **Cabinet** — the shared physical storage location for registered household tools in the pilot neighborhood.
- **Cabinet item** — a household tool registered for possible borrowing through the Cabinet.
- **Borrower** — the resident currently responsible for a borrowed Cabinet item.
- **Lender** — the resident who contributes or owns a Cabinet item.
- **Steward** — the one neighborhood role responsible for operating the Cabinet loop and inspecting returns.
- **Custody event** — a time-ordered record of an item's registration, borrow, return, inspection, damage, loss, or withdrawal state.
- **Condition history** — the append-only record of a Cabinet item's observed state across custody events.
- **Damage rule** — the pilot rule that defines how a reported damaged item is reviewed and what responsibility or next action follows. Exact terms remain an open question.
- **Pilot neighborhood** — the single neighborhood in the first test; it is not a citywide network.
- **QR code** — the scannable identifier attached to a Cabinet or Cabinet item that opens its current record or instructions.

## 6. Solution Thesis

If a neighborhood moves lending from an ad hoc social request into a shared physical Cabinet with QR-linked records, one Steward, and a visible Damage rule, then residents can access rarely used tools with less social friction and lenders can judge custody more clearly. The thesis is about trust made operational: a physical place, a named role, and a history of states.

The solution is deliberately bounded. It preserves the physical object and the human steward instead of assuming that an open marketplace, a smart locker, or local-store delivery is necessary for the first pilot. `[ASSUMPTION: a QR-linked record may use a lightweight web flow or another scan destination; the technical transport is not decided by the turns]`

## 7. Operating Model and Roles

### 7.1 Operating rules

1. Only a registered Cabinet item can be borrowed through the pilot.
2. Every borrow creates a custody event with a responsible Borrower and an expected return state.
3. Every return creates a custody event; the item is not silently assumed to be available before the Steward's inspection step defined by the pilot.
4. Condition history is preserved across events; a new observation does not erase an earlier one.
5. A reported damaged or lost item is routed through the Damage rule and is not treated as an ordinary successful return.
6. Availability shown at the Cabinet and in the QR-linked record must be updated when the Steward learns they disagree.
7. The pilot serves one Pilot neighborhood only. It does not promise a citywide network.

### 7.2 Roles and responsibilities

- **Borrower:** reviews the borrow expectation, takes custody, returns the Cabinet item, and reports the observed condition.
- **Lender:** supplies a Cabinet item, confirms its starting condition, and accepts or declines the pilot's Damage rule before the item becomes active.
- **Steward:** maintains the Cabinet routine, updates availability, inspects returned items, records condition, and routes damage or loss according to the rule.
- **Building committee:** approves the pilot boundary, Steward role, Cabinet location, and Damage rule before launch. `[ASSUMPTION: committee approval and a single physical location are governance prerequisites implied by the building-committee handoff]`

## 8. Features and Functional Requirements

### 8.1 Cabinet discovery and QR access

**Description:** The physical Cabinet and each Cabinet item provide a QR-linked entry point to the current record or instructions. The experience must make the physical and digital states legible without turning the MVP into an open marketplace. Realizes UJ-1 and UJ-4.

**Functional Requirements:**

#### FR-1: Identify a Cabinet item

The system must let a person identify a Cabinet item from its QR code or a clearly labeled Cabinet record.

**Consequences (testable):**

- Scanning an active QR code resolves to exactly one Cabinet item record or a clear unavailable/error state.
- The record shows the item name or label, current availability state, and next permitted action.
- The flow does not require a public neighbor-to-neighbor message thread to discover the current state.

#### FR-2: Show physical-to-record instructions

The system must connect the QR-linked record to the physical Cabinet action needed next.

**Consequences (testable):**

- A borrower can see how to proceed from the record to borrow, return, or ask the Steward for help.
- The Cabinet label and the QR-linked record use the same Cabinet item identifier.
- A failed or unavailable scan gives a recovery instruction rather than a blank state.

### 8.2 Item registration and availability

**Description:** Lenders and the Steward can register Cabinet items and make their initial condition and availability explicit. Registration is the boundary between a household tool and a Cabinet item. Realizes UJ-3 and UJ-4.

**Functional Requirements:**

#### FR-3: Register a Cabinet item

The Lender or Steward must be able to register a Cabinet item with an identifier, item description, starting condition, and responsible Lender.

**Consequences (testable):**

- A new record cannot become active without an identifier, description, starting condition, and responsible Lender.
- The record can be linked to a QR code that identifies only that Cabinet item.
- The registration date and actor are retained as part of the item record.

#### FR-4: Set and update availability

The Steward must be able to set a Cabinet item's availability state and correct a mismatch between the physical Cabinet and the record.

**Consequences (testable):**

- The record supports at least available, borrowed, returned/under inspection, damaged, lost, and withdrawn states. `[ASSUMPTION: these state labels are the minimum vocabulary needed to express the confirmed custody and condition requirements]`
- Every state change retains the prior state and actor in the Custody event history.
- A withdrawn Cabinet item no longer appears as available for new borrowing.

#### FR-5: Withdraw an item

The Lender or Steward must be able to mark a Cabinet item withdrawn without deleting its Custody events or Condition history.

**Consequences (testable):**

- A withdrawn item cannot be newly borrowed.
- Its prior history remains retrievable by the Steward.
- The record distinguishes withdrawn from lost or damaged.

### 8.3 Borrow and return

**Description:** Borrow and return are explicit custody transitions anchored to the physical Cabinet. The MVP must make responsibility and next action visible without requiring an open marketplace. Realizes UJ-1 and UJ-2.

**Functional Requirements:**

#### FR-6: Start a borrow

The system must let a Borrower start a borrow for an available Cabinet item and associate the item with that Borrower.

**Consequences (testable):**

- A borrow cannot start for an item whose current state is not available.
- The borrow creates a Custody event with item, Borrower, start time, and expected return information.
- The record immediately changes to borrowed for subsequent viewers.

#### FR-7: Show custody responsibility

The system must show the active Borrower responsibility and expected return action to the Borrower and Steward.

**Consequences (testable):**

- The active borrow record has one current Borrower or an explicit unresolved state.
- The Borrower can reach the return action from the active borrow record.
- The Steward can identify which item is currently borrowed and what next action is expected.

#### FR-8: Complete a return

The Borrower or Steward must be able to record a Cabinet item return and create a new Custody event.

**Consequences (testable):**

- A return cannot silently erase the active borrow event.
- The return records the actor, time, and observed condition.
- The item moves to the pilot's defined returned/inspection state before it is shown as available.

### 8.4 Condition history and damage rule

**Description:** Condition and damage are treated as part of custody, not as an afterthought. The MVP includes a Condition history and a clear Damage rule; the exact responsibility and remedy terms must be decided before pilot launch. Realizes UJ-2, UJ-3, and UJ-4.

**Functional Requirements:**

#### FR-9: Append condition observations

The Borrower or Steward must be able to append a condition observation to a Cabinet item's Condition history at registration, return, inspection, or damage report.

**Consequences (testable):**

- An observation includes item, actor, time, and condition state or note.
- Earlier observations remain readable after a later observation is added.
- A return observation can be compared with the previous recorded observation.

#### FR-10: Apply the Damage rule

The Steward must be able to route a reported damaged item through the approved Damage rule.

**Consequences (testable):**

- A damage report creates a Custody event and does not mark the item as ordinarily available.
- The record exposes the next responsibility or decision state defined by the approved rule.
- The rule is visible to Lenders and Borrowers before they accept a borrow or registration.

#### FR-11: Handle loss distinctly

The Steward must be able to record a lost item as distinct from a damaged or available item.

**Consequences (testable):**

- A lost item cannot be borrowed.
- The loss remains in the item's history and can be reviewed by the Lender and Steward according to the pilot's privacy decision.
- The record exposes an open next action rather than implying that the item returned.

### 8.5 Steward operations

**Description:** One neighborhood Steward keeps the physical Cabinet and records aligned. This group handles the manual inspection and reconciliation that the paper-board alternative made visible. Realizes UJ-4.

**Functional Requirements:**

#### FR-12: Review returned items

The Steward must be able to view Cabinet items awaiting inspection and record an inspection outcome.

**Consequences (testable):**

- Returned/under-inspection items are distinguishable from available items.
- An inspection records actor, time, observed condition, and next state.
- The item cannot be treated as inspected without an outcome.

#### FR-13: Reconcile cabinet state

The Steward must be able to flag and resolve a mismatch between a physical Cabinet item and its recorded state.

**Consequences (testable):**

- A mismatch can be recorded without overwriting the prior state history.
- The Steward can leave the item unavailable while the mismatch is unresolved.
- The record identifies the next Steward action.

#### FR-14: Maintain one-steward operating view

The system must provide the Steward with a view of active borrows, items awaiting inspection, and damage/loss states for the Pilot neighborhood.

**Consequences (testable):**

- The view contains each item at most once per current state.
- The Steward can reach the underlying Custody event and Condition history from each item.
- The view makes unresolved actions distinguishable from informational history.

### 8.6 Pilot governance and feedback

**Description:** The first Pilot neighborhood needs a bounded launch record, operating rule visibility, and a way to review whether the model is earning repeat lending and on-time returns. No numeric targets are claimed in this PRD. Realizes UJ-3 and UJ-4.

**Functional Requirements:**

#### FR-15: Publish pilot rules and boundary

The Steward or Building committee must be able to publish the Pilot neighborhood boundary, roles, borrow/return expectations, and approved Damage rule.

**Consequences (testable):**

- A resident can find the current operating rules from the Cabinet entry point.
- The published boundary states that the first pilot is one neighborhood and is not a citywide network.
- A rule change retains its effective date and approving role.

#### FR-16: Record pilot signals

The Steward or Building committee must be able to review whether Lenders come back and whether items return on time, without treating an unchosen numeric target as an existing result.

**Consequences (testable):**

- The pilot review can count or list repeat Lender participation using recorded events once a measurement definition is approved.
- The pilot review can identify returns relative to their recorded expected return information once that definition is approved.
- The interface labels missing targets or definitions as open decisions rather than reporting fabricated performance.

## 9. Non-Functional Requirements

### 9.1 Accessibility and clarity

- The QR-linked flow must be keyboard operable, use visible focus, expose labels and errors to assistive technology, and maintain readable contrast. `[ASSUMPTION: a web-accessible flow is the most likely scan destination, but the accessibility obligation applies to whichever interface is selected]`
- The physical QR label must have a readable item identifier and a non-scan fallback instruction for a resident who cannot scan.
- Borrowed, returned/under inspection, damaged, lost, withdrawn, and available states must not be communicated by color alone.

### 9.2 Reliability and recovery

- A temporary scan or record failure must not create a false borrow or false return.
- A Steward must be able to reconcile a physical/record mismatch without deleting history.
- The operating procedure must define what to do during a power or connectivity outage before the pilot begins. `[ASSUMPTION: outage procedure is required because the smart-locker critique identifies power outage as a relevant failure mode, even though the chosen Cabinet is not a smart locker]`

### 9.3 Privacy and data minimization

- The pilot must collect only the information needed to identify the Cabinet item, responsible role, custody event, condition, and approved operating action. `[ASSUMPTION: exact identity fields and retention period require committee approval]`
- The system must not expose a public directory of household tools, owners, or borrowers beyond what the approved operating rule requires.
- Access to Steward-only inspection and damage details must be distinct from resident-facing status where the approved privacy rule requires it. `[ASSUMPTION: the committee will decide the minimum visibility boundary before launch]`

### 9.4 Auditability

- Custody events and Condition history must be append-oriented: corrections add a new event or correction record rather than silently changing the past.
- Each operational change must retain actor and time sufficient for the Steward to explain the current state.

## 10. Information Architecture and Surface Boundaries

- **Cabinet entry:** physical Cabinet label, QR code, item identifier, and fallback instruction.
- **Item record:** item identity, current state, current next action, and condition history visibility appropriate to the role.
- **Borrow flow:** borrow confirmation, active custody, and expected return information.
- **Return flow:** return confirmation, condition observation, and inspection state.
- **Steward view:** active borrows, returned/under inspection items, damage/loss states, and reconciliation actions.
- **Pilot rules:** roles, Cabinet boundary, borrow/return expectations, Damage rule, and pilot review signals.

## 11. MVP Scope and Sequencing

### 11.1 In scope for MVP

- One physical Cabinet in one Pilot neighborhood.
- QR codes that identify the Cabinet or Cabinet item and connect to the current record or instructions.
- One neighborhood Steward role.
- Item registration with starting condition and responsible Lender.
- Borrow and return flows anchored to explicit Custody events.
- Condition history.
- A clear Damage rule, published before pilot launch, with exact terms still to be decided.
- Availability upkeep, returned-item inspection, and physical/record reconciliation.
- Pilot review of repeat Lender participation and on-time returns once numeric definitions are chosen.

### 11.2 Explicitly out of scope for MVP

- `[NON-GOAL for MVP]` An open marketplace with public listings and neighbor-to-neighbor messaging; the group explicitly chose not to start there.
- `[NON-GOAL for MVP]` A smart locker or power-dependent automated access; the group identified cost and outage risk.
- `[NON-GOAL for MVP]` Local-store tool rental and delivery.
- `[NON-GOAL for MVP]` A citywide or multi-neighborhood network.
- `[NON-GOAL for MVP]` Numeric success targets; they remain open until the committee defines the measurement window and baseline.
- `[NON-GOAL for MVP]` Unbounded support coverage or a support team; the operating model is one Steward for the first pilot.

### 11.3 Sequencing

1. **Rule and site readiness:** approve the one-neighborhood boundary, Cabinet location, Steward role, item eligibility, custody vocabulary, and Damage rule.
2. **Physical record loop:** label the Cabinet and Cabinet items with QR codes; register initial items and starting conditions.
3. **Borrow/return loop:** test borrow, return, condition history, inspection, and reconciliation with the Steward.
4. **Pilot review:** observe repeat Lender participation and on-time returns; decide numeric targets and any next-scope change from evidence.

## 12. Success Signals and Counter-Metrics

The turns provide directional success signals but no numeric targets. These are signals to measure, not claimed outcomes.

### Primary success signals

- **SM-1:** Lenders come back to lend again during the Pilot neighborhood review period. Definition and numeric target are open. Validates FR-3, FR-9, FR-15, and FR-16.
- **SM-2:** Cabinet items return on time relative to the approved expected-return definition. Numeric target is open. Validates FR-6, FR-7, FR-8, and FR-16.

### Secondary success signals

- **SM-3:** Steward can keep the physical Cabinet state and recorded state aligned through inspection and reconciliation. Measurement definition is open. Validates FR-4, FR-12, FR-13, and FR-14.
- **SM-4:** Residents can find an available item without relying on an open marketplace message thread. Measurement method is open. Validates FR-1, FR-2, and FR-6.

### Counter-metrics

- **SM-C1:** Number of registered items must not be optimized at the expense of return timeliness or repeat Lender participation; validates the MVP boundary around trust and custody.
- **SM-C2:** Borrow volume must not be optimized by weakening the Damage rule, inspection, or condition history; validates FR-9, FR-10, and FR-12.
- **SM-C3:** Automation level must not be optimized by removing the named Steward before the pilot demonstrates a safe operating loop; validates FR-12 through FR-15.

## 13. Risks and Mitigations

| Risk | Why it matters | MVP mitigation | Remaining decision |
|---|---|---|---|
| Damage or loss | Owners may stop lending if nobody is responsible. | Publish a Damage rule, record custody, preserve Condition history, and route exceptions to the Steward. | Exact responsibility, remedy, and dispute path. |
| Availability drift | A paper-style record can say available when the physical item is gone. | QR-linked state, one Steward, inspection, and reconciliation view. | Inspection cadence and escalation. |
| Steward overload | One role may become a hidden support team. | Keep one Pilot neighborhood and expose only the core operating queue. | Maximum operating load and backup coverage. |
| Social friction | Residents may still avoid asking or may not understand the flow. | Use a physical Cabinet, clear labels, QR entry, and a defined next action. | Non-scan fallback and resident-facing language. |
| Access interruption | Power or connectivity problems could block a digital record. | Do not use a smart locker; define a manual outage procedure before launch. | Offline record and reconciliation procedure. |
| Scope expansion | A successful pilot may tempt a citywide network before custody works. | State one-neighborhood boundary in rules and artifacts. | Evidence threshold for any expansion. |

## 14. Assumptions Index

- **A-1:** Journey names are narrative placeholders, not real customers, testimonials, or evidence.
- **A-2:** A QR-linked record may use a lightweight web flow or another scan destination; the turns do not select a transport.
- **A-3:** Available, borrowed, returned/under inspection, damaged, lost, and withdrawn are the minimum state vocabulary needed to represent the confirmed MVP; the committee may refine labels.
- **A-4:** Building-committee approval and a single physical location are governance prerequisites implied by the handoff audience.
- **A-5:** Accessibility applies to the selected scan destination; the selected technical surface is not confirmed.
- **A-6:** An outage procedure is required because the smart-locker critique identified power outage as a relevant failure mode.
- **A-7:** Exact identity fields, retention, privacy visibility, inspection cadence, and backup coverage require committee decisions.

## 15. Open Questions

1. What exact Damage rule makes a Lender willing to lend again, and who approves a disputed outcome?
2. What counts as “on time,” including whether an expected return time is required for every borrow?
3. What numeric targets and measurement window should define “Lenders come back” and “items return on time”?
4. What item categories and physical storage constraints are eligible for the first Cabinet?
5. Where is the Cabinet located, and what physical access hours apply?
6. What is the non-scan fallback for residents who cannot use a QR code?
7. What identity and contact data are needed for custody, and how long are they retained?
8. Which condition vocabulary is sufficient for the pilot, and can residents attach a photo or only a note? `[NOTE FOR PM: do not add media until the operating need is confirmed]`
9. What is the Steward's inspection cadence and backup plan when the Steward is unavailable?
10. What happens during a power or connectivity outage, and how is the manual record reconciled later?
11. What evidence would justify expansion beyond one neighborhood?

## 16. Acceptance Criteria

- **AC-1:** A building committee reader can identify the problem, target roles, chosen solution, MVP boundary, and pilot neighborhood without reading the transcript.
- **AC-2:** A registered Cabinet item has an identifier, starting condition, responsible Lender, QR-linked record, and visible current state.
- **AC-3:** A Borrower can start a borrow only when the item is available, and the borrow creates a traceable Custody event.
- **AC-4:** A Borrower can record a return and condition observation without erasing the borrow or prior Condition history.
- **AC-5:** A returned item is distinct from an available item until the defined inspection step resolves it.
- **AC-6:** A Steward can inspect, reconcile, and route damaged or lost items without deleting history.
- **AC-7:** The Damage rule is visible before registration or borrowing, with unresolved terms listed as open questions rather than invented policy.
- **AC-8:** The pilot rules explicitly state one neighborhood, one Steward role, and no citywide-network promise.
- **AC-9:** The PRD does not claim numeric traction, customers, testimonials, or success results; it records only directional signals and open targets.
- **AC-10:** The landing page and deck can be traced back to this PRD's physical Cabinet, QR, Steward, custody/damage rule, one-neighborhood pilot, and explicit MVP boundary.

## 17. Traceability Notes

The transcript is the provenance source for this PRD at `transcript.md`; `.memlog.md` is the append-only replay audit trail. User-confirmed decisions are the physical Cabinet with QR codes, one neighborhood Steward, item registration, borrow and return, Condition history, a clear Damage rule, a one-neighborhood pilot, and directional success signals without numeric targets. Alternatives remain documented as rejected or out of scope, not as shipped capabilities.
