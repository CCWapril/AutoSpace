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