---
case: 02-tablemate
title: Tablemate
mode: headless replay
stance: creative_partner
branch: frontend-design: pitch-deck
source: evals/golden-data.yaml
---

# Recorded Replay — Tablemate

The 19 user turns below are reproduced verbatim from `evals/golden-data.yaml`. Assistant responses are concise facilitation records. Ideas, critiques, decisions, boundaries, and missing evidence remain attributed to the user.

## Opening

1. **User:** I want to help student groups brainstorm more fairly in class.

   **Assistant:** I’m capturing the goal as fairer classroom brainstorming. **Question:** What makes the current group experience feel unfair?

## Framing

2. **User:** The first problem is that one fast, confident student pulls everyone toward their own idea.

   **Assistant:** The first problem is dominance by one fast, confident student, which can pull the group toward one idea. **Question:** Who is missing from that conversation?

3. **User:** Quieter students may have good ideas but cannot enter the conversation.

   **Assistant:** The participation gap is explicit: quieter students may have ideas but no easy entry into the spoken exchange. **Question:** What constraint does the teacher face while groups are working?

4. **User:** A teacher cannot stand in the middle of every group and manage every speaking turn.

   **Assistant:** The teacher cannot manually manage every group’s speaking turns, so any direction must operate without the teacher standing inside each group. **Question:** What different mechanisms could create room for more voices?

## Diverging

5. **User:** We could use speaking tokens, ask everyone to write before talking, or use a bot that reminds people to make room.

   **Assistant:** I’m recording three candidate mechanisms: speaking tokens, write-before-talk, and a bot reminder to make room. **Question:** What would a facilitator do beyond reminding people to take turns?

6. **User:** The group wants a voice facilitator that asks one short question at a time and records what each person contributed.

   **Assistant:** The voice-facilitator direction is concrete: one short question at a time, with a trace of each person’s contribution. **Question:** What should happen to ideas that receive no immediate attention?

7. **User:** It could also bring back ideas that were mentioned once and then forgotten.

   **Assistant:** I’m recording idea recall as part of the direction: the facilitator can bring back an idea that was mentioned once and then forgotten. **Question:** What would make participation feel safer from a quieter student’s point of view?

## Shifting

8. **User:** Look at this from the shy student's point of view: what would make speaking feel safe?

   **Assistant:** The lens shifts to psychological safety for the shy student; the product must not assume that more recording automatically creates more participation. **Question:** What must the teacher be able to see to trust the facilitator?

9. **User:** Look at this from the teacher's point of view: what must be visible so they trust that AI is not steering the answer?

   **Assistant:** Teacher trust requires visibility into whether AI is steering the answer. **Question:** What is the shortest useful interaction for a group with only fifteen minutes?

10. **User:** Look at this from a group with only fifteen minutes: the facilitator must stay short and cannot become a lecture.

   **Assistant:** The time constraint is explicit: prompts must stay short and the facilitator cannot become a lecture. **Question:** What failure would make an AI facilitator feel unfair even if everyone gets a turn?

## Critiquing

11. **User:** AI might praise one idea and accidentally make the group think it is the correct answer.

   **Assistant:** Praise can become accidental authority, so the facilitator must not make one idea appear correct through approval. **Question:** What other kinds of trace could make students hold back?

12. **User:** Recording who said what might make students afraid of being judged.

   **Assistant:** Attribution can improve traceability but can also make students afraid of judgment. This is a privacy and participation trade-off, not a solved design choice. **Question:** What could go wrong after a transcript is saved?

13. **User:** If the transcript is saved, a teacher might use it for grading even though the group did not agree to that.

   **Assistant:** A saved transcript must not silently become a grading record; the use boundary and group agreement remain critical. **Question:** What happens when the voice trace itself is wrong?

14. **User:** Voice transcription may misunderstand a student and create a false trace.

   **Assistant:** A transcription error can create a false attribution, so any trace must preserve uncertainty and provide a way to notice or correct errors. **Question:** Which default would keep authority with the group and teacher?

## Converging

15. **User:** The default mode should only ask questions. A mode where AI contributes one bounded suggestion must be explicitly enabled by the teacher.

   **Assistant:** This is the control decision: question-only is the default; bounded AI contribution requires explicit teacher enablement. AI should not quietly steer the answer.

16. **User:** The first version supports one group, English and Vietnamese, a trace of ideas, and PRD export. It does not grade students.

   **Assistant:** V1 scope is explicit: one group, English and Vietnamese, an idea trace, and PRD export. Grading is out of scope.

## Confirmation

17. **User:** Any AI suggestion must keep its AI provenance even if the group likes it and develops it further.

   **Assistant:** Provenance is a confirmed invariant: an AI suggestion remains identified as AI-originated through later group development.

18. **User:** The desired outcome is more balanced participation, but we do not have a numeric metric yet.

   **Assistant:** The desired outcome is recorded without inventing a target. No numeric success metric is confirmed; the PRD must keep measurement open.

## Handoff

19. **User:** Create a complete PRD and then create one deep HTML pitch deck using prd.md for teachers and school decision-makers. Missing metrics must remain open questions.

   **Assistant:** Handoff accepted. I’m creating the final PRD and deriving a self-contained pitch deck from it for teachers and school decision-makers. Missing metrics, privacy policy details, and other unspecified choices will remain open questions or be marked `[ASSUMPTION]`.
