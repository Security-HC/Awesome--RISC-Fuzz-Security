# SpecDoctor: Differential Fuzz Testing to Find Transient Execution Vulnerabilities

## 基本信息

- 作者：Jaewon Hur、Suhwan Song、Sunwoo Kim、Byoungyoung Lee
- 发表日期：2022-11-07
- 更新日期：
- 来源：Semantic Scholar
- 来源编号：421ce75a3fe38d85194a9510b3d8e68881cd1869
- 研究类别：RISC-V Fuzzing 研究、微架构安全、RTL 与硬件验证
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[https://doi.org/10.1145/3548606.3560578](https://doi.org/10.1145/3548606.3560578)
- PDF：[]()
- 分析模式：仅元数据分析

## 摘要

Transient execution vulnerabilities have critical security impacts to software systems since those break the fundamental security assumptions guaranteed by the CPU. Detecting these critical vulnerabilities in the RTL development stage is particularly important, as it offers a chance to fix the vulnerability early before reaching the chip manufacturing stage. This paper proposes SpecDoctor, an automated RTL fuzzer to discover transient execution vulnerabilities in the CPU. To be specific, SpecDoctor designs a fuzzing template, allowing it to test all different scenarios of transient execution vulnerabilities (e.g., Meltdown, Spectre, ForeShadow, etc.) with a single template. Then SpecDoctor performs a multi-phased fuzzing, where each phase is dedicated to solve an individual vulnerability constraint in the RTL context, thereby effectively finding the vulnerabilities. We implemented and evaluated SpecDoctor on two out-of-order RISC-V CPUs, Boom and NutShell-Argo. During the evaluation, SpecDoctor found transient-execution vulnerabilities which share the similar attack vectors as the previous works. Furthermore, SpecDoctor found two interesting variants which abuse unique attack vectors: Boombard, and Birgus. Boombard exploits an unknown implementation bug in RISC-V Boom, exacerbating it into a critical transient execution vulnerability. Birgus launches a Spectre-type attack with a port contention side channel in NutShell CPU, which is constructed using a unique combination of instructions. We reported the vulnerabilities, and both are confirmed by the developers, illustrating the strong practical impact of SpecDoctor.

## 研究问题

Transient execution vulnerabilities have critical security impacts to software systems since those break the fundamental security assumptions guaranteed by the CPU. Detecting these critical vulnerabilities in the RTL development stage is particularly important, as it offers a chance to fix the vulnerability early before reaching the chip manufacturing stage. This paper proposes SpecDoctor, an automated RTL fuzzer to discover transient execution vulnerabilities in the CPU. To be specific, SpecDoctor designs a fuzzing template, allowing it to test all different scenarios of transient execution vulnerabilities (e.g., Meltdown, Spectre, ForeShadow, etc.) with a single template. Then SpecDoctor performs a multi-phased fuzzing, where each phase is dedicated to solve an individual vulnerability constraint in the RTL context, thereby effectively finding the vulnerabilities. We implemented and evaluated SpecDoctor on two out-of-order RISC-V CPUs, Boom and NutShell-Argo. During the evaluation, SpecDoctor found transient-execution vulnerabilities which share the similar attack vectors as the previous works. Furthermore, SpecDoctor found two interesting variants which abuse unique attack vectors: Boombard, and Birgus. Boombard exploits an unknown implementation bug in RISC-V Boom, exacerbating it into a critical transient execution vulnerability. Birgus launches a Spectre-type attack with a port contention side channel in NutShell CPU, which is constructed using a unique combination of instructions. We reported the vulnerabilities, and both are confirmed by the developers, illustrating the strong practical impact of SpecDoctor.

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
