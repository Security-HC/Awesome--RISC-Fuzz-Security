# Securing Accelerators with Dynamic Information Flow Tracking

## 基本信息

- 作者：Luca Piccolboni、Giuseppe Di Guglielmo、Luca Carloni
- 发表日期：2019-02-19
- 会议/期刊：arXiv
- 主分类：覆盖、Oracle 与 Fuzzing 方法
- 相关性：A·直接相关（score=5）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：Coverage, Oracles & Fuzzing Methodology
- 纳入依据：hardware/processor object: processor, soc；verification/fuzzing method: information flow tracking；security relevance: security
- 论文页面：[http://arxiv.org/abs/1903.06801v1](http://arxiv.org/abs/1903.06801v1)
- PDF：[https://arxiv.org/pdf/1903.06801v1](https://arxiv.org/pdf/1903.06801v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 2 页，提取 10547 字符

## 摘要

Systems-on-chip (SoCs) are becoming heterogeneous: they combine general-purpose processor cores with application-specific hardware components, also known as accelerators, to improve performance and energy efficiency. The advantages of heterogeneity, however, come at a price of threatening security. The architectural dissimilarities of processors and accelerators require revisiting the current security techniques. With this hardware demo, we show how accelerators can break dynamic information flow tracking (DIFT), a well-known security technique that protects systems against software-based attacks. We also describe how the security guarantees of DIFT can be re-established with a hardware solution that has low performance and area penalties.

## 研究问题

如何保护异构SoC中的硬件加速器免受软件攻击，特别是确保动态信息流跟踪（DIFT）技术在整个SoC中一致有效，防止加速器成为攻击向量。

## Introduction 梳理

现有DIFT技术主要针对处理器设计，未充分考虑加速器的架构差异性，导致加速器可能成为攻击突破口。本文通过硬件演示展示加速器如何绕过DIFT，并提出一种低开销的硬件解决方案来重新建立安全保证。

## 方法

输入生成：采用具体应用（面部模糊处理）的配置参数作为攻击向量，通过修改参数缩小模糊区域；反馈/coverage：无；Oracle：DIFT标签检查和策略执行，要求输出数据必须为非敏感；DUT/平台：基于PULPino的RISC-V（RI5CY）SoC，扩展为DIFT感知的D-RI5CY，集成加速器（OBFUSCATOR）和DIFT shell；是否需要golden model：不需要，通过对比有无攻击和有无shell的场景验证。

## 实验与评估

baseline：原始PULPino SoC；实验预算：未明确；统计：无；bug/CVE：无；开销：D-RI5CY数据内存增加12.5%（32KB到36KB），LUT资源增加不超过0.82%，性能无影响；加速器shell仅需~200 LUTs和~700 flops/latches，性能开销可忽略；Artifact：演示视频（http://www.cs.columbia.edu/~piccolboni/demos/host2019.mp4）和ZedBoard原型。

## 核心贡献

硬件演示证明加速器可破坏DIFT安全保证，并提供低开销的硬件shell解决方案；展示耦合标签方案在异构SoC中的实现。

## 与本仓库研究主线的关系

弱相关：主题涉及RISC-V处理器和硬件安全，但非Fuzzing或验证。方法（DIFT、硬件shell）可借鉴于安全验证，但无覆盖、Oracle或Fuzzing内容。与多hart/一致性路径无直接关系。

## 结论

异构SoC中的加速器若不被DIFT保护，即使处理器和内存支持DIFT，仍可被利用泄露敏感信息。提出的DIFT shell能有效恢复安全保证，且开销极低。

## 局限性

仅考虑一种特定攻击模型（修改配置参数）；未评估多种攻击类型或复杂攻击；假设硬件可信；未讨论多核或多hart场景；结果基于单个应用和自定义SoC。

## 详细阅读分析

建议进一步阅读作者的相关工作PAGURUS [2] 以获取完整方法，以及D-RI5CY [4] 的详细设计。

## 后续核验问题

- DIFT shell如何处理加速器内部的数据流（如中间状态）？
- 该方法能否扩展到多hart系统或一致性协议？
- 是否考虑过更复杂的攻击路径（如侧信道）？
