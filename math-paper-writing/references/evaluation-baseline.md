# Evaluation baseline

## 2026-09-04 maintainer dry-run

**Scope:** `math-paper-writing` after adding submission, peer-review, visual, genre, voice, traceability, and evaluation guidance.

**Method:** The maintaining agent applied E01--E12 in the same context used to edit the skill and recorded the decision each fixture elicited. This is a coverage and self-consistency test, not an independent behavioral evaluation. No paper file, external submission, or publication account was used.

| Case | Observed decision | Hard failures | Verdict |
| --- | --- | --- | --- |
| E01 | Retained `proof-draft`; rejected unrestricted solution, novelty, and optimality language pending evidence and literature gates | 0 | pass |
| E02 | Flagged `f` as unchosen; offered either an explicit choice followed by a supported property or a correctly quantified combined statement | 0 | pass |
| E03 | Identified the missing implication rather than rewriting it as routine; preserved upstream work and froze dependent claims | 0 | pass |
| E04 | Treated the label, reference, citation key, parameter interval, delimiters, and `Faber--Krahn` typography as protected | 0 | pass |
| E05 | Restored the universal quantifier, interval `(0,T)`, and connectedness assumption in the Chinese version; required affected proofs to be compared | 0 | pass |
| E06 | Rejected the visual's proof claim; required axes, parameter range, non-color encodings, provenance, and reproducibility information | 0 | pass |
| E07 | Drafted only verified title/result/fit material; left exclusivity, consent, conflicts, permissions, and novelty unresolved and took no external action | 0 | pass |
| E08 | Kept the necessary compactness hypothesis, grounded the disagreement at its proof use, and proposed a manuscript clarification synchronized with the response | 0 | pass |
| E09 | Converted the named-author request into high-level traits and prioritized the approved researcher sample without copying distinctive wording | 0 | pass |
| E10 | Required a dependency contract and relocation of necessary hypotheses and the boundary-case proof before shortening | 0 | pass |
| E11 | Refused to infer commutativity from common endpoints or the word `natural`; required typed arrows and proof, and clarified blank table entries | 0 | pass |
| E12 | Reported the undefined citation and limit-interchange gap separately and refused to infer mathematical correctness from compilation | 0 | pass |

## Remaining validation boundary

The twelve fixtures have zero hard failures in this maintainer dry-run. They have not yet been run in fresh model contexts or evaluated by an independent agent. A future independent run should use the protocol in `evaluation-suite.md`, preserve the raw outputs, and compare failures against this baseline rather than assuming these verdicts transfer.

## 2026-10-15 execution-contract maintenance

Maintainer: GPT-6 Astra. Skill entry SHA256: `f4ed98708d5c0ab545bb29e1c0d157ebb5e9807a396c55173a977630083157e4`. Scope: inherited author decisions, output locations, evidence-matched delivery, and causal repair scope. Structural validation passed using the supplied quick_validate.py with /usr/bin/python3; all 12 relative Markdown reference targets exist. The graphlab/default Python lacked PyYAML, so the existing system interpreter was used without installing dependencies.

The following is an in-context maintainer walkthrough, **not** a fresh-context execution or independent behavioral test. The fresh-context release gate remains unperformed; do not describe this update as behaviorally validated.

