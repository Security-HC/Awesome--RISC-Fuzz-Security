# Enter, Exit, Page Fault, Leak ${ }^{\ddagger}$: Testing Isolation Boundaries for Microarchitectural Leaks

## 基本信息

- 作者：Oleksii Oleksenko、Flavien Solt、Cédric Fournet、Jana Hofmann、Boris Köpf、Stavros Volos
- 发表日期：2026-05-01
- 会议/期刊：IEEE Symposium on Security and Privacy (S&P)
- 主分类：形式化与定向处理器验证
- 相关性：A·直接相关（score=5）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：Formal & Directed Processor Verification
- 纳入依据：hardware/processor object: processor, cpu, microarchitectural；verification/fuzzing method: validation；security relevance: security, side channel, leakage
- 论文页面：[https://doi.org/10.1109/sp63933.2026.00007](https://doi.org/10.1109/sp63933.2026.00007)
- PDF：[https://arxiv.org/pdf/2507.06039](https://arxiv.org/pdf/2507.06039)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 17 页，提取 88320 字符

## 摘要

CPUs provide isolation mechanisms like virtualization and privilege levels to protect software. Yet these focus on architectural isolation while typically overlooking microarchitectural side channels, exemplified by Meltdown and Foreshadow. Software must therefore supplement architectural defenses with ad-hoc microarchitectural patches, which are constantly evolving as new attacks emerge and defenses are proposed. Such reactive approach makes ensuring complete isolation a daunting task, and leaves room for errors and oversights. We address this problem by developing a tool that stress tests microarchitectural isolation between security domains such as virtual machines, kernel, and processes, with the goal of detecting flaws in the isolation boundaries. The tool extends model-based relational testing (MRT) methodology to enable detection of cross-domain information leakage. We design a new test case generator and execution sandbox to handle multidomain execution, new leakage models to encode expected leaks, and new analysis techniques to manage nondeterminism. We use this tool to perform an in-depth testing campaign on six x86-64 CPUs for leakage across different isolation boundaries. The testing campaign exposed four new leaks and corroborated numerous known ones, with only two false positives throughout the entire campaign. These results show critical gaps in current isolation mechanisms as well as validate a robust methodology for detecting microarchitectural flaws. As such, this approach enables a shift from reactive patching to proactive security validation in processor design.

## 研究问题

如何系统、自动地检测安全域之间的微架构隔离缺陷，而不仅限于单一域、单一泄漏类型或单一缓解措施。论文关注VM、内核、用户进程等隔离边界上的跨域信息泄漏。

## Introduction 梳理

研究缺口是：架构隔离机制（页表、虚拟化、特权级）不覆盖共享微架构状态导致的侧信道；软件补丁碎片化且常被后续攻击推翻，厂商关于微架构安全的声明也常被证伪。既有自动测试多为点解决方案：Revizor等MRT工具主要在单域（内核）运行，Scam-V也限于单信任域，Transynther/RegCheck针对已知Meltdown/MDS或Meltdown-3a变体，SpeechMiner等不显式测试域转换。作者贡献是：提出actor抽象与模板/宏测试用例生成、支持多域执行的沙箱、面向actor的非干扰泄漏模型、用统计方法处理域转换非确定性，并在六款x86-64 CPU上开展跨H2V、V2V、K2U、U2U的测试活动。

## 方法

{'DUT/平台': '六款x86-64商用CPU：Intel KabyLake R、Coffee Lake、RaptorCove；AMD Zen1、Zen2、Zen4。执行环境为自定义Linux内核模块执行器，正文称超过3500行代码，支持host-kernel、host-user、guest-kernel，配置VMCS/VMCB、E/NPT、页表、MSR、Prime+Probe或Flush+Reload测量等。', 'Oracle': '基于contract的多actor非干扰。定义要求：若攻击者数据相同且受害者contract trace相同，则硬件测量trace应相同；contract模型允许受害者load/store地址和PC/控制流变化泄漏。实现上模型基于Unicorn扩展，只收集受害者actor的contract trace；比较的是暴露信息而非原始硬件trace，并用统计分布相等替代单条trace相等。', '反馈/coverage': 'MRT随机测试，未确认覆盖率反馈或覆盖引导；测试按轮生成程序与输入，发现模型违反后保存细节并终止该campaign；正文未提供覆盖率指标。', '总体方法': '扩展模型基关系测试MRT与Revizor：执行随机程序，收集硬件trace，与抽象模型预测的期望泄漏比较；若实际暴露的信息超出模型允许范围，则报告潜在泄漏。', '是否需要golden model': '需要抽象模型/契约模型作为期望泄漏的golden reference，但不是逐周期RTL golden model；模型允许与真实CPU行为偏离，只要覆盖预期会泄漏的信息。', '泄漏模型与统计': '支持强弱不同的隔离模型：基线要求不泄漏受害者状态，也支持允许内存访问模式泄漏的contract。对域转换微码导致的非确定性，把trace相等检验提升为分布相等检验，使用Pearson χ2检验；样本量自适应从N=15开始，若发现违反再增至40、160、320，只有最大样本仍违反才报告。', '输入生成': '用户提供actor模板和配置文件；模板用汇编段与宏定义actor边界、域转换和测量点；生成器用random_instructions宏在随机上下文插入随机指令序列，指令池由配置的allowlist指定；每个actor生成三页随机数据初始化内存和寄存器；另有插桩pass随机把某次内存访问改为指向其他actor内存，当前实现主要针对Meltdown类用户到内核访问。'}

## 实验与评估

{'Artifact': '工具作为Revizor v1.3+的一部分开源在GitHub microsoft/sca-fuzzer；正文提供可用性链接。未确认有独立第三方复现或完整实验artifact评估。', 'baseline': '正文以已知泄漏（MDS及其变体、Foreshadow、Meltdown、DSS、Meltdown 3a/RSRR变体）和已知补丁效果作为正/负对照；Related Work对Revizor、Scam-V、Transynther、SpeechMiner、RegCheck等做定性比较。未确认存在与其他工具的同台性能或检测率baseline。', 'bug/CVE': '作者报告4个新跨域泄漏并获CVE：CVE-2024-36357为AMD3上跨VM泄漏，可逐位推断另一VM已缓存内存；CVE-2024-36350为AMD3上内核到用户泄漏最近约32次store；CVE-2024-36349为用户态投机读RDTSCP AUX，影响Int1/Int2/Int3/AMD1；CVE-2024-36348为用户态投机执行SMSW，影响AMD2/AMD3。还复现MDS、Foreshadow、Meltdown、DSS、Meltdown 3a/RSRR等已知泄漏，并测试补丁：VERW与L1D_FLUSH_CMD对MDS有效，WBINVD无效；DSS新补丁有效而旧异常处理补丁无效；KPTI三种变体效果不同。AMD1的R/W-bit违例厂商未能复现。', '实验实际证明': '在作者配置与六款x86 CPU上，工具能发现4个新CVE泄漏、复现配置内可出现的已知泄漏、识别部分补丁有效/无效，并将误报控制在2个。未证明对所有微架构泄漏完备，也未证明对其他架构或多hart一致性场景有效。', '实验预算': '304个测试campaign，合计88 machine-days；测试近3000万个程序，超过200亿次硬件测量。每个campaign测试100K个随机程序，每个程序50个随机输入；组合模板与配置在六款CPU上用相同种子。样本量自适应为15/40/160/320。', '开销': '硬件测量速率800–4500 measurements/s；摘要称60–700 test case executions/s。完成100K测试用例×50输入的时间：MEM配置2–24小时，COMP配置3–8小时，REG配置1.5–11小时；多数违例4小时内发现，所有测试24小时内完成。', '统计': '使用Pearson χ2对trace样本分布做相等检验；整个campaign仅2个误报，经人工检查丢弃。检测时间：85%的违例在1小时内、98%在4小时内；按轮数85%在20K轮内、93%在40K轮内；4%的测试未检出违例。χ2阈值、置信区间和统计功效细节未在正文给出，未确认。'}

## 核心贡献

作者声称提出首个系统测试多安全域间微架构隔离的工具；核心贡献是actor抽象、模板与宏的多域测试生成、低开销可配置执行沙箱、面向actor的contract非干扰模型、用χ2和自适应样本处理域转换非确定性，以及六款x86 CPU上的大规模campaign和4个新CVE。实验实际展示的是在这些配置和平台上发现/复现泄漏及验证补丁，而非完备性证明。

## 与本仓库研究主线的关系

{'与多hart/一致性路径研究的关系': '其actor抽象可类比hart、VM、内核/用户等隔离域，contract非干扰Oracle和统计trace比较可迁移到跨hart微架构泄漏测试；但它不提供hart间内存一致性Oracle、不建模共享内存通信、不覆盖多hart一致性路径。若repo聚焦多hart/一致性，本文主要提供测试生成、执行沙箱、Oracle与抗非确定性方法借鉴，需另行实现RISC-V执行环境和一致性/共享内存语义。', '定位': '对“微架构安全自动测试”是直接相关；对RISC-V/多hart/内存一致性验证不是直接相关，属于强邻近/方法借鉴。论文不涉及RISC-V、多hart、内存一致性模型、RTL/SoC Fuzzing或一致性litmus测试。'}

## 结论

作者结论：通过actor抽象、模板化多域测试生成、专用执行环境、多actor非干扰contract和统计非确定性处理，MRT可系统测试安全域间微架构隔离；在商用x86 CPU上的campaign发现新泄漏并验证补丁，说明可从反应式打补丁转向处理器设计中的主动安全验证。

## 局限性

作者明确限制：不支持actor间架构信息流如共享内存；不支持自修改代码；控制结构（IDT/GDT）位置固定，若CPU预测其位置则可能漏检；测量框架插入的代码会影响微架构状态，最坏可能阻止泄漏检测；评估只覆盖部分泄漏类型，未覆盖跨域分支训练等控制流攻击；部分泄漏需要大量测量，实验时长可能不足以发现所有泄漏；当前仅支持host-kernel、host-user、guest-kernel和x86。审稿推断：无覆盖引导、无同台工具基线、统计阈值与功效未详述，可能影响泛化与可复现性判断。

## 详细阅读分析

['§2.3：MRT与Revizor的五步循环，理解程序生成、输入生成、硬件执行、模型执行、泄漏比较。', '§4：模板、宏、random_instructions、actor内存访问插桩和自定义二进制包，理解多域测试如何结构化。', '§5：内核模块执行器、状态保存/恢复、VM与用户actor配置、内存别名化，理解低开销多域执行的关键工程。', '§6：多actor非干扰定义、contract trace和模型实现，重点看允许受害者load/store地址与控制流泄漏的Oracle。', '§7：Pearson χ2、trace分布相等和自适应样本量，理解误报控制与吞吐折中。', '§8.2：四个新CVE的触发gadget、已知泄漏复现和补丁有效性测试，区分实验证明与作者解释。', '§9：限制与未来工作，特别是共享内存、自修改代码、控制结构位置和测量干扰。']

## 后续核验问题

- 如何把actor抽象映射到RISC-V多hart场景：hart、特权级、VM、用户进程之间的转换和共享状态如何建模？
- 多hart内存一致性与跨hart微架构泄漏的Oracle应如何结合：contract非干扰是否可与内存模型litmus测试或CheckMate类方法组合？
- 在RTL/SoC仿真中，Pearson χ2和自适应样本是否仍必要，还是确定性仿真可用更直接trace比较？
- 缺少覆盖引导是否会导致域转换、微码路径和缓解措施组合上的盲区；能否引入覆盖反馈而不破坏MRT的Oracle？
- 如何扩展共享内存支持，使V2V/K2U/U2U测试覆盖合法通信与非法泄漏的边界？
- 四个新CVE的根因和最小gadget是否已被厂商公告或后续工作独立确认；Zen1 R/W违例为何无法复现？
- 若移植到RISC-V，需要哪些执行环境能力：创建VM/用户进程、配置页表与PMP、触发异常、收集cache trace？
- 本文方法能否检测注入型泄漏（LVI/Spectre V2类）以及多hart下的分支预测器跨域训练？
