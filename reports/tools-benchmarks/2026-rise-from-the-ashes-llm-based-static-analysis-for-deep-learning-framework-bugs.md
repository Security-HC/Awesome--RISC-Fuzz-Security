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
- 分析模式：仅元数据分析

## 摘要

Deep learning (DL) frameworks are critical AI infrastructures that often hide bugs with serious security implications. While dynamic approaches such as fuzzing are effective in uncovering these bugs, they require real test execution and incur high computational costs. Static analysis is a natural complement because it can detect bugs without runtime execution, offering fast and scalable testing. Unfortunately, there is still limited work targeting static analysis for DL frameworks due to their multilingual architectures and tensor-related program state. We present Phoenix, the first LLM-based static analysis technique for DL frameworks. Our key insight is that cross-language tensor flows in DL frameworks can be modeled, together with concrete code context, as a structured semantic bridge intermediate representation (SBIR) that LLMs can analyze for potential bugs in tensor semantic propagation. We implement this insight through a multi-agent workflow. A summarization agent first distills bug summaries from historical bug-fix patches and CWE rules. Guided by each summary, an extraction agent identifies bug-relevant repository symbols for code retrieval, and a generation agent synthesizes grounded SBIRs from the retrieved context. Finally, an analysis agent is leveraged to check SBIRs and report potential bugs. Our evaluation shows that Phoenix is a practical complement to dynamic DL framework testing for bug finding. To date, Phoenix has found 31 real new bugs in PyTorch for different heterogeneous hardware backends (Intel CPU, NVIDIA CUDA, and Apple MPS). Among them, 20 submitted bug-fixing patches have been merged into upstream.

## 研究问题

Deep learning (DL) frameworks are critical AI infrastructures that often hide bugs with serious security implications. While dynamic approaches such as fuzzing are effective in uncovering these bugs, they require real test execution and incur high computational costs. Static analysis is a natural complement because it can detect bugs without runtime execution, offering fast and scalable testing. Unfortunately, there is still limited work targeting static analysis for DL frameworks due to their multilingual architectures and tensor-related program state. We present Phoenix, the first LLM-based static analysis technique for DL frameworks. Our key insight is that cross-language tensor flows in DL frameworks can be modeled, together with concrete code context, as a structured semantic bridge intermediate representation (SBIR) that LLMs can analyze for potential bugs in tensor semantic propagation. We implement this insight through a multi-agent workflow. A summarization agent first distills bug summaries from historical bug-fix patches and CWE rules. Guided by each summary, an extraction agent identifies bug-relevant repository symbols for code retrieval, and a generation agent synthesizes grounded SBIRs from the retrieved context. Finally, an analysis agent is leveraged to check SBIRs and report potential bugs. Our evaluation shows that Phoenix is a practical complement to dynamic DL framework testing for bug finding. To date, Phoenix has found 31 real new bugs in PyTorch for different heterogeneous hardware backends (Intel CPU, NVIDIA CUDA, and Apple MPS). Among them, 20 submitted bug-fixing patches have been merged into upstream.

## Introduction 梳理

当前为基于题名和摘要生成的记录。配置 OPENAI_API_KEY 或 DEEPSEEK_API_KEY 后，可以启用全文阅读分析。

## 方法

等待全文提取后补充。

## 实验与评估

等待全文提取后补充。

## 结论

等待全文提取后补充。

## 局限性

等待全文提取后补充。初步阅读时应重点检查适用架构、测试对象、oracle 设计、覆盖率指标和复现实验条件。

## 详细阅读分析

等待全文提取后补充。建议结合论文 PDF、开源 artifact、实验对象和可迁移到 RISC-V/处理器 fuzzing 的部分继续分析。

## 后续跟进问题

- 论文是否提供开源实现或实验 artifact？
- 方法是否可以迁移到 RISC-V core、RTL 仿真器或真实处理器？
- 论文依赖什么 oracle、覆盖率指标或差分测试对象？
