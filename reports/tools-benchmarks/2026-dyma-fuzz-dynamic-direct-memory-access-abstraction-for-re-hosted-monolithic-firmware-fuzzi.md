# DyMA-Fuzz: Dynamic Direct Memory Access Abstraction for Re-hosted Monolithic Firmware Fuzzing

## 基本信息

- 作者：Guy Farrelly、Michael Chesser、Seyit Camtepe、Damith C. Ranasinghe
- 发表日期：2026-02-09
- 更新日期：2026-02-09
- 来源：arXiv
- 来源编号：2602.08750v1
- 研究类别：工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2602.08750v1](http://arxiv.org/abs/2602.08750v1)
- PDF：[https://arxiv.org/pdf/2602.08750v1](https://arxiv.org/pdf/2602.08750v1)
- 分析模式：仅元数据分析

## 摘要

The rise of smart devices in critical domains--including automotive, medical, industrial--demands robust firmware testing. Fuzzing firmware in re-hosted environments is a promising method for automated testing at scale, but remains difficult due to the tight coupling of code with a microcontroller's peripherals. Existing fuzzing frameworks primarily address input challenges in providing inputs for Memory-Mapped I/O or interrupts, but largely overlook Direct Memory Access (DMA), a key high-throughput interface used that bypasses the CPU. We introduce DyMA-Fuzz to extend recent advances in stream-based fuzz input injection to DMA-driven interfaces in re-hosted environments. It tackles key challenges--vendor-specific descriptors, heterogeneous DMA designs, and varying descriptor locations--using runtime analysis techniques to infer DMA memory access patterns and automatically inject fuzzing data into target buffers, without manual configuration or datasheets. Evaluated on 94 firmware samples and 8 DMA-guarded CVE benchmarks, DyMA-Fuzz reveals vulnerabilities and execution paths missed by state-of-the-art tools and achieves up to 122% higher code coverage. These results highlight DyMA-Fuzz as a practical and effective advancement in automated firmware testing and a scalable solution for fuzzing complex embedded systems.

## 研究问题

The rise of smart devices in critical domains--including automotive, medical, industrial--demands robust firmware testing. Fuzzing firmware in re-hosted environments is a promising method for automated testing at scale, but remains difficult due to the tight coupling of code with a microcontroller's peripherals. Existing fuzzing frameworks primarily address input challenges in providing inputs for Memory-Mapped I/O or interrupts, but largely overlook Direct Memory Access (DMA), a key high-throughput interface used that bypasses the CPU. We introduce DyMA-Fuzz to extend recent advances in stream-based fuzz input injection to DMA-driven interfaces in re-hosted environments. It tackles key challenges--vendor-specific descriptors, heterogeneous DMA designs, and varying descriptor locations--using runtime analysis techniques to infer DMA memory access patterns and automatically inject fuzzing data into target buffers, without manual configuration or datasheets. Evaluated on 94 firmware samples and 8 DMA-guarded CVE benchmarks, DyMA-Fuzz reveals vulnerabilities and execution paths missed by state-of-the-art tools and achieves up to 122% higher code coverage. These results highlight DyMA-Fuzz as a practical and effective advancement in automated firmware testing and a scalable solution for fuzzing complex embedded systems.

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
