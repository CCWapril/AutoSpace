# go-tiny-claw

跟随《从 0 开始构建 Agent Harness》逐讲实现的最小 Agent 引擎，用 Go 手写，不依赖 LangChain 一类的重框架。

模型只负责推理；循环控制、工具调度、上下文组装由本项目在模型外面完成。

## 当前状态

项目仍在随课程推进中，**目前还不能编译通过**，在做飞书接入这一讲：

| 位置 | 问题 |
| --- | --- |
| `internal/feishu/bot.go` | 引用了 SDK 中不存在的 `larkim.ReceiveIdTypeChatId`，需对照所装版本（`oapi-sdk-go/v3 v3.13.0`）的常量名修正 |
| `cmd/claw/main.go` | 使用了 `http.HandleFunc` 但没有导入 `net/http`；导入的 `context` 没有被使用 |

下面的"运行"一节描述的是修好之后的目标行为，其中的步骤还没有经过完整验证。

## 架构

```text
飞书 Webhook ──► feishu.Bot ──► engine.AgentEngine ──► provider.LLMProvider ──► 大模型
                                     │   ▲
                                     ▼   │
                                  tools.Registry ──► read_file / write_file / edit_file / bash
```

| 模块 | 职责 |
| --- | --- |
| `engine` | 核心 ReAct 循环：思考 → 调用工具 → 观察 → 再思考；支持"慢思考"阶段；`Reporter` 接口把输出与引擎解耦 |
| `provider` | 大模型适配层，统一为 `LLMProvider` 接口；已有 OpenAI 兼容与 Claude 两种实现，均指向智谱 |
| `tools` | 工具注册表与四个内置工具 |
| `context` | 动态组装 System Prompt：内置核心纪律 + 工作区 `AGENTS.md` + `.claw/skills/*/SKILL.md` |
| `schema` | `Message`、`ToolCall`、`ToolResult`、`ToolDefinition` 等公共数据结构 |
| `feishu` | 飞书事件监听与消息回复 |

### 引擎的几个设计点

- **慢思考（Thinking）**：开启后，每轮先以"不挂载任何工具"的方式请求一次，迫使模型只输出纯文本的推理，再恢复工具让它行动。由 `NewAgentEngine` 的最后一个参数控制。
- **并行执行工具**：同一轮里模型返回的多个 tool call 用 goroutine 并行执行，结果按原调用顺序回填。串行版本作为注释保留在 `engine/loop.go` 中，便于对比。注意：有先后依赖的调用（如先建目录再写文件）并行后可能乱序。
- **动态提示词**：`PromptComposer` 每次从工作目录读取 `AGENTS.md` 与技能文件，规范放在文件里而不是写死在代码中。工作区示例见仓库的 [`Harness/agent/`](../agent/)。
- **工作目录**：三个文件类工具把相对路径拼在启动时的工作目录下，`bash` 以它作为当前目录。目前没有校验路径是否越出该目录（如 `../`），所以它只是默认根目录，还不是安全边界。

### 内置工具

| 工具 | 作用 | 备注 |
| --- | --- | --- |
| `read_file` | 读取文件 | |
| `write_file` | 创建或覆盖文件 | 需同时提供 `path` 与 `content` |
| `edit_file` | 局部字符串替换 | 要求 `old_text` 在文件中唯一，匹配逻辑在 `fuzzyReplace` |
| `bash` | 执行 shell 命令 | 单次 30 秒超时；目前没有危险命令拦截 |

### 已定义但尚未接入引擎的部分

- `engine/session.go`：带读写锁的会话历史，`AgentEngine` 目前还没有使用它。
- `engine/terminal_reporter.go`：命令行版本的 `Reporter`，预留给后续的 CLI。
- `internal/memory/`：空目录，预留给记忆外部化。

## 配置

全部通过环境变量提供，**不要写进代码或提交到仓库**（仓库已忽略 `.env`）。

| 变量 | 是否必需 | 说明 |
| --- | --- | --- |
| `ZHIPU_API_KEY` | 必需 | 智谱大模型 API Key，当前模型为 `glm-4.5-air` |
| `FEISHU_APP_ID` | 必需 | 飞书应用 App ID |
| `FEISHU_APP_SECRET` | 必需 | 飞书应用 App Secret |
| `FEISHU_ENCRYPT_KEY` | 可选 | 飞书事件加密密钥，开启事件加密时才需要 |
| `FEISHU_VERIFY_TOKEN` | 可选 | 飞书事件校验 Token |

## 运行

要求 Go 1.26.0 及以上（`go.mod` 声明；较低版本的 Go 会自动下载匹配的工具链，需要联网）。

```bash
export ZHIPU_API_KEY=你的key
export FEISHU_APP_ID=你的app_id
export FEISHU_APP_SECRET=你的app_secret

cd Harness/go-tiny-claw
go run ./cmd/claw
```

服务监听 `:48080`，事件回调路径为 `/webhook/event`。在飞书开放平台把"事件订阅"的请求地址配置为 `http://<你的公网地址>:48080/webhook/event`，并订阅"接收消息"事件。

## 目录结构

```text
go-tiny-claw/
├── cmd/claw/
│   └── main.go                  入口：组装引擎、注册工具、启动飞书 Webhook 服务
├── internal/
│   ├── context/
│   │   ├── composer.go          System Prompt 动态组装
│   │   └── skill.go             扫描并解析 .claw/skills 下的 SKILL.md
│   ├── engine/
│   │   ├── loop.go              ReAct 主循环
│   │   ├── reporter.go          Reporter 接口
│   │   ├── terminal_reporter.go 命令行 Reporter
│   │   └── session.go           会话历史（未接入）
│   ├── feishu/
│   │   └── bot.go               事件监听与消息回复
│   ├── memory/                  预留（空）
│   ├── provider/
│   │   ├── interface.go         LLMProvider 接口
│   │   ├── openai.go            OpenAI 兼容实现
│   │   └── claude.go            Claude 实现
│   ├── schema/
│   │   └── message.go           公共数据结构
│   └── tools/
│       ├── registry.go          注册表
│       ├── bash.go
│       ├── read_file.go
│       ├── write_file.go
│       └── edut_file.go         edit_file 工具（文件名中的 edut 为拼写笔误）
├── go.mod
└── go.sum
```

## 本讲目标结构（飞书接入）

以下是课程笔记中记录的本讲目标，保留作对照：

```text
go-tiny-claw/
├── cmd/
│   └── claw/
│       └── main.go          # 【重构】启动 HTTP Server 监听飞书 Webhook
├── internal/
│   ├── engine/
│   │   ├── loop.go          # 【重构】将 fmt.Println 替换为 Reporter 接口调用
│   │   ├── reporter.go      # 【新增】定义 Reporter 接口规范
│   │   └── terminal_reporter.go # (本讲暂时用不到，预留给后续的 CLI)
│   ├── feishu/              # 【新增】飞书集成层
│   │   └── bot.go           # 实现事件监听与飞书消息 API 的封装
│   ├── provider/            # 保持不变
│   ├── schema/              # 保持不变
│   └── tools/               # 保持不变
├── go.mod
└── go.sum
```
