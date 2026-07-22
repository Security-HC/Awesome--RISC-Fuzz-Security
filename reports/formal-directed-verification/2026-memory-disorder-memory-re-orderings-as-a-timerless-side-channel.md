# Memory DisOrder: Memory Re-orderings as a Timerless Side-channel

## 基本信息

- 作者：Sean Siddens、Sanya Srivastava、Reese Levine、Josiah Dykstra、Tyler Sorensen
- 发表日期：2026-01-13
- 会议/期刊：arXiv
- 主分类：形式化与定向处理器验证
- 相关性：A·直接相关（score=5）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：Formal & Directed Processor Verification
- 纳入依据：hardware/processor object: processor, cpu；verification/fuzzing method: fuzz；security relevance: vulnerability
- 论文页面：[http://arxiv.org/abs/2601.08770v1](http://arxiv.org/abs/2601.08770v1)
- PDF：[https://arxiv.org/pdf/2601.08770v1](https://arxiv.org/pdf/2601.08770v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 16 页，提取 74944 字符

## 摘要

To improve efficiency, nearly all parallel processing units (CPUs and GPUs) implement relaxed memory models in which memory operations may be re-ordered, i.e., executed out-of-order. Prior testing work in this area found that memory re-orderings are observed more frequently when other cores are active, e.g., stressing the memory system, which likely triggers aggressive hardware optimizations. In this work, we present Memory DisOrder: a timerless side-channel that uses memory re-orderings to infer activity on other processes. We first perform a fuzzing campaign and show that many mainstream processors (X86/Arm/Apple CPUs, NVIDIA/AMD/Apple GPUs) are susceptible to cross-process signals. We then show how the vulnerability can be used to implement classic attacks, including a covert channel, achieving up to 16 bits/second with 95% accuracy on an Apple M3 GPU, and application fingerprinting, achieving reliable closed-world DNN architecture fingerprinting on several CPUs and an Apple M3 GPU. Finally, we explore how low-level system details can be exploited to increase re-orderings, showing the potential for a covert channel to achieve nearly 30K bits/second on X86 CPUs. More precise attacks can likely be developed as the vulnerability becomes better understood.

## 研究问题

内存重排序（memory re-ordering）现象尚未被系统性地利用作为侧信道，现有侧信道攻击通常需要定时器或性能计数器等能力，缺乏低能力、广覆盖的利用方法。

## Introduction 梳理

现有侧信道攻击依赖定时器或硬件计数器，能力要求较高。作者观察到内存重排序在系统压力下频率增加，提出无需定时器的侧信道MemoryDisOrder，利用处理器放松内存一致性模型导致的重排序来推断其他进程活动。贡献包括：提出新型侧信道、通过模糊测试验证多平台易受攻击、实现隐蔽信道和应用程序指纹识别。

## 方法

输入生成：使用6种经典litmus测试（如Message Passing, Store Buffering等）及4种测试框架（Basic, Litmus7, Perpetual, GPU Parallel），其中Basic框架由本文提出。反馈/覆盖：记录每次测试运行中观察到的重排序次数。Oracle：通过比较有无压力下的重排序频率，使用Mann-Whitney U检验和Common Language Effect Size (CLES)判断信号可靠性。DUT/平台：6种设备（Intel X86, Arm A78, Apple M1-CPU, Apple M3-GPU, NVIDIA RTX 4070, AMD RX 7900 XT），以及跨KVM边界。是否需要golden model：不需要，采用统计方法。

## 实验与评估

baseline：无压力时的重排序频率。实验预算：每个设备8小时模糊测试（overnight），每个试验含10次测试运行。统计：Mann-Whitney U检验，CLES，独立样本t-test。bug/CVE：未确认。开销：隐蔽信道速率最高16 bps（M3-GPU），指纹识别需约5秒收集30个样本。Artifact：未确认。

## 核心贡献

1. 提出MemoryDisOrder：一种利用内存重排序的无定时器侧信道。2. 通过模糊测试证明6种主流CPU/GPU易受攻击。3. 实现隐蔽信道（最高16 bps）和DNN架构指纹识别（5秒内分类）。4. 探索低层系统细节可大幅提升攻击效果（X86上近30K bps）。

## 与本仓库研究主线的关系

直接相关：该工作聚焦处理器侧信道，利用内存一致性模型的重排序行为，属于微架构安全自动测试范畴。与多hart/一致性路径研究关联紧密：侧信道利用的是多线程程序中的内存重排序，与内存一致性验证中使用的litmus测试相同，可启发一致性违规的自动检测方法。

## 结论

MemoryDisOrder是一种无定时器侧信道，广泛存在于主流CPU和GPU中，可用于实现隐蔽信道和应用程序指纹识别，且具有低能力要求、广泛影响、基于实证等特点。

## 局限性

攻击带宽有限（CPU上仅0.3-0.6 bps，GPU上16 bps）；重排序的根本硬件原因未明确，难以制定严格缓解措施；部分攻击（如X86-arch）尚不成熟；缓解措施存在性能开销或需修改应用程序。

## 详细阅读分析

建议深入阅读第3、4、5节，了解模糊测试设计、实验结果和攻击实现细节，特别是第5.3节的架构感知攻击。

## 后续核验问题

- 如何在不同微架构上自动发现类似的重排序触发条件？
- 除CPU/GPU外，其他处理器（如FPGA、NPU）是否受MemoryDisOrder影响？
- 能否利用MemoryDisOrder实现更细粒度的数据泄漏，如密钥提取？
- 是否存在不需要修改应用程序的软件缓解措施？
