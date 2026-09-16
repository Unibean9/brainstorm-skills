---
title: Tablemate
status: final
created: 2026-09-16
updated: 2026-09-16
source: evals/golden-data.yaml, case 02-tablemate, turns 1-19
stance: creative_partner
branch: frontend-design: pitch-deck
---

# PRD: Tablemate

## 0. Document Purpose

This final PRD records the direction explicitly chosen in the 19-turn Tablemate replay. It is for product, learning-experience, privacy, engineering, and downstream frontend work, including the requested pitch deck for teachers and school decision-makers. Directly stated problems, ideas, constraints, critiques, decisions, and confirmations are preserved as source material. Any implementation detail, policy, metric, or outcome not stated by the user is marked `[ASSUMPTION]` and/or kept in Open Questions.

## 1. Executive Summary

Student groups can be pulled toward one fast, confident student’s idea while quieter students struggle to enter the conversation. A teacher cannot stand inside every group and manually manage every speaking turn. The desired outcome is more balanced participation, but no numeric metric has been confirmed.

Tablemate is a proposed voice facilitator for one classroom group. In v1 it asks one short question at a time, keeps an idea trace of contributions, can bring back an idea that was mentioned once and forgotten, and supports English and Vietnamese. The default mode only asks questions. A bounded mode in which AI contributes one suggestion must be explicitly enabled by the teacher. Any AI suggestion retains its AI provenance even if the group develops it further.

The product thesis is that short, question-led facilitation plus a transparent idea trace can create more room for participation while keeping authority with the group and teacher. This thesis is not a measured result. The PRD does not promise improved participation, accurate transcription, student safety, adoption, or learning outcomes.

## 2. Problem

### 2.1 Problem statement

In a classroom group brainstorm, one fast, confident student may pull everyone toward their own idea. Quieter students may have good ideas but cannot enter the conversation. The teacher cannot stand in the middle of every group and manage every speaking turn. A voice facilitator may also introduce new risks: AI praise could make one idea seem correct, speaker attribution could make students afraid of being judged, saved transcripts could be used for grading without agreement, and transcription errors could create a false trace.

### 2.2 Evidence and provenance

- The desired outcome and participation problem come from user turns 1–4.
- Speaking tokens, write-before-talk, bot reminders, voice facilitation, contribution recording, and idea recall come from user turns 5–7.
- Safety, teacher visibility, and fifteen-minute brevity constraints come from user turns 8–10.
- AI praise, attribution anxiety, grading misuse, and false transcription traces come from user turns 11–14.
- Question-only default, teacher-enabled bounded suggestions, v1 scope, no grading, and provenance persistence come from user turns 15–17.
- The missing numeric metric and requested audience come from user turns 18–19.

## 3. Target Users

### 3.1 Primary users

- **Student group:** Students brainstorming together in one classroom group. The replay specifically distinguishes a fast, confident student and quieter students; it does not provide ages, class level, subject, group size, accessibility needs, or evidence from real groups.
- **Teacher:** A teacher overseeing classroom groups who cannot manage every speaking turn directly and needs visibility into whether AI is steering the answer.

### 3.2 Decision audience

Teachers and school decision-makers are the audience for the requested pitch deck. `[ASSUMPTION: school decision-makers may require deployment, safeguarding, procurement, or data-governance information beyond this replay; those needs are open rather than treated as confirmed requirements.]`

### 3.3 Non-users and boundaries

- Tablemate v1 is not a grading system.
- It is not a teacher replacement or an autonomous answer generator.
- It is not a claim of accurate voice transcription.
- `[ASSUMPTION: parents, administrators, and school IT staff are stakeholders rather than direct v1 users unless confirmed.]`

## 4. Jobs To Be Done

- **Student, functional:** When brainstorming with a group, get a short prompt that creates room to contribute without the facilitator turning into a lecture.
- **Student, social:** When I have an idea but cannot enter a fast conversation, have a participation experience that feels safe enough to contribute. The replay does not define what “safe” means operationally.
- **Group, continuity:** When an idea is mentioned once and forgotten, bring it back into the group’s working conversation.
- **Teacher, oversight:** When groups use AI to brainstorm, see enough of the facilitation and provenance to judge whether AI is steering the answer.
- **Teacher, control:** When AI contribution is allowed, explicitly enable the bounded suggestion mode; otherwise keep the facilitator question-only.
- **Downstream artifact:** When the brainstorm is complete, export a PRD from the idea trace. `[ASSUMPTION: export format, schema, and destination were not discussed.]`

