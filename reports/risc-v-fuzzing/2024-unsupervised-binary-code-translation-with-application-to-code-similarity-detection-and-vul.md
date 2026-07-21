# Unsupervised Binary Code Translation with Application to Code Similarity Detection and Vulnerability Discovery

## 基本信息

- 作者：Iftakhar Ahmad、Lannan Luo
- 发表日期：2024-04-29
- 更新日期：2024-04-29
- 来源：arXiv
- 来源编号：2404.19025v1
- 研究类别：RISC-V Fuzzing 研究
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2404.19025v1](http://arxiv.org/abs/2404.19025v1)
- PDF：[https://arxiv.org/pdf/2404.19025v1](https://arxiv.org/pdf/2404.19025v1)
- 分析模式：仅元数据分析

## 摘要

Binary code analysis has immense importance in the research domain of software security. Today, software is very often compiled for various Instruction Set Architectures (ISAs). As a result, cross-architecture binary code analysis has become an emerging problem. Recently, deep learning-based binary analysis has shown promising success. It is widely known that training a deep learning model requires a massive amount of data. However, for some low-resource ISAs, an adequate amount of data is hard to find, preventing deep learning from being widely adopted for binary analysis. To overcome the data scarcity problem and facilitate cross-architecture binary code analysis, we propose to apply the ideas and techniques in Neural Machine Translation (NMT) to binary code analysis. Our insight is that a binary, after disassembly, is represented in some assembly language. Given a binary in a low-resource ISA, we translate it to a binary in a high-resource ISA (e.g., x86). Then we can use a model that has been trained on the high-resource ISA to test the translated binary. We have implemented the model called UNSUPERBINTRANS, and conducted experiments to evaluate its performance. Specifically, we conducted two downstream tasks, including code similarity detection and vulnerability discovery. In both tasks, we achieved high accuracies.

## 研究问题

Binary code analysis has immense importance in the research domain of software security. Today, software is very often compiled for various Instruction Set Architectures (ISAs). As a result, cross-architecture binary code analysis has become an emerging problem. Recently, deep learning-based binary analysis has shown promising success. It is widely known that training a deep learning model requires a massive amount of data. However, for some low-resource ISAs, an adequate amount of data is hard to find, preventing deep learning from being widely adopted for binary analysis. To overcome the data scarcity problem and facilitate cross-architecture binary code analysis, we propose to apply the ideas and techniques in Neural Machine Translation (NMT) to binary code analysis. Our insight is that a binary, after disassembly, is represented in some assembly language. Given a binary in a low-resource ISA, we translate it to a binary in a high-resource ISA (e.g., x86). Then we can use a model that has been trained on the high-resource ISA to test the translated binary. We have implemented the model called UNSUPERBINTRANS, and conducted experiments to evaluate its performance. Specifically, we conducted two downstream tasks, including code similarity detection and vulnerability discovery. In both tasks, we achieved high accuracies.

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
