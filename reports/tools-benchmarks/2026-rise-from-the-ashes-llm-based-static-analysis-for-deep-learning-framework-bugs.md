# Rise From The Ashes: LLM-based Static Analysis for Deep Learning Framework Bugs

## 基本信息

- 作者：Shaoyu Yang、Haifeng Lin、Chunrong Fang、Xiang Chen、Wei Cheng、Jiawei Liu、Yiyu Zhang、Hongyu Liu、Zhenyu Chen
- 发表日期：2026-07-01
- 更新日期：2026-07-01
- 来源：arXiv
- 来源编号：2607.00555v1
- 研究类别：工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：2
- 论文页面：[http://arxiv.org/abs/2607.00555v1](http://arxiv.org/abs/2607.00555v1)
- PDF：[https://arxiv.org/pdf/2607.00555v1](https://arxiv.org/pdf/2607.00555v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash

## 摘要

Deep learning (DL) frameworks are critical AI infrastructures that often hide bugs with serious security implications. While dynamic approaches such as fuzzing are effective in uncovering these bugs, they require real test execution and incur high computational costs. Static analysis is a natural complement because it can detect bugs without runtime execution, offering fast and scalable testing. Unfortunately, there is still limited work targeting static analysis for DL frameworks due to their multilingual architectures and tensor-related program state. We present Phoenix, the first LLM-based static analysis technique for DL frameworks. Our key insight is that cross-language tensor flows in DL frameworks can be modeled, together with concrete code context, as a structured semantic bridge intermediate representation (SBIR) that LLMs can analyze for potential bugs in tensor semantic propagation. We implement this insight through a multi-agent workflow. A summarization agent first distills bug summaries from historical bug-fix patches and CWE rules. Guided by each summary, an extraction agent identifies bug-relevant repository symbols for code retrieval, and a generation agent synthesizes grounded SBIRs from the retrieved context. Finally, an analysis agent is leveraged to check SBIRs and report potential bugs. Our evaluation shows that Phoenix is a practical complement to dynamic DL framework testing for bug finding. To date, Phoenix has found 31 real new bugs in PyTorch for different heterogeneous hardware backends (Intel CPU, NVIDIA CUDA, and Apple MPS). Among them, 20 submitted bug-fixing patches have been merged into upstream.

## 研究问题

深度学习框架中跨语言张量语义不一致导致的bug难以通过现有静态分析工具检测，因为现有工具无法处理多语言架构（Python/C++/CUDA）和张量相关程序状态。

## Introduction 梳理

深度学习框架（如PyTorch）是关键的AI基础设施，其bug可能造成严重后果。动态测试（如fuzzing）虽有效，但需要实际执行且计算成本高。静态分析作为补充无需运行时执行，但现有工具（如Bandit、CSA）无法处理框架的多语言架构和张量语义。本文提出Phoenix，首个基于LLM的静态分析技术，通过建模跨语言张量流为语义桥接中间表示（SBIR），结合多智能体工作流（总结代理、提取代理、生成代理、分析代理）检测bug。在PyTorch上发现31个真实bug，其中20个补丁已合并。

## 方法

Phoenix包含四个阶段：1) 构建bug数据集：从PyTorch历史修复PR和CWE规则中收集56个弱项。2) LLM总结：使用LLM从PR和CWE中提取结构化bug模式（向下具体化或向上泛化）。3) ERG策略：提取代理从bug模式和摘要中预测精确代码标识符，检索函数级代码上下文；生成代理基于上下文生成SBIR（五元组：源实体、目标实体、传输类型、约束集、代码上下文）。4) 分析代理：LLM检查SBIR中语义约束的一致性，若违反则输出bug报告。SBIR抽象了跨语言张量属性（dtype、shape、device等）的传递。

## 实验与评估

在PyTorch上评估：Phoenix报告36个告警，其中31个为真实bug（假阳性率13.89%），显著优于Bandit（172告警，1个真bug，假阳性率99.41%）和CSA（218告警，0个真bug）。与动态fuzzer（TitanFuzz、WhiteFox）对比，Phoenix检测的31个bug中30个未被动态方法发现，而动态方法检测的20个bug中19个未被Phoenix发现，显示正交性。bug类型覆盖验证逻辑、前置条件、语义公式、API契约等，且分布于CPU（9个）、CUDA（7个）、MPS（2个）及其他组件（13个）。26个被维护者确认，20个补丁已合并。

## 结论

Phoenix是首个基于LLM的DL框架静态分析技术，通过SBIR捕获跨语言张量语义传播，有效检测跨层语义不一致漏洞。实验表明其优于传统静态分析工具，并与动态fuzzing互补，共同覆盖更广的bug空间。

## 局限性

1) 依赖LLM的性能和训练数据，可能漏检与训练数据中模式不同的bug。2) SBIR作为轻量级抽象可能无法完整表示复杂张量语义（如高阶数学属性）。3) bug数据集仅包含PyTorch历史修复和CWE规则，对新框架或未覆盖的bug类型泛化性有限。4) 13.89%的假阳性率仍需要人工确认。5) 仅针对PyTorch评估，对其他DL框架（如JAX、TVM）的适用性未知。6) 依赖于检索到的代码上下文，若检索失败则无法生成SBIR。

## 详细阅读分析

论文的核心洞察是将跨语言张量流建模为SBIR，这是一个结构化的五元组（源实体、目标实体、传输类型、约束集、代码上下文），抽象了语言特定语法，保留了张量属性（shape/dtype/device等）和守卫条件。多智能体工作流的设计使LLM专注于具体代码上下文而非全局扫描：总结代理构建领域知识，提取代理精确定位代码标识符（如API名或内核函数），生成代理基于真实代码生成SBIR，分析代理检查语义一致性。ERG策略通过分离提取和生成步骤，避免了LLM直接搜索整个代码库导致的幻觉。实验的互补性分析表明，静态SBIR分析能发现动态测试难以触发的潜伏语义不一致，尤其是涉及多后端配置的bug。

## 后续跟进问题

- 1) Phoenix能否扩展到其他深度学习框架（如JAX、TensorFlow）或异构计算平台？2) SBIR的传输类型和元数据键是否可以自动扩展以适应新类型的跨语言bug？3) 不同LLM（如开源模型）对Phoenix性能（检测率和假阳性率）有何影响？4) 能否通过结合轻量级动态分析（如符号执行）进一步减少假阳性并提高检测覆盖率？5) 如何自动维护和更新bug数据集以适应框架的持续演进？
