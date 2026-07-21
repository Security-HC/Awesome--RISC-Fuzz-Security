# When Fuzzing Meets Understanding: LLM-Driven Semantic Test Generation for RTL Verification

## 基本信息

- 作者：Kun Wang、Cangyuan Li、Kaiyan Chang、Siyang Cai、Yinhe Han、Ying Wang
- 发表日期：2026-07-11
- 更新日期：2026-07-11
- 来源：arXiv
- 来源编号：2607.10340v1
- 研究类别：RTL 与硬件验证、工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：5
- 论文页面：[http://arxiv.org/abs/2607.10340v1](http://arxiv.org/abs/2607.10340v1)
- PDF：[https://arxiv.org/pdf/2607.10340v1](https://arxiv.org/pdf/2607.10340v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash

## 摘要

The growing complexity of modern chips poses significant challenges to hardware verification. In recent years, coverage-guided fuzzing has emerged as a promising approach for improving verification efficiency. However, existing hardware fuzzers still struggle to achieve high coverage and expose corner-case bugs, as they predominantly rely on heuristic strategies with limited ability to reason about the internal logic and semantic behavior of the design under test (DUT). In this work, we propose ChipFuzzer, a hardware fuzzing framework that leverages the semantic reasoning capabilities of large language models (LLMs) to improve fuzzing effectiveness. ChipFuzzer adopts a dual-stage workflow comprising a Coverage-Guided stage and a Bug-Guided stage. In the Coverage-Guided stage, ChipFuzzer employs control-flow similarity and discrepancy analysis to guide LLM-driven testcase generation, thereby improving coverage. In the Bug-Guided stage, ChipFuzzer leverages historical bug data to identify bug-prone code regions and prioritize testcase generation for those regions, thus enhancing bug discovery efficiency. Experimental results on three open-source CPU designs show that ChipFuzzer improves average condition coverage by 5.8 percentage points and bug detection rate by 21.1 percentage points over the strongest baseline.

## 研究问题

现有硬件fuzzer依赖启发式策略，缺乏对DUT内部逻辑和语义行为的推理能力，导致覆盖率低且难以发现边界bug。

## Introduction 梳理

芯片复杂度增加使得验证成为设计周期中最耗费资源的阶段，现有硬件fuzzer继承自软件fuzzing，无法理解硬件结构语义，覆盖率增长平缓。LLM的出现为语义感知测试生成提供了新思路。本文提出ChipFuzzer，利用LLM语义推理能力提高fuzzing效率，采用双阶段流程：覆盖率引导阶段和bug引导阶段。在覆盖率引导阶段，通过控制流相似性和差异分析指导LLM生成测试用例；在bug引导阶段，利用历史bug数据识别易错区域。实验表明，ChipFuzzer在平均条件覆盖率和bug检测率上分别提高5.8和21.1个百分点。

## 方法

ChipFuzzer采用双阶段流程。阶段I（覆盖率引导）：从DUT未覆盖代码行中选择目标代码段，通过路径相似性索引检索最相似测试用例模板，进行差异分析（5条规则），将目标代码段、模板和差异分析结果组成提示词给LLM生成候选测试用例。语法错误通过语法修正器修复，语义错误通过语义修正器修复。测试用例在RTL和ISA模拟器上执行，若覆盖目标则存入种子库。阶段II（bug引导）：基于128个已验证历史bug数据，采用三种策略识别易错区域：历史bug实例、模块级重复模式、信号级混淆模式。复用阶段I的生成流程。最后通过语义级种子融合策略结合两个阶段的种子。

## 实验与评估

在三个开源CPU（RocketCore、BOOM、CVA6）上评估，与TheHuzz、Cascade、BMCFuzz比较。24小时fuzzing预算下，ChipFuzzer在条件覆盖率上提高9.1/1.2/7.0个百分点。测试用例效率：达到75%覆盖率仅需645个用例（比BMCFuzz少6.7倍）。bug检测率平均61.1%（基线最高40%）。消融实验显示，仅覆盖率引导达88.1%条件覆盖率，仅bug引导检测率38.9%，两者结合最佳。

## 结论

ChipFuzzer通过LLM的语义推理能力显著提高了硬件fuzzing的覆盖率和bug检测率，可作为传统方法的补充。但存在依赖LLM推理质量、开销大、适用范围限于RISC-V CPU等局限。

## 局限性

依赖LLM推理质量，可能对自定义指令或文档不充分的行为产生幻觉；LLM生成引入较大开销，早期阶段测试用例吞吐量受限；当前评估仅限于开源RISC-V CPU设计，对更广泛RTL设计的有效性需进一步研究。

## 详细阅读分析

本文深入分析了现有硬件fuzzer的局限性，并详细描述了ChipFuzzer的语义感知方法。关键技术包括控制流相似性索引、差异分析规则、语法语义修正、历史bug引导策略和语义级种子融合。实验设计全面，消融分析揭示了各组件贡献。但未讨论LLM的token成本和实时性，以及如何扩展到更复杂设计。

## 后续跟进问题

- ChipFuzzer如何适应非RISC-V架构（如ARM或自定义ISA）？
- LLM生成测试用例的延迟如何影响实际验证效率？
- 是否可以将LLM驱动生成与形式化方法结合以进一步提升覆盖率？
- 历史bug数据收集和标注的成本如何？
- 对于Chisel和SystemVerilog，LLM的语义理解有何差异？
