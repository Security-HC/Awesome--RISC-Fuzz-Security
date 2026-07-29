# SPARC: Automated Root-Cause Analysis of Pre-Silicon Power Side-Channel Leakage in the Processor Design Flow

## 基本信息

- 作者：Andrija Nešković、Christian Ewert、Mladen Berekovic、Saleh Mulhem
- 发表日期：2026-07-25
- 会议/期刊：arXiv
- 主分类：微架构安全自动测试
- 相关性：A·直接相关（score=5）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：Microarchitectural Security Testing、Coverage, Oracles & Fuzzing Methodology
- 纳入依据：hardware/processor object: risc-v, processor, cpu, microarchitectural；verification/fuzzing method: information flow tracking；security relevance: security, leakage
- 论文页面：[http://arxiv.org/abs/2607.23218v1](http://arxiv.org/abs/2607.23218v1)
- PDF：[https://arxiv.org/pdf/2607.23218v1](https://arxiv.org/pdf/2607.23218v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 9 页，提取 53763 字符

## 摘要

Power-Side-Channel Leakage (PSCL) originates from architectural and micro-architectural artifacts in a processor and poses a severe threat to the confidentiality of cryptographic software. Consequently, pre-silicon PSCL evaluation is indispensable for secure hardware design. Existing frameworks are either limited by poor simulation scalability or fail to attribute leakage to the correct hardware signals and software instructions, thereby impeding a comprehensive root-cause analysis. This paper presents SPARC, an automated framework for pre-silicon PSCL evaluation and root-cause analysis. SPARC leverages macro-cell-level Information Flow Tracking (IFT) augmented with enhanced shadow logic that tags switching activity originating from secret-dependent data. By isolating this activity, SPARC applies statistical leakage tests to detect PSCL, while simultaneously attributing the leakage to specific hardware signals and mapping those signals to the corresponding software instructions. This approach thus delivers a full end-to-end leakage evaluation and root-cause analysis for both hardware and software. To demonstrate and validate SPARC, PSCL of multiple open-source RISC-V CPUs, encompassing 32-bit and 64-bit cores with both in-order and out-of-order pipelines, is evaluated across a range of cryptographic workloads, including masked and unmasked AES and ML-KEM (CRYSTALS-Kyber-512). SPARC recovers known leakage sources as a sanity check and identifies specific microarchitectural leakage sources, achieving an 8x per-trace simulation speedup over previously shown approaches on comparable designs. By enabling precise and scalable root-cause analysis at the pre-silicon stage, this work provides a practical framework to mitigate PSCL early in the design flow, thereby strengthening the security of future processors.

## 研究问题

现有预硅前功耗侧信道泄漏(PSCL)评估框架要么仿真可扩展性差，要么无法将泄漏归因到正确的硬件信号和软件指令，缺乏同时具备可扩展性、秘密敏感性和软硬件联合归因的框架。

## Introduction 梳理

已有方法如ACA在门级需要60小时，Telescope未使用IFT，Archer只到ISA层。SPARC填补了这些空白，提供可扩展的预硅前PSCL评估和根因分析，同时实现硬件信号和软件指令归因。

## 方法

输入生成：匹配对痕迹，每组N条痕迹，明文相同但密钥不同(K0和K1)；掩码实现中随机掩码配对匹配。反馈/coverage：基于Welch's t-test的TVLA，每周期计算t统计量，阈值|t|>4.5判定泄漏。Oracle：无golden model，使用统计假设检验。DUT/平台：三种RISC-V处理器(Ibex 32位2级顺序，Proteus 32位乱序，Rocket 64位5级顺序)在Verilator上仿真。是否需要golden model：否。

## 实验与评估

baseline：声称8x per-trace仿真加速，但未列出直接对比实验；实验预算：AMD Ryzen 7 7800X3D CPU, 64GB DDR5 RAM；统计：每周期Welch's t-test；bug/CVE：未披露具体CVE，但恢复已知泄漏源并识别新泄漏；开销：仪器化设计增大~11-12%相对于纯CellIFT；总评估时间：AES(<25分钟)，Kyber(~10小时)；Artifact：开源代码在https://github.com/iti-luebeck/sparc-sca。

## 核心贡献

提出SPARC框架，结合宏单元级IFT和泄漏估计逻辑，实现可扩展的预硅前PSCL评估，并自动进行硬件信号和软件指令的双重根因分析。

## 与本仓库研究主线的关系

直接相关。属于微架构安全自动测试，聚焦于功耗侧信道泄漏的评估和根因分析，与多hart/一致性路径研究不直接相关，但涉及处理器安全验证。

## 结论

SPARC实现了预硅前PSCL评估和根因分析，在三个RISC-V CPU上验证了掩码和非掩码AES及ML-KEM。检出已知泄漏并识别了微架构泄漏(如Proteus乱序流水线)，实现了8倍仿真速度提升。

## 局限性

动态IFT仅覆盖被激活的路径，未评估未激活路径；宏单元级抽象忽略低于宏单元级的效果(如毛刺)；未来工作需要门级交叉验证、掩码ML-KEM和片上多核系统。

## 详细阅读分析

需要深读。方法核心是IFT和泄漏建模，评估了多种RISC-V处理器和加密工作负载。

## 后续核验问题

- 如何将SPARC扩展到多核SoC并处理一致性协议中引入的泄漏？
- SPARC的泄漏模型能否适应其他侧信道(如电磁)？
- 对于掩码实现，SPARC能否区分一阶泄漏与高阶泄漏？
