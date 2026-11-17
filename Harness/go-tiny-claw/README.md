go-tiny-claw/
├── cmd/
│   └── claw/
│       └── main.go          # 测试入口：将挂载 Mock 组件运行 Main Loop
├── internal/
│   ├── engine/              # 【核心引擎层】
│   │   └── loop.go          # 本讲核心：Main Loop 逻辑
│   ├── provider/            # 【模型适配层】
│   │   └── interface.go     # LLM Provider 接口定义
│   ├── schema/              # 【公共数据结构】
│   │   └── message.go       # 统一的消息与工具调用类型定义
│   └── tools/               # 【工具与执行层】
│       └── registry.go      # 工具注册与分发接口
├── go.mod
└── README.md
