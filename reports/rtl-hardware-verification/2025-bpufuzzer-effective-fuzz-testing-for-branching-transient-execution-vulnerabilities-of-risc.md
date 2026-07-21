# BPUFuzzer: Effective Fuzz Testing for Branching Transient Execution Vulnerabilities of RISC-V CPU

## 基本信息

- 作者：Rihui Sun、Jin Wu、Hanyin Liu、Zikang Tao、Gang Qu、Dongsheng Wang、Yongqiang Lyu、Jian Dong
- 发表日期：2025-06-22
- 更新日期：
- 来源：Semantic Scholar
- 来源编号：a8e8ab9bd14cd9f2d4827fba1fdcacc67f75c477
- 研究类别：RISC-V Fuzzing 研究、微架构安全、RTL 与硬件验证、工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[https://doi.org/10.1109/DAC63849.2025.11133085](https://doi.org/10.1109/DAC63849.2025.11133085)
- PDF：[]()
- 分析模式：仅元数据分析

## 摘要

This paper presents BPUFuzzer, a fuzz testing tool for detecting branching transient execution vulnerabilities in CPU RTL design. BPUFuzzer addresses two key challenges: generating testcases that capture complex control flows, and extracting essential data from vast hardware states to guide testcase selection. Utilizing a control flow graph-based testcase generation strategy with anomaly detection and employing fitness and coverage metrics, BPUFuzzer works on testcases that cover broader program flows and deliberately selects testcases to discover transient execution vulnerabilities effectively. When applied on RISC-V Boom v3, BPUFuzzer uncovered more Spectre types than the state-of-the-arts, including a previously unidentified variant, named Spectre-LOOP.

## 研究问题

This paper presents BPUFuzzer, a fuzz testing tool for detecting branching transient execution vulnerabilities in CPU RTL design. BPUFuzzer addresses two key challenges: generating testcases that capture complex control flows, and extracting essential data from vast hardware states to guide testcase selection. Utilizing a control flow graph-based testcase generation strategy with anomaly detection and employing fitness and coverage metrics, BPUFuzzer works on testcases that cover broader program flows and deliberately selects testcases to discover transient execution vulnerabilities effectively. When applied on RISC-V Boom v3, BPUFuzzer uncovered more Spectre types than the state-of-the-arts, including a previously unidentified variant, named Spectre-LOOP.

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
