# The Emergence of Hardware Fuzzing: A Critical Review of its Significance

## 基本信息

- 作者：Raghul Saravanan、Sai Manoj Pudukotai Dinakarrao
- 发表日期：2024-03-19
- 更新日期：2024-03-19
- 来源：arXiv
- 来源编号：2403.12812v1
- 研究类别：RTL 与硬件验证、工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：2
- 论文页面：[http://arxiv.org/abs/2403.12812v1](http://arxiv.org/abs/2403.12812v1)
- PDF：[https://arxiv.org/pdf/2403.12812v1](https://arxiv.org/pdf/2403.12812v1)
- 分析模式：仅元数据分析

## 摘要

In recent years, there has been a notable surge in attention towards hardware security, driven by the increasing complexity and integration of processors, SoCs, and third-party IPs aimed at delivering advanced solutions. However, this complexity also introduces vulnerabilities and bugs into hardware systems, necessitating early detection during the IC design cycle to uphold system integrity and mitigate re-engineering costs. While the Design Verification (DV) community employs dynamic and formal verification strategies, they encounter challenges such as scalability for intricate designs and significant human intervention, leading to prolonged verification durations. As an alternative approach, hardware fuzzing, inspired by software testing methodologies, has gained prominence for its efficacy in identifying bugs within complex hardware designs. Despite the introduction of various hardware fuzzing techniques, obstacles such as inefficient conversion of hardware modules into software models impede their effectiveness. This Systematization of Knowledge (SoK) initiative delves into the fundamental principles of existing hardware fuzzing, methodologies, and their applicability across diverse hardware designs. Additionally, it evaluates factors such as the utilization of golden reference models (GRMs), coverage metrics, and toolchains to gauge their potential for broader adoption, akin to traditional formal verification methods. Furthermore, this work examines the reliability of existing hardware fuzzing techniques in identifying vulnerabilities and identifies research gaps for future advancements in design verification techniques.

## 研究问题

In recent years, there has been a notable surge in attention towards hardware security, driven by the increasing complexity and integration of processors, SoCs, and third-party IPs aimed at delivering advanced solutions. However, this complexity also introduces vulnerabilities and bugs into hardware systems, necessitating early detection during the IC design cycle to uphold system integrity and mitigate re-engineering costs. While the Design Verification (DV) community employs dynamic and formal verification strategies, they encounter challenges such as scalability for intricate designs and significant human intervention, leading to prolonged verification durations. As an alternative approach, hardware fuzzing, inspired by software testing methodologies, has gained prominence for its efficacy in identifying bugs within complex hardware designs. Despite the introduction of various hardware fuzzing techniques, obstacles such as inefficient conversion of hardware modules into software models impede their effectiveness. This Systematization of Knowledge (SoK) initiative delves into the fundamental principles of existing hardware fuzzing, methodologies, and their applicability across diverse hardware designs. Additionally, it evaluates factors such as the utilization of golden reference models (GRMs), coverage metrics, and toolchains to gauge their potential for broader adoption, akin to traditional formal verification methods. Furthermore, this work examines the reliability of existing hardware fuzzing techniques in identifying vulnerabilities and identifies research gaps for future advancements in design verification techniques.

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
