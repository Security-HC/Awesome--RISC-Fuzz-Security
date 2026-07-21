# Osiris: Automated Discovery of Microarchitectural Side Channels

## 基本信息

- 作者：Daniel Weber、Ahmad Ibrahim、Hamed Nemati、Michael Schwarz、Christian Rossow
- 发表日期：2021-06-07
- 更新日期：2021-06-07
- 来源：arXiv
- 来源编号：2106.03470v1
- 研究类别：微架构安全、工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：2
- 论文页面：[http://arxiv.org/abs/2106.03470v1](http://arxiv.org/abs/2106.03470v1)
- PDF：[https://arxiv.org/pdf/2106.03470v1](https://arxiv.org/pdf/2106.03470v1)
- 分析模式：仅元数据分析

## 摘要

In the last years, a series of side channels have been discovered on CPUs. These side channels have been used in powerful attacks, e.g., on cryptographic implementations, or as building blocks in transient-execution attacks such as Spectre or Meltdown. However, in many cases, discovering side channels is still a tedious manual process. In this paper, we present Osiris, a fuzzing-based framework to automatically discover microarchitectural side channels. Based on a machine-readable specification of a CPU's ISA, Osiris generates instruction-sequence triples and automatically tests whether they form a timing-based side channel. Furthermore, Osiris evaluates their usability as a side channel in transient-execution attacks, i.e., as the microarchitectural encoding for attacks like Spectre. In total, we discover four novel timing-based side channels on Intel and AMD CPUs. Based on these side channels, we demonstrate exploitation in three case studies. We show that our microarchitectural KASLR break using non-temporal loads, FlushConflict, even works on the new Intel Ice Lake and Comet Lake microarchitectures. We present a cross-core cross-VM covert channel that is not relying on the memory subsystem and transmits up to 1 kbit/s. We demonstrate this channel on the AWS cloud, showing that it is stealthy and noise resistant. Finally, we demonstrate Stream+Reload, a covert channel for transient-execution attacks that, on average, allows leaking 7.83 bytes within a transient window, improving state-of-the-art attacks that only leak up to 3 bytes.

## 研究问题

In the last years, a series of side channels have been discovered on CPUs. These side channels have been used in powerful attacks, e.g., on cryptographic implementations, or as building blocks in transient-execution attacks such as Spectre or Meltdown. However, in many cases, discovering side channels is still a tedious manual process. In this paper, we present Osiris, a fuzzing-based framework to automatically discover microarchitectural side channels. Based on a machine-readable specification of a CPU's ISA, Osiris generates instruction-sequence triples and automatically tests whether they form a timing-based side channel. Furthermore, Osiris evaluates their usability as a side channel in transient-execution attacks, i.e., as the microarchitectural encoding for attacks like Spectre. In total, we discover four novel timing-based side channels on Intel and AMD CPUs. Based on these side channels, we demonstrate exploitation in three case studies. We show that our microarchitectural KASLR break using non-temporal loads, FlushConflict, even works on the new Intel Ice Lake and Comet Lake microarchitectures. We present a cross-core cross-VM covert channel that is not relying on the memory subsystem and transmits up to 1 kbit/s. We demonstrate this channel on the AWS cloud, showing that it is stealthy and noise resistant. Finally, we demonstrate Stream+Reload, a covert channel for transient-execution attacks that, on average, allows leaking 7.83 bytes within a transient window, improving state-of-the-art attacks that only leak up to 3 bytes.

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
