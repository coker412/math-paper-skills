---
name: math-paper-writing
description: Draft, revise, audit, or prepare mathematical manuscripts and submission materials; distill reusable mathematical writing choices from an author's papers or the researcher's own drafts, including small samples. Use for writing and style analysis, not standalone proof search or learning editions.
---

# Mathematical Paper Writing

Write papers readers can understand, check and use. Mathematical fidelity is essential; also organize the argument, explain decisive choices and allocate detail to the intended reader. State supported contributions directly, with their necessary scope, without a default limitations paragraph.

## Identify whether to draft or revise

Resolve the source mathematics, audience, scope, accepted author decisions and destination from the request and project. Follow applicable repository rules for evidence, paths, builds and publication. Ask only about unresolved choices that materially affect the task.

For a **first draft**, deliver prose, statements and proofs, not just an outline. Use the [first-draft guidance](references/exposition-and-structure.md#from-results-to-a-first-draft). Organize the question, contribution and dependencies; write the body, then the full introduction, then the abstract. Source-note chronology need not dictate exposition.

For a **revision**, use the authoritative manuscript as baseline. Diagnose a concrete reading difficulty; retain effective text and approved choices outside scope. A local edit covers its passage, neighboring argument and dependencies; a whole-paper review includes proofs, appendices and included files. Neither scope implies a rewrite quota.

## Scope and mathematical boundaries

- Preserve hypotheses, quantifiers, definitions, domains, conclusions and evidence status. Language editing does not authorize proof completion or certify a result. Expose unsupported implications and their downstream effects.
- Preserve approved notation, LaTeX structure, labels, citations, terminology and declarations. Introduce necessary nonstandard objects before use. Before adding or renaming an object, apply the [notation and necessity gate](references/mathematical-integrity.md#notation-and-necessity).
- Do not invent citations, priority, motivations, examples, applications or declarations. Keep heuristic explanations distinct from formal claims and audit history outside manuscript prose.
- Honor requested language and synchronization scope; report existing divergence. Preparing submission materials does not authorize submission.

## Load guidance for the writing task

Load this entrypoint before batching manuscript and reference reads. Reuse instructions and source text already visible in context. Read only the relevant **sections** below; a linked file is not automatically a requirement to load every section. Locate headings with `rg -n '^##' PATH` and read bounded ranges. Recover missing context when needed rather than guessing.

For the two language reviews, use `python <skill-dir>/scripts/language_rules.py <installed-skill>/SKILL.md --language en` (choose `zh` for Chinese manuscript prose, `both` for bilingual work). This [version-checked reader](scripts/language_rules.py) returns the original rules unchanged, deferring reviewed examples and the other language's duplicate text. Return one skill at a time within the tool budget. Read a deferred example at its source line range when its rule is unclear; never infer applicability from a keyword alone. Unknown revisions or unavailable helpers require bounded reading of the original skill, not silent filtering. This is an original-rule review, not a claim to have read every example.

For successive edits to the same manuscript, reuse loaded guidance and confirmed conventions. Read the current changed passage and affected dependencies; refresh stale or compacted-away context. Group related requested edits before final review/build, and report material gaps as they arise. Do not expand a local revision into a whole-paper audit or load unrelated workspace protocols solely because the text contains a proof; applicable repository requirements still govern.

| Task | Required additional guidance |
| --- | --- |
| Ordinary local prose edit | The two language interfaces in step 3; the boundaries above and final read-back below suffice unless a mathematical or structural issue arises |
| Draft claims, change a formal statement, edit a proof-bearing step, or audit mathematics | [Mathematical integrity](references/mathematical-integrity.md) |
| Whole-paper composition or structural revision | Full [exposition guidance](references/exposition-and-structure.md) |
| Local abstract, introduction, proof exposition or notation work | Corresponding sections of [exposition guidance](references/exposition-and-structure.md); include dependencies and content-selection guidance when reorganizing. For introductions, execute its prose read-back and source reconciliation |
| TeX edits/builds | Project-preservation and build sections of [LaTeX guidance](references/latex-and-bilingual-writing.md); theorem, bibliography, translation and typography sections only when touched |
| Figures/captions; submission/referee response; genre/audience change | The applicable [figure](references/figures-tables-and-diagrams.md), [submission](references/submission-and-peer-review.md), or [voice](references/voice-and-genre.md) guidance |
| Author-profile distillation | Invoke original [Writing DNA](assets/writing-dna-skill/SKILL.md) with [mathematical adaptations](references/style-distillation.md). Standard: twenty complete works and five reports; explicitly chosen provisional profile: three or more works. Never reduce a requested count. Optional [Tao](references/profile-tao.md) and [field profiles](references/field-profiles.md) load only when relevant |
| Learning edition | Use `math-paper-study-guide`, which owns teaching detail |

Budget combined tool output so it arrives intact. Use bounded ranges or the [exact text reader](scripts/read_text.py); for a complete read, continue its `next_start` with the source hash until the end. Character limits are not token limits. After truncation, recover missing ranges, not entire already-read files. An outline or keyword search does not establish full manuscript coverage.

## Execute the requested review

1. **Read and establish coverage.** Follow the source's section/proof boundaries. Keep compact locations for issues and retained decisions in working context; distinguish revised, reviewed-and-retained and unread material. No new checklist or per-paragraph report is required.
2. **Write and assess.** Mathematical writing owns content selection, structure and proof-bearing edits. Complete the requested text; compare the benefit against added length, notation and navigation. Preserving mathematics does not require preserving every proof sentence.
3. **Apply both language reviews.** Read the [anti-defensive interface](references/anti-defensive-interface.md) and [Humanizer interface](references/humanizer-interface.md), and actually apply the available original anti-defensive-writing, then Humanizer. Reuse loaded instructions and the same visible manuscript; these are review stages, not automatic separate agents or full-file rereads. Inspect clean-looking prose too; retention is valid. For each review retain a concrete passage and reason in working context. Disclose unavailable add-ons. Useful explanations and mathematical contrasts survive the [function check](references/anti-defensive-interface.md#check-function-before-editing).
4. **Check the final version.** Compare changed text with its mathematical source and neighboring argument, and inspect the actual diff. A later edit reopens that passage and dependencies. Apply the relevant [delivery checks](references/delivery-checks.md) and required build/visual checks; rerun only checks affected by subsequent changes or unresolved failures. Match completion claims to actual coverage.

## Delivery and maintenance

Deliver the requested prose or edited files and a short note on changes, review scope and unresolved issues. Do not echo a whole source file, long diff, build log or review ledger when a file and a focused comparison suffice; honor explicit requests for full text. Keep complete build logs on disk and return status/diagnostic summaries, expanding relevant errors on failure. Build success is not mathematical certification.

Execute helpers without loading their implementation: [PDF pages](scripts/pdf_pages.py), [TeX diagnostics](scripts/check_tex_log.py), [bounded text](scripts/read_text.py); use `--help` when needed. Reuse editable or page-labelled source. PDF indexes/search hits are not reading evidence; complete required text/notation/figure inspection. Log scans do not establish build freshness or PDF quality.

Only for maintenance, evaluation or source questions, read [sources](references/sources.md) and [evaluation cases](references/evaluation-suite.md). Benchmark runs and their reports are not steps to repeat during ordinary manuscript work.
