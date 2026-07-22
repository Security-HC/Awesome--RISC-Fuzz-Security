# PAGURUS: Low-Overhead Dynamic Information Flow Tracking on Loosely Coupled Accelerators

## 基本信息

- 作者：Luca Piccolboni、Giuseppe Di Guglielmo、Luca P. Carloni
- 发表日期：2019-12-18
- 会议/期刊：arXiv
- 主分类：覆盖、Oracle 与 Fuzzing 方法
- 相关性：A·直接相关（score=5）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：Coverage, Oracles & Fuzzing Methodology
- 纳入依据：hardware/processor object: risc-v, processor；verification/fuzzing method: information flow tracking；security relevance: security, leakage
- 论文页面：[http://arxiv.org/abs/1912.11153v1](http://arxiv.org/abs/1912.11153v1)
- PDF：[https://arxiv.org/pdf/1912.11153v1](https://arxiv.org/pdf/1912.11153v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 12 页，提取 69901 字符

## 摘要

Software-based attacks exploit bugs or vulnerabilities to get unauthorized access or leak confidential information. Dynamic information flow tracking (DIFT) is a security technique to track spurious information flows and provide strong security guarantees against such attacks. To secure heterogeneous systems, the spurious information flows must be tracked through all their components, including processors, accelerators (i.e., application-specific hardware components) and memories. We present PAGURUS, a flexible methodology to design a low-overhead shell circuit that adds DIFT support to accelerators. The shell uses a coarse-grain DIFT approach, thus not requiring to make modifications to the accelerator's implementation. We analyze the performance and area overhead of the DIFT shell on FPGAs and we propose a metric, called information leakage, to measure its security guarantees. We perform a design-space exploration to show that we can synthesize accelerators with different characteristics in terms of performance, cost and security guarantees. We also present a case study where we use the DIFT shell to secure an accelerator running on a embedded platform with a DIFT-enhanced RISC-V core.

## 研究问题

如何在异构SoC中为松散耦合加速器提供低开销的动态信息流跟踪（DIFT）安全保护，以防范软件攻击（如缓冲区溢出）？

## Introduction 梳理

现有DIFT实现多聚焦于处理器核心，忽略加速器（尤其是松散耦合加速器）的安全保护，导致攻击者可利用加速器泄露信息。既有方法（如WHISK、TaintHLS）采用细粒度DIFT，需要修改加速器内部逻辑，面积开销大（可达31%），且不适用于第三方IP核。本文提出PAGURUS，一种粗粒度DIFT shell电路，不修改加速器实现，通过标签交错和随机化实现安全跟踪，同时保持低开销。

## 方法

PAGURUS设计了一个双解耦的shell电路，封装加速器，不修改其内部逻辑。输入生成：标签与数据交错存储，标签位置随机化（基于伪随机数生成器）。反馈/coverage：shell在加载时检查输入标签是否与src_tag匹配，不匹配则停止加速器。Oracle：无需golden model，通过标签值匹配检测攻击。DUT/平台：针对FPGA（Xilinx Virtex-7 XC7V2000T、Xilinx XC7Z020）上设计的三个加速器（GRAY、MEAN、MULTS），基于SystemC设计，使用高综合和FPGA原型。需要golden model：否（基于标签策略）。

## 实验与评估

baseline：不带DIFT shell的加速器。实验预算：三个加速器，三种工作负载（小/中/大），突发大小和标签偏移变化。统计：执行时间归一化（FPGA测量），信息泄漏百分比（最坏情况计算），面积开销（LUT/FF）。bug/CVE：通过案例研究验证对缓冲区溢出攻击的防御。开销：shell面积约1600 LUT、1400 FF；执行时间开销随标签密度增加，但通常低于2倍（大标签偏移时更低）。Artifact：未确认（论文未提供开源代码或网站链接）。

## 核心贡献

1) 提出低开销DIFT shell方法，实现双解耦、粗粒度DIFT；2) 定义信息泄漏指标量化安全；3) 展示设计空间探索，实现性能-成本-安全权衡；4) 在RISC-V平台上集成DIFT的案例研究。

## 与本仓库研究主线的关系

直接相关。属于硬件DIFT安全方法，涉及RISC-V核心集成，与多hart/一致性路径研究无关，但可作为硬件安全验证的Oracle/覆盖方法参考。

## 结论

PAGURUS能有效为松散耦合加速器添加DIFT保护，面积开销可忽略，性能开销可控（取决于标签密度）。信息泄漏指标可用于指导设计空间探索，实现性能、成本与安全的权衡。案例研究（PULPino平台）展示了整体DIFT保护的必要性。

## 局限性

仅支持粗粒度DIFT，可能产生假阳性；仅针对松散耦合加速器，未覆盖紧耦合加速器；标签随机化依赖于伪随机数生成器，安全性依赖于随机性；评估限于三个特定加速器和FPGA平台，通用性需进一步验证。

## 详细阅读分析

重点阅读Section IV（shell架构）、Section V（信息泄漏指标）、Section VI（实验评估）、Section VII（PULPino案例研究）。

## 后续核验问题

- 粗粒度DIFT的假阳性率如何，如何减少？
- 如何将PAGURUS扩展到紧耦合加速器？
- 标签随机化的安全性分析是否完整？
- 能否在更复杂的SoC（如多hart）上集成并验证？
