# Math Paper Skills

[简体中文](README.md) | **English**

Two AI skills for mathematical research: **understand a paper's proofs and explain your own mathematics clearly.**

| Skill | What it does | Entry point |
| --- | --- | --- |
| `math-paper-writing` | Draft, revise and review mathematical manuscripts; maintain bilingual consistency; distill reusable writing methods from papers | [Instructions](math-paper-writing/SKILL.md) |
| `math-paper-study-guide` | Explain difficult proof steps, work through calculations at the reader's level, and produce a whole-paper study PDF with editable source | [Instructions](math-paper-study-guide/SKILL.md) |

## Installation

With Codex's built-in skill installer, ask:

```text
Install these two skills from the GitHub repository coker412/math-paper-skills:
math-paper-writing
math-paper-study-guide
```

Alternatively, clone the repository and place the skill folders you need in `~/.codex/skills/`, or in the `skills/` directory under `CODEX_HOME` if it is set. Compare local modifications before replacing an existing folder. Each skill can be installed independently. Other tools supporting `SKILL.md` can import the folders using their own installation procedure.

```bash
git clone https://github.com/coker412/math-paper-skills.git
```

Ordinary explanations and revisions do not require LaTeX. Study PDFs require XeLaTeX, ctex, AMS packages and Fandol fonts; latexmk is recommended. If the build environment is unavailable, the skill should retain the editable source and state that PDF delivery is pending.

## Optional file tools

Both skills include the following two tools and can be installed independently. Run these commands from the relevant skill directory:

```bash
python scripts/pdf_pages.py /path/to/paper.pdf --cache /path/to/reading/pages.json
python scripts/pdf_pages.py /path/to/paper.pdf --cache /path/to/reading/pages.json --find "Proposition 2.1"
python scripts/pdf_pages.py /path/to/paper.pdf --cache /path/to/reading/pages.json --pages 3-5
python scripts/check_tex_log.py /path/to/_build/main.log /path/to/_build/main.blg
```

The PDF tool requires PyMuPDF in the Python environment for initial extraction. Its cache is bound to the source PDF's SHA-256 and is refreshed when the source changes. By default it returns an index, including the page count; selecting pages returns their complete extracted text. Use `--pages all` for all pages. Reuse existing page-labelled text when available. Empty extraction does not mean the original page is blank: inspect the PDF or use OCR. Search results cannot replace whole-paper reading.

The log tool uses only the Python standard library and does not wrap the compiler. Supply only existing logs from the relevant build. It reports complete issue counts and, by default, the first three examples per category; adjust this with `--examples`. Exit codes 0, 1 and 2 mean no matching issues, issues found, and unreadable or empty input, respectively. It does not establish that the PDF was rebuilt or that the mathematics is correct. Neither tool calls a model API. They reduce repeated file-processing code and irrelevant output; their end-to-end token savings have not been measured.

## See actual examples

Writing evaluation first checks mathematical fidelity, then compares organization, explanation, usability and language. Shorter is not automatically better. The [development tests](tests/writing-quality.md) retain examples of both revision and justified retention; they are not human-reader validation.

Start with the [public examples](examples/README.md), particularly the [six revision comparisons](examples/04-selected-revisions.md) selected from sixteen local trials. They include full Chinese translations of the source passages, English revisions and notes on preserved information. Other examples discuss abstract and proof-overview tradeoffs and explain Hessian positive definiteness. All use OpenAI's public manuscripts and identify pinned source locations.

## Usage

**Revise a paper while preserving its mathematics and accepted author decisions:**

```text
Use $math-paper-writing to revise this introduction.
Preserve all assumptions, notation, conclusions and the approved abstract.
Make the purpose of the auxiliary construction clearer and explain the changes.
```

**Understand one step:**

```text
Use $math-paper-study-guide to explain why the limit and integral can be
interchanged here. I know calculus and linear algebra. Work through the
conditions and calculations actually used. Answer in English in this
conversation; do not create files.
```

**Study a whole paper:**

```text
Use $math-paper-study-guide to produce an English study PDF and editable
source for this complete paper. Start with the precise problem and main
result, then explain the proof's dependencies and decisive calculations.
Identify gaps in the source instead of silently filling them.
```

Study guides default to Chinese unless another language is requested. An English guide uses the same teaching standard; it does not assume a more advanced reader.

## Writing DNA: learn writing methods from papers

The writing skill bundles the [original Writing DNA runtime](math-paper-writing/assets/writing-dna-skill/SKILL.md), its English workflow, Chinese and English templates, and the cleanup skill it references, with pinned provenance and licenses. Mathematical distillation directly invokes the original `writing-dna-skill`; its entry point adds only a link to the [mathematical adaptation](math-paper-writing/references/style-distillation.md). No separate distillation plugin is required. Ordinary manuscript revisions do not load the whole distillation corpus.

