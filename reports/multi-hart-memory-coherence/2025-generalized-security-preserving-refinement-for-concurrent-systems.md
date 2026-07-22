# Generalized Security-Preserving Refinement for Concurrent Systems

## 基本信息

- 作者：Huan Sun、David Sanán、Jingyi Wang、Yongwang Zhao、Jun Sun、Wenhai Wang
- 发表日期：2025-11-10
- 会议/期刊：arXiv
- 主分类：多 Hart、内存一致性与缓存一致性
- 相关性：B·强邻近（score=5）
- 证据等级：全文核验
- 全文状态：已完成
- 标签：Multi-Hart, Memory Consistency & Cache Coherence
- 纳入依据：hardware/processor object: multicore；verification/fuzzing method: verification；security relevance: security
- 论文页面：[http://arxiv.org/abs/2511.06862v1](http://arxiv.org/abs/2511.06862v1)
- PDF：[https://arxiv.org/pdf/2511.06862v1](https://arxiv.org/pdf/2511.06862v1)
- 分析模式：DeepSeek 全文分析：deepseek-v4-flash；PDF 全文共 15 页，提取 91619 字符

## 摘要

Ensuring compliance with Information Flow Security (IFS) is known to be challenging, especially for concurrent systems with large codebases such as multicore operating system (OS) kernels. Refinement, which verifies that an implementation preserves certain properties of a more abstract specification, is promising for tackling such challenges. However, in terms of refinement-based verification of security properties, existing techniques are still restricted to sequential systems or lack the expressiveness needed to capture complex security policies for concurrent systems. In this work, we present a generalized security-preserving refinement technique, particularly for verifying the IFS of concurrent systems governed by potentially complex security policies. We formalize the IFS properties for concurrent systems and present a refinement-based compositional approach to prove that the generalized security properties (e.g., intransitive noninterference) are preserved between implementation and abstraction. The key intuition enabling such reasoning, compared to previous refinement work, is to establish a step-mapping relation between the implementation and the abstraction, which is sufficient to ensure that every paired step (in the abstraction and the implementation, respectively) is either permitted or prohibited by the security policy. We apply our approach to verify two non-trivial case studies against a collection of security policies. Our proofs are fully mechanized in Isabelle/HOL, during which we identified that two covert channels previously reported in the ARINC 653 single-core standard also exist in the ARINC 653 multicore standard. We subsequently proved the correctness of the revised mechanism, showcasing the effectiveness of our approach.

## 研究问题

并发系统在精化下信息流安全属性的保持问题，现有精化技术限于顺序系统或无法表达非传递安全策略，且并发场景下中间步骤可能被隐藏导致信息泄露。

## Introduction 梳理

现有精化技术多针对安全或活性属性，不保持安全属性；并发系统中中间执行可被其他组件观察到，而标准精化可能隐藏这些步骤；透明追踪精化限于隔离策略，不支持非传递非干涉。本文提出一种新的unwinding-preserving simulation，通过步骤映射和状态不变关系处理并发中间步骤，支持intransitive noninterference，并在ARINC 653多核IPC和密封投标拍卖两个案例中验证。

## 方法

输入生成：手动建模，非自动生成。反馈/coverage：无。Oracle：安全属性由unwinding conditions（Local Respect和Step Consistent）定义，通过Isabelle/HOL定理证明。DUT/平台：ARINC 653多核IPC机制和密封投标拍卖系统的形式化模型。golden model：抽象规范（抽象发送/接收函数）。核心方法：定义状态不变关系α和步骤映射函数ζ，证明实现模拟抽象并保持unwinding conditions；采用rely-guarantee分解实现组合验证。

## 实验与评估

baseline：未明确提到，但与标准精化技术比较了额外证明负担。实验预算：表1显示ARINC 653案例中实现代码260行、抽象140行、模拟关系57行、安全检查48行、模拟证明848行；拍卖案例分别为202、137、53、46、620行。统计：无。bug/CVE：发现ARINC 653多核标准中两个隐蔽通道（队列满状态和端口标识符泄露），并证明修订版本安全。开销：未说明具体时间，但声称扩展标准精化负担不大。Artifact：Isabelle/HOL源代码发布于https://github.com/IS2Lab/Refine_IFS。

## 核心贡献

(1) 一种新型模拟技术，保持并发系统下unwinding conditions，支持intransitive noninterference（含降级策略）；(2) 端到端安全证明，在Isabelle/HOL中完全形式化，应用于两个非平凡案例；(3) 发现并修复了ARINC 653多核标准中两个隐蔽通道。

## 与本仓库研究主线的关系

强邻近但不直接相关：该论文关注多核OS级并发系统的形式化信息安全验证，与存储库中“多hart与内存一致性验证”主题有概念关联，但并非针对硬件Fuzzing或RTL测试。方法中使用的精化和模拟思想可借鉴于硬件验证，但当前工作不涉及RISC-V或硬件覆盖。与多hart/一致性路径研究的关系：间接，提供的形式化精化框架可应用于验证多核系统中通道隔离，但非直接针对缓存一致性。

## 结论

提出了一个用于并发系统安全保持精化的框架，通过unwinding conditions和组合方法实现。在ARINC 653多核IPC和密封投标拍卖两个案例中成功验证，发现并修复隐藏通道。未来计划应用于其他多核OS（如CertiKOS with IPC）。

## 局限性

（论文第7.3节）不允许抽象层次的stuttering；不支持抽象中domain可见的非确定性（防止确定性不安全实现精化随机安全抽象）；不处理时间通道；依赖交互式定理证明。

## 详细阅读分析

建议深入阅读第4节（unwinding-preserving simulation定义）和第5节（ARINC 653案例的形式化细节），以理解状态不变关系和步骤映射函数的构建方式。对于关注硬件fuzzing的研究者，可了解其组合验证思路，但技术细节（事件语言、rely-guarantee）与硬件测试差异较大。

## 后续核验问题

- 该方法能否扩展到硬件描述语言（如Verilog）级别的信息安全属性验证？
- 如何自动生成步骤映射函数ζ和状态不变关系α？
- 该精化框架是否适用于RISC-V平台的安全关键系统？
- 能否将精化思想与硬件fuzzing结合，例如指导覆盖引导的测试生成？