## 5. Glossary

- **Tablemate** — The proposed classroom voice facilitator described in this PRD.
- **Student Group** — One classroom group using Tablemate together; v1 supports one group at a time.
- **Teacher** — The classroom adult who can oversee the Student Group and explicitly enable the Bounded Suggestion Mode.
- **Facilitation Mode** — The active behavior of Tablemate: Question-Only Mode or Bounded Suggestion Mode.
- **Question-Only Mode** — The default Facilitation Mode in which Tablemate only asks short questions and does not contribute an AI suggestion.
- **Bounded Suggestion Mode** — The Facilitation Mode in which Tablemate may contribute one bounded suggestion after explicit Teacher enablement.
- **Idea Trace** — The record of ideas and contributions produced during a Student Group session, including origin and any known uncertainty. `[ASSUMPTION: the replay does not specify its exact data fields.]`
- **Contribution** — An idea or spoken input attributable to a Student Group participant or to Tablemate as AI-originated.
- **AI Provenance** — The persistent label that identifies an AI-originated suggestion even after the Student Group develops it.
- **Short Question** — One prompt asked at a time and kept brief enough for a group with fifteen minutes; exact length is open.
- **PRD Export** — The v1 output requested by the user; exact format and content mapping are open.
- **Transcript** — A saved or in-session representation of voice input. Its retention, access, correction, and grading-use policy are not confirmed.
- **False Trace** — A Contribution record that does not accurately represent what a student said, including one caused by voice transcription error.
- **v1** — The first version supporting one Student Group, English and Vietnamese, an Idea Trace, and PRD Export, with grading out of scope.

## 6. Key User Journeys

### UJ-1. Mina enters a fast group conversation safely

- **Persona + context:** Mina is an illustrative quieter Student Group member who may have a good idea but struggles to enter a fast conversation. `[ASSUMPTION: “Mina” is an illustrative name, not a real student or testimonial.]`
- **Entry state:** Mina is in a classroom Student Group brainstorm with Tablemate active. The replay does not specify authentication, device, room setup, or consent flow.
- **Path:** Tablemate asks one Short Question; Mina gets a chance to contribute; the Contribution is represented in the Idea Trace; the group continues without Tablemate praising one idea as correct.
- **Climax:** Mina’s idea has a visible place in the group’s working trace. `[ASSUMPTION: “visible” may mean visible to the group; the replay does not decide speaker-display behavior.]`
- **Resolution:** The group proceeds to its next Short Question. Whether Mina’s name is shown, hidden, or chosen by the student is an open privacy decision.
- **Edge case:** If the trace misrepresents Mina’s words, the system must not present the False Trace as certain. Correction behavior is open.

### UJ-2. Mr. Alvarez oversees AI control without standing in the group

- **Persona + context:** Mr. Alvarez is an illustrative Teacher overseeing a classroom Student Group while unable to manage every speaking turn directly. `[ASSUMPTION: “Mr. Alvarez” is an illustrative name, not a real teacher or testimonial.]`
- **Entry state:** A Student Group is ready to use Tablemate; the Teacher can select or review a Facilitation Mode. The replay does not specify the Teacher surface.
- **Path:** The Teacher sees that Question-Only Mode is the default; the Teacher reviews whether AI is steering the answer; only if desired, the Teacher explicitly enables Bounded Suggestion Mode; any AI suggestion remains labeled as AI-originated.
- **Climax:** The Teacher can distinguish question-led facilitation from an AI contribution and retains the enablement decision.
- **Resolution:** The Student Group continues within the selected mode. The product does not turn the trace into a grading record.
- **Edge case:** If the Teacher has not explicitly enabled Bounded Suggestion Mode, Tablemate must not produce a bounded AI suggestion.

### UJ-3. Linh revisits a forgotten idea

- **Persona + context:** Linh is an illustrative Student Group member whose idea was mentioned once and then forgotten. `[ASSUMPTION: “Linh” is an illustrative name, not a real student or testimonial.]`
- **Entry state:** The Student Group has a growing Idea Trace during a short session.
- **Path:** Tablemate identifies an earlier Contribution; it brings the idea back with its existing provenance; the group discusses or develops it; if the source is AI, AI Provenance remains attached.
- **Climax:** The forgotten idea re-enters the group’s working conversation without being silently rewritten as a new or human-originated idea.
- **Resolution:** The Idea Trace retains the relationship between the earlier Contribution and its later development. Exact versioning is open.

