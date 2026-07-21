# PowerFuzz: Power-Based Black-Box Firmware Fuzzing

## 基本信息

- 作者：Dakshina Tharindu、Sahan Sanjaya、Philip Baptist、Prabhat Mishra
- 发表日期：2026-06-23
- 更新日期：2026-06-23
- 来源：arXiv
- 来源编号：2606.24692v1
- 研究类别：RTL 与硬件验证、工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2606.24692v1](http://arxiv.org/abs/2606.24692v1)
- PDF：[https://arxiv.org/pdf/2606.24692v1](https://arxiv.org/pdf/2606.24692v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash

## 摘要

Fuzzing is widely used for software and hardware verification, offering an effective alternative to random testing. While gray-box fuzzers benefit from full visibility into the system under test and can leverage execution feedback such as branch coverage, these approaches are not applicable when verifying systems whose firmware or binaries are not publicly available. In such scenarios, obtaining coverage information for guiding the fuzzer becomes infeasible. In this paper, we introduce PowerFuzz, a statistical black-box fuzzing framework that leverages power side-channel measurements as a substitute for binary instrumentation, requiring no internal visibility into the target firmware. A central challenge in black-box firmware fuzzing is determining the executed branches during test execution. To address this challenge, we use power traces to identify branches utilizing a sliding window followed by a growing window full-trace correlation method. This approach also enables the construction of a high-level control-flow graph of the black-box firmware, which we utilize to drive the fuzzer to unexplored execution paths. Extensive evaluation using three embedded hardware platforms and ten firmware benchmarks demonstrates that PowerFuzz can provide branch coverage comparable (within 13.5%) to gray-box fuzzers while significantly outperforming (up to 22%) state-of-the-art black-box fuzzers.

## 研究问题

黑盒固件模糊测试中，由于固件二进制不可访问，无法获取分支覆盖反馈来指导变异，导致模糊测试效率低下。现有方法如电磁侧信道需要昂贵设备，而功耗侧信道尚未被利用。

## Introduction 梳理

嵌入式设备固件常因加密或专有而不可获取，传统灰盒模糊测试依赖二进制插桩获取分支覆盖率，无法用于黑盒场景。本文提出PowerFuzz，首次利用功耗侧信道测量作为黑盒固件模糊测试的反馈机制，通过功耗迹分析推断执行路径，构建迹引导控制流图（TCFG），驱动变异引擎探索新路径。

## 方法

PowerFuzz包含三个核心模块：1）相似性分析：使用滑动窗口和增长窗口全迹相关方法，结合动态时间规整（DTW）比较当前功耗迹与已存储迹，检测执行分支分歧；2）动态TCFG构建：基于检测到的分歧，增量构建TCFG，节点存储基本块对应的功耗迹段，边表示分支转移；3）分支选择：利用TCFG识别未探索路径，通过深度优先策略选择分支，指导AFL变变异引擎生成新输入。

## 实验与评估

在三个嵌入式硬件平台（如STM32等）和十个固件基准上评估，与灰盒模糊器（AFL等）对比，PowerFuzz的分支覆盖度在13.5%以内；相比最先进的黑盒模糊器（如EM-Fuzz），覆盖度提升高达22%。使用分支覆盖率、路径发现数等指标。

## 结论

PowerFuzz是首个基于功耗侧信道黑盒固件模糊测试框架，通过功耗迹替代二进制插桩实现覆盖引导，实验表明其性能接近灰盒模糊器，显著优于现有黑盒方法，为无固件二进制访问场景提供了有效验证手段。

## 局限性

1）依赖外部物理测量设备，需要精确的同步触发和功率采集，可能受环境噪声和测量误差影响；2）仅适用于可测量功耗的微控制器，对于功耗变化不敏感或包含复杂外设的系统可能效果有限；3）TCFG可能无法完全等价于真实CFG，尤其是当某些分支未被触发时；4）实验仅基于三个平台和十个基准，通用性需进一步验证。

## 详细阅读分析

论文的核心创新在于利用功耗迹的时间序列相似性检测分支执行差异，并动态构建TCFG。关键挑战是区分数据依赖和操作依赖引起的功耗变化，作者通过DTW和相关性分析实现。同时，滑动窗口和增长窗口方法降低了计算开销。未来可探索多侧信道融合或机器学习方法提高分支识别精度。

## 后续跟进问题

- PowerFuzz如何处理多任务或中断导致的功耗迹混叠？
- 对于不同架构（如RISC-V）的微控制器，功耗迹的区分度是否足够？
- 能否结合其他侧信道（如电磁）提高分支识别鲁棒性？
- TCFG的构建是否需要大量初始种子来建立基线？
- PowerFuzz是否适用于非嵌入式系统（如SoC）？
