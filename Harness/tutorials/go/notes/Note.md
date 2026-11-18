# 学习笔记：从 0 开始构建 Agent Harness

<!-- |   |   | -->
<!-- | - | - | -->

<!-- > 来源：腾讯学堂培养项目《从 0 开始构建 Agent Harness | 极客时间》（作者 Tony Bai）   -->
<!-- > 链接：<https://sdc.qq.com/s/Zkma1k?scheme_type=mooc\&mooc_course_id=uM2LYJ8G>   -->
<!-- > 说明：学堂接口只返回课程简介，未返回 24 讲正文。本笔记依据课程简介整理，标注"（补充）"的内容为个人工程经验补充，非课程原文。 -->

<!-- --- -->

## 一、什么是 Harness

**Harness 就是给大模型写的"微型操作系统"。** 模型只负责思考，上下文管理、工具调度、安全拦截、状态持久化都由 Harness 在模型外面完成。

| OS 概念 | Agent 对应    | Harness 要干的事      |
| ----- | ----------- | ----------------- |
| CPU   | 大模型         | 只负责推理和规划          |
| RAM   | 上下文窗口       | 内存回收（压缩、降级）       |
| 外设    | Shell、文件、网络 | 统一注册、调度、拦截        |
| 中断    | 人工审批、超时     | Human-in-the-loop |

---

## 二、为什么需要 Harness

| 现象                   | 根因           | Harness 解法               |
| -------------------- | ------------ | ------------------------ |
| 读 3000 行日志就 Token 超限 | Token溢出却无法精细化干预（**上下文失控 ContextBloat**） | 阶梯降级压缩（Compaction）       |
| 同一个错误命令重复跑 10 遍      | 提示词对长程任务彻底失效（**状态失控 DoomLoop**）       | 运行时 Reminders 打断         |
| 差点执行 `rm -rf ./`     | 缺乏底层的物理拦截防线（**边界失控 YOLODisaster**）      | Middleware 拦截 + 人工审批 |

课程暗线是"框架坍塌，Harness 崛起"：模型自己会规划和调工具后，LangChain、AutoGen 这类重框架反而成了黑盒，状态藏在内存里，开发者插不上手。“大道至简”的核心：极简工具法则 Minimal Toolset、状态外部化 Externalized State、YOLO哲学与防御纵深。Harness架构图：

![Harness 整体架构图](images/MainLoop.png)

---

## 三、知识梳理

### 1. 核心引擎（The Core Engine）

- Main Loop - ReAct (Reason + Act) 循环：思考（Reason / Thought） → 调用工具(Action) → 观察(Observe) → 再思考。参考论文：[ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/pdf/2210.03629)

![DAG](images/DAG.png)

- 引入 Thinking 慢思考机制，提升复杂任务规划成功率：Two-Stage ReAct两阶段
    - 慢思考：仅传context，输出纯文本的推理与规划（核心修改engine/loop.go）
    - 行动：传入context及tool schema，按照规划完成输出
    - 观察：返回结果
- 多模型适配层：接 Claude 和 OpenAI 兼容 API
![API](images/API.png)

### 2. 工具层(Action & Tools)

- Tool Registry 统一注册工具，核心职责：动态挂载（Register）、描述暴露（Expose Schema）、路由分发与执行（Dispatch & Execute）。构建动态 Registry & Tool接口：
    - 定义BaseTool接口，能接收一段原始的 JSON 字节数组
    - 实现路由和分发
    - 物理工具read_file，向大模型清晰地描述这个工具的用途和参数格式，实现长度截断保护
- 极简主义与 YOLO（You Only Live Once）模式。核心4个基础工具：
    - read
    - write：指定工作区，创建文件
    - edit：精准的局部代码替换（包含特殊转义符的多行正则表达式易翻车）
      - 最大幻觉：格式丢失
      - 降级策略：多级模糊匹配链（精确匹配>>换行符归一化匹配>>整体去空匹配>>逐行去缩进匹配）
    - bash：工作区约束、底线（时间预算、工作区目录、错误原样回传、长度截断保护）
- 用 Go 并发做并行工具执行（Go 语言基础与并发见：[Go 语言精讲教材](../Go语言精讲教材.md)）并发 Fork-Join：如何规避并发带来的数据竞争
    - 每个文件路径维护单独 `RWMutex`，“先获锁，再操作文件”
    - 先读后写/先写后读
    - 细节：并发安全陷阱、无锁设计、上下文顺序对齐

### 3. 上下文工程（Context Engineering）