| Cases | Maintainer decision under the fixture | Validation boundary |
| --- | --- | --- |
| E01 | Keep the main claim proof-draft; omit unrestricted solution and priority claims. | Reasoned response only. |
| E02 | Choose the asserted isomorphism explicitly before discussing its continuity; do not quantify over all isomorphisms. | Reasoned response only. |
| E03 | Identify the missing implication and keep dependent claims conditional. | Reasoned response only. |
| E04 | Change prose only; retain labels, reference keys, interval and mathematical typography. | No new TeX fixture executed. |
| E05 | Restore the English source's universal quantifier, open interval and connectedness in the translation. | Reasoned response only. |
| E06 | Remove the proof claim; require axes, parameter range, non-color encoding and reproducible provenance. | No plot generated. |
| E07 | Draft only verified mathematical/fit content; leave unsupported declarations unresolved and do not submit. | No external action. |
| E08 | Retain necessary compactness, explain its proof use, and synchronize any clarification. | Reasoned response only. |
| E09–E11 | Preserve approved voice, necessary proof dependencies and typed/proved diagram identities; the new baseline guidance does not authorize imitation or mathematical changes. | Coverage review, no independent run. |
| E12 | Separate citation/proof defects from a successful compile; do not certify the paper. | Reasoned response only. |
| E13 | Compare the approved template beyond its class name; preserve the latest accepted short abstract and declaration. | New fixture added; fresh-context run pending. |
| E14 | Reuse the existing output paths and fix native output configuration before building; inspect the file listing. | Prior Q25 native-config build is direct artifact evidence, not a new isolated skill evaluation. |
| E15 | Put cross-project execution agreements in the user-level entrypoint and the manuscript-specific behavior in the shared skill. | Actual changes and paths checked in this turn; future model compliance not established. |

The original 2026-09-04 baseline is retained above. New fixture definitions are in evaluation-suite.md. This historical record describes the maintainer walkthrough; it requires no private workspace artifacts to use the skill.

## 2026-11-03 task execution and targeted regression

A separate testing agent, without the maintainer's verdicts or evaluation references, executed six synthetic writing requests in one fresh context: a conditional-result abstract, a false uniform-convergence argument, bilingual quantifier repair, a two-work style profile with duplicate versions, a cover letter with unknown declarations, and an accepted classification statement. The maintainer inspected the actual responses. Mathematical scope, source counts, translation constraints, and unknown declarations were preserved in these cases. The abstract nevertheless repeated its hypothesis and included commentary about retaining it: a concrete exposition failure despite mathematical fidelity.

The exposition guidance was revised to state each necessary qualification once and avoid padding an approximate word target. The same tester then produced a revised conditional abstract and an abstract for different classification material. Both stayed shorter than the suggested length without repetitive qualifications or invented facts; editing notes stayed outside the manuscript. These are targeted regressions, not two additional independent contexts or a causal test of the anti-defensive add-on, which was not loaded in this run.

Raw requests, responses and maintainer checks are retained with the maintenance task. The six tasks and two regressions do not establish execution of all 24 numbered fixtures, general reliability on long manuscripts, or reader preference. The structural resource checker verifies reference routing and fixture completeness only. The earlier dry-runs remain historical evidence at their stated scope.

## 2026-11-04 fidelity-first exposition development

The maintainer wrote and inspected responses for E25–E30, eight instantiated fidelity regressions E01–E08, and two focused learning questions. Requests, full responses and individual judgments are distributed in the repository's `tests/writing-quality.md` (workspace distribution: `tools/tests/writing-quality.md`). The new quality cases exercise result hierarchy, estimate mechanisms, local-to-global compatibility, audience-dependent detail, a deliberately unchanged original and a complete short section. Five revisions plausibly improve particular dimensions; one original remains unchanged. This is not a measured success rate.

The E28 fixture was clarified during development to require compact closure in a metric space; precompactness without the needed limit existence is insufficient. The record distinguishes this fixture repair from a demonstrated failure of the old skill. Existing authentic-paper comparisons also retain rejected compression attempts; these motivated keeping length and quality separate.

This work was performed in one authoring/review context. The fresh-context release protocol and human-reader comparison have not been completed for these changes. The quality dimensions are an editorial aid, not a validated scale. No claim of causal improvement, human comprehension, model preference agreement, or long-manuscript performance follows from these examples. The resource checker now verifies 30 case definitions, not 30 behavioral passes.

### First-draft follow-up

Researcher feedback identified that the entrypoint and quality examples still emphasized revision. The entrypoint now distinguishes composition from revision; the exposition reference supplies a compact first-draft route. E31 uses unordered spectral facts without an existing manuscript. The maintainer produced a complete short section with motivation, proposition and proof, recorded in the same development report. Source fidelity and completed exposition were checked separately. This remains same-context self-review; the checker now covers 31 case definitions. The earlier evidence and snapshots above remain historical records.

## 2026-11-04 introduction execution follow-up

