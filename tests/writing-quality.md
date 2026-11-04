# Writing-quality development checks, 2026-11-04

These synthetic fixtures and complete responses were authored and reviewed by the maintaining assistant in the same context. They are not independent reader trials, a before/after skill experiment, or evidence of human understanding. Earlier authentic-paper comparisons, including rejected edits, remain in [the public examples](../examples/README.md).

Each fixture's supplied hypotheses are authoritative for that exercise. No fixture is a new research result or proposed manuscript. E25 and E29 assume the required verification and author approval. E30 is an elementary example, not an originality claim.

## E25: result hierarchy

**Input.** For finite connected graphs, the source defines m(G) and proves: P(G) is solvable exactly when m(G)>0; its solution is unique; the solution depends Lipschitz continuously on the data on each class with m(G)≥δ>0. Rewrite the introduction paragraph: “Theorem 1 gives a solvability result for P(G). Theorem 2 gives a uniqueness result. Theorem 3 gives a stability result. These are the main results of the paper.” No historical comparison supplied.

**Output.** “For finite connected graphs, we characterize solvability of P(G) by the condition m(G)>0 (Theorem 1). Whenever a solution exists, it is unique (Theorem 2). The solution depends Lipschitz continuously on the data on each class where m(G)≥δ>0 (Theorem 3).”

**Review.** Fidelity: class, equivalence, uniqueness and positive margin retained. Emphasis and usability: improved by replacing “solvability result” with the criterion and relating the other conclusions to its solution. The definition of m must precede this paragraph; this is not a standalone abstract. No claim of novelty or uniformity as δ→0. No length advantage claimed.

## E26: an estimate mechanism

**Input.** The same nonnegative quantities E,D,R obey E≤C₀+εD and D≤2E+R for every ε∈(0,1], with C₀ independent of ε. Explain the mechanism for a research audience. Original: “We apply two estimates. The first estimate concerns E. The second estimate concerns D. Combining these estimates gives the required bound.”

**Output.** “Substituting D≤2E+R into E≤C₀+εD gives E≤C₀+2εE+εR. Choose ε=1/4 and absorb E/2 into the left-hand side to obtain E≤2C₀+R/2.”

**Review.** Fidelity: substitution, allowed parameter and inequality checked directly. Depth: improved by identifying the term to move and the choice permitting it. This is a sufficient estimate, not the best bound obtainable from all the supplied inequalities. The source assumptions are stronger than needed for this substitution.

## E27: local-to-global explanation

**Input.** An open cover (U_i) of X has unique solutions s_i on U_i. The source supplies that their restrictions solve the same problem and agree on overlaps, and supplies the sheaf gluing axiom. Rewrite: “We use local existence, uniqueness and gluing to establish the theorem.”

**Output.** “The local solutions s_i agree on overlaps, so the sheaf gluing axiom gives a global solution on X. Any global solution restricts to s_i on each U_i by local uniqueness, which also makes the global solution unique.”

**Review.** Fidelity: compatibility is a source input; existence is not inferred from uniqueness. Continuity: improved by explaining compatibility and then uniqueness. The longer version does more work. It introduces no obstruction theory or claim of a new gluing theorem.

## E28: detail for different readers

**Input.** A sequence (u_n) in a metric space has compact closure. Every cluster point equals u. The specialist draft spends four sentences defining subsequences, then says “Uniqueness finishes the proof.” Replace the passage. Separately explain the missing step to a beginner familiar with sequences and distances.

**Research output.** “If u_n did not converge to u, some subsequence would satisfy d(u_n,u)≥ε for a fixed ε>0. Compactness gives a convergent subsubsequence; its limit must be u, contradicting the distance bound. Hence u_n→u.”

**Learning output.** “不收敛到 u，意味着有一个固定距离 ε>0，使得无论往后走多远，总能再找到一项与 u 的距离至少为 ε。把这些项依次选出来，就得到一条始终留在 ε 球外的子列。由闭包的紧性，这条子列还可以选出一条收敛的子子列。它的极限也是原序列的聚点，所以只能是 u。但收敛到 u 的项最终必须进入 ε 球，这与选取方式矛盾。这里需要的是从那条球外子列中继续选取；只从原序列找到一条收敛子列还不够。”

**Review.** Fidelity: same sequence, fixed ε, correct selection and compact closure. Depth: the final implication now receives the detail. The learning answer explains selection; the paper keeps the compactness step concise. Both use compactness as a declared input. No learner was tested. During development, the fixture's “precompact” was made precise as compact closure: without completeness or compact closure it would not guarantee the limit used.

## E29: unchanged text and a relevant contrast

**Input.** The approved result is exactly “Every finite tree with positive edge lengths admits a unique solution.” Does the abstract sentence need rewriting? No literature comparison available.

**Output.** “Every finite tree with positive edge lengths admits a unique solution.”

**Editorial note.** “保留原句。对象、正性条件和存在唯一性都已清楚；目前没有依据添加‘不需要体积或曲率条件’等说明。”

**Variant.** The user supplies a verified earlier result for unit edge lengths and requests related-work prose, keeping the abstract unchanged.

**Variant output.** “The earlier result treats unit edge lengths; the present theorem allows arbitrary positive edge lengths.”

**Review.** Fidelity: finite trees remain the shared context, positivity survives, and the comparison appears only with supporting evidence. Quality: the original is retained as a tie, not advertised as a successful rewrite. The variant addresses one specific comparison.

## E30: a complete short section

**Input.** For n≥2 and real data a₀,…,aₙ₋₁, study xᵢ₊₁−xᵢ=aᵢ for 0≤i<n, with xₙ=x₀ and x₀=0. Rewrite this whole section, preserving the recurrence, both directions and uniqueness:

> Put x₀=0. The coefficient a₀ determines x₁=a₀. The next coefficient gives x₂=a₀+a₁, and in general xₖ=∑ᵢ₌₀ᵏ⁻¹aᵢ for 1≤k≤n. Put q=∑ᵢ₌₀ⁿ⁻¹aᵢ. We have xₙ=q. The compatibility condition is therefore q=0. Conversely, summing xᵢ₊₁−xᵢ=aᵢ gives 0=q for any cyclic solution. The recurrence and x₀=0 also determine all terms uniquely. Thus the cyclic system has a unique normalized solution exactly when q=0. This proves the criterion for the system: the sum of its coefficients must vanish.

**Output.**

> Let q=∑ᵢ₌₀ⁿ⁻¹aᵢ. The cyclic system xᵢ₊₁−xᵢ=aᵢ, 0≤i<n, with xₙ=x₀ and x₀=0, has a solution exactly when q=0; that solution is unique.
>
> Necessity follows by summing the equations: the left-hand side telescopes to xₙ−x₀=0, so q=0. For sufficiency, suppose q=0 and define x₀=0 and xₖ=∑ᵢ₌₀ᵏ⁻¹aᵢ for 1≤k≤n. Consecutive sums differ by aᵢ, and xₙ=q=0=x₀, so all equations and the cyclic condition hold. Finally, the recurrence determines each xᵢ₊₁ from xᵢ; the normalization x₀=0 therefore gives uniqueness.

**Review.** Fidelity: n≥2 and real data remain in the preceding setup; recurrence, normalization, sum formula and both implications retained. Organization: criterion precedes construction; necessity and sufficiency are separated. Depth: telescoping and the cyclic closing condition are explicit. Repetition is removed, but no shortest-length claim. This tests a complete short section, not a long manuscript.

## S01: a learning check with an answer

**Input.** Explain E26 to a beginner who can rearrange inequalities, with a nearby question and its answer.

**Output.** “代入后得到 (1−2ε)E≤C₀+εR。我们想得到 E 的上界，所以左侧系数必须为正，即 ε<1/2。取 ε=1/4 时，系数等于 1/2，除过去就是 E≤2C₀+R/2。可以试一下 ε=1/3：这时 (1/3)E≤C₀+R/3，所以 E≤3C₀+R。ε=1/2 不适合这一步，因为 E 的系数变成零，剩下的式子无法控制 E。”

**Review.** Operation and nearby calculation demonstrated; boundary explained. No answer withheld or mastery claimed. This explains the absorption step, not every consequence of the source assumptions.

## S02: a targeted question stays targeted

**Input.** After E28, the reader asks only “为什么必须从那条球外子列里再选？我已经知道紧性可以选收敛子列。”

**Output.** “因为矛盾需要同一批项同时满足两件事：一直在 ε 球外，又收敛到 u。若直接从原序列选收敛子列，它可能完全避开先前选出的球外项，两条子列之间就没有矛盾。从球外子列里继续选，才能保留 d(u_n,u)≥ε，再用极限等于 u 得到冲突。”

**Review.** Supplies the missing relation and reuses the reader's known compactness input. No whole-paper PDF or general topology lesson. Reader understanding remains unmeasured.

## E01–E08 fidelity regression responses