- 系统提示词 Prompt 动态组装
![Prompt](images/prompt.png)
    - skill规范(渐进式暴露 Progressive Disclosure)
    ```text
    my-skill/
    ├── SKILL.md          # 必填：包含 YAML 元数据与 Markdown 格式的执行指令
    ├── scripts/          # 选填：技能专属的可执行脚本
    ├── references/       # 选填：参考文档
    └── assets/           # 选填：模板或静态资源
    ```
- 多端并发的Session（会话）物理隔离
- 超长文本阶梯降级压缩（Compaction）
    - Observation Masking 掩码 & Head-Tail Truncation 触发截断
        - System Prompt（直接保留）
        - 远期历史（直接替换）
        - Working Memory（掐头去尾）
- **记忆和待办外部化到文件系统**，不用内部状态机
    - 复杂任务 —> Plan Mode（计划+状态）文件系统记忆法（File-based Memory）
- 上下文感知的Error Recovery提示模板注入
    - 定义错误分类器与模板 Domain Error Codes
    - 将 recovery 机制缝合进main loop

### 4. 稳定性与多智能体(Safety & Coordination)

- Reminders 斩断死循环 Doom Loop/Exploration Spiral
    - 大模型行为陷阱：上下文内容分布偏移、近因偏差
    - system reminder：高优先级引导新的user message
- Middleware 拦截危险操作，高危动作走人工审批 Human-in-the-loop
    - Middleware / Hook 模式：统一拦截点、审批通道、Human-in-the-loop、放行或阻断
![Midddleware](images/Human-in-the-loop.png)
- Subagent 隔离复杂任务，避免污染主上下文
    - 主agent/子agent（普通工具）

### 5. 可观测与度量(Observability & Evaluation)

- Tracing 链路追踪
    - 模型适配器 Provider Adapter
    - CostTracker中间件：提取token、更新session、记录time、返回结果
    - Agent链路追踪：根 root、子 child、叶子 leaf，输出json记录执行链路
- 成本审计
    - Prompt Tokens
    - Completion Tokens
- 自动化 Benchmark，用数据衡量 evaluation 每次改动是否变好
    - 经典评测集：SWE-bench
    - 靶机->设定指令->客观断言->计算得分

### 6. 端到端实战(End-to-End Practice)

- 一个 CLI 工具
![agent-CLI](images/agent-CLI.png)
- 一个飞书群里的 AgentOps 运维自动化助手
![agent-feishu](images/agent-feishu.png)
---

## 四、五条核心设计原则

1. **不调包**：核心循环自己写，保证可控
2. **工具极简**：少而强
3. **状态外部化**：记忆、待办存文件系统，可审计、可恢复、可人工介入
4. **上下文当内存管**：必须有回收策略
5. **先度量再优化**：没有 Benchmark 就没有进步
![overview](images/overview.png)

<!-- ## 五、学习建议

- **优先级**：第 3 章（上下文）和第 4 章（稳定性）最值得精读，所有 Agent 项目都会遇到
- **学习方式**：跟着敲 go-tiny-claw。看懂 ReAct 循环 + Tool Registry，就掌握了骨架的大头
- **语言**：代码是 Go。如果主要用 Python / TF，读懂设计即可，不必强行学 Go
- **交付物**：go-tiny-claw 完整源码，含 ReAct 循环、多模型适配、上下文压缩、死循环检测、链路追踪
- （补充）若要做推荐分析自动化 Agent，如自动跑 AUC 报表、排查训练任务，第 3、4、5 章可直接借鉴 -->

---

## 五、常见问题

### A. 概念理解

**Q1.** 用 OS 类比解释：大模型、上下文窗口、本地操作、Harness 分别对应什么？Harness 为什么不负责"教模型怎么想"？

<details><summary>参考思路</summary>  
CPU / RAM / 外设 / OS 内核。Harness 的职责是资源调度和保护（内存回收、硬件调度、系统中断），推理能力来自模型本身。  
</details>

**Q2.** 为什么说"框架越重，失控越狠"？重框架和 Harness 的核心差别是什么？

<details><summary>参考思路</summary>  
重框架把状态藏在内存、塞大量工具描述，开发者无法观测和介入。Harness 强调自己掌握循环、状态外部化、工具极简，可控可观测。  
</details>

**Q3.** 三个典型翻车现象（Token 超限、重复命令死循环、危险命令）分别对应 Harness 的哪个机制？

<details><summary>参考思路</summary>  
Compaction 压缩；Reminders 打断；Middleware 拦截 + 人工审批。  
</details>

