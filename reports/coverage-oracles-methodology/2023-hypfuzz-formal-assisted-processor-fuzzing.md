# HyPFuzz: Formal-Assisted Processor Fuzzing

## 基本信息

- 作者：Chen Chen、Rahul Kande、Nathan Nguyen、Flemming Andersen、Aakash Tyagi、A. Sadeghi、Jeyavijayan Rajendran
- 发表日期：2023-04-05
- 会议/期刊：USENIX Security Symposium
- 主分类：覆盖、Oracle 与 Fuzzing 方法
- 相关性：A·直接相关（score=100）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：Coverage, Oracles & Fuzzing Methodology、Formal & Directed Processor Verification
- 纳入依据：manual direct seed title
- 论文页面：[https://doi.org/10.48550/arXiv.2304.02485](https://doi.org/10.48550/arXiv.2304.02485)
- PDF：[http://arxiv.org/pdf/2304.02485](http://arxiv.org/pdf/2304.02485)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 19 页，提取 88875 字符

## 摘要

Recent research has shown that hardware fuzzers can effectively detect security vulnerabilities in modern processors. However, existing hardware fuzzers do not fuzz well the hard-to-reach design spaces. Consequently, these fuzzers cannot effectively fuzz security-critical control- and data-flow logic in the processors, hence missing security vulnerabilities. To tackle this challenge, we present HyPFuzz, a hybrid fuzzer that leverages formal verification tools to help fuzz the hard-to-reach part of the processors. To increase the effectiveness of HyPFuzz, we perform optimizations in time and space. First, we develop a scheduling strategy to prevent under- or over-utilization of the capabilities of formal tools and fuzzers. Second, we develop heuristic strategies to select points in the design space for the formal tool to target. We evaluate HyPFuzz on five widely-used open-source processors. HyPFuzz detected all the vulnerabilities detected by the most recent processor fuzzer and found three new vulnerabilities that were missed by previous extensive fuzzing and formal verification. This led to two new common vulnerabilities and exposures (CVE) entries. HyPFuzz also achieves 11.68$\times$ faster coverage than the most recent processor fuzzer.

## 研究问题

现有硬件fuzzer无法有效探索处理器设计中难以到达的设计空间（hard-to-reach design spaces），导致覆盖率低于70%，远低于行业90%标准，从而遗漏安全漏洞。

## Introduction 梳理

硬件设计日益复杂，安全漏洞在制造后难以修复。现有硬件验证技术包括形式化验证和模拟（随机回归、fuzzing）。形式化验证虽能穷举，但需人工编写属性且存在状态爆炸问题，无法验证整个处理器。随机回归难以触发硬核区域。硬件fuzzer虽优于传统方法，但覆盖率不足70%，尤其难以覆盖安全关键的控制流和数据流逻辑。本文提出HyPFuzz，一种结合形式化工具和fuzzing的混合fuzzer，利用形式化工具生成种子帮助fuzzer探索难到达区域，并通过调度和选择策略优化。

## 方法

输入生成：通过形式化工具（Cadence JasperGold）的cover property生成布尔赋值，再经test case converter转换为可执行二进制文件（指令序列）作为fuzzer种子。反馈/coverage：fuzzer使用分支覆盖率作为反馈，同时支持condition和FSM覆盖率；HyPFuzz收集覆盖率数据指导点选择。Oracle：差分测试，比较DUT（处理器RTL仿真）和黄金参考模型（GRM，RISC-V用Spike，OpenRISC用or1ksim）的架构状态（GPR、CSR、指令提交、异常），不一致表示漏洞。DUT/平台：五个开源处理器（Rocket Core、CVA6、BOOM、mor1kx、OR1200），仿真使用Synopsys VCS和Chipyard，形式化工具为Cadence JasperGold。是否需要golden model：是，使用Spike或or1ksim作为GRM。

## 实验与评估

baseline：与最先进的处理器fuzzer TheHuzz和随机回归比较。实验预算：每个实验运行72小时，重复3次；硬件为32核2.6GHz Intel Xeon，512GB RAM。统计：覆盖率、速度（覆盖率加速比）、漏洞检测时间、指令数。HyPFuzz平均比TheHuzz快11.68×覆盖率加速，3.06×运行时间加速；比随机回归快239.93×。bug/CVE：检测到TheHuzz所有11个漏洞，新发现3个漏洞（V1、V2、V3），其中V2和V3获得CVE-2022-33021和CVE-2022-33023。开销：形式化工具JasperGold在CVA6上处理所有分支点需8天，但HyPFuzz通过调度在50.71小时达到相同覆盖率；每个属性设置时间限制（通过生存分析求得）。Artifact：未提及。

## 核心贡献

提出首个结合形式化验证和fuzzing的混合硬件fuzzer HyPFuzz；开发动态调度策略和点选择策略（MaxUncovd等）；实现属性生成器和测试用例转换器；在五个处理器上评估达到更快覆盖率和发现新漏洞。

## 与本仓库研究主线的关系

直接相关（Directly relevant）。HyPFuzz专门针对处理器fuzzing，涉及RISC-V处理器，使用覆盖率反馈和差分测试Oracle，属于Coverage, Oracles & Fuzzing Methodology范畴。与多hart/一致性路径研究无直接关联，但其方法和覆盖指标可借鉴用于多核fuzzing。

## 结论

HyPFuzz通过结合形式化工具和fuzzing，解决了现有fuzzer难以覆盖硬核区域的问题。在五个开源处理器上评估，覆盖率比最先进fuzzer快11.68×，发现了三个新漏洞和两个CVE。它是第一次尝试构建混合硬件fuzzer。

## 局限性

目前仅使用分支、条件、FSM覆盖率；形式化工具JasperGold可能无法处理所有覆盖点（undetermined结果）；不支持FPGA仿真；点选择策略基于经验，小处理器上RandSel可能更好；依赖商业形式化工具（JasperGold），可能限制可移植性。

## 详细阅读分析

建议深入阅读调度策略（Section 4.3）和点选择策略（Section 4.4），以及漏洞检测方法（Section 5.5）。特别关注形式化工具输出如何转化为fuzzer种子的流程（Section 4.5）。

## 后续核验问题

- HyPFuzz的动态调度策略是否可适用于其他硬件fuzzer？
- 对于多核处理器（multi-hart）的内存一致性验证，HyPFuzz的覆盖指标和Oracle是否需要扩展？
- 如何将HyPFuzz扩展到FPGA仿真以加速？
- 除了分支覆盖，其他覆盖指标（如状态机覆盖）下HyPFuzz的效果如何？
- 点选择策略中的MaxUncovd在更大规模处理器中是否始终最优？
