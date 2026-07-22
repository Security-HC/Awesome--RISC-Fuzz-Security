# Beyond Random Inputs: A Novel ML-Based Hardware Fuzzing

## 基本信息

- 作者：Mohamadreza Rostami、Marco Chilese、Shaza Zeitouni、Rahul Kande、Jeyavijayan Rajendran、Ahmad-Reza Sadeghi
- 发表日期：2024-04-10
- 会议/期刊：arXiv
- 主分类：RISC-V 处理器 Fuzzing
- 相关性：A·直接相关（score=10）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：RISC-V Processor Fuzzing、Coverage, Oracles & Fuzzing Methodology、Formal & Directed Processor Verification
- 纳入依据：strong phrase in title: hardware fuzzing；hardware/processor object: risc-v, riscv, processor；verification/fuzzing method: fuzz, verification, formal verification；security relevance: security, vulnerability
- 论文页面：[http://arxiv.org/abs/2404.06856v1](http://arxiv.org/abs/2404.06856v1)
- PDF：[https://arxiv.org/pdf/2404.06856v1](https://arxiv.org/pdf/2404.06856v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 6 页，提取 36582 字符

## 摘要

Modern computing systems heavily rely on hardware as the root of trust. However, their increasing complexity has given rise to security-critical vulnerabilities that cross-layer at-tacks can exploit. Traditional hardware vulnerability detection methods, such as random regression and formal verification, have limitations. Random regression, while scalable, is slow in exploring hardware, and formal verification techniques are often concerned with manual effort and state explosions. Hardware fuzzing has emerged as an effective approach to exploring and detecting security vulnerabilities in large-scale designs like modern processors. They outperform traditional methods regarding coverage, scalability, and efficiency. However, state-of-the-art fuzzers struggle to achieve comprehensive coverage of intricate hardware designs within a practical timeframe, often falling short of a 70% coverage threshold. We propose a novel ML-based hardware fuzzer, ChatFuzz, to address this challenge. Ourapproach leverages LLMs like ChatGPT to understand processor language, focusing on machine codes and generating assembly code sequences. RL is integrated to guide the input generation process by rewarding the inputs using code coverage metrics. We use the open-source RISCV-based RocketCore processor as our testbed. ChatFuzz achieves condition coverage rate of 75% in just 52 minutes compared to a state-of-the-art fuzzer, which requires a lengthy 30-hour window to reach a similar condition coverage. Furthermore, our fuzzer can attain 80% coverage when provided with a limited pool of 10 simulation instances/licenses within a 130-hour window. During this time, it conducted a total of 199K test cases, of which 6K produced discrepancies with the processor's golden model. Our analysis identified more than 10 unique mismatches, including two new bugs in the RocketCore and discrepancies from the RISC-V ISA Simulator.

## 研究问题

现有硬件fuzzer在复杂处理器设计上难以在合理时间内达到高覆盖率，通常低于70%，主要受限于随机输入生成效率低和缺乏引导性。

## Introduction 梳理

传统硬件验证方法如随机回归和形式验证分别存在效率低和手动工作量大、状态爆炸等问题。硬件fuzzing虽有效但覆盖率仍不足，特别是对RISC-V RocketCore等复杂设计，现有fuzzer需30小时才能达到约75%条件覆盖率。本文提出ChatFuzz，利用LLM学习机器语言生成相互依赖的指令序列，结合RL用覆盖率反馈优化，旨在快速提升覆盖率。

## 方法

输入生成：基于GPT2的LLM，三步训练：（1）无监督学习机器语言结构；（2）使用反汇编器作为奖励进行PPO-RL，清除无效指令；（3）使用RTL仿真条件覆盖率作为奖励进行PPO-RL，优化生成。反馈/覆盖率：Synopsys VCS报告的条件覆盖率，分为单次、增量和总覆盖率。Oracle：差分测试，比较DUT（RocketCore/BOOM）与golden model（RISC-V ISA Simulator Spike）的执行迹。DUT/平台：RISC-V RocketCore和BOOM，在Chipyard仿真环境中，使用10个Synopsys VCS实例。需要golden model（Spike）。

## 实验与评估

baseline：TheHuzz（以及DifuzzRTL）。实验预算：10个VCS实例，24小时，重复3次。统计：ChatFuzz在RocketCore上52分钟达到74.96%条件覆盖率（TheHuzz需30小时，快34.6×）；最终用199K测试达到79.14%（TheHuzz为76.7%）。在BOOM上49分钟达到97.02%。发现5,866个迹不匹配，经自动过滤得100+唯一不匹配，包括两个新bug：cache coherency管理问题（CWE-1202）和执行迹问题（CWE-440）。还发现RISC-V规范角落案例偏差。开销：使用Synopsys VCS和Spike，训练在高端服务器上进行。Artifact：开源RocketCore和BOOM处理器，但ChatFuzz代码未明确开源。

## 核心贡献

第一个将ML（LLM+RL）用于处理器fuzzing的工作；三步训练方法生成相互依赖的指令序列；在RocketCore上达到同等覆盖率比TheHuzz快34.6×；发现两个新bug（CWE-1202和CWE-440）。

## 与本仓库研究主线的关系

直接相关：聚焦RISC-V处理器fuzzing，使用RocketCore和BOOM。虽主要关注单核覆盖率，但发现的cache coherency bug直接与多hart/一致性验证相关，为一致性测试提供案例。

## 结论

ChatFuzz显著加速了条件覆盖率的提升，比当前最先进fuzzer快34.6倍，并发现新漏洞和规范偏差，展示了ML在硬件fuzzing中的有效性。

## 局限性

论文未明确列出局限性，但隐含包括：仅评估了两个RISC-V处理器（RocketCore和BOOM），泛化性未验证；训练需要大量机器码数据集（约500K来自Linux内核）；RL训练可能需要较多计算资源；未讨论多核扩展。

## 详细阅读分析

论文仅6页，内容紧凑，方法新颖（LLM+RL），实验设计清晰，值得精读以借鉴其ML引导生成思想。

## 后续核验问题

- 如何将ChatFuzz扩展到多核RISC-V处理器？
- 训练数据量对效果的影响如何？
- 能否复现其训练和实验结果？
- 在不同ISA（如ARM）上表现如何？
