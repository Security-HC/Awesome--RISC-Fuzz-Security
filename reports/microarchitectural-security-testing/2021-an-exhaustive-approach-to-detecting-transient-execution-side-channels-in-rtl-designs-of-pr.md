# An Exhaustive Approach to Detecting Transient Execution Side Channels in RTL Designs of Processors

## 基本信息

- 作者：M. R. Fadiheh、A. Wezel、Johannes Mueller、J. Bormann、Sayak Ray、Jason M. Fung、S. Mitra、D. Stoffel、W. Kunz
- 发表日期：2021-08-04
- 会议/期刊：IEEE transactions on computers
- 主分类：微架构安全自动测试
- 相关性：A·直接相关（score=5）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：Microarchitectural Security Testing
- 纳入依据：hardware/processor object: processor, microarchitectural, rtl；verification/fuzzing method: verification；security relevance: security, side channel, transient execution
- 论文页面：[https://doi.org/10.1109/TC.2022.3152666](https://doi.org/10.1109/TC.2022.3152666)
- PDF：[https://arxiv.org/pdf/2108.01979](https://arxiv.org/pdf/2108.01979)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 14 页，提取 85578 字符

## 摘要

Hardware (HW) security issues have been emerging at an alarming rate in recent years. Transient execution attacks, such as Spectre and Meltdown, in particular, pose a genuine threat to the security of modern computing systems. Despite recent advances, understanding the intricate implications of microarchitectural design decisions on processor security remains a great challenge and has caused a number of update cycles in the past. This papers addresses the need for a new approach to HW sign-off verification which guarantees the security of processors at the Register Transfer Level (RTL). To this end, we introduce a formal definition of security with respect to transient execution attacks, formulated as a HW property. We present a formal proof methodology based on Unique Program Execution Checking (UPEC) which can be used to systematically detect all vulnerabilities to transient execution attacks in RTL designs. UPEC does not exploit any a priori knowledge on known attacks and can therefore detect also vulnerabilities based on new, so far unknown, types of channels. This is demonstrated by two new attack scenarios discovered in our experiments with UPEC. UPEC scales to a wide range of HW designs, including in-order processors (RocketChip), pipelines with out-of-order writeback (Ariane), and processors with deep out-of-order speculative execution (BOOM). To the best of our knowledge, UPEC is the first RTL verification technique that exhaustively covers transient execution side channels in processors of realistic complexity.

## 研究问题

针对瞬态执行攻击（如Spectre和Meltdown）带来的处理器硬件安全威胁，需要在寄存器传输级（RTL）对处理器进行安全签核验证，但现有方法缺乏对瞬态执行侧信道的穷尽覆盖，且难以扩展到具有实际复杂度的处理器。

## Introduction 梳理

现有安全验证方法多基于抽象模型（如gem5、InSpectre、CheckMate）或软件层语义扩展，无法捕捉RTL细节引入的漏洞；taint分析需要预先知道攻击路径，对未知变体能力有限；硬件fuzzing（如IntroSpectre、HyperFuzzing）非穷尽，无法提供形式化保证。该论文提出UPEC方法，通过形式化定义安全属性并基于唯一程序执行检查（UPEC）在RTL层面系统性地检测全部瞬态执行漏洞，无需已知攻击先验知识。贡献包括：揭示简单处理器也可能产生TES；提出微架构级漏洞形式化定义；提出可扩展的UPEC形式化验证流程；在RocketChip、Ariane和BOOM中发现新漏洞并验证安全性。

## 方法

输入生成：形式化方法，输入为任意程序P、公开信息Xp、秘密信息Xc以及初始微架构状态S0，通过约束宏（如secret data protected、secret load speculative）限定瞬态访问场景。反馈/覆盖：基于SAT的区间属性检查（IPC），迭代枚举P-location（秘密传播到的微架构状态变量），使用阻塞子句避免重复，并利用锥形影响缩减优化。Oracle：无需golden model，而是构建两个SoC实例的miter模型，比较微架构执行轨迹；安全属性要求当架构观察一致时，微架构执行也必须一致。DUT/平台：RTL设计包括RocketChip（v1.2.0）、Ariane（v4.1.2）和BOOM（v2.0.1），使用商业工具OneSpin 360 DV在Intel Core i7上验证。

## 实验与评估

Baseline：论文未提供与传统fuzzing或模型检查的定量比较，但通过对比其他方法（如taint分析、抽象模型验证）说明全exhaustive优势，或提及无其他方法能完成相同任务。实验预算：报告了每个设计验证的CPU时间（分钟级到小时级）和内存（2.7GB至8.8GB）。Bug/CVE：发现RocketChip对Orc攻击的两种变体（通过修改设计注入）、原始RocketChip的PMP锁定机制ISA违规、Ariane的指令缓存信息泄露，以及BOOM的Spectre-STC两种版本和原始Spectre（缓存侧信道）漏洞，并设计补丁验证修复。Artifact：提供了BOOM的UPEC验证套件（GitHub链接），并发布了一个经过形式化验证的安全BOOM变体。开销：手动工作量约每人天10天（RocketChip/Ariane）和数人周（BOOM微等价性）。结论：UPEC成功验证了多个设计，并能发现未知新攻击。

## 核心贡献

1) 提出形式化的瞬态执行安全定义，以硬件属性形式表达，并区分功能泄漏与TES；2) 提出UPEC方法，通过自组合miter和迭代证明实现穷尽检测，无需预知攻击类型；3) 首次发现Orc攻击和Spectre-STC等新变体，并证明简单顺序处理器也可能存在TES；4) 形式的验证覆盖RocketChip、Ariane、BOOM等真实复杂度处理器，并发布首个带形式化安全保证的BOOM开源变体。

