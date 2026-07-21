# Memory DisOrder: Memory Re-orderings as a Timerless Side-channel

## 基本信息

- 作者：Sean Siddens、Sanya Srivastava、Reese Levine、Josiah Dykstra、Tyler Sorensen
- 发表日期：2026-01-13
- 更新日期：2026-01-13
- 来源：arXiv
- 来源编号：2601.08770v1
- 研究类别：未分类
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：3
- 论文页面：[http://arxiv.org/abs/2601.08770v1](http://arxiv.org/abs/2601.08770v1)
- PDF：[https://arxiv.org/pdf/2601.08770v1](https://arxiv.org/pdf/2601.08770v1)
- 分析模式：仅元数据分析

## 摘要

To improve efficiency, nearly all parallel processing units (CPUs and GPUs) implement relaxed memory models in which memory operations may be re-ordered, i.e., executed out-of-order. Prior testing work in this area found that memory re-orderings are observed more frequently when other cores are active, e.g., stressing the memory system, which likely triggers aggressive hardware optimizations. In this work, we present Memory DisOrder: a timerless side-channel that uses memory re-orderings to infer activity on other processes. We first perform a fuzzing campaign and show that many mainstream processors (X86/Arm/Apple CPUs, NVIDIA/AMD/Apple GPUs) are susceptible to cross-process signals. We then show how the vulnerability can be used to implement classic attacks, including a covert channel, achieving up to 16 bits/second with 95% accuracy on an Apple M3 GPU, and application fingerprinting, achieving reliable closed-world DNN architecture fingerprinting on several CPUs and an Apple M3 GPU. Finally, we explore how low-level system details can be exploited to increase re-orderings, showing the potential for a covert channel to achieve nearly 30K bits/second on X86 CPUs. More precise attacks can likely be developed as the vulnerability becomes better understood.

## 研究问题

To improve efficiency, nearly all parallel processing units (CPUs and GPUs) implement relaxed memory models in which memory operations may be re-ordered, i.e., executed out-of-order. Prior testing work in this area found that memory re-orderings are observed more frequently when other cores are active, e.g., stressing the memory system, which likely triggers aggressive hardware optimizations. In this work, we present Memory DisOrder: a timerless side-channel that uses memory re-orderings to infer activity on other processes. We first perform a fuzzing campaign and show that many mainstream processors (X86/Arm/Apple CPUs, NVIDIA/AMD/Apple GPUs) are susceptible to cross-process signals. We then show how the vulnerability can be used to implement classic attacks, including a covert channel, achieving up to 16 bits/second with 95% accuracy on an Apple M3 GPU, and application fingerprinting, achieving reliable closed-world DNN architecture fingerprinting on several CPUs and an Apple M3 GPU. Finally, we explore how low-level system details can be exploited to increase re-orderings, showing the potential for a covert channel to achieve nearly 30K bits/second on X86 CPUs. More precise attacks can likely be developed as the vulnerability becomes better understood.

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
