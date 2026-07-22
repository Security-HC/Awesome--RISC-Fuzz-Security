# Rise From The Ashes: LLM-based Static Analysis for Deep Learning Framework Bugs

## 基本信息

- 作者：Shaoyu Yang、Haifeng Lin、Chunrong Fang、Xiang Chen、Wei Cheng、Jiawei Liu、Yiyu Zhang、Hongyu Liu、Zhenyu Chen
- 发表日期：2026-07-01
- 会议/期刊：arXiv
- 主分类：形式化与定向处理器验证
- 相关性：A·直接相关（score=5）
- 证据等级：摘要级
- 标签：Formal & Directed Processor Verification
- 纳入依据：hardware/processor object: cpu；verification/fuzzing method: fuzz；security relevance: security
- 论文页面：[http://arxiv.org/abs/2607.00555v1](http://arxiv.org/abs/2607.00555v1)
- PDF：[https://arxiv.org/pdf/2607.00555v1](https://arxiv.org/pdf/2607.00555v1)
- 分析模式：DeepSeek PDF 首 8 页与末 2 页文本：deepseek-v4-flash

## 摘要

Deep learning (DL) frameworks are critical AI infrastructures that often hide bugs with serious security implications. While dynamic approaches such as fuzzing are effective in uncovering these bugs, they require real test execution and incur high computational costs. Static analysis is a natural complement because it can detect bugs without runtime execution, offering fast and scalable testing. Unfortunately, there is still limited work targeting static analysis for DL frameworks due to their multilingual architectures and tensor-related program state. We present Phoenix, the first LLM-based static analysis technique for DL frameworks. Our key insight is that cross-language tensor flows in DL frameworks can be modeled, together with concrete code context, as a structured semantic bridge intermediate representation (SBIR) that LLMs can analyze for potential bugs in tensor semantic propagation. We implement this insight through a multi-agent workflow. A summarization agent first distills bug summaries from historical bug-fix patches and CWE rules. Guided by each summary, an extraction agent identifies bug-relevant repository symbols for code retrieval, and a generation agent synthesizes grounded SBIRs from the retrieved context. Finally, an analysis agent is leveraged to check SBIRs and report potential bugs. Our evaluation shows that Phoenix is a practical complement to dynamic DL framework testing for bug finding. To date, Phoenix has found 31 real new bugs in PyTorch for different heterogeneous hardware backends (Intel CPU, NVIDIA CUDA, and Apple MPS). Among them, 20 submitted bug-fixing patches have been merged into upstream.

## 研究问题

深度学习框架中跨语言张量语义错误的静态检测问题。现有动态测试（如fuzzing）需要执行代码且成本高，而传统静态分析工具无法处理多语言架构和张量相关程序状态。

## Introduction 梳理

现有动态测试方法（如fuzzing）能有效发现深度学习框架错误，但需要构造可执行测试并承担高计算成本。静态分析作为补充，可以无需运行代码检测错误，但现有工具（如Bandit、Clang Static Analyzer）因难以处理Python/C++/CUDA多语言架构和张量语义而效果不佳。本文提出Phoenix，首个基于LLM的静态分析技术，通过构建语义桥接中间表示（SBIR）捕获跨语言张量传播的语义约束，并由多智能体工作流实现。

## 方法

输入生成：从PyTorch历史bug修复PR和CWE规则中提取缺陷知识，经LLM总结为结构化bug摘要。反馈/覆盖：无显式覆盖度量，基于SBIR的语义一致性检查作为oracle。DUT/平台：PyTorch（Python/C++/CUDA混合架构）。需要Golden Model：否。具体流程：1）LLM-based Bug Summarization：生成归一化的bug摘要；2）LLM-based SBIR Generation：通过Extract-Retrieve-Generate（ERG）策略，提取标识符、检索代码上下文、生成SBIR；3）LLM-based SBIR Analysis：分析SBIR中的语义约束是否在跨语言传播中破坏，输出bug报告。

## 实验与评估

Baseline：静态工具Bandit（仅Python）和Clang Static Analyzer（C/C++/CUDA）；动态工具TitanFuzz和WhiteFox（LLM-based fuzzers）。实验预算：使用GPT-5.4，每个PR/CWE项目处理10次。统计：Phoenix报告36个警报，其中31个为真实bug（13.89%假阳性）；Bandit报告172个警报仅1个真实bug（99.41%假阳性）；CSA报告218个警报全部假阳性。与动态工具重叠：仅1个bug与TitanFuzz/WhiteFox重叠，30个为Phoenix独有，19个为动态工具独有。Bug/CVE：31个新bug，26个被确认，20个补丁已合并。开销：未明确报告时间开销。Artifact：补丁已提交到PyTorch上游。

## 核心贡献

1) 提出面向深度学习框架的跨语言张量语义一致性静态分析视角，将bug模式形式化为跨张量语义不一致。2) 设计Phoenix，基于LLM的多智能体工作流，包括bug摘要、基于检索的SBIR生成和语义分析。3) 实验证明Phoenix在PyTorch上以低假阳性率发现31个真实bug，且与动态测试互补。4) 26个bug被确认，20个补丁已合并。

## 与本仓库研究主线的关系

不相关。本文针对深度学习框架（PyTorch）的静态分析，而本数据库聚焦于RISC-V/处理器Fuzzing、多hart与内存一致性验证、微架构安全自动测试、RTL/SoC硬件Fuzzing。本文方法（基于SBIR和LLM）可能为硬件描述语言的多层次语义分析提供思路，但无直接关联。

## 结论

Phoenix能有效检测深度学习框架中的跨语言张量语义错误，且与动态fuzzing互补。在PyTorch上发现31个真实bug，其中30个未被现有LLM-based fuzzer发现。SBIR为跨层语义分析提供了可行的抽象。

## 局限性

评估限于PyTorch一个框架，可能不具普遍性；bug知识来源（历史PR和CWE）可能遗漏部分bug类型；依赖LLM质量，LLM的不确定性可能影响重复性；未评估扩展性（如千级API数量时的性能）。

## 详细阅读分析

如果关注LLM辅助静态分析或跨语言语义建模，可深入阅读；但对于处理器验证或硬件Fuzzing主题，仅作为工具方法论参考，无直接借鉴价值。

## 后续核验问题

- SBIR能否适应硬件描述语言（Verilog/VHDL）的跨层次语义？LLM能否用于分析RTL中的时序约束一致性？Phoenix的多智能体框架是否可迁移到SoC互连协议验证（如AXI）？
