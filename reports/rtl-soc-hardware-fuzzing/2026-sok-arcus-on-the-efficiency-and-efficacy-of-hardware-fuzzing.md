# SoK: ARCUS: On the Efficiency and Efficacy of Hardware Fuzzing

## 基本信息

- 作者：Alenkruth Krishnan Murali、Raghul Saravanan、Sai Manoj P D、Ashish Venkat
- 发表日期：2026-08-25
- 会议/期刊：arXiv
- 主分类：RTL 与 SoC 硬件 Fuzzing
- 相关性：A·直接相关（score=9）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：RTL & SoC Hardware Fuzzing、Coverage, Oracles & Fuzzing Methodology
- 纳入依据：strong phrase in title: hardware fuzzing；hardware/processor object: microarchitecture, rtl；verification/fuzzing method: fuzz, test generation, verification
- 论文页面：[http://arxiv.org/abs/2608.23933v1](http://arxiv.org/abs/2608.23933v1)
- PDF：[https://arxiv.org/pdf/2608.23933v1](https://arxiv.org/pdf/2608.23933v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 19 页，提取 100000 字符

## 摘要

This work presents a comprehensive analysis of contemporary hardware fuzzing techniques applied across three major abstraction layers: Instruction Set Architecture (ISA), microarchitecture, and Register-Transfer Level (RTL). Our study examines key factors including input stimulus quality, mutation strategies, feedback mechanisms, target platforms, reference models, and achieved coverage. We find challenges, goals, and design trade-offs vary significantly across abstraction layers. We further identify several unmet needs in current hardware fuzzing practices, such as intelligent input generation, reliable and scalable golden reference models, expressive feedback channels, and cross-layer integration. Building on these insights, we outline future research directions, including hybrid fuzzing frameworks, AI-assisted test generation, scalable reference models, standardized evaluation metrics and benchmarks, and human-in-the-loop automation for guided exploration and analysis. Together, they aim to unlock efficient, reliable, and comprehensive hardware verification solutions.

## 研究问题

硬件fuzzing领域缺乏跨抽象层的系统性分析与比较。现有调查（如Encarsia、Fuzz-Odyssey）仅覆盖白盒RTL fuzzer，未涵盖ISA、微架构和RTL三个主要硬件抽象层，且未统一比较不同工具的输入生成、反馈机制、GRM依赖等关键设计维度，导致研究碎片化，难以评估各方法优劣与适用场景。

## Introduction 梳理

随着处理器复杂度增长，硬件漏洞频发，传统验证方法难以扩展，fuzzing被引入硬件验证。已有的硬件fuzzer目标多样，涵盖黑盒CPU、解码器、RTL等，跨多个抽象层，各自面临独特挑战。但现有比较研究（如Encarsia仅分析4个fuzzer，Fuzz-Odyssey仅调查12个白盒RTL fuzzer）范围有限，未充分系统化。为此，本文提出ARCUS，首个跨ISA、µArch、RTL三个抽象层的系统化分析，引入两层分类法（按抽象层和方法论），定义核心分析维度（输入刺激、变异策略、反馈、GRM等），用于标准化比较。基于分析，识别出智能输入生成、可靠GRM、表达性反馈通道和跨层集成等未满足需求，并展望未来研究方向。

## 方法

本文为SoK（Systematization of Knowledge），采用系统性文献分析方法：收集并分类34个硬件fuzzer（来自已有论文），提出两级分类（第一级按抽象层：ISA、µArch、RTL；第二级按方法论，如Fault Analysis、Differential Fuzzing、Tracing等）。定义表1中的9个分析维度，包括输入刺激、fuzzing方法、目标类型、黑白盒属性、覆盖/反馈、变异算法、GRM使用及类型、自动化程度、bug类型。对每个fuzzer按维度进行编码和比较，并通过表格（如表2）汇总。未进行任何自己的实验，所有定量数据（如表3-6）均直接摘自原始论文。

## 实验与评估

本文没有自己的实验评估，而是对已有fuzzer的文献数据进行系统性比较。主要比较包括：表3显示SkipScan在识别未公开指令时的测试效率是Sandsifter的4倍（基于指令总数与未公开指令数之比）；表4比较了硬件与软件参考模型的时间/吞吐（如iDEV、Examiner等）；表5展示µArch fuzzer发现漏洞的时间（如Revizor找到Spectre V1用时4m51s，Medusa需26小时）；表6展示在CV A6上不同RTL fuzzer（TheHuzz、HypFuzz、PSOFuzz、MABFuzz）触发相同CWE漏洞所需测试用例数，差异显著。报告了TheHuzz不可用导致基线重置问题，以及覆盖率指标不标准化等问题。未确认：无原始开销数据、无统一统计、无正式基准。Artifact：本文无新增artifact，但引用了多个开源工具。

## 核心贡献

1. 进行首个跨ISA、µArch（post-silicon）和RTL（pre-silicon）三层的硬件fuzzer综合分析。2. 引入两层分类法，按抽象层和方法论对fuzzer分类。3. 定义核心分析维度（如输入刺激、fuzzing算法、覆盖反馈、GRM等），系统化比较现有方法。4. 识别关键不足：包括反馈机制受限、输入生成弱、GRM依赖不可靠、跨层集成缺乏。5. 提出未来研究方向：混合fuzzing框架、AI辅助测试生成、可扩展参考模型、标准化指标与基准、人在回路自动化。

## 与本仓库研究主线的关系

直接相关。本文系统梳理了硬件fuzzing领域，覆盖多个RISC-V相关fuzzer（如RISCVuzz、ProcessorFuzz、DiFuzzRTL、Cascade等），并讨论了多核一致性（如表6中V2 cache coherency violation）及微架构安全（如侧信道、幽灵/熔断变体）。与多hart和内存一致性验证路径的关系：RTL fuzzing中通过GRM比较检测不一致性，微架构fuzzing则探测未指定实现细节（如缓存行为），这些均涉及多核/一致性安全。

## 结论

本文系统化分析了跨ISA、µArch和RTL的硬件fuzzing工作，提出两层分类法和分析维度，揭示现有方法在反馈机制、输入生成、GRM可靠性和跨层集成方面的不足。作者强调，硬件fuzzing已从随机暴力搜索演进为更精细的方法，但仍受限于不完整的参考模型和孤立的测试方法。未来需要智能指令序列生成、可扩展分层硬件oracle、标准化指标与基准，以及跨层混合fuzzing，以实现系统化、全面的硬件验证。

## 局限性

本文是SoK，不包含原始实验，所有结论基于对已发表论文的解读，可能受原始论文局限性影响。由于各fuzzer报告指标不一致（如覆盖率类型、时间、测试数量），定量比较存在困难。部分关键工具（如TheHuzz）未开源，导致不同论文中基线数据差异大，影响可比性。此外，作者未提供标准化基准或统一评估协议，因此无法进行严格统计验证。

## 详细阅读分析

建议深入阅读第2-4节，分别了解ISA、µArch、RTL层fuzzer的详细分析与权衡；表2可作为快速参考图谱；第5节跨层见解总结了结构化输入、指标异构性、攻击驱动等主题；第6节未来方向为研究提供具体切入点。

## 后续核验问题

- 1. 如何建立跨抽象层的统一硬件fuzzing基准和标准化指标，以实现公平比较？2. 如何自动构建可靠且可扩展的黄金参考模型（GRM），特别是针对微架构行为？3. 如何设计跨层（ISA→µArch→RTL）混合fuzzing框架，协同测试不同抽象层？4. 如何利用LLM或强化学习在缺少反馈（如黑盒CPU）时生成有效输入？5. 如何将微架构fuzzing从已知攻击模板拓展到未知侧信道/时序漏洞的发现？