E32 adds an authentic public-source introduction task. The maintainer drafted an introduction focused on Ellenberg–Gijswijt's cap-set consequence, read back its question/result/payoff/mechanism, checked it against fixed source passages, and narrowed one comparison sentence. Three follow-up controls exercise missing literature, an unsupported support claim and mechanism compression. E01–E08 were repeated at their supplied fragment scope. Actual outputs are retained in the distribution's tests/writing-quality.md. This is same-context development, with prior access to the original introduction, not independent evaluation or evidence of better reader comprehension. Static validation now covers 32 case definitions; it does not execute them.

## 2026-11-04 content selection and skill coordination

E33 exercises structural versus language-only scope, contextual clarification, repeated paragraph functions, causal expansion, iterative integration, protected mathematical contrast, whitelist applicability and teaching detail. Actual supplied inputs and outputs are retained in tests/writing-quality.md in the distribution; E01–E08 were repeated at fragment scope. This is same-context maintenance, not independent execution or reader validation. Two documented mathematics-only additions to bundled upstream skills were checked by reconstructing the original hashes. Static validation covers 33 case definitions, not 33 behavioral passes.

## 2026-11-04 explanation-function follow-up

The E33 extension records ten synthetic same-context outputs: three contextual deletions, one framing-only revision, five retained effective passages and one unresolved-context retention. Read-back checks mathematical meaning and reader function separately; negative controls distinguish an unproved stronger conclusion from a proved negative result. This is a narrow development walkthrough, not a fresh-context test or measured quality gain. Earlier cases were not newly rerun. The case-definition count remains 33. The entrypoint, anti-defensive interface and delivery check now route this decision at actual edit time.

## 2026-11-04 execution-coverage follow-up

Five synthetic input/output tasks were completed in the maintenance context after reading the original anti-defensive-writing and Humanizer instructions and applying their mathematical interfaces. The tasks cover a clean introduction with padded proof prose, a wholly retained proof, a local-only edit with an out-of-scope mathematical defect, a first draft from notes, and a redundant disclaimer adjacent to a useful contrast. Each has actual final prose and passage-specific outcomes for both language reviews, retained in the distribution's `tests/writing-quality.md`. Exact-retention and artifact-hash checks passed; mathematical read-back and editorial judgments are recorded separately as maintainer judgments.

Two evaluator controls reject an unsupported whole-paper completion claim and a review based on a version preceding the last edit. These are checks of the grading criteria, not successful executions by another agent. The five development outputs and controls do not measure repeatability, quality gain over the previous skill, or independent/human-reader agreement. E01–E08 were not newly rerun; fresh-context regression and repeated trials remain open. The case count stays 33 because these are E33 variants. No manuscripts or published remote repositories changed in this follow-up.

### Authorized fresh-context execution follow-up

After the development tests above, the researcher authorized three independently spawned fresh-context executions of the same short whole-text revision request. All three explicitly used the main skill, accessed both original language skills, revised the padded proof opening, retained the clean statement and useful T/n distinction, and supplied passage-specific review outcomes. The maintainer inspected actual tool-call/return records and final artifacts. Nonblank original skill lines were recovered from normalized returns across reads; this checks exposure, not understanding. Source comparisons confirmed that the statement and application paragraph were retained. The unspecified application itself was not independently proved. Actual outputs and the tested entrypoint hash are in `tests/writing-quality.md`.

This is 3/3 observed execution on one repeated short task, not a general reliability rate, a baseline-controlled improvement or blinded quality evaluation. E01–E08 and long manuscripts were not newly tested. All three traces exposed repeated instruction reads following output truncation; loading efficiency remains unresolved. No extra runtime framework or completion-form validator was added, and the tested execution guidance was not changed after the runs.

## 2026-11-04 longer-manuscript coverage and read-cost pilot

