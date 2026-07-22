# RealityCheck: Bringing Modularity, Hierarchy, and Abstraction to Automated Microarchitectural Memory Consistency Verification

## 基本信息

- 作者：Yatin A. Manerkar、Daniel Lustig、Margaret Martonosi
- 发表日期：2020-03-09
- 会议/期刊：arXiv
- 主分类：多 Hart、内存一致性与缓存一致性
- 相关性：A·直接相关（score=9）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：Multi-Hart, Memory Consistency & Cache Coherence
- 纳入依据：strong phrase in title: memory consistency verification；hardware/processor object: risc-v, processor, microarchitectural, soc；verification/fuzzing method: verification, litmus
- 论文页面：[http://arxiv.org/abs/2003.04892v1](http://arxiv.org/abs/2003.04892v1)
- PDF：[https://arxiv.org/pdf/2003.04892v1](https://arxiv.org/pdf/2003.04892v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 13 页，提取 69941 字符

## 摘要

Modern SoCs are heterogeneous parallel systems comprised of components developed by distinct teams and possibly even different vendors. The memory consistency model (MCM) of processors in such SoCs specifies the ordering rules which constrain the values that can be read by load instructions in parallel programs running on such systems. The implementation of required MCM orderings can span components which may be designed and implemented by many different teams. Ideally, each team would be able to specify the orderings enforced by their components independently and then connect them together when conducting MCM verification. However, no prior automated approach for formal hardware MCM verification provided this. To bring automated hardware MCM verification in line with the realities of the design process, we present RealityCheck, a methodology and tool for automated formal MCM verification of modular microarchitectural ordering specifications. RealityCheck allows users to specify their designs as a hierarchy of distinct modules connected to each other rather than a single flat specification. It can then automatically verify litmus test programs against these modular specifications. RealityCheck also provides support for abstraction, which enables scalable verification by breaking up the verification of the entire design into smaller verification problems. We present results for verifying litmus tests on 7 different designs using RealityCheck. These include in-order and out-of-order pipelines, a non-blocking cache, and a heterogeneous processor. Our case studies cover the TSO and RISC-V (RVWMO) weak memory models. RealityCheck is capable of verifying 98 RVWMO litmus tests in under 4 minutes each, and its capability for abstraction enables up to a 32.1% reduction in litmus test verification time for RVWMO.

## 研究问题

现有自动化硬件MCM验证方法缺乏模块化、层次化和抽象支持，导致全局属性不匹配实际硬件，难以扩展。

## Introduction 梳理

现代SoC由多团队开发，但现有自动化正式硬件MCM验证方法（如Check套件、PipeProof）均为扁平化设计，不支持模块化、层次化和抽象，导致公理隐含全局可见性，与实际硬件组件分布不符，且无法独立验证组件或分步验证。为此，本文提出RealityCheck，通过μspec++语言实现模块化、层次化和抽象的自动微架构MCM验证，支持组件独立验证和分步扩展。

## 方法

输入包括μspec++实现公理文件、模块定义文件、litmus测试或接口-实现对、边界。通过μspec++定义模块事件和公理，利用连接公理映射不同模块的操作。生成公式后转化为Z3 SMT求解，通过检查μhb图是否有环判断执行是否可观察。Oracle为ISA级MCM（如SC、TSO、RVWMO）的允许/禁止行为。无需golden model，而是通过有界探索所有可能执行。

## 实验与评估

baseline: 与无接口版本对比。实验在Ubuntu 18.04、4 Intel Xeon Gold 6230（80核）、1TB RAM上运行，每线程单核。测试集：95个SC/TSO litmus测试、98个RVWMO litmus测试。统计：92/95个SC/TSO测试在4分钟内完成，RVWMO测试均在4分钟内。接口验证时间：inOrderCore <1秒，sbCore 18秒，rvwmoCore 42分钟（bound=15）；L1Hier接口验证在bound=10时>14小时。Bug发现：注入3种bug，均在≤4秒内（bound≤4）或≤2分钟（bound≤15）发现。开销：接口抽象使cacheProcTSO验证时间减少29.7%，cacheProcRISCV减少32.1%。Artifact: RealityCheck工具（Coq/Gallina + OCaml + Z3 API）。

## 核心贡献

1. 提出μspec++语言，支持模块化、层次化、抽象的微架构排序规范；2. 实现首个自动化验证模块化设计规范的框架RealityCheck；3. 通过接口分解实现可扩展验证，并展示对7种微架构的验证结果。

## 与本仓库研究主线的关系

直接相关：论文专注于多hart（多核）和内存一致性模型验证，方法涵盖RISC-V RVWMO弱内存模型，属于内存一致性验证范畴。其模块化思路可用于多hart一致性路径研究中的组件独立验证。

## 结论

RealityCheck是首个支持模块化、层次化和抽象的自动化微架构MCM验证方法，通过μspec++语言实现，能在有界范围内快速验证litmus测试并高效发现bug，为完全验证异构并行SoC迈出重要一步。

## 局限性

有界验证无法保证所有程序正确；接口验证在高边界时耗时显著（如L1Hier在bound=10超过14小时）；模块分解时若子模块间通信过多可能不适合；未支持无界证明。

## 详细阅读分析

重点关注μspec++语言设计（第V节）、连接公理如何映射操作（第V-B3节）、接口验证流程（第IV节）、抽象提高可扩展性的实验（第VIII-B节）、bug注入案例（第VIII-D节）。

## 后续核验问题

- 1. 如何将RealityCheck扩展至无界验证？2. 能否与RTLCheck结合实现RTL级模块化验证？3. 该方法是否可推广至安全属性（如微架构安全）？4. 在更大规模SoC上的扩展性如何？
