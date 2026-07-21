# Uncovering New Classes of Kernel Vulnerabilities

## 基本信息

- 作者：Jakob Koschel
- 发表日期：
- 更新日期：
- 来源：Semantic Scholar
- 来源编号：5bda7998ca60b8ed1e61fb1862f9009c64546002
- 研究类别：微架构安全
- 首次发现：2026-07-21
- 最近更新：2026-07-21
- 命中次数：1
- 论文页面：[https://doi.org/10.5463/thesis.833](https://doi.org/10.5463/thesis.833)
- PDF：[https://research.vu.nl/files/380101013/thesis%20-%20674c5b8426eb2.pdf](https://research.vu.nl/files/380101013/thesis%20-%20674c5b8426eb2.pdf)
- 分析模式：仅元数据分析

## 摘要

Modern operating systems evolved into massively complex pieces of software with tens of millions lines of code. It is inevitable to have bugs in such large code bases, many of them with serious security implications. For decades, the kernel of such operating systems has been an interesting target for attackers due to its elevated privileges. Initially, attacks primarily targeted traditional software vulnerabilities like memory corruption. However, recent academic research has increasingly highlighted side-channel and transient execution vulnerabilities as well. While kernels have mitigations deployed against the most common vulnerability classes, many are too expensive for production systems. Instead, they are often used during continuous fuzzing efforts to find bugs. In recent years the amount of bugs discovered increased steadily with the improvements in bug detection during fuzzing, indicating that we are still scratching the surface and far from bug-free kernels. Additionally, state-of-the-art kernel fuzzers only focus on well-known bug classes and still find too many bugs to fix, urging the need to improve the security of our kernels. In this thesis, we uncover new classes of kernel vulnerabilities. Within the category of side-channel vulnerabilities, we demonstrate a novel way to combine multiple side channels to overcome limitations when attacking the kernel. With our attack we demonstrate that the very same feature that makes mitigation of side channels efficient, opens up a new attack surface. For transient execution vulnerabilities, we demonstrated the first gadget scanner based on dynamic analysis for the kernel. Detecting such gadgets is often difficult without suffering from large amounts of false positives, we showed that we can yield more precise detection by facilitating dynamic taint tracking. We implemented our scanner as a sanitizer to expose transient execution to traditional fuzzing environments to rely on existing bug detection capabilities. For software vulnerabilities, we find previously undiscovered type confusion bugs which we call container confusion bugs. Such bugs can be found in many large C code bases, such as kernels, that use nested structures to implement object-orientated functionality. We designed a specialized sanitizer to detect such bug patterns with continuous fuzzing and designed static analyzers to expand our search to sections of the kernel that are difficult to reach during fuzzing. In conclusion, we demonstrate that it is not enough to focus on currently well-established bug types and need to continue looking for new classes of vulnerabilities. We explored such new classes and improved fuzzing in all the main categories: software vulnerabilities, side channels, and transient execution attacks. Only by exploring such new exploitation angles and including them in our bug detection capabilities, we can slowly turn our kernels into a safe foundation of modern computing.

## 研究问题

Modern operating systems evolved into massively complex pieces of software with tens of millions lines of code. It is inevitable to have bugs in such large code bases, many of them with serious security implications. For decades, the kernel of such operating systems has been an interesting target for attackers due to its elevated privileges. Initially, attacks primarily targeted traditional software vulnerabilities like memory corruption. However, recent academic research has increasingly highlighted side-channel and transient execution vulnerabilities as well. While kernels have mitigations deployed against the most common vulnerability classes, many are too expensive for production systems. Instead, they are often used during continuous fuzzing efforts to find bugs. In recent years the amount of bugs discovered increased steadily with the improvements in bug detection during fuzzing, indicating that we are still scratching the surface and far from bug-free kernels. Additionally, state-of-the-art kernel fuzzers only focus on well-known bug classes and still find too many bugs to fix, urging the need to improve the security of our kernels. In this thesis, we uncover new classes of kernel vulnerabilities. Within the category of side-channel vulnerabilities, we demonstrate a novel way to combine multiple side channels to overcome limitations when attacking the kernel. With our attack we demonstrate that the very same feature that makes mitigation of side channels efficient, opens up a new attack surface. For transient execution vulnerabilities, we demonstrated the first gadget scanner based on dynamic analysis for the kernel. Detecting such gadgets is often difficult without suffering from large amounts of false positives, we showed that we can yield more precise detection by facilitating dynamic taint tracking. We implemented our scanner as a sanitizer to expose transient execution to traditional fuzzing environments to rely on existing bug detection capabilities. For software vulnerabilities, we find previously undiscovered type confusion bugs which we call container confusion bugs. Such bugs can be found in many large C code bases, such as kernels, that use nested structures to implement object-orientated functionality. We designed a specialized sanitizer to detect such bug patterns with continuous fuzzing and designed static analyzers to expand our search to sections of the kernel that are difficult to reach during fuzzing. In conclusion, we demonstrate that it is not enough to focus on currently well-established bug types and need to continue looking for new classes of vulnerabilities. We explored such new classes and improved fuzzing in all the main categories: software vulnerabilities, side channels, and transient execution attacks. Only by exploring such new exploitation angles and including them in our bug detection capabilities, we can slowly turn our kernels into a safe foundation of modern computing.

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
