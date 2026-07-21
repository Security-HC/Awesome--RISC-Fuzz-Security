# CRAFT: Characterizing and Root-Causing Fault Injection Threats at Pre-Silicon

## 基本信息

- 作者：Arsalan Ali Malik、Harshvadan Mihir、Aydin Aysu
- 发表日期：2025-03-05
- 更新日期：2025-10-22
- 来源：arXiv
- 来源编号：2503.03877v4
- 研究类别：RISC-V Fuzzing 研究、微架构安全、工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2503.03877v4](http://arxiv.org/abs/2503.03877v4)
- PDF：[https://arxiv.org/pdf/2503.03877v4](https://arxiv.org/pdf/2503.03877v4)
- 分析模式：仅元数据分析

## 摘要

Fault injection attacks (FIA) pose significant security threats to embedded systems as they exploit weaknesses across multiple layers, including system software, instruction set architecture (ISA), microarchitecture, and physical hardware. Early detection and understanding of how physical faults propagate to system-level behavior are essential to safeguarding cyberinfrastructure. This work introduces CRAFT, a framework that combines pre-silicon analysis with post-silicon validation to systematically uncover and analyze fault injection vulnerabilities. Our study, conducted on a RISC-V soft-core processor (cv32e40x) reveals two novel vulnerabilities. First, we demonstrate a method to induce instruction skips by glitching the clock (single-glitch attack), which prevents critical values from being loaded from memory, thus disrupting program execution. Second, we show a technique that converts a fetched legal instruction into an illegal one mid-execution, diverting control flow in a manner exploitable by attackers. Notably, we identified a specific timing window in which the processor fails to detect these illegal control-flow diversions, allowing silent, undetected corruption of the program state. By simulating 9248 FIA scenarios at pre-silicon and conducting root-cause analysis of the RISC-V pipeline, we trace the faults to a previously unreported vulnerability in a pipeline register shared between the instruction fetch and decode stages. Our approach reduced the search space for post-silicon experiments by 97.31%, showing pre-silicon advantages for post-silicon testing. Finally, we validate our identified exploit cases on real hardware (FPGA).

## 研究问题

Fault injection attacks (FIA) pose significant security threats to embedded systems as they exploit weaknesses across multiple layers, including system software, instruction set architecture (ISA), microarchitecture, and physical hardware. Early detection and understanding of how physical faults propagate to system-level behavior are essential to safeguarding cyberinfrastructure. This work introduces CRAFT, a framework that combines pre-silicon analysis with post-silicon validation to systematically uncover and analyze fault injection vulnerabilities. Our study, conducted on a RISC-V soft-core processor (cv32e40x) reveals two novel vulnerabilities. First, we demonstrate a method to induce instruction skips by glitching the clock (single-glitch attack), which prevents critical values from being loaded from memory, thus disrupting program execution. Second, we show a technique that converts a fetched legal instruction into an illegal one mid-execution, diverting control flow in a manner exploitable by attackers. Notably, we identified a specific timing window in which the processor fails to detect these illegal control-flow diversions, allowing silent, undetected corruption of the program state. By simulating 9248 FIA scenarios at pre-silicon and conducting root-cause analysis of the RISC-V pipeline, we trace the faults to a previously unreported vulnerability in a pipeline register shared between the instruction fetch and decode stages. Our approach reduced the search space for post-silicon experiments by 97.31%, showing pre-silicon advantages for post-silicon testing. Finally, we validate our identified exploit cases on real hardware (FPGA).

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
