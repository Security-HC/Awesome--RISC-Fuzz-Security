# INSTILLER: Towards Efficient and Realistic RTL Fuzzing

## 基本信息

- 作者：Gen Zhang、Pengfei Wang、Tai Yue、Danjun Liu、Yubei Guo、Kai Lu
- 发表日期：2024-01-29
- 更新日期：2024-01-29
- 来源：arXiv
- 来源编号：2401.15967v1
- 研究类别：RTL and Hardware Verification、Fuzzing Methodology
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：2
- 论文页面：[http://arxiv.org/abs/2401.15967v1](http://arxiv.org/abs/2401.15967v1)
- PDF：[https://arxiv.org/pdf/2401.15967v1](https://arxiv.org/pdf/2401.15967v1)
- 分析模式：仅元数据分析

## 摘要

Bugs exist in hardware, such as CPU. Unlike software bugs, these hardware bugs need to be detected before deployment. Previous fuzzing work in CPU bug detection has several disadvantages, e.g., the length of RTL input instructions keeps growing, and longer inputs are ineffective for fuzzing. In this paper, we propose INSTILLER (Instruction Distiller), an RTL fuzzer based on ant colony optimization (ACO). First, to keep the input instruction length short and efficient in fuzzing, it distills input instructions with a variant of ACO (VACO). Next, related work cannot simulate realistic interruptions well in fuzzing, and INSTILLER solves the problem of inserting interruptions and exceptions in generating the inputs. Third, to further improve the fuzzing performance of INSTILLER, we propose hardware-based seed selection and mutation strategies. We implement a prototype and conduct extensive experiments against state-of-the-art fuzzing work in real-world target CPU cores. In experiments, INSTILLER has 29.4% more coverage than DiFuzzRTL. In addition, 17.0% more mismatches are detected by INSTILLER. With the VACO algorithm, INSTILLER generates 79.3% shorter input instructions than DiFuzzRTL, demonstrating its effectiveness in distilling the input instructions. In addition, the distillation leads to a 6.7% increase in execution speed on average.

## 研究问题

Bugs exist in hardware, such as CPU. Unlike software bugs, these hardware bugs need to be detected before deployment. Previous fuzzing work in CPU bug detection has several disadvantages, e.g., the length of RTL input instructions keeps growing, and longer inputs are ineffective for fuzzing. In this paper, we propose INSTILLER (Instruction Distiller), an RTL fuzzer based on ant colony optimization (ACO). First, to keep the input instruction length short and efficient in fuzzing, it distills input instructions with a variant of ACO (VACO). Next, related work cannot simulate realistic interruptions well in fuzzing, and INSTILLER solves the problem of inserting interruptions and exceptions in generating the inputs. Third, to further improve the fuzzing performance of INSTILLER, we propose hardware-based seed selection and mutation strategies. We implement a prototype and conduct extensive experiments against state-of-the-art fuzzing work in real-world target CPU cores. In experiments, INSTILLER has 29.4% more coverage than DiFuzzRTL. In addition, 17.0% more mismatches are detected by INSTILLER. With the VACO algorithm, INSTILLER generates 79.3% shorter input instructions than DiFuzzRTL, demonstrating its effectiveness in distilling the input instructions. In addition, the distillation leads to a 6.7% increase in execution speed on average.

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
