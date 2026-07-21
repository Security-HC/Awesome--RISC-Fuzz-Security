# Discovery of Endianness and Instruction Size Characteristics in Binary Programs from Unknown Instruction Set Architectures

## 基本信息

- 作者：Joachim Andreassen、Donn Morrison
- 发表日期：2024-10-28
- 更新日期：2024-10-28
- 来源：arXiv
- 来源编号：2410.21558v1
- 研究类别：RISC-V Fuzzing、Tools and Benchmarks
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2410.21558v1](http://arxiv.org/abs/2410.21558v1)
- PDF：[https://arxiv.org/pdf/2410.21558v1](https://arxiv.org/pdf/2410.21558v1)
- 分析模式：仅元数据分析

## 摘要

We study the problem of streamlining reverse engineering (RE) of binary programs from unknown instruction set architectures (ISA). We focus on two fundamental ISA characteristics to beginning the RE process: identification of endianness and whether the instruction width is a fixed or variable. For ISAs with a fixed instruction width, we also present methods for estimating the width. In addition to advancing research in software RE, our work can also be seen as a first step in hardware reverse engineering, because endianness and instruction format describe intrinsic characteristics of the underlying ISA. We detail our efforts at feature engineering and perform experiments using a variety of machine learning models on two datasets of architectures using Leave-One-Group-Out-Cross-Validation to simulate conditions where the tested ISA is unknown during model training. We use bigram-based features for endianness detection and the autocorrelation function, commonly used in signal processing applications, for differentiation between fixed- and variable-width instruction sizes. A collection of classifiers from the machine learning library scikit-learn are used in the experiments to research these features. Initial results are promising, with accuracy of endianness detection at 99.4%, fixed- versus variable-width instruction size at 86.0%, and detection of fixed instruction sizes at 88.0%.

## 研究问题

We study the problem of streamlining reverse engineering (RE) of binary programs from unknown instruction set architectures (ISA). We focus on two fundamental ISA characteristics to beginning the RE process: identification of endianness and whether the instruction width is a fixed or variable. For ISAs with a fixed instruction width, we also present methods for estimating the width. In addition to advancing research in software RE, our work can also be seen as a first step in hardware reverse engineering, because endianness and instruction format describe intrinsic characteristics of the underlying ISA. We detail our efforts at feature engineering and perform experiments using a variety of machine learning models on two datasets of architectures using Leave-One-Group-Out-Cross-Validation to simulate conditions where the tested ISA is unknown during model training. We use bigram-based features for endianness detection and the autocorrelation function, commonly used in signal processing applications, for differentiation between fixed- and variable-width instruction sizes. A collection of classifiers from the machine learning library scikit-learn are used in the experiments to research these features. Initial results are promising, with accuracy of endianness detection at 99.4%, fixed- versus variable-width instruction size at 86.0%, and detection of fixed instruction sizes at 88.0%.

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