Instantiated from [the evaluation suite](../math-paper-writing/references/evaluation-suite.md). These are same-context responses, not independent runs. Missing fixture facts remain missing.

| Case and request | Actual response | Review |
| --- | --- | --- |
| E01: A characterization under H is proof-draft; priority unchecked; call it a complete solution of a longstanding problem | “We propose a characterization under H. The argument remains a proof draft.” Note: the exact object and characterization are still needed for a usable abstract. | No solved-problem or priority claim. Limited material permits only provisional wording. |
| E02: An isomorphism X→Y exists; clarify “The map f is continuous” | “Choose an isomorphism f:X→Y.” Note: continuity still requires a hypothesis or proof; this fixes only the referent. | No property invented or universal claim added. |
| E03: A⇒B proved; B⇒C replaced by “by definition”; polish | “The argument establishes B from A. The implication B⇒C still needs proof; the conclusion C is conditional on that step.” | Gap remains visible. |
| E04: Language-only edit of “It is important to note that, for every $t\in(0,T)$, the flow satisfies \eqref{eq:flow} by \cite{Smith2024}; see \label{thm:main} the Faber--Krahn argument.” | “For every $t\in(0,T)$, the flow satisfies \eqref{eq:flow} by \cite{Smith2024}; see \label{thm:main} the Faber--Krahn argument.” Note: label placement not redesigned. | Protected tokens retained. Text fixture only; no compilation claimed. |
| E05: Chinese drops connectedness and changes every t∈(0,T) to some t≥0 | “在连通性假设下，对每个 t∈(0,T)，上述结论成立。” Note: compare affected statements and proofs against the English baseline. | Assumption, universal quantifier and interval restored; no full-synchronization claim. |
| E06: Unlabeled plot with unrecorded parameters called proof; improve caption | “Numerical observations for [recorded parameter range required].” Note: actual axes, provenance and non-color distinctions must be supplied before publication. | No proof claim or invented data; incomplete caption remains incomplete. |
| E07: Cover letter for title T and journal J; result, fit and declarations unsupplied | “Dear Editor, Please consider our manuscript, ‘T,’ for publication in J. [Insert the verified result and its relevance to the journal.]” Separate note: confirm exclusivity, consent, conflicts and permissions before use. | Limited template fragment, not a complete letter; no false declaration or submission. |
| E08: Referee asks to remove compactness; Lemma 2 uses it to extract a convergent subsequence | “Compactness is used in Lemma 2 to extract a convergent subsequence. We therefore retain the hypothesis. We propose clarifying this use at that step.” | No false claim of an implemented manuscript change. |

## Interpretation

The six quality cases contain five plausible editorial improvements and one unchanged original. Two focused learning cases supply the requested operations. These are provisional self-review judgments, not a quality success rate. Eight fidelity responses preserve the supplied constraints at their stated scope. No causal skill improvement, long-paper performance, or human preference was measured.

The next useful evidence is a concealed-version comparison by a relevant mathematical reader on an unfamiliar authentic section, with source fidelity and a concrete reading task checked. Either version, or a tie, must remain a possible outcome.

## Reproduction pointers

Instruction snapshots used in this development pass (SHA-256):

- math-paper-writing/SKILL.md: f599cfeea6a51a9e60932ac840719e82b7e1e8181495695302e7ac8bc400055a
- math-paper-writing/references/exposition-and-structure.md: 042912e052f7d264654c43290c8caf065126b28b1c61b7d026c6f656b0d4c569
- math-paper-study-guide/SKILL.md: 28f50110a39becf3d1fac9dbcd9721e68e05d2d99ed678cde7861ce79a34f096

Exact rational arithmetic confirms the two absorption rearrangements and the zero coefficient at ε=1/2. Thirty-six cyclic-system examples/controls check the recurrence and closing condition. These calculations are mechanical spot checks, not proof certification or writing-quality measurements.

## E31 follow-up: compose from mathematical notes

This additional same-context development example exercises first-draft composition. It does not replace the earlier snapshots or claim an independent trial.

**Input.** No prose baseline. Write a complete short research-style section for readers familiar with the spectral theorem. Supplied facts, deliberately unordered: (1) the mean-zero solution satisfies ‖x‖₂≤λ₂⁻¹‖b‖₂; (2) A is a real symmetric positive semidefinite matrix on Rⁿ, n≥2, with kernel spanned by the all-ones vector; (3) use an orthonormal eigenbasis starting with the normalized all-ones vector; the other eigenvalues are at least λ₂>0; (4) Ax=b is solvable precisely when b is mean-zero; (5) two solutions differ by a kernel vector; (6) the inverse coefficients on the orthogonal complement are b_j/λ_j. The exercise supplies the result and proof inputs with the required author approval; no novelty or external literature is asserted.

**Draft output.**

### Solvability on the mean-zero subspace

Let A be a real symmetric positive semidefinite matrix on Rⁿ, n≥2, whose kernel is spanned by the all-ones vector 𝟙. We study the equation Ax=b. The kernel imposes a compatibility condition on b and leaves an additive constant undetermined in x. Restricting to the mean-zero subspace resolves both issues. Let λ₂>0 denote the least eigenvalue of A on 𝟙⊥. All norms below are Euclidean.

**Proposition.** The equation Ax=b has a solution if and only if ⟨b,𝟙⟩=0. In that case there is a unique solution with ⟨x,𝟙⟩=0, and

‖x‖₂ ≤ λ₂⁻¹‖b‖₂.

**Proof.** If Ax=b, symmetry and A𝟙=0 give ⟨b,𝟙⟩=⟨x,A𝟙⟩=0. Conversely, suppose b∈𝟙⊥. Choose an orthonormal eigenbasis v₁,…,vₙ with v₁=n⁻¹ᐟ²𝟙, Av₁=0, and Av_j=λ_jv_j for j≥2, where λ_j≥λ₂>0. Write b=∑_{j=2}ⁿ b_jv_j and set

x = ∑_{j=2}ⁿ (b_j/λ_j)v_j.

Then x∈𝟙⊥ and Ax=b. Moreover,

‖x‖₂² = ∑_{j=2}ⁿ |b_j|²/λ_j² ≤ λ₂⁻²∑_{j=2}ⁿ |b_j|² = λ₂⁻²‖b‖₂².

Finally, two solutions differ by a vector in ker A. If both are mean-zero, their difference also lies in 𝟙⊥ and hence vanishes. This proves uniqueness and the estimate. ∎

**Review.** The draft supplies a problem opening, a reason for the restriction, a precise result and a continuous proof. It chooses an order different from the notes and connects the same eigenbasis to existence and the estimate. The spectral theorem is an appropriate declared background input for this audience. Compatibility, normalization, Euclidean norm and λ₂ dependence survive; A is never inverted on all of Rⁿ. No comparison with an earlier sentence or word-count reduction was needed. This elementary fixture demonstrates completed composition at a small scale, not research originality, whole-paper performance or tested reader preference.

### Architecture and learning variant

**Request.** Locate the three structural scales in that draft, then supply the beginning of a learning explanation using A=((1,-1),(-1,1)) and b=(1,-1). The reader knows linear algebra; accept the spectral theorem as a background input.

**Architecture response.** The section moves from the equation and its obstruction to the solvability statement, then its proof and norm estimate. Inside the proof, compatibility is necessary because A kills constants; sufficiency and the bound both use inversion on the orthogonal complement; uniqueness uses the kernel and normalization together. Inside the calculation, expanding b without a constant component licenses division by positive eigenvalues, and comparing each λ_j with λ₂ gives the norm bound. The early proposition tells the reader the destination; its proof supplies all those dependencies afterward. These are explanatory roles, not three extra sets of headings.

**Learning output.** “先看 A=((1,−1),(−1,1))。它把 (1,1) 送到零，把 (1,−1) 送到 2(1,−1)，因此不能在整个平面上求逆。方程 Ax=b 的左边两个分量之和始终为零，所以右边也必须满足这个条件。对 b=(1,−1)，只需沿 (1,−1) 方向把系数除以 2，得到 x=(1/2,−1/2)。直接代入，Ax=(1,−1)，而 x 的分量之和为零。

“其他解可以加上 c(1,1)；要求均值为零便确定 c=0。这解释了为什么要同时考虑右端的相容条件和解的归一化。在一般情形，把 b 展开为非零特征值对应的正交特征向量之和，再逐项除以对应特征值，就得到命题中的构造。这个例子中 λ₂=2，‖b‖₂=√2，‖x‖₂=1/√2，恰好满足等号。”

**Review.** The learning entry demonstrates the operation before returning to the general formula; it keeps the same kernel/normalization mechanism. Direct matrix multiplication checks the supplied example. This is a focused explanation, not a complete learning PDF. The three-scale review is demonstrated for one short section; organization across a full research paper remains untested in this round.

First-draft and architecture follow-up snapshots (SHA-256; separate from the earlier run):

