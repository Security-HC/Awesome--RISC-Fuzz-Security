# BETA: Automated Black-box Exploration for Timing Attacks in Processors

## 基本信息

- 作者：Congcong Chen、Jinhua Cui、Jiliang Zhang
- 发表日期：2024-10-22
- 会议/期刊：arXiv
- 主分类：微架构安全自动测试
- 相关性：A·直接相关（score=5）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：Microarchitectural Security Testing、Coverage, Oracles & Fuzzing Methodology
- 纳入依据：hardware/processor object: processor, microarchitecture, microarchitectural；verification/fuzzing method: fuzz；security relevance: security
- 论文页面：[http://arxiv.org/abs/2410.16648v1](http://arxiv.org/abs/2410.16648v1)
- PDF：[https://arxiv.org/pdf/2410.16648v1](https://arxiv.org/pdf/2410.16648v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 13 页，提取 73687 字符

## 摘要

Modern processor advancements have introduced security risks, particularly in the form of microarchitectural timing attacks. High-profile attacks such as Meltdown and Spectre have revealed critical flaws, compromising the entire system's security. Recent black-box automated methods have demonstrated their advantages in identifying these vulnerabilities on various commercial processors. However, they often focus on specific attack types or incorporate numerous ineffective test cases, which severely limits the detection scope and efficiency. In this paper, we present BETA, a novel black-box framework that harnesses fuzzing to efficiently uncover multifaceted timing vulnerabilities in processors. Our framework employs a two-pronged approach, enhancing both mutation space and exploration efficiency: 1) we introduce an innovative fuzzer that precisely constrains mutation direction for diverse instruction combinations, including opcode, data, address, and execution level; 2) we develop a coverage feedback mechanism based on our instruction classification to discard potentially trivial or redundant test cases. This mechanism significantly expands coverage across a broader spectrum of instruction types. We evaluate the performance and effectiveness of BETA on four processors from Intel and AMD, each featuring distinct microarchitectures. BETA has successfully detected all x86 processor vulnerabilities previously identified by recent black-box methods, as well as 8 previously undiscovered timing vulnerabilities. BETA outperforms the existing state-of-the-art black-box methods, achieving at least 3x faster detection speed.

## 研究问题

现有黑盒方法在发现处理器微架构时序漏洞时，检测范围有限、效率低下，且多局限于特定攻击类型或包含大量无效测试用例。

## Introduction 梳理

现有黑盒自动时序漏洞检测方法（如Osiris）依赖随机指令生成，缺乏覆盖反馈，导致检测效率低且无法覆盖多种漏洞类型。本文提出BETA框架，通过约束变异方向和基于指令分类的覆盖反馈，高效发现多种时序漏洞。

## 方法

输入生成：从uops.info提取指令列表，预处理过滤异常指令，通过变异（位翻转、拼接、插入）生成测试序列。反馈/覆盖：基于ISA-set的指令分类覆盖反馈，记录已测试类型组合，避免重复。Oracle：比较有无触发时的执行时间差，阈值设10或20 cycles。DUT/平台：Intel i5-8400, i7-4790, Xeon 8444H, AMD Ryzen 5 5600U。无需golden model。

## 实验与评估

baseline：Osiris。实验预算：超过100小时（每平台约3天）。统计：发现12个已知和8个新时序通道。bug/CVE：未明确提及CVE。开销：检测速度至少比Osiris快3倍（22小时 vs Osiris的约7.8倍时间）。Artifact：未确认。

## 核心贡献

提出了BETA框架，包含约束变异方向的fuzzer和基于指令分类的覆盖率反馈机制，首次在黑盒处理器中高效检测多种时序漏洞（包括数据、易失、持久信道），并发现8个新漏洞。

## 与本仓库研究主线的关系

直接相关：针对处理器时序漏洞的黑盒fuzzing方法。与多hart/内存一致性验证不直接相关，但其覆盖反馈和变异策略可借鉴于其他硬件fuzzing场景。

## 结论

BETA能够高效自动发现处理器中的多种微架构时序漏洞，并验证其可用于构建隐蔽信道和瞬态执行攻击。

## 局限性

1）未完全测试eviction-based通道（时间限制）；2）指令分类粒度较粗（仅基于ISA-set），更细分类可能发现新漏洞但扩大测试空间；3）每组合测试的指令数T的最优值需进一步研究。

## 详细阅读分析

重点阅读第4节（种子变异、fuzzer设计、覆盖反馈）、第5节（新漏洞的发现与验证）和第6节（讨论与局限）。

## 后续核验问题

- BETA如何扩展以检测eviction-based side channels？
- 指令分类的粒度如何影响覆盖率和检测效率？
- BETA能否应用于RISC-V处理器或非x86架构？
