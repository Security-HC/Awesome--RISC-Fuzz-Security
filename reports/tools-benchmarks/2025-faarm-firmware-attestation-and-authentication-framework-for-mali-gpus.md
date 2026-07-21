# FAARM: Firmware Attestation and Authentication Framework for Mali GPUs

## 基本信息

- 作者：Md. Mehedi Hasan
- 发表日期：2025-10-26
- 更新日期：2025-10-26
- 来源：arXiv
- 来源编号：2510.22566v1
- 研究类别：工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2510.22566v1](http://arxiv.org/abs/2510.22566v1)
- PDF：[https://arxiv.org/pdf/2510.22566v1](https://arxiv.org/pdf/2510.22566v1)
- 分析模式：仅元数据分析

## 摘要

Recent work has revealed MOLE, the first practical attack to compromise GPU Trusted Execution Environments (TEEs), by injecting malicious firmware into the embedded Microcontroller Unit (MCU) of Arm Mali GPUs. By exploiting the absence of cryptographic verification during initialization, adversaries with kernel privileges can bypass memory protections, exfiltrate sensitive data at over 40 MB/s, and tamper with inference results, all with negligible runtime overhead. This attack surface affects commodity mobile SoCs and cloud accelerators, exposing a critical firmware-level trust gap in existing GPU TEE designs. To address this gap, this paper presents FAARM, a lightweight Firmware Attestation and Authentication framework that prevents MOLE-style firmware subversion. FAARM integrates digital signature verification at the EL3 secure monitor using vendor-signed firmware bundles and an on-device public key anchor. At boot, EL3 verifies firmware integrity and authenticity, enforces version checks, and locks the firmware region, eliminating both pre-verification and time-of-check-to-time-of-use (TOCTOU) attack vectors. We implement FAARM as a software-only prototype on a Mali GPU testbed, using a Google Colab-based emulation framework that models the firmware signing process, the EL1 to EL3 load path, and secure memory configuration. FAARM reliably detects and blocks malicious firmware injections, rejecting tampered images before use and denying overwrite attempts after attestation. Firmware verification incurs only 1.34 ms latency on average, demonstrating that strong security can be achieved with negligible overhead. FAARM thus closes a fundamental gap in shim-based GPU TEEs, providing a practical, deployable defense that raises the security baseline for both mobile and cloud GPU deployments.

## 研究问题

Recent work has revealed MOLE, the first practical attack to compromise GPU Trusted Execution Environments (TEEs), by injecting malicious firmware into the embedded Microcontroller Unit (MCU) of Arm Mali GPUs. By exploiting the absence of cryptographic verification during initialization, adversaries with kernel privileges can bypass memory protections, exfiltrate sensitive data at over 40 MB/s, and tamper with inference results, all with negligible runtime overhead. This attack surface affects commodity mobile SoCs and cloud accelerators, exposing a critical firmware-level trust gap in existing GPU TEE designs. To address this gap, this paper presents FAARM, a lightweight Firmware Attestation and Authentication framework that prevents MOLE-style firmware subversion. FAARM integrates digital signature verification at the EL3 secure monitor using vendor-signed firmware bundles and an on-device public key anchor. At boot, EL3 verifies firmware integrity and authenticity, enforces version checks, and locks the firmware region, eliminating both pre-verification and time-of-check-to-time-of-use (TOCTOU) attack vectors. We implement FAARM as a software-only prototype on a Mali GPU testbed, using a Google Colab-based emulation framework that models the firmware signing process, the EL1 to EL3 load path, and secure memory configuration. FAARM reliably detects and blocks malicious firmware injections, rejecting tampered images before use and denying overwrite attempts after attestation. Firmware verification incurs only 1.34 ms latency on average, demonstrating that strong security can be achieved with negligible overhead. FAARM thus closes a fundamental gap in shim-based GPU TEEs, providing a practical, deployable defense that raises the security baseline for both mobile and cloud GPU deployments.

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
