# RAG-Based Fuzzing of Cross-Architecture Compilers

## 基本信息

- 作者：Rana Elnaggar、Brian Delgado、Jason M. Fung
- 发表日期：2025-04-11
- 更新日期：2025-04-11
- 来源：arXiv
- 来源编号：2504.08967v1
- 研究类别：工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2504.08967v1](http://arxiv.org/abs/2504.08967v1)
- PDF：[https://arxiv.org/pdf/2504.08967v1](https://arxiv.org/pdf/2504.08967v1)
- 分析模式：仅元数据分析

## 摘要

OneAPI is an open standard that supports cross-architecture software development with minimal effort from developers. It brings DPC++ and C++ compilers which need to be thoroughly tested to verify their correctness, reliability, and security. Compilers have numerous code flows and optimization features. This process requires developers with deep understanding of the different compiler flows to craft testcases specific to target paths in the compiler. This testcase creation is a time-consuming and costly process. In this paper, we propose a large-language model (LLM)-based compiler fuzzing tool that integrates the concept of retrieval-augmented generation (RAG). This tool automates the testcase generation task and relieves experienced compiler developers from investing time to craft testcase generation patterns. We test our proposed approach on the Intel DPC++/C++ compiler. This compiler compiles SYCL code and allows developers to offload it to different architectures, e.g. GPUs and CPUs from different vendors. Using this tool, we managed to identify 87 SYCL code test cases that lead to output value mismatch or compiler runtime errors when compiled using Intel DPC++ and clang++ compilers and run on different architectures. The testcases and the identified unexpected behaviors of the compilers under test were obtained within only few hours with no prior background on the compiler passes under tests. This tool facilitates efficient compiler fuzzing with reduced developer time requirements via the dynamic testcase creation capability provided by an LLM with RAG.

## 研究问题

OneAPI is an open standard that supports cross-architecture software development with minimal effort from developers. It brings DPC++ and C++ compilers which need to be thoroughly tested to verify their correctness, reliability, and security. Compilers have numerous code flows and optimization features. This process requires developers with deep understanding of the different compiler flows to craft testcases specific to target paths in the compiler. This testcase creation is a time-consuming and costly process. In this paper, we propose a large-language model (LLM)-based compiler fuzzing tool that integrates the concept of retrieval-augmented generation (RAG). This tool automates the testcase generation task and relieves experienced compiler developers from investing time to craft testcase generation patterns. We test our proposed approach on the Intel DPC++/C++ compiler. This compiler compiles SYCL code and allows developers to offload it to different architectures, e.g. GPUs and CPUs from different vendors. Using this tool, we managed to identify 87 SYCL code test cases that lead to output value mismatch or compiler runtime errors when compiled using Intel DPC++ and clang++ compilers and run on different architectures. The testcases and the identified unexpected behaviors of the compilers under test were obtained within only few hours with no prior background on the compiler passes under tests. This tool facilitates efficient compiler fuzzing with reduced developer time requirements via the dynamic testcase creation capability provided by an LLM with RAG.

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
