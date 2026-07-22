# RTL2M$μ$PATH: Multi-$μ$PATH Synthesis with Applications to Hardware Security Verification

## 基本信息

- 作者：Yao Hsiao、Nikos Nikoleris、Artem Khyzha、Dominic P. Mulligan、Gustavo Petri、Christopher W. Fletcher、Caroline Trippel
- 发表日期：2024-09-28
- 会议/期刊：arXiv
- 主分类：多 Hart、内存一致性与缓存一致性
- 相关性：A·直接相关（score=5）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：Multi-Hart, Memory Consistency & Cache Coherence、Microarchitectural Security Testing
- 纳入依据：hardware/processor object: processor, microarchitecture, microarchitectural, rtl；verification/fuzzing method: verification；security relevance: security, side channel, leakage
- 论文页面：[http://arxiv.org/abs/2409.19478v1](http://arxiv.org/abs/2409.19478v1)
- PDF：[https://arxiv.org/pdf/2409.19478v1](https://arxiv.org/pdf/2409.19478v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 18 页，提取 100000 字符

## 摘要

The Check tools automate formal memory consistency model and security verification of processors by analyzing abstract models of microarchitectures, called $μ$SPEC models. Despite the efficacy of this approach, a verification gap between $μ$SPEC models, which must be manually written, and RTL limits the Check tools' broad adoption. Our prior work, called RTL2$μ$SPEC, narrows this gap by automatically synthesizing formally verified $μ$SPEC models from SystemVerilog implementations of simple processors. But, RTL2$μ$SPEC assumes input designs where an instruction (e.g., a load) cannot exhibit more than one microarchitectural execution path ($μ$PATH, e.g., a cache hit or miss path) -- its single-execution-path assumption. In this paper, we first propose an automated approach and tool, called RTL2M$μ$PATH, that resolves RTL2$μ$SPEC's single-execution-path assumption. Given a SystemVerilog processor design, instruction encodings, and modest design metadata, RTL2M$μ$PATH finds a complete set of formally verified $μ$PATHs for each instruction. Next, we make an important observation: an instruction that can exhibit more than one $μ$PATH strongly indicates the presence of a microarchitectural side channel in the input design. Based on this observation, we then propose an automated approach and tool, called SynthLC, that extends RTL2M$μ$PATH with a symbolic information flow analysis to support synthesizing a variety of formally verified leakage contracts from SystemVerilog processor designs. Leakage contracts are foundational to state-of-the-art defenses against hardware side-channel attacks. SynthLC is the first automated methodology for formally verifying hardware adherence to them.

## 研究问题

RTL2μSPEC 假设每个指令只有单一微架构执行路径（μPATH），这限制了其在具有缓存、可变延迟单元等特性的处理器上的应用，并无法用于微架构侧信道验证。本文旨在自动从 RTL 合成多 μPATH，并利用多 μPATH 检测微架构侧信道，从而自动生成泄漏契约。

## Introduction 梳理

Check 工具通过分析手动编写的 μSPEC 模型进行形式化一致性/安全验证，但手动编写 μSPEC 模型存在验证鸿沟。之前工作 RTL2μSPEC 能自动从简单处理器 RTL 合成 μSPEC 模型，但假设单一路径。本文提出 RTL2MμPATH 解决该假设，发现多 μPATH 强烈指示侧信道存在，进而提出 SynthLC 自动合成多种形式化验证的泄漏契约。

## 方法

输入：SystemVerilog 设计、指令编码、设计元数据（包括 μFSM 的 PCR 和状态变量、提交信号、寄存器文件、内存等）。RTL2MμPATH 使用静态网表分析、LTL 属性生成（从模板）和模型检查，通过扩展 μHB 图至周期精度、将 μHB 节点映射到执行地点（PL）来发现每个指令的完整 μPATH 集。SynthLC 扩展 RTL2MμPATH，添加符号信息流分析（IFT 电路），通过模型检查判断候选转发器决策是否依赖于发射器操作数（分为内在、动态、静态）。需要用户提供元数据，不需要 golden model。DUT 为 CV A6 核心和缓存。Oracle 为基于 IFT 的符号分析。

## 实验与评估

在 RV64IM 的 CV A6 核心（8,577 行 SystemVerilog）和 L1 数据缓存（2,279 行）上评估。RTL2MμPATH 评估 124,459 个属性，平均 4.43 分钟/属性，16.39% 未定；SynthLC 评估 30,774 个属性，平均 2.35 分钟/属性，13.74% 未定；缓存评估 4,178 个属性，平均 3 秒内完成。发现 94 个唯一泄漏签名、72 个转发器、26 个发射器，包括一个之前未报道的存储-加载地址匹配通道。发现三个功能 bug（两个有安全影响）。开销：需用户标注 21 个 μFSM（7 个原始 + 14 个加）、1 个 IFR、1 个提交信号、2 个寄存器文件、1 个内存。Artifact 开源。

## 核心贡献

1) 提出 RTL2MμPATH，自动从 RTL 合成每个指令的完整形式化验证的 μPATH 集合，解决了单路径假设。2) 观察到指令的 μPATH 可变性强烈指示微架构侧信道，引入转发器（transponder）概念。3) 提出 SynthLC，第一个自动从 RTL 合成微架构泄漏契约的方法，支持 CT、STT、SDO 等六种契约，并发现新侧信道和处理器 bug。

## 与本仓库研究主线的关系

直接相关。该论文聚焦 RISC-V 处理器（CV A6）的微架构路径合成与安全验证，属于本仓库的 RISC-V/处理器 Fuzzing、微架构安全自动测试核心主题。其方法（自动化 μPATH 探索、泄漏契约合成）可直接用于多 hart/一致性验证路径研究（μHB 图基础），并为硬件 Fuzzing 提供 oracle 和覆盖指导。

## 结论

本文设计了第一个自动从 RTL 合成多 μPATH 的工具 RTL2MμPATH，并基于该观察自动合成微架构泄漏契约（SynthLC），支持六种泄漏契约和十种防御机制。

## 局限性

SynthLC 存在假阳性（14/94 泄漏签名有额外显式输入）由 IFT 不精确导致；模型检查器未定结果（16.39% 属性）导致不完整性；需要用户提供较多元数据（μFSM 等），可能增加人工负担；评估限于单个单核处理器 CV A6 和简化缓存，扩展性待验证。

## 详细阅读分析

建议深入学习 RTL2MμPATH 的 PL 识别方法（μFSM 与 LTL 属性生成）和 SynthLC 的符号信息流分析，特别是如何将决策归因于发射器类型，这对自动化安全评估至关重要。

## 后续核验问题

- 1) 如何将该方法扩展到多核/多 hart 处理器以验证内存一致性？2) 如何处理更大规模设计（如 BOOM）中的状态爆炸？3) 如何减少 IFT 假阳性以提升泄漏契约的精确性？4) 该方法需要的人工元数据标注能否自动化？
