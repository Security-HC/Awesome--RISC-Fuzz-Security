# Information Flow Paths from RTL Traces

## 基本信息

- 作者：Calvin Deutschbein、Owyn Wyatt
- 发表日期：2026-06-11
- 会议/期刊：arXiv
- 主分类：覆盖、Oracle 与 Fuzzing 方法
- 相关性：B·强邻近（score=5）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：Coverage, Oracles & Fuzzing Methodology
- 纳入依据：hardware/processor object: rtl；verification/fuzzing method: validation, information flow tracking；security relevance: security
- 论文页面：[http://arxiv.org/abs/2606.13860v1](http://arxiv.org/abs/2606.13860v1)
- PDF：[https://arxiv.org/pdf/2606.13860v1](https://arxiv.org/pdf/2606.13860v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 9 页，提取 40966 字符

## 摘要

Security validation is an important yet challenging part of the hardware design process, yet, by convention, validation engineers are tasked with defining the threat model, specifying the relevant security properties, detecting any violations of those properties, and assessing the consequences to system security, each of which is manually intensive and may introduce errors. The combined technologies of information flow tracking and specification mining represent an automated approach to property generation and validation, but prior work on information flow tracking on RTL trace data was limited to find cases under which information flowed between registers, without reproducing full paths to capture how sensitive information propagates through a design. With the introduction of new technologies accelerating hardware analysis, we develop a novel approach for constructing information flow paths from register transfer level (RTL) trace data.

## 研究问题

从RTL跟踪数据中重建信息流路径，以识别硬件安全漏洞，尤其是微架构信息泄漏路径。现有IFT只能检测信息是否流动，无法确定路径。

## Introduction 梳理

研究缺口：先前IFT工作（如Isadora）只能确定信息是否在寄存器之间流动，但无法重建完整路径来捕捉敏感信息如何传播。既有方法不足：手动定义威胁模型、安全属性、检测违规和评估后果，劳动密集且易出错。贡献：提出一种从RTL跟踪数据构建信息流路径的新方法，可实现自动化路径提取。

## 方法

输入生成：使用测试平台生成RTL跟踪数据（VCD文件）。反馈/coverage：通过信息流跟踪（IFT）的跟踪信号获取时间流信息。Oracle：使用IFT技术（Radix）的跟踪标签，通过检查跟踪信号是否非零来确定信息流。DUT/平台：PicoRV32 RISC-V CPU（开源Verilog设计）。是否需要golden model：不需要，但需要测试平台和IFT工具。

## 实验与评估

baseline：未明确提及。实验预算：PicoRV32有232个寄存器，182个有非平凡信息流；模拟总时长8小时45分钟（串行），每个寄存器平均约3分钟；VCD文件64MB，数据框525MB，稀疏表示419KB。统计：找到已知路径长度2-5，数量分别为151,130,71,59。bug/CVE：发现一个路径对应CWE-1244；扩展案例发现CWE-411。开销：串行模拟耗时，但可并行化；稀疏表示节省空间。Artifact：开源脚本在GitHub上。

## 核心贡献

提出从RTL跟踪数据构建信息流路径的算法，包括时间流提取、图构建、候选边推广和路径回环；实现并应用于PicoRV32，发现实际漏洞路径。

## 与本仓库研究主线的关系

直接相关：涉及RISC-V（PicoRV32）的硬件安全验证，使用信息流跟踪和路径重建方法。与多hart/一致性路径研究：不直接涉及，但方法可扩展用于多核一致性验证中的信息泄漏检测。

## 结论

成功演示了从RTL跟踪数据提取信息流路径的方法，能够识别CWE漏洞。方法依赖于设计源和测试平台。

## 局限性

依赖跟踪数据，测试覆盖不足可能遗漏路径；候选边无法唯一确定时需进一步分析（静态分析或符号执行）；工具依赖专有IFT（Radix），但可使用开源替代。

## 详细阅读分析

建议阅读Isadora（[1]）作为基础，以及Myrtha（[2]）和vcd2df（[3]）等加速工具。

## 后续核验问题

- 如何处理多个同时信息流源导致的候选边不确定性？
- 方法能否扩展到门级或大型SoC？
- 是否可与随机测试生成结合提高覆盖？
- 在验证RISC-V多核一致性路径时如何应用？