### UJ-4. A Student Group reviews a false trace

- **Persona + context:** An illustrative Student Group notices that voice transcription may have misunderstood a student.
- **Entry state:** A Transcript or Idea Trace contains a possible False Trace.
- **Path:** The group or Teacher notices uncertainty; the product marks or exposes the possible error; the group decides how to correct, annotate, or exclude it. `[ASSUMPTION: a correction path is proposed because the user identified false traces as a risk; the exact actor and controls are open.]`
- **Climax:** The false transcription is not treated as unquestionable evidence of what a student said.
- **Resolution:** The corrected or disputed state remains distinct from the original machine transcription. `[ASSUMPTION: preserving both states is proposed for provenance and auditability.]`

## 7. Solution Thesis

Tablemate bets on a narrow role for AI: ask one Short Question at a time, keep an Idea Trace, and bring back ideas that the group might otherwise forget. The default keeps AI in a question-only role so the tool does not quietly become the source of the answer. If a Teacher wants AI to contribute one bounded suggestion, that mode must be explicitly enabled.

The product’s trust model has three visible boundaries: the Teacher controls whether AI may suggest; AI-originated suggestions keep AI Provenance through later group development; and v1 does not grade students. The Idea Trace is useful only if the product also treats privacy and accuracy as first-class constraints: attribution can make students afraid of judgment, a saved Transcript may be misused for grading, and voice transcription may create a False Trace. Exact consent, retention, correction, and access policies are not confirmed and remain open.

## 8. Feature Groups and Functional Requirements

### 8.1 Question-led facilitation

**Description:** Tablemate keeps the core interaction short and sequential for a Student Group with only fifteen minutes. It asks one Short Question at a time. The default is Question-Only Mode. Realizes UJ-1, UJ-2, and UJ-3.

**Functional Requirements:**

#### FR-1: Ask one question at a time

Tablemate must present one Short Question at a time during a Student Group session.

**Consequences (testable):**

- A session view never presents a batch of simultaneous facilitator questions as the active prompt.
- A review can identify the current question and the group’s next response opportunity.
- The exact question length and pacing threshold remain open.

#### FR-2: Keep prompts short

Tablemate must keep facilitation concise enough that the experience does not become a lecture during a fifteen-minute group session.

**Consequences (testable):**

- Content review rejects facilitator copy that behaves as a lecture or long explanation.
- A timing/content review defines the acceptable prompt length before release. `[ASSUMPTION: a review gate is inferred from the confirmed constraint.]`

#### FR-3: Question-only default

Tablemate must start Student Group sessions in Question-Only Mode unless the Teacher has explicitly enabled Bounded Suggestion Mode.

**Consequences (testable):**

- A new session produces questions but no AI suggestion when no Teacher enablement exists.
- The active Facilitation Mode is identifiable to the Teacher. `[ASSUMPTION: a visible mode label is inferred from the Teacher-control requirement.]`

### 8.2 Contribution capture and Idea Trace

**Description:** Tablemate records what each person contributed as an Idea Trace, while acknowledging that attribution can create fear of judgment and transcription can be wrong. Realizes UJ-1, UJ-3, and UJ-4.

#### FR-4: Capture Contributions

Tablemate must represent Student Group Contributions in an Idea Trace during the session.

**Consequences (testable):**

- A completed session contains a retrievable Idea Trace for the Contributions that were captured.
- The trace distinguishes a captured Contribution from an unrecorded or unavailable input. `[ASSUMPTION: this distinction is inferred because transcription may fail.]`

#### FR-5: Preserve contribution origin

Each Idea Trace entry must retain whether the Contribution originated from a Student Group participant or from Tablemate as AI.

**Consequences (testable):**

- A reviewer can inspect an entry’s origin without relying on memory of the live session.
- Origin is not silently changed when a later participant develops the idea.

#### FR-6: Surface trace uncertainty

Tablemate must not present a voice-transcribed Contribution as certain when it may be a False Trace.

**Consequences (testable):**

- The product has a defined uncertain, disputed, or correction state before release. `[ASSUMPTION: a state is inferred from the false-trace risk; the label is open.]`
- A false transcription is not silently converted into a definitive student statement.

### 8.3 Idea recall and development

