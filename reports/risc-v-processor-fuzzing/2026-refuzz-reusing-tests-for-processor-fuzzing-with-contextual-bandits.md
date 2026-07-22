# ReFuzz: Reusing Tests for Processor Fuzzing with Contextual Bandits

## 基本信息

- 作者：Chen Chen、Zaiyan Xu、Mohamadreza Rostami、David Liu、Dileep Kalathil、Ahmad‐Reza Sadeghi、Jeyavijayan Rajendran
- 发表日期：2026-01-01
- 会议/期刊：未记录
- 主分类：RISC-V 处理器 Fuzzing
- 相关性：A·直接相关（score=100）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：RISC-V Processor Fuzzing、Coverage, Oracles & Fuzzing Methodology
- 纳入依据：manual direct seed title
- 论文页面：[https://doi.org/10.14722/ndss.2026.240118](https://doi.org/10.14722/ndss.2026.240118)
- PDF：[https://doi.org/10.14722/ndss.2026.240118](https://doi.org/10.14722/ndss.2026.240118)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 18 页，提取 100000 字符

## 摘要

Processor designs rely on iterative modifications and reuse well-established designs.However, this reuse of prior designs also leads to similar vulnerabilities across multiple processors.As processors grow increasingly complex with iterative modifications, efficiently detecting vulnerabilities from modern processors is critical.Inspired by software fuzzing, hardware fuzzing has recently demonstrated its effectiveness in detecting processor vulnerabilities.Yet, to our best knowledge, existing processor fuzzers fuzz each design individually, lacking the capability to understand known vulnerabilities in prior processors to finetune fuzzing to identify similar or new variants of vulnerabilities.To address this gap, we present ReFuzz, an adaptive fuzzing framework that leverages contextual bandit to reuse highly effective tests from prior processors to fuzz a processor-undertest (PUT) within a given ISA.By intelligently mutating tests that trigger vulnerabilities in prior processors, ReFuzz detects similar and new variants of vulnerabilities in PUTs.ReFuzz uncovered three new security vulnerabilities and two new functional bugs.ReFuzz detected one vulnerability by reusing a test that triggers a known vulnerability in a prior processor.One functional bug exists across three processors that share design modules.The second bug has two variants.Additionally, ReFuzz reuses highly effective tests to enhance efficiency in coverage, achieving an average 511.23coverage speedup and up to 9.33% more total coverage, compared to existing fuzzers.

## 研究问题

现有处理器fuzzer独立地对每个设计进行fuzzing，未能利用先前处理器中已知漏洞的知识来微调fuzzing以发现相似或新的漏洞变体。

## Introduction 梳理

处理器设计依赖于迭代修改和设计复用，但这也导致相似漏洞跨处理器传播。现有硬件fuzzer逐设计独立fuzzing，缺乏利用先前处理器已知漏洞来指导fuzzing的能力。ReFuzz提出首个利用上下文强盗（contextual bandit）自适应复用先前处理器有效测试的框架，以提升对被测处理器（PUT）的fuzzing效率。

## 方法

输入生成：从先前处理器fuzzing campaign中收集测试（包括漏洞测试和覆盖测试），通过测试最小化器去除冗余后，使用自适应上下文强盗算法训练模型，输出漏洞列表和多个覆盖列表。fuzzing时，ReFuzz与现有fuzzer集成，先使用漏洞列表，再使用覆盖列表，动态决定是继续变异当前测试还是切换到下一个。反馈/覆盖：使用Synopsys VCS收集分支覆盖或条件覆盖作为反馈和上下文。Oracle：采用差分测试，以Spike作为golden reference模型。DUT/平台：在Chipyard环境中模拟CVA6、Rocket Core、BOOMV3、BOOMV4和RSD等RISC-V处理器。无需golden model（Spike为golden reference）。

## 实验与评估

Baseline：TheHuzz和Cascade。实验预算：每个fuzzer生成21K测试，重复3次取平均。统计：ReFuzz平均覆盖加速511.23×，最高9.33%更多总覆盖。Bug/CVE：发现3个新安全漏洞和2个新功能bug，CVSS评分7.1至8.5。开销：训练阶段测试最小化平均944.28秒，CB训练约1.30小时。Artifact：论文未明确提供artifact可用性，但提及测试来自公开处理器和fuzzer。

## 核心贡献

1) 首个利用上下文强盗算法复用先前处理器测试的硬件fuzzing框架。2) 提出了自适应CB算法和测试最小化器，有效识别高效应测试。3) 实验证明该方法可检测到已知漏洞的变体以及新漏洞，覆盖速度提升511.23×，总覆盖提升1.89%。

## 与本仓库研究主线的关系

方法借鉴。ReFuzz不直接处理多hart或内存一致性验证，但其测试复用和变异思想可潜在应用于多hart一致性测试的生成。不过本文聚焦单处理器fuzzing，与多hart/一致性路径研究弱相关。

## 结论

ReFuzz通过复用和变异先前处理器的有效测试，显著提升了fuzzing的覆盖速度和总覆盖，并成功检测到跨处理器漏洞及其变体，验证了设计复用导致漏洞传播的现象。

## 局限性

1) 当PUT为32位而训练处理器为64位时，PP-tests的有效性降低（如RSD上覆盖提升有限）。2) 依赖现有fuzzer的突变引擎，若fuzzer缺乏突变能力（如Cascade），则提升较小。3) 测试最小化使用整数规划，大规模工业测试套件可能面临可扩展性问题。4) 对于没有历史设计数据的供应商，复用受限。

## 详细阅读分析

建议重点关注其上下文强盗建模、自适应消除无效测试的算法，以及测试最小化如何影响训练效率。同时注意其对不同ISA宽度（32-bit vs 64-bit）的限制。

## 后续核验问题

- ReFuzz是否可扩展到支持多hart的处理器或跨ISA复用？
- 测试最小化中的整数规划如何适应更大规模的测试集？
- 当PUT与训练处理器ISA扩展不同时，如何调整测试复用？
