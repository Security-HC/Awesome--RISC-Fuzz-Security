# Rise From The Ashes: LLM-based Static Analysis for Deep Learning Framework Bugs

## 基本信息

- 作者：Shaoyu Yang、Haifeng Lin、Chunrong Fang、Xiang Chen、Wei Cheng、Jiawei Liu、Yiyu Zhang、Hongyu Liu、Zhenyu Chen
- 发表日期：2026-07-01
- 会议/期刊：arXiv
- 主分类：形式化与定向处理器验证
- 相关性：A·直接相关（score=5）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：Formal & Directed Processor Verification
- 纳入依据：hardware/processor object: cpu；verification/fuzzing method: fuzz；security relevance: security
- 论文页面：[http://arxiv.org/abs/2607.00555v1](http://arxiv.org/abs/2607.00555v1)
- PDF：[https://arxiv.org/pdf/2607.00555v1](https://arxiv.org/pdf/2607.00555v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 12 页，提取 67605 字符

## 摘要

Deep learning (DL) frameworks are critical AI infrastructures that often hide bugs with serious security implications. While dynamic approaches such as fuzzing are effective in uncovering these bugs, they require real test execution and incur high computational costs. Static analysis is a natural complement because it can detect bugs without runtime execution, offering fast and scalable testing. Unfortunately, there is still limited work targeting static analysis for DL frameworks due to their multilingual architectures and tensor-related program state. We present Phoenix, the first LLM-based static analysis technique for DL frameworks. Our key insight is that cross-language tensor flows in DL frameworks can be modeled, together with concrete code context, as a structured semantic bridge intermediate representation (SBIR) that LLMs can analyze for potential bugs in tensor semantic propagation. We implement this insight through a multi-agent workflow. A summarization agent first distills bug summaries from historical bug-fix patches and CWE rules. Guided by each summary, an extraction agent identifies bug-relevant repository symbols for code retrieval, and a generation agent synthesizes grounded SBIRs from the retrieved context. Finally, an analysis agent is leveraged to check SBIRs and report potential bugs. Our evaluation shows that Phoenix is a practical complement to dynamic DL framework testing for bug finding. To date, Phoenix has found 31 real new bugs in PyTorch for different heterogeneous hardware backends (Intel CPU, NVIDIA CUDA, and Apple MPS). Among them, 20 submitted bug-fixing patches have been merged into upstream.

## 研究问题

针对深度学习框架中跨语言张量语义不一致导致的安全漏洞，现有动态测试（fuzzing）虽有效但需执行测试且成本高，而传统静态分析工具（如Bandit、CSA）无法处理多语言架构和张量相关程序状态，缺乏实用的静态分析技术。

## Introduction 梳理

深度学习框架是关键的AI基础设施，其错误可能带来严重安全影响。动态测试（如fuzzing）需要实际执行，计算成本高昂；静态分析无需运行即可检测缺陷，但现有工具因框架的多语言架构和基于张量的程序状态而难以适用。本文提出Phoenix，首个基于LLM的静态分析技术，核心洞察是可将跨语言张量流与具体代码上下文建模为结构化语义桥接中间表示（SBIR），并利用LLM进行语义不一致性分析。贡献包括：提出跨语言张量语义不一致的静态分析视角；设计多智能体工作流（总结、提取、生成、分析）；评估发现31个真实错误，与传统和动态工具互补；20个补丁已被合入上游。

## 方法

Phoenix使用基于LLM的多智能体工作流。输入生成：从历史bug-fix PR和CWE规则构建bug数据集（56项）。反馈/coverage：无反馈循环，不涉及覆盖率。Oracle：通过分析智能体检查SBIR中的语义约束是否被破坏，输出bug报告或'No bug'。DUT/平台：PyTorch（Python/C++/CUDA混合架构）。是否需要golden model：不需要，基于语义一致性推断。具体步骤：(1) 总结智能体利用LLM将bug数据归纳为结构化bug总结；(2) 提取智能体根据总结识别代码仓库中的关键标识符；(3) 生成智能体利用检索的代码上下文合成SBIR（记录源/目标实体、传输类型、语义属性、代码上下文）；(4) 分析智能体检查SBIR中的约束是否一致，报告潜在bug。

## 实验与评估

baseline：静态工具Bandit（Python）和CSA（C/C++/CUDA）；动态工具TitanFuzz和WhiteFox（基于LLM的fuzzer）。实验预算：使用GPT-5.4，每个bug项处理10次生成SBIR。统计：Phoenix报告36个告警，31个真实bug（5个假阳性，假阳性率13.89%）；Bandit发现1个真实bug（172告警，99.41%假阳性）；CSA发现0个真实bug（218告警，100%假阳性）。与动态工具正交性：30个bug未被TitanFuzz/WhiteFox发现，19个动态发现的bug未被Phoenix检测。bug实例：跨CPU、CUDA、MPS后端的31个bug中26个已确认，20个补丁已合入主线。开销：未明确报告时间和计算开销。Artifact：论文提及补丁已合并至PyTorch仓库，未提供独立artifact包。

## 核心贡献

1. 提出跨语言张量语义不一致的静态分析新视角；2. 设计Phoenix技术，基于LLM的多智能体工作流（总结、提取、生成、分析）和语义桥接中间表示SBIR；3. 在PyTorch上发现31个真实bug，26个确认，20个补丁合并；4. 证明静态分析与动态fuzzing正交互补，联合覆盖50个bug。

## 与本仓库研究主线的关系

本文研究对象是深度学习框架（PyTorch），而非处理器或RISC-V、多hart一致性等硬件验证主题。因此不直接相关。但其中基于LLM的语义中间表示和多智能体工作流方法可能启发放到硬件静态分析中，例如将硬件模块间的信号传递建模为类似SBIR的表示。属于方法借鉴层次，与多hart/一致性路径等无直接关系。

## 结论

Phoenix是首个基于LLM的深度学习框架静态分析技术，通过SBIR捕获跨语言张量语义传播，利用LLM智能体构建和分析语义桥。在PyTorch上检测到31个真实bug，其中26个被确认，20个补丁已合并。结果表明，SBIR引导的LLM静态分析是对现有动态测试的有效补充。

## 局限性

内部有效性威胁：手动决策（如PR筛选、CWE选择）、基线配置（未完全公平对比）、LLM非确定性（重复10次缓解）。外部有效性威胁：仅评估PyTorch，结果可能不直接泛化到其他框架；bug知识源（40个PR+16个CWE）可能遗漏部分bug类型。

## 详细阅读分析

对于希望在LLM辅助代码分析中应用中间表示或多智能体协作的读者，本文提供了详细设计（SBIR形式定义、ERG策略、prompt模板等），值得参考。但对于本仓库的处理器验证主题，深入阅读的必要性较低。

## 后续核验问题

- 如何将SBIR思想扩展到硬件设计中跨模块的语义保真性检查？
- Phoenix的多智能体架构能否用于RTL级静态安全分析？
- 论文中SBIR对张量属性的建模能否类比于硬件中的信号属性（如宽度、使能、时序）？
