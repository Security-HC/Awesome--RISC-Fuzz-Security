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
- 命中次数：3
- 论文页面：[http://arxiv.org/abs/2607.10340v1](http://arxiv.org/abs/2607.10340v1)
- PDF：[https://arxiv.org/pdf/2607.10340v1](https://arxiv.org/pdf/2607.10340v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash

## 摘要

The growing complexity of modern chips poses significant challenges to hardware verification. In recent years, coverage-guided fuzzing has emerged as a promising approach for improving verification efficiency. However, existing hardware fuzzers still struggle to achieve high coverage and expose corner-case bugs, as they predominantly rely on heuristic strategies with limited ability to reason about the internal logic and semantic behavior of the design under test (DUT). In this work, we propose ChipFuzzer, a hardware fuzzing framework that leverages the semantic reasoning capabilities of large language models (LLMs) to improve fuzzing effectiveness. ChipFuzzer adopts a dual-stage workflow comprising a Coverage-Guided stage and a Bug-Guided stage. In the Coverage-Guided stage, ChipFuzzer employs control-flow similarity and discrepancy analysis to guide LLM-driven testcase generation, thereby improving coverage. In the Bug-Guided stage, ChipFuzzer leverages historical bug data to identify bug-prone code regions and prioritize testcase generation for those regions, thus enhancing bug discovery efficiency. Experimental results on three open-source CPU designs show that ChipFuzzer improves average condition coverage by 5.8 percentage points and bug detection rate by 21.1 percentage points over the strongest baseline.

## 研究问题

现有硬件fuzzer主要依赖启发式策略，无法对设计内部逻辑和语义行为进行推理，导致覆盖率和bug发现效率低下，尤其在复杂CPU设计中难以触达边界情况。

## Introduction 梳理

本文提出ChipFuzzer，一个利用大语言模型（LLM）语义推理能力增强硬件fuzzing的框架。该框架包含两个阶段：覆盖率引导阶段（Stage I）通过控制流相似性索引、差异分析和LLM驱动的测试生成来提升覆盖率；错误引导阶段（Stage II）利用历史bug数据识别易错代码区域并优先生成测试用例。在三个开源RISC-V CPU设计上的实验表明，ChipFuzzer在条件覆盖率和bug检测率上分别超过最强基线5.8和21.1个百分点。

## 方法

ChipFuzzer采用双阶段流水线。Stage I（覆盖率引导）：从DUT未覆盖代码行中选择目标代码段，利用Pyverilog提取控制流路径，通过路径相似性索引从种子库中检索最相似测试模板，再进行差异分析（对齐路径、识别缺失分支条件、状态准备、触发事件和合法性），将目标段、模板和差异分析结果输入LLM生成候选测试，经语法校正器（修复编译错误）和语义校正器（基于执行反馈修正）后仿真，成功覆盖的种子存入覆盖率引导种子库。Stage II（错误引导）：基于128个历史bug PR构建三种先验（历史bug实例、模块级重复模式、信号级混淆模式），识别易错区域并重复上述生成管线，种子存入错误引导种子库。最后通过语义融合策略结合两类种子生成更丰富的测试。

## 实验与评估

在RocketCore、BOOM、CV A6三个处理器上评估，对比TheHuzz、Cascade、BMCFuzz。覆盖指标：条件覆盖率、寄存器翻转覆盖率、多路选择器翻转覆盖率。ChipFuzzer平均条件覆盖率提升5.8pp，bug检测率提升21.1pp（Encarsia平台90个bug）。消融实验：仅LLM无引导（LO）覆盖率低；仅覆盖率引导（CG）达88.1%；增加错误引导（CBG）达89.2%；错误引导（BG）主要提升bug检测（38.9%），CBG达61.1%。不同LLM（GPT-5.3、Gemini 3、DeepSeek-V3）均优于基线，GPT-5.3最优。测试效率：达到75%（RocketCore）和90%（BOOM）覆盖率所需测试数远少于基线。

## 结论

ChipFuzzer通过语义引导的测试生成显著优于传统方法，可有效补充现有fuzzer。其优势在于利用LLM推理控制流和状态条件，而传统方法依赖随机突变。两个阶段互补：覆盖率引导确保基本覆盖，错误引导聚焦易错区域。整体上提高了验证效率。

## 局限性

1) 依赖LLM推理质量，可能对自定义指令或文档不足的行为产生幻觉。2) LLM推理引入较大开销，导致早期测试吞吐量低。3) 当前评估仅针对开源RISC-V CPU，对其他硬件类型（如GPU、外设）的有效性未知。4) 历史bug数据需要人工收集和验证，可能不完整。

## 详细阅读分析

ChipFuzzer的核心创新在于将LLM的语义理解与结构化差异分析结合，使测试生成从盲目的突变转向基于设计逻辑的定向生成。路径相似性索引和差异分析规则（路径对齐、分支条件、状态准备、事件触发、合法性）为LLM提供了清晰的推理框架。此外，错误引导阶段利用历史bug先验（实例、模块模式、信号模式）有效提高了bug发现效率。种子融合策略进一步增强了测试语义丰富性。与形式化方法结合可能是未来方向，以减少LLM的不确定性。

## 后续跟进问题

- 如何减少LLM推理延迟以提高ChipFuzzer的测试吞吐量？可以用小模型或蒸馏吗？
- ChipFuzzer能否应用于非RISC-V架构或更复杂的SoC设计？
- 自动收集和验证历史bug数据的方法有哪些？如何减少人工标注工作量？
- 能否将差异分析规则形式化，与符号执行或模型检查结合以提供更精确的引导？
- ChipFuzzer在处理RTL仿真反馈时是否可能被覆盖反馈误导？如何增强反馈信号（如覆盖盲点检测）？
