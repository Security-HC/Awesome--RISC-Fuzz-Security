# A Multi-stage Error Diagnosis for APB Transaction

## 基本信息

- 作者：Cheng-Yang Tsai、Tzu-Wei Huang、Jen-Wei Shih、I-Hsiang Wang、Yu-Cheng Lin、Rung-Bin Lin
- 发表日期：2025-09-03
- 更新日期：2025-09-03
- 来源：arXiv
- 来源编号：2509.03554v1
- 研究类别：Tools and Benchmarks
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2509.03554v1](http://arxiv.org/abs/2509.03554v1)
- PDF：[https://arxiv.org/pdf/2509.03554v1](https://arxiv.org/pdf/2509.03554v1)
- 分析模式：仅元数据分析

## 摘要

Functional verification and debugging are critical bottlenecks in modern System-on-Chip (SoC) design, with manual detection of Advanced Peripheral Bus (APB) transaction errors in large Value Change Dump (VCD) files being inefficient and error-prone. Addressing the 2025 ICCAD Contest Problem D, this study proposes an automated error diagnosis framework using a hierarchical Random Forest-based architecture. The multi-stage error diagnosis employs four pre-trained binary classifiers to sequentially detect Out-of-Range Access, Address Corruption, and Data Corruption errors, prioritizing high-certainty address-related faults before tackling complex data errors to enhance efficiency. Experimental results show an overall accuracy of 91.36%, with near-perfect precision and recall for address errors and robust performance for data errors. Although the final results of the ICCAD 2025 CAD Contest are yet to be announced as of the submission date, our team achieved first place in the beta stage, highlighting the method's competitive strength. This research validates the potential of hierarchical machine learning as a powerful automated tool for hardware debugging in Electronic Design Automation (EDA).

## 研究问题

Functional verification and debugging are critical bottlenecks in modern System-on-Chip (SoC) design, with manual detection of Advanced Peripheral Bus (APB) transaction errors in large Value Change Dump (VCD) files being inefficient and error-prone. Addressing the 2025 ICCAD Contest Problem D, this study proposes an automated error diagnosis framework using a hierarchical Random Forest-based architecture. The multi-stage error diagnosis employs four pre-trained binary classifiers to sequentially detect Out-of-Range Access, Address Corruption, and Data Corruption errors, prioritizing high-certainty address-related faults before tackling complex data errors to enhance efficiency. Experimental results show an overall accuracy of 91.36%, with near-perfect precision and recall for address errors and robust performance for data errors. Although the final results of the ICCAD 2025 CAD Contest are yet to be announced as of the submission date, our team achieved first place in the beta stage, highlighting the method's competitive strength. This research validates the potential of hierarchical machine learning as a powerful automated tool for hardware debugging in Electronic Design Automation (EDA).

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