### B. 设计思考

**Q4.** ReAct 循环的终止条件应有哪些？只靠模型输出"完成"够吗？

<details><summary>参考思路（补充）</summary>  
不够。还需要最大轮数、Token 或成本预算、超时、死循环检测、人工中断，防止模型一直不收敛。  
</details>

**Q5.** 做上下文压缩时，哪些信息必须保留？哪些可以降级或丢弃？什么叫"阶梯降级"？

<details><summary>参考思路（补充）</summary>  
必须保留：任务目标、用户约束、关键决策、未完成待办。可降级：已读过的长日志和文件内容，先保留摘要，再保留引用，最后丢弃。阶梯降级指按"旧、大、低价值"的顺序逐级压缩，而不是一次性全截断。  
</details>

**Q6.** 为什么要把记忆和待办放到文件系统，而不是放在内存状态机里？列出至少 3 个好处。

<details><summary>参考思路</summary>  
可审计（人能直接看）、可恢复（进程崩溃或重启后可续跑）、可人工修改、可跨 Subagent 共享、不占上下文。  
</details>

**Q7.** 如何判定"死循环"？只看"相同命令重复 N 次"可靠吗？

<details><summary>参考思路（补充）</summary>  
不够可靠。更稳的做法是：相同命令 + 相同报错 + 环境状态无变化，连续多次才判定。判定后注入 Reminder 提示模型换策略，仍无效再升级为中断或人工介入。  
</details>

**Q8.** 哪些工具调用必须走人工审批？审批机制放在哪一层最合适，为什么？

<details><summary>参考思路（补充）</summary>  
删除、覆盖写、网络外发、生产环境操作、花费较大的调用。放在 Middleware 层，对所有工具统一生效，不依赖模型自觉，也不需要每个工具各写一遍。  
</details>

**Q9.** Edit 工具为什么需要"多级模糊匹配"？只做精确字符串匹配会出什么问题？

<details><summary>参考思路（补充）</summary>  
模型生成的 old_string 常有空白、缩进、换行的细微差异，精确匹配会频繁失败，导致重试和死循环。需要逐级放宽匹配（精确 → 忽略空白 → 行级模糊），同时保证匹配唯一，避免误改。  
</details>

**Q10.** Subagent 解决了什么问题？什么任务适合派给 Subagent？

<details><summary>参考思路</summary>  
隔离复杂任务，避免中间过程污染主上下文。适合搜索大量文件、跑长日志分析等"过程长、只需要结论"的任务。  
</details>

### C. 工程实践

**Q11.** 工具并行执行时，要注意哪些并发风险？

<details><summary>参考思路（补充）</summary>  
读操作可并行；写同一文件、有依赖顺序的命令必须串行。结果要按调用顺序回填给模型。  
</details>

**Q12.** 没有 Benchmark 时，怎么知道改了上下文压缩策略是变好还是变差？你会设计哪些指标？

<details><summary>参考思路（补充）</summary>  
任务成功率、平均轮数、Token 和成本、死循环触发率、人工介入次数。用固定任务集做回归，对比改动前后。  
</details>

**Q13.** Tracing 至少应该记录哪些字段，才能事后复盘一次 Agent 失败？

<details><summary>参考思路（补充）</summary>  
每步的模型输入输出摘要、工具名和参数、耗时、Token 用量、错误信息、触发的 Reminder 或拦截事件、会话 ID 和步骤 ID。  
</details>

### D. 迁移应用

**Q14.** 假设要做一个"自动排查训练任务 QPS 下降"的 Agent，请列出你会设计的工具集（不超过 5 个）、必须拦截的操作、需要外部化的状态。

<details><summary>参考思路（补充）</summary>  
工具：读日志、查指标、读配置、执行只读命令、写排查报告。拦截：重启或终止任务、改配置、删数据。外部化：排查假设清单、已验证结论、待办项。  
</details>

---

<!-- ## 七、学习打卡

- [ ] 通读课程简介，理解 Harness 定位
- [ ] 第 1 章：跑通 ReAct 循环
- [ ] 第 2 章：实现 Tool Registry 和 Edit 工具
- [ ] 第 3 章：实现上下文压缩（重点）
- [ ] 第 4 章：死循环检测 + 审批拦截（重点）
- [ ] 第 5 章：加 Tracing 和 Benchmark
- [ ] 第 6 章：端到端串讲
- [ ] 自测题 Q1–Q14 全部自答一遍 -->
