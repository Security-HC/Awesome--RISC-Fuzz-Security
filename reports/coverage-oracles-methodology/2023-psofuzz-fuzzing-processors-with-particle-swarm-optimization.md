# PSOFuzz: Fuzzing Processors with Particle Swarm Optimization

## 基本信息

- 作者：Chen Chen、Vasudev Gohil、Rahul Kande、Ahmad-Reza Sadeghi、Jeyavijayan Rajendran
- 发表日期：2023-07-26
- 会议/期刊：arXiv
- 主分类：覆盖、Oracle 与 Fuzzing 方法
- 相关性：A·直接相关（score=8）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：Coverage, Oracles & Fuzzing Methodology
- 纳入依据：strong phrase in abstract: hardware fuzzing；hardware/processor object: processor；verification/fuzzing method: fuzz；security relevance: security, vulnerability
- 论文页面：[http://arxiv.org/abs/2307.14480v2](http://arxiv.org/abs/2307.14480v2)
- PDF：[https://arxiv.org/pdf/2307.14480v2](https://arxiv.org/pdf/2307.14480v2)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 9 页，提取 47657 字符

## 摘要

Hardware security vulnerabilities in computing systems compromise the security defenses of not only the hardware but also the software running on it. Recent research has shown that hardware fuzzing is a promising technique to efficiently detect such vulnerabilities in large-scale designs such as modern processors. However, the current fuzzing techniques do not adjust their strategies dynamically toward faster and higher design space exploration, resulting in slow vulnerability detection, evident through their low design coverage. To address this problem, we propose PSOFuzz, which uses particle swarm optimization (PSO) to schedule the mutation operators and to generate initial input programs dynamically with the objective of detecting vulnerabilities quickly. Unlike traditional PSO, which finds a single optimal solution, we use a modified PSO that dynamically computes the optimal solution for selecting mutation operators required to explore new design regions in hardware. We also address the challenge of inefficient initial seed generation by employing PSO-based seed generation. Including these optimizations, our final formulation outperforms fuzzers without PSO. Experiments show that PSOFuzz achieves up to 15.25$\times$ speedup for vulnerability detection and up to 2.22$\times$ speedup for coverage compared to the state-of-the-art simulation-based hardware fuzzer.

## 研究问题

当前硬件fuzzer使用静态的变异操作符调度和种子生成策略，不能根据覆盖率动态调整，导致设计空间探索缓慢、漏洞检测慢。

## Introduction 梳理

已有fuzzer（如TheHuzz、DIFUZZRTL等）采用静态调度策略，覆盖率增长停滞。本文首次将粒子群优化（PSO）引入硬件fuzzing，用于动态调度变异操作符和生成种子，并提出重置策略防止粒子饱和。

## 方法

输入生成：二进制可执行程序（RISC-V指令序列）。变异操作符：Bitflip、OpcodeMut等（具体列表未完全给出）。反馈/coverage：分支覆盖率（主报告指标），沿用TheHuzz的多种覆盖率反馈。Oracle：将DUT输出与黄金参考模型Spike（RISC-V ISA模拟器）比较，检测架构状态失配。DUT/平台：CVA6（OoO）、BOOM（超标量）、Rocket Core（顺序），Synopsys VCS仿真，Chipyard SoC环境。需要golden model：是，Spike。

## 实验与评估

baseline：TheHuzz（状态最先进的仿真硬件fuzzer）。实验预算：每个benchmark运行24小时，重复3次。统计：速度提升（speedup）和覆盖率增量。bug/CVE：在CVA6上检测到7个漏洞（V1-V7），Rocket Core上1个（V8），分类为CWE-1252等，未提及CVE编号。开销：未明确测量，但提到阈值β影响运行时间开销。Artifact：未提供开源仓库或具体Artifact。

## 核心贡献

1) 首次将PSO用于硬件fuzzing的变异操作符调度和种子生成；2) 解决PSO应用于硬件fuzzing的挑战：粒子饱和问题（重置策略）和无效种子生成（PSO种子生成）；3) 实验验证在三个处理器上加速漏洞检测和覆盖率。

## 与本仓库研究主线的关系

直接相关：主题为RISC-V处理器fuzzing，使用覆盖反馈和GRM Oracle。与多hart/一致性路径研究的关系：论文未涉及多hart或内存一致性，但方法可扩展至多核。属于覆盖与fuzzing方法论。

## 结论

PSOFuzz通过动态调度变异操作符和种子生成，显著提高漏洞检测速度和覆盖率，在三个RISC-V处理器上漏洞检测加速最高15.25倍，覆盖率加速最高2.22倍。

## 局限性

1) 重置策略是启发式，未建模分析β的影响；2) 仅评估三个RISC-V处理器，通用性有限；3) 仅与TheHuzz对比，未与其他fuzzer比较；4) PSOFuzz在CVA6上速度略低于PSO+Reset（因为初始种子探索）；5) 未考虑其他元启发式算法（如模拟退火）。

## 详细阅读分析

已阅读全文，理解PSO集成、重置机制和种子生成。重点关注粒子饱和问题及动态调整变异权重。

## 后续核验问题

- 重置阈值β如何影响性能？是否有理论分析？
- 是否考虑了多核或一致性验证？
- 与其他元启发式（如模拟退火）的比较？
- 是否开源？代码是否可用？
- 不同覆盖率指标（如FSM覆盖率）下的表现如何？
