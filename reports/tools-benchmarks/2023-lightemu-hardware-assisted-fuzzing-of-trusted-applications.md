# LightEMU: Hardware Assisted Fuzzing of Trusted Applications

## 基本信息

- 作者：Haoqi Shan、Sravani Nissankararao、Yujia Liu、Moyao Huang、Shuo Wang、Yier Jin、Dean Sullivan
- 发表日期：2023-11-16
- 更新日期：2023-11-16
- 来源：arXiv
- 来源编号：2311.09532v1
- 研究类别：工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2311.09532v1](http://arxiv.org/abs/2311.09532v1)
- PDF：[https://arxiv.org/pdf/2311.09532v1](https://arxiv.org/pdf/2311.09532v1)
- 分析模式：仅元数据分析

## 摘要

Trusted Execution Environments (TEEs) are deployed in many CPU designs because of the confidentiality and integrity guarantees they provide. ARM TrustZone is a TEE extensively deployed on smart phones, IoT devices, and notebooks. Specifically, TrustZone is used to separate code execution and data into two worlds, normal world and secure world. However, this separation inherently prevents traditional fuzzing approaches which rely upon coverage-guided feedback and existing fuzzing research is, therefore, extremely limited. In this paper, we present a native and generic method to perform efficient and scalable feedback-driven fuzzing on Trusted Applications (TAs) using ARM CoreSight. We propose LightEMU, a novel fuzzing framework that allows us to fuzz TAs by decoupling them from relied TEE. We argue that LightEMU is a promising first-stage approach for rapidly discovering TA vulnerabilities prior to investing effort in whole system TEE evaluation precisely because the majority of publicly disclosed TrustZone bugs reside in the TA code itself. We implement LightEMU and adapt it to Teegris, Trusty, OP-TEE and QSEE and evaluate 8 real-world TAs while triggering 3 unique crashes and achieving x10 time speedup when fuzzing TAs using the state-of-the-art TrustZone fuzzing framework.

## 研究问题

Trusted Execution Environments (TEEs) are deployed in many CPU designs because of the confidentiality and integrity guarantees they provide. ARM TrustZone is a TEE extensively deployed on smart phones, IoT devices, and notebooks. Specifically, TrustZone is used to separate code execution and data into two worlds, normal world and secure world. However, this separation inherently prevents traditional fuzzing approaches which rely upon coverage-guided feedback and existing fuzzing research is, therefore, extremely limited. In this paper, we present a native and generic method to perform efficient and scalable feedback-driven fuzzing on Trusted Applications (TAs) using ARM CoreSight. We propose LightEMU, a novel fuzzing framework that allows us to fuzz TAs by decoupling them from relied TEE. We argue that LightEMU is a promising first-stage approach for rapidly discovering TA vulnerabilities prior to investing effort in whole system TEE evaluation precisely because the majority of publicly disclosed TrustZone bugs reside in the TA code itself. We implement LightEMU and adapt it to Teegris, Trusty, OP-TEE and QSEE and evaluate 8 real-world TAs while triggering 3 unique crashes and achieving x10 time speedup when fuzzing TAs using the state-of-the-art TrustZone fuzzing framework.

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