## 与本仓库研究主线的关系

直接相关。论文针对RISC-V处理器（RocketChip、Ariane、BOOM）的RTL设计进行形式化安全验证，与处理器fuzzing和微架构安全自动测试的目标一致，但方法论上是形式化验证而非动态fuzzing，可视为强邻近技术。对于多hart与内存一致性验证：论文主要关注单线程单核处理器的瞬态执行侧信道，未涉及多hart并发或缓存一致性协议，但提出的安全属性和miter结构可扩展到对称多核场景（需增加一致性验证维度）。可作为硬件安全验证的基线参考，用于比较fuzzing方法是否遗漏已知漏洞。

## 结论

论文证明瞬态执行侧信道不仅存在于高级特性处理器，也可能由低层RTL设计决策引入，甚至可能被恶意植入难以察觉的后门。UPEC方法能在RTL级别穷尽、可扩展且高自动地检测TES，显著优于现有技术，能发现未知信道。通过实验在RocketChip、Ariane和BOOM中验证了有效性，并首次给出了具有明确安全保证的深度乱序处理器RTL模型。手动工作量相对较小，且方法有潜力用于存量硬件安全分析。未来工作将探索与HW/SW契约的组合验证。

## 局限性

实验聚焦于单核处理器，未涉及多核或多hart一致性场景；微等价性约束需要针对不同乱序处理器人工开发（约4人周工作量），且BOOM的修复策略保守，性能不佳；对于某些设计（如RocketChip）需要手动添加不变量来消除不可达状态；方法基于形式化验证，受限于SAT求解能力，对于更大规模SoC可能仍面临可扩展性挑战；论文中对于原始RocketChip和Ariane的验证结果基于特定配置（如PMP、页表假设），泛化性需进一步确认。

## 详细阅读分析

论文详细阐述了UPEC的形式化框架：通过构建两个初始仅秘密不同的SoC实例，要求当架构观察一致时微架构执行完全一致，从而排除秘密的影响。方法基于归纳，基步枚举所有P-alert（秘密传播到非架构状态），步进证明P-alert不会扩展到L-alert（泄漏到架构状态）。关键技术包括：使用任何状态证明（any-state proof）处理任意初始状态，通过P-location枚举分解证明，利用锥形影响缩减减小复杂度，以及针对乱序处理器的微等价性约束（如基于ROB槽位划分主序列和瞬态序列）。实验部分特别展示了Spectre-STC如何发现未知信道：功能部件（ALU、乘法器、除法器）共享写端口且优先级固定，导致除法被年轻指令延迟，从而产生秒表型信道。

## 后续核验问题

- 1. UPEC如何扩展到多核或同时多线程（SMT）处理器，以检测跨hart的微架构侧信道？2. 微等价性约束能否自动生成，减少人工工作？3. UPEC与基于覆盖的硬件fuzzing（如HyperFuzzing）在发现漏洞的完备性和效率上有何定量差异？4. 论文发现的Orc攻击在真实SoC中是否已出现类似设计优化？5. 如何将UPEC与软件层安全契约（如硬件-软件合约）结合，实现跨层安全验证？