One fresh-context baseline run and two fresh-context runs of the revised entrypoint edited the same isolated 1,025-line manuscript, producing 14-page PDFs. The writers received the same task and source, without the planted-target list or other writers' outputs. Five target locations covered introduction padding, an inflated proof explanation, a duplicated cutoff explanation, an unsupported pointwise-to-global-uniform inference near the end, and appendix filler. Necessary fixed-parameter qualifications served as retention controls. These are intentionally injected test defects, not findings about the live paper. The maintainer inspected all final diffs; this is not blinded reader assessment.

All three resolved the five targets and retained the useful qualification, formal statement/definition blocks, equations, labels, citations and bibliography. Builds and final log scans passed. Visible tool returns contained matches for all 935 nonblank manuscript lines. That establishes text exposure only, not understanding or independent proof certification. No live source changed.

Process inspection found a real failure hidden by the baseline's apparently successful output: 21 nonblank Humanizer lines and 12 exposition-reference lines were absent from its visible returns after truncation. Both revised runs exposed all nonblank lines of the required references and original language skills. The revised runs still had truncated returns, however, and neither invoked the optional new reader. Thus complete recovery was observed twice, not mechanically guaranteed by the skill.

| Run | Total input tokens | Cached input | Uncached input | Output tokens | Tool calls | Truncated returns | Seconds |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Baseline | 1,133,638 | 1,061,248 | 72,390 | 5,273 | 16 | 4 | 216.7 |
| Revised 1 | 1,118,179 | 954,496 | 163,683 | 5,457 | 16 | 2 | 258.2 |
| Revised 2 | 868,614 | 802,304 | 66,310 | 4,983 | 13 | 4 | 237.1 |

These are recorded cumulative token categories, not unique text or monetary charges. Revised 1's final model step recorded 92,242 input tokens with zero cache hits; its cause was not established. Revised 2 used about 8.4% less uncached input, while Revised 1 used more. Neither wall-clock time improved. This pilot does **not** demonstrate stable end-to-end cost savings or a general miss rate.

The stdlib `read_text.py` helper returns exact bounded UTF-8 slices with source hashes and continuation offsets. A subsequent prompted recovery in the baseline's existing context used it to fill the observed instruction gaps: 6,321 source characters instead of reloading both 52,345-character files, zero truncated returns, all previously missing lines exposed, and no further manuscript edits. This is about 88% less source text for that recovery operation, not 88% lower total task cost or autonomous adoption. The recovery added 5,818 uncached input tokens, 381,440 cached input tokens and 1,623 output tokens; it is excluded from the baseline table. Its original incomplete run remains recorded as incomplete.

Nine helper tests passed, including Unicode/long-line slice reconstruction, exact CRLF output, stale-hash rejection and invalid inputs. The entrypoint now addresses combined tool-output budgets, structural coverage and reuse of already visible text. The helper is optional and does not summarize, filter or replace either original language review. The unchanged original skills and actual prose still require review. Raw manuscript variants and trace summaries remain in the local maintenance artifacts; they are not bundled as a public author example. This pilot supplements E33; it does not rerun E01–E08 or satisfy the entire release gate.

Tested baseline entry SHA256: `7afdfda11eb6c0af590510eee8ed4044e57ee5370a11a2fcacf004385945ef56`. Tested revised entry SHA256: `9041c1688e0da83ca8bd093de5ae8434165ea321d90beaaa149aa357301da7d6`.

## 2026-11-04 instruction-budget revision

The entrypoint, Humanizer interface and delivery checks were deduplicated. Detailed notation/necessity gates moved verbatim to mathematical-integrity.md and remain required before adding or renaming objects. Both original language skills are unchanged and still run by default. Local tasks now select relevant reference sections; whole-paper structure work still reads the full exposition guide. Review stages reuse visible source text in the same agent by default, and final build/log/report handling avoids duplicate full outputs. Repository checks and required mathematical coverage are retained.

Measured instruction sizes for a single cold load, including both complete original language skills:

| Assumed task | Previous UTF-8 bytes | Revised UTF-8 bytes | Reduction |
| --- | ---: | ---: | ---: |
| Local prose edit | 80,501 | 70,993 | 11.8% |
| Local proof exposition | 109,461 | 83,853 | 23.4% |
| Abstract with mathematical claims | 109,461 | 81,881 | 25.2% |
| Whole-paper TeX revision | 117,229 | 105,004 | 10.4% |

