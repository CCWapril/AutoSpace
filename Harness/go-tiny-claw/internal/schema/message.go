package schema

import "encoding/json"

// Role 定义消息的角色，包括系统(System)、用户(User)、助手(Assistant)等。
type Role string

const (
    RoleSystem    Role = "system"    // 系统提示词：确立 Agent 的性格与红线
    RoleUser      Role = "user"      // 用户输入 / 工具执行的返回结果 (Observation)
    RoleAssistant Role = "assistant" // 模型的输出：包含推理(Reasoning)或工具调用(ToolCall)
)

// Message 定义了一个消息结构体，包含角色、内容和可选的名称。
type Message struct {
    Role    Role   `json:"role"`
    Content string `json:"content"` // 放纯文本内容
    
	// 如果模型决定调用工具，此字段将被填充（支持并行调用多个工具）
	ToolCalls []ToolCall `json:"tool_calls,omitempty"`

	// 如果这是对某个工具调用的响应，此字段必须填写，以告知模型上下文的关联性
	ToolCallID string `json:"tool_call_id,omitempty"`
}
