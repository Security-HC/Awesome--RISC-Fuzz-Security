# MicroWalk: A Framework for Finding Side Channels in Binaries

## 基本信息

- 作者：Jan Wichelmann、Ahmad Moghimi、Thomas Eisenbarth、Berk Sunar
- 发表日期：2018-08-16
- 会议/期刊：arXiv
- 主分类：微架构安全自动测试
- 相关性：A·直接相关（score=5）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：Microarchitectural Security Testing
- 纳入依据：hardware/processor object: cpu, microarchitectural；verification/fuzzing method: verification；security relevance: security, side channel, leakage
- 论文页面：[http://arxiv.org/abs/1808.05575v2](http://arxiv.org/abs/1808.05575v2)
- PDF：[https://arxiv.org/pdf/1808.05575v2](https://arxiv.org/pdf/1808.05575v2)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 12 页，提取 76960 字符

## 摘要

Microarchitectural side channels expose unprotected software to information leakage attacks where a software adversary is able to track runtime behavior of a benign process and steal secrets such as cryptographic keys. As suggested by incremental software patches for the RSA algorithm against variants of side-channel attacks within different versions of cryptographic libraries, protecting security-critical algorithms against side channels is an intricate task. Software protections avoid leakages by operating in constant time with a uniform resource usage pattern independent of the processed secret. In this respect, automated testing and verification of software binaries for leakage-free behavior is of importance, particularly when the source code is not available. In this work, we propose a novel technique based on Dynamic Binary Instrumentation and Mutual Information Analysis to efficiently locate and quantify memory based and control-flow based microarchitectural leakages. We develop a software framework named \tool~for side-channel analysis of binaries which can be extended to support new classes of leakage. For the first time, by utilizing \tool, we perform rigorous leakage analysis of two widely-used closed-source cryptographic libraries: \emph{Intel IPP} and \emph{Microsoft CNG}. We analyze $15$ different cryptographic implementations consisting of $112$ million instructions in about $105$ minutes of CPU time. By locating previously unknown leakages in hardened implementations, our results suggest that \tool~can efficiently find microarchitectural leakages in software binaries.

## 研究问题

二进制软件中微架构侧信道的自动检测与量化，尤其针对闭源密码学库。

## Introduction 梳理

现有自动化侧信道检测方法（如静态分析、符号执行）存在局限性：依赖源码、无法处理编译器引入的泄漏、开销大等。本文提出基于动态二进制插桩（DBI）和互信息分析（MI）的技术，能够高效定位和量化二进制中的内存和基于控制流的微架构泄漏，并首次对闭源库Intel IPP和Microsoft CNG进行系统分析，发现未知漏洞。

## 方法

输入生成：使用密码学安全随机数生成器生成随机测试用例，支持自定义格式（如PEM）；反馈/覆盖：通过Pin进行DBI收集内存访问、分支、堆/栈操作等轨迹，并支持CPU指令模拟和RDRAND覆盖；Oracle：基于轨迹比较、全轨迹MI、单指令MI三类分析，不依赖golden model；DUT：x86/64二进制可执行文件或库；平台：Intel Core i7-7700, Windows 10, Pin v3.6。

## 实验与评估

baseline：未明确对比基线；实验预算：分析15个实现共1.12亿条指令，耗时约105分钟；统计：Intel IPP发现13个泄漏，MS CNG发现4个泄漏；bug/CVE：已分配CVE-2018-12155、CVE-2018-12156；开销：时间开销如表1所示（73分钟分析9200万条指令）；Artifact：开源框架（https://github.com/UzL-ITS/Microwalk）。

## 核心贡献

1. 首次对闭源库Intel IPP和MS CNG进行系统侧信道泄漏分析，发现新漏洞；2. 提出基于DBI和MI的二进制泄漏检测技术，支持内存和基于控制流的泄漏；3. 开源框架，易于扩展。

## 与本仓库研究主线的关系

强邻近：属于微架构安全自动测试范畴，方法可借鉴用于处理器/RTL级fuzzing，但与多hart/内存一致性路径无直接关系。

## 结论

MicroWalk框架能够高效发现二进制中的微架构泄漏，在Intel IPP和MS CNG中定位了多个之前未知的泄漏，表明现有防护不完善，并已向厂商报告。

## 局限性

正文未明确列出，但从未来工作可推断：随机测试用例对非密码学协议或数据结构覆盖率不足；控制流泄漏在高层算法中可能掩盖底层子程序泄漏；区分调用图中泄漏根因困难。

## 详细阅读分析

是，需深入理解MI在单指令层面的应用细节、哈希压缩方法、以及泄漏量化与定位技术。

## 后续核验问题

- 如何将MicroWalk扩展至多hart场景？
- 对于非密码学二进制，如何利用覆盖率引导提高测试效率？
- 能否将MI分析用于硬件RTL级泄漏检测？
