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

## 可选小工具

两个 skill 均自带相同的两个工具，可以单独安装使用。在对应 skill 目录运行：

```bash
python scripts/pdf_pages.py /path/to/paper.pdf --cache /path/to/reading/pages.json
python scripts/pdf_pages.py /path/to/paper.pdf --cache /path/to/reading/pages.json --find "Proposition 2.1"
python scripts/pdf_pages.py /path/to/paper.pdf --cache /path/to/reading/pages.json --pages 3-5
python scripts/check_tex_log.py /path/to/_build/main.log /path/to/_build/main.blg
```

PDF 工具首次提取需要该 Python 环境安装 PyMuPDF；缓存绑定原 PDF 的 SHA-256，源文件变化后重新提取。默认只输出页数等索引，指定页码时完整输出对应页；`--pages all` 可读全部。优先复用已有带页码文本。空白提取不代表空白原页，需要另看 PDF 或 OCR；搜索也不能替代全文阅读。

日志工具只用 Python 标准库，不重新封装编译器。只传实际存在且属于本次构建的日志；问题总数完整，默认每类显示前三处，`--examples` 可调整。退出码 0/1/2 分别表示未匹配到问题、发现问题、输入不可读或为空。它不证明 PDF 已重新生成，也不判断数学正确性。两个工具不调用模型 API；减少的是临时代码和无关输出，尚未测量端到端 token 节省。

## 看实际样例

[公开样例](examples/README.md)：先看从十六组试写中筛出的[六组改写对照](examples/04-selected-revisions.md)，包含原段完整中译、英文改写与信息保留说明；另有摘要和证明概览的取舍讨论、Hessian 正定性的学习讲解。均取材于 OpenAI 公开稿件，附固定原文定位。

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

写作 skill 内置[原版 Writing DNA](math-paper-writing/assets/writing-dna-skill/SKILL.md)及其英文流程、中英文模板和原版引用的清理 skill，并保留固定版本与许可。数学蒸馏直接触发原版 `writing-dna-skill`，入口只增加一段数学适配链接；随后应用[数学适配](math-paper-writing/references/style-distillation.md)；无需另装蒸馏插件，普通改稿不加载整套蒸馏材料。数学适配保留数学条件、符号和证明状态，并支持用户明确选择的小样本模式，不把原版的风格相似度目标当作已经测得的分数。

- **标准模式：至少 20 篇完整、去重的作品，生成五份分析文档。**
- **也支持用户主动选择的 3 篇以上小样本模式**，输出暂定画像；1–2 篇可以做局部分析。
- 修订版、译本和同一论文的不同章节不增加作品数。合著和相关系列分别注明。
- 可以分析自己喜欢的最终稿，也可以比较修改前后的稿件；私人材料应留在自己的工作目录。

```text
使用 $writing-dna-skill，为这位数学作者做标准 Writing DNA 蒸馏，
并读取随包的数学适配说明。
收集至少20篇相关的完整作品，列出篇目、版本和证据页码，
分析重复选择和相反例子，输出五份报告。不要用小样本替代本次要求。
```

### 五个可选作者包

| 作者 | 本次选样覆盖 | 训练作品 | 报告 |
| --- | --- | ---: | ---: |
| [Tao](math-paper-writing/references/profile-tao.md) | 跨领域：PDE、几何、组合、数论等 | 20 | 5 |
| [Evans](math-paper-writing/references/profile-evans.md) | 非线性 PDE、变分方法 | 20 | 5 |
| [Stanley](math-paper-writing/references/profile-stanley.md) | 枚举与代数组合 | 20 | 5 |
| [Mumford](math-paper-writing/references/profile-mumford.md) | 经典代数几何 | 20 | 5 |
| [Milnor](math-paper-writing/references/profile-milnor.md) | 经典微分几何与几何拓扑 | 20 | 5 |

每包包含 `language-dna.md`、`structure-patterns.md`、`cognitive-framework.md`、`visual-style-guide.md` 和 `Writing-DNA.md`。结构报告列出全部来源、作者、日期、结构分析和阅读页码。选样含明确标注的研究短文、综述或研究通信，合计100篇，并非同质的期刊研究长文。Evans、Stanley、Mumford、Milnor各有一篇早期对照文章，不计入20篇；Tao没有预留未读的测试文章。Tao包含18篇研究论文或短文、2篇综述，重点是跨领域的改写与证明组织。

这些包提炼的是有出处、带适用条件的写作选择。局部改写只加载相关规则与原文段落；完整画像指导的写作按说明读取五份报告和五篇匹配的完整来源。普通改稿不必加载所有包。[详细范围与方法](math-paper-writing/references/field-profiles.md)。另有 [Tao 跨领域方法速览](math-paper-writing/references/author-models.md)。

## 集成与边界

`lieflat-less-ai-tone` 是原版 Writing DNA 附带的成稿清理 skill：只改规则清单命中的表达，保留未命中的文字和文章框架。它与去防御性写作有部分重叠，但不是同一个工具。数学工作按需要选择一种局部清理方式，不默认连续执行多个清理 skill。

`anti-defensive-writing` 和 Humanizer 是按需使用的可选辅助 skill。去掉空泛示弱时仍保留必要条件、反例和未解决步骤；不要求每次改稿都连续运行多轮重写。未安装且无法读取原始辅助说明时，继续使用本 skill 的基本指导，并如实说明未加载该辅助 skill。

论文全文通过链接获取，本仓库只分发 skill、原创分析与模板。写作画像不会自动确认数学结论，学习稿完成也不等于读者已经掌握。论文中的假设、量词、证明状态和已有作者决定始终优先。

## 测试与许可

本次发布做了结构与链接检查、100篇训练来源的去重和文件核验，以及六项局部使用回归。测试范围、构建环境限制和已有证据见 [TESTING.md](TESTING.md)。尚未完成新的盲测或完整独立行为评估。

采用 [MIT License](LICENSE)。Writing DNA 和 anti-defensive-writing 的来源说明与原始许可保留在 [写作 skill 的来源页](math-paper-writing/references/sources.md)和 `licenses/` 中。学习 skill 的教学设计依据见其[方法说明](math-paper-study-guide/references/chinese-study-edition-method.md)。

---

**English:** Two skills for mathematical manuscript writing and proof-focused paper study. The writing skill includes optional twenty-work profiles of Tao, Evans, Stanley, Mumford and Milnor, plus the bundled original Writing DNA runtime and a mathematical adaptation supporting explicitly chosen smaller corpora. Install either skill folder through your tool's skill installer. Full-paper study defaults to a Chinese PDF and editable source; request English or conversation-only explanations when preferred.
