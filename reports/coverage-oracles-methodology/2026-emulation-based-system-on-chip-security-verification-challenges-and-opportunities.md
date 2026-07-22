# Emulation-based System-on-Chip Security Verification: Challenges and Opportunities

## 基本信息

- 作者：Tanvir Rahman、Shuvagata Saha、Ahmed Y. Alhurubi、Sujan Kumar Saha、Farimah Farahmandi、Mark Tehranipoor
- 发表日期：2026-04-16
- 会议/期刊：arXiv
- 主分类：覆盖、Oracle 与 Fuzzing 方法
- 相关性：B·强邻近（score=5）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：Coverage, Oracles & Fuzzing Methodology、Formal & Directed Processor Verification
- 纳入依据：hardware/processor object: rtl, system-on-chip, soc；verification/fuzzing method: verification, validation, formal verification；security relevance: security, vulnerability
- 论文页面：[http://arxiv.org/abs/2604.15073v1](http://arxiv.org/abs/2604.15073v1)
- PDF：[https://arxiv.org/pdf/2604.15073v1](https://arxiv.org/pdf/2604.15073v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 32 页，提取 92425 字符

## 摘要

Increasing system-on-chip (SoC) heterogeneity, deep hardware/software integration, and the proliferation of third-party intellectual property (IP) have brought security validation to the forefront of semiconductor design. While simulation and formal verification remain indispensable, they often struggle to expose vulnerabilities that emerge only under realistic execution conditions, long software-driven interactions, and adversarial stimuli. In this context, hardware emulation is emerging as an increasingly important pre-silicon verification technology because it enables higher-throughput execution of RTL designs under realistic hardware/software workloads while preserving sufficient fidelity for security-oriented analysis. This paper presents a comprehensive survey and perspective on emulation-based security verification and validation. We organize the landscape of prior work across assertion-based security checking, coverage-driven exploration, adversarial testing, information-flow tracking, fault injection, and side-channel-oriented evaluation. We provide a structured view of emulation-enabled security verification workflows, including instrumentation, stimulus generation, runtime monitoring, and evidence-driven analysis. We also examine practical challenges related to observability, scalability, property specification, and the definition of security-oriented coverage metrics for emulation-based verification. Finally, we discuss emerging directions such as AI-assisted emulation, digital security twins, chiplet-scale security exploration, automated vulnerability assessment, and cloud-scale secure emulation. Overall, this paper positions emulation as a promising foundation for the next generation of pre-silicon hardware security assurance.

## 研究问题

现代SoC的安全验证面临规模、真实性和验证量三重约束：仿真和形式化方法在处理长期软件驱动交互、真实执行条件和对抗性刺激时存在不足。硬件仿真作为一种预硅验证技术，能够以更高吞吐量执行RTL设计，但如何在安全验证中系统性地应用硬件仿真尚缺乏清晰的工作流组织、技术分类和挑战分析。

## Introduction 梳理

现有安全验证方法（形式化验证、仿真、信息流追踪、模糊测试、故障注入等）各有局限：形式化方法在SoC规模下面临状态爆炸和软件建模困难；仿真速度慢限制了深度状态探索和长时间运行；模糊测试和渗透测试依赖输入质量和执行吞吐量。硬件仿真（FPGA原型、商业仿真系统、混合协同仿真）能提供更高吞吐量和真实硬件/软件交互，但文献对仿真在安全验证中的角色、工作流设计和工程权衡缺乏系统梳理。本文旨在填补这一空白，提供仿真安全验证的结构化视角、分类法和开放挑战。

## 方法

本文是一篇综述，未提出具体方法。文章分类和分析了现有仿真安全验证工作流，按三个维度组织：刺激/验证驱动（工作负载驱动、对抗性输入驱动、扰动驱动、泄漏导向）、验证引擎集成（仿真中心、混合引擎、跟踪驱动定位）、可观测性/仪器化（黑盒、灰盒、白盒）。并讨论了核心构建模块（嵌入式监视器、动态模糊测试、故障注入、跨层分析）和挑战（计算开销、集成、可调试性/覆盖）。

## 实验与评估

本文无实验评估。文中引用了多个现有工具和框架（如SoCFuzzer、TaintFuzzer、FormalFuzzer、SoFI、EmFIA等）的实验结果，但未提供统一基线或新实验。市场预测数据引用自第三方报告（Future Market Insights等），非本文实验。未确认Artifact。

## 核心贡献

1）厘清了硬件仿真在SoC安全验证中的定位；2）提出了ESV工作流的三维分类法（刺激驱动、引擎集成、可观测性）；3）分析了工程权衡和主要挑战；4）指出了未来研究方向和开放问题。

## 与本仓库研究主线的关系

强邻近。本文系统综述了基于仿真的安全验证，涵盖了模糊测试、故障注入、覆盖度、Oracle等主题，与处理器RTL Fuzzing和多hart一致性验证间接相关（仿真平台可用于执行多核一致性工作负载，但本文未明确聚焦多hart一致性）。文中提及的硬件模糊测试（如SoCFuzzer、TaintFuzzer）和故障注入（如SoFI、EmFIA）属于存储库直接相关技术。

## 结论

硬件仿真安全验证（ESV）是一个设计空间，需区分平台选择和工作流选择。提出分类法组织ESV，并指出关键挑战（编译/映射开销、有限可观测性、跟踪可扩展性、监视器自动化）和研究机会（AI驱动的闭环仿真、故障注入与模糊测试协同、异构系统扩展、数字孪生、形式化辅助仿真、覆盖度和标准化）。未来最有影响力的进展是将ESV视为连续回归工作流。

## 局限性

本文是综述，未提出新方法或新实验。讨论的挑战基于已有文献和工业实践，未量化。安全覆盖度指标仍不成熟。文中的市场预测仅为引用。

## 详细阅读分析

建议重点阅读第4节（分类法）、第5节（ESV核心构建模块）、第6节（挑战）和第7节（研究方向），特别是7.7和7.8两个具体研究问题（仿真故障注入和强化学习引导的模糊测试）。

## 后续核验问题

- 如何将仿真安全验证的分类法扩展到多hart内存一致性验证？
- 文中提到的灰盒仪器化策略在RTL模糊测试中的具体实施难点是什么？
- EmFIA框架如何与覆盖度导向的模糊测试结合？
- 数字孪生概念如何应用于处理器fuzzing的持续验证？
