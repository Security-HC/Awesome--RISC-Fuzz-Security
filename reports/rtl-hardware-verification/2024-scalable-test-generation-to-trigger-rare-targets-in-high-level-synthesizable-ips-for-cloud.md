# Scalable Test Generation to Trigger Rare Targets in High-Level Synthesizable IPs for Cloud FPGAs

## 基本信息

- 作者：Mukta Debnath、Animesh Basak Chowdhury、Debasri Saha、Susmita Sur-Kolay
- 发表日期：2024-05-30
- 更新日期：2024-05-30
- 来源：arXiv
- 来源编号：2405.19948v1
- 研究类别：RTL 与硬件验证、Fuzzing 方法论、工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：2
- 论文页面：[http://arxiv.org/abs/2405.19948v1](http://arxiv.org/abs/2405.19948v1)
- PDF：[https://arxiv.org/pdf/2405.19948v1](https://arxiv.org/pdf/2405.19948v1)
- 分析模式：仅元数据分析

## 摘要

High-Level Synthesis (HLS) has transformed the development of complex Hardware IPs (HWIP) by offering abstraction and configurability through languages like SystemC/C++, particularly for Field Programmable Gate Array (FPGA) accelerators in high-performance and cloud computing contexts. These IPs can be synthesized for different FPGA boards in cloud, offering compact area requirements and enhanced flexibility. HLS enables designs to execute directly on ARM processors within modern FPGAs without the need for Register Transfer Level (RTL) synthesis, thereby conserving FPGA resources. While HLS offers flexibility and efficiency, it also introduces potential vulnerabilities such as the presence of hidden circuitry, including the possibility of hosting hardware trojans within designs. In cloud environments, these vulnerabilities pose significant security concerns such as leakage of sensitive data, IP functionality disruption and hardware damage, necessitating the development of robust testing frameworks. This research presents an advanced testing approach for HLS-developed cloud IPs, specifically targeting hidden malicious functionalities that may exist in rare conditions within the design. The proposed method leverages selective instrumentation, combining greybox fuzzing and concolic execution techniques to enhance test generation capabilities. Evaluation conducted on various HLS benchmarks, possessing characteristics of FPGA-based cloud IPs with embedded cloud related threats, demonstrates the effectiveness of our framework in detecting trojans and rare scenarios, showcasing improvements in coverage, time efficiency, memory usage, and testing costs compared to existing methods.

## 研究问题

High-Level Synthesis (HLS) has transformed the development of complex Hardware IPs (HWIP) by offering abstraction and configurability through languages like SystemC/C++, particularly for Field Programmable Gate Array (FPGA) accelerators in high-performance and cloud computing contexts. These IPs can be synthesized for different FPGA boards in cloud, offering compact area requirements and enhanced flexibility. HLS enables designs to execute directly on ARM processors within modern FPGAs without the need for Register Transfer Level (RTL) synthesis, thereby conserving FPGA resources. While HLS offers flexibility and efficiency, it also introduces potential vulnerabilities such as the presence of hidden circuitry, including the possibility of hosting hardware trojans within designs. In cloud environments, these vulnerabilities pose significant security concerns such as leakage of sensitive data, IP functionality disruption and hardware damage, necessitating the development of robust testing frameworks. This research presents an advanced testing approach for HLS-developed cloud IPs, specifically targeting hidden malicious functionalities that may exist in rare conditions within the design. The proposed method leverages selective instrumentation, combining greybox fuzzing and concolic execution techniques to enhance test generation capabilities. Evaluation conducted on various HLS benchmarks, possessing characteristics of FPGA-based cloud IPs with embedded cloud related threats, demonstrates the effectiveness of our framework in detecting trojans and rare scenarios, showcasing improvements in coverage, time efficiency, memory usage, and testing costs compared to existing methods.

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
