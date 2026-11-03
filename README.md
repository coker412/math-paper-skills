# Math Paper Skills

两套面向数学研究的 AI skills：**读懂论文的证明，写清自己的数学。**

| Skill | 解决什么问题 | 入口 |
| --- | --- | --- |
| `math-paper-writing` | 起草、改写和检查数学论文；处理中英文一致性；从论文中蒸馏可复用的写作方法 | [使用说明](math-paper-writing/SKILL.md) |
| `math-paper-study-guide` | 解释难懂的证明步骤；按读者基础展开计算；制作整篇论文的学习 PDF 与可编辑源文件 | [使用说明](math-paper-study-guide/SKILL.md) |

## 安装

在 Codex 中使用内置的 skill installer，可以直接提出：

```text
请从 GitHub 仓库 coker412/math-paper-skills 安装这两个 skill：
math-paper-writing
math-paper-study-guide
```

也可以克隆本仓库，把需要的 skill 文件夹放到 `~/.codex/skills/`。若设置了 `CODEX_HOME`，使用其下的 `skills/`。已有同名文件夹时，先比较本地修改再更新。两个文件夹可以单独安装；支持 `SKILL.md` 的其他工具可按各自的安装方式导入。

```bash
git clone https://github.com/coker412/math-paper-skills.git
```

日常解释与改写不需要 LaTeX。生成学习 PDF 需要 XeLaTeX、ctex、AMS 宏包和 Fandol 字体，建议配合 latexmk。缺少编译环境时，skill 应保留可编辑源并明确 PDF 尚未生成。

## 怎么用

**修改论文，但保持数学内容和作者已确定的选择：**

```text
使用 $math-paper-writing 修改这段引言。
保留所有假设、记号、结论和已确认的摘要。
让辅助构造的用途更清楚，并给我说明具体改了什么。
```

**读懂一个步骤：**

```text
使用 $math-paper-study-guide 解释这里为什么能交换极限与积分。
我只熟悉微积分和线性代数。请展开实际用到的条件和计算，
只在对话里解释，不生成文件。
```

**学习整篇论文：**

```text
使用 $math-paper-study-guide，为这篇完整论文制作中文学习 PDF
和可编辑源。先解释准确问题与主结果，再展开证明的关键依赖和计算。
如果源文有缺口，请指出，不要替作者默默补上。
```

## Writing DNA：从论文中学习写作方法

写作 skill 包含 Writing DNA 的数学适配，覆盖语言、结构、问题切入、证据作用、推理呈现和视觉组织。无需另装蒸馏插件。

- **标准模式：至少 20 篇完整、去重的作品，生成五份分析文档。**
- **也支持用户主动选择的 3 篇以上小样本模式**，输出暂定画像；1–2 篇可以做局部分析。
- 修订版、译本和同一论文的不同章节不增加作品数。合著和相关系列分别注明。
- 可以分析自己喜欢的最终稿，也可以比较修改前后的稿件；私人材料应留在自己的工作目录。

```text
使用 $math-paper-writing，为这位作者做标准 Writing DNA 蒸馏。
收集至少20篇相关的完整作品，列出篇目、版本和证据页码，
分析重复选择和相反例子，输出五份报告。不要用小样本替代本次要求。
```

### 四个可选领域包

| 作者 | 本次选样覆盖 | 训练作品 | 报告 |
| --- | --- | ---: | ---: |
| [Evans](math-paper-writing/references/profile-evans.md) | 非线性 PDE、变分方法 | 20 | 5 |
| [Stanley](math-paper-writing/references/profile-stanley.md) | 枚举与代数组合 | 20 | 5 |
| [Mumford](math-paper-writing/references/profile-mumford.md) | 经典代数几何 | 20 | 5 |
| [Milnor](math-paper-writing/references/profile-milnor.md) | 经典微分几何与几何拓扑 | 20 | 5 |

每包包含 `language-dna.md`、`structure-patterns.md`、`cognitive-framework.md`、`visual-style-guide.md` 和 `Writing-DNA.md`。结构报告列出全部来源、作者、日期、结构分析和阅读页码。选样含明确标注的研究短文、综述或研究通信，并非80篇同质的期刊研究长文。每位作者另外有一篇早期对照文章，不计入20篇。

这些包提炼的是有出处、带适用条件的写作选择。局部改写只加载相关规则与原文段落；完整画像指导的写作按说明读取五份报告和五篇匹配的完整来源。普通改稿不必加载所有包。[详细范围与方法](math-paper-writing/references/field-profiles.md)。另有 [Tao 跨领域方法参考](math-paper-writing/references/author-models.md)。

## 集成与边界

`anti-defensive-writing` 和 Humanizer 是按需使用的可选辅助 skill。去掉空泛示弱时仍保留必要条件、反例和未解决步骤；不要求每次改稿都连续运行多轮重写。未安装且无法读取原始辅助说明时，继续使用本 skill 的基本指导，并如实说明未加载该辅助 skill。

论文全文通过链接获取，本仓库只分发 skill、原创分析与模板。写作画像不会自动确认数学结论，学习稿完成也不等于读者已经掌握。论文中的假设、量词、证明状态和已有作者决定始终优先。

## 测试与许可

本次发布做了结构与链接检查、80篇训练来源的去重和文件核验，以及六项局部使用回归。测试范围、构建环境限制和已有证据见 [TESTING.md](TESTING.md)。尚未完成新的盲测或完整独立行为评估。

采用 [MIT License](LICENSE)。Writing DNA 和 anti-defensive-writing 的来源说明与原始许可保留在 [写作 skill 的来源页](math-paper-writing/references/sources.md)和 `licenses/` 中。学习 skill 的教学设计依据见其[方法说明](math-paper-study-guide/references/chinese-study-edition-method.md)。

---

**English:** Two skills for mathematical manuscript writing and proof-focused paper study. The writing skill includes optional twenty-work profiles of Evans, Stanley, Mumford and Milnor, plus a self-contained Writing DNA workflow supporting explicitly chosen smaller corpora. Install either skill folder through your tool's skill installer. Full-paper study defaults to a Chinese PDF and editable source; request English or conversation-only explanations when preferred.
