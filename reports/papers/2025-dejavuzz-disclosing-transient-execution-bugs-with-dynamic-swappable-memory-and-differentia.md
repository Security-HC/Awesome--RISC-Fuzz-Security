# DejaVuzz: Disclosing Transient Execution Bugs with Dynamic Swappable Memory and Differential Information Flow Tracking assisted Processor Fuzzing

## 基本信息

- 作者：Jinyan Xu、Yangye Zhou、Xingzhi Zhang、Yinshuai Li、Qinhan Tan、Yinqian Zhang、Yajin Zhou、Rui Chang、Wenbo Shen
- 发表日期：2025-04-29
- 更新日期：2025-04-29
- 来源：arXiv
- 来源编号：2504.20934v1
- 研究类别：Processor and CPU Fuzzing、Microarchitecture Security、Fuzzing Methodology
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：3
- 论文页面：[http://arxiv.org/abs/2504.20934v1](http://arxiv.org/abs/2504.20934v1)
- PDF：[https://arxiv.org/pdf/2504.20934v1](https://arxiv.org/pdf/2504.20934v1)
- 分析模式：仅元数据分析

## 摘要

Transient execution vulnerabilities have emerged as a critical threat to modern processors. Hardware fuzzing testing techniques have recently shown promising results in discovering transient execution bugs in large-scale out-of-order processor designs. However, their poor microarchitectural controllability and observability prevent them from effectively and efficiently detecting transient execution vulnerabilities. This paper proposes DejaVuzz, a novel pre-silicon stage processor transient execution bug fuzzer. DejaVuzz utilizes two innovative operating primitives: dynamic swappable memory and differential information flow tracking, enabling more effective and efficient transient execution vulnerability detection. The dynamic swappable memory enables the isolation of different instruction streams within the same address space. Leveraging this capability, DejaVuzz generates targeted training for arbitrary transient windows and eliminates ineffective training, enabling efficient triggering of diverse transient windows. The differential information flow tracking aids in observing the propagation of sensitive data across the microarchitecture. Based on taints, DejaVuzz designs the taint coverage matrix to guide mutation and uses taint liveness annotations to identify exploitable leakages. Our evaluation shows that DejaVuzz outperforms the state-of-the-art fuzzer SpecDoctor, triggering more comprehensive transient windows with lower training overhead and achieving a 4.7x coverage improvement. And DejaVuzz also mitigates control flow over-tainting with acceptable overhead and identifies 5 previously undiscovered transient execution vulnerabilities (with 6 CVEs assigned) on BOOM and XiangShan.

## 研究问题

Transient execution vulnerabilities have emerged as a critical threat to modern processors. Hardware fuzzing testing techniques have recently shown promising results in discovering transient execution bugs in large-scale out-of-order processor designs. However, their poor microarchitectural controllability and observability prevent them from effectively and efficiently detecting transient execution vulnerabilities. This paper proposes DejaVuzz, a novel pre-silicon stage processor transient execution bug fuzzer. DejaVuzz utilizes two innovative operating primitives: dynamic swappable memory and differential information flow tracking, enabling more effective and efficient transient execution vulnerability detection. The dynamic swappable memory enables the isolation of different instruction streams within the same address space. Leveraging this capability, DejaVuzz generates targeted training for arbitrary transient windows and eliminates ineffective training, enabling efficient triggering of diverse transient windows. The differential information flow tracking aids in observing the propagation of sensitive data across the microarchitecture. Based on taints, DejaVuzz designs the taint coverage matrix to guide mutation and uses taint liveness annotations to identify exploitable leakages. Our evaluation shows that DejaVuzz outperforms the state-of-the-art fuzzer SpecDoctor, triggering more comprehensive transient windows with lower training overhead and achieving a 4.7x coverage improvement. And DejaVuzz also mitigates control flow over-tainting with acceptable overhead and identifies 5 previously undiscovered transient execution vulnerabilities (with 6 CVEs assigned) on BOOM and XiangShan.

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