**Description:** Tablemate can bring back an idea mentioned once and then forgotten. Later development must retain the original provenance. Realizes UJ-3.

#### FR-7: Bring back forgotten ideas

Tablemate must provide a way for a previously mentioned idea to return to the Student Group’s working conversation.

**Consequences (testable):**

- A test session can mention an idea, move on, and later retrieve that same idea as a prior Contribution.
- The recalled entry is distinguishable from a newly generated suggestion.

#### FR-8: Preserve development history

When a Student Group develops a recalled idea, Tablemate must retain the relationship between the earlier Contribution and the later development. `[ASSUMPTION: relationship preservation is inferred; the exact history UI is open.]`

**Consequences (testable):**

- Reviewers can determine which earlier entry the later development extends.
- The later development does not erase the earlier origin or AI Provenance.

### 8.4 Teacher control and AI boundaries

**Description:** Teacher control is explicit and narrow. Question-Only Mode is default; Bounded Suggestion Mode requires explicit Teacher enablement and allows one bounded suggestion. Realizes UJ-2.

#### FR-9: Explicitly enable Bounded Suggestion Mode

The Teacher must be able to explicitly enable Bounded Suggestion Mode for a Student Group session.

**Consequences (testable):**

- Bounded Suggestion Mode is not active merely because a session exists.
- A test without explicit Teacher enablement produces no bounded AI suggestion.

#### FR-10: Bound AI contribution

When Bounded Suggestion Mode is enabled, Tablemate may contribute one bounded suggestion and must not behave as an unrestricted answer generator.

**Consequences (testable):**

- The mode’s output is limited to the defined one-suggestion boundary before release. `[ASSUMPTION: a boundary definition is required; the replay does not specify wording or count semantics.]`
- The product review can distinguish a Short Question from the bounded suggestion.

#### FR-11: Show active mode and control state

Tablemate must make the active Facilitation Mode and the fact of Teacher enablement reviewable. `[ASSUMPTION: “make visible” is inferred from the Teacher’s stated trust need.]`

**Consequences (testable):**

- A Teacher can determine whether the Student Group is in Question-Only Mode or Bounded Suggestion Mode.
- A Teacher can determine whether the bounded mode was explicitly enabled before an AI suggestion appears.

### 8.5 AI Provenance and non-authority

**Description:** AI must not acquire authority through praise or through later group editing. The Idea Trace carries AI Provenance through development. Realizes UJ-2 and UJ-3.

#### FR-12: Retain AI Provenance

Any AI suggestion must retain its AI Provenance even if the Student Group likes it and develops it further.

**Consequences (testable):**

- A developed idea can be traced back to its AI-originated suggestion.
- Export does not remove or rewrite AI Provenance. `[ASSUMPTION: PRD Export must carry provenance because the user called provenance an invariant; exact export fields remain open.]`

#### FR-13: Avoid correctness praise

Tablemate must not praise one idea in a way that makes the group think it is the correct answer.

**Consequences (testable):**

- Content review rejects approval language that positions one Contribution as the correct answer without group reasoning.
- The product does not use praise as an unconfirmed proxy for quality or correctness.

### 8.6 Language and v1 session scope

**Description:** V1 deliberately supports one Student Group and English and Vietnamese. It does not claim broader class, language, or deployment coverage. Realizes UJ-1 through UJ-4.

#### FR-14: Support one Student Group

V1 must scope a session to one Student Group rather than promise multi-group orchestration.

**Consequences (testable):**

- A v1 session has one identifiable Student Group boundary.
- Cross-group comparisons and coordination are not required for v1.

#### FR-15: Support English and Vietnamese

V1 must provide the intended facilitation and Idea Trace experience in English and Vietnamese.

**Consequences (testable):**

- A content review can exercise core Question-Only Mode and trace labels in both languages.
- The exact translation quality bar and localized terminology are open.

### 8.7 PRD export and grading boundary

**Description:** V1 includes PRD Export and explicitly does not grade students. Export is a downstream artifact, not a grading workflow. Realizes UJ-2 and the v1 handoff.

#### FR-16: Export a PRD

Tablemate must provide the v1 PRD Export requested by the user from the Idea Trace.

**Consequences (testable):**

- A completed session can produce a PRD Export artifact.
- The export preserves AI Provenance and any trace uncertainty that the source trace exposes. `[ASSUMPTION: preserving uncertainty in export is inferred from the False Trace risk.]`
- Export format, field mapping, and editability remain open.

