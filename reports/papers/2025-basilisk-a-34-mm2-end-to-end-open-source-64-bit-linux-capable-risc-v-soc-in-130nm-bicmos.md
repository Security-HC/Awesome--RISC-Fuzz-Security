# Basilisk: A 34 mm2 End-to-End Open-Source 64-bit Linux-Capable RISC-V SoC in 130nm BiCMOS

## 基本信息

- 作者：Philippe Sauter、Thomas Benz、Paul Scheffler、Martin Povišer、Frank K. Gürkaynak、Luca Benini
- 发表日期：2025-05-15
- 更新日期：2025-05-15
- 来源：arXiv
- 来源编号：2505.10060v1
- 研究类别：RISC-V Fuzzing
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2505.10060v1](http://arxiv.org/abs/2505.10060v1)
- PDF：[https://arxiv.org/pdf/2505.10060v1](https://arxiv.org/pdf/2505.10060v1)
- 分析模式：仅元数据分析

## 摘要

End-to-end open-source electronic design automation (OSEDA) enables a collaborative approach to chip design conducive to supply chain diversification and zero-trust step-by-step design verification. However, existing end-to-end OSEDA flows have mostly been demonstrated on small designs and have not yet enabled large, industry-grade chips such as Linux-capable systems-on-chip (SoCs). This work presents Basilisk, the largest end-to-end open-source SoC to date. Basilisk's 34 mm2, 2.7 MGE design features a 64-bit Linux-capable RISC-V core, a lightweight 124 MB/s DRAM controller, and extensive IO, including a USB 1.1 host, a video output, and a fully digital 62 Mb/s chip-to-chip (C2C) link. We implement Basilisk in IHP's open 130 nm BiCMOS technology, significantly improving on the state-of-the-art (SoA) OSEDA flow. Our enhancements of the Yosys-based synthesis flow improve design timing and area by 2.3x and 1.6x, respectively, while consuming significantly less system resources. By tuning OpenROAD place and route (P&R) to our design and technology, we decrease the die size by 12%. The fabricated Basilisk chip reaches 62 MHz at its nominal 1.2 V core voltage and up to 102 MHz at 1.64 V. It achieves a peak energy efficiency of 18.9 DP MFLOP/s/W at 0.88 V.

## 研究问题

End-to-end open-source electronic design automation (OSEDA) enables a collaborative approach to chip design conducive to supply chain diversification and zero-trust step-by-step design verification. However, existing end-to-end OSEDA flows have mostly been demonstrated on small designs and have not yet enabled large, industry-grade chips such as Linux-capable systems-on-chip (SoCs). This work presents Basilisk, the largest end-to-end open-source SoC to date. Basilisk's 34 mm2, 2.7 MGE design features a 64-bit Linux-capable RISC-V core, a lightweight 124 MB/s DRAM controller, and extensive IO, including a USB 1.1 host, a video output, and a fully digital 62 Mb/s chip-to-chip (C2C) link. We implement Basilisk in IHP's open 130 nm BiCMOS technology, significantly improving on the state-of-the-art (SoA) OSEDA flow. Our enhancements of the Yosys-based synthesis flow improve design timing and area by 2.3x and 1.6x, respectively, while consuming significantly less system resources. By tuning OpenROAD place and route (P&R) to our design and technology, we decrease the die size by 12%. The fabricated Basilisk chip reaches 62 MHz at its nominal 1.2 V core voltage and up to 102 MHz at 1.64 V. It achieves a peak energy efficiency of 18.9 DP MFLOP/s/W at 0.88 V.

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
