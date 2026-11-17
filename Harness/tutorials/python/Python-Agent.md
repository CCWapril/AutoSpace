# Python 精简教程：以搭建 Agent 为目的

<!-- > 共两章：**第 1 章**讲 Python 在 Agent 里的核心（背景、联合类型、pydantic、asyncio），**第 2 章**手写完整的 Tool-calling Agent。第 1 章的代码块和第 2 章的完整实现都已运行并通过 `mypy --strict`，第 2 章含 8 个 pytest 用例。 -->

## 总目录

- [**第 1 章 Python 在 Agent 里的核心**](#ch1)
  - [1.1 背景：为什么 Agent 主力是 Python](#ch1-s01)
  - [1.2 Python 的四个短板，和对策](#ch1-s02)
  - [1.3 三个习惯在 Agent 里怎么配合](#ch1-s03)
  - [1.4 习惯 1：用联合类型建模「多种形态」](#ch1-s04)
  - [1.5 习惯 2：pydantic 在边界校验](#ch1-s05)
  - [1.6 习惯 3：asyncio 的三件事](#ch1-s06)
  - [1.7 串起来：约 80 行的迷你 Agent](#ch1-s07)
  - [1.8 环境与检查](#ch1-s08)
  - [1.9 TS ↔ Python 速查](#ch1-s09)
  - [小结](#ch1-s10)
  - [练习](#ch1-s11)
- [**第 2 章 实战：从零写一个 Tool-calling Agent**](#ch2)
  - [2.1 本章地图与 TS 概念对照](#ch2-s01)
  - [2.2 Agent 的本质：一个循环](#ch2-s02)
  - [2.3 数据模型](#ch2-s03)
  - [2.4 工具：一个 pydantic 模型，三种用途](#ch2-s04)
  - [2.5 安全地执行工具](#ch2-s05)
  - [2.6 主循环](#ch2-s06)
    - [2.6.1 取消与超时：不用 signal](#ch2-s07)
    - [2.6.2 设计细节](#ch2-s08)
  - [2.7 用假模型跑起来](#ch2-s09)
  - [2.8 测试](#ch2-s10)
  - [2.9 接入真实模型](#ch2-s11)
    - [2.9.1 不联网验证](#ch2-s12)
  - [2.10 事件流式输出](#ch2-s13)
  - [2.11 护栏清单](#ch2-s14)
  - [2.12 类型检查与框架](#ch2-s15)
  - [小结](#ch2-s16)
  - [练习](#ch2-s17)

---

<a id="ch1"></a>

# 第 1 章 Python 在 Agent 里的核心

<!-- > **本章定位**：你已经会 Python，这里只补写 Agent 真正绕不开的三件事，其余语法不重复。  
> **阅读时间**：约 15 分钟，所有代码都能直接复制运行。  
> **学完你能**：说清 Python 在 Agent 技术栈里的位置；用联合类型建模模型响应；用 pydantic 挡住脏数据；用 asyncio 并行执行工具并正确处理超时取消；读懂第 2 章的完整实现。 -->

<a id="ch1-s01"></a>

## 1.1 背景：为什么 Agent 主力是 Python

一个典型 Agent 系统从上到下大致分五层，Python 主要占中间"编排"这一层，也是本教程的主角：

```text
产品壳    Web / CLI / IDE 插件           TypeScript 为主，Rust 在上升
网关      鉴权、限流、长连接              Go / Rust
编排 ★    循环、工具、上下文、护栏         Python        <-- 本教程
工具      MCP Server、业务 API           Python / TS / Go 混用
模型      推理服务、推理引擎              Python 调用，C++ / CUDA 实现
```

Python 占优的三个原因：

1. **生态先发**：模型 SDK、向量库、评测框架、数据管线都先出 Python 版，OpenAI Agents SDK、Claude Agent SDK、LangGraph、AutoGen、pydantic-ai、smolagents 等 Agent 框架自然长在上面。做推荐和机器学习的人，手边的数据、指标、实验代码也都是 Python。
2. **瓶颈不在语言**：一次模型调用要几百毫秒到几秒，工具调用也在等 IO。解释器那点开销淹没在等待里，换成 Go 不会让 Agent 变快。
3. **协议与语言无关**：MCP、A2A 都是 JSON-RPC / HTTP。Python 写的 Agent 可以调用任何语言写的工具，也可以被任何语言写的界面消费。

什么时候**不该**用 Python：

| 场景               | 更合适的选择      | 原因                                 |
| ------------------ | ----------------- | ------------------------------------ |
| 浏览器里的聊天界面 | TypeScript        | 前端只能是 JS / TS                   |
| 超高并发的接入网关 | Go / Rust         | 长连接和鉴权与"智能"无关，要的是吞吐 |
| 单二进制分发的 CLI | Rust / TypeScript | 免去用户装 Python 环境               |

<a id="ch1-s02"></a>

## 1.2 Python 的四个短板，和对策

| 短板                     | 对 Agent 的实际影响                                          | 对策                             |
| ------------------------ | ------------------------------------------------------------ | -------------------------------- |
| 类型标注**运行时不检查** | 模型输出、HTTP 响应里的脏数据不会自动报错                    | pydantic 在边界校验              |
| 并发模型有认知成本       | 忘了 `await`、不小心吞掉取消                                 | 只用 asyncio 一套                |
| 同步阻塞会卡住事件循环   | 在 `async def` 里调 `requests` 或 `time.sleep`，所有并行失效 | 用异步库，或 `asyncio.to_thread` |
| 类型检查是可选的         | 不跑 mypy，标注就等于注释                                    | `mypy --strict` 进 CI            |

所以写 Python Agent，难点不是语法，而是三个工程习惯：**类型建模、边界校验、asyncio**。

<a id="ch1-s03"></a>

## 1.3 三个习惯在 Agent 里怎么配合

下图是一次工具调用里数据的流向，后面三节分别对应图中的三个环节：

```text
模型输出（不可信的字符串 / JSON）
    │   [习惯 2] pydantic 校验，失败就变成错误文本          <-- 1.5
    ▼
类型化的内部数据（dataclass + 联合类型），mypy 守护           <-- 1.4
    │   [习惯 3] asyncio 并行执行工具，带超时与取消          <-- 1.6
    ▼
结果文本  ──►  追加到对话历史，进入下一轮循环
```

1.7 会用约 80 行代码把三者串成一个能跑的迷你 Agent。

<a id="ch1-s04"></a>

## 1.4 习惯 1：用联合类型建模「多种形态」

模型响应、消息、事件都有多种形态：要么是最终文本，要么是一批工具调用。用 `frozen dataclass` + `A | B` + `match`，再用 `assert_never` 做穷尽检查：**给联合加了新成员，却忘了改处理函数，`mypy --strict` 会直接报错**。对应 TS 的可辨识联合加 `never`。

```python
from __future__ import annotations

from dataclasses import dataclass
from typing import assert_never


@dataclass(frozen=True)
class TextResponse:
    content: str


@dataclass(frozen=True)
class ToolCallsResponse:
    names: tuple[str, ...]


ModelResponse = TextResponse | ToolCallsResponse


def handle(r: ModelResponse) -> str:
    match r:
        case TextResponse(content=text):
            return f"最终回答: {text}"
        case ToolCallsResponse(names=names):
            return f"调用工具: {', '.join(names)}"
        case _:
            assert_never(r)  # 漏了分支，mypy 在这里报错


print(handle(TextResponse("晴，26 度")))
print(handle(ToolCallsResponse(("get_weather", "calculator"))))
```

运行结果：

```text
最终回答: 晴，26 度
调用工具: get_weather, calculator
```

选哪种"类型容器"，按下表决定：

| 场景                       | 用什么                    | 理由                                       |
| -------------------------- | ------------------------- | ------------------------------------------ |
| 内部数据：消息、事件、结果 | `@dataclass(frozen=True)` | 轻量、不可变、可直接放进历史列表           |
| 来自外部的不可信数据       | pydantic `BaseModel`      | 构造时就校验（见 1.5）                     |
| 只约定"形状"，便于替换实现 | `typing.Protocol`         | 假模型和真模型有同名方法即可互换，不用继承 |
| 同一个值有多种形态         | `A \| B` + `match`        | 配合 `assert_never` 得到穷尽检查           |

两条配套习惯：函数入参用 `Sequence` / `Mapping`（只读，调用方传 tuple 也行）；数据尽量 `frozen=True`，需要"修改"时用 `dataclasses.replace`。

<a id="ch1-s05"></a>

## 1.5 习惯 2：pydantic 在边界校验

`json.loads` 返回 `Any`。你把变量标成 `dict`，只是声明，**不代表检查过它是 `dict`**。模型给的工具参数一律当不可信数据，用 pydantic 一份定义同时拿到三样东西：

| 用途                   | 写法                                                           |
| ---------------------- | -------------------------------------------------------------- |
| 静态类型（给 mypy）    | `args: WeatherArgs`                                            |
| 运行时校验（挡脏数据） | `WeatherArgs.model_validate(...)` / `model_validate_json(...)` |
| 给模型看的 tool schema | `WeatherArgs.model_json_schema()`                              |

```python
from __future__ import annotations

from pydantic import BaseModel, Field, ValidationError


class WeatherArgs(BaseModel):
    city: str = Field(description="城市名，如 深圳")
    unit: str = "c"


def validate_args(raw: str) -> WeatherArgs | str:
    try:
        return WeatherArgs.model_validate_json(raw)
    except ValidationError as e:
        detail = "; ".join(
            f"{'.'.join(map(str, err['loc'])) or '(root)'}: {err['msg']}"
            for err in e.errors()
        )
        return f"错误：参数不合法 —— {detail}"  # 变成文本回灌给模型，让它自行修正


print(validate_args('{"city": "深圳"}'))
print(validate_args('{"city": 123}'))
print(validate_args("{bad json"))
print(WeatherArgs.model_json_schema()["properties"]["city"])
```

运行结果：

```text
city='深圳' unit='c'
错误：参数不合法 —— city: Input should be a valid string
错误：参数不合法 —— (root): Invalid JSON: key must be a string at line 1 column 2
{'description': '城市名，如 深圳', 'title': 'City', 'type': 'string'}
```

> **Agent 和普通后端最大的差别**：可预期的失败（参数不合法、工具不存在、用户拒绝）**不抛异常，而是返回错误文本**，追加进对话历史。模型下一轮看到后会自己改参数，整个流程不崩。这里的错误信息是写给模型看的，所以要具体到字段名和原因。

对应 TS 的 zod：`parse` / `safeParse` / `toJSONSchema` 大致等于 `model_validate` / `try-except ValidationError` / `model_json_schema`。

<a id="ch1-s06"></a>

## 1.6 习惯 3：asyncio 的三件事

Agent 是 IO 密集程序，要等模型、等工具、等流式 token。先记住心智模型：`async def` 调用后只得到协程对象，不会自动执行；`await` 是"让出执行权"的挂起点，不是开线程；同一时刻只有一个协程在跑，但某个在等 IO 时，别的可以接着跑。

要掌握三件事：

1. **并行**：同一轮模型返回的多个工具调用用 `asyncio.gather` 并发。
2. **超时与取消**：`asyncio.timeout(s)` 包整体；取消沿 `await` 链自动传播，不用像 TS 那样逐层透传 `AbortSignal`。
3. **不阻塞事件循环**：同步阻塞函数用 `asyncio.to_thread` 挪走。

```python
from __future__ import annotations

import asyncio
import time


async def tool(name: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"{name} ok"


def blocking_io() -> str:
    time.sleep(0.05)  # 同步阻塞：直接在 async def 里调会卡死整个事件循环
    return "blocking done"


async def main() -> None:
    # 1) 并行：总耗时约等于最慢的那个，而不是相加
    start = time.perf_counter()
    results = await asyncio.gather(tool("weather", 0.1), tool("calc", 0.1))
    print(results, f"耗时 {time.perf_counter() - start:.2f}s")

    # 2) 同步阻塞调用放到线程里
    print(await asyncio.to_thread(blocking_io))

    # 3) 超时：内部协程被取消，外层看到 TimeoutError
    try:
        async with asyncio.timeout(0.05):
            await tool("slow", 10)
    except TimeoutError:
        print("超时，内部协程已被取消")

    print("CancelledError 是 Exception 子类吗:", issubclass(asyncio.CancelledError, Exception))


asyncio.run(main())  # 只在最顶层调一次
```

运行结果（耗时数字会有轻微波动）：

```text
['weather ok', 'calc ok'] 耗时 0.10s
blocking done
超时，内部协程已被取消
CancelledError 是 Exception 子类吗: False
```

最后一行是关键：**`CancelledError` 继承 `BaseException`，所以 `except Exception` 不会吞掉取消**，用户点"中止"能穿透整个调用链。反过来，**绝不能写 `except BaseException` 或裸 `except:`**，否则 Agent 会变得关不掉。

另一个差异：Python 的 async generator **不能 `return` 值**，事件流版本要把最终结果作为最后一个 `yield`（见 2.10）。

四个最常踩的坑：

| 坑                                   | 现象                                                                               | 修法                                        |
| ------------------------------------ | ---------------------------------------------------------------------------------- | ------------------------------------------- |
| 在 `async def` 里调同步阻塞函数      | `gather` 退化成串行，整个服务卡住                                                  | 换异步库（httpx、aiofiles），或 `to_thread` |
| 忘了 `await`                         | 拿到协程对象，什么都没执行，并有 `RuntimeWarning: coroutine ... was never awaited` | mypy 会提示类型不符                         |
| `except BaseException` 或裸 `except` | 取消被吞，Agent 关不掉                                                             | 只捕获 `Exception` 或更具体的类型           |
| 在循环里反复 `asyncio.run()`         | 每次新建并关闭事件循环，连接池等资源失效                                           | 顶层只调一次，内部全用 `await`              |

<a id="ch1-s07"></a>

## 1.7 串起来：约 80 行的迷你 Agent

把三个习惯放进一个能跑的循环：联合类型描述模型响应，pydantic 校验工具参数，`gather` 并行执行工具，`Protocol` 让假模型可以替换真模型。第 2 章就是把这个骨架逐步做完整。

```python
from __future__ import annotations

import asyncio
from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from typing import Protocol, assert_never

from pydantic import BaseModel, ValidationError


@dataclass(frozen=True)
class ToolCall:
    name: str
    arguments: str  # 模型给的原始 JSON 字符串，不可信


@dataclass(frozen=True)
class Text:
    content: str


@dataclass(frozen=True)
class Calls:
    calls: tuple[ToolCall, ...]


Response = Text | Calls


class LLM(Protocol):
    async def complete(self, history: list[str]) -> Response: ...


class AddArgs(BaseModel):
    a: int
    b: int


async def add(raw: str) -> str:
    try:
        args = AddArgs.model_validate_json(raw)  # 边界校验
    except ValidationError as e:
        return f"错误：参数不合法（{e.error_count()} 处）"  # 失败变成文本，不抛异常
    await asyncio.sleep(0.01)
    return str(args.a + args.b)


TOOLS: dict[str, Callable[[str], Awaitable[str]]] = {"add": add}


async def run_tool(call: ToolCall) -> str:
    fn = TOOLS.get(call.name)
    return await fn(call.arguments) if fn else f"错误：没有名为 {call.name} 的工具"


async def run(llm: LLM, question: str, max_steps: int = 5) -> str:
    history = [question]
    for _ in range(max_steps):  # 护栏：最大步数
        r = await llm.complete(history)
        match r:
            case Text(content=text):  # 模型给出最终回答，结束
                return text
            case Calls(calls=calls):  # 模型要调工具：并行执行，结果回灌
                outputs = await asyncio.gather(*(run_tool(c) for c in calls))
                history.extend(outputs)
            case _:
                assert_never(r)
    return "达到最大步数"


class Scripted:
    """假模型：第 1 轮请求两次工具调用（一次合法、一次参数错误），第 2 轮给最终回答。"""

    def __init__(self) -> None:
        self.step = 0

    async def complete(self, history: list[str]) -> Response:
        self.step += 1
        if self.step == 1:
            return Calls((ToolCall("add", '{"a": 2, "b": 3}'), ToolCall("add", '{"a": "x"}')))
        return Text("工具返回: " + " | ".join(history[1:]))


print(asyncio.run(run(Scripted(), "2+3=?")))
```


运行结果：

```text
工具返回: 5 | 错误：参数不合法（2 处）
```

注意第二个调用的参数是错的，但程序没有崩：错误变成文本进入 `history`，假模型在第二轮读到了它。真实模型会据此修正参数再调一次。`Scripted` 没有继承 `LLM`，只因为有同签名的 `complete` 就能传给 `llm: LLM`，这就是 Protocol。

<a id="ch1-s08"></a>
## 1.8 环境与检查

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install "pydantic>=2" httpx pytest mypy
mypy --strict . && pytest -q      # 进 CI；不跑 mypy，assert_never 的穷尽检查不会生效
```

需要 Python 3.11 及以上（用到 `asyncio.timeout`、`match`、`typing.assert_never`）。

<a id="ch1-s09"></a>
## 1.9 TS ↔ Python 速查

| TypeScript                       | Python                                                   |
| -------------------------------- | -------------------------------------------------------- |
| 可辨识联合 + `switch` + `never`  | `frozen dataclass` + `A \| B` + `match` + `assert_never` |
| `interface`                      | `Protocol`                                               |
| `zod` + `z.infer`                | pydantic `BaseModel`（类本身就是类型）                   |
| `z.toJSONSchema`                 | `model_json_schema()`                                    |
| `Promise.all`                    | `asyncio.gather`                                         |
| `AbortSignal`                    | `task.cancel()` + `asyncio.timeout()`                    |
| `async function*` 可 `return` 值 | async generator 不能 `return` 值                         |
| `tsc --strict` / `vitest`        | `mypy --strict` / `pytest`                               |

<a id="ch1-s10"></a>
## 小结

- Python 占优在**编排层**；前端、网关、单二进制分发另选语言。
- 类型标注运行时不检查：内部用 dataclass + 联合类型 + mypy，外部数据用 pydantic。
- 可预期的失败变成错误文本回灌给模型，只有取消和意外错误才向上抛。
- asyncio 三件事：`gather` 并行、`timeout` 加取消、`to_thread` 挪走阻塞调用；永远不要吞掉 `CancelledError`。
- 接下来：第 2 章把 1.7 的骨架做成完整 Agent。

<a id="ch1-s11"></a>
## 练习

1. 给 1.7 的 `Response` 加第三种形态 `Refusal(reason: str)`，**不改** `run`，运行 `mypy --strict`，看它在哪里报错，再补上分支。
2. 把 1.6 里的 `gather` 换成两次串行 `await`，对比耗时。
3. 把 `tool` 里的 `asyncio.sleep` 换成同步的 `time.sleep`，观察 `gather` 是否还能并行；再用 `to_thread` 修复。
4. 给 `WeatherArgs` 传 `{"city": "深圳", "extra": 1}`，看是否报错；再想办法让多余字段也报错。

**参考思路**

1. mypy 会在 `assert_never(r)` 处报 `Argument 1 to "assert_never" has incompatible type "Refusal"; expected "Never"`，这正是穷尽检查要告诉你的：还有一个形态没处理。
2. 并行约 0.1 秒，串行约 0.2 秒。
3. 阻塞版两个调用串行，总耗时约 0.2 秒；`await asyncio.to_thread(time.sleep, 0.1)` 版回到约 0.1 秒。
4. pydantic 默认忽略多余字段，不报错。给模型加 `model_config = ConfigDict(extra="forbid")` 后，会报 `extra_forbidden`。让模型乱填的字段被明确拒绝，更利于它自我修正。

---

<a id="ch2"></a>
# 第 2 章 实战：从零写一个 Tool-calling Agent

> **本章目标**：不借助任何框架，用约 450 行 Python 手写一个能并行调用工具、能超时取消、能流式输出的 Agent，并带完整测试。
> **前置**：读过第 1 章，或已熟悉 dataclass、pydantic、asyncio。
> **产出**：`agent.py`、`test_agent.py`、`test_wire.py`，无需 API Key 即可全部跑通。

环境：Python 3.11+（用到 `asyncio.timeout`、`match`）。

```bash
python -m venv .venv && source .venv/bin/activate
pip install pydantic httpx pytest mypy
```

本章的 `agent.py`、`test_agent.py`、`test_wire.py` 由 `extract.py` 从单章版 `Python版Agent.md` 的代码块自动抽取，随本目录一并提供。

<a id="ch2-s01"></a>
## 2.1 本章地图与 TS 概念对照

**本章代码地图**：每一节产出一块代码，最后拼成完整的 `agent.py`。

| 小节         | 产出                                           | 关键点                               |
| ------------ | ---------------------------------------------- | ------------------------------------ |
| 2.3 数据模型 | `Message`、`ModelResponse`、`LLM` 协议         | 联合类型 + `Protocol`                |
| 2.4 工具     | `Tool`、`ToolRegistry`、计算器与天气工具       | pydantic 一份定义三种用途            |
| 2.5 执行工具 | `execute_tool`                                 | 校验、人工确认、错误转文本           |
| 2.6 主循环   | `run_agent`                                    | `gather` 并行、`max_steps` 兜底      |
| 2.7 假模型   | `ScriptedLLM`、`main`                          | 不联网跑通整条链路                   |
| 2.8 测试     | `test_agent.py`                                | 参数错误、死循环、危险工具、超时取消 |
| 2.9 真实模型 | `OpenAICompatibleLLM`、`retry`、`test_wire.py` | 边界校验、离线 Mock 验证             |
| 2.10 流式    | `run_agent_stream`                             | async generator                      |

**TS 与 Python 概念对照**：

| TS 版                                | Python 版                                          | 备注                                         |
| ------------------------------------ | -------------------------------------------------- | -------------------------------------------- |
| 可辨识联合 `{ role: "user" } \| ...` | 多个 `@dataclass` + `X \| Y` 联合 + `match`        | `match` 的类模式就是"按类型收窄"             |
| `switch` + `never` 穷尽检查          | `match` + `assert_never`（`typing`）               | 需要 mypy / pyright 才有编译期检查           |
| `interface LLM`                      | `typing.Protocol`                                  | 同样是结构化类型，鸭子类型                   |
| zod schema + `z.infer`               | pydantic `BaseModel`                               | 类本身既是类型，也是校验器                   |
| `z.toJSONSchema`                     | `Model.model_json_schema()`                        | 直接给模型当工具定义                         |
| `Promise.all`                        | `asyncio.gather`                                   |                                              |
| `AbortSignal`                        | **任务取消** `task.cancel()` + `asyncio.timeout()` | 不用手动透传 signal，见 2.6                  |
| `async function*`                    | `async def` + `yield`                              | 但**不能 `return` 值**，见 2.10              |
| vitest                               | pytest                                             |                                              |
| 类型只在编译期                       | 类型提示只被 mypy/pyright 检查                     | 运行时完全不检查，所以**边界校验同样必须做** |

**心智模型不变**：Python 的类型提示和 TS 一样不会在运行时保护你。模型输出、HTTP 响应进来时，必须用 pydantic 校验。

<a id="ch2-s02"></a>
## 2.2 Agent 的本质：一个循环

> 1. 把「对话历史 + 工具列表」发给模型
> 2. 模型返回：最终文本 或 工具调用请求
> 3. 若是工具调用 → 本地执行 → 结果追加到历史
> 4. 回到 1，直到得到最终文本 或 达到最大步数

**设计顺序：数据模型 → 工具 → 执行 → 循环 → 测试 → 接真实模型。**

下面是一次完整交互结束后，`messages` 里依次存了什么（对应 2.7 的演示）：

```text
system    你是一个乐于助人的助手，必要时调用工具。
user      深圳天气如何？顺便算 6×7
assistant （发起 2 个工具调用：get_weather、calculator）
tool      {"city": "深圳", "temp": 26, "desc": "晴"}
tool      42
assistant 汇总：...
```

整个 Agent 的状态就是这个列表，每一轮往里追加。所以持久化会话、断点续跑、做评测回放，都只是在存取这个列表。

<a id="ch2-s03"></a>
## 2.3 数据模型

消息和模型响应用 `frozen dataclass`（不可变、轻量）。联合类型 `A | B` 加 `match`，等价于 TS 的可辨识联合。

```python
from __future__ import annotations

import asyncio
import json
from collections.abc import AsyncIterator, Awaitable, Callable, Sequence
from dataclasses import dataclass
from typing import Any, Generic, Literal, Protocol, TypeVar, assert_never

from pydantic import BaseModel, Field, ValidationError


@dataclass(frozen=True)
class ToolCall:
    id: str
    name: str
    arguments: Any  # 来自模型，不可信：类型是 Any，进入工具前必须校验


@dataclass(frozen=True)
class SystemMessage:
    content: str
    role: Literal["system"] = "system"


@dataclass(frozen=True)
class UserMessage:
    content: str
    role: Literal["user"] = "user"


@dataclass(frozen=True)
class AssistantMessage:
    content: str
    tool_calls: tuple[ToolCall, ...] = ()
    role: Literal["assistant"] = "assistant"


@dataclass(frozen=True)
class ToolMessage:
    tool_call_id: str
    name: str
    content: str
    role: Literal["tool"] = "tool"


Message = SystemMessage | UserMessage | AssistantMessage | ToolMessage


@dataclass(frozen=True)
class TextResponse:
    content: str


@dataclass(frozen=True)
class ToolCallsResponse:
    calls: tuple[ToolCall, ...]


ModelResponse = TextResponse | ToolCallsResponse


@dataclass(frozen=True)
class ToolDescriptor:
    name: str
    description: str
    parameters: dict[str, Any]  # JSON Schema


class LLM(Protocol):
    """只依赖接口：测试用假模型，上线换真模型。"""

    async def complete(
        self, messages: Sequence[Message], tools: Sequence[ToolDescriptor]
    ) -> ModelResponse: ...
```

要点：`Protocol` 是结构化类型，任何有 `complete` 方法的对象都满足 `LLM`，不需要继承。

<a id="ch2-s04"></a>
## 2.4 工具：一个 pydantic 模型，三种用途

`BaseModel` 同时给出：**参数类型**（给 mypy）、**运行时校验**（给模型输入）、**JSON Schema**（给模型看）。

```python
ArgsT = TypeVar("ArgsT", bound=BaseModel)


@dataclass
class Tool(Generic[ArgsT]):
    name: str
    description: str
    args_model: type[ArgsT]
    run: Callable[[ArgsT], Awaitable[str]]
    dangerous: bool = False  # 需要人工确认的工具


class CalcArgs(BaseModel):
    a: float
    b: float
    op: Literal["add", "sub", "mul", "div"]


async def _calc(args: CalcArgs) -> str:
    match args.op:
        case "add":
            r = args.a + args.b
        case "sub":
            r = args.a - args.b
        case "mul":
            r = args.a * args.b
        case "div":
            if args.b == 0:
                raise ValueError("除数不能为 0")
            r = args.a / args.b
        case _:
            assert_never(args.op)  # 给 op 加新值却忘了处理时，mypy 会报错
    return f"{r:g}"


calculator = Tool("calculator", "计算两个数的四则运算", CalcArgs, _calc)


class WeatherArgs(BaseModel):
    city: str = Field(description="城市名，如 深圳")


async def _weather(args: WeatherArgs) -> str:
    return json.dumps({"city": args.city, "temp": 26, "desc": "晴"}, ensure_ascii=False)


get_weather = Tool("get_weather", "查询城市天气", WeatherArgs, _weather)
```

注册表：统一存放各种参数类型的工具，并导出给模型看的描述。

```python
class ToolRegistry:
    def __init__(self) -> None:
        self._tools: dict[str, Tool[Any]] = {}

    def register(self, *tools: Tool[Any]) -> ToolRegistry:
        for t in tools:
            self._tools[t.name] = t
        return self

    def get(self, name: str) -> Tool[Any] | None:
        return self._tools.get(name)

    def descriptors(self) -> list[ToolDescriptor]:
        return [
            ToolDescriptor(t.name, t.description, t.args_model.model_json_schema())
            for t in self._tools.values()
        ]


registry = ToolRegistry().register(calculator, get_weather)
```

<a id="ch2-s05"></a>
## 2.5 安全地执行工具

原则：**工具调用来自不可信的模型，必须校验；失败要变成"给模型看的文本"，不能让整个 Agent 崩溃。**

```python
Approve = Callable[[ToolCall], Awaitable[bool]]


async def execute_tool(
    registry: ToolRegistry, call: ToolCall, approve: Approve | None = None
) -> str:
    tool = registry.get(call.name)
    if tool is None:
        return f"错误：不存在名为 {call.name} 的工具"

    try:
        args = tool.args_model.model_validate(call.arguments)
    except ValidationError as e:
        detail = "; ".join(
            f"{'.'.join(map(str, err['loc'])) or '(root)'}: {err['msg']}"
            for err in e.errors()
        )
        return f"错误：参数不合法 —— {detail}"  # 反馈给模型，让它自行修正

    if tool.dangerous and not (approve and await approve(call)):
        return "错误：用户拒绝了该操作"

    try:
        return await tool.run(args)
    except Exception as e:  # 注意：CancelledError 不是 Exception 子类，取消会自然向上传播
        return f"错误：工具执行失败 —— {e}"
```

最后一个 `except Exception` 是关键：Python 3.8+ 的 `asyncio.CancelledError` 继承自 `BaseException`，**不会被它吞掉**，所以"用户取消"天然向上传播，不需要像 TS 那样手动判断 `signal.aborted`。

<a id="ch2-s06"></a>
## 2.6 主循环

```python
@dataclass(frozen=True)
class ModelResponseEvent:
    step: int
    response: ModelResponse


@dataclass(frozen=True)
class ToolStartEvent:
    call: ToolCall


@dataclass(frozen=True)
class ToolEndEvent:
    call: ToolCall
    output: str


AgentEvent = ModelResponseEvent | ToolStartEvent | ToolEndEvent


@dataclass(frozen=True)
class Done:
    answer: str
    messages: list[Message]


@dataclass(frozen=True)
class MaxSteps:
    messages: list[Message]


AgentResult = Done | MaxSteps

DEFAULT_PROMPT = "你是一个乐于助人的助手，必要时调用工具。"


async def run_agent(
    user_input: str,
    *,
    llm: LLM,
    registry: ToolRegistry,
    system_prompt: str = DEFAULT_PROMPT,
    max_steps: int = 8,
    approve: Approve | None = None,
    on_event: Callable[[AgentEvent], None] | None = None,
) -> AgentResult:
    def emit(e: AgentEvent) -> None:
        if on_event:
            on_event(e)

    messages: list[Message] = [SystemMessage(system_prompt), UserMessage(user_input)]

    for step in range(1, max_steps + 1):
        response = await llm.complete(messages, registry.descriptors())
        emit(ModelResponseEvent(step, response))

        match response:
            case TextResponse(content=text):
                messages.append(AssistantMessage(text))
                return Done(text, messages)

            case ToolCallsResponse(calls=calls):
                messages.append(AssistantMessage("", calls))

                async def run_one(call: ToolCall) -> str:
                    emit(ToolStartEvent(call))
                    output = await execute_tool(registry, call, approve)
                    emit(ToolEndEvent(call, output))
                    return output

                # 同一轮的多个调用并行执行
                outputs = await asyncio.gather(*(run_one(c) for c in calls))
                for call, output in zip(calls, outputs, strict=True):
                    messages.append(ToolMessage(call.id, call.name, output))

    return MaxSteps(messages)  # 防止模型死循环烧钱
```


<a id="ch2-s07"></a>
### 2.6.1 取消与超时：不用 signal

Python 的取消是**任务级**的：

```py
# 整体超时：超时后内部所有 await 处抛 CancelledError，最外层转成 TimeoutError
async with asyncio.timeout(30):
    result = await run_agent("...", llm=llm, registry=registry)

# 用户主动中止：对任务调用 cancel()
task = asyncio.create_task(run_agent("...", llm=llm, registry=registry))
task.cancel()          # 之后 await task 会抛 CancelledError
```

| TS                          | Python                                    |
| --------------------------- | ----------------------------------------- |
| 每个函数接收并透传 `signal` | **不需要**，取消沿 `await` 链自动传播     |
| `AbortSignal.timeout(ms)`   | `asyncio.timeout(s)` / `asyncio.wait_for` |
| `signal.throwIfAborted()`   | 不需要，下一个 `await` 处自动抛出         |
| 工具里 `catch` 要排除取消   | `except Exception` 天然不吞               |

**唯一要注意**：不要写 `except BaseException` 或裸 `except:`，会把取消吞掉。

<a id="ch2-s08"></a>
### 2.6.2 设计细节

| 设计                   | 作用                                      |
| ---------------------- | ----------------------------------------- |
| `max_steps`            | 兜底，防死循环                            |
| 工具错误转文本         | 模型可自我修正，流程不崩                  |
| `asyncio.gather`       | 同轮多个工具调用并行                      |
| `on_event`             | 解耦"过程"与"展示"，便于做 UI、日志、测试 |
| 返回完整 `messages`    | 可持久化会话、继续对话                    |
| 关键字参数（`*` 之后） | 参数多时调用处可读，等价于 TS 的对象参数  |

<a id="ch2-s09"></a>
## 2.7 用假模型跑起来

```python
@dataclass
class ScriptedLLM:
    """脚本化的假模型：按顺序返回预设响应。"""

    script: list[Callable[[Sequence[Message]], ModelResponse]]
    _i: int = 0

    async def complete(
        self, messages: Sequence[Message], tools: Sequence[ToolDescriptor]
    ) -> ModelResponse:
        if self._i >= len(self.script):
            raise RuntimeError("脚本已耗尽")
        fn = self.script[self._i]
        self._i += 1
        return fn(messages)


async def main() -> None:
    scripted = ScriptedLLM(
        [
            # 第 1 轮：同时调用两个工具
            lambda msgs: ToolCallsResponse(
                (
                    ToolCall("c1", "get_weather", {"city": "深圳"}),
                    ToolCall("c2", "calculator", {"a": 6, "b": 7, "op": "mul"}),
                )
            ),
            # 第 2 轮：读到工具结果，给出最终回答
            lambda msgs: TextResponse(
                "汇总：" + " | ".join(m.content for m in msgs if isinstance(m, ToolMessage))
            ),
        ]
    )

    async with asyncio.timeout(30):
        result = await run_agent(
            "深圳天气如何？顺便算 6×7",
            llm=scripted,
            registry=registry,
            on_event=lambda e: print("事件:", type(e).__name__),
        )

    match result:
        case Done(answer=answer):
            print("回答:", answer)
        case MaxSteps():
            print("达到最大步数")
```

运行结果（`main()` 部分）：

```text
事件: ModelResponseEvent
事件: ToolStartEvent
事件: ToolEndEvent
事件: ToolStartEvent
事件: ToolEndEvent
事件: ModelResponseEvent
回答: 汇总：{"city": "深圳", "temp": 26, "desc": "晴"} | 42
```

两个工具先后各出现一次 Start / End，说明它们被并行启动，随后第二轮模型读到两条工具结果并给出回答。

`ScriptedLLM` 没有继承 `LLM`，但有同签名的 `complete`，所以能直接传给 `llm: LLM` 参数。这就是 Protocol。

<a id="ch2-s10"></a>
## 2.8 测试

```python
# test_agent.py
import asyncio

import pytest

from agent import (
    Done, MaxSteps, ScriptedLLM, TextResponse, Tool, ToolCall, ToolCallsResponse,
    ToolMessage, ToolRegistry, WeatherArgs, calculator, get_weather, run_agent,
)


def test_invalid_args_are_fed_back_to_model() -> None:
    llm = ScriptedLLM(
        [
            lambda ms: ToolCallsResponse((ToolCall("c1", "calculator", {"a": "x"}),)),
            lambda ms: TextResponse(
                ms[-1].content if isinstance(ms[-1], ToolMessage) else "没有工具消息"
            ),
        ]
    )
    r = asyncio.run(run_agent("算一下", llm=llm, registry=ToolRegistry().register(calculator)))
    assert isinstance(r, Done)
    assert "参数不合法" in r.answer


def test_stops_at_max_steps() -> None:
    one = lambda ms: ToolCallsResponse((ToolCall("x", "get_weather", {"city": "A"}),))
    llm = ScriptedLLM([one] * 10)
    r = asyncio.run(
        run_agent("loop", llm=llm, registry=ToolRegistry().register(get_weather), max_steps=3)
    )
    assert isinstance(r, MaxSteps)


def test_dangerous_tool_needs_approval() -> None:
    async def _run(args: WeatherArgs) -> str:
        return "已删除"

    danger = Tool("delete", "删除", WeatherArgs, _run, dangerous=True)

    def make_llm() -> ScriptedLLM:
        return ScriptedLLM(
            [
                lambda ms: ToolCallsResponse((ToolCall("d", "delete", {"city": "x"}),)),
                lambda ms: TextResponse(
                    ms[-1].content if isinstance(ms[-1], ToolMessage) else "没有工具消息"
                ),
            ]
        )

    reg = ToolRegistry().register(danger)

    async def deny(call: ToolCall) -> bool:
        return False

    async def allow(call: ToolCall) -> bool:
        return True

    r1 = asyncio.run(run_agent("x", llm=make_llm(), registry=reg, approve=deny))
    r2 = asyncio.run(run_agent("x", llm=make_llm(), registry=reg, approve=allow))
    assert isinstance(r1, Done) and "拒绝" in r1.answer
    assert isinstance(r2, Done) and r2.answer == "已删除"


def test_timeout_cancels_slow_tool() -> None:
    async def _slow(args: WeatherArgs) -> str:
        await asyncio.sleep(10)
        return "never"

    slow = Tool("slow", "慢工具", WeatherArgs, _slow)
    llm = ScriptedLLM([lambda ms: ToolCallsResponse((ToolCall("s", "slow", {"city": "x"}),))])

    async def go() -> None:
        async with asyncio.timeout(0.1):
            await run_agent("x", llm=llm, registry=ToolRegistry().register(slow))

    with pytest.raises(TimeoutError):  # 取消没有被工具里的 except 吞掉
        asyncio.run(go())
```

```bash
pytest -q
```

<a id="ch2-s11"></a>
## 2.9 接入真实模型

只需实现 `LLM` 协议，业务代码一行不改。下面是兼容 OpenAI Chat Completions 的实现（国内多数厂商同一格式，改 `base_url` 和 `model` 即可）。响应在**边界处用 pydantic 校验**。

```python
import httpx


class WireFunction(BaseModel):
    name: str
    arguments: str


class WireToolCall(BaseModel):
    id: str
    function: WireFunction


class WireMessage(BaseModel):
    content: str | None = None
    tool_calls: list[WireToolCall] | None = None


class WireChoice(BaseModel):
    message: WireMessage


class WireResponse(BaseModel):
    choices: list[WireChoice] = Field(min_length=1)


def to_wire(m: Message) -> dict[str, Any]:
    match m:
        case AssistantMessage(content=content, tool_calls=calls):
            d: dict[str, Any] = {"role": "assistant", "content": content}
            if calls:
                d["tool_calls"] = [
                    {
                        "id": c.id,
                        "type": "function",
                        "function": {"name": c.name, "arguments": json.dumps(c.arguments, ensure_ascii=False)},
                    }
                    for c in calls
                ]
            return d
        case ToolMessage():
            return {"role": "tool", "tool_call_id": m.tool_call_id, "content": m.content}
        case _:
            return {"role": m.role, "content": m.content}


def safe_json(s: str) -> Any:
    try:
        return json.loads(s)
    except json.JSONDecodeError:
        return s  # 原样传下去，让工具参数校验报错并反馈给模型


class OpenAICompatibleLLM:
    def __init__(self, base_url: str, api_key: str, model: str, timeout: float = 60.0) -> None:
        self._model = model
        self._client = httpx.AsyncClient(
            base_url=base_url,
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=timeout,
        )

    async def complete(
        self, messages: Sequence[Message], tools: Sequence[ToolDescriptor]
    ) -> ModelResponse:
        payload: dict[str, Any] = {
            "model": self._model,
            "messages": [to_wire(m) for m in messages],
        }
        if tools:
            payload["tools"] = [
                {"type": "function", "function": {"name": t.name, "description": t.description, "parameters": t.parameters}}
                for t in tools
            ]
        resp = await self._client.post("/chat/completions", json=payload)
        resp.raise_for_status()

        msg = WireResponse.model_validate(resp.json()).choices[0].message  # 边界处校验
        if msg.tool_calls:
            return ToolCallsResponse(
                tuple(ToolCall(c.id, c.function.name, safe_json(c.function.arguments)) for c in msg.tool_calls)
            )
        return TextResponse(msg.content or "")

    async def aclose(self) -> None:
        await self._client.aclose()


# llm = OpenAICompatibleLLM("https://api.openai.com/v1", os.environ["API_KEY"], "gpt-4o")
```

<a id="ch2-s12"></a>
### 2.9.1 不联网验证

连真实 API 前，先用 `httpx.MockTransport` 把 HTTP 响应伪造出来，验证序列化、边界校验和工具调用解析：

```python
# test_wire.py
"""不联网验证 OpenAICompatibleLLM：用 httpx.MockTransport 伪造 HTTP 响应。"""
import asyncio

import httpx
import pytest

from agent import (
    OpenAICompatibleLLM, TextResponse, ToolCallsResponse, UserMessage, WireResponse,
)


def fake_llm(payload: dict[str, object]) -> OpenAICompatibleLLM:
    llm = OpenAICompatibleLLM("https://example.test/v1", "sk-test", "m")
    llm._client = httpx.AsyncClient(
        transport=httpx.MockTransport(lambda req: httpx.Response(200, json=payload)),
        base_url="https://example.test/v1",
    )
    return llm


def test_text_response() -> None:
    llm = fake_llm({"choices": [{"message": {"content": "你好"}}]})
    r = asyncio.run(llm.complete([UserMessage("hi")], []))
    assert isinstance(r, TextResponse) and r.content == "你好"


def test_tool_call_arguments_are_parsed() -> None:
    llm = fake_llm({"choices": [{"message": {"content": None, "tool_calls": [
        {"id": "c1", "function": {"name": "get_weather", "arguments": '{"city": "深圳"}'}},
    ]}}]})
    r = asyncio.run(llm.complete([UserMessage("天气")], []))
    assert isinstance(r, ToolCallsResponse) and r.calls[0].arguments == {"city": "深圳"}


def test_bad_json_arguments_do_not_crash() -> None:
    llm = fake_llm({"choices": [{"message": {"content": None, "tool_calls": [
        {"id": "c2", "function": {"name": "calculator", "arguments": "{bad json"}},
    ]}}]})
    r = asyncio.run(llm.complete([UserMessage("算一下")], []))
    assert isinstance(r, ToolCallsResponse) and isinstance(r.calls[0].arguments, str)


def test_empty_choices_rejected_at_boundary() -> None:
    with pytest.raises(ValueError):  # pydantic ValidationError 是 ValueError 子类
        WireResponse.model_validate({"choices": []})
```

`pytest -q` 会把 `test_agent.py` 和 `test_wire.py` 一起收集。

对应关系：TS 里用 `AbortSignal.any([...])` 合并取消与超时，这里取消由 asyncio 负责，超时由 `httpx` 的 `timeout` 管。外部调用建议再套重试：

```python
R = TypeVar("R")


async def retry(fn: Callable[[], Awaitable[R]], retries: int = 3, base_delay: float = 0.2) -> R:
    import random

    last: Exception | None = None
    for attempt in range(retries + 1):
        try:
            return await fn()
        except (httpx.TransportError, httpx.HTTPStatusError) as e:  # 只重试可恢复错误
            last = e
            if attempt == retries:
                break
            await asyncio.sleep(base_delay * 2**attempt + random.random() * 0.1)  # 指数退避 + 抖动
    assert last is not None
    raise last
```


这里用 `TypeVar` 而非 3.12 的 `def retry[T]` 新语法，保证 3.11 可用。

<a id="ch2-s13"></a>
## 2.10 事件流式输出

把回调改成 **async generator**，调用方用 `async for` 消费。

**与 TS 的关键差异**：Python 的 async generator **不能 `return` 值**，所以把最终结果作为最后一个 `yield`。

```python
async def run_agent_stream(
    user_input: str,
    *,
    llm: LLM,
    registry: ToolRegistry,
    system_prompt: str = DEFAULT_PROMPT,
    max_steps: int = 8,
    approve: Approve | None = None,
) -> AsyncIterator[AgentEvent | AgentResult]:
    messages: list[Message] = [SystemMessage(system_prompt), UserMessage(user_input)]

    for step in range(1, max_steps + 1):
        response = await llm.complete(messages, registry.descriptors())
        yield ModelResponseEvent(step, response)

        if isinstance(response, TextResponse):
            messages.append(AssistantMessage(response.content))
            yield Done(response.content, messages)
            return

        messages.append(AssistantMessage("", response.calls))
        for call in response.calls:
            yield ToolStartEvent(call)
            output = await execute_tool(registry, call, approve)
            yield ToolEndEvent(call, output)
            messages.append(ToolMessage(call.id, call.name, output))

    yield MaxSteps(messages)


async def stream_demo() -> None:
    llm = ScriptedLLM(
        [
            lambda msgs: ToolCallsResponse((ToolCall("c1", "get_weather", {"city": "深圳"}),)),
            lambda msgs: TextResponse("晴，26 度"),
        ]
    )
    async for item in run_agent_stream("深圳天气？", llm=llm, registry=registry):
        match item:
            case Done(answer=answer):
                print("最终:", answer)
            case MaxSteps():
                print("达到最大步数")
            case _:
                print("事件:", type(item).__name__)
```

注意这里为了逐个 `yield` 事件，工具改成了**串行**执行；2.6 的主循环用 `asyncio.gather` 是**并行**。要两者兼得，可用 `asyncio.TaskGroup` + `asyncio.Queue` 把并行产生的事件推给生成器（练习 4）。

这里是**事件级**流式。**token 级**流式：给 `LLM` 加一个 `stream()` 方法，返回 `AsyncIterator[str]`，用 `httpx` 的 `client.stream(...)` + `response.aiter_lines()` 解析 `data: {...}` 行，遇到 `data: [DONE]` 结束。

跑起来：

```python
if __name__ == "__main__":
    asyncio.run(main())
    asyncio.run(stream_demo())
```

```bash
python agent.py
```

完整输出是前面 2.7 的 7 行，加上流式版的 5 行：

```text
事件: ModelResponseEvent
事件: ToolStartEvent
事件: ToolEndEvent
事件: ModelResponseEvent
最终: 晴，26 度
```

<a id="ch2-s14"></a>
## 2.11 护栏清单

| 风险                               | 对策                                                             |
| ---------------------------------- | ---------------------------------------------------------------- |
| 模型死循环、烧钱                   | `max_steps`；累计 token / 成本上限                               |
| 参数乱填                           | pydantic 校验，错误回传给模型                                    |
| 危险操作（删文件、发消息、花钱）   | `dangerous=True` + `approve` 回调人工确认                        |
| 请求挂起                           | `asyncio.timeout` 包整体 + `httpx` 超时                          |
| 用户想中止                         | `task.cancel()`；别吞 `CancelledError`                           |
| 提示注入（工具返回内容里夹带指令） | 工具输出视为**数据而非指令**；限制工具权限；敏感操作必须人工确认 |
| 密钥泄露                           | 只放环境变量；日志脱敏；不进提示词                               |
| 上下文过长                         | 截断或摘要旧消息；限制单个工具输出长度                           |
| 同步阻塞调用卡住事件循环           | CPU 或同步 IO 用 `asyncio.to_thread(...)`                        |

最后一条是 Python 特有的：**在 `async def` 里调 `requests.get()`、`time.sleep()` 这类同步函数会卡死整个事件循环**，所有并行都失效。要么用异步库（httpx、aiofiles），要么 `await asyncio.to_thread(sync_fn, ...)`。

<a id="ch2-s15"></a>
## 2.12 类型检查与框架

```bash
pip install mypy
mypy --strict agent.py
```

mypy / pyright 对应 TS 的 `tsc --noEmit`，**CI 里要跑**。`assert_never` 与 `match` 配合能得到和 TS `never` 一样的穷尽检查。

| 方向          | 说明                                                                             |
| ------------- | -------------------------------------------------------------------------------- |
| 现成框架      | OpenAI Agents SDK、Claude Agent SDK、LangGraph、pydantic-ai、smolagents、AutoGen |
| MCP           | 官方 `mcp` Python SDK；把 MCP 工具适配成本章的 `Tool`                            |
| 多 Agent      | 把子 Agent 包装成一个 `Tool`                                                     |
| 记忆 / 持久化 | `messages` 是 dataclass 列表，转 dict 即可存储                                   |

**先手写一遍本章的循环，再看框架，你会更清楚框架替你做了什么。**

<a id="ch2-s16"></a>
## 小结

- **Agent = 一个循环**：模型返回文本就结束，返回工具调用就执行、回灌、再问。`max_steps` 是兜底。
- **边界校验**：模型给的工具参数用 pydantic 校验；失败转成错误文本回灌，而不是抛异常。
- **并行与取消**：同轮工具调用用 `gather` 并行；取消沿 `await` 链传播，`except Exception` 天然不吞它。
- **可替换与可测试**：`LLM` 是 `Protocol`，用 `ScriptedLLM` 和 `httpx.MockTransport` 做到完全离线测试。
- **上线前**：对照 2.11 的护栏清单逐项检查。

**怎么跑**：

```bash
python3 extract.py        # 从本文档同步代码
python agent.py           # 跑演示（无需 API Key）
pytest -q                 # 8 个测试
mypy --strict agent.py test_agent.py test_wire.py
```

**常见报错速查**：

| 现象                                                                     | 原因                                             | 处理                                           |
| ------------------------------------------------------------------------ | ------------------------------------------------ | ---------------------------------------------- |
| `RuntimeWarning: coroutine ... was never awaited`                        | 调用异步函数时漏了 `await`                       | 补 `await`，或用 `asyncio.run` / `gather` 驱动 |
| `RuntimeError: asyncio.run() cannot be called from a running event loop` | 在已有事件循环里（如 Jupyter）又调 `asyncio.run` | 直接 `await main()`                            |
| mypy：`Argument 1 to "assert_never" has incompatible type ...`           | `match` 漏了联合里的某个成员                     | 补上对应的 `case`，这是穷尽检查在起作用        |
| `ValidationError` 提示 `Field required` / `Input should be ...`          | 模型给的参数缺字段或类型不对                     | 正常现象，`execute_tool` 已转成文本回灌模型    |
| `RuntimeError: 脚本已耗尽`                                               | `ScriptedLLM` 的预设响应比循环轮数少             | 给脚本补响应，或检查是否进入了意外的额外一轮   |
| 并行没有变快                                                             | 工具里调了同步阻塞函数                           | 换异步库，或 `await asyncio.to_thread(...)`    |
| Python 3.10 报 `asyncio.timeout` 不存在                                  | 该 API 是 3.11 引入的                            | 升级到 3.11+，或改用 `asyncio.wait_for`        |

<a id="ch2-s17"></a>
## 练习

1. 给 `execute_tool` 加单个工具超时：`async with asyncio.timeout(10)`，超时返回错误文本（注意区分"工具超时"与"整体取消"）
2. 实现真实的 `search` 工具：用 `httpx` 调某个 HTTP API，并用 pydantic 校验返回值
3. 给 `LLM` 加 `stream()` 方法，实现 token 级流式
4. 把同轮工具调用改成可配置的并行 / 串行

**参考思路**

1. 在 `execute_tool` 里用 `try: async with asyncio.timeout(10): return await tool.run(args)`，再 `except TimeoutError: return "错误：工具执行超时"`。注意：只有这个**局部**的 `TimeoutError` 转成文本；外层整体超时抛出的 `TimeoutError` 不在这个 `try` 里，仍会向上传播。
2. 定义一个 `SearchArgs(BaseModel)`，再定义一个 `SearchResult(BaseModel)` 去 `model_validate(resp.json())`，校验失败时返回错误文本。网络错误交给 `retry`。
3. 在 `LLM` 协议里加 `def stream(...) -> AsyncIterator[str]`，实现里用 `client.stream("POST", ...)` + `response.aiter_lines()` 解析 `data: {...}`，遇到 `data: [DONE]` 结束。
4. 给 `run_agent` 加参数 `parallel: bool = True`；为 `False` 时用 `for call in calls: outputs.append(await run_one(call))` 代替 `gather`。
