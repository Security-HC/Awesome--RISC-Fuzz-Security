# Sharing is leaking: blocking transient-execution attacks with core-gapped confidential VMs

## 基本信息

- 作者：Charly Castes、Andrew Baumann
- 发表日期：2024-04-27
- 更新日期：
- 来源：Semantic Scholar
- 来源编号：2ca723a0bd93622ee4e7cae881bbc8bc724620ba
- 研究类别：微架构安全
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[https://doi.org/10.1145/3622781.3674190](https://doi.org/10.1145/3622781.3674190)
- PDF：[https://dl.acm.org/doi/pdf/10.1145/3622781.3674190](https://dl.acm.org/doi/pdf/10.1145/3622781.3674190)
- 分析模式：仅元数据分析

## 摘要

Confidential VMs on platforms such as Intel TDX, AMD SEV and Arm CCA promise greater security for cloud users against even a hypervisor-level attacker, but this promise has been shattered by repeated transient-execution vulnerabilities and CPU bugs. At the root of this problem lies the need to multiplex CPU cores with all their complex microarchitectural state among distrusting entities, with an untrusted hypervisor in control of the multiplexing. We propose core-gapped confidential VMs, a set of software-only modifications that ensure that no distrusting code shares a core, thus removing all same-core side-channels and transient-execution vulnerabilities from the guest's TCB. We present an Arm-based prototype along with a performance evaluation showing that, not only does core-gapping offer performance competitive with non-confidential VMs, the greater locality achieved by avoiding shared cores can even improve performance for CPU-intensive workloads.

## 研究问题

Confidential VMs on platforms such as Intel TDX, AMD SEV and Arm CCA promise greater security for cloud users against even a hypervisor-level attacker, but this promise has been shattered by repeated transient-execution vulnerabilities and CPU bugs. At the root of this problem lies the need to multiplex CPU cores with all their complex microarchitectural state among distrusting entities, with an untrusted hypervisor in control of the multiplexing. We propose core-gapped confidential VMs, a set of software-only modifications that ensure that no distrusting code shares a core, thus removing all same-core side-channels and transient-execution vulnerabilities from the guest's TCB. We present an Arm-based prototype along with a performance evaluation showing that, not only does core-gapping offer performance competitive with non-confidential VMs, the greater locality achieved by avoiding shared cores can even improve performance for CPU-intensive workloads.

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