The adaptation preserves mathematical conditions, notation and proof status. It supports explicitly chosen smaller samples and does not present a style-similarity target as a measured score.

- **Standard mode: at least 20 complete, distinct works and five analysis documents.**
- **An explicitly chosen small-sample mode supports three or more works**, producing a provisional profile. One or two works support local analysis.
- Revisions, translations and separate sections of one paper do not increase the work count. Coauthorship and related series are recorded.
- Analyze your preferred final drafts or compare before/after versions. Keep private material in your own working directory.

```text
Use $writing-dna-skill for standard Writing DNA distillation of this
mathematical author, and read the bundled mathematical adaptation.
Collect at least 20 relevant complete works. Record titles, versions and
evidence pages; analyze recurring choices and counterexamples, and produce
five reports. Do not substitute a small-sample profile for this request.
```

### Five optional author profiles

| Author | Coverage of the selected corpus | Training works | Reports |
| --- | --- | ---: | ---: |
| [Tao](math-paper-writing/references/profile-tao.md) | Across PDE, geometry, combinatorics, number theory and other fields | 20 | 5 |
| [Evans](math-paper-writing/references/profile-evans.md) | Nonlinear PDE and variational methods | 20 | 5 |
| [Stanley](math-paper-writing/references/profile-stanley.md) | Enumerative and algebraic combinatorics | 20 | 5 |
| [Mumford](math-paper-writing/references/profile-mumford.md) | Classical algebraic geometry | 20 | 5 |
| [Milnor](math-paper-writing/references/profile-milnor.md) | Classical differential geometry and geometric topology | 20 | 5 |

Each profile includes `language-dna.md`, `structure-patterns.md`, `cognitive-framework.md`, `visual-style-guide.md` and `Writing-DNA.md`. The structure reports record all sources, authors, dates, structural analysis and inspected pages. The 100 works include explicitly labelled research notes, surveys and research communications; they are not a uniform set of full-length journal articles. Evans, Stanley, Mumford and Milnor each have an early comparison work outside the twenty-work training corpus. Tao has no reserved unread test work: its corpus contains eighteen research papers or notes and two surveys, emphasizing cross-field exposition and proof organization.

The profiles describe sourced writing choices with conditions for use. A local revision loads relevant rules and source passages; writing guided by a complete profile follows its instructions to read all five reports and five matching complete sources. Ordinary revisions need not load every profile. See [scope and method](math-paper-writing/references/field-profiles.md) and the [overview of Tao's cross-field methods](math-paper-writing/references/author-models.md).

## Integration and boundaries

`lieflat-less-ai-tone` is the original Writing DNA bundle's cleanup skill. It changes only expressions matched by its explicit rules and preserves unmatched text and article structure. It overlaps with anti-defensive editing but is a separate tool. It is not an additional default step for ordinary mathematical revision; use it when its specific rules apply.

`anti-defensive-writing` and Humanizer are optional installations. When available, the writing workflow applies anti-defensive review followed by Humanizer review, including body text and proof exposition within the requested scope. Review may retain the original text; it does not require a rewrite or repeated cleanup loops. Remove empty hedging while preserving necessary conditions, counterexamples, unresolved steps and useful explanations. If an add-on is unavailable and its original instructions cannot be accessed, use the writing skill's basic guidance and disclose that the add-on was not loaded.

The writing skill also includes `scripts/read_text.py` and `scripts/language_rules.py`. The first reads exact text slices with source-hash continuity checks. The second preserves original rules for reviewed add-on versions while deferring purely illustrative examples and selecting the manuscript's language. Unknown versions require reading the original source. Both language reviews and mathematical checks still apply. Local trials observed lower reading costs, but do not establish a fixed saving for whole papers.

Full papers are obtained through source links; this repository distributes skills, original analyses and templates. A writing profile does not certify mathematical conclusions, and completing a study guide does not establish that its reader has mastered the material. Assumptions, quantifiers, proof status and accepted author decisions take precedence.

## Testing and license

Checks include structure and links, deduplication and file verification for the 100 training sources, local-use regressions, script tests, and fresh-context execution trials on short passages and an isolated longer manuscript. In a paired comparison of complete and deferred examples, both arms produced identical text for twelve passages; this does not establish equivalent long-paper quality. See [TESTING.md](TESTING.md) for scope, build-environment limits, observed costs and unverified claims. There is no human-reader efficacy validation or complete independent evaluation of every behavior.

Released under the [MIT License](LICENSE). Source notices and original licenses for Writing DNA and anti-defensive-writing are retained in the [writing skill's source notes](math-paper-writing/references/sources.md) and [bundled license directory](math-paper-writing/licenses/). The study skill's teaching design is documented in its [method guide](math-paper-study-guide/references/chinese-study-edition-method.md).
