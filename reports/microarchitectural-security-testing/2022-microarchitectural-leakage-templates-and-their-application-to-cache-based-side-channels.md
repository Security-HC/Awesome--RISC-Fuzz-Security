# Microarchitectural Leakage Templates and Their Application to Cache-Based Side Channels

## 基本信息

- 作者：Ahmad Ibrahim、Hamed Nemati、Till Schlüter、Nils Ole Tippenhauer、Christian Rossow
- 发表日期：2022-11-25
- 会议/期刊：arXiv
- 主分类：微架构安全自动测试
- 相关性：A·直接相关（score=5）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：Microarchitectural Security Testing
- 纳入依据：hardware/processor object: processor, cpu, microarchitectural；verification/fuzzing method: fuzz；security relevance: vulnerability, side channel, leakage
- 论文页面：[http://arxiv.org/abs/2211.13958v1](http://arxiv.org/abs/2211.13958v1)
- PDF：[https://arxiv.org/pdf/2211.13958v1](https://arxiv.org/pdf/2211.13958v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 15 页，提取 94813 字符

## 摘要

The complexity of modern processor architectures has given rise to sophisticated interactions among their components. Such interactions may result in potential attack vectors in terms of side channels, possibly available to user-land exploits to leak secret data. Exploitation and countering of such side channels require a detailed understanding of the target component. However, such detailed information is commonly unpublished for many CPUs. In this paper, we introduce the concept of Leakage Templates to abstractly describe specific side channels and identify their occurrences in binary applications. We design and implement Plumber, a framework to derive the generic Leakage Templates from individual code sequences that are known to cause leakage (e.g., found by prior work). Plumber uses a combination of instruction fuzzing, instructions' operand mutation and statistical analysis to explore undocumented behavior of microarchitectural optimizations and derive sufficient conditions on vulnerable code inputs that, if hold can trigger a distinguishing behavior. Using Plumber we identified novel leakage primitives based on Leakage Templates (for ARM Cortex-A53 and -A72 cores), in particular related to previction (a new premature cache eviction), and prefetching behavior. We show the utility of Leakage Templates by re-identifying a prefetcher-based vulnerability in OpenSSL 1.1.0g first reported by Shin et al. [40].

## 研究问题

如何从已知的泄露代码示例泛化出通用的Leakage Templates（LTs），并利用这些模板在二进制应用中自动化识别缓存在微架构层面的侧信道漏洞。

## Introduction 梳理

现有微架构侧信道发现方法（如ABSynthe、Osiris、Transynther）虽实现了自动化，但局限于特定攻击向量（如竞争、Meltdown），搜索空间有限（忽略操作数变异性），且侧重于生成攻击代码而非提取通用可匹配的泄露模式。本文引入Leakage Templates概念，它由泛化代码序列和输入参数关系构成，触发特定微架构行为。设计Plumber框架，通过指令fuzzing、操作数变异和统计分析从已知泄露示例中自动推导LTs，并展示其在ARM Cortex-A53/A72上的应用，发现previction和prefetching相关的新型侧信道。

## 方法

输入生成：基于生成性测试用例规范（GTS）的领域特定语言，通过指令fuzzing、操作数变异（如地址偏移蛮力）、宏（如通配符、排列）生成大量程序-输入对。反馈/coverage：通过ARM TrustZone特权调试接口直接读取缓存状态，或使用Flush+Reload等侧信道探针测量微架构行为（如缓存内容、执行时间），分类器根据行为生成位表。Oracle：需要已知的泄露示例（如来自Scam-V或手动）作为起点；无需golden model。DUT/平台：ARM Cortex-A53（Raspberry Pi 3）和Cortex-A72（Raspberry Pi 4）裸机环境，使用ARM TrustZone获取最高特权。

## 实验与评估

baseline：与Scam-V等工具互补，但无直接性能对比；实验预算：表2给出各实验总执行时间（eviction 62分钟，previction 0.7天，prefetching 4天等）；统计：使用混淆矩阵（表5）评估LT对prefetching行为的分类性能（66例P0正确，6例P3正确，无错误分类，28例因参数超出训练范围而无法判定）；bug/CVE：重新识别了OpenSSL 1.1.0g中由Shin等人首先报告的prefetcher漏洞；开销：实验时间见表格，硬件为5个Pi 3和1个Pi 4；Artifact：Plumber源码公开于[36]。

## 核心贡献

1. 提出Leakage Templates概念，用于泛化描述侧信道并匹配应用中的漏洞。2. 设计并实现Plumber框架，通过指令fuzzing、操作数变异和统计分析自动生成LTs。3. 发现ARM Cortex-A53/A72上5个新型侧信道原语（PR_FR、PR_PP、PRF_CF、PRF_IS、PRF_OS）。4. 展示LT用于重新识别OpenSSL中已知prefetching漏洞。

## 与本仓库研究主线的关系

直接相关。论文属于微架构安全测试和硬件fuzzing领域，核心方法（指令序列生成、统计行为分类）与处理器fuzzing高度契合。与多hart/一致性路径研究间接相关：侧信道利用可影响共享缓存行为，进而干扰内存一致性验证；而多hart场景下的cache coherence亦可能受此类泄露影响。

## 结论

Leakage Templates抽象描述了特定侧信道及其触发条件，Plumber通过指令fuzzing和统计分析自动推导LTs。实验证明LTs能有效发现ARM Cortex-A53/A72上的previction和prefetching侧信道，并识别出5个新型泄露原语。LTs还可用于逆向工程（如分支预测器），并可在二进制中匹配已知漏洞。

## 局限性

当前Plumber实现主要针对缓存侧信道，且限于ARM架构（ARMv7/v8和RISC-V）；移植到x86需替换ARM TrustZone的检测模块为Flush+Reload等替代机制。推导的LTs可能不完整（如实验未覆盖的参数范围导致未定类），依赖于用户对潜在泄露行为的先验知识。分支预测器逆向工程的结论基于对PHT结构的假设，未充分验证。

## 详细阅读分析

建议阅读Scam-V [28]以了解侧信道泄露示例的生成方法；ABSynthe [11]和Osiris [51]作为本工作的直接前驱；Transynther [27]用于对比攻击合成方法；以及Shin等人[40]的prefetching攻击以理解验证案例。

## 后续核验问题

- Plumber如何扩展至x86等复杂架构以应对不同的微架构特性？如何衡量LT的完备性并处理大型程序中的代码段匹配？如何将LT应用到多核/多hart环境中以发现跨核心一致性相关的侧信道？
