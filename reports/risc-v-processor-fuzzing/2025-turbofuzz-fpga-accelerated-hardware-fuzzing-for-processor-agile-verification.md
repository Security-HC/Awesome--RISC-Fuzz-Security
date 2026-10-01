# TurboFuzz: FPGA Accelerated Hardware Fuzzing for Processor Agile Verification

## 基本信息

- 作者：Yang Zhong、Haoran Wu、Xueqi Li、Sa Wang、David Boland、Yungang Bao、Kan Shi
- 发表日期：2025-09-12
- 会议/期刊：arXiv
- 主分类：RISC-V 处理器 Fuzzing
- 相关性：A·直接相关（score=9）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：RISC-V Processor Fuzzing、Coverage, Oracles & Fuzzing Methodology
- 纳入依据：strong phrase in title: hardware fuzzing；hardware/processor object: risc-v, processor；verification/fuzzing method: fuzz, test generation, verification
- 论文页面：[http://arxiv.org/abs/2509.10400v2](http://arxiv.org/abs/2509.10400v2)
- PDF：[https://arxiv.org/pdf/2509.10400v2](https://arxiv.org/pdf/2509.10400v2)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 14 页，提取 71964 字符

## 摘要

Verification is a critical process for ensuring the correctness of modern processors. The increasing complexity of processor designs and the emergence of new instruction set architectures (ISAs) like RISC-V have created demands for more agile and efficient verification methodologies, particularly regarding verification efficiency and faster coverage convergence. While simulation-based approaches now attempt to incorporate advanced software testing techniques such as fuzzing to improve coverage, they face significant limitations when applied to processor verification, notably poor performance and inadequate test case quality. Hardware-accelerated solutions using FPGA or ASIC platforms have tried to address these issues, yet they struggle with challenges including host-FPGA communication overhead, inefficient test pattern generation, and suboptimal implementation of the entire multi-step verification process. In this paper, we present TurboFuzz, an end-to-end hardware-accelerated verification framework that implements the entire Test Generation-Simulation-Coverage Feedback loop on a single FPGA for modern processor verification. TurboFuzz enhances test quality through optimized test case (seed) control flow, efficient inter-seed scheduling, and hybrid fuzzer integration, thereby improving coverage and execution efficiency. Additionally, it employs a feedback-driven generation mechanism to accelerate coverage convergence. Experimental results show that TurboFuzz achieves up to 2.23x more coverage collection than software-based fuzzers within the same time budget, and up to 571x performance speedup when detecting real-world issues, while maintaining full visibility and debugging capabilities with moderate area overhead.

## 研究问题

处理器验证效率低，现有硬件加速方法存在主机-FPGA通信开销、测试模式生成效率低、覆盖收敛慢等问题。

## Introduction 梳理

现代处理器设计日益复杂，RISC-V等新ISA对敏捷验证方法需求迫切。传统验证方法（如UVM、FPGA原型）效率低、调试困难。软件fuzzing应用于硬件验证（如DifuzzRTL、Cascade）存在性能瓶颈（2-4次/秒）、测试质量低、调试不便等问题。本文提出TurboFuzz，在单个FPGA上实现完整的测试生成-仿真-覆盖反馈闭环，通过优化控制流指令生成、语料库调度、混合fuzzing（deepExplore）和覆盖仪器化，提升覆盖收集速度和发现bug能力。

## 方法

输入生成：使用LFSR生成伪随机指令，支持直接模式和突变模式；反馈/coverage：基于寄存器覆盖（控制寄存器）的覆盖反馈，优化消除不可达覆盖点；Oracle：细粒度自检，将DUT和参考模型（REF）分别映射到FPGA逻辑和ARM硬核处理器，实现指令级同步自动比较；DUT/平台：AMD Zynq UltraScale+ FPGA，DUT包括Rocket、CVA6、BOOM RISC-V核；需要golden model：是，使用参考模型（REF）进行差异检查。

## 实验与评估

baseline：DifuzzRTL和Cascade；实验预算：1、2、4小时时间预算；统计：TurboFuzz达到2.23倍覆盖收集（比DifuzzRTL），1.26-1.31倍（比Cascade），覆盖35000点加速278倍，bug检测加速最高571倍；bug/CVE：发现9个已知bug和2个新bug（C9、C10）；开销：TurboFuzz IP消耗13% LUT、18% BRAM；整个框架17% LUT、23% BRAM、13%寄存器；Artifact：承诺开源。

## 核心贡献

1. 提出TurboFuzz，首个在单个FPGA上实现完整闭环的硬件加速验证框架（测试生成、仿真、自检、覆盖收集均硬件化）；2. 首个全综合硬件fuzzer，支持种子突变、改进覆盖仪器化和更深的覆盖探索；3. 提出混合fuzzing方法deepExplore，结合覆盖引导突变和基准程序结构化区间提取，构建高质量种子。

## 与本仓库研究主线的关系

直接相关：针对RISC-V处理器硬件fuzzing，覆盖生成、反馈和自检。但论文主要关注单核（Rocket、CVA6、BOOM），未涉及多hart或内存一致性验证。其优化方法（如覆盖仪器化、语料库调度）可借鉴，但需扩展以支持多核和一致性路径。

## 结论

本文提出TurboFuzz，一个端到端硬件加速验证框架，在单个FPGA上实现覆盖驱动生成、自检和覆盖收集。实验表明覆盖收集最多2.23倍，性能加速最高571倍，并发现新bug。未来工作包括资源感知覆盖度量、多FPGA扩展、支持非RISC-V ISA。

## 局限性

论文未明确提及局限，但可从上下文推断：当前仅支持单核处理器（未验证多hart）；覆盖仪器化方法可能存在偏置，虽经优化；仅适用于RISC-V（需修改指令生成模块）；硬件快照依赖FPGA特性，可能限制可移植性；面积开销虽适度，但较大设计可能受限。

## 详细阅读分析

TurboFuzz的覆盖仪器化优化通过顺序排列控制寄存器并处理回绕，消除了不可达覆盖点，使所有仪器化点均可达。控制流指令生成优化限制跳转范围并使用异常处理模板，使执行指令中fuzzing指令占比（prevalence）高达0.97。语料库调度根据覆盖增量保留有效种子，而非FIFO替换，实现7.5%覆盖提升和17.7倍加速（达27500点）。deepExplore方法通过SimPoint提取基准程序代表性区间，构建种子后用fuzzing探索，相比纯fuzzing多覆盖2.6%状态（在高覆盖水平下关键）。整体系统在相同时间预算下优于软件fuzzer，且发现新bug。

## 后续核验问题

- TurboFuzz如何扩展到多核或同时多线程处理器？其自检机制能否处理hart间的交互？
- 硬件快照（snapshot）的具体实现细节？是否支持断点续传？
- deepExplore中提取的指令区间如何确保与fuzzing生成指令的无缝衔接？
- 对于非RISC-V ISA，修改指令生成和操作数分配模块的工作量有多大？
