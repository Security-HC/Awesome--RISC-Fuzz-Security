# The Open-Source BlackParrot-BedRock Cache Coherence System

## 基本信息

- 作者：Mark Unruh Wyse
- 发表日期：2025-05-02
- 会议/期刊：arXiv
- 主分类：多 Hart、内存一致性与缓存一致性
- 相关性：A·直接相关（score=7）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：Multi-Hart, Memory Consistency & Cache Coherence
- 纳入依据：strong phrase in abstract: cache coherence protocol；hardware/processor object: risc-v, processor, microarchitecture, cache coherence；verification/fuzzing method: verification
- 论文页面：[http://arxiv.org/abs/2505.00962v1](http://arxiv.org/abs/2505.00962v1)
- PDF：[https://arxiv.org/pdf/2505.00962v1](https://arxiv.org/pdf/2505.00962v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 188 页，提取 100000 字符

## 摘要

This dissertation revisits the topic of programmable cache coherence engines in the context of modern shared-memory multicore processors. First, the open-source BedRock cache coherence protocol is described. BedRock employs the canonical MOESIF coherence states and reduces implementation burden by eliminating transient coherence states from the protocol. The protocol's design complexity, concurrency, and verification effort are analyzed and compared to a canonical directory-based invalidate coherence protocol. Second, the architecture and microarchitecture of three separate cache coherence directories implementing the BedRock protocol within the BlackParrot 64-bit RISC-V multicore processor, collectively called BlackParrot-BedRock (BP-BedRock), are described. A fixed-function coherence directory engine implementation provides a baseline design for performance and area comparisons. A microcode-programmable coherence directory implementation demonstrates the feasibility of implementing a programmable coherence engine capable of maintaining sufficient protocol processing performance. A hybrid fixed-function and programmable coherence directory blends the protocol processing performance of the fixed-function design with the programmable flexibility of the microcode-programmable design. Collectively, the BedRock coherence protocol and its three BP-BedRock implementations demonstrate the feasibility and challenges of including programmable logic within the coherence system of modern shared-memory multicore processors, paving the way for future research into the application- and system-level benefits of programmable coherence engines.

## 研究问题

在现代计算环境变化（技术缩放减慢、多样化应用需求）下，重新审视可编程缓存一致性引擎是否可行且高效。

## Introduction 梳理

现有硬件一致性系统（如目录协议）固定不变，无法灵活适应新兴应用和领域需求。过去虽曾探索可编程一致性，但当时技术背景不同。作者假设可在现代多核处理器中引入可编程性而不显著牺牲性能或面积，并提出了开放源代码的BedRock协议和在BlackParrot上的三种实现，验证了可行性。

## 方法

论文采用自底向上的架构设计方法。先设计BedRock缓存一致性协议，强调减少复杂性（无瞬态状态）。然后在BlackParrot RISC-V多核处理器上实现三种CCE：固定功能FSM CCE、微码可编程ucode CCE和混合Hybrid CCE。使用CMurphi模型检查器验证MESI协议变体。性能评估采用Splash-3基准测试在FPGA上运行，面积比较使用FPGA资源利用率。未涉及硬件Fuzzing或自动输入生成。Oracle为SWMR和数据值不变性。DUT为BlackParrot处理器及FPGA实现。不需要golden model。

## 实验与评估

Baseline: 固定功能CCE作为性能与面积基线。实验使用Splash-3基准测试（8核心），归一化执行时间比较。统计方法明确（均值？未细述）。未报告具体bug或CVE。开销：ucode CCE相比FSM CCE性能接近（最多约5%退化），面积增加约10-20%（具体见表4.20和附录E）。Artifact: 全部设计开放源代码（GitHub）。

## 核心贡献

1. 提出BedRock缓存一致性协议，消除瞬态状态，降低实现复杂度。2. 在BlackParrot RISC-V多核处理器上实现三种CCE（FSM、ucode、Hybrid），并开源。3. 通过实验证明可编程一致性引擎性能与固定功能竞争，面积开销可控。4. 提供详细的架构、微架构和性能面积分析。

## 与本仓库研究主线的关系

直接相关：论文涉及RISC-V多核处理器缓存一致性设计及实现，提供开放硬件平台，适用于多hart一致性验证研究。可作为验证目标或基线，但论文本身不聚焦于自动测试或Fuzzing，而是设计和评估。

## 结论

可编程一致性引擎在现代多核处理器中是可行的。微码可编程设计在性能上与固定功能设计竞争，面积开销较小。混合设计结合两者优点，提供了灵活性和高效性。BedRock协议简化了实现且适用于小到中等规模系统。

## 局限性

协议面向小-中等规模系统（8-16核心），未在更大规模系统中验证；微码可编程设计的灵活性仍受限于ISA，且编程模型复杂；混合设计的可编程管道仅支持有限操作；验证仅针对MESI变体进行形式化建模，未覆盖完全MOESIF。

## 详细阅读分析

建议重点阅读第4章（BP-BedRock实现）、第5章（混合CCE）和第3.4节（协议验证）。附录A-D提供完整协议表。

## 后续核验问题

- 如何将可编程一致性引擎扩展到更大规模（>16核心）系统？
- 能否对微码可编程CCE进行形式化验证，确保协议实现的正确性？
- 混合CCE的可编程管道能否支持更复杂的应用级操作（如安全检查、监视）？
- 与其他开放RISC-V多核（如BOOM、Rocket）的一致性系统相比，性能和面积如何？
