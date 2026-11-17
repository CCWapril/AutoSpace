# Harness 学习目录

学习《从 0 开始构建 Agent Harness》（极客时间，Tony Bai）的笔记、配套语言教材与实战项目。

Harness 可以理解为给大模型写的"微型操作系统"：模型只负责推理，上下文管理、工具调度、安全拦截和状态持久化由 Harness 在模型之外完成。

## 目录结构

```text
Harness/
├── agent/                       go-tiny-claw 运行时读取的工作区配置
│   ├── AGENTS.md                项目专属规范，会被注入 System Prompt
│   └── .claw/skills/            技能外挂，每个技能一个 SKILL.md
├── go-tiny-claw/                Go 实现的最小 Agent 引擎
└── tutorials/
    ├── go/
    │   ├── Go语言精讲教材.md
    │   ├── notes/               课程学习笔记 Note.md 与配图
    │   └── practice/            本地练习（不上传）
    ├── python/
    │   ├── Python-Agent.md
    │   └── practice/            本地练习（不上传）
    └── typescript/
        ├── TypeScript教材.md
        └── practice/            本地练习（不上传）
```

## 内容索引

| 内容 | 说明 |
| --- | --- |
| [课程学习笔记](tutorials/go/notes/Note.md) | Harness 的定位、六块核心知识、五条设计原则，以及常见问题 |
| [Go 语言精讲教材](tutorials/go/Go语言精讲教材.md) | 从语法到并发、工程化、运行时原理、trpc-go，附两个综合实战（URL 检查器、工具调用 Agent） |
| [Python 精简教程](tutorials/python/Python-Agent.md) | 以搭建 Agent 为目的：联合类型、pydantic 校验、asyncio，并手写一个 Tool-calling Agent |
| [TypeScript 教材](tutorials/typescript/TypeScript教材.md) | 以搭建 Agent 为目的的 TypeScript 精简教程，8 章加附录，含完整 Agent 实战 |
| [go-tiny-claw](go-tiny-claw/README.md) | 跟随课程逐讲实现的最小 Agent 引擎：ReAct 循环、多模型适配、工具、动态提示词、飞书接入 |

## 建议的学习顺序

1. 读 [笔记](tutorials/go/notes/Note.md)，先建立整体概念：为什么需要 Harness、三类失控现象与对应机制。
2. 补语言基础：课程代码是 Go，读 [Go 教材](tutorials/go/Go语言精讲教材.md) 的并发与工程化两章即可；主要用 Python 的话，读 [Python 教程](tutorials/python/Python-Agent.md) 更直接。
3. 对照 [go-tiny-claw](go-tiny-claw/README.md) 的源码，理解 ReAct 循环、Tool Registry 与上下文组装。

## 说明

- 各教材下的 `practice/` 是本地练习区，已被 `.gitignore` 忽略，克隆仓库后不会看到。
- `agent/` 目录是 `go-tiny-claw` 的"被管理对象"：引擎以工作目录为边界，读取其中的 `AGENTS.md` 和 `.claw/skills/` 来组装系统提示词。
