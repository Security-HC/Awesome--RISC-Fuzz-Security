# The Emergence of Hardware Fuzzing: A Critical Review of its Significance

## 基本信息

- 作者：Raghul Saravanan、Sai Manoj Pudukotai Dinakarrao
- 发表日期：2024-03-19
- 会议/期刊：arXiv
- 主分类：RTL 与 SoC 硬件 Fuzzing
- 相关性：A·直接相关（score=10）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：RTL & SoC Hardware Fuzzing、Coverage, Oracles & Fuzzing Methodology、Formal & Directed Processor Verification
- 纳入依据：strong phrase in title: hardware fuzzing；hardware/processor object: processor, soc；verification/fuzzing method: fuzz, verification, formal verification；security relevance: security
- 论文页面：[http://arxiv.org/abs/2403.12812v1](http://arxiv.org/abs/2403.12812v1)
- PDF：[https://arxiv.org/pdf/2403.12812v1](https://arxiv.org/pdf/2403.12812v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 13 页，提取 73188 字符

## 摘要

In recent years, there has been a notable surge in attention towards hardware security, driven by the increasing complexity and integration of processors, SoCs, and third-party IPs aimed at delivering advanced solutions. However, this complexity also introduces vulnerabilities and bugs into hardware systems, necessitating early detection during the IC design cycle to uphold system integrity and mitigate re-engineering costs. While the Design Verification (DV) community employs dynamic and formal verification strategies, they encounter challenges such as scalability for intricate designs and significant human intervention, leading to prolonged verification durations. As an alternative approach, hardware fuzzing, inspired by software testing methodologies, has gained prominence for its efficacy in identifying bugs within complex hardware designs. Despite the introduction of various hardware fuzzing techniques, obstacles such as inefficient conversion of hardware modules into software models impede their effectiveness. This Systematization of Knowledge (SoK) initiative delves into the fundamental principles of existing hardware fuzzing, methodologies, and their applicability across diverse hardware designs. Additionally, it evaluates factors such as the utilization of golden reference models (GRMs), coverage metrics, and toolchains to gauge their potential for broader adoption, akin to traditional formal verification methods. Furthermore, this work examines the reliability of existing hardware fuzzing techniques in identifying vulnerabilities and identifies research gaps for future advancements in design verification techniques.

## 研究问题

硬件fuzzing技术作为设计验证方法的有效性、局限性及其与现有验证范式的差距。

## Introduction 梳理

现代IC设计复杂性导致漏洞激增，传统动态验证和形式化验证面临可扩展性和人力投入大等问题。硬件fuzzing作为替代方案出现，但存在硬件到软件转换低效等障碍。本文系统化综述现有硬件fuzzing的原理、方法和适用性，评估黄金参考模型(GRM)、覆盖度量和工具链的使用情况，并识别研究空白。

## 方法

本文为系统化知识(SoK)综述，而非提出新方法。它基于对现有硬件fuzzing框架的分类（直接适配软件fuzzer、硬件转软件、硬件即硬件、SoC fuzzer），分析其输入生成（如指令序列、字节序列）、覆盖率度量（MUX toggle、FSM、CSR等）、Oracle（断言、GRM、ISA模拟器）以及DUT/平台（RISC-V处理器如Ariane、IBEX，外围IP，SoC）。文中表I总结了各框架特征。

## 实验与评估

未涉及新实验。论文自身评估了现有框架的局限性，包括工具依赖（AFL的硬件不兼容、Verilator翻译不完整、FPGA开销、instrumentation开销）、覆盖率度量局限（人类偏倚、粒度不足、无法捕获安全漏洞）、以及验证依赖（断言人工介入、GRM可用性受限、ISA模拟器差异）。论文未提供baseline、实验预算、新发现bug/CVE、开销量化或artifact。

## 核心贡献

1) 系统化综述硬件fuzzing技术，分类现有方法；2) 指出工具依赖性（如AFL、Verilator）的固有限制；3) 揭示覆盖率度量的偏见和不完备性；4) 论证硬件fuzzing作为独立验证范式的局限性（'delusion'），并指出未来方向。

## 与本仓库研究主线的关系

直接相关。本文是硬件fuzzing的系统化综述，涵盖RISC-V处理器fuzzing、SoC fuzzing等主题，与仓库主题（处理器fuzzing、RTL/SoC硬件fuzzing）高度一致。但未涉及多hart/内存一致性验证，该方法论可用于指导该方向研究。

## 结论

本文SoK揭示了硬件fuzzing的现状：虽有多种方法，但存在工具依赖、覆盖率选择偏见、验证依赖等问题。硬件fuzzing尚未达到替代传统验证的标准，需解决等效性、泛化性和安全性漏洞检测等挑战。

## 局限性

论文未明确提及自身局限性。基于内容，可能的限制包括：综述范围限于所引用的工作，可能遗漏某些近期或非英语来源；对工具和方法的分析基于作者解读；未提出实验验证自身观点。

## 详细阅读分析

是。作为SoK，本文提供了硬件fuzzing的全面概览和批判性分析，对于理解领域挑战和未来工作至关重要。

## 后续核验问题

- 1) 如何解决AFL等软件fuzzer与硬件不兼容的问题？2) 哪种覆盖率度量最能兼顾功能验证与安全漏洞发现？3) 当缺乏GRM时，如何有效评估外设IP的正确性？4) 如何统一不同ISA的fuzzing框架？
