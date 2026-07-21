# Challenges and Design Considerations for Finding CUDA Bugs Through GPU-Native Fuzzing

## 基本信息

- 作者：Mingkai Li、Joseph Devietti、Suman Jana、Tanvir Ahmed Khan
- 发表日期：2026-03-05
- 更新日期：2026-03-05
- 来源：arXiv
- 来源编号：2603.05725v1
- 研究类别：未分类
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：2
- 论文页面：[http://arxiv.org/abs/2603.05725v1](http://arxiv.org/abs/2603.05725v1)
- PDF：[https://arxiv.org/pdf/2603.05725v1](https://arxiv.org/pdf/2603.05725v1)
- 分析模式：仅元数据分析

## 摘要

Modern computing is shifting from homogeneous CPU-centric systems to heterogeneous systems with closely integrated CPUs and GPUs. While the CPU software stack has benefited from decades of memory safety hardening, the GPU software stack remains dangerously immature. This discrepancy presents a critical ethical challenge: the world's most advanced AI and scientific workloads are increasingly deployed on vulnerable hardware components. In this paper, we study the key challenges of ensuring memory safety on heterogeneous systems. We show that, while the number of exploitable bugs in heterogeneous systems rises every year, current mitigation methods often rely on unfaithful translations, i.e., converting GPU programs to run on CPUs for testing, which fails to capture the architectural differences between CPUs and GPUs. We argue that the faithfulness of the program behavior is at the core of secure and reliable heterogeneous systems design. To ensure faithfulness, we discuss several design considerations of a GPU-native fuzzing pipeline for CUDA programs.

## 研究问题

Modern computing is shifting from homogeneous CPU-centric systems to heterogeneous systems with closely integrated CPUs and GPUs. While the CPU software stack has benefited from decades of memory safety hardening, the GPU software stack remains dangerously immature. This discrepancy presents a critical ethical challenge: the world's most advanced AI and scientific workloads are increasingly deployed on vulnerable hardware components. In this paper, we study the key challenges of ensuring memory safety on heterogeneous systems. We show that, while the number of exploitable bugs in heterogeneous systems rises every year, current mitigation methods often rely on unfaithful translations, i.e., converting GPU programs to run on CPUs for testing, which fails to capture the architectural differences between CPUs and GPUs. We argue that the faithfulness of the program behavior is at the core of secure and reliable heterogeneous systems design. To ensure faithfulness, we discuss several design considerations of a GPU-native fuzzing pipeline for CUDA programs.

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