#### FR-17: Do not grade students

Tablemate must not produce grades, scores, or grading judgments about Student Group members in v1.

**Consequences (testable):**

- A v1 review finds no grading output in the session, Idea Trace, or PRD Export.
- A saved Transcript is not treated as a grading record by the product. `[ASSUMPTION: product behavior is distinguished from school policy; policy confirmation remains open.]`

## 9. Non-Functional Requirements

### 9.1 Privacy and data governance

- The product must not assume that recording who said what is harmless; the privacy trade-off must be visible in design review.
- A saved Transcript must not silently become a grading record. Exact retention, access, deletion, consent, and permitted-use policy are open questions.
- The product must not expose a student’s identity or Contribution beyond the audience and controls approved for v1. `[ASSUMPTION: audience minimization is inferred from the judgment concern; exact visibility is open.]`
- Any export must preserve the privacy boundary and not create a new grading surface. `[ASSUMPTION: export governance is inferred from the saved-transcript risk.]`

### 9.2 Accuracy and provenance

- Voice transcription must expose the possibility of a False Trace rather than presenting uncertain words as unquestioned fact.
- AI Provenance must persist through Idea Trace recall, later development, and PRD Export.
- The product must not claim transcription accuracy, balanced participation, learning impact, or school adoption without evidence.

### 9.3 Usability and time

- The core interaction must remain short enough for the stated fifteen-minute group constraint.
- Question-Only Mode, Bounded Suggestion Mode, and Teacher enablement must be distinguishable. `[ASSUMPTION: distinguishability is a product requirement inferred from the trust need.]`
- English and Vietnamese core flows must be reviewable before v1 release.

### 9.4 Accessibility and reliability

- `[ASSUMPTION: the final product needs an accessibility review for voice, text, and classroom use; the replay provides no standard, device, or threshold.]`
- `[ASSUMPTION: the final product needs a defined behavior for missing audio, unavailable transcription, and interrupted sessions; no reliability target was confirmed.]`

## 10. Constraints and Guardrails

- **Participation:** The goal is more balanced participation; no numeric target is confirmed.
- **Teacher control:** Question-Only Mode is default; Bounded Suggestion Mode requires explicit Teacher enablement.
- **Non-authority:** AI must not praise one idea into appearing correct.
- **Privacy:** Recording who said what can make students afraid of judgment.
- **Use boundary:** A saved Transcript must not become grading evidence without agreed boundaries; v1 does not grade.
- **Accuracy:** Voice transcription can create a False Trace.
- **Provenance:** AI suggestions retain AI Provenance after group development.
- **Time:** The facilitator stays short for a fifteen-minute group.
- **Scope:** One Student Group, English and Vietnamese, Idea Trace, and PRD Export in v1.

## 11. Non-Goals (Explicit)

- Grading students or producing participation scores in v1.
- Allowing AI to steer the answer by default.
- Unbounded AI ideation or answer generation.
- Treating AI praise as evidence that an idea is correct.
- Hiding AI Provenance after a group develops an AI-originated suggestion.
- Promising accurate transcription or treating every Transcript as ground truth.
- Turning saved Transcripts into grading records without an explicitly agreed policy.
- Supporting multiple groups in one v1 session.
- Claiming languages beyond English and Vietnamese in v1.
- Claiming improved participation, learning outcomes, adoption, or school traction before measurement.

## 12. MVP Scope and Sequencing

### 12.1 In Scope for v1

- One Student Group session.
- Question-Only Mode as the default.
- Explicit Teacher enablement of Bounded Suggestion Mode with one bounded suggestion.
- One Short Question at a time.
- Contribution capture in an Idea Trace.
- Recall of an idea mentioned once and forgotten.
- Persistent AI Provenance through development and PRD Export.
- English and Vietnamese support.
- PRD Export.
- No grading output.
- Product-level handling of privacy, provenance, and False Trace boundaries sufficient for review. Exact policy is open.

### 12.2 Out of Scope for MVP

- Student grading, rubric scoring, or participation ranking.
- Multi-group orchestration.
- Languages beyond English and Vietnamese.
- A default AI suggestion mode.
- Unbounded AI answers or lecture-like facilitation.
- A confirmed retention, deletion, consent, or access policy not supplied by the replay; these are release-blocking open questions rather than silent implementation details.
- `[NON-GOAL for MVP]` A claim that the product makes students feel safe; the product can preserve the concern and test it, but the replay supplies no evidence or definition.

