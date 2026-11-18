package engine

import (
	"context"
	"fmt"
	"log"
	"sync"

	ctxpkg "github.com/CCWapril/AutoSpace/Harness/go-tiny-claw/internal/context"
	"github.com/CCWapril/AutoSpace/Harness/go-tiny-claw/internal/provider"
	"github.com/CCWapril/AutoSpace/Harness/go-tiny-claw/internal/schema"
	"github.com/CCWapril/AutoSpace/Harness/go-tiny-claw/internal/tools"
)

// AgentEngine 是微型 OS 的核心驱动
type AgentEngine struct {
	provider provider.LLMProvider
	registry tools.Registry
	// WorkDir (工作区): 借鉴 OpenClaw 的理念，Agent 必须有一个明确的物理边界
	// WorkDir        string // session自带
	EnableThinking bool                   // 【新增】慢思考模式开关
	PlanMode       bool                   // 【新增】计划模式开关
	composer       *ctxpkg.PromptComposer // 【新增】引擎持有 Composer 实例
	compactor      *ctxpkg.Compactor      // 【新增】压缩器实例
}

func NewAgentEngine(p provider.LLMProvider, r tools.Registry, EnableThinking bool, PlanMode bool) *AgentEngine {
	return &AgentEngine{
		provider: p,
		registry: r,
		// WorkDir:        workDir,
		EnableThinking: EnableThinking,
		PlanMode:       PlanMode,
		// composer:       ctxpkg.NewPromptComposer("."), // 初始化组装器
		// 【初始化压缩器】：为了便于今天的极端测试，我们将水位线阈值设积极（例如 3000 字符），
		// 并保护最近的 6 条消息（大约两轮 Turn 的交互）
		compactor: ctxpkg.NewCompactor(3000, 6),
	}
}

// Run 方法新增了 Reporter 参数
func (e *AgentEngine) Run(ctx context.Context, session *Session, reporter Reporter) error {
	// log.Printf("[Engine] 引擎启动，锁定工作区: %s\n", e.WorkDir)
	log.Printf("[Engine] 唤醒会话 [%s]，锁定工作区: %s\n", session.ID, session.WorkDir, e.PlanMode)

	// 添加planmode
	e.composer = ctxpkg.NewPromptComposer(session.WorkDir, e.PlanMode)
	// 【核心修改】动态组装 System Prompt，彻底替换掉以前硬编码的面条提示词！
	systemMsg := e.composer.Build()

	// contextHistory := []schema.Message{
	// 	// {Role: schema.RoleSystem, Content: "You are go-tiny-claw, an expert coding assistant."},
	// 	systemMsg, // 注入动态组装的内核、AGENTS.md 与 Skills
	// 	{Role: schema.RoleUser, Content: userPrompt},
	// }

	for {
		availableTools := e.registry.GetAvailableTools()

		// 1. 从 Session 提取出近期的 Working Memory (例如最近 20 条，给压缩器留下充足的判断空间)
		workingMemory := session.GetWorkingMemory(20)

		var contextHistory []schema.Message
		contextHistory = append(contextHistory, systemMsg)
		contextHistory = append(contextHistory, workingMemory...)

		// 2. 【核心注入点】: 在向 Provider 发起推理前，过一遍内存压缩器！
		// 无论你带出了多少上下文，如果字符总数超标，早期日志将被掩码化，超大日志将被掐头去尾
		compactedContext := e.compactor.Compact(contextHistory)

		// 3. 后续的 Provider.Generate 全面使用被保护过的新鲜上下文 (compactedContext)
		// ================= Phase 1: Thinking =================
		if e.EnableThinking {
			if reporter != nil {
				reporter.OnThinking(ctx)
			}
			thinkResp, err := e.provider.Generate(ctx, compactedContext, nil)
			if err != nil {
				return fmt.Errorf("Thinking 阶段失败: %w", err)
			}
			if thinkResp.Content != "" {
				// 将思考过程持久化到 Session 中！
				session.Append(*thinkResp)
				// 把它追加到当前这一轮的临时上下文中，供 Action 阶段使用
				compactedContext = append(compactedContext, *thinkResp)
			}
		}

		// 3. ================= Phase 2: Action =================
		actionResp, err := e.provider.Generate(ctx, compactedContext, availableTools)
		if err != nil {
			return fmt.Errorf("Action 阶段失败: %w", err)
		}

		// 将大模型的行动响应持久化到 Session 中
		// 【驾驭精髓】：注意，写入 Session（硬盘/全量内存）的永远是全量的真实响应，不受 Compact 影响！
		// Compact 只作用于本轮发给大模型的那个临时 Context。
		session.Append(*actionResp)
		compactedContext = append(compactedContext, *actionResp)

		if actionResp.Content != "" && reporter != nil {
			reporter.OnMessage(ctx, actionResp.Content)
		}

		if len(actionResp.ToolCalls) == 0 {
			// 如果没有工具调用，说明本次任务已完成，打破 ReAct 循环，挂起等待人类的下一条指令
			break
		}

		// 4. ================= 并发执行底层工具 =================
		observationMsgs := make([]schema.Message, len(actionResp.ToolCalls))
		var wg sync.WaitGroup

		for i, toolCall := range actionResp.ToolCalls {
			wg.Add(1)

			go func(idx int, call schema.ToolCall) {
				defer wg.Done()

				if reporter != nil {
					reporter.OnToolCall(ctx, call.Name, string(call.Arguments))
				}

				result := e.registry.Execute(ctx, call)

				if reporter != nil {
					displayOutput := result.Output
					if len(displayOutput) > 200 {
						displayOutput = displayOutput[:200] + "... (已截断)"
					}
					reporter.OnToolResult(ctx, call.Name, displayOutput, result.IsError)
				}

				observationMsgs[idx] = schema.Message{
					Role:       schema.RoleUser,
					Content:    result.Output,
					ToolCallID: call.ID,
				}
			}(i, toolCall)
		}

		wg.Wait()

		// 将所有的工具执行结果（Observation）持久化到 Session 中，开启下一轮的复盘与推理
		session.Append(observationMsgs...)
	}

	return nil
}
