# NecoFuzz: Effective Fuzzing of Nested Virtualization via Fuzz-Harness Virtual Machines

## 基本信息

- 作者：Reima Ishii、Takaaki Fukai、Takahiro Shinagawa
- 发表日期：2025-12-09
- 更新日期：2025-12-09
- 来源：arXiv
- 来源编号：2512.08858v1
- 研究类别：Tools and Benchmarks
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[http://arxiv.org/abs/2512.08858v1](http://arxiv.org/abs/2512.08858v1)
- PDF：[https://arxiv.org/pdf/2512.08858v1](https://arxiv.org/pdf/2512.08858v1)
- 分析模式：仅元数据分析

## 摘要

Nested virtualization is now widely supported by major cloud vendors, allowing users to leverage virtualization-based technologies in the cloud. However, supporting nested virtualization significantly increases host hypervisor complexity and introduces a new attack surface in cloud platforms. While many prior studies have explored hypervisor fuzzing, none has explicitly addressed nested virtualization due to the challenge of generating effective virtual machine (VM) instances with a vast state space as fuzzing inputs. We present NecoFuzz, the first fuzzing framework that systematically targets nested virtualization-specific logic in hypervisors. NecoFuzz synthesizes executable fuzz-harness VMs with internal states near the boundary between valid and invalid, guided by an approximate model of hardware-assisted virtualization specifications. Since vulnerabilities in nested virtualization often stem from incorrect handling of unexpected VM states, this specification-guided, boundary-oriented generation significantly improves coverage of security-critical code across different hypervisors. We implemented NecoFuzz on Intel VT-x and AMD-V by extending AFL++ to support fuzz-harness VMs. NecoFuzz achieved 84.7% and 74.2% code coverage for nested virtualization-specific code on Intel VT-x and AMD-V, respectively, and uncovered six previously unknown vulnerabilities across three hypervisors, including two assigned CVEs.

## 研究问题

Nested virtualization is now widely supported by major cloud vendors, allowing users to leverage virtualization-based technologies in the cloud. However, supporting nested virtualization significantly increases host hypervisor complexity and introduces a new attack surface in cloud platforms. While many prior studies have explored hypervisor fuzzing, none has explicitly addressed nested virtualization due to the challenge of generating effective virtual machine (VM) instances with a vast state space as fuzzing inputs. We present NecoFuzz, the first fuzzing framework that systematically targets nested virtualization-specific logic in hypervisors. NecoFuzz synthesizes executable fuzz-harness VMs with internal states near the boundary between valid and invalid, guided by an approximate model of hardware-assisted virtualization specifications. Since vulnerabilities in nested virtualization often stem from incorrect handling of unexpected VM states, this specification-guided, boundary-oriented generation significantly improves coverage of security-critical code across different hypervisors. We implemented NecoFuzz on Intel VT-x and AMD-V by extending AFL++ to support fuzz-harness VMs. NecoFuzz achieved 84.7% and 74.2% code coverage for nested virtualization-specific code on Intel VT-x and AMD-V, respectively, and uncovered six previously unknown vulnerabilities across three hypervisors, including two assigned CVEs.

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
