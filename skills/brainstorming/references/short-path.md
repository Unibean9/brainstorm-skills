# Short Path (`--sp`)

Use this mode only when the invocation explicitly includes `--sp`. It is for a user who wants to provide the important idea once and receive an expanded, useful direction without walking through the normal brainstorming stages.

## Intake

Ask for only the user's key input in one concise message: what they want to build or explore, who it is for or what problem it addresses, and the desired outcome. Mention that they may include constraints, references, or existing files, but do not turn these into a questionnaire. If the opening message already contains enough of this, do not ask another question; acknowledge the input and proceed.

Do not open the browser composer, ask the user to choose a stance or techniques, offer a technique menu, or run an interactive convergence loop. `--sp` is the user's process choice.

## One-pass expansion

After intake, work autonomously in one internal pass. Use relevant knowledge from the model to fill missing components such as target users, jobs, value proposition, core experience, differentiators, alternatives, risks, and a sensible first scope. Do not claim invented market facts, customer evidence, metrics, testimonials, validation, or technical guarantees. Treat model-supplied content as a proposal, not as user intent.

Keep provenance explicit:

- Record the user's statements as user direction or user ideas.
- Record derived ideas as coach/model ideas.
- Mark inferred facts, choices, and constraints as `[ASSUMPTION]` and include them in the open questions or assumptions section.
- If a missing decision materially changes the direction, choose a reasonable default for this pass and flag it for review instead of stopping for another round of questions.

The internal expansion should cover, at minimum:

1. the problem and the people affected;
2. the proposed direction and its core user journey;
3. a small set of useful capabilities and differentiators;
4. key trade-offs, risks, and unresolved questions; and
5. a recommended next step or MVP boundary.

Do not expose a fake sequence of brainstorming techniques. Present the result as a compact synthesis with clear labels for user input, agent proposals, assumptions, and decisions.

## Persistence and output

Bind `{doc_workspace}` using the same convention as the normal session. Create the memlog as soon as the topic is known. Keep the regular memlog mode value `autonomous` for compatibility with existing resume tooling and add `short_path=true` when the memlog helper accepts extra fields. Log the short-path choice and all material user directions, agent proposals, assumptions, and decisions; use the available `by user`/`by coach` author markers.

By default, finish in the same turn with:

- the updated `.memlog.md`; and
- a succinct `{doc_workspace}/brainstorm-intent.md` suitable as input to the PRD skill.

Do not ask which artifact to make. Produce `brainstorm.html` only when the user explicitly requests it or the caller's artifact settings require it. Mark the session complete after the synthesis and share the output paths. If the user later corrects an assumption, update the memlog and intent rather than defending the inferred content.

When `--sp` is combined with a non-interactive/headless caller, do not ask the intake question. Use the supplied `topic`, `goal`, `context`, and other payload fields, record every inference in `assumptions[]`, and return the caller's required status payload after writing the same artifacts.
