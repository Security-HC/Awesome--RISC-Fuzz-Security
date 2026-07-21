# ProcessorFuzz: Processor Fuzzing with Control and Status Registers Guidance

## 基本信息

- 作者：Sadullah Canakci、Chathura Rajapaksha、Leila Delshadtehrani、Anoop Mysore Nataraja、Michael B. Taylor、Manuel Egele、Ajay Joshi
- 发表日期：2023-05-01
- 更新日期：
- 来源：Semantic Scholar
- 来源编号：7113419eb7b0069db4d3eec2ff9e47e72a8aaa50
- 研究类别：RISC-V Fuzzing 研究、处理器与 CPU Fuzzing、RTL 与硬件验证
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[https://doi.org/10.1109/HOST55118.2023.10133714](https://doi.org/10.1109/HOST55118.2023.10133714)
- PDF：[]()
- 分析模式：仅元数据分析

## 摘要

As the complexity of modern processors has increased over the years, developing effective verification strategies to identify bugs prior to manufacturing has become critical. Inspired by software fuzzing, a technique commonly used for software testing, multiple recent works use hardware fuzzing for the verification of Register-Transfer Level (RTL) designs. However, these works suffer from several limitations such as lack of support for widelyused Hardware Description Languages (HDLs) and misleading coverage-signals that misidentify ‘‘interesting’’ inputs. Towards overcoming these shortcomings, we present ProcessorFuzz, a processor fuzzer that guides the fuzzer with a novel CSR-transition coverage metric. ProcessorFuzz monitors the transitions in Control and Status Registers (CSRs) as CSRs are in charge of controlling and holding the state of the processor. Therefore, transitions in CSRs indicate a new processor state, and guiding the fuzzer based on this feedback enables ProcessorFuzz to explore new processor states. We evaluated ProcessorFuzz with three real-world opensource processors — Rocket, BOOM, and BlackParrot. ProcessorFuzz triggered a set of ground-truth bugs $1.23 \times$ faster (on average) than DIFUZZRTL. Moreover, our experiments exposed 8 new bugs across the three RISC-V cores and one new bug in a reference model. All nine bugs were confirmed by the developers of the corresponding projects.

## 研究问题

As the complexity of modern processors has increased over the years, developing effective verification strategies to identify bugs prior to manufacturing has become critical. Inspired by software fuzzing, a technique commonly used for software testing, multiple recent works use hardware fuzzing for the verification of Register-Transfer Level (RTL) designs. However, these works suffer from several limitations such as lack of support for widelyused Hardware Description Languages (HDLs) and misleading coverage-signals that misidentify ‘‘interesting’’ inputs. Towards overcoming these shortcomings, we present ProcessorFuzz, a processor fuzzer that guides the fuzzer with a novel CSR-transition coverage metric. ProcessorFuzz monitors the transitions in Control and Status Registers (CSRs) as CSRs are in charge of controlling and holding the state of the processor. Therefore, transitions in CSRs indicate a new processor state, and guiding the fuzzer based on this feedback enables ProcessorFuzz to explore new processor states. We evaluated ProcessorFuzz with three real-world opensource processors — Rocket, BOOM, and BlackParrot. ProcessorFuzz triggered a set of ground-truth bugs $1.23 \times$ faster (on average) than DIFUZZRTL. Moreover, our experiments exposed 8 new bugs across the three RISC-V cores and one new bug in a reference model. All nine bugs were confirmed by the developers of the corresponding projects.

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
