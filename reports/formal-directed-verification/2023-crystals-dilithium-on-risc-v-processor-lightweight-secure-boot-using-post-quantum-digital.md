# CRYSTALS-Dilithium on RISC-V Processor: Lightweight Secure Boot Using Post-Quantum Digital Signature

## 基本信息

- 作者：Naina Gupta、A. Jati、Anupam Chattopadhyay
- 发表日期：2023-10-28
- 会议/期刊：2023 IEEE/ACM International Conference on Computer Aided Design (ICCAD)
- 主分类：形式化与定向处理器验证
- 相关性：A·直接相关（score=5）
- 证据等级：摘要级
- 全文状态：PDF待补
- 标签：Formal & Directed Processor Verification
- 纳入依据：hardware/processor object: risc-v, processor；verification/fuzzing method: verification；security relevance: security
- 论文页面：[https://doi.org/10.1109/ICCAD57390.2023.10323688](https://doi.org/10.1109/ICCAD57390.2023.10323688)
- PDF：未记录
- 分析模式：摘要级占位（未全文核验）

## 摘要

With the ongoing efforts for transitioning towards post-quantum security, NIST has recently selected the digital signature algorithm CRYSTALS-Dilithium for standardization. In this work, we demonstrate the first Dilithium based hardware accelerated secure boot architecture developed around Ariane, an open-source RISC- V core. By utilizing a compact design with novel verification engine, a secure boot flow is implemented with only 3.48ms runtime overhead compared to normal boot, while requiring 10.4K LUTs and 5.7K FFs on an FPGA. Compared to the state-of-the-art we achieve a reduction of 3.42× and 7.88 × for LUTs and FFs respectively. Also, the design when realized in 65nm ASIC requires only 125 kGE and 6.3 mW power at 100 MHz. Further, as secure boot is one of the critical processes and the security of the whole system depends on it, we implemented hardware fault countermeasures and evaluated their effectiveness in preventing secure boot bypass.

## 研究问题

摘要级初步判断（未核验正文）：With the ongoing efforts for transitioning towards post-quantum security, NIST has recently selected the digital signature algorithm CRYSTALS-Dilithium for standardization. In this work, we demonstrate the first Dilithium based hardware accelerated secure boot architecture developed around Ariane, an open-source RISC- V core. By utilizing a compact design with novel verification engine, a secure boot flow is implemented with only 3.48ms runtime overhead compared to normal boot, while requiring 10.4K LUTs and 5.7K FFs on an FPGA. Compared to the state-of-the-art we achieve a reduction of 3.42× and 7.88 × for LUTs and FFs respectively. Also, the design when realized in 65nm ASIC requires only 125 kGE and 6.3 mW power at 100 MHz. Further, as secure boot is one of the critical processes and the security of the whole system depends on it, we implemented hardware fault countermeasures and evaluated their effectiveness in preventing secure boot bypass.

## Introduction 梳理

尚未读取论文正文，不能可靠重建作者在 Introduction 中提出的研究缺口、威胁模型和贡献边界。

## 方法

尚未读取论文正文。请勿将检索关键词或摘要中的宣传性表述当作完整方法；后续需核对输入生成、反馈、Oracle、DUT、基线和实现细节。

## 实验与评估

尚未读取实验章节。当前不能确认实验平台、基线、公平预算、统计显著性、漏洞数量、运行开销或 Artifact 可复现性。

## 核心贡献

待全文核验；当前仅能确认论文题名为《CRYSTALS-Dilithium on RISC-V Processor: Lightweight Secure Boot Using Post-Quantum Digital Signature》，初步归入“Formal & Directed Processor Verification”。 原因：未找到可直接下载的 PDF；请在 config/pdf_overrides.json 中补充作者版或官方 PDF URL

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