The local proof/abstract cases do not edit TeX files. The whole-paper case does not change bibliography, figures or translation; those tasks add their relevant guidance. All cases exclude optional profiles, manuscript/task text, workspace rules, tool returns, repeated context and cache effects. These are reproducible file/section byte totals, **not measured model-token savings or monetary costs**. The entrypoint itself falls from 12,638 to 7,913 bytes. Original add-on hashes, verbatim gate preservation and resource routing were checked; semantic-contract comparison was maintainer review. No new independent writing runs were performed, and the preceding pilot does not validate this later revision's behavior. Full E01–E08 and reader evaluation remain unrerun for this update.

## 2026-11-04 local before/after budget test

Two fresh-context agents, both gpt-6-astra, received the same self-contained proof-editing task with the Statement locked. One used the pre-compression snapshot and one the compressed snapshot. Neither received expected answers, prior results or the grading list. No browsing, TeX build or additional agents were part of the task. The maintainer inspected both actual outputs and visible tool returns.

Both revisions preserve the Statement verbatim, the integrating-factor calculation, absolute-continuity/a.e. justification, supremum bound and necessary fixed-T qualification. Both reorder the proof into derivation → bound → convergence and remove inflated framing and the irrelevant general-theory disclaimer. The revised-skill output additionally writes the integrated inequality explicitly, exposing the initial-value term. These are maintainer editorial judgments, not blinded reader preference or independent proof certification.

| Metric per writing run | Before compression | After compression |
| --- | ---: | ---: |
| Cumulative input tokens | 349,520 | 291,806 |
| Cached input tokens | 316,160 | 260,480 |
| Uncached input tokens | 33,360 | 31,326 |
| Output tokens | 2,759 | 2,123 |
| Tool calls | 8 | 7 |
| Truncated returns | 2 | 1 |
| Elapsed seconds | 95.2 | 71.1 |

Uncached input decreased 6.1%, output 23.1%, and duration 25.3% in this pair. These are complete individual writer runs, excluding parent evaluation/recording work; no monetary saving is calculated. The new trace used relevant reference sections. Both traces exposed all 343 nonblank anti-defensive-writing lines and all 319 Humanizer lines after recovery, and the source-to-output comparisons support actual application. Line exposure alone does not establish comprehension. Truncation still occurred; automatic prevention is not solved.

This is one paired local task, not a stable average, a full-paper regression, E01–E08 rerun or an unskilled control. The fixed cost remains substantial for a short passage. No bad run was discarded or repeated to improve the result. Earlier long-manuscript cost variability remains relevant. Runtime skill instructions were not changed after this test.

Tested old entry SHA256: `9041c1688e0da83ca8bd093de5ae8434165ea321d90beaaa149aa357301da7d6`; tested compressed entry SHA256: `7ee1186bae52c4e03ec02f2c85a5030bf939f2c718365f0086248e3749309d50`.

## 2026-11-04 original-rule views and successive edits

The installed original language skills remain byte-identical. A stdlib reader uses a reviewed SHA256-bound line map to return their original rules, deferring illustrative blocks and selecting one original anti-defensive language version. It makes no textual summary or heuristic rule selection at runtime. Unknown revisions exit with a request to read the original in bounded chunks. English/Chinese defaults follow manuscript language; bilingual work keeps both. An ambiguous rule requires its deferred example. The map is a local reading adaptation, not an upstream modification or a claim of full-file reading.

The maintainer read both entire sources and checked every omitted span. Humanizer rules 21, 23 and 25 remain complete because their examples contain operational instructions or constitute the rule. All 33 numbered rules, false-positive guidance, mathematical interface protections and invocation steps remain available. The English and Chinese anti-defensive sections were reviewed for corresponding requirements, with their language-specific rules retained in each version. Required selected lines match the source verbatim. Twelve portable helper tests passed, including language selection, unchanged rule text, unknown-source failure and range validation. Both original hashes are recorded in the distributed `scripts/language-skill-ranges.json`.

