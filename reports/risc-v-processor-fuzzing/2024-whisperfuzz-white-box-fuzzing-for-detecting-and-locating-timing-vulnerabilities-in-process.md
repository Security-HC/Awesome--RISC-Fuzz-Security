# WhisperFuzz: White-Box Fuzzing for Detecting and Locating Timing Vulnerabilities in Processors

## 基本信息

- 作者：Pallavi Borkar、Chen Chen、Mohamadreza Rostami、Nikhilesh Singh、Rahul Kande、Ahmad-Reza Sadeghi、Chester Rebeiro、Jeyavijayan Rajendran
- 发表日期：2024-02-06
- 会议/期刊：arXiv
- 主分类：RISC-V 处理器 Fuzzing
- 相关性：A·直接相关（score=100）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：RISC-V Processor Fuzzing、Microarchitectural Security Testing、RTL & SoC Hardware Fuzzing、Coverage, Oracles & Fuzzing Methodology
- 纳入依据：manual direct seed title
- 论文页面：[http://arxiv.org/abs/2402.03704v2](http://arxiv.org/abs/2402.03704v2)
- PDF：[https://arxiv.org/pdf/2402.03704v2](https://arxiv.org/pdf/2402.03704v2)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 19 页，提取 88230 字符

## 摘要

Timing vulnerabilities in processors have emerged as a potent threat. As processors are the foundation of any computing system, identifying these flaws is imperative. Recently fuzzing techniques, traditionally used for detecting software vulnerabilities, have shown promising results for uncovering vulnerabilities in large-scale hardware designs, such as processors. Researchers have adapted black-box or grey-box fuzzing to detect timing vulnerabilities in processors. However, they cannot identify the locations or root causes of these timing vulnerabilities, nor do they provide coverage feedback to enable the designer's confidence in the processor's security. To address the deficiencies of the existing fuzzers, we present WhisperFuzz--the first white-box fuzzer with static analysis--aiming to detect and locate timing vulnerabilities in processors and evaluate the coverage of microarchitectural timing behaviors. WhisperFuzz uses the fundamental nature of processors' timing behaviors, microarchitectural state transitions, to localize timing vulnerabilities. WhisperFuzz automatically extracts microarchitectural state transitions from a processor design at the register-transfer level (RTL) and instruments the design to monitor the state transitions as coverage. Moreover, WhisperFuzz measures the time a design-under-test (DUT) takes to process tests, identifying any minor, abnormal variations that may hint at a timing vulnerability. WhisperFuzz detects 12 new timing vulnerabilities across advanced open-sourced RISC-V processors: BOOM, Rocket Core, and CVA6. Eight of these violate the zero latency requirements of the Zkt extension and are considered serious security vulnerabilities. Moreover, WhisperFuzz also pinpoints the locations of the new and the existing vulnerabilities.

## 研究问题

现有黑盒/灰盒处理器时序fuzzer无法定位时序漏洞的根因，也不提供时序行为覆盖度量，导致设计师对安全信心不足且缓解延迟。

## Introduction 梳理

时序漏洞是处理器安全的重要威胁，现有检测方法有形式化方法（可扩展性差，因状态爆炸）和fuzzing（如黑盒Osiris、灰盒SIGFuzz等）。但这些fuzzer仅能检测存在性，不能自动定位根因，且缺乏覆盖反馈。本文提出WhisperFuzz，首个结合静态分析的白盒fuzzer，通过提取微体系结构状态转移（Micro-Event Graph, MEG）实现定位和覆盖度量。

## 方法

输入生成：先通过覆盖反馈fuzzer（HyPFuzz）生成种子（指令序列），再通过Operand mutator变异操作数（立即数/内存地址）生成200个数据相关输入。反馈/覆盖：种子生成阶段使用代码覆盖（分支、条件、FSM）；时序覆盖通过将MEG路径转化为SystemVerilog Assertion cover property并仿真收集。Oracle：针对同一指令序列不同数据输入，通过Leakage Analyzer比较各模块实例的执行时间差，若存在显著差异且非功能异常则判为时序漏洞。DUT/平台：Synopsys VCS仿真，Chipyard环境，处理器为BOOM、Rocket Core和CVA6。不需要golden model，采用差分时序比较。

## 实验与评估

baseline：与UPEC、Checkmate、Osiris、ABSynthe、PLUMBER、SIGFuzz对比（表1）。实验预算：72小时fuzzing，重复3次，每个种子生成200个数据相关输入。统计：检测12个新漏洞，8个违反RISC-V Zkt零延迟要求；成功率100%（二进制状态区分），中位数差异12-83 cycles；最大偏差101 cycles。bug/CVE：12个新时序漏洞（DIVUW+REM in BOOM, DIVUW/REMW/压缩指令 in CVA6等）。开销：种子生成3.67-146秒，输入生成0.53-29.15×10³秒，泄漏分析1.65-34.10×10⁴秒（表2）。Artifact：附录C提供PoC代码，但未确认公开链接。

## 核心贡献

1. 首个结合静态分析的白盒fuzzer（WhisperFuzz），提取微体系结构状态转移（MEG）实现时序漏洞检测与定位。2. 自动定位根因（通过MEG和Diagnozer算法）。3. 引入时序覆盖度量（MEP路径覆盖）。4. 在三个开源RISC-V处理器上发现12个新时序漏洞，其中8个为Zkt严重漏洞。

## 与本仓库研究主线的关系

直接相关：主题为RISC-V处理器fuzzing及时序漏洞检测，与硬件fuzzing覆盖和Oracle技术密切相关。与多hart/一致性路径的关系：本文方法聚焦单核微体系结构状态转移，未涉及多hart或内存一致性，但MEG概念可扩展至多核模块间依赖，属于强邻近工作。

## 结论

WhisperFuzz成功检测12个新时序漏洞并定位所有新/已知漏洞的根因，同时提供时序覆盖度量。方法自动化、可扩展，为处理器时序漏洞检测和缓解开辟新途径。

## 局限性

1. 操作数变异器与代码覆盖变异器的使用是启发式的，未建模最优概率（第6节）。2. 目标处理器无SMT，端口扫描漏洞无法检测。3. 当前fuzzing配置仅覆盖默认配置（如CVA6 64位），其他配置（如浮点不同位宽）未覆盖。4. 实验仅限三个开源RISC-V处理器，未在商业处理器上验证。

## 详细阅读分析

需仔细研读：MEG的提取算法（Algorithm 1）、Diagnozer定位算法（Algorithm 2）、SVA cover property生成（Algorithm 3）、操作数变异器具体实现（Section 3.8）、与SIGFuzz的详细对比（Section 5）。

## 后续核验问题

- WhisperFuzz如何扩展到多核/多hart的时序漏洞检测？是否需要考虑hart间同步？
- 操作数变异器的200个样本数量是否通过实验确定？能否自适应决定种子输入数量？
- MEG的路径爆炸问题（如多路缓存）如何系统性地解决？文中使用析取，但复杂模块是否仍面临指数增长？
