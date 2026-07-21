# SyzSpec: Specification Generation for Linux Kernel Fuzzing via Under-Constrained Symbolic Execution

## 基本信息

- 作者：Yu Hao、Juefei Pu、Xingyu Li、Zhiyun Qian、A. A. Sani
- 发表日期：2025-11-19
- 更新日期：
- 来源：Semantic Scholar
- 来源编号：2c0b7c7a1796e7753192caa2f447679296792186
- 研究类别：微架构安全、Fuzzing 方法论、工具与基准测试
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[https://doi.org/10.1145/3719027.3744811](https://doi.org/10.1145/3719027.3744811)
- PDF：[https://doi.org/10.1145/3719027.3744811](https://doi.org/10.1145/3719027.3744811)
- 分析模式：仅元数据分析

## 摘要

Fuzzing has become one of the most effective and widely used techniques for discovering bugs and vulnerabilities, particularly in large-scale and complex programs like operating system kernels. A notable example is the kernel fuzzer syzkaller, which has identified over 6,800 bugs in the Linux kernel, with more than 5,500 already fixed. A crucial reason behind the success of the syzkaller is its collection of syscall descriptions, which are typically provided by human experts. Although some methods exist for automatically generating these syscall descriptions for device drivers, they often fall short when dealing with complex user inputs. These existing methods either lack precision or have a limited analysis scope, resulting in incomplete syscall descriptions. In this paper, we present SyzSpec, a tool designed to address these limitations by performing fully inter- procedural under- constrained symbolic execution on syscall handler functions. This approach enables SyzSpec to explore all possible user inputs and generate syscall descriptions with more precision. The primary innovation in SyzSpec is a novel method to improve symbolic pointer reasoning in under-constrained symbolic execution, working along with the under-under-constrained memory object (UCMO). We compared SyzSpec with existing automated solutions and manually written syscall descriptions from syzkaller. Our results demonstrate that SyzSpec achieves better coverage than other automated tools and offers coverage comparable to that of manually written syscall descriptions. Additionally, we evaluated SyzSpec on the latest stable version of the Linux kernel (v6.10) and identified 86 unique and previously unknown crashes across 11 different categories.

## 研究问题

Fuzzing has become one of the most effective and widely used techniques for discovering bugs and vulnerabilities, particularly in large-scale and complex programs like operating system kernels. A notable example is the kernel fuzzer syzkaller, which has identified over 6,800 bugs in the Linux kernel, with more than 5,500 already fixed. A crucial reason behind the success of the syzkaller is its collection of syscall descriptions, which are typically provided by human experts. Although some methods exist for automatically generating these syscall descriptions for device drivers, they often fall short when dealing with complex user inputs. These existing methods either lack precision or have a limited analysis scope, resulting in incomplete syscall descriptions. In this paper, we present SyzSpec, a tool designed to address these limitations by performing fully inter- procedural under- constrained symbolic execution on syscall handler functions. This approach enables SyzSpec to explore all possible user inputs and generate syscall descriptions with more precision. The primary innovation in SyzSpec is a novel method to improve symbolic pointer reasoning in under-constrained symbolic execution, working along with the under-under-constrained memory object (UCMO). We compared SyzSpec with existing automated solutions and manually written syscall descriptions from syzkaller. Our results demonstrate that SyzSpec achieves better coverage than other automated tools and offers coverage comparable to that of manually written syscall descriptions. Additionally, we evaluated SyzSpec on the latest stable version of the Linux kernel (v6.10) and identified 86 unique and previously unknown crashes across 11 different categories.

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