For English work, original source size totals 52,429 UTF-8 bytes; rule views with metadata total about 33,828 bytes (35.5% less; source path length slightly affects metadata). This is text volume, not a price or token estimate.

A fresh gpt-6-astra writer executed the same plain-text proof task used in the preceding budget test, without grading answers. It actually invoked both rule readers. Every required nonblank rule line was exposed (Humanizer 181; anti-defensive 129), with no truncated returns. The Statement stayed verbatim; the derivation, almost-everywhere justification and fixed-T scope remained intact. The previous run serves as a historical control, not a new randomized or simultaneous baseline.

| Writer usage | Previous local run | Rule-view first run | Subsequent passage, incremental |
| --- | ---: | ---: | ---: |
| Cumulative input tokens | 291,806 | 217,452 | 131,750 |
| Cached input tokens | 260,480 | 193,408 | 130,176 |
| Uncached input tokens | 31,326 | 24,044 | 1,574 |
| Output tokens | 2,123 | 1,911 | 994 |
| Tool calls | 7 | 6 | 2 |
| Truncated returns | 1 | 0 | 0 |
| Seconds | 71.1 | 71.9 | 31.3 |

The first run's uncached input is 23.2% lower than the historical control, without a measured speed improvement. In the same context, the writer then revised a different, shorter proof of L2-to-L1 convergence on a finite-measure space. It reused guidance without loading it again, performed both language reviews on the new passage, retained the exact Statement and finite-measure explanation, and removed only padding/disclaimer material. The follow-up's cached input still counts as usage; 1,574 is not its total input or a bill. Different task lengths and cache state prevent treating the difference as a controlled cache-effect estimate.

These are two inspected outputs, with maintainer semantic judgments rather than independent certification or reader preference. The subsequent task is not an independent context. Chinese/bilingual behavioral performance, example retrieval on an ambiguous case, unknown-version recovery by an agent, whole-paper performance and stable average savings remain untested. E01–E08 were not rerun. No live paper or remote repository was changed.

Tested entry SHA256: `ee1f047805691947a49ffc961d3698024adfb43bfb5edccb1bbaad999b9d78fb`.

## 2026-11-04 — Same-language example ablation

Two fresh writing contexts processed the same 12 synthetic English paragraphs with identical task and mathematical language interfaces. Arm X read complete English rules and examples; arm Y read the existing exact rule view with illustrative examples deferred. The rubric was saved before execution and hidden from both writers; the maintainer then reviewed both outputs. This is one run per arm, not twelve independent repetitions.

All 12 final paragraph strings were identical between arms. Both retained the scope of fixed-T estimates, finite-measure justification, image/preimage distinction, supported removal of a volume hypothesis, empirical uncertainty, a delayed reminder about zero weights, parameter dependence, arbitrary-solution choice, and subsequence dependence. Both removed the unsupported assumption list, immediate redundant reminders, empty announcements and promotional framing. No optional example reads occurred. All supplied instruction lines were visible in both traces.

English rule text was 41,771 bytes with examples versus 33,074 with reviewed examples deferred (20.8% reduction, excluding identical interfaces and metadata). Observed uncached input was 17,288 versus 13,214; cached input 275,456 versus 187,776; output 1,854 versus 1,880 tokens; elapsed time 84.9 versus 69.4 seconds. X made an unnecessary git-diff attempt outside a repository (exit 129, truncated help output); no instruction text was truncated. These are total observed writer runs, not a clean cost estimate attributable solely to examples; parent evaluation costs are excluded.

Decision: retain the current runtime reader and interfaces unchanged; keep rule-bearing examples and on-demand access to original illustrations. The test supplies no observed benefit from preloading all illustrations on these short, explicitly contextualized tasks. It does not establish long-paper quality, Chinese performance, human preference, equivalence, or that examples never help. No additional mandatory examples were added merely to increase guidance.

Artifacts: local `release/tests/paper/writing/coverage-cost/example-ablation/` contains predeclared input/rubric, source checks, instruction packets, both outputs and `evaluation.json` with trace hashes and per-case maintainer judgments. Source/output excerpts are in the release repository's `tests/writing-quality.md`.
