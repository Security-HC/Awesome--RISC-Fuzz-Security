# Shesha: Multi-head Microarchitectural Leakage Discovery in new-generation Intel Processors

## 基本信息

- 作者：Anirban Chakraborty、Nimish Mishra、Debdeep Mukhopadhyay
- 发表日期：2024-06-10
- 会议/期刊：arXiv
- 主分类：微架构安全自动测试
- 相关性：A·直接相关（score=5）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：Microarchitectural Security Testing
- 纳入依据：hardware/processor object: processor, microarchitectural；verification/fuzzing method: fuzz；security relevance: side channel, transient execution, leakage
- 论文页面：[http://arxiv.org/abs/2406.06034v2](http://arxiv.org/abs/2406.06034v2)
- PDF：[https://arxiv.org/pdf/2406.06034v2](https://arxiv.org/pdf/2406.06034v2)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 22 页，提取 100000 字符

## 摘要

Transient execution attacks have been one of the widely explored microarchitectural side channels since the discovery of Spectre and Meltdown. However, much of the research has been driven by manual discovery of new transient paths through well-known speculative events. Although a few attempts exist in literature on automating transient leakage discovery, such tools focus on finding variants of known transient attacks and explore a small subset of instruction set. Further, they take a random fuzzing approach that does not scale as the complexity of search space increases. In this work, we identify that the search space of bad speculation is disjointedly fragmented into equivalence classes, and then use this observation to develop a framework named Shesha, inspired by Particle Swarm Optimization, which exhibits faster convergence rates than state-of-the-art fuzzing techniques for automatic discovery of transient execution attacks. We then use Shesha to explore the vast search space of extensions to the x86 Instruction Set Architecture (ISAs), thereby focusing on previously unexplored avenues of bad speculation. As such, we report five previously unreported transient execution paths in Instruction Set Extensions (ISEs) on new generation of Intel processors. We then perform extensive reverse engineering of each of the transient execution paths and provide root-cause analysis. Using the discovered transient execution paths, we develop attack building blocks to exhibit exploitable transient windows. Finally, we demonstrate data leakage from Fused Multiply-Add instructions through SIMD buffer and extract victim data from various cryptographic implementations.

## 研究问题

自动发现新一代Intel处理器指令集扩展（ISE）中的瞬态执行泄漏路径，现有方法局限于已知攻击变体且搜索空间受限。

## Introduction 梳理

瞬态执行攻击（如Spectre、Meltdown）被广泛研究，但多数依赖手动发现。现有自动化工具（如Transynther、Speechminer）仅针对特定猜测类别，使用随机fuzzing，无法扩展到ISE的庞大搜索空间。本文提出Shesha，利用粒子群优化（PSO）和坏猜测的等价类分解，实现对ISE中未探索的坏猜测路径的快速收敛发现。贡献包括：1）提出新框架；2）发现5个新瞬态执行路径；3）提供根因分析；4）展示FMA指令泄漏的实际攻击。

## 方法

Shesha基于PSO，将指令序列映射为粒子位置，使用性能计数器（PMU）监测坏猜测发生作为适应度函数。将搜索空间分解为不相交的等价类（分支误预测、微码辅助、机器清除），分两阶段优化：认知阶段（仅粒子行为，β=0.4,γ=0）让粒子收敛到子群；混合阶段（粒子+群行为，β=0.1,γ=0.4）利用子群内全局最佳加速收敛。输入生成：从uops.info构建ISE指令池，随机采样10条指令+操作数作为粒子。反馈：PMU事件（表1）提供二进制适应度（是否发生坏猜测）。Oracle：无需golden model，直接测量PMU事件。DUT：Intel Alder Lake, Comet Lake, Sapphire Rapids, Ice Lake处理器。

## 实验与评估

{'artifact': '工具和PoC代码在https://github.com/SEAL-IIT-KGP/shesha。', 'baseline': '与Shesha自身6种变体对比（表3），定性比较Transynther、Speechminer等工具（未提供定量时间）。', 'bug_or_CVE': '发现5个新瞬态执行路径（SIMD-Vector转换、单双精度混合、FMA、AES-SSE非规格化数）。', 'experiment_budget': '24小时测试，大部分结果在8小时内获得。N=50，n=10，每个变体重复运行。', 'overhead': '未报告Shesha本身的运行开销。', 'statistics': '声称零假阳性（PMU可靠），但未提供统计显著性测试。'}

## 核心贡献

1) 提出基于PSO和等价类分解的自动化瞬态泄漏发现框架；2) 发现5个新的瞬态执行路径；3) 对FMA指令泄漏进行深入分析和利用；4) 提供根因分析和攻击构建块。

## 与本仓库研究主线的关系

方法借鉴：PSO和基于等价类的fuzzing策略可推广到RISC-V处理器验证，但论文聚焦x86 Intel，与多hart/内存一致性验证无直接关系。

## 结论

Shesha基于PSO和等价类分解，能高效发现ISE中的瞬态执行路径，揭示Intel新处理器中5个新路径。FMA泄漏被证明可攻击多种密码实现。瞬态执行难以缓解，建议软件措施如lfence和vzeroupper。

## 局限性

1) 仅测试Intel CPU，未验证其他架构；2) FMA intra-engine泄漏未观察到；3) 部分根因分析基于推测；4) 未与其他工具做严格定量对比；5) 未讨论可扩展性到其他ISA。

## 详细阅读分析

阅读Section 3（Shesha框架）、Section 4（新路径）、Section 6（根因分析）、Section 8（FMA泄漏及其利用）。

## 后续核验问题

- Shesha的等价类分解方法能否直接迁移到RISC-V设计空间探索？需如何调整适应度函数？
- FMA泄漏是否也在AMD或ARM处理器中存在？
- Shesha的收敛速度是否对初始粒子数N和维度n敏感？是否提供敏感性分析？
