# AKER: A Design and Verification Framework for Safe andSecure SoC Access Control

## 基本信息

- 作者：Francesco Restuccia、Andres Meza、Ryan Kastner
- 发表日期：2021-06-24
- 会议/期刊：arXiv
- 主分类：多 Hart、内存一致性与缓存一致性
- 相关性：B·强邻近（score=5）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：Multi-Hart, Memory Consistency & Cache Coherence
- 纳入依据：hardware/processor object: soc, multicore；verification/fuzzing method: verification；security relevance: security
- 论文页面：[http://arxiv.org/abs/2106.13263v1](http://arxiv.org/abs/2106.13263v1)
- PDF：[https://arxiv.org/pdf/2106.13263v1](https://arxiv.org/pdf/2106.13263v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 9 页，提取 58217 字符

## 摘要

Modern systems on a chip (SoCs) utilize heterogeneous architectures where multiple IP cores have concurrent access to on-chip shared resources. In security-critical applications, IP cores have different privilege levels for accessing shared resources, which must be regulated by an access control system. AKER is a design and verification framework for SoC access control. AKER builds upon the Access Control Wrapper (ACW) -- a high performance and easy-to-integrate hardware module that dynamically manages access to shared resources. To build an SoC access control system, AKER distributes the ACWs throughout the SoC, wrapping controller IP cores, and configuring the ACWs to perform local access control. To ensure the access control system is functioning correctly and securely, AKER provides a property-driven security verification using MITRE common weakness enumerations. AKER verifies the SoC access control at the IP level to ensure the absence of bugs in the functionalities of the ACW module, at the firmware level to confirm the secure operation of the ACW when integrated with a hardware root-of-trust (HRoT), and at the system level to evaluate security threats due to the interactions among shared resources. The performance, resource usage, and security of access control systems implemented through AKER is experimentally evaluated on a Xilinx UltraScale+ programmable SoC, it is integrated with the OpenTitan hardware root-of-trust, and it is used to design an access control system for the OpenPULP multicore architecture.

## 研究问题

现代SoC中多IP核并发访问共享资源需要灵活的访问控制系统，但现有方案在动态性、性能开销和安全性验证方面存在不足。

## Introduction 梳理

现有SoC访问控制方法（如基于互连硬编码、外设ID识别、集中式策略引擎）难以支持动态策略、易受非法请求干扰或产生性能瓶颈。AKER提出基于ACW的分布式框架，并通过MITRE CWE驱动的属性验证确保安全。

## 方法

输入生成：可配置AXI DMA作为控制器，测试台迭代重置和配置。反馈/覆盖：使用Tortuga Logic Radix-S进行安全属性仿真，通过断言失败次数评估。Oracle：安全属性（信息流和跟踪属性）。DUT/平台：ACW模块，验证在Xilinx Zynq UltraScale+和OpenPULP上。无golden model。

## 实验与评估

baseline：与AXI SmartConnect（INTC）和XMPU两种方法比较。实验预算：FPGA实验，测量隔离和DoS场景响应时间。统计：平均响应时间变化，未提供置信区间。bug/CVE：未报告具体漏洞，仅验证了316+1438+76个安全属性。开销：ACW引入1时钟周期延迟，资源消耗LUT 263-730。Artifact：开源仓库（GitHub）。

## 核心贡献

提出ACW模块和AKER框架，实现分布式、可动态配置的访问控制；提供基于MITRE CWE的属性驱动安全验证方法，覆盖IP、固件、系统级别；开源实现。

## 与本仓库研究主线的关系

直接相关：访问控制是多hart共享资源安全的基础；与多hart/一致性路径研究强邻近，但未覆盖内存一致性协议验证。

## 结论

AKER框架提供高效灵活的SoC访问控制，性能影响小，资源占用低，支持动态配置和HRoT集成，并通过多级安全属性验证确保正确性。

## 局限性

实验仅基于AXI协议，未覆盖TileLink；安全验证依赖仿真，可能遗漏路径；威胁模型假设ACW、HRoT和外围设备可信；未讨论扩展至缓存一致性或非一致内存访问场景。

## 详细阅读分析

需要深入了解安全属性模板的生成与自动化，以及ACW在更多SoC架构（如非AXI协议）中的适配性。

## 后续核验问题

- AKER框架如何扩展到TileLink或其他片上网络协议？
- 安全属性验证能否完全自动化以避免手动设计模板？
- 对于支持缓存一致性的多hart系统，AKER是否需要修改？
- 是否评估过属性验证的完备性（如覆盖所有CWE路径）？
