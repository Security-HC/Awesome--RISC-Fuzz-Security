# GoldenFuzz: Generative Golden Reference Hardware Fuzzing

## 基本信息

- 作者：Lichao Wu、Mohamadreza Rostami、Huimin Li、Nikhilesh Singh、Ahmad-Reza Sadeghi
- 发表日期：2026-01-01
- 会议/期刊：未记录
- 主分类：RISC-V 处理器 Fuzzing
- 相关性：A·直接相关（score=100）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：RISC-V Processor Fuzzing、Coverage, Oracles & Fuzzing Methodology
- 纳入依据：manual direct seed title
- 论文页面：[https://doi.org/10.14722/ndss.2026.231663](https://doi.org/10.14722/ndss.2026.231663)
- PDF：[https://doi.org/10.14722/ndss.2026.231663](https://doi.org/10.14722/ndss.2026.231663)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 16 页，提取 86567 字符

## 摘要

Modern hardware systems, driven by demands for high performance and application-specific functionality, have grown increasingly complex, introducing large surfaces for bugs and security-critical vulnerabilities. Fuzzing has emerged as a scalable solution for discovering such flaws. Yet, existing hardware fuzzers suffer from limited semantic awareness, inefficient test refinement, and high computational overhead due to reliance on slow device simulation. In this paper, we present GoldenFuzz, a novel two-stage hardware fuzzing framework that partially decouples test case refinement from coverage and vulnerability exploration. GoldenFuzz leverages a fast, ISA-compliant Golden Reference Model (GRM) as a ``digital twin'' of the Device Under Test (DUT). It fuzzes the GRM first, enabling rapid, low-cost test case refinement, accelerating deep architectural exploration and vulnerability discovery on DUT. During the fuzzing pipeline, GoldenFuzz iteratively constructs test cases by concatenating carefully chosen instruction blocks that balance the subtle inter- and intra-instructions quality. A feedback-driven mechanism leveraging insights from both high- and low-coverage samples further enhances GoldenFuzz's capability in hardware state exploration. Our evaluation of three RISC-V processors, RocketChip, BOOM, and CVA6, demonstrates that GoldenFuzz significantly outperforms existing fuzzers in achieving the highest coverage with minimal test case length and computational overhead. GoldenFuzz uncovers all known vulnerabilities and discovers five new ones, four of which are classified as highly severe with CVSS v3 severity scores exceeding seven out of ten. It also identifies two previously unknown vulnerabilities in the commercial BA51-H core extension.

## 研究问题

现有硬件fuzzer缺乏语义感知、测试用例优化效率低、依赖慢速设备仿真导致高计算开销，难以高效发现深层硬件漏洞。

## Introduction 梳理

现代处理器复杂度增加引入大量bug和安全漏洞，硬件fuzzing成为可扩展解决方案，但现有fuzzer存在三大挑战：随机变异无法捕捉ISA复杂依赖；测试用例优化缺乏结构化机制；全部在慢速DUT仿真上执行导致高开销。本文提出GoldenFuzz，通过两阶段框架解耦测试用例优化与覆盖探索，先利用快速ISA兼容的Golden Reference Model (GRM)进行低成本策略优化，再在DUT上进行深度探索，从而加速漏洞发现。贡献包括：首次利用GRM作为数字孪生加速策略优化；块级测试用例生成与混合评分机制；基于语言模型的生成器结合胜负样本偏好优化。

## 方法

{'dut_platform': 'RocketChip、BOOM、CVA6；GRM使用Spike模拟器。', 'feedback_coverage': 'GRM阶段使用有效性反馈；DUT阶段使用硬件覆盖率（FSM、条件、行覆盖），并采用intra-test和inter-test双层评分机制。', 'golden_model_required': '是，需要GRM作为数字孪生进行策略优化和差分Oracle。', 'input_generation': '基于定制GPT-2模型，通过块级生成策略（每测试用例5个指令块，每块6条指令），利用GRM或DUT反馈通过SimPO进行策略优化。', 'oracle': '差分测试：比较DUT（Synopsys VCS）与GRM（Spike）的执行轨迹，并采用已知不匹配过滤机制。'}

## 实验与评估

{'artifact': '代码将限制访问，仅提供请求。', 'baseline': 'Cascade, DifuzzRTL, TheHuzz, ChatFuzz', 'bug_cve': '发现5个新漏洞（CVA6上4个严重，CVSS>7；1个中等5.5），2个在商业BA51-H核心中，并获取CVE-2025-45883和CVE-2025-45881。', 'experiment_budget': '未明确说明总测试用例数量或时间预算，但提到GRM fuzzing阶段每次迭代产生80个IBs，DUT fuzzing阶段每测试用例1.36秒（80并行）。', 'overhead': '预训练约1小时（A6000 GPU）；测试用例生成CPU 0.34s、GPU 0.012s；策略优化每迭代<40s GPU；DUT仿真1.36s/用例（80并行）。', 'statistical_results': 'GoldenFuzz在覆盖率（条件、行、FSM）上 consistently 超越所有baseline，且测试用例长度仅30条指令。'}

## 核心贡献

['首次利用GRM进行低成本fuzzing策略优化', '块级指令生成与混合评分机制', '基于语言模型和偏好优化的在线策略更新', '发现5个新漏洞（4个严重）和2个商业核心漏洞']

## 与本仓库研究主线的关系

直接相关：针对RISC-V处理器fuzzing，但未涉及多hart或内存一致性验证；可借鉴块生成和双阶段方法到多核场景。

## 结论

GoldenFuzz通过两阶段解耦和GRM数字双胞胎，显著提升覆盖率和漏洞发现效率，发现7个新漏洞，四个严重。

## 局限性

依赖GRM和RTL级覆盖率；对闭源或缺乏GRM的ISA适应性有限；手动分析仍必要（每漏洞5-30分钟）。

## 详细阅读分析

是

## 后续核验问题

- GRM与DUT的差异如何影响漏洞检测？
- 如何将两阶段方法扩展到多核一致性验证？
- 语言模型的过拟合风险如何进一步缓解？
