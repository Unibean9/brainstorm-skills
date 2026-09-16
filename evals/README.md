# Evaluation set

The evaluation set is intentionally written in English so it can be reused across agents and runtimes. Each case contains a basic idea followed by 19 user turns. The turns exercise opening, framing, divergent exploration, perspective shifts, critique, convergence, confirmation, and the explicit handoff to PRD and final artifact generation.

## Golden data

[`golden-data.yaml`](golden-data.yaml) is the source of truth. It defines:

- the exact user turns;
- the chosen brainstorming stance and output branch;
- provenance and anti-fabrication rules;
- quality gates for a complete PRD, one self-contained HTML landing page, and a deep single-file HTML deck.

## Recorded live runs

- [`runs/01-goc-ban-cong`](runs/01-goc-ban-cong) — complete PRD plus one HTML landing page.
- [`runs/02-tablemate`](runs/02-tablemate) — complete PRD plus a 12-slide pitch deck with speaker notes.
- [`runs/03-community-cabinet`](runs/03-community-cabinet) — complete PRD plus one HTML landing page and 11-slide HTML pitch deck.

These are review fixtures: compare a future live run against the source turns and the quality gates, not only against wording.

The evaluator also checks visual depth: landing-page section count and interaction signals, plus deck speaker notes, print styles, and visual-mode variety.

Re-run the recorded evaluation with:

```bash
python evals/run_eval.py
```
