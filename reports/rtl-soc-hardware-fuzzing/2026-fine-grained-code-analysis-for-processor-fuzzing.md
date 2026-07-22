# Fine-Grained Code Analysis for Processor Fuzzing

## 基本信息

- 作者：Ziyue Zheng、Zhi Qu、Yangdi Lyu
- 发表日期：2026-04-20
- 会议/期刊：未记录
- 主分类：RTL 与 SoC 硬件 Fuzzing
- 相关性：A·直接相关（score=9）
- 证据等级：摘要级
- 标签：RTL & SoC Hardware Fuzzing、Coverage, Oracles & Fuzzing Methodology
- 纳入依据：strong phrase in title: processor fuzzing；hardware/processor object: processor, rtl；verification/fuzzing method: fuzz, test generation, verification
- 论文页面：[https://doi.org/10.23919/date69613.2026.11539325](https://doi.org/10.23919/date69613.2026.11539325)
- PDF：未记录
- 分析模式：摘要级占位（未全文核验）

## 摘要

The increasing complexity of modern processor designs has posed significant challenges in achieving comprehensive coverage metrics for functional verification of Register-Transfer Level (RTL) designs. Despite the availability of white-box RTL models, recent advancements in hardware fuzzing have predominantly focused on grey-box methodologies, which lack effective utilization of internal logic and structural information.This paper presents a novel approach that addresses this limitation by extracting control flow graphs (CFGs) from processor designs and analyzing the dependencies within these graphs. The analyzed CFGs serve as heuristic information to guide the generation of processor stimuli. By effectively leveraging internal logic information during the simulation of complex processors, this method provides interpretable heuristics for test generation. Experimental results demonstrate the effectiveness of utilizing control flow information derived from processor designs in enhancing the convergence speed of coverage metrics and guiding test sequences towards hard-to-reach states.

## 研究问题

摘要级初步判断（未核验正文）：The increasing complexity of modern processor designs has posed significant challenges in achieving comprehensive coverage metrics for functional verification of Register-Transfer Level (RTL) designs. Despite the availability of white-box RTL models, recent advancements in hardware fuzzing have predominantly focused on grey-box methodologies, which lack effective utilization of internal logic and structural information.This paper presents a novel approach that addresses this limitation by extracting control flow graphs (CFGs) from processor designs and analyzing the dependencies within these graphs. The analyzed CFGs serve as heuristic information to guide the generation of processor stimuli. By effectively leveraging internal logic information during the simulation of complex processors, this method provides interpretable heuristics for test generation. Experimental results demonstrate the effectiveness of utilizing control flow information derived from processor designs in enhancing the convergence speed of coverage metrics and guiding test sequences towards hard-to-reach states.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《Fine-Grained Code Analysis for Processor Fuzzing》，初步归入“RTL & SoC Hardware Fuzzing”。

## 与本仓库研究主线的关系

该条目已通过自动相关性筛选，但尚未完成人工或全文级核验。

## 结论

尚未核验正文，因此不对论文最终结论作确定性概括。

## 局限性

尚未核验正文。至少需要检查方法是否只适用于特定 ISA、处理器、协议、仿真器或人工模板，以及实验是否存在目标泄漏和基线不公平。

## 详细阅读分析

优先阅读 Introduction、Background/Threat Model、Method、Evaluation、Limitations/Discussion，并核对官方论文页、DOI、Artifact 和代码仓库。

## 后续核验问题

- 论文的在线反馈信号和最终 Oracle 分别是什么？
- 实验是否包含公平的 random、通用 RTL coverage 和领域专用 coverage 基线？
- 论文是否提供开源 Artifact、真实漏洞、CVE 或可复现 PoC？
