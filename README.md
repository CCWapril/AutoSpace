# AutoSpace

个人学习与实践工作区，目前围绕两件事：

- **[Harness](Harness/)**：学习《从 0 开始构建 Agent Harness》，包含课程笔记、Go / Python / TypeScript 教材，以及手写的最小 Agent 引擎 `go-tiny-claw`。
- **[idea](idea/idea.md)**：待做项目的构想，目前记录了两个：实时量化交易助手、智能音乐创作助手。

## 目录结构

```text
AutoSpace/
├── Harness/                 Agent Harness 学习目录（详见 Harness/README.md）
│   ├── agent/               go-tiny-claw 运行时读取的工作区配置（AGENTS.md、skills）
│   ├── go-tiny-claw/        Go 实现的最小 Agent 引擎
│   └── tutorials/           笔记与语言教材（go / python / typescript）
├── idea/
│   └── idea.md              项目构想
├── .gitignore
└── README.md
```

## 从哪里开始

| 想做什么 | 看这里 |
| --- | --- |
| 理解 Harness 是什么、为什么需要它 | [课程学习笔记](Harness/tutorials/go/notes/Note.md) |
| 补 Go 语言基础与并发 | [Go 语言精讲教材](Harness/tutorials/go/Go语言精讲教材.md) |
| 用 Python 写 Tool-calling Agent | [Python 精简教程](Harness/tutorials/python/Python-Agent.md) |
| 对照 TypeScript 的写法 | [TypeScript 教材](Harness/tutorials/typescript/TypeScript教材.md) |
| 看手写引擎的实现与进度 | [go-tiny-claw](Harness/go-tiny-claw/README.md) |

建议顺序：先读笔记建立整体概念，再按需补语言教材，最后对照 `go-tiny-claw` 的代码。

## 环境要求

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| Go | 1.26.0 及以上 | `go-tiny-claw/go.mod` 声明的版本；Go 1.21 起会自动下载匹配的工具链 |
| Python | 3.11 及以上 | 仅 Python 教程的示例需要（用到 `assert_never`、`match` 等特性） |

运行 `go-tiny-claw` 还需要大模型与飞书的凭据，见 [go-tiny-claw/README.md](Harness/go-tiny-claw/README.md)。

## 仓库约定

- **密钥不入库**：`.env` 已在 `.gitignore` 中，API Key 等一律通过环境变量或 `.env` 提供，不要写进代码或文档。
- **练习代码不上传**：各教材下的 `practice/` 目录是本地练习区，已被 `.gitignore` 忽略。
- **本地草稿**：`go-tiny-claw` 里的 `loop_test.go`、`cmd/claw/_main.go` 也被忽略，仅在本地使用。
- **IDE 配置不入库**：`.idea/`、`.vscode/`、`*.iml` 等编辑器配置已被 `.gitignore` 忽略，各自本地维护。

## 说明

仓库的早期提交里包含 `quant_trading/`、`music_creation/` 两个 Streamlit 应用原型（对应 `idea/idea.md` 中的两个构想），它们已不在当前工作区，需要时可从 git 历史中找回（首个提交 `32ac75a`）。
