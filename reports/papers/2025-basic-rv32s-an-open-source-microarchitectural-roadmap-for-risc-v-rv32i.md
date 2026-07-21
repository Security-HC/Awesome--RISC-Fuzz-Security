# basic_RV32s: An Open-Source Microarchitectural Roadmap for RISC-V RV32I

## 基本信息

- 作者：Hyun Woo Kang、Ji Woong Choi
- 发表日期：2025-09-04
- 更新日期：2025-09-04
- 来源：arXiv
- 来源编号：2510.15887v1
- 研究类别：RISC-V Fuzzing、Microarchitecture Security、RTL and Hardware Verification、Tools and Benchmarks
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2510.15887v1](http://arxiv.org/abs/2510.15887v1)
- PDF：[https://arxiv.org/pdf/2510.15887v1](https://arxiv.org/pdf/2510.15887v1)
- 分析模式：仅元数据分析

## 摘要

This paper introduces BASIC_RV32s, an open-source framework providing a practical microarchitectural roadmap for the RISC-V RV32I architecture, addressing the gap between theoretical knowledge and hardware implementation. Following the classic Patterson and Hennessy methodology, the design evolves from a basic single-cycle core to a 5-stage pipelined core design with full hazard forwarding, dynamic branch prediction, and exception handling. For verification, the final core design is integrated into a System-on-Chip (SoC) with Universal Asynchronous Receiver-Transmitter (UART) communication implemented on a Xilinx Artix-7 Field-Programmable Gate Array (FPGA), achieving 1.09 Dhrystone million instructions per second per megahertz (DMIPS/MHz) at 50 MHz. By releasing all Register-Transfer Level (RTL) source code, signal-level logic block diagrams, and development logs under MIT license on GitHub, BASIC_RV32s offers a reproducible instructional pathway for the open-source hardware ecosystem.

## 研究问题

This paper introduces BASIC_RV32s, an open-source framework providing a practical microarchitectural roadmap for the RISC-V RV32I architecture, addressing the gap between theoretical knowledge and hardware implementation. Following the classic Patterson and Hennessy methodology, the design evolves from a basic single-cycle core to a 5-stage pipelined core design with full hazard forwarding, dynamic branch prediction, and exception handling. For verification, the final core design is integrated into a System-on-Chip (SoC) with Universal Asynchronous Receiver-Transmitter (UART) communication implemented on a Xilinx Artix-7 Field-Programmable Gate Array (FPGA), achieving 1.09 Dhrystone million instructions per second per megahertz (DMIPS/MHz) at 50 MHz. By releasing all Register-Transfer Level (RTL) source code, signal-level logic block diagrams, and development logs under MIT license on GitHub, BASIC_RV32s offers a reproducible instructional pathway for the open-source hardware ecosystem.

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
