# Automatically Detecting Heterogeneous Bugs in High-Performance Computing Scientific Software

## 基本信息

- 作者：Matthew Davis、Aakash Kulkarni、Ziyan Chen、Yunhan Qiao、Christopher Terrazas、Manish Motwani
- 发表日期：2025-01-16
- 更新日期：2025-01-16
- 来源：arXiv
- 来源编号：2501.09872v1
- 研究类别：RTL and Hardware Verification、Fuzzing Methodology
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2501.09872v1](http://arxiv.org/abs/2501.09872v1)
- PDF：[https://arxiv.org/pdf/2501.09872v1](https://arxiv.org/pdf/2501.09872v1)
- 分析模式：仅元数据分析

## 摘要

Scientific advancements rely on high-performance computing (HPC) applications that model real-world phenomena through simulations. These applications process vast amounts of data on specialized accelerators (eg., GPUs) using special libraries. Heterogeneous bugs occur in these applications when managing data movement across different platforms, such as CPUs and GPUs, leading to divergent behavior when using heterogeneous platforms compared to using only CPUs. Existing software testing techniques often fail to detect such bugs because either they do not account for platform-specific characteristics or target specific platforms. To address this problem, we present HeteroBugDetect, an automated approach to detect platform-dependent heterogeneous bugs in HPC scientific applications. HeteroBugDetect combines natural-language processing, off-target testing, custom fuzzing, and differential testing to provide an end-to-end solution for detecting platform-specific bugs in scientific applications. We evaluate HeteroBugDetect on LAMMPS, a molecular dynamics simulator, where it detected multiple heterogeneous bugs, enhancing its reliability across diverse HPC environments.

## 研究问题

Scientific advancements rely on high-performance computing (HPC) applications that model real-world phenomena through simulations. These applications process vast amounts of data on specialized accelerators (eg., GPUs) using special libraries. Heterogeneous bugs occur in these applications when managing data movement across different platforms, such as CPUs and GPUs, leading to divergent behavior when using heterogeneous platforms compared to using only CPUs. Existing software testing techniques often fail to detect such bugs because either they do not account for platform-specific characteristics or target specific platforms. To address this problem, we present HeteroBugDetect, an automated approach to detect platform-dependent heterogeneous bugs in HPC scientific applications. HeteroBugDetect combines natural-language processing, off-target testing, custom fuzzing, and differential testing to provide an end-to-end solution for detecting platform-specific bugs in scientific applications. We evaluate HeteroBugDetect on LAMMPS, a molecular dynamics simulator, where it detected multiple heterogeneous bugs, enhancing its reliability across diverse HPC environments.

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
