# Protocol-Aware Firmware Rehosting for Effective Fuzzing of Embedded Network Stacks

## 基本信息

- 作者：Moritz Bley、Tobias Scharnowski、Simon Wörner、Moritz Schloegel、Thorsten Holz
- 发表日期：2025-09-17
- 更新日期：2025-09-17
- 来源：arXiv
- 来源编号：2509.13740v1
- 研究类别：工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2509.13740v1](http://arxiv.org/abs/2509.13740v1)
- PDF：[https://arxiv.org/pdf/2509.13740v1](https://arxiv.org/pdf/2509.13740v1)
- 分析模式：仅元数据分析

## 摘要

One of the biggest attack surfaces of embedded systems is their network interfaces, which enable communication with other devices. Unlike their general-purpose counterparts, embedded systems are designed for specialized use cases, resulting in unique and diverse communication stacks. Unfortunately, current approaches for evaluating the security of these embedded network stacks require manual effort or access to hardware, and they generally focus only on small parts of the embedded system. A promising alternative is firmware rehosting, which enables fuzz testing of the entire firmware by generically emulating the physical hardware. However, existing rehosting methods often struggle to meaningfully explore network stacks due to their complex, multi-layered input formats. This limits their ability to uncover deeply nested software faults. To address this problem, we introduce a novel method to automatically detect and handle the use of network protocols in firmware called Pemu. By automatically deducing the available network protocols, Pemu can transparently generate valid network packets that encapsulate fuzzing data, allowing the fuzzing input to flow directly into deeper layers of the firmware logic. Our approach thus enables a deeper, more targeted, and layer-by-layer analysis of firmware components that were previously difficult or impossible to test. Our evaluation demonstrates that Pemu consistently improves the code coverage of three existing rehosting tools for embedded network stacks. Furthermore, our fuzzer rediscovered several known vulnerabilities and identified five previously unknown software faults, highlighting its effectiveness in uncovering deeply nested bugs in network-exposed code.

## 研究问题

One of the biggest attack surfaces of embedded systems is their network interfaces, which enable communication with other devices. Unlike their general-purpose counterparts, embedded systems are designed for specialized use cases, resulting in unique and diverse communication stacks. Unfortunately, current approaches for evaluating the security of these embedded network stacks require manual effort or access to hardware, and they generally focus only on small parts of the embedded system. A promising alternative is firmware rehosting, which enables fuzz testing of the entire firmware by generically emulating the physical hardware. However, existing rehosting methods often struggle to meaningfully explore network stacks due to their complex, multi-layered input formats. This limits their ability to uncover deeply nested software faults. To address this problem, we introduce a novel method to automatically detect and handle the use of network protocols in firmware called Pemu. By automatically deducing the available network protocols, Pemu can transparently generate valid network packets that encapsulate fuzzing data, allowing the fuzzing input to flow directly into deeper layers of the firmware logic. Our approach thus enables a deeper, more targeted, and layer-by-layer analysis of firmware components that were previously difficult or impossible to test. Our evaluation demonstrates that Pemu consistently improves the code coverage of three existing rehosting tools for embedded network stacks. Furthermore, our fuzzer rediscovered several known vulnerabilities and identified five previously unknown software faults, highlighting its effectiveness in uncovering deeply nested bugs in network-exposed code.

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
