# SpecASan: Mitigating Transient Execution Attacks Using Speculative Address Sanitization

## 基本信息

- 作者：Saber Ganjisaffar、Esmaeil Mohammadian Koruyeh、Jason Zellmer、Hodjat Asghari Esfeden、Chengyu Song
- 发表日期：2025-06-20
- 更新日期：
- 来源：Semantic Scholar
- 来源编号：b46e68b99d2b92824236eb36f87438bbde863969
- 研究类别：微架构安全
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[https://doi.org/10.1145/3695053.3731119](https://doi.org/10.1145/3695053.3731119)
- PDF：[https://dl.acm.org/doi/pdf/10.1145/3695053.3731119](https://dl.acm.org/doi/pdf/10.1145/3695053.3731119)
- 分析模式：仅元数据分析

## 摘要

Transient execution attacks (TEAs), such as Spectre and Meltdown, exploit speculative execution to leak sensitive data through residual microarchitectural state. Traditional defenses often incur high performance and hardware costs by delaying speculative execution or requiring additional shadow structures and dynamic information flow tracking. In contrast, our approach models these attacks as violations of software-defined security contracts and enforces these contracts in hardware using existing features. We introduce Speculative Address Sanitization (SpecASan), which leverages ARM’s Memory Tagging Extension (MTE) to extend memory safety protection from the committed path to the speculative path. When a speculative access does not pass the MTE tag comparison, this access is delayed until speculation resolves. This ensures that only validated accesses affect the microarchitectural state while preserving the performance benefits of speculation. When combined with Control-Flow Integrity (CFI) enforcement mechanisms, already supported by some hardware implementations, our evaluation shows that SpecASan effectively mitigates a broad class of transient execution attacks, including Spectre and Microarchitectural Data Sampling (MDS). Furthermore, SpecASan achieves this with low performance overhead and minimal hardware complexity, highlighting its practicality and efficiency.

## 研究问题

Transient execution attacks (TEAs), such as Spectre and Meltdown, exploit speculative execution to leak sensitive data through residual microarchitectural state. Traditional defenses often incur high performance and hardware costs by delaying speculative execution or requiring additional shadow structures and dynamic information flow tracking. In contrast, our approach models these attacks as violations of software-defined security contracts and enforces these contracts in hardware using existing features. We introduce Speculative Address Sanitization (SpecASan), which leverages ARM’s Memory Tagging Extension (MTE) to extend memory safety protection from the committed path to the speculative path. When a speculative access does not pass the MTE tag comparison, this access is delayed until speculation resolves. This ensures that only validated accesses affect the microarchitectural state while preserving the performance benefits of speculation. When combined with Control-Flow Integrity (CFI) enforcement mechanisms, already supported by some hardware implementations, our evaluation shows that SpecASan effectively mitigates a broad class of transient execution attacks, including Spectre and Microarchitectural Data Sampling (MDS). Furthermore, SpecASan achieves this with low performance overhead and minimal hardware complexity, highlighting its practicality and efficiency.

## Introduction 梳理

当前为基于题名和摘要生成的记录。配置 OPENAI_API_KEY 或 DEEPSEEK_API_KEY 后，可以启用全文阅读分析。

## 方法

等待全文提取后补充。

## 实验与评估

等待全文提取后补充。

## 结论

等待全文提取后补充。

## 局限性

等待全文提取后补充。初步阅读时应重点检查适用架构、测试对象、oracle 设计、覆盖率指标和复现实验条件。

## 详细阅读分析

等待全文提取后补充。建议结合论文 PDF、开源 artifact、实验对象和可迁移到 RISC-V/处理器 fuzzing 的部分继续分析。

## 后续跟进问题

- 论文是否提供开源实现或实验 artifact？
- 方法是否可以迁移到 RISC-V core、RTL 仿真器或真实处理器？
- 论文依赖什么 oracle、覆盖率指标或差分测试对象？
