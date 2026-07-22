# Scalable Test Generation to Trigger Rare Targets in High-Level Synthesizable IPs for Cloud FPGAs

## 基本信息

- 作者：Mukta Debnath、Animesh Basak Chowdhury、Debasri Saha、Susmita Sur-Kolay
- 发表日期：2024-05-30
- 会议/期刊：arXiv
- 主分类：RTL 与 SoC 硬件 Fuzzing
- 相关性：A·直接相关（score=5）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：RTL & SoC Hardware Fuzzing、Coverage, Oracles & Fuzzing Methodology、Benchmarks, Bug Injection & Artifacts
- 纳入依据：hardware/processor object: processor, rtl；verification/fuzzing method: fuzz, test generation；security relevance: security, leakage
- 论文页面：[http://arxiv.org/abs/2405.19948v1](http://arxiv.org/abs/2405.19948v1)
- PDF：[https://arxiv.org/pdf/2405.19948v1](https://arxiv.org/pdf/2405.19948v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 27 页，提取 97110 字符

## 摘要

High-Level Synthesis (HLS) has transformed the development of complex Hardware IPs (HWIP) by offering abstraction and configurability through languages like SystemC/C++, particularly for Field Programmable Gate Array (FPGA) accelerators in high-performance and cloud computing contexts. These IPs can be synthesized for different FPGA boards in cloud, offering compact area requirements and enhanced flexibility. HLS enables designs to execute directly on ARM processors within modern FPGAs without the need for Register Transfer Level (RTL) synthesis, thereby conserving FPGA resources. While HLS offers flexibility and efficiency, it also introduces potential vulnerabilities such as the presence of hidden circuitry, including the possibility of hosting hardware trojans within designs. In cloud environments, these vulnerabilities pose significant security concerns such as leakage of sensitive data, IP functionality disruption and hardware damage, necessitating the development of robust testing frameworks. This research presents an advanced testing approach for HLS-developed cloud IPs, specifically targeting hidden malicious functionalities that may exist in rare conditions within the design. The proposed method leverages selective instrumentation, combining greybox fuzzing and concolic execution techniques to enhance test generation capabilities. Evaluation conducted on various HLS benchmarks, possessing characteristics of FPGA-based cloud IPs with embedded cloud related threats, demonstrates the effectiveness of our framework in detecting trojans and rare scenarios, showcasing improvements in coverage, time efficiency, memory usage, and testing costs compared to existing methods.

## 研究问题

云FPGA环境中高层次综合（HLS）IP的硬件木马检测，特别是隐藏在稀有条件中的恶意功能。

## Introduction 梳理

HLS在云FPGA中广泛应用，但第三方IP可能包含硬件木马，在稀有条件下触发，造成安全威胁。现有方法如模糊测试（AFL）难以满足复杂条件分支，符号执行（S2E）存在可扩展性问题。本文提出GreyConE+框架，结合灰盒模糊测试和符号执行，并引入选择性插桩技术，高效触发稀有目标，检测木马。贡献包括混成测试框架、选择性插桩、参考模型验证等。

## 方法

输入生成：初始随机测试识别稀有目标；然后灰盒模糊测试（AFL）和符号执行（S2E）交替进行。反馈/覆盖：覆盖引导，重点跟踪稀有分支的覆盖。Oracle：通过参考模型生成的查找表（LUT）提供正确输出，与DUT输出比较。DUT/平台：HLS编写的SystemC/C++设计，未指定具体FPGA平台，实验在x86 Linux上运行。不需要golden model？是，需要可信第三方提供的参考模型，但作者声称无golden时也可通过覆盖驱动检测。

## 实验与评估

baseline：AFL、S2E、GreyConE以及AFL-SHT、SCT-HTD等先前工作。实验预算：2小时时间限制，5秒和10秒的引擎切换阈值。统计指标：稀有目标覆盖数、时间、测试用例数、分支覆盖率、内存使用。bug/CVE：检测到所有基准中的木马，无CVE报告。开销：时间开销降低（见图5），内存使用比纯符号执行低（图7）。Artifact：使用S3CBench、S2CBench、SCBench、Rosetta等公开基准，未提及提供新工具或数据。

## 核心贡献

1. 提出GreyConE+框架，结合灰盒模糊测试和符号执行，用于HLS IP的稀有目标触发和木马检测。2. 引入选择性插桩技术，减少不必要的插桩，提升效率。3. 采用参考模型验证流程，在云FPGA场景下实现安全测试。

## 与本仓库研究主线的关系

直接相关：属于RTL & SoC Hardware Fuzzing主题。不涉及多hart或内存一致性验证，但其混合fuzzing方法可借鉴到处理器核微架构级fuzzing中。

## 结论

GreyConE+能更快覆盖稀有目标并有效检测木马，在时间、测试用例数和内存方面优于先前方法。但结果依赖随机输入和阈值参数，未来需改进泛化性。

## 局限性

框架效果高度依赖随机输入选择和阈值参数设置；目前仅针对HLS设计，未验证RTL；对更大设计（如多核）的可扩展性未评估。

## 详细阅读分析

需要深入理解选择性插桩的IRL优化策略（基于支配树），以及AFL与S2E交替切换的阈值逻辑。参考模型的LUT通信协议也是关键。

## 后续核验问题

- 1. 选择性插桩如何自动化，无需手动指定稀有目标？2. 该方法能否直接应用于RTL级（如Verilog）设计？3. 在多核或SoC环境下，如何扩展以同时测试多个hart的一致性？4. 与DirectFuzz等RTL fuzzer相比，性能如何？