### 12.3 Sequencing

1. Define the Question-Only Mode, Bounded Suggestion Mode boundary, and Teacher enablement behavior. `[ASSUMPTION: sequencing is proposed to lock the trust model before building adjacent features.]`
2. Define Idea Trace fields, AI Provenance behavior, and False Trace states. `[ASSUMPTION: these are prerequisite definitions inferred from confirmed risks.]`
3. Define privacy, retention, access, correction, and grading-use policy before saving or exporting a Transcript. `[ASSUMPTION: policy decisions are required before release; exact owner and standard are open.]`
4. Implement one-group English/Vietnamese facilitation, idea recall, and PRD Export after the boundaries above are reviewed.
5. Measure the desired outcome only after a baseline, method, sample, owner, and target are confirmed.

## 13. Success Metrics and Counter-Metrics

No numeric success metric was confirmed. The following are `[ASSUMPTION]` measurement proposals, not targets or evidence.

### Primary

- **SM-1 [ASSUMPTION]: Balanced participation signal** — define and measure whether participation is more balanced in a specified evaluation of one Student Group. Baseline, definition of balanced, target, sample, method, and owner are open. Validates FR-1, FR-3, FR-4, and FR-7.

### Secondary

- **SM-2 [ASSUMPTION]: Question-led brevity** — measure whether Student Groups complete the intended brainstorm within the stated fifteen-minute constraint without the facilitator becoming a lecture. Target and method are open. Validates FR-1 and FR-2.
- **SM-3 [ASSUMPTION]: Teacher control comprehension** — measure whether Teachers can identify the active Facilitation Mode and whether Bounded Suggestion Mode was explicitly enabled. Target and method are open. Validates FR-3, FR-9, FR-10, and FR-11.
- **SM-4 [ASSUMPTION]: Idea continuity** — measure whether a previously mentioned idea can be recalled and connected to later development. Target and method are open. Validates FR-7 and FR-8.

### Counter-metrics (do not optimize)

- **SM-C1 [ASSUMPTION]: Student inhibition or fear of judgment** — monitor whether attribution or recording causes students to hold back. This counterbalances SM-1 and validates the privacy boundary.
- **SM-C2 [ASSUMPTION]: False Trace rate or severity** — monitor transcription errors that create incorrect attribution. This prevents optimizing capture volume at the expense of accuracy and provenance.
- **SM-C3 [ASSUMPTION]: Unauthorized grading use** — monitor whether saved Transcripts or exports are used as grading evidence despite the v1 boundary. Target, detection method, and owner are open.
- **SM-C4 [ASSUMPTION]: AI authority signal** — monitor whether students interpret praise or a bounded suggestion as the correct answer. This counterbalances any engagement or completion metric.

## 14. Risks and Mitigations

| Risk | Evidence / impact | Mitigation or unresolved item |
|---|---|---|
| AI praise makes one idea appear correct | User turn 11 | Default to questions; review language; define the bounded suggestion boundary. |
| Attribution makes students afraid of judgment | User turn 12 | Make privacy behavior explicit; decide identity visibility, consent, retention, access, and correction before release. |
| Saved Transcript is used for grading without agreement | User turn 13 | Keep grading out of v1; define permitted use and export policy before saving/exporting. |
| Voice transcription creates a False Trace | User turn 14 | Surface uncertainty and correction state; do not present machine text as unquestionable fact. |
| Short session becomes a lecture | User turn 10 | One Short Question at a time; review prompt length and fifteen-minute flow. |
| Teacher cannot tell whether AI is steering | User turn 9 | Show active mode and explicit enablement; exact Teacher surface remains open. |
| Forgotten ideas disappear | User turn 7 | Provide Idea Trace recall while retaining original provenance. |
| Missing metrics create false confidence | User turn 18 | Keep all targets, baselines, and methods open; do not use invented numbers. |

## 15. Open Questions

