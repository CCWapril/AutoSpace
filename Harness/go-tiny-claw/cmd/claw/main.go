// cmd/claw/main.go
package main

import (
	"context"
	"flag"
	"fmt"
	"log"
	"os"

	"github.com/CCWapril/AutoSpace/Harness/go-tiny-claw/internal/engine"
	"github.com/CCWapril/AutoSpace/Harness/go-tiny-claw/internal/provider"
	"github.com/CCWapril/AutoSpace/Harness/go-tiny-claw/internal/schema"
	"github.com/CCWapril/AutoSpace/Harness/go-tiny-claw/internal/tools"
)

func main() {
	// 通过命令行参数接收用户prompt
	promptPtr := flag.String("prompt", "", "要交给agent执行任务描述")
	flag.Parse()

	if *promptPtr == "" {
		fmt.Println("用法: go run cmd/claw/main.go -prompt \"你的任务指令\"")
		os.Exit(1)
	}

	if os.Getenv("ZHIPU_API_KEY") == "" {
		log.Fatal("请先导出 ZHIPU_API_KEY 环境变量")
	}

	workDir, _ := os.Getwd()
	llmProvider := provider.NewZhipuOpenAIProvider("glm-4.5-air")

	// 注册工具
	registry := tools.NewRegistry()
	registry.Register(tools.NewReadFileTool(workDir))
	registry.Register(tools.NewWriteFileTool(workDir))
	registry.Register(tools.NewBashTool(workDir))
	registry.Register(tools.NewEditFileTool(workDir))

	// 实例化引擎 (关闭思考模式以提速,planmode开启)
	eng := engine.NewAgentEngine(llmProvider, registry, false, true)
	reporter := engine.NewTerminalReporter()

	// sessionID := "test_oom_protection_001"
	sessionID := "task_web_server_01"
	sess := engine.GlobalSessionMgr.GetOrCreate(sessionID, workDir)

	// 发起一个会导致读取大文件的恶意任务
	// prompt := `
	// 请帮我执行以下三个步骤：
	// 1. 使用 bash 执行 echo "开始排查日志"
	// 2. 使用 read_file 工具读取当前目录下的巨大文件 mock_log.txt
	// 3. 使用 bash 执行 date 命令获取当前时间，并告诉我任务全部完成。
	// `
	// 固定sessionID，重启后内存历史依然存在
	log.Printf("\n>>> 🚀 收到指令: %s\n", *promptPtr)

	sess.Append(schema.Message{Role: schema.RoleUser, Content: *promptPtr})

	err := eng.Run(context.Background(), sess, reporter)
	if err != nil {
		log.Fatalf("引擎运行崩溃: %v", err)
	}
}
