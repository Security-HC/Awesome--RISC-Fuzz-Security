# Osiris: Automated Discovery of Microarchitectural Side Channels

## 基本信息

- 作者：Daniel Weber、Ahmad Ibrahim、Hamed Nemati、Michael Schwarz、Christian Rossow
- 发表日期：2021-06-07
- 会议/期刊：arXiv
- 主分类：微架构安全自动测试
- 相关性：A·直接相关（score=100）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：Microarchitectural Security Testing
- 纳入依据：manual direct seed title
- 论文页面：[http://arxiv.org/abs/2106.03470v1](http://arxiv.org/abs/2106.03470v1)
- PDF：[https://arxiv.org/pdf/2106.03470v1](https://arxiv.org/pdf/2106.03470v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 18 页，提取 93096 字符

## 摘要

In the last years, a series of side channels have been discovered on CPUs. These side channels have been used in powerful attacks, e.g., on cryptographic implementations, or as building blocks in transient-execution attacks such as Spectre or Meltdown. However, in many cases, discovering side channels is still a tedious manual process. In this paper, we present Osiris, a fuzzing-based framework to automatically discover microarchitectural side channels. Based on a machine-readable specification of a CPU's ISA, Osiris generates instruction-sequence triples and automatically tests whether they form a timing-based side channel. Furthermore, Osiris evaluates their usability as a side channel in transient-execution attacks, i.e., as the microarchitectural encoding for attacks like Spectre. In total, we discover four novel timing-based side channels on Intel and AMD CPUs. Based on these side channels, we demonstrate exploitation in three case studies. We show that our microarchitectural KASLR break using non-temporal loads, FlushConflict, even works on the new Intel Ice Lake and Comet Lake microarchitectures. We present a cross-core cross-VM covert channel that is not relying on the memory subsystem and transmits up to 1 kbit/s. We demonstrate this channel on the AWS cloud, showing that it is stealthy and noise resistant. Finally, we demonstrate Stream+Reload, a covert channel for transient-execution attacks that, on average, allows leaking 7.83 bytes within a transient window, improving state-of-the-art attacks that only leak up to 3 bytes.

## 研究问题

微架构时序侧信道的自动发现

## Introduction 梳理

现有侧信道发现依赖人工，缺乏自动化方法。既有自动化工具如Covert Shotgun和ABSynthe局限于竞争型侧信道，Transynther仅关注MDS攻击变体。Osiris提出通用方法自动发现不依赖竞争的时序侧信道，基于指令序列三元组（reset, trigger, measure）表示侧信道，并实现fuzzing框架进行检测。

## 方法

输入生成：基于x86 ISA机器可读规范（uops.info）离线生成所有指令变体，在线阶段清理非法指令，随机组合单指令三元组（reset仅用sleep伪指令触发）。反馈/coverage：无引导，基于随机生成和时序测量。Oracle：比较带trigger（hot path）和不带trigger（cold path）下measure序列的执行时间，若中位数差大于阈值则视为候选。DUT/平台：Intel Core i7-9750H等5种CPU，Ubuntu/Arch Linux。无需golden model。

## 实验与评估

Baseline：未提及其他方法作为基线。实验预算：21天fuzzing，每次完整运行约41秒（单循环）到近5天（所有三元组）。统计：在i7-9750H上发现68,597个侧信道候选，聚类后16-26个簇。bug/CVE：发现4种新侧信道（RDRAND、XSAVE、MMX-x87-FPU、AVX2-x87-FPU），并构造FlushConflict KASLR break、跨核/VM隐蔽信道（95.2 bit/s AWS）、Spectre/Meltdown改进。开销：未提供详细性能开销分析。Artifact：开源代码https://github.com/cispa/osiris。

## 核心贡献

1. 提出通用指令序列三元组表示法并实现fuzzing框架Osiris。2. 发现4种新时序侧信道。3. 构造FlushConflict KASLR break（可在Ice Lake/Comet Lake上工作）和跨核/VM RDRAND隐蔽信道。4. 分析现有检测/防御方法在新侧信道下的不足。

## 与本仓库研究主线的关系

强邻近。方法属于硬件fuzzing（RTL/SoC级别），直接聚焦微架构安全自动测试。虽针对x86且未涉及多hart一致性验证，但FlushConflict涉及缓存一致性，与内存一致性路径有间接关联。方法可迁移至RISC-V等ISA。

## 结论

Osiris能自动发现时序侧信道，已发现新侧信道并展示实际攻击，强调自动化工具的重要性。

## 局限性

仅支持单指令序列，无法检测eviction-based侧信道（如Evict+Reload）；时序差异需约100cycle以上，无法检测较小差异；运行于Linux导致噪声干扰；未考虑多hart场景。

## 详细阅读分析

True

## 后续核验问题

- 如何扩展Osiris支持多指令序列？
- 如何将Osiris迁移至RISC-V架构？
- Osiris能否用于自动化检测缓存一致性协议侧信道？
- 如何结合性能计数器引导fuzzing过程？
