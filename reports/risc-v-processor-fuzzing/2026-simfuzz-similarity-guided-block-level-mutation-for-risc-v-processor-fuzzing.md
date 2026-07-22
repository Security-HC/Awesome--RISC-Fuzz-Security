# SimFuzz: Similarity-guided Block-level Mutation for RISC-V Processor Fuzzing

## 基本信息

- 作者：Hao Lyu、Jingzheng Wu、Xiang Ling、Yicheng Zhong、Zhiyuan Li、Tianyue Luo
- 发表日期：2026-01-17
- 会议/期刊：arXiv
- 主分类：RISC-V 处理器 Fuzzing
- 相关性：A·直接相关（score=100）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：RISC-V Processor Fuzzing、Coverage, Oracles & Fuzzing Methodology
- 纳入依据：manual direct seed title
- 论文页面：[http://arxiv.org/abs/2601.11838v1](http://arxiv.org/abs/2601.11838v1)
- PDF：[https://arxiv.org/pdf/2601.11838v1](https://arxiv.org/pdf/2601.11838v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 7 页，提取 38799 字符

## 摘要

The Instruction Set Architecture (ISA) defines processor operations and serves as the interface between hardware and software. As an open ISA, RISC-V lowers the barriers to processor design and encourages widespread adoption, but also exposes processors to security risks such as functional bugs. Processor fuzzing is a powerful technique for automatically detecting these bugs. However, existing fuzzing methods suffer from two main limitations. First, their emphasis on redundant test case generation causes them to overlook cross-processor corner cases. Second, they rely too heavily on coverage guidance. Current coverage metrics are biased and inefficient, and become ineffective once coverage growth plateaus. To overcome these limitations, we propose SimFuzz, a fuzzing framework that constructs a high-quality seed corpus from historical bug-triggering inputs and employs similarity-guided, block-level mutation to efficiently explore the processor input space. By introducing instruction similarity, SimFuzz expands the input space around seeds while preserving control-flow structure, enabling deeper exploration without relying on coverage feedback. We evaluate SimFuzz on three widely used open-source RISC-V processors: Rocket, BOOM, and XiangShan, and discover 17 bugs in total, including 14 previously unknown issues, 7 of which have been assigned CVE identifiers. These bugs affect the decode and memory units, cause instruction and data errors, and can lead to kernel instability or system crashes. Experimental results show that SimFuzz achieves up to 73.22% multiplexer coverage on the high-quality seed corpus. Our findings highlight critical security bugs in mainstream RISC-V processors and offer actionable insights for improving functional verification.

## 研究问题

现有处理器模糊测试方法存在两个主要局限：1) 生成大量冗余测试用例，忽略跨处理器角落情况；2) 过度依赖覆盖率反馈，覆盖率指标有偏且低效，在覆盖率达到平台后失效。因此需要一种不依赖覆盖率反馈、能够有效探索处理器输入空间并发现bug的方法。

## Introduction 梳理

ISA是软硬件接口，RISC-V开放降低了处理器设计门槛但也带来了安全风险。处理器模糊测试是自动检测bug的有效技术，但现有方法（如PathFuzz）过度依赖覆盖率引导，生成冗余测试用例，并且覆盖率指标有偏，达到平台后无法提供有效指导。本文提出SimFuzz，通过构建高质量种子语料库（来自真实历史bug触发输入）和采用相似性引导的块级变异来探索输入空间，无需覆盖率反馈。在三个RISC-V处理器上实验，发现17个bug（14个新，7个CVE），证明了有效性。

## 方法

输入生成：从Rocket、BOOM和XiangShan的GitHub issues和CVE中爬取历史bug报告，筛选并构造综合种子语料库（42个二进制测试用例）。变异阶段采用块级变异：将种子按控制转移指令（CTI）切分为块，在块内进行指令级变异，但不修改CTI以保持控制流结构。相似性引导：计算变异后块与原块的指令相似度（加权组合类型、操作码、子语义和字段级相似度），若相似度低于阈值T（实验设为0.5）则接受该变异，否则保留原块。Oracle：将变异后的测试用例分别在RTL模拟器和ISA参考模拟器（Rocket/BOOM使用Spike，XiangShan使用NEMU）上执行，通过差分测试检测行为不一致。DUT：Rocket、BOOM、XiangShan三个开源RISC-V处理器。需要golden model：ISA模拟器作为参考。

## 实验与评估

Baseline：PathFuzz以及SimFuzz*（无相似性引导的变异）。实验预算：Csmith和Cascade种子各变异10次（共10000个测试用例），历史种子变异100次（4200个）。覆盖率指标：mux和toggle。结果：在历史种子语料库上，SimFuzz达到73.22% mux覆盖率（PathFuzz 71.33%），54.51% toggle覆盖率（PathFuzz 54.57%）。在Cascade和Csmith种子上覆盖率略低于PathFuzz（表II）。发现17个bug，其中14个为新，7个获CVE。Bug影响解码单元、内存单元等，导致指令/数据错误及系统崩溃。开销未明确，Artifact已开源（https://github.com/has2lab/SimFuzz）。

## 核心贡献

1) 构建了来自真实世界RISC-V处理器bug触发测试用例的高质量种子语料库；2) 提出了SimFuzz框架，以指令相似性引导的块级变异替代传统覆盖率反馈机制；3) 实验证明SimFuzz在三个主流RISC-V处理器上达到较高覆盖率，并发现14个新bug（7个CVE）。

## 与本仓库研究主线的关系

强邻近：直接相关于RISC-V处理器模糊测试，但未涉及多hart或内存一致性验证。其相似性引导变异方法可借鉴到多核/一致性输入生成，但论文本身未覆盖该场景。因此对多hart/一致性路径研究具有方法论借鉴意义。

## 结论

SimFuzz通过构建高质量历史种子语料库和相似性引导的块级变异，在不依赖覆盖率反馈的情况下有效探索处理器输入空间。实验结果表明其覆盖率接近甚至优于PathFuzz，并发现了14个新bug（7个CVE）。此外，发现相同架构的不同处理器可能共享相似bug，强调了在验证中融入真实bug样本的重要性。

## 局限性

1) 种子语料库依赖已知bug，可能限制对新类型bug的发现；2) 相似性阈值T需手动设定（本文取0.5），缺乏自适应调整；3) 仅与PathFuzz进行覆盖率比较，未与其他处理器fuzzer（如DifuzzRTL等）全面对比；4) 覆盖率在达到一定程度后出现饱和（图4），论文指出覆盖率本身可能不足以表征状态空间探索程度；5) 方法仅在单核RISC-V处理器上验证，未涉及多核/一致性场景。

## 详细阅读分析

论文在相似性度量设计中未公开四个权重（w1-w4）的具体数值，阈值T=0.5通过初步测试确定，缺乏系统性调节分析。此外，历史种子库虽然规模小（42个），但能触发跨处理器重复bug（如B7在Rocket和XiangShan重现），证明了其有效性。参考模型NEMU本身存在bug（B2-B4等），突出了差分测试中参考模型正确性的关键作用。

## 后续核验问题

- 如何自动学习或优化相似性度量中的权重和阈值？
- 能否将相似性引导变异扩展到多核/内存一致性验证场景？
- 种子语料库的构建能否完全自动化并持续更新？
- 当覆盖率饱和后，除了调整阈值，还有哪些方法能进一步探索输入空间？
- 该方法对于发现安全关键漏洞（如幽灵、熔断类）的效果如何？
