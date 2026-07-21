# HeisenTrojans: They Are Not There Until They Are Triggered

## 基本信息

- 作者：Akshita Reddy Mavurapu、Haoqi Shan、Xiaolong Guo、Orlando Arias、Dean Sullivan
- 发表日期：2023-12-20
- 更新日期：2023-12-20
- 来源：arXiv
- 来源编号：2312.13190v1
- 研究类别：Tools and Benchmarks
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2312.13190v1](http://arxiv.org/abs/2312.13190v1)
- PDF：[https://arxiv.org/pdf/2312.13190v1](https://arxiv.org/pdf/2312.13190v1)
- 分析模式：仅元数据分析

## 摘要

The hardware security community has made significant advances in detecting Hardware Trojan vulnerabilities using software fuzzing-inspired automated analysis. However, the Electronic Design Automation (EDA) code base itself remains under-examined by the same techniques. Our experiments in fuzzing EDA tools demonstrate that, indeed, they are prone to software bugs. As a consequence, this paper unveils HeisenTrojan attacks, a new hardware attack that does not generate harmful hardware, but rather, exploits software vulnerabilities in the EDA tools themselves. A key feature of HeisenTrojan attacks is that they are capable of deploying a malicious payload on the system hosting the EDA tools without triggering verification tools because HeisenTrojan attacks do not rely on superfluous or malicious hardware that would otherwise be noticeable. The aim of a HeisenTrojan attack is to execute arbitrary code on the system on which the vulnerable EDA tool is hosted, thereby establishing a permanent presence and providing a beachhead for intrusion into that system. Our analysis reveals 83% of the EDA tools analyzed have exploitable bugs. In what follows, we demonstrate an end- to-end attack and provide analysis on the existing capabilities of fuzzers to find HeisenTrojan attacks in order to emphasize their practicality and the need to secure EDA tools against them.

## 研究问题

The hardware security community has made significant advances in detecting Hardware Trojan vulnerabilities using software fuzzing-inspired automated analysis. However, the Electronic Design Automation (EDA) code base itself remains under-examined by the same techniques. Our experiments in fuzzing EDA tools demonstrate that, indeed, they are prone to software bugs. As a consequence, this paper unveils HeisenTrojan attacks, a new hardware attack that does not generate harmful hardware, but rather, exploits software vulnerabilities in the EDA tools themselves. A key feature of HeisenTrojan attacks is that they are capable of deploying a malicious payload on the system hosting the EDA tools without triggering verification tools because HeisenTrojan attacks do not rely on superfluous or malicious hardware that would otherwise be noticeable. The aim of a HeisenTrojan attack is to execute arbitrary code on the system on which the vulnerable EDA tool is hosted, thereby establishing a permanent presence and providing a beachhead for intrusion into that system. Our analysis reveals 83% of the EDA tools analyzed have exploitable bugs. In what follows, we demonstrate an end- to-end attack and provide analysis on the existing capabilities of fuzzers to find HeisenTrojan attacks in order to emphasize their practicality and the need to secure EDA tools against them.

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
