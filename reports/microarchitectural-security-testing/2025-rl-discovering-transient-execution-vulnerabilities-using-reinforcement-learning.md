# μRL: Discovering Transient Execution Vulnerabilities Using Reinforcement Learning

## 基本信息

- 作者：M. Caner Tol、Kemal Derya、Berk Sunar
- 发表日期：2025-02-20
- 会议/期刊：arXiv
- 主分类：微架构安全自动测试
- 相关性：A·直接相关（score=5）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：Microarchitectural Security Testing
- 纳入依据：hardware/processor object: processor, microarchitecture, microarchitectural；verification/fuzzing method: fuzz；security relevance: security, transient execution, leakage
- 论文页面：[http://arxiv.org/abs/2502.14307v1](http://arxiv.org/abs/2502.14307v1)
- PDF：[https://arxiv.org/pdf/2502.14307v1](https://arxiv.org/pdf/2502.14307v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 19 页，提取 79198 字符

## 摘要

We propose using reinforcement learning to address the challenges of discovering microarchitectural vulnerabilities, such as Spectre and Meltdown, which exploit subtle interactions in modern processors. Traditional methods like random fuzzing fail to efficiently explore the vast instruction space and often miss vulnerabilities that manifest under specific conditions. To overcome this, we introduce an intelligent, feedback-driven approach using RL. Our RL agents interact with the processor, learning from real-time feedback to prioritize instruction sequences more likely to reveal vulnerabilities, significantly improving the efficiency of the discovery process. We also demonstrate that RL systems adapt effectively to various microarchitectures, providing a scalable solution across processor generations. By automating the exploration process, we reduce the need for human intervention, enabling continuous learning that uncovers hidden vulnerabilities. Additionally, our approach detects subtle signals, such as timing anomalies or unusual cache behavior, that may indicate microarchitectural weaknesses. This proposal advances hardware security testing by introducing a more efficient, adaptive, and systematic framework for protecting modern processors. When unleashed on Intel Skylake-X and Raptor Lake microarchitectures, our RL agent was indeed able to generate instruction sequences that cause significant observable byte leakages through transient execution without generating any $μ$code assists, faults or interrupts. The newly identified leaky sequences stem from a variety of Intel instructions, e.g. including SERIALIZE, VERR/VERW, CLMUL, MMX-x87 transitions, LSL+RDSCP and LAR. These initial results give credence to the proposed approach.

## 研究问题

如何自动化发现现代处理器中由瞬态执行引起的微架构漏洞,克服传统随机模糊测试在巨大指令空间中低效的问题。

## Introduction 梳理

现有方法如随机模糊测试难以高效探索复杂指令空间,难以发现特定条件下触发的漏洞。作者提出基于强化学习(RL)的智能反馈驱动方法,通过RL agent与处理器交互,实时学习优先选择可能揭示漏洞的指令序列,提高发现效率。贡献包括:提出RL框架、构建自定义环境、在Intel Skylake-X和Raptor Lake上发现新的瞬态执行泄漏机制。

## 方法

输入生成:RL agent从x86指令集分层选择指令(先选指令集,再选指令,最后选操作数),构建指令序列。反馈/coverage:使用硬件性能计数器(12种)和Flush+Reload检测字节泄漏;奖励函数结合坏推测测量(公式2)和可观察字节泄漏。Oracle:通过不同分支条件(JE/JNE)和插入lfence确认瞬态执行导致的泄漏。DUT/平台:Intel Skylake-X (i9-7900X)和Raptor Lake (i9-14900K)黑盒测试。无需golden model。

## 实验与评估

baseline:未明确与其他工具对比。实验预算:Skylake-X训练4.5天,Raptor Lake 10.5天,收集27天和20天数据,API费用2.46美元。统计:平均奖励和序列长度随时间增加(图4、5),高奖励序列在可视化中突出(图6)。bug/CVE:发现8类新瞬态执行机制(如Masked FP Exception、MMX-x87、SERIALIZE、VERW/VERR、CLMUL、LSL+RDSCP、LAR等),未提及CVE编号。开销:训练时间长但API成本低。Artifact:代码和框架在论文中描述但未明确提供开源仓库。

## 核心贡献

提出使用强化学习自动发现微架构漏洞的方法;构建了自定义RL环境;在Intel处理器上发现了新的瞬态执行泄漏机制。

## 与本仓库研究主线的关系

论文直接关联微架构安全自动测试领域(方法借鉴),但目标为x86而非RISC-V。RL+性能计数器+泄漏检测的思路可迁移至RISC-V处理器模糊测试;与多hart/内存一致性验证不直接相关。

## 结论

RL框架能高效探索指令空间,发现新漏洞,并适应不同微架构。未来可扩展至GPU等异构硬件。

## 局限性

探索焦点限于指令序列,未考虑系统级交互(如OS、Hyperthreading等);奖励稀疏且延迟;CPU状态仅通过性能计数器部分可观察。

## 详细阅读分析

建议重点阅读第5节(RL框架细节,尤其是奖励函数、性能计数器列表)、第7节(发现的新漏洞机制及泄漏率分析)、图1和2(系统架构和测试流程)。

## 后续核验问题

- 1. RL方法如何迁移到RISC-V处理器?2. 奖励函数能否泛化到其他微架构?3. 如何检测跨hart或内存一致性相关的漏洞?4. 为何MMX-x87泄漏在特定迭代次数下才显著?5. 是否可与其他模糊测试工具(如Osiris)进行定量对比?