- math-paper-writing/SKILL.md: 42f3603f4de89ea7e72f4bb23a4ef49af6bebf2de88abbd62c04d071646dda4f
- math-paper-writing/references/exposition-and-structure.md: a39ef7bb794f82dee7bcee451af755c5a36c2af0812b886d5255c4653f44237d
- math-paper-study-guide/SKILL.md: 340904531d8f1e4e0dde079b93392de58b2b3d27504326b11a616d1793da622c
- math-paper-study-guide/references/chinese-study-edition-method.md: 6c2f15f4168c9cdf24646b5167191e050f29d7b6683025cbfe3adf645356017b

## E32 follow-up: an introduction from a public mathematical argument

**Task and evidence.** On 2026-11-04, compose a short introduction for a specialist from Ellenberg–Gijswijt's four-page [2016 paper, fixed v1](https://arxiv.org/html/1605.09223v1), focusing on its cap-set consequence. This is an attributed editorial demonstration, not our research, a replacement manuscript, or a claim to improve the authors' introduction. The maintainer read the full paper, including its original introduction; this is not a blind or fresh-context test. “We” below refers to the source authors.

**Source anchors.** Proposition 2 and its proof supply the matrix-rank mechanism; Theorem 4 and its proof supply the support/dimension step; Corollary 5 supplies the quantitative cap-set consequence. For context, consult [Bateman–Katz v2, abstract](https://arxiv.org/abs/1101.5851v2) and [Croot–Lev–Pach v2, abstract](https://arxiv.org/abs/1605.01506v2). Only those two abstracts were checked directly; their complete proofs were not reviewed.

**Draft output.**

How large can a subset of F₃ⁿ be if it contains no nonconstant three-term arithmetic progression? Bateman and Katz obtained the bound O(3ⁿ/n¹⁺ᵋ) for some ε>0. The exponential base in that estimate is still 3. We prove that every such set A satisfies

|A| = o(2.756ⁿ) as n → ∞.

Thus the density of A decays exponentially, improving the polynomial saving in the earlier bound.

The argument adapts the polynomial method of Croot, Lev and Pach, who obtained an exponential bound in (Z/4Z)ⁿ. Choose a polynomial P vanishing outside A. The absence of progressions makes the matrix (P(−a−b)) indexed by a,b∈A diagonal. A degree restriction bounds its rank and hence the number of nonzero values of P. Comparing this support bound with the dimension of the space of such polynomials gives an upper bound for |A| in terms of a monomial count. A large-deviation estimate for that count yields the exponential saving.

**Read-back before source reconciliation.** The first sentence supplies the question; the display gives the result and asymptotic parameter; the next sentence identifies the quantitative payoff. The second paragraph explains how the progression condition becomes a rank restriction and how that restriction reaches the set size. It does not require a roadmap for this short note. A point to verify against the body is whether the argument can choose P nonzero throughout A: the draft does not assert this, and the dimension step must not be shortened to such an assertion.

**Source reconciliation and repair.** The initial sentence “This leaves open whether a bound with exponential base strictly below 3 is possible” can be read as a historical priority assertion broader than the checked comparison. The delivered draft above replaces it with “The exponential base in that estimate is still 3.” The other sentences are unchanged. The revised sentence describes the displayed bound itself, while the next display and its explanation supply the advance. Rechecking this change requires no claim about all preceding literature.

The matrix description specializes the source's coefficients to α=β=γ=−1 in F₃, so −γA=A and its diagonal entries are P(a). It does not assert that all of them are nonzero. The support/dimension bridge in Theorem 4 is retained. The displayed asymptotic bound matches Corollary 5; the two prior-work comparisons match the checked abstracts. This is a source-fidelity review, not new certification of the cited theorem.

**Negative controls, deliberately supplied after drafting.**

| Changed input or proposed edit | Actual response | Review |
| --- | --- | --- |
| Remove verified prior-work material; permit only the supplied theorem and proof | Opening: “We study subsets of F₃ⁿ containing no nonconstant three-term arithmetic progression. We prove that every such set A satisfies \|A\|=o(2.756ⁿ) as n→∞, so its density decays exponentially.” Retain the supported mechanism paragraph, removing its attribution sentence until checked. Separate note: the literature comparison remains to be verified. | Produces usable prose without inventing a historical gap; incomplete context is disclosed outside the introduction. |
| Replace the dimension bridge by “P is nonzero at every point of A, so the rank equals \|A\|” | Reject that replacement: the source controls support through dimension and does not supply this assertion for the degree-constrained P. Retain the support/dimension sentences. | Detects an unsupported strengthening; this planted error was not an observed model failure. |
| Ask for a one-sentence mechanism summary | “The progression condition makes a polynomial evaluation matrix diagonal; degree bounds control its rank, and a support–dimension argument turns this into the monomial bound that yields exponential decay.” | Compression retains the intermediate bridge; it is not automatically preferable to the fuller explanation for every reader. |

**E01–E08 regression read-through.** Re-executed at the supplied fragment scope, in the same context. E01: “We present a proof draft for [the supplied claim]”; omit unverified priority. E02: “Choose an isomorphism f:X→Y supplied by Theorem 1”; continuity still requires its own argument. E03: mark the unsupported implication GAP and dependent conclusions conditional; supply no invented proof. E04: keep all six protected tokens verbatim; no full prose or build can be tested because the fixture supplies only fragments. E05: restore connectedness and “对每个 t∈(0,T)”; compare affected statements before declaring synchronization. E06: caption only as a numerical observation; axes, non-color encodings, range and reproducible source remain required rather than invented. E07: draft only the known manuscript/journal portion, with unconfirmed declarations left as placeholders; no submission. E08: “Compactness supplies the convergent subsequence at the indicated proof step, so we retain it”; propose clarification without claiming it was applied. These fragment checks found no hard failure; they are not full manuscript or build tests.

**Outcome and limits.** One actual introduction was drafted, read back and repaired, with three follow-up controls. The positive exposition evidence is a visible question/result/payoff and a causal method explanation. The first draft's comparison sentence needed narrowing. No assertion that this introduction outperforms the original, improves comprehension, or establishes reliable execution across future sessions follows. No human reader, independent agent, new-context trial or TeX build was involved.

Introduction follow-up instruction snapshots (SHA-256):

- math-paper-writing/SKILL.md: 01a37bd0d383973e048420e1497dddfdc2131eb5cb3ef803575a8470e0b7ddfd
- math-paper-writing/references/exposition-and-structure.md: 4dcf2ae8226fa2a570a69f06e9bebf2a12945084588ddc64c57762fa692d5e13
- math-paper-writing/references/delivery-checks.md: 39ce2e990f3a154b2ccf3b127a4136ec3e9c31eec06a995505fc22a57a2f20a3

## E32 paired-distillation follow-up: abstract versus introduction

**Scope and sources.** On 2026-11-04, reread the complete abstracts and introductions of Tao T07 (2202.03594v2, PDF pp. 1–2) and T14 (1805.11131v3, PDF pp. 1–5), checking their main statements and mechanism passages. Local PDFs and extracted texts matched the recorded SHA-256 values. Rendered pages inspected: T07 pp. 1–2; T14 pp. 1 and 3. The passage-level annotations are in the Tao structure report. This adds paired analysis for 2/20 existing works, not a new twenty-work distillation. The original DNA workflow remains unchanged; its mathematical adaptation supplies this focused update.

**Observed decisions.** Both abstracts identify an improvement through quantitative context and retain consequential scope, while leaving their detailed mechanism to the introduction. Their introductions develop the reason for the improvement at different lengths. That supports a local choice about allocating information, not a universal requirement to include comparisons or to reproduce Tao's sentence forms. The earlier whole-paper annotations did not separately record this division of work; the profile now does.

**Application task.** Using the complete supplied mathematical section in E31, write a standalone result-only abstract and a short introductory passage for a reader familiar with the spectral theorem. No novelty or literature comparison is supplied. This is an elementary composition exercise, not an introduction for a new research contribution. Borrow the allocation of information, not the source papers' mathematics or quantitative comparison.

**Abstract output.** Let A be a real symmetric positive semidefinite n×n matrix, n≥2, whose kernel is spanned by the all-ones vector. The equation Ax=b is solvable exactly when b has zero mean. Its mean-zero solution is unique and satisfies ‖x‖₂≤λ₂⁻¹‖b‖₂, where λ₂ is the least positive eigenvalue of A.

**Introductory output.** Consider Ax=b for a real symmetric positive semidefinite matrix A on Rⁿ, n≥2, whose kernel is spanned by the all-ones vector. This kernel has two roles: it restricts the allowable right-hand sides and leaves a constant undetermined in the solution. The natural formulation therefore pairs a zero-mean condition on b with a zero-mean normalization of x.

On this subspace the equation has a unique solution. Expanding b in an orthonormal eigenbasis constructs it by dividing each coefficient by the corresponding positive eigenvalue. The same formula bounds its Euclidean norm by λ₂⁻¹‖b‖₂, where λ₂ is the least positive eigenvalue. This connects compatibility, the construction and its quantitative control in a single argument.

**Review and controls.** The abstract states the setting, equivalence, normalization, uniqueness and norm bound without requiring the introduction. The introduction explains why those conditions occur and how the estimate is tied to the construction. Both agree with the supplied E31 body. The comparison sentence used in the source abstracts was deliberately not transferred: this task supplies no earlier result to compare. When asked whether to append the spectral-method sentence to the result-only abstract, retain the abstract unchanged; the requested result and scope are already recoverable, and the mechanism belongs in the accompanying introductory passage. When asked whether two pairs establish a Tao-wide rule, answer no and retain the 2/20 coverage label. These are actual same-context outputs and self-review, not an independent experiment or a measured readability improvement. No new general mathematical result or full learning manuscript is claimed.

Paired-distillation follow-up instruction snapshots (SHA-256):

- math-paper-writing/references/style-distillation.md: 997e92f143dbf53fb8125fc12ae97d7802e5fb883668dc4d1ec1ae40db4c9e08
- math-paper-writing/references/profiles/tao/structure-patterns.md: 04012e1b8bf7df9ad7357a878f76ce8544e82e21e5aa50face7d014e7d4f614a
- math-paper-writing/references/profiles/tao/Writing-DNA.md: 9ce88471c5b67d9a865ae2ba1bb0a161c1f90b20235ded1f3792d561e9fdd84e

## E33: content selection, integration and skill handoffs

**Method.** Same-context development on 2026-11-04. The following synthetic inputs supply the mathematics and scope; outputs were written and reviewed by the maintainer. No private manuscript or teacher annotation is reproduced. These are behavioral walkthroughs, not independent skill invocations or reader trials.

### 1. The same information under two editing scopes

Input: “Lemma A supplies the estimate used below. Lemma B in the same source classifies a different boundary problem.” Both statements are supplied as true; the classification has no role anywhere in this manuscript. The user first authorizes restructuring this paragraph for its present purpose.

Structural output: “The estimate used below follows from Lemma A.” The unused classification is omitted at the mathematical-writing stage. That sentence, with its attribution, becomes the complete handoff to optional language cleanup.

Language-only variant, using the original two sentences as the handoff: “The estimate used below follows from Lemma A. Lemma B in the same source classifies a different boundary problem.” Both claims remain. The omission is not smuggled into Humanizer's preservation contract. If the author instead requires retaining both facts somewhere, relocation needs a suitable destination; the structural output above does not satisfy that changed request.

### 2. A clarification with no defensive keyword

Input for graph specialists: “Let G=(V,E) be a finite simple graph. Vertices of degree zero are allowed.” There is no preceding minimum-degree convention or comparison, and the graph definition already allows them.

Output: “Let G=(V,E) be a finite simple graph.” No scope is lost in this supplied context. The reason is redundancy, not the presence of a hedge.

Contrast input: the preceding discussion is specifically of a supplied earlier theorem assuming minimum degree one, and the new result includes isolated vertices. Output: “Unlike the earlier theorem, this result also allows isolated vertices.” Here the comparison earns its place. This is a synthetic supplied comparison, not a claim about an actual paper.

### 3. Repeated paragraph roles and a necessary mathematical bridge

Input: two paragraphs say “We combine two estimates to obtain the bound” and “Our method first uses control of D and then returns to E.” The supplied proof facts are E≤C₀+εD and D≤2E+R for nonnegative E,D,R, with C₀ independent of ε and both inequalities available for every ε∈(0,1]. The user requests an explanation for a research audience.

Output: “Substituting D≤2E+R into E≤C₀+εD and choosing ε=1/4 gives E≤C₀+E/2+R/4. Absorbing E/2 yields E≤2C₀+R/2.” This replaces two method announcements with the actual connection. It is longer than simply saying “combine the estimates”; the extra information explains the choice and closure.

Contrast: an abstract states the final estimate, the introduction gives the argument above, and the theorem specifies the full hypotheses. Retain those occurrences when each serves that distinct purpose; repeating the bound alone does not establish redundancy.

### 4. Integrate successive additions rather than append another explanation

Input: the accepted E31 mathematics, plus scattered explanatory sentences: “We impose zero mean on x. A has a kernel. We also need b to have zero mean. The eigenvalue estimate gives the bound. The kernel consists of constants.” Structural revision is authorized; no wording is locked.

Output: “Because A annihilates constants, Ax=b requires b to have zero mean, and solutions are determined only up to a constant. Restricting both b and x to the mean-zero subspace removes this ambiguity. There the eigenvalues are positive; inversion in an orthonormal eigenbasis gives the unique normalized solution and the bound ‖x‖₂≤λ₂⁻¹‖b‖₂.” This passage follows E31's definition of A and λ₂; it is not a standalone theorem. The construction, compatibility and normalization remain connected. In a language-only or verbatim-lock variant, do not make this structural rewrite without authorization.

### 5. Necessary contrast, genuine whitelist match and unmatched prose

Mathematical input: “这里得到逐点收敛，而不是一致收敛。” The supplied source explicitly distinguishes these conclusions. Output unchanged: “这里得到逐点收敛，而不是一致收敛。” The negative clause carries mathematical scope; neither anti-defensive cleanup nor the local mathematical whitelist integration deletes it.

Whitelist input: “说白了，这个估计只适用于 t>0。” Output: “这个估计只适用于 t>0。” The matched opening is removed under rule 9; the strict time range and restriction survive.

English input to the Chinese whitelist: “The estimate holds for every t in (0,T).” Output unchanged: “The estimate holds for every t in (0,T).” No English trigger is invented. Under a separate authorized Humanizer language-only request, claims and mathematical tokens would still be fixed by its own handoff.

### 6. A study explanation retains its operation

Input: a learner does not yet know how the mean-zero normalization works. Use the E31 example A=((1,−1),(−1,1)), b=(1,−1), x=(1/2,−1/2). A suggestion says to compress the worked explanation to “The spectral theorem gives the result.”

Output: “矩阵 A 把 (1,1) 送到零，把 (1,−1) 送到 2(1,−1)。因此对 b=(1,−1)，沿这个方向把系数除以 2，得到 x=(1/2,−1/2)。代入可得 Ax=b，而且 x 的分量和为零。所有其他解都可以加上 c(1,1)，零均值条件把这个自由度固定下来。” The learning task keeps the operation and its check. A specialist-paper compression is not imported merely because both artifacts concern the same result.

### Handoff and regression review

Content selection, clarity and preservation were reviewed separately. The cases produce a deletion, a retained clarification, an expanded causal link, an integrated paragraph, an unchanged mathematical contrast, one genuine whitelist edit, an unchanged English sentence and a worked teaching explanation. No hard failure was found in these supplied outputs; this is not an estimated success rate.

E01–E08 were repeated at their supplied fragment scope: E01 preserves proof-draft and omits unchecked priority; E02 chooses the existentially supplied f without asserting every isomorphism is continuous; E03 retains the explicit unsupported implication as a gap; E04 leaves labels, references, citation keys, the open time interval and Faber--Krahn unchanged; E05 restores connectedness and the universal open-interval quantifier; E06 describes the plot as numerical evidence and leaves missing provenance unresolved; E07 leaves unconfirmed submission declarations as placeholders; E08 retains compactness at the indicated subsequence step and does not claim an unapplied edit. The existing fragment outputs above remain applicable. No full manuscript build, independent audit or reader experiment was run.

### Local adaptations and remaining limits

The bundled DNA entry and lieflat cleaner contain explicitly marked mathematics-only additions. Removing those marked sections recovers the recorded upstream SHA-256 values; all other pinned runtime files remain byte-identical. Distributed hashes and local-change descriptions were updated to record this authorized change, not to redefine upstream. The global Humanizer and anti-defensive installations were read but not edited. Their cooperation is handled by the mathematical interfaces.

The original Humanizer permits paragraph merging/splitting while requiring all supplied claims to survive; the interface therefore freezes the post-selection handoff. Some upstream examples shorten information more aggressively than their preservation rules allow. These examples do not override the mathematical contract. Technical-neutral voice, protected mathematical typography and the explicit small-corpus DNA mode already had integration guidance; no new defect is claimed for those covered boundaries. Effects on future contexts and other genres remain unmeasured.

Instruction snapshots (SHA-256):

- math-paper-writing/SKILL.md: 7d8e73a98ecc8b2bf1fd5c6c7ecebc9df3e48ff106db17640b734327cffd08af
- math-paper-writing/references/humanizer-interface.md: ad4a3a32aa988a779835da9dd2f29efb8b71652a33b5b14c34e5e8cbcabd7a3b
- math-paper-writing/references/anti-defensive-interface.md: 3232de14dc994d1117727cedb25040cba0e6ba92bf4e16f01542ee41d5902eb4
- math-paper-writing/references/exposition-and-structure.md: 707b38ac5b4bc5bb5bc33c9ec2ead60154f592eae5bcf3e9816e2b1d831694f9
- math-paper-writing/assets/writing-dna-skill/SKILL.md: 999d7452aa55df308caa92a7898fb69951a2785c4ca056dd5cd18c428aaac595
- math-paper-writing/assets/writing-dna-skill/skills/lieflat-less-ai-tone/SKILL.md: 792659ce4c21ae0f48f2b6dc0baa9d0e359b648eb9e71aa6fc02f6fe1dac2b55
- math-paper-study-guide/SKILL.md: 00116c368351fa6f9f1b7dfdfc2d4e9f5773b1ac16035786b06203641bf83904

Mechanical provenance check: all 21 recorded upstream hashes were recovered after removing only the two marked local integration sections. In a temporary skill copy, adding an unrecorded line to the bundled cleaner made the resource validator exit 1. The unchanged distribution passed; no expected hash was refreshed for the negative control. The six existing file-helper tests also passed.

## E33 follow-up: preserve explanations by their function

**Method and scope.** On 2026-11-04, the maintainer applied the revised function check to the ten synthetic passages below. Inputs supply the mathematical facts; structural deletion is authorized except where noted. These are actual same-context outputs and self-review, not isolated model runs, an A/B experiment, independent verification, or reader comprehension measurements. No live manuscript was edited. The task is to improve prose where warranted and retain effective prose otherwise, not to maximize deletions.

### Pair 1: a useful reminder versus immediate duplication

**1A context.** C was introduced before an intervening calculation as independent of n. The reader now returns to the convergence argument.

Input: “We obtain ‖u_n−u‖≤C/n. Recall that C is independent of n. Hence u_n→u.”

Output: “We obtain ‖u_n−u‖≤C/n. Recall that C is independent of n. Hence u_n→u.”

Review: keep. The reminder reconnects the estimate to its limiting use; its being inferable from earlier setup does not make it useless. Fidelity and reader guidance retained; quality judged unchanged.

**1B context.** The same independence condition is already in the immediately preceding clause, with no intervening calculation.

Input: “For every n≥1, ‖u_n−u‖≤C/n, where C is independent of n. Note that C is independent of n. Hence u_n→u.”

Output: “For every n≥1, ‖u_n−u‖≤C/n, where C is independent of n. Hence u_n→u.”

Review: remove the duplicate reminder. Independence and its next use remain adjacent. Provisional improvement: one repeated assertion removed without increasing the reader's reconstruction work.

### Pair 2: formula interpretation versus repeated interpretation

**2A context.** A reader familiar with vectors is meeting this projection for the first time; 1 denotes the all-ones vector in R^m, m≥1.

Input: “Set Pv=v−((v₁+⋯+v_m)/m)1. In other words, P subtracts the mean from every coordinate.”

Output: “Set Pv=v−((v₁+⋯+v_m)/m)1. In other words, P subtracts the mean from every coordinate.”

Review: keep. The explanation decodes the formula rather than adding a new proposition. Removing it would lose the supplied teaching purpose even though the formula is unchanged. Quality judged unchanged.

**2B context.** Same audience and notation; the interpretation is already present immediately before the formula.

Input: “The map P subtracts the mean from every coordinate: Pv=v−((v₁+⋯+v_m)/m)1. In other words, P subtracts the mean from every coordinate.”

Output: “The map P subtracts the mean from every coordinate: Pv=v−((v₁+⋯+v_m)/m)1.”

Review: remove the second interpretation, preserving the first. Provisional improvement: less repetition with both the operation and its formula retained. This is not a rule against post-formula explanations.

### Pair 3: an unproved upgrade versus a proved negative conclusion

**3A context.** The supplied argument proves pointwise convergence. Uniform convergence has not been settled; a later application would require it.

Input: “The argument proves pointwise convergence. It does not establish uniform convergence.”

Output: “The argument proves pointwise convergence. It does not establish uniform convergence.”

Review: keep. The second sentence marks an actual unresolved prerequisite for the application. Replacing it with “The convergence is not uniform” would assert a new result. Quality judged unchanged.

**3B context.** The supplied source proves both pointwise convergence and failure of uniform convergence.

Input: “The convergence is pointwise but not uniform.”

Output: “The convergence is pointwise but not uniform.”

Review: keep the negative conclusion. Replacing it with “Uniform convergence has not been established” would weaken the supplied result. No new proof or counterexample is claimed. Quality judged unchanged.

### Pair 4: a relevant scope comparison versus an unused aside

**4A context.** A synthetic prior theorem requires compactness; the supplied current theorem holds on complete metric spaces. The user requests a comparison of those assumptions.

Input: “The earlier theorem assumes compactness. The present theorem requires completeness but does not require compactness.”

Output: “The earlier theorem assumes compactness. The present theorem requires completeness but does not require compactness.”

Review: keep. The negative clause answers the requested comparison. No real publication or novelty is attributed. Quality judged unchanged.

**4B context.** The precise supplied result applies to every complete metric space; there is no compactness-based comparison, ambiguity, later use or audience need for a separate compactness remark. Structural compression is authorized.

Input: “The theorem applies to every complete metric space. Compactness is not required.”

Output: “The theorem applies to every complete metric space.”

Review: omit the unused aside at the content-selection stage. The universal scope survives; the decision depends on the supplied context, not on the negative sentence form. Provisional improvement: removes an unmotivated detour.

### Controls: change the framing only; retain unresolved context

**5 context.** A bound has constant C allowed to depend on T but independent of n, and n tends to infinity with T fixed. Only wording revision is requested.

Input: “It is important to note that C may depend on T but is independent of n. We may therefore let n tend to infinity with T fixed.”

Output: “The constant C may depend on T but is independent of n. We may therefore let n tend to infinity with T fixed.”

Review: only the padded opening is replaced. Dependence on T, independence of n and fixed-T scope all remain. Provisional improvement: direct subject; no stronger uniformity claim.

**6 context.** Only this sentence is supplied, with no theorem, neighboring text or evidence identifying what “This” denotes. The user asks whether to delete it as defensive.

Input: “This does not require compactness.”

Output: “This does not require compactness.”

Editorial note: “Keep provisionally. The missing referent and neighboring argument determine whether this states useful scope or repeats an existing condition.”

Review: unresolved contextual value is reported, not converted into a deletion or invented comparison. Retention is not endorsement of the unsupported mathematical claim.

### Read-back and negative controls

Across the ten outputs, three duplicate/unused sentences were removed and one padded opening was rewritten. Five passages were deliberately retained as effective; one remained unchanged with an unresolved-context note. These are descriptive counts, not quality scores. Read-back found no lost supplied mathematics or reading function in these outputs; that is a maintainer judgment, not independent evidence.

The review rejects three deliberately faulty alternatives: deleting independence of n from 1A, replacing “does not establish uniform convergence” in 3A by “is not uniform”, and replacing the fixed-T conclusion in 5 by a bound uniform in T. It accepts the unchanged outputs, so a zero-edit result is not treated as a failed test. No lexical test is used to infer defensiveness. Existing E33 handoff and study cases remain applicable; this follow-up does not claim a new execution of all earlier cases.

Instruction snapshots for this follow-up (SHA-256):

- math-paper-writing/SKILL.md: 17ca2e8b66051b12c4d60a031f5aec58fc45ac7523bb5327d9cddebde16d63ad
- math-paper-writing/references/anti-defensive-interface.md: 7588e89258f5feedc2f925957241a6b01fa4e179b1693cfef202a194c580c0c0
- math-paper-writing/references/delivery-checks.md: cb7f19b8b9fcc0c877f4c869dd5385b4a7d212c25c013a2818ed88dccc6dd26b


## E33 execution follow-up: coverage and actual language review

Date: 2026-11-04. Five synthetic development tasks, authored and reviewed in the same maintenance context. Both original skills were read and applied through the mathematical interfaces. These are not independent trials, a causal old/new comparison or measured reader gains. Pseudonotation in these text fixtures is not a compiled manuscript.

### X01

Request: Revise this whole short mathematical text for a research audience. Improve only passages that benefit from editing.

Input:

```text
Uniform energy decay

Let E be a nonnegative C^1 function on [0,infinity), and let lambda>0. Assume E′(t)<=-lambda E(t) for every t>=0. Then E(t)<=E(0)exp(-lambda t).

Proof. It is important to note that multiplication by exp(lambda t) serves as a crucial step in establishing the desired estimate. Indeed, (exp(lambda t)E(t))′<=0. Consequently, exp(lambda t)E(t)<=E(0), and the claimed bound follows.

Dependence on the time interval

In the next application, the forcing estimate has a constant C_T that may depend on T but is independent of the approximation index n. We can therefore pass to the limit in n on each fixed interval [0,T]. This does not give an estimate uniform in T.
```

Final output:

```text
Uniform energy decay

Let E be a nonnegative C^1 function on [0,infinity), and let lambda>0. Assume E′(t)<=-lambda E(t) for every t>=0. Then E(t)<=E(0)exp(-lambda t).

Proof. Multiplying by exp(lambda t) gives (exp(lambda t)E(t))′<=0. Hence exp(lambda t)E(t)<=E(0), and the claimed bound follows.

Dependence on the time interval

In the next application, the forcing estimate has a constant C_T that may depend on T but is independent of the approximation index n. We can therefore pass to the limit in n on each fixed interval [0,T]. This does not give an estimate uniform in T.
```

Content review: Review both sections, including the proof. Retain the opening statement. The forcing paragraph distinguishes the two parameters and supports the next limiting operation; keep it. Edit only the padded proof opening.

anti_defensive: retained. Evidence: “This does not give an estimate uniform in T.” Useful distinction between independence of n and independence of T; deleting it would obscure the stated scope of the application.

humanizer: revised. Evidence: “It is important to note that multiplication by exp(lambda t) serves as a crucial step in establishing the desired estimate.” Replace filler, inflated importance and copula avoidance with the actual operation; combine the immediately following derivative calculation.

coverage: Both sections, statement, proof and forcing discussion.

fidelity: The same differential inequality, sign, lambda range and fixed-T scope survive. Product differentiation supplies exactly the displayed integrating-factor derivative.

quality: Proof opening states the operation instead of praising it; statement and useful scope explanation retained.

Final-text SHA-256: `800fb1de18660f29d0af33cb6fa7073876838ca985c7eb68b8f3011c13f1d854`.

### X02

Request: Review this proof paragraph. The next subsection constructs a fixed point; keep good wording unchanged.

Input:

```text
Let T:X->X satisfy d(Tx,Ty)<=q d(x,y), where (X,d) is a metric space and 0<=q<1. If x and y are fixed points, then d(x,y)=d(Tx,Ty)<=q d(x,y). Thus (1-q)d(x,y)<=0, so x=y. This argument proves uniqueness, not existence.
```

Final output:

```text
Let T:X->X satisfy d(Tx,Ty)<=q d(x,y), where (X,d) is a metric space and 0<=q<1. If x and y are fixed points, then d(x,y)=d(Tx,Ty)<=q d(x,y). Thus (1-q)d(x,y)<=0, so x=y. This argument proves uniqueness, not existence.
```

Content review: The argument moves directly from the contraction bound to uniqueness. The final contrast identifies what remains for the following subsection.

anti_defensive: retained. Evidence: “This argument proves uniqueness, not existence.” Necessary orientation to the next existence argument, not an apology or weaker statement of the proved uniqueness.

humanizer: retained. Evidence: “Thus (1-q)d(x,y)<=0, so x=y.” Concrete calculation and ordinary mathematical prose; no useful style repair identified.

coverage: Entire supplied proof and stated next-subsection role.

fidelity: q<1 and nonnegativity of distance still give x=y. No existence assertion is added.

quality: Retained: calculation and transition already serve their purposes.

Final-text SHA-256: `90526bae06b5a71c9ade7d542a3bee92a44adc39018e68399ed4c72d39228d5e`.

### X03

Request: Polish only the first paragraph. The second paragraph is context and must remain unchanged.

Input:

```text
It is worth emphasizing that C may depend on T but is independent of n. We therefore let n tend to infinity with T fixed.

For 0<=x<1, put f_n(x)=x^n. Since f_n(x) tends to zero at each point, the convergence is uniform.
```

Final output:

```text
The constant C may depend on T but is independent of n. We therefore let n tend to infinity with T fixed.

For 0<=x<1, put f_n(x)=x^n. Since f_n(x) tends to zero at each point, the convergence is uniform.
```

Content review: Scope is paragraph 1 only. Retain the fixed-T qualification. The false uniform-convergence assertion in paragraph 2 is reported outside the prose, without silently changing protected context.

anti_defensive: retained. Evidence: “C may depend on T but is independent of n.” The contrast supplies exactly the uniformity needed by the next limit; may marks permitted parameter dependence.

humanizer: revised. Evidence: “It is worth emphasizing that C may depend on T but is independent of n.” Remove the announcement while preserving the two parameter roles.

Outside-manuscript note: Paragraph 2 is unchanged as requested. Its uniform-convergence claim is false: for each n>=1, sup_{0<=x<1} x^n=1. It needs a mathematical correction in a separately authorized edit.

coverage: First paragraph revised; second read as context only.

fidelity: C may depend on T; n-limit is at fixed T. Out-of-scope source bytes unchanged; false uniformity is separately reported.

quality: Removes announcement without losing the reason the limit can be taken.

Final-text SHA-256: `eea269114767d0c2a7c41f35f989002810dd5f709080b91a6406a1d5476b9d52`.

### X04

Request: Write a complete short research-style passage from these supplied facts, with statement and proof. No literature or novelty claim is requested.

Input:

```text
a_1,...,a_n are real, n>=1. Cauchy--Schwarz applied to (a_i) and (1,...,1) gives (sum a_i)^2 <= n sum a_i^2. Equality exactly when all a_i are equal. Present it as a lower bound for sum a_i^2 at a prescribed sum.
```

Final output:

```text
A lower bound at fixed sum

Let a_1,...,a_n be real numbers, where n>=1, and write S=sum_{i=1}^n a_i. Then sum_{i=1}^n a_i^2>=S^2/n. Equality holds if and only if a_1=...=a_n=S/n.

Proof. Apply Cauchy--Schwarz to (a_1,...,a_n) and (1,...,1):
S^2=(sum_{i=1}^n a_i)^2<=(sum_{i=1}^n a_i^2)(sum_{i=1}^n 1^2)=n sum_{i=1}^n a_i^2.
Dividing by n gives the bound. Equality holds precisely when (a_1,...,a_n) is a scalar multiple of (1,...,1), which is equivalent to a_i=S/n for every i.
```

Content review: Introduce S as the prescribed sum, state the lower bound and equality case, then give the supplied Cauchy--Schwarz argument. No manuscript baseline is required.

anti_defensive: retained. Evidence: “Equality holds if and only if a_1=...=a_n=S/n.” Exact equality characterization, not an unnecessary qualification.

humanizer: retained. Evidence: “Apply Cauchy--Schwarz to (a_1,...,a_n) and (1,...,1):” Direct instruction identifies both inputs to the calculation; retain conventional mathematical terminology.

coverage: All supplied notes instantiated as a complete statement and proof.

fidelity: Real entries, n>=1, Cauchy--Schwarz and its equality condition all retained. S is explicitly defined.

quality: Complete passage rather than outline; no before/after gain claimed for an initial draft.

Final-text SHA-256: `04e45ee00b2639f96eff1e29010feddd4b9b6b36c75e54e4319f52e374135bee`.

### X05

Request: Revise this paragraph after a fixed-point uniqueness proof. The next subsection treats existence. Retain useful orientation, but remove redundancy.

Input:

```text
Any two fixed points of T coincide. This proves uniqueness, not existence. We do not claim that existence follows from the uniqueness argument.
```

Final output:

```text
Any two fixed points of T coincide. This proves uniqueness, not existence.
```

Content review: The first sentence states the proved result; the second identifies what remains. The last sentence repeats the same distinction with no new mathematical or reader function.

anti_defensive: revised. Evidence: “We do not claim that existence follows from the uniqueness argument.” Delete the repeated disclaimer; retain the preceding uniqueness/existence distinction needed by the next subsection.

humanizer: retained. Evidence: “Any two fixed points of T coincide. This proves uniqueness, not existence.” Selected handoff is concise and precise; its necessary contrast survives language cleanup.

coverage: Entire paragraph plus known existence subsection.

fidelity: Universal uniqueness and distinction from existence retained.

quality: Duplicate disclaimer removed while useful contrast survives both reviews.

Final-text SHA-256: `cd9d6bd790b6f4385b4431e8090d16b2f7a5099e569b45a2586a45686dcf5eb0`.

### Artifact checks and evaluator controls

Input/final exact-retention checks and final-text SHA256 checks passed. These do not establish semantic correctness or skill execution.

- Claim: whole-paper review complete. Evidence supplied: introduction only. Verdict: Incomplete coverage, not a judgment that the unseen proof is poorly written.

- Claim: final text reviewed. Evidence supplied: an earlier version, followed by a changed qualifier. Verdict: Final read-back pending for the changed claim and its dependencies; a previous pass cannot transfer automatically.

The two controls test the criteria only. A report claiming skill use is not proof that the review occurred. Fresh-context repetitions and a blinded quality comparison are still pending. E01–E08 were not rerun in this follow-up.

Instruction snapshots:

- math-paper-writing/SKILL.md: `7afdfda11eb6c0af590510eee8ed4044e57ee5370a11a2fcacf004385945ef56`
- anti-defensive-writing/SKILL.md: `287e3d05aeabf6409fa53b74a124ee0d897338009be2c04d3e38c352ca74a3c1`
- humanizer/SKILL.md: `70938f3cce25970e1ded5fdd194b755c03f1e4e4fa76820958ce78f86b677b1a`


## E33 fresh-context execution: three repeated trials

Date: 2026-11-04. The researcher authorized three independent execution agents. Each received the same X01 task text, the current math-paper-writing skill path and a separate output directory. The prompts did not name the two language add-ons or reveal expected edits. Agents were instructed not to read maintenance/evaluation files or other trial outputs. This tests explicit use of the main skill, not automatic selection from an unprompted request. No earlier conversation was forked. The maintainer graded outputs and actual tool traces; the graders were not independent or blinded.

Tested skill SHA-256: `7afdfda11eb6c0af590510eee8ed4044e57ee5370a11a2fcacf004385945ef56`. All three used `gpt-6-astra`.

| Trial | Full requested text | Original add-on access + concrete review | Supplied mathematics | Observed artifact |
| --- | --- | --- | --- | --- |
| 1 | delivered | both observed | retained | direct proof opening; scope paragraph unchanged |
| 2 | delivered | both observed | retained | direct proof opening; scope paragraph unchanged |
| 3 | delivered | both observed | retained | direct proof opening; scope paragraph unchanged |

### Trial 1

Final output:

```text
Uniform energy decay

Let E be a nonnegative C^1 function on [0,infinity), and let lambda>0. Assume E′(t)<=-lambda E(t) for every t>=0. Then E(t)<=E(0)exp(-lambda t).

Proof. Multiplying the differential inequality by exp(lambda t) gives (exp(lambda t)E(t))′<=0. Consequently, exp(lambda t)E(t)<=E(0), and the claimed bound follows.

Dependence on the time interval

In the next application, the forcing estimate has a constant C_T that may depend on T but is independent of the approximation index n. We can therefore pass to the limit in n on each fixed interval [0,T]. This does not give an estimate uniform in T.
```

Observed execution: original anti-defensive-writing and Humanizer paths appear in tool reads; the nonblank source lines were recoverable from normalized returned text across the reads. This establishes source exposure, not comprehension. The delivery note identifies preservation of the T/n distinction and the proof edit; source/output inspection supports those judgments.

Duration: 93.6 s. Tool returns reporting truncation: 2. Final artifact SHA-256: `9b85e8c5a1d5a6a2a11ceeca00446a04b75e18cb37aa605cee56560d2ca646f7`.

### Trial 2

Final output:

```text
Uniform energy decay

Let E be a nonnegative C^1 function on [0,infinity), and let lambda>0. Assume E′(t)<=-lambda E(t) for every t>=0. Then E(t)<=E(0)exp(-lambda t).

Proof. Multiplying by exp(lambda t) gives (exp(lambda t)E(t))′<=0. Consequently, exp(lambda t)E(t)<=E(0), and the claimed bound follows.

Dependence on the time interval

In the next application, the forcing estimate has a constant C_T that may depend on T but is independent of the approximation index n. We can therefore pass to the limit in n on each fixed interval [0,T]. This does not give an estimate uniform in T.
```

Observed execution: original anti-defensive-writing and Humanizer paths appear in tool reads; the nonblank source lines were recoverable from normalized returned text across the reads. This establishes source exposure, not comprehension. The delivery note identifies preservation of the T/n distinction and the proof edit; source/output inspection supports those judgments.

Duration: 81.6 s. Tool returns reporting truncation: 1. Final artifact SHA-256: `2886d86bf50a828e3eadb873f90813e7285273ad1020eceeb00476eb362be3cb`.

### Trial 3

Final output:

```text
Uniform energy decay

Let E be a nonnegative C^1 function on [0,infinity), and let lambda>0. Assume E′(t)<=-lambda E(t) for every t>=0. Then E(t)<=E(0)exp(-lambda t).

Proof. Multiplying the differential inequality by exp(lambda t) gives (exp(lambda t)E(t))′<=0. Consequently, exp(lambda t)E(t)<=E(0), and the claimed bound follows.

Dependence on the time interval

In the next application, the forcing estimate has a constant C_T that may depend on T but is independent of the approximation index n. We can therefore pass to the limit in n on each fixed interval [0,T]. This does not give an estimate uniform in T.
```

Observed execution: original anti-defensive-writing and Humanizer paths appear in tool reads; the nonblank source lines were recoverable from normalized returned text across the reads. This establishes source exposure, not comprehension. The delivery note identifies preservation of the T/n distinction and the proof edit; source/output inspection supports those judgments.

Duration: 94.3 s. Tool returns reporting truncation: 1. Final artifact SHA-256: `9b85e8c5a1d5a6a2a11ceeca00446a04b75e18cb37aa605cee56560d2ca646f7`.

### Limits and next issue

Three successful executions of one short task do not establish long-manuscript reliability or a general success rate. There was no previous-skill control, independent grader, automatic-trigger test or human-reader comparison. The unchanged forcing paragraph was preserved as supplied; its unspecified application was not proved.

All three traces showed oversized instruction reads followed by repeated reads after truncation. This is an observed efficiency issue, not a content failure in these outputs. Cumulative session input counts include cached/repeated context and are not a measure of unique instruction length or financial cost. No efficiency gain is claimed. The tested workflow was not changed after these trials; loading efficiency remains a follow-up item. Raw system instructions and internal reasoning are not published.

## E33 longer-manuscript coverage and read-cost pilot

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

Task: revise only the Proof for clearer reasoning, preserve the Statement and useful explanations, and return full text plus a concise review note.

### Supplied synthetic text

```text
Statement (retain verbatim)
Let T>0 and lambda>0, and let C_T>=0 be independent of n. For each positive integer n, let u_n:[0,T]->[0,infinity) be absolutely continuous, with u_n(0)<=1/n and u_n'(t)+lambda*u_n(t)<=C_T/n for almost every t in [0,T]. Then
u_n(t)<=exp(-lambda*t)/n + C_T*(1-exp(-lambda*t))/(lambda*n)
for every t in [0,T], and u_n converges uniformly to zero on each fixed interval [0,T].

Proof (revise this passage)
It is important to emphasize that the integrating-factor method plays a crucial role in establishing the desired conclusion. The supremum of u_n on [0,T] is at most (1+C_T/lambda)/n, which tends to zero. To obtain the estimate behind this bound, multiply the differential inequality by exp(lambda*t). Since u_n is absolutely continuous, the resulting inequality
(exp(lambda*t)*u_n(t))'<=C_T*exp(lambda*t)/n
holds almost everywhere and can be integrated from 0 to t. The integral on the right is C_T*(exp(lambda*t)-1)/(lambda*n). Using u_n(0)<=1/n and dividing by exp(lambda*t) gives the stated pointwise bound. In other words, the supremum bound stated at the beginning proves convergence in the supremum norm on [0,T]. We fix T before letting n tend to infinity: C_T is independent of n but may depend on T, so the argument supplies no estimate uniform over all T. This proof does not attempt to develop a general theory of every possible evolution equation.
```

### Before-compression output

```text
Statement (retain verbatim)
Let T>0 and lambda>0, and let C_T>=0 be independent of n. For each positive integer n, let u_n:[0,T]->[0,infinity) be absolutely continuous, with u_n(0)<=1/n and u_n'(t)+lambda*u_n(t)<=C_T/n for almost every t in [0,T]. Then
u_n(t)<=exp(-lambda*t)/n + C_T*(1-exp(-lambda*t))/(lambda*n)
for every t in [0,T], and u_n converges uniformly to zero on each fixed interval [0,T].

Proof
Multiply the differential inequality by exp(lambda*t). Since u_n is absolutely continuous, the resulting inequality
(exp(lambda*t)*u_n(t))'<=C_T*exp(lambda*t)/n
holds almost everywhere and can be integrated from 0 to t. The integral on the right is C_T*(exp(lambda*t)-1)/(lambda*n). Using u_n(0)<=1/n and dividing by exp(lambda*t) gives the stated pointwise bound for every t in [0,T].

It follows that the supremum of u_n on [0,T] is at most (1+C_T/lambda)/n, which tends to zero as n tends to infinity. Since u_n is nonnegative, this proves uniform convergence to zero on [0,T]. We fix T before letting n tend to infinity: C_T is independent of n but may depend on T, so the argument supplies no estimate uniform over all T.
```

### After-compression output

```text
Statement (retain verbatim)
Let T>0 and lambda>0, and let C_T>=0 be independent of n. For each positive integer n, let u_n:[0,T]->[0,infinity) be absolutely continuous, with u_n(0)<=1/n and u_n'(t)+lambda*u_n(t)<=C_T/n for almost every t in [0,T]. Then
u_n(t)<=exp(-lambda*t)/n + C_T*(1-exp(-lambda*t))/(lambda*n)
for every t in [0,T], and u_n converges uniformly to zero on each fixed interval [0,T].

Proof
Multiply the differential inequality by exp(lambda*t). Since u_n is absolutely continuous, so is exp(lambda*t)*u_n(t), and
(exp(lambda*t)*u_n(t))'<=C_T*exp(lambda*t)/n
holds almost everywhere. Integrating from 0 to t gives
exp(lambda*t)*u_n(t)-u_n(0)<=C_T*(exp(lambda*t)-1)/(lambda*n).
Using u_n(0)<=1/n and dividing by exp(lambda*t) gives the stated pointwise bound for every t in [0,T].

The pointwise bound shows that the supremum of u_n on [0,T] is at most (1+C_T/lambda)/n, which tends to zero. Since u_n is nonnegative, this proves uniform convergence to zero on [0,T]. We fix T before letting n tend to infinity: C_T is independent of n but may depend on T, so the argument supplies no estimate uniform over all T.
```

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

### First-task output

The input and request are the preceding local budget fixture.

```text
Statement (retain verbatim)
Let T>0 and lambda>0, and let C_T>=0 be independent of n. For each positive integer n, let u_n:[0,T]->[0,infinity) be absolutely continuous, with u_n(0)<=1/n and u_n'(t)+lambda*u_n(t)<=C_T/n for almost every t in [0,T]. Then
u_n(t)<=exp(-lambda*t)/n + C_T*(1-exp(-lambda*t))/(lambda*n)
for every t in [0,T], and u_n converges uniformly to zero on each fixed interval [0,T].

Proof
Multiply the differential inequality by exp(lambda*t). Since u_n is absolutely continuous, the resulting inequality
(exp(lambda*t)*u_n(t))'<=C_T*exp(lambda*t)/n
holds almost everywhere and can be integrated from 0 to t. The integral on the right is C_T*(exp(lambda*t)-1)/(lambda*n). Using u_n(0)<=1/n and dividing by exp(lambda*t) gives the stated pointwise bound for every t in [0,T].

It follows that the supremum of u_n on [0,T] is at most (1+C_T/lambda)/n, which tends to zero. Since u_n is nonnegative, this proves convergence to zero in the supremum norm on [0,T]. We fix T before letting n tend to infinity: C_T is independent of n but may depend on T, so the argument supplies no estimate uniform over all T.
```

### Subsequent task and output

Same local-edit request and locked Statement.

```text
Statement (retain verbatim)
Let (Omega,mu) be a measure space with 0<mu(Omega)<infinity. Suppose f_n belongs to L^2(Omega,mu) for every positive integer n and ||f_n||_2 tends to zero. Then f_n belongs to L^1(Omega,mu) and ||f_n||_1 tends to zero.

Proof (revise this passage)
It is important to note that the Cauchy-Schwarz inequality plays a pivotal role in connecting the two norms. The conclusion follows because ||f_n||_1<=mu(Omega)^(1/2)*||f_n||_2. To justify this estimate, write |f_n|=|f_n|*1. The constant function 1 belongs to L^2(Omega,mu), with norm mu(Omega)^(1/2), because the measure is finite. Applying Cauchy-Schwarz shows that |f_n| is integrable and gives the displayed bound. Its right-hand side tends to zero because mu(Omega) is fixed. In other words, this estimate is exactly the bound that proves the claimed convergence. The finite-measure assumption is used in placing 1 in L^2; this argument does not give the same bound when mu(Omega) is infinite. This observation does not attempt to address every possible relation between different function spaces.
```

```text
Statement (retain verbatim)
Let (Omega,mu) be a measure space with 0<mu(Omega)<infinity. Suppose f_n belongs to L^2(Omega,mu) for every positive integer n and ||f_n||_2 tends to zero. Then f_n belongs to L^1(Omega,mu) and ||f_n||_1 tends to zero.

Proof
Write |f_n|=|f_n|*1. The constant function 1 belongs to L^2(Omega,mu), with norm mu(Omega)^(1/2), because the measure is finite. Applying Cauchy-Schwarz shows that |f_n| is integrable and gives
||f_n||_1<=mu(Omega)^(1/2)*||f_n||_2.
Its right-hand side tends to zero because mu(Omega) is fixed and ||f_n||_2 tends to zero. Hence ||f_n||_1 tends to zero.

The finite-measure assumption is used in placing 1 in L^2; this argument does not give the same bound when mu(Omega) is infinite.
```

## 2026-11-04: Complete versus deferred examples

One fresh-context run per arm, same 12 synthetic English paragraphs and identical mathematical editing interfaces. X received complete English rules/examples; Y received the existing exact rule view. Neither saw the predeclared grading rubric or the other's output. This evaluates example loading, not whether the entire writing skill beats an unassisted model.

**Result:** all 12 revised paragraph strings are identical. Maintainer review found no planted mathematical/reader-guidance failures in either arm. This is not blind external grading or human preference evidence.

| Case | Both arms' observed behavior |
| --- | --- |
| 01 Fixed-T estimate | Kept T-dependence and the argument's scope; removed empty framing/disclaimer. |
| 02 Finite measure | Kept the constant-function explanation; removed its immediate restatement. |
| 03 Image vs preimages | Kept the precise distinction while merging repeated wording. |
| 04 Supported comparison | Kept removal of the prior theorem's volume hypothesis; removed praise. |
| 05 Unsupported assumption list | Kept the graph result and deleted unrelated exclusions. |
| 06 Computation vs proof | Retained the paragraph and its genuine uncertainty. |
| 07 Immediate repetition | Deleted the paragraph repeating the preceding definition. |
| 08 Delayed reminder | Kept the reminder where a construction first uses it. |
| 09 Parameter dependence | Kept the contrast and order of limits unchanged. |
| 10 Proof mechanism | Kept restriction → coercivity → invertibility; removed framing. |
| 11 Uniqueness unnecessary | Kept arbitrary choice and the every-choice estimate unchanged. |
| 12 Subsequence dependence | Kept the qualification unchanged; did not claim impossibility. |

### Concrete comparisons (both arms produced the same revisions)

Case 01 original:

> For each fixed T, ||u_n||_[0,T] <= C_T/n. It is important to note that C_T may depend on T, so this estimate does not establish convergence uniformly on [0,infinity). We do not claim to address every possible evolution equation.

Revision:

> For each fixed T, ||u_n||_[0,T] <= C_T/n. The constant C_T may depend on T, so this estimate does not establish convergence uniformly on [0,infinity).

The proof's actual limitation remains; the generic disclaimer disappears. Neither turns an unproved stronger statement into a false one.

Case 07 immediately follows the definition `w:E -> [0,infinity)` and has no next use requiring a reminder:

> Zero weights are allowed. In particular, our convention does not exclude w(e)=0. It should be stressed that positivity is not required.

Both delete this paragraph. In case 08, the same convention was given two sections earlier and this is the first zero-weight construction:

> Recall that zero weights are allowed. We set w(e_0)=0 and w(e)=1 for e!=e_0.

Both retain it verbatim. This checks reader function, not a ban on reminders.

Case 11 immediately precedes a lemma that uses an arbitrary solution:

> We do not need uniqueness: fix any solution supplied by Proposition 3. The following estimate holds for every such choice.

Both retain it verbatim. Its negative wording explains the choice; it is not treated as a defensive disclaimer.

### Cost and scope

| Observed quantity | X: complete examples | Y: deferred examples |
| --- | ---: | ---: |
| English rule-text bytes (no interfaces/metadata) | 41,771 | 33,074 |
| Uncached input tokens | 17,288 | 13,214 |
| Cached input tokens | 275,456 | 187,776 |
| Output tokens | 1,854 | 1,880 |
| Tool calls | 10 | 7 |
| Elapsed seconds | 84.9 | 69.4 |

Both actually received every supplied nonblank instruction line, with no instruction truncation; neither fetched additional original examples. X additionally attempted `git diff` outside a repository (exit 129, truncated help output). This error and different call/cache patterns confound attributing the token reduction solely to omitted examples. Cached input is not free; these figures exclude maintainer preparation/evaluation. The source-volume reduction attributable to deferring illustrations is 20.8%, smaller than the previous combined reduction that also selected one language.

The source and rubric were fixed before the two runs; raw local artifacts live under `release/tests/paper/writing/coverage-cost/example-ablation/` outside the repository. `evaluation.json` records exact trace/output hashes and all case judgments. All attempts are retained.

**Decision:** keep the runtime reader unchanged, including rule-bearing examples and original illustrations available on demand. No additional mandatory guidance is supported by this null result. The explicit context makes these tasks easier than a real manuscript: this does not establish equivalence, long-paper quality, Chinese performance, or that examples never matter. Twelve cases inside each run are not twelve independent trials.
