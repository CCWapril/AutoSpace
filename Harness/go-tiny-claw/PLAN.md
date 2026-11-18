# Go 极简 Web Server 项目

## 项目目标
搭建一个极简的 Go 语言 Web Server，提供基本的 HTTP 服务功能。

## 架构设计
- 项目结构：采用标准的 Go 项目布局
- 主程序：cmd/server/main.go
- 路由处理：极简的路由系统
- 中间件：支持基本的日志中间件

## 技术选型
- Go 1.20+
- 标准库 net/http
- 无额外依赖，保持极简

## 项目结构
```
cmd/
└── server/
    └── main.go
internal/
└── handlers/
    └── routes.go
go.mod
go.sum
README.md
```

## 核心功能
1. 基础 HTTP 服务器
2. 简单的路由系统
3. 日志中间件
4. 健康检查端点
5. 优雅关闭