1. What definition of “more balanced participation” should SM-1 use, and what baseline, sample, method, owner, and target should accompany it?
2. What exactly makes speaking feel safe for quieter students, and how can that be evaluated without creating a new judgment signal?
3. What student identity, attribution, and visibility behavior is acceptable for an Idea Trace?
4. What consent or agreement is required before Contributions, Transcripts, or PRD Exports are saved?
5. Who can view, edit, export, delete, or correct a Transcript and Idea Trace?
6. What retention and deletion rules apply to saved Transcripts and exports?
7. What rule explicitly prevents a saved Transcript or PRD Export from being used for grading?
8. What exactly counts as one bounded AI suggestion, and how does the product enforce that boundary?
9. How does a Teacher enable Bounded Suggestion Mode, and what evidence of enablement is retained?
10. What wording or behavior prevents AI praise from signaling a correct answer?
11. How are False Traces labeled, corrected, disputed, excluded, and preserved for provenance?
12. What are the device, audio, connectivity, accessibility, and classroom-environment requirements?
13. What does English and Vietnamese support include: prompts, trace labels, export, transcription, or all of these?
14. What is the exact PRD Export format and how are provenance and uncertainty represented in it?
15. Does v1 need a student-visible trace, a teacher-only trace, or configurable visibility?
16. What evidence and revisit trigger would justify future scope beyond one Student Group or the two confirmed languages?

## 16. Assumptions Index

Every `[ASSUMPTION]` below is an inference or proposed product rule, not a confirmed user decision.

- School decision-makers may need deployment and governance details beyond the replay — §3.2.
- Parents, administrators, and IT staff are stakeholders rather than direct v1 users — §3.3.
- PRD Export format and destination were not discussed — §4.
- Mina, Mr. Alvarez, and Linh are illustrative protagonists, not real customers or testimonials — §6.
- Visibility of Mina’s Contribution to the group is inferred; identity display is open — UJ-1.
- A correction or uncertainty state is required for False Traces — UJ-1 and FR-6.
- A Teacher-visible mode label is inferred — FR-3 and FR-11.
- A prompt-length review gate is inferred — FR-2.
- An uncertain, disputed, or correction state is needed; exact label is open — FR-6.
- Relationship preservation and history UI are inferred — FR-8.
- One bounded suggestion needs an explicit boundary definition — FR-10.
- Active mode and enablement visibility are inferred — FR-11.
- PRD Export must preserve AI Provenance — FR-12 and FR-16.
- Preserving uncertainty in export is inferred — FR-16.
- Audience minimization and export governance are inferred from privacy risks — §9.1.
- Accessibility and reliability reviews are needed; standards and thresholds are not confirmed — §9.4.
- Product-level handling of privacy and False Trace boundaries is release-relevant; exact policy remains open — §12.
- Sequencing is proposed to lock trust and provenance before adjacent features — §12.3.
- All SM definitions and counter-metrics are measurement proposals, not targets — §13.

## 17. Acceptance Criteria

- **AC-1:** A new v1 session starts in Question-Only Mode unless a Teacher explicitly enables Bounded Suggestion Mode.
- **AC-2:** The facilitator presents one Short Question at a time and does not become a lecture in the fifteen-minute scenario review.
- **AC-3:** The Idea Trace records captured Contributions and preserves their stated origin.
- **AC-4:** A previously mentioned idea can be brought back without being represented as a new or silently rewritten idea.
- **AC-5:** Any AI suggestion remains labeled with AI Provenance after the Student Group develops it.
- **AC-6:** AI praise or approval language does not make one idea appear to be the correct answer in content review.
- **AC-7:** The product has a reviewed behavior for possible False Traces and does not present uncertain transcription as unquestionable fact.
- **AC-8:** V1 supports one Student Group and English and Vietnamese; the product does not claim broader coverage.
- **AC-9:** PRD Export is available from the Idea Trace and preserves the applicable provenance and uncertainty boundaries. `[ASSUMPTION: exact export shape remains open.]`
- **AC-10:** V1 produces no student grades, scores, or grading judgments.
- **AC-11:** Saved Transcript and export behavior has an explicit, reviewed boundary against unauthorized grading use before release. `[ASSUMPTION: release gate inferred from user turn 13.]`
- **AC-12:** Numeric success targets, customer evidence, testimonials, traction, and impact claims absent from the replay are not presented as confirmed facts.

## 18. Golden Quality Gate Coverage

This final PRD includes the required executive summary, problem, target users, jobs to be done, glossary, named user journeys, solution thesis, seven feature groups, seventeen numbered functional requirements, non-functional requirements, privacy and governance guardrails, non-goals, scope and sequencing, success and counter-metrics, risks, assumptions, open questions, and acceptance criteria. It preserves teacher-control, privacy, provenance, non-grading, and missing-metric boundaries from the replay and keeps unconfirmed details open.
