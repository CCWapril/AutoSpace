# Go 语言精讲教材

**从 Python/C++ 到后端微服务**

基础语法 · 类型系统 · 并发编程 · 工程化 · 运行时原理 · trpc-go · 综合实战

适用读者：具备 Python / C++ 基础、目标为后端与微服务开发的工程师

版本基准：Go 1.22 及以上（示例在 Go 1.25 下实测） · 2026 年 11 月

## 目录

- [使用说明](#使用说明)
- [第 1 章 Go 语言概览](#第-1-章-go-语言概览)
  - [1.1 Go 是什么](#11-go-是什么)
  - [1.2 适合与不适合](#12-适合与不适合)
  - [1.3 第一个程序](#13-第一个程序)
  - [1.4 包与模块](#14-包与模块)
- [第 2 章 基础语法](#第-2-章-基础语法)
  - [2.1 变量、常量与零值](#21-变量常量与零值)
  - [2.2 控制流](#22-控制流)
  - [2.3 函数](#23-函数)
  - [2.4 defer](#24-defer)
  - [2.5 数组、切片与 map](#25-数组切片与-map)
  - [2.6 指针](#26-指针)
- [第 3 章 类型系统](#第-3-章-类型系统)
  - [3.1 struct 与方法](#31-struct-与方法)
  - [3.2 组合代替继承](#32-组合代替继承)
  - [3.3 interface](#33-interface)
  - [3.4 错误处理](#34-错误处理)
  - [3.5 泛型](#35-泛型)
- [第 4 章 并发编程](#第-4-章-并发编程)
  - [4.1 goroutine](#41-goroutine)
  - [4.2 channel](#42-channel)
  - [4.3 select](#43-select)
  - [4.4 sync 包](#44-sync-包)
  - [4.5 context](#45-context)
  - [4.6 经典模式：worker pool](#46-经典模式worker-pool)
- [第 5 章 工程化](#第-5-章-工程化)
  - [5.1 Go Modules](#51-go-modules)
  - [5.2 测试与基准](#52-测试与基准)
  - [5.3 常用标准库](#53-常用标准库)
  - [5.4 HTTP 服务与优雅退出](#54-http-服务与优雅退出)
  - [5.5 项目布局建议](#55-项目布局建议)
  - [5.6 性能分析 pprof](#56-性能分析-pprof)
- [第 6 章 运行时原理与进阶](#第-6-章-运行时原理与进阶)
  - [6.1 GMP 调度模型](#61-gmp-调度模型)
  - [6.2 垃圾回收（GC）](#62-垃圾回收gc)
  - [6.3 逃逸分析](#63-逃逸分析)
  - [6.4 内存模型与 happens-before](#64-内存模型与-happens-before)
  - [6.5 运行时的其他要点](#65-运行时的其他要点)
- [第 7 章 微服务与 trpc-go 入门](#第-7-章-微服务与-trpc-go-入门)
  - [7.1 RPC 基础](#71-rpc-基础)
  - [7.2 gRPC 开发流程](#72-grpc-开发流程)
  - [7.3 trpc-go](#73-trpc-go)
  - [7.4 微服务通用实践](#74-微服务通用实践)
  - [7.5 结合场景](#75-结合场景)
- [第 8 章 综合实战：并发 URL 检查器](#第-8-章-综合实战并发-url-检查器)
  - [第 1 步：定义结果与单个检查](#第-1-步定义结果与单个检查)
  - [第 2 步：带并发度限制的批量检查](#第-2-步带并发度限制的批量检查)
  - [第 3 步：组装入口](#第-3-步组装入口)
  - [第 4 步：验证与改进](#第-4-步验证与改进)
- [第 9 章 综合实战：构建工具调用 Agent](#第-9-章-综合实战构建工具调用-agent)
  - [第 1 步：定义消息与工具说明书](#第-1-步定义消息与工具说明书)
  - [第 2 步：封装 LLM 客户端](#第-2-步封装-llm-客户端)
  - [第 3 步：定义工具](#第-3-步定义工具)
  - [第 4 步：实现 Agent 主循环](#第-4-步实现-agent-主循环)
  - [第 5 步：组装入口并运行](#第-5-步组装入口并运行)
  - [第 6 步：不调用真实模型的测试](#第-6-步不调用真实模型的测试)
  - [第 7 步：验证与改进](#第-7-步验证与改进)
- [附录 A 速查表](#附录-a-速查表)
  - [A.1 语法速查](#a1-语法速查)
  - [A.2 并发安全检查清单](#a2-并发安全检查清单)
  - [A.3 版本特性一览](#a3-版本特性一览)
  - [A.4 学习路线与资料](#a4-学习路线与资料)
- [附录 B 各章练习题](#附录-b-各章练习题)

## 使用说明

本部分说明教材的定位、读法与环境准备，建议先通读，再动手实践。

#### TL;DR

Go 是一门为"大规模工程 + 高并发服务"而生的语言：语法极简、编译极快、并发是一等公民。本教材面向有 Python/C++ 基础、目标是做后端与微服务（含 trpc-go）的开发者，用 7 章把 Go 从语法讲到运行时原理，并配一个可运行的实战项目。

#### 本教材的读法

- 目标读者：具备 Python 或 C++ 经验的后端开发者
- 前置知识：变量、函数、指针、线程与锁的基本概念
- 技术栈版本：Go 1.22 及以上（文中示例在 Go 1.25 下实测通过）；标注"1.xx 起"的特性请留意版本
- 预计学习时间：每章 2 到 3 小时，全书约 3 周

每章结构统一：学习目标、核心内容、与 Python/C++ 的对比、常见坑、本章小结。建议每个代码块都亲手敲一遍并运行。

#### 环境准备

1. 从 go.dev/dl 下载安装 Go，执行 `go version` 确认版本。
2. 新建目录并初始化模块：`go mod init demo`。
3. 保存为 `main.go`，用 `go run .` 运行。
4. 编辑器推荐 VS Code + Go 插件，或 GoLand。

## 第 1 章 Go 语言概览

本章先从整体上认识 Go：它为何诞生、适合做什么，并完成第一个程序，熟悉工具链与代码组织方式。

#### 学习目标

- 理解 Go 的设计哲学与适用场景
- 能写出并运行第一个程序
- 掌握 Go 的工具链与代码组织方式

### 1.1 Go 是什么

Go 由 Google 的 Robert Griesemer、Rob Pike、Ken Thompson 设计，2009 年开源，2012 年发布 1.0。它要解决的是 Google 内部的工程痛点：C++ 编译慢、依赖复杂，Python 运行慢、并发弱，而服务端程序既要高性能又要容易维护。

Go 的核心特征可以浓缩为五点：

- **静态类型 + 编译为原生二进制**：编译快，部署时通常只需拷贝一个可执行文件。
- **自带垃圾回收**：不需要手动管理内存，GC 与程序并发运行，停顿通常在亚毫秒级。
- **并发内建**：goroutine 与 channel 是语言级特性，而不是库。
- **语法刻意保持小**：关键字只有 25 个，没有类继承、没有异常、没有运算符重载。
- **工具链统一**：格式化（`gofmt`）、测试（`go test`）、依赖管理（`go mod`）、性能分析（`pprof`）都是官方自带。

### 1.2 适合与不适合

| 场景 | 是否适合 | 原因 |
| --- | --- | --- |
| 微服务、RPC 网关、中间件 | 非常适合 | 高并发、部署简单、启动快 |
| 云原生基础设施（Docker、Kubernetes 均用 Go 编写） | 非常适合 | 生态成熟 |
| 命令行工具 | 适合 | 单文件分发，跨平台编译方便 |
| 机器学习训练与数值计算 | 不适合 | 生态集中在 Python/C++，Go 缺少成熟的张量库 |
| 极致低延迟、需精确控制内存 | 谨慎 | 有 GC，不如 C++/Rust 可控 |

### 1.3 第一个程序

```go
// main.go
package main

import "fmt"

func main() {
    fmt.Println("Hello, Go")
}
```

运行 `go run .`，预期输出：

```text
Hello, Go
```

这里有三个要点。`package main` 表示这是可执行程序的入口包；`import` 引入标准库的 `fmt`；`main` 函数是程序起点。Go 要求"导入了就必须使用，声明了局部变量就必须使用"，否则编译报错，这是在强制保持代码整洁。

### 1.4 包与模块

Go 的代码组织分两层：

- **包（package）**：同一目录下的所有 `.go` 文件属于同一个包。首字母**大写**的标识符对包外可见（导出），小写则仅包内可见。没有 `public/private` 关键字，大小写就是访问控制。
- **模块（module）**：一组包的集合，由根目录的 `go.mod` 描述，包含模块路径和依赖版本。

常用命令：

| 命令 | 作用 |
| --- | --- |
| `go run .` | 编译并运行 |
| `go build` | 编译生成可执行文件 |
| `go fmt ./...` | 格式化全部代码 |
| `go vet ./...` | 静态检查常见错误 |
| `go mod tidy` | 整理依赖，增删 `go.mod` 条目 |
| `go test ./...` | 运行所有测试 |

#### 与 Python/C++ 对比

| 维度 | Python | C++ | Go |
| --- | --- | --- | --- |
| 执行方式 | 解释执行 | 编译原生 | 编译原生 |
| 内存管理 | GC | 手动或 RAII | GC |
| 并发模型 | 线程受 GIL 限制 | 线程与锁 | goroutine 与 channel |
| 构建 | 无需构建 | CMake 等，复杂 | `go build`，一条命令 |
| 部署 | 需环境与依赖 | 需动态库 | 常为单个静态二进制 |

#### 常见坑

- 误以为 `:=` 能在函数外使用。包级变量必须用 `var` 声明。
- 把项目放在 `GOPATH` 下才能编译。这是旧做法，现在使用 Go Modules，任意目录均可。
- 格式不统一。直接用 `gofmt`，团队不用争论风格。

#### 本章小结

Go 的价值在"简单、可部署、会并发"。语法小，工具链全，是做服务端的务实选择。

## 第 2 章 基础语法

本章讲解 Go 的基础语法。内容看似简单，但切片共享、`defer` 求值时机等细节正是新手最容易出错的地方，请结合代码逐一验证。

#### 学习目标

- 熟练使用变量、常量与基本类型
- 掌握控制流（`if`、`for`、`switch`）与函数特性
- 理解数组、切片、map 的底层行为，尤其是切片的共享与扩容
- 正确使用指针与 `defer`

### 2.1 变量、常量与零值

```go
var a int           // 零值 0
var s string        // 零值 ""
b := 10             // 短声明，仅限函数内，类型推断为 int
const Pi = 3.14159  // 常量

const (
    Read = iota // 0
    Write       // 1
    Exec        // 2
)
```

Go 的每种类型都有**零值**：数字为 0，布尔为 `false`，字符串为 `""`，指针、切片、map、channel、接口、函数为 `nil`。因此"变量未初始化"这种状态在 Go 里不存在，这让许多代码可以省去初始化步骤。

基本类型：`int`/`int64`/`uint8` 等整型，`float32`/`float64`，`bool`，`string`，`byte`（即 `uint8`），`rune`（即 `int32`，表示一个 Unicode 码点）。`string` 是不可变的字节序列，`len(s)` 返回字节数而不是字符数；需要按字符遍历时，`for _, r := range s` 得到的是 `rune`。

类型之间**没有隐式转换**，`int` 与 `int64` 相加必须显式写 `int64(x)`。

### 2.2 控制流

Go 只有一种循环关键字 `for`：

```go
for i := 0; i < 3; i++ { }          // 经典形式
for cond { }                        // 相当于 while
for { }                             // 无限循环
for i, v := range []int{7, 8} { }   // 遍历切片，得到下标与值
for i := range 3 { }                // Go 1.22 起：整数 range，i 为 0,1,2
```

`if` 可以带一个初始化语句，作用域仅限该 `if`，这是 Go 错误处理的惯用写法：

```go
if v, err := strconv.Atoi("42"); err != nil {
    return err
} else {
    fmt.Println(v)
}
```

`switch` 不需要 `break`，匹配到一个分支就结束；需要穿透时才写 `fallthrough`。`switch` 后面可以不带表达式，等价于一串 `if-else if`。

### 2.3 函数

函数支持多返回值、命名返回值、可变参数与闭包，函数本身也是一等公民，可以作为参数和返回值。

```go
func divmod(a, b int) (q, r int, err error) {
    if b == 0 {
        err = fmt.Errorf("division by zero")
        return // 裸返回，返回命名结果的当前值
    }
    return a / b, a % b, nil
}
```

调用 `divmod(7, 2)` 返回 `3 1 <nil>`。命名返回值适合短函数，函数较长时建议显式写出返回值，避免可读性下降。

### 2.4 defer

`defer` 把一个函数调用推迟到**外层函数返回前**执行，多个 `defer` 按后进先出（LIFO）顺序执行。它是 Go 版的 RAII，常用于释放资源：

```go
f, err := os.Open("data.txt")
if err != nil {
    return err
}
defer f.Close() // 无论后面如何返回，都会关闭文件
```

两个必须记住的规则：

1. **参数在 `defer` 语句执行时就被求值**，而不是在真正调用时。
2. 在循环中使用 `defer` 要小心，它们要等到函数结束才执行，大循环可能导致资源长期占用。

### 2.5 数组、切片与 map

**数组**长度固定，是值类型，赋值时会整体拷贝，实际开发中很少直接使用。

**切片（slice）** 是 Go 最常用的序列类型。它不是数组本身，而是一个三元组：指向底层数组的指针、长度 `len`、容量 `cap`。

```go
a := []int{1, 2, 3}
b := a[:2]          // b 与 a 共享同一个底层数组
b = append(b, 99)   // 容量够用，直接覆盖 a[2]
fmt.Println(a, b)   // [1 2 99] [1 2 99]
```

这个例子是 Go 新手必踩的坑：`b` 的 `append` 修改了 `a` 的数据。原因是 `b` 的容量为 3，追加没有触发扩容，因此仍然写入同一个底层数组。

扩容规则：容量不足时，`append` 会分配新数组并拷贝旧数据。小切片容量大致翻倍，超过 256 个元素后增长因子逐渐降到约 1.25 倍。在 Go 1.25 上从空切片逐个追加 2000 个元素，容量依次为：

```text
2 4 8 16 32 64 128 256 512 848 1280 1792 2560
```

具体数字取决于版本和内存对齐，不要依赖。实践建议：**已知大小时用 `make([]T, 0, n)` 预分配容量**，避免反复扩容；需要独立副本时用 `slices.Clone` 或 `copy`。

**map** 是哈希表：

```go
m := map[string]int{"a": 1}
m["b"] = 2
v, ok := m["c"]   // 逗号 ok 惯用法：ok 为 false 表示不存在
delete(m, "a")
```

注意：遍历 map 的顺序**故意随机**，不能依赖；对 `nil` map 读取返回零值，但**写入会 panic**；map 的 key 必须是可比较类型（切片、map、函数不行）。

### 2.6 指针

Go 有指针，但**没有指针运算**。`&x` 取地址，`*p` 解引用，`new(T)` 返回 `*T`。

```go
func inc(p *int) { *p++ }

x := 1
inc(&x) // x 变为 2
```

Go 的参数传递永远是**值传递**。传切片、map、channel 看起来像引用，是因为它们内部包含指针，拷贝的只是那个小结构。理解这一点，才能解释为什么在函数里对切片 `append` 后，调用方的切片长度没变。

#### 与 Python/C++ 对比

| 点 | Python | C++ | Go |
| --- | --- | --- | --- |
| 循环 | `for`、`while` | `for`、`while`、`do` | 只有 `for` |
| 资源释放 | `with` | 析构函数 | `defer` |
| 动态数组 | `list` | `std::vector` | slice（语义接近 vector，但有共享陷阱） |
| 字典 | `dict`（保序） | `unordered_map` | `map`（遍历随机） |
| 未初始化变量 | 不存在 | 未定义值 | 一律为零值 |
| 指针运算 | 无指针 | 支持 | 不支持 |

#### 常见坑

- 切片共享底层数组导致"意外修改"：需要隔离时拷贝。
- 对 `nil` map 写入 panic：使用前 `make`。
- 遍历 map 顺序随机：需要稳定顺序时先取 key 排序。
- `defer` 在循环里堆积：把循环体放进独立函数。
- `string` 的 `len` 是字节数：中文字符占 3 字节。

#### 本章小结

掌握"零值、切片三元组、值传递、`defer` 求值时机"这四个概念，基础语法就过关了。

## 第 3 章 类型系统

本章讲解 Go 的类型系统。Go 没有类与继承，却用 struct、interface 与组合提供了同样强大的抽象能力。

#### 学习目标

- 用 `struct` 与方法建模，理解值接收者与指针接收者
- 理解 interface 的隐式实现与"接口值为 nil"的陷阱
- 掌握 Go 的错误处理范式与 `errors.Is/As`
- 会使用泛型编写通用函数

### 3.1 struct 与方法

Go 没有 `class`。数据用 `struct` 定义，行为用**方法**（带接收者的函数）绑定：

```go
type Rect struct{ W, H float64 }

func (r Rect) Area() float64 { return r.W * r.H }   // 值接收者

type Counter struct{ n int }

func (c *Counter) Inc() { c.n++ }                   // 指针接收者
```

选择接收者类型的经验规则：

- 方法需要**修改**接收者，或结构体较大（拷贝成本高），用指针接收者。
- 同一个类型的方法，**要么全部用指针接收者，要么全部用值接收者**，不要混用。
- 值类型的变量可以直接调用指针方法（编译器自动取地址），但值类型存入接口时，方法集只包含值接收者方法，这是下一节的重点。

### 3.2 组合代替继承

Go 用**嵌入（embedding）** 实现代码复用：

```go
type Animal struct{ Name string }

func (a Animal) Speak() string { return a.Name + " makes a sound" }

type Dog struct {
    Animal        // 嵌入，Dog 自动获得 Animal 的字段与方法
    Breed string
}

d := Dog{Animal{"Rex"}, "Lab"}
fmt.Println(d.Speak(), d.Name) // Rex makes a sound Rex
```

这不是继承：`Dog` 不是 `Animal` 的子类型，不能把 `Dog` 传给要求 `Animal` 参数的函数。它只是编译器帮你做了方法"提升"。设计思路是"是什么"用接口表达，"有什么"用组合表达。

### 3.3 interface

接口是**方法签名的集合**，实现是**隐式**的：只要类型拥有接口要求的全部方法，就自动满足，不需要 `implements` 声明。

```go
type Shape interface{ Area() float64 }

var s Shape = Rect{3, 4}
fmt.Println(s.Area()) // 12
```

这带来两个好处：接口可以在**使用方**定义，而不必由实现方预先声明；第三方类型也能满足你自己定义的接口。Go 的名言是"接受接口，返回结构体"，并且接口应当**小**，标准库的 `io.Reader` 只有一个方法。

空接口 `any`（即 `interface{}`）可以保存任意值。取出具体类型要用类型断言或类型分支：

```go
switch v := x.(type) {
case int:
    fmt.Println("int", v)
case string:
    fmt.Println("string", v)
default:
    fmt.Println("other")
}
```

**接口值为 nil 的陷阱**：接口内部由"动态类型 + 动态值"两部分组成，只有二者都为空，接口才等于 `nil`。

```go
type MyErr struct{}

func (*MyErr) Error() string { return "x" }

func mayFail() error {
    var p *MyErr // 值为 nil 的指针
    return p     // 接口的类型部分是 *MyErr，不为空
}

fmt.Println(mayFail() == nil) // false
```

结果是 `false`，调用方 `if err != nil` 会误判为出错。正确做法是：没有错误时直接 `return nil`，不要返回类型化的 nil 指针。

### 3.4 错误处理

Go 没有异常，`error` 是一个普通接口，函数把错误作为最后一个返回值：

```go
data, err := os.ReadFile("conf.json")
if err != nil {
    return fmt.Errorf("read conf: %w", err) // %w 包装，保留错误链
}
```

这种写法啰嗦，但好处是**错误路径在代码中一目了然**。几个关键工具：

- `errors.New` 创建哨兵错误，如 `var ErrNotFound = errors.New("not found")`。
- `fmt.Errorf("...: %w", err)` 包装错误并附加上下文。
- `errors.Is(err, target)` 沿错误链判断是否是某个特定错误，替代 `==` 比较。
- `errors.As(err, &target)` 沿错误链提取某个具体类型的错误，取出其字段。
- `errors.Join`（1.20 起）合并多个错误。

自定义错误类型并支持链式判断：

```go
var ErrNotFound = errors.New("not found")

type QueryError struct {
    Key string
    Err error
}

func (e *QueryError) Error() string {
    return "query " + e.Key + ": " + e.Err.Error()
}
func (e *QueryError) Unwrap() error { return e.Err }

err := fmt.Errorf("handler: %w", &QueryError{Key: "k1", Err: ErrNotFound})
var qe *QueryError
fmt.Println(errors.Is(err, ErrNotFound), errors.As(err, &qe), qe.Key)
// true true k1
```

`panic` 用于程序无法继续的情况（如不可恢复的编程错误），`recover` 只能在 `defer` 函数中捕获 panic。业务错误一律用 `error` 返回，不要把 `panic` 当异常使用。

### 3.5 泛型

Go 1.18 起支持泛型，用方括号声明类型参数，用**约束**限制可用类型：

```go
type Number interface{ ~int | ~int64 | ~float64 }

func Sum[T Number](xs []T) T {
    var s T
    for _, x := range xs {
        s += x
    }
    return s
}

func Map[T, U any](xs []T, f func(T) U) []U {
    out := make([]U, 0, len(xs))
    for _, x := range xs {
        out = append(out, f(x))
    }
    return out
}
```

调用 `Sum([]float64{1.5, 2.5})` 得到 `4`，`Map([]int{1, 2}, ...)` 可以做类型转换。`~int` 表示"底层类型为 int 的所有类型"。

使用建议：泛型适合**容器与通用算法**（如切片、map 工具），不要为了"优雅"而滥用。标准库的 `slices` 与 `maps`（1.21 起）已经提供了排序、查找、克隆等常用泛型函数，优先使用它们。

#### 与 Python/C++ 对比

| 点 | Python | C++ | Go |
| --- | --- | --- | --- |
| 多态 | 鸭子类型，运行时检查 | 虚函数、模板 | 隐式接口，编译期检查 |
| 复用 | 继承 | 继承 | 嵌入与组合 |
| 错误处理 | 异常 | 异常或错误码 | 返回 `error` |
| 泛型 | 动态类型天然通用 | 模板（编译期展开） | 类型参数 + 约束（1.18 起） |

#### 常见坑

- 值接收者方法无法修改原对象：需要修改就用指针接收者。
- 把类型化的 nil 指针当作 `error` 返回，导致 `err != nil` 为真。
- 用 `==` 比较被包装过的错误：改用 `errors.Is`。
- 在接口里放大量方法：接口越小越好用。

#### 本章小结

Go 的类型系统可以概括为：struct 承载数据，方法绑定行为，interface 解耦依赖，error 显式传递失败，泛型消除重复。

## 第 4 章 并发编程

> 这是 Go 最有特色的部分，也是后端面试和线上故障的高发区，请投入最多时间。

#### 学习目标

- 理解 goroutine 与线程的区别
- 熟练使用 channel、`select`、`sync` 包
- 用 `context` 实现取消与超时
- 能识别并避免 goroutine 泄漏、数据竞争、死锁

### 4.1 goroutine

在函数调用前加 `go`，就启动了一个 goroutine：

```go
go doSomething()
go func() { fmt.Println("in goroutine") }()
```

goroutine 是由 Go 运行时调度的**轻量级协程**，初始栈约 2KB 并可按需增长，创建和切换成本远低于操作系统线程，同时存在几十万个也是常态。需要注意：`main` 函数返回时，程序立即退出，不会等待其他 goroutine，所以必须用同步机制等待它们完成。

### 4.2 channel

Go 的并发哲学是："**不要通过共享内存来通信，而要通过通信来共享内存**。"channel 就是 goroutine 之间传递数据的管道。

```go
ch := make(chan int)        // 无缓冲：发送与接收必须同时就绪（同步）
bch := make(chan int, 10)   // 有缓冲：缓冲区未满时发送不阻塞

go func() { ch <- 42 }()
fmt.Println(<-ch) // 42

close(ch)         // 只有发送方应当关闭
```

channel 的行为规则需要熟记：

| 操作 | nil channel | 已关闭 channel | 正常 channel |
| --- | --- | --- | --- |
| 发送 | 永久阻塞 | panic | 可能阻塞 |
| 接收 | 永久阻塞 | 立即返回零值，ok 为 false | 可能阻塞 |
| 关闭 | panic | panic | 正常 |

`for v := range ch` 会持续接收，直到 channel 被关闭。单向 channel 类型 `chan<- int`（只发）与 `<-chan int`（只收）用于在函数签名里表达意图。

### 4.3 select

`select` 同时等待多个 channel 操作，哪个先就绪就执行哪个，常用于超时与取消：

```go
select {
case v := <-ch:
    fmt.Println("got", v)
case <-time.After(50 * time.Millisecond):
    fmt.Println("timeout")
}
```

带 `default` 分支的 `select` 是非阻塞操作。注意在循环里反复使用 `time.After` 会不断创建定时器，长期运行的循环更推荐复用 `time.Timer`。

### 4.4 sync 包

channel 并不是万能的。保护共享状态时，锁往往更直接：

```go
var mu sync.Mutex
cnt := 0
var wg sync.WaitGroup
for i := 0; i < 1000; i++ {
    wg.Add(1)
    go func() {
        defer wg.Done()
        mu.Lock()
        cnt++
        mu.Unlock()
    }()
}
wg.Wait()
fmt.Println(cnt) // 1000
```

常用组件：

| 组件 | 用途 |
| --- | --- |
| `Mutex` / `RWMutex` | 互斥锁与读写锁，读多写少用后者 |
| `WaitGroup` | 等待一组 goroutine 结束 |
| `Once` | 保证初始化只执行一次 |
| `sync/atomic` | 无锁的原子计数与标志位 |
| `sync.Pool` | 对象池，降低 GC 压力 |
| `sync.Map` | 并发安全的 map，适合读多写少或 key 集合稳定的场景 |

锁和 `WaitGroup` 都**不能被拷贝**，传参时用指针。运行 `go test -race` 或 `go run -race` 可以检测数据竞争，线上之前务必跑一遍。

### 4.5 context

`context.Context` 用于在调用链上传递**取消信号、截止时间和请求级元数据**。几乎所有服务端代码、数据库驱动和 RPC 框架都以它作为第一个参数。

```go
ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)
defer cancel() // 必须调用，释放资源

select {
case <-ctx.Done():
    fmt.Println(ctx.Err()) // context deadline exceeded
case res := <-doWork(ctx):
    fmt.Println(res)
}
```

使用规范：

1. `ctx` 作为函数的**第一个参数**，命名为 `ctx`。
2. 不要把 `ctx` 存进结构体，随调用链显式传递。
3. 创建带取消的 `ctx` 后，务必 `defer cancel()`。
4. `context.Value` 只放请求级数据（如 trace id），不要用来传业务参数。

### 4.6 经典模式：worker pool

下面是一个完整可运行的 worker pool：3 个 worker 并发处理任务，支持通过 `ctx` 取消：

```go
func worker(ctx context.Context, jobs <-chan int,
    results chan<- int, wg *sync.WaitGroup) {
    defer wg.Done()
    for {
        select {
        case <-ctx.Done():
            return
        case j, ok := <-jobs:
            if !ok {
                return // jobs 已关闭，正常退出
            }
            results <- j * j
        }
    }
}

func main() {
    ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)
    defer cancel()
    jobs := make(chan int)
    results := make(chan int, 100)
    var wg sync.WaitGroup
    for i := 0; i < 3; i++ {
        wg.Add(1)
        go worker(ctx, jobs, results, &wg)
    }
    go func() {
        for i := 1; i <= 5; i++ {
            jobs <- i
        }
        close(jobs)
    }()
    wg.Wait()
    close(results)
    sum := 0
    for r := range results {
        sum += r
    }
    fmt.Println("sum", sum) // 55
}
```

这里的关键设计：任务由发送方关闭 `jobs`；结果 channel 带缓冲，避免 worker 阻塞；`wg.Wait()` 之后才 `close(results)`，保证不会向已关闭的 channel 写入。

#### 与 Python/C++ 对比

| 点 | Python | C++ | Go |
| --- | --- | --- | --- |
| 并发单位 | 线程（GIL）、asyncio 协程 | 线程 | goroutine |
| 线程通信 | `queue.Queue` | 条件变量、队列 | channel |
| 取消机制 | `asyncio.CancelledError` | 自行实现 | `context` |
| 竞态检测 | 无内置 | TSan | `-race` 内置 |
| 异步写法 | `async/await` 有函数着色问题 | 回调或协程 | 同步写法，运行时调度 |

Go 最大的差别是：代码**写成同步阻塞的样子**，由运行时把阻塞转换为调度，不存在 `async/await` 的"函数染色"。

#### 常见坑

- **goroutine 泄漏**：goroutine 阻塞在永远没人收发的 channel 上，永不退出。每个 goroutine 都要有明确的退出条件，并用 `ctx` 兜底。
- **向已关闭的 channel 发送会 panic**：只由发送方关闭，且只关一次。
- **map 并发读写会触发 fatal error**，不能 `recover`：用锁或 `sync.Map` 保护。
- **循环变量捕获**：Go 1.22 之前，`for i := ...` 的 `i` 在所有迭代中共享同一个变量，闭包会捕获到最终值；1.22 起每次迭代都有独立变量。如果 `go.mod` 声明的版本低于 1.22，仍是旧行为。
- **死锁**：所有 goroutine 都在等待时，运行时报 `all goroutines are asleep - deadlock!`。加锁顺序要一致，避免嵌套持锁。
- **忘记 `cancel()`**：造成计时器与 goroutine 资源泄露。

#### 本章小结

并发的核心是三件事：用 channel 或锁**同步**，用 `context` **控制生命周期**，用 `-race` **验证正确性**。写之前先想清楚每个 goroutine 怎么结束。

## 第 5 章 工程化

本章把语言知识落到工程实践：依赖、测试、标准库、服务与性能分析，是从"会写"到"能上线"的关键一环。

#### 学习目标

- 使用 Go Modules 管理依赖，包括私有仓库
- 编写表驱动测试与基准测试
- 熟悉常用标准库，会写简单的 HTTP 服务
- 掌握日志、配置与优雅退出的基本实践

### 5.1 Go Modules

`go.mod` 记录模块路径、Go 版本与依赖，`go.sum` 记录依赖哈希以保证可复现：

```gomod
module example.com/demo

go 1.22

require github.com/google/uuid v1.6.0
```

常用操作：

| 命令 | 作用 |
| --- | --- |
| `go get pkg@version` | 添加或升级依赖 |
| `go mod tidy` | 同步依赖，移除未使用项 |
| `go mod vendor` | 把依赖拷贝到本地 `vendor/` |
| `go list -m all` | 查看全部依赖 |

**公司内网私有库**常见配置：设置 `GOPRIVATE=内部域名/*` 避免走公共代理与校验库，并配置内部 `GOPROXY`；本地联调未发布的依赖时，在 `go.mod` 中用 `replace` 指向本地路径。具体地址以公司文档为准。

模块遵循**语义化版本**；主版本号 2 及以上时，模块路径需要带 `/v2` 后缀。

### 5.2 测试与基准

测试文件以 `_test.go` 结尾，测试函数以 `Test` 开头。Go 社区的主流写法是**表驱动测试**：

```go
func TestAdd(t *testing.T) {
    tests := []struct {
        name string
        a, b int
        want int
    }{
        {"pos", 1, 2, 3},
        {"neg", -1, -2, -3},
    }
    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            if got := Add(tt.a, tt.b); got != tt.want {
                t.Errorf("Add(%d,%d)=%d, want %d", tt.a, tt.b, got, tt.want)
            }
        })
    }
}

func BenchmarkAdd(b *testing.B) {
    for i := 0; i < b.N; i++ {
        Add(1, 2)
    }
}
```

运行方式：

- `go test ./...`：运行全部测试
- `go test -run TestAdd -v`：只运行指定用例并显示详情
- `go test -bench . -benchmem`：运行基准并显示内存分配
- `go test -race -cover ./...`：开启竞态检测并统计覆盖率

接口让依赖易于替换：测试时传入伪造实现（mock 或 fake）即可，不需要重型框架。

### 5.3 常用标准库

| 包 | 用途 |
| --- | --- |
| `fmt`、`log`、`log/slog` | 格式化输出与结构化日志（`slog` 为 1.21 起） |
| `net/http` | HTTP 客户端与服务端 |
| `encoding/json` | JSON 编解码 |
| `io`、`bufio`、`os` | 输入输出与文件 |
| `time` | 时间与定时器 |
| `sort`、`slices`、`maps` | 排序与泛型工具 |
| `strings`、`strconv`、`bytes` | 字符串与字节处理 |
| `regexp` | 正则 |
| `flag` | 命令行参数 |

JSON 通过 struct tag 控制字段名，例如 `Msg string` 加上标签 `json:"msg"`。字段必须**首字母大写**才能被 `encoding/json` 访问。

### 5.4 HTTP 服务与优雅退出

Go 1.22 起，标准库路由支持方法和路径参数，小服务不需要第三方框架：

```go
mux := http.NewServeMux()
mux.HandleFunc("GET /hello/{name}",
    func(w http.ResponseWriter, r *http.Request) {
        w.Header().Set("Content-Type", "application/json")
        json.NewEncoder(w).Encode(resp{Msg: "hello " + r.PathValue("name")})
    })
srv := &http.Server{Addr: ":8080", Handler: mux}
go func() {
    if err := srv.ListenAndServe(); !errors.Is(err, http.ErrServerClosed) {
        log.Fatal(err)
    }
}()
ctx, stop := signal.NotifyContext(context.Background(),
    os.Interrupt, syscall.SIGTERM)
defer stop()
<-ctx.Done() // 等待退出信号
shutdownCtx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
defer cancel()
log.Println("shutdown:", srv.Shutdown(shutdownCtx))
```

`Shutdown` 会停止接收新连接并等待在途请求完成，超时则强制返回。**优雅退出**对容器化部署尤为重要，否则发布时会丢请求。

### 5.5 项目布局建议

```text
myservice/
  cmd/myservice/main.go   // 入口，只做组装
  internal/               // 私有代码，外部模块无法 import
    service/              // 业务逻辑
    store/                // 数据访问
  api/                    // 接口定义（proto、openapi）
  go.mod
```

`internal/` 目录由编译器保证：只有同一模块内的代码才能导入。不必照搬某个"标准布局"，按团队约定保持清晰即可。

### 5.6 性能分析 pprof

`net/http/pprof` 或 `runtime/pprof` 可以采集 CPU、堆内存、goroutine、阻塞和锁竞争的 profile：

```bash
go tool pprof -http=:9999 http://localhost:6060/debug/pprof/profile?seconds=30
go tool pprof http://localhost:6060/debug/pprof/heap
go tool pprof http://localhost:6060/debug/pprof/goroutine
```

排障套路：CPU 高看 `profile`；内存涨看 `heap`；goroutine 数持续增长看 `goroutine`，通常对应泄漏。`go tool trace` 可进一步观察调度与 GC 的时间线。

#### 与 Python/C++ 对比

| 点 | Python | C++ | Go |
| --- | --- | --- | --- |
| 依赖管理 | pip、poetry | CMake、vcpkg、conan | `go mod`，官方内置 |
| 测试框架 | pytest | gtest | 标准库 `testing` |
| 格式化 | black（可选） | clang-format（可选） | `gofmt`，统一强制 |
| 性能分析 | cProfile | perf、gprof | pprof，官方内置 |

#### 常见坑

- 忘记执行 `go mod tidy`，导致 CI 与本地依赖不一致。
- 测试里在 goroutine 内调用 `t.Fatal`：它只能在测试 goroutine 中调用。
- 自己启动的 `http.Client` 不设超时：默认无超时，下游变慢会拖垮自己。要设置 `Timeout`。
- 生产环境暴露 pprof 端口到公网。

#### 本章小结

Go 的工程化是"开箱即用"：模块、测试、基准、格式化、性能分析全部官方提供。养成"写代码就写测试、上线前跑 `-race`、出问题先 pprof"的习惯。

## 第 6 章 运行时原理与进阶

本章深入运行时。理解调度、GC 与逃逸分析，才能解释并解决线上常见的性能问题。

#### 学习目标

- 理解 GMP 调度模型
- 理解 GC 的基本原理与调优参数
- 理解逃逸分析与内存分配
- 了解 Go 内存模型的核心约定

### 6.1 GMP 调度模型

Go 运行时用三个角色调度 goroutine：

```text
G (goroutine)   待执行的任务，持有自己的栈与上下文
M (machine)     操作系统线程，真正执行代码
P (processor)   调度器上下文，持有本地运行队列；P 的数量 = GOMAXPROCS
```

运行规则：每个 M 必须绑定一个 P 才能执行 G；P 拥有一个本地可运行 G 队列，另外还有全局队列。默认 `GOMAXPROCS` 等于 CPU 核数。

几个关键机制：

- **Work stealing**：某个 P 的本地队列空了，会先查全局队列，再从其他 P 的队列"偷"一半任务，保证负载均衡。
- **系统调用处理**：G 进入阻塞的系统调用时，M 会和 P 解绑，P 去找其他 M 继续跑别的 G，不会让 CPU 闲着。
- **网络 I/O**：通过 netpoller（Linux 上基于 epoll）实现，阻塞的 G 会被挂起，而不占用线程。
- **抢占**：自 Go 1.14 起支持基于信号的异步抢占，一个死循环的 goroutine 也不会独占 P 导致其他 G 饿死。

容器部署的提示：在 Go 1.24 及更早版本中，`GOMAXPROCS` 默认读取宿主机的核数，在被 cgroup 限制 CPU 的容器里可能远大于实际配额，造成调度抖动和 CPU 限流，通常要借助 `automaxprocs` 之类的库或环境变量显式设置。Go 1.25 起运行时会感知 cgroup 的 CPU 限制并自动调整，但仍建议在你的运行环境里实测确认。

### 6.2 垃圾回收（GC）

Go 使用**并发的三色标记清除**算法，且不做内存整理（非移动式）：

- 三色标记：白（未访问）、灰（已发现，子对象待扫描）、黑（已扫描完成）。标记结束后仍为白色的对象就是垃圾。
- 并发：标记与清扫的大部分工作与业务 goroutine 同时进行，仅有极短的 stop-the-world 阶段。
- 写屏障：并发标记期间，业务代码修改指针时，运行时通过写屏障记录变化，保证不会漏标。

两个最重要的调优旋钮：

| 参数 | 含义 |
| --- | --- |
| `GOGC` | 堆增长比例，默认 100，即堆大小相对上次回收后翻倍时触发下一次 GC。调大则 GC 更少、内存占用更高 |
| `GOMEMLIMIT`（1.19 起） | 软内存上限，接近上限时 GC 会更积极，适合容器场景防止 OOM |

调优思路：**优先减少分配**，而不是先调参数。具体手段有：预分配切片与 map 容量、复用对象（`sync.Pool`）、避免不必要的字符串拼接和 `[]byte` 与 `string` 的转换。

### 6.3 逃逸分析

变量到底分配在栈上还是堆上，由编译器的**逃逸分析**决定，而不是由是否使用 `new` 决定。栈上分配随函数返回自动回收，几乎无成本；堆上分配则要经过 GC。

```go
func newP() *P { return &P{1, 2} } // 返回局部变量的地址，P 逃逸到堆
```

查看逃逸结果：

```bash
go build -gcflags=-m
# ./main.go:8:25: &P{...} escapes to heap
```

常见的逃逸原因：返回局部变量的指针、被闭包捕获并在函数外使用、赋值给 `interface` 类型（如传给 `fmt.Println`）、切片长度在编译期无法确定、发送到 channel 的指针。

不必对每个函数都做逃逸分析。**只在 pprof 显示分配热点时，再回头优化**，过早优化只会损害可读性。

### 6.4 内存模型与 happens-before

Go 内存模型规定：在没有同步的情况下，一个 goroutine 对变量的写入，**不保证**被另一个 goroutine 看到。要建立可见性，必须使用同步原语，常见的 happens-before 关系有：

- channel 的发送先于对应的接收完成。
- 对 channel 的关闭先于因关闭而返回的接收。
- `Mutex` 的 `Unlock` 先于后续的 `Lock`。
- `sync.Once` 中 `f` 的执行先于任何一次 `Do` 的返回。
- `atomic` 操作提供顺序一致的语义。

实用结论：**有数据竞争的程序行为未定义**，不要写"看起来没问题"的无锁代码，一律用 `-race` 检查。

### 6.5 运行时的其他要点

- **栈**：goroutine 栈初始很小，通过栈拷贝动态增长，因此不要依赖栈上变量的地址保持不变。
- **逃逸与内联**：编译器会对小函数做内联，可用 `-gcflags=-m` 观察。
- **反射与 unsafe**：`reflect` 灵活但慢，`unsafe` 绕过类型安全，二者都应当限制在少数基础库里。
- **cgo**：Go 调用 C 有额外开销并会增加部署复杂度，尽量避免在热点路径上使用。

#### 与 Python/C++ 对比

| 点 | Python | C++ | Go |
| --- | --- | --- | --- |
| 内存回收 | 引用计数 + 分代 GC | 手动、RAII | 并发三色标记清除 |
| 调优手段 | 少 | 完全自控 | `GOGC`、`GOMEMLIMIT`、减少分配 |
| 栈与堆 | 全在堆上 | 程序员决定 | 编译器逃逸分析决定 |
| 线程调度 | OS 线程 | OS 线程 | 用户态 GMP 调度 |

#### 常见坑

- 一味调大 `GOGC` 换低 GC 频率，却忽视容器内存上限引发 OOM：配合 `GOMEMLIMIT`。
- 在热路径上无意中产生大量小对象，导致 GC 压力。用 pprof 的 `alloc_space` 定位。
- 大 map 或大切片存放大量指针，会增加 GC 扫描成本。

#### 本章小结

GMP 解释了"为什么 goroutine 便宜"，GC 与逃逸分析解释了"为什么要少分配"。面对性能问题，流程应是：测量，定位热点，减少分配，最后才是调参。

## 第 7 章 微服务与 trpc-go 入门

本章把前面的知识放到微服务场景，介绍 RPC 的基本组成、gRPC 与 trpc-go 的开发流程，以及通用的可靠性实践。

#### 学习目标

- 理解 RPC 服务的基本组成
- 了解 gRPC 与 trpc-go 的开发流程
- 掌握微服务中的通用工程实践

### 7.1 RPC 基础

微服务之间通过 **RPC** 调用，其核心是：

1. 用 **IDL**（接口定义语言，如 Protocol Buffers）描述服务与消息。
2. 工具根据 IDL **生成**桩代码（客户端 stub 与服务端接口）。
3. 开发者实现服务端接口，客户端像调用本地函数一样发起调用。
4. 框架负责序列化、网络传输、服务发现、负载均衡、超时与重试、监控等。

一个典型的 proto 定义：

```protobuf
syntax = "proto3";
package demo;
option go_package = "example.com/demo/pb";

service Greeter {
  rpc SayHello (HelloReq) returns (HelloRsp);
}
message HelloReq { string name = 1; }
message HelloRsp { string msg = 2; }
```

### 7.2 gRPC 开发流程

gRPC 是业界通用的 RPC 框架，基于 HTTP/2 与 Protobuf。流程：编写 `.proto`，用 `protoc` 加 `protoc-gen-go`、`protoc-gen-go-grpc` 生成代码，实现服务接口，再注册到 `grpc.Server`。客户端通过 `grpc.NewClient` 建立连接，使用生成的 client 调用。每次调用都应传入带超时的 `ctx`。

### 7.3 trpc-go

tRPC 是腾讯开源的多语言 RPC 框架，trpc-go 是它的 Go 实现，在公司内部广泛使用。它在 RPC 之上提供了名字服务、负载均衡、过滤器（拦截器）、监控与调用链等能力，通过配置文件接入这些基础设施。

典型的开发步骤如下，具体命令与内部版本的导入路径请以公司文档为准：

1. **定义服务**：编写 `.proto`，描述 service 与 message。
2. **生成脚手架**：用 `trpc` 命令行工具生成服务端代码骨架、配置文件与 stub。
3. **实现业务逻辑**：实现生成的 service 接口，函数签名都形如 `func(ctx, req) (rsp, error)`。
4. **配置**：在 `trpc_go.yaml` 中配置服务名、监听地址、协议、日志、名字服务（如 Polaris）等。
5. **启动**：入口代码很简短：

```go
func main() {
    s := trpc.NewServer()                 // 读取配置并创建 server
    pb.RegisterGreeterService(s.Service("demo.Greeter"), &greeterImpl{})
    if err := s.Serve(); err != nil {
        log.Fatal(err)
    }
}
```

客户端使用生成的 `NewGreeterClientProxy()`，调用时传入 `ctx` 与请求，目标服务通过名字服务解析，而不是写死地址。

注意：上面只是结构示意，真实项目中包路径、`Register` 的入参形式随版本略有差异，请以生成器产出的代码为准。

### 7.4 微服务通用实践

| 主题 | 实践要点 |
| --- | --- |
| 超时 | 每次下游调用都设置超时，且上游超时应大于下游，避免链路雪崩 |
| 重试 | 只对幂等操作重试，加退避与上限 |
| 错误码 | 区分业务错误与系统错误，使用统一的错误码规范 |
| 日志 | 使用结构化日志，带上 trace id |
| 监控 | 统计 QPS、耗时分位数（P99）、错误率 |
| 限流熔断 | 保护自己，也保护下游 |
| 配置 | 配置与代码分离，支持热加载 |
| 优雅退出 | 先摘除流量，再等待在途请求完成 |

### 7.5 结合场景

如果日常接触的推荐与广告在线链路，本质上是"一个请求扇出到多个下游（特征服务、召回、排序、预估），在严格的 RT 预算内汇总返回"。这正是 Go 的强项：

- 用 goroutine 并行拉取多路特征，用 `errgroup` 或 `WaitGroup` 汇总，用 `ctx` 统一控制超时。
- 用 `sync.Pool` 复用请求与特征缓冲，降低 GC 抖动。
- 用 pprof 与 trace 定位长尾延迟。

模型推理本身仍然适合交给专用的推理服务（C++/GPU），Go 侧负责编排与协议转换。

#### 常见坑

- 不传递 `ctx`，导致上游已超时，下游仍在白白计算。
- 无限制地并发扇出，打爆下游：用带缓冲 channel 或信号量限制并发度。
- 把 `ctx` 里的超时当成"一定会取消 CPU 计算"：取消只是一个信号，计算代码要主动检查 `ctx.Done()`。

#### 本章小结

微服务是"IDL 驱动 + 框架治理"。Go 在其中负责高效编排。掌握 `ctx`、超时、重试和优雅退出，就掌握了服务可靠性的大半。

## 第 8 章 综合实战：并发 URL 检查器

本章用一个小项目串联前面所学。建议先自己独立实现，再对照示例代码。

#### 项目目标

实现一个命令行工具：并发检查一批 URL 是否可访问，限制并发度，设置全局超时，汇总统计结果。它综合运用了 goroutine、channel、`sync`、`context` 与 `net/http`。

### 第 1 步：定义结果与单个检查

```go
type Result struct {
    URL    string
    Status int
    Err    error
}

func check(ctx context.Context, url string) Result {
    req, err := http.NewRequestWithContext(ctx, http.MethodGet, url, nil)
    if err != nil {
        return Result{URL: url, Err: err}
    }
    resp, err := http.DefaultClient.Do(req)
    if err != nil {
        return Result{URL: url, Err: err}
    }
    defer resp.Body.Close()
    return Result{URL: url, Status: resp.StatusCode}
}
```

要点：用 `NewRequestWithContext` 让请求可被取消；`defer resp.Body.Close()` 防止连接泄漏。

### 第 2 步：带并发度限制的批量检查

```go
func checkAll(ctx context.Context, urls []string, limit int) []Result {
    results := make([]Result, len(urls))
    sem := make(chan struct{}, limit) // 信号量：容量即最大并发数
    var wg sync.WaitGroup
    for i, u := range urls {
        wg.Add(1)
        sem <- struct{}{} // 获取令牌，满了就阻塞
        go func() {
            defer wg.Done()
            defer func() { <-sem }() // 归还令牌
            results[i] = check(ctx, u)
        }()
    }
    wg.Wait()
    return results
}
```

设计说明：用带缓冲的 channel 当信号量，是 Go 里限制并发度的常用手法；每个 goroutine 只写自己下标的 `results[i]`，不同 goroutine 访问不同元素，因此不需要加锁；`i` 和 `u` 在 Go 1.22 起每次迭代独立，闭包可以直接使用。

### 第 3 步：组装入口

```go
func main() {
    urls := []string{
        "https://go.dev", "https://example.com", "https://nonexistent.invalid",
    }
    ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
    defer cancel()
    ok, fail := 0, 0
    for _, r := range checkAll(ctx, urls, 2) {
        if r.Err != nil || r.Status >= 400 {
            fail++
            fmt.Printf("FAIL %s: %v (status %d)\n", r.URL, r.Err, r.Status)
            continue
        }
        ok++
        fmt.Printf("OK   %s: %d\n", r.URL, r.Status)
    }
    fmt.Printf("ok=%d fail=%d\n", ok, fail)
}
```

运行结果取决于网络环境，预期会看到前两个 URL 返回 200，最后一个因域名无法解析而失败。

### 第 4 步：验证与改进

1. 用 `go run -race .` 验证没有数据竞争。
2. 为 `checkAll` 编写测试：用 `net/http/httptest` 启动本地假服务，避免依赖外网。
3. 改进方向：加入重试与退避；使用 `errgroup` 取代手写 `WaitGroup`；把结果以 JSON 输出；增加 `-c`（并发度）、`-t`（超时）命令行参数。
4. 进阶挑战：把它改造为 HTTP 服务，参照第 5 章加入优雅退出；再用 trpc-go 把检查能力暴露成一个 RPC 接口。

## 第 9 章 综合实战：构建工具调用 Agent

本章用一个完整项目串联前面所学：从零写一个能调用工具的 LLM Agent。建议先自己独立实现，再对照示例代码。完整可运行的源码随教材附带，位于 `code/agent/` 目录，本章各步骤的代码都来自这些文件（为节省篇幅，省略了每个文件开头的 `package` 与 `import`，编辑器可自动补全）。

### 项目目标

实现一个命令行 Agent：接收用户的问题，调用大模型；模型需要外部信息时会要求调用工具（示例是查天气），Agent 负责并行执行这些工具，把结果交还给模型，直到模型给出最终答案。

Agent 的本质就是下面这个循环，没有更多魔法：

```text
用户输入 -> 调用 LLM -> 模型要调工具吗？
                         要 -> 执行工具(并行) -> 结果追加进历史 -> 回到"调用 LLM"
                         不要 -> 把模型回复作为最终答案
```

模型本身不会执行任何代码，它只会返回"我想调用 `get_weather`，参数是 `{"city":"深圳"}`"。真正执行的是你的 Go 程序。所以 Agent 开发的工作量集中在：消息结构、工具抽象、循环控制、错误处理，以及并发与超时。

本项目用到的前面章节知识如下：

| 知识点                     | 在项目中的作用                   | 章节      |
| ----------------------- | ------------------------- | ------- |
| interface               | 抽象 `LLM` 与 `Tool`，便于替换与测试 | 3.3     |
| error 与 `%w`            | 包装错误、区分是否可重试              | 3.4     |
| JSON 标签                 | 与大模型接口收发数据                | 5.3     |
| `net/http` 与超时          | 调用模型接口                    | 5.3、5.4 |
| goroutine 与 `WaitGroup` | 并行执行同一轮的多个工具调用            | 4.1、4.4 |
| `context`               | 超时与取消                     | 4.5     |
| `httptest` 与表驱动测试       | 不依赖真实模型的测试                | 5.2     |

模型接口采用 OpenAI 兼容的 `/chat/completions` 协议，换一个 `base_url` 就能接入其他兼容该协议的厂商。项目结构：

```text
agent/
  types.go       消息与工具说明书的数据结构
  client.go      LLM 接口与 OpenAI 兼容客户端
  tool.go        Tool 接口与示例工具
  agent.go       Agent 主循环
  main.go        入口
  agent_test.go  用 httptest 伪造模型服务的测试
  go.mod
```

### 第 1 步：定义消息与工具说明书

先把协议里的数据结构用 struct 表达出来：

```go
// types.go
// Message 对应 OpenAI 兼容接口里的一条对话消息
type Message struct {
    Role       string     `json:"role"` // system / user / assistant / tool
    Content    string     `json:"content,omitempty"`
    ToolCalls  []ToolCall `json:"tool_calls,omitempty"`   // assistant 发起的工具调用
    ToolCallID string     `json:"tool_call_id,omitempty"` // tool 消息对应哪次调用
}

type ToolCall struct {
    ID       string       `json:"id"`
    Type     string       `json:"type"`
    Function FunctionCall `json:"function"`
}

type FunctionCall struct {
    Name      string `json:"name"`
    Arguments string `json:"arguments"` // 注意：是 JSON 字符串，不是对象
}

// ToolSpec 是发给模型的工具说明书
type ToolSpec struct {
    Type     string  `json:"type"`
    Function FuncDef `json:"function"`
}

type FuncDef struct {
    Name        string          `json:"name"`
    Description string          `json:"description"`
    Parameters  json.RawMessage `json:"parameters"` // JSON Schema，原样透传
}
```

这里有三个要点，都源于第 5.3 节的 JSON 知识：

- `Arguments` 是一个**包着 JSON 的字符串**，不是 JSON 对象。模型返回的工具参数形如 `"{\"city\":\"深圳\"}"`，需要自己再 `json.Unmarshal` 一次。
- `Parameters` 是 JSON Schema，结构多变，没必要逐个建模，用 `json.RawMessage` 原样透传即可。
- `Content` 加了 `omitempty`：模型发起工具调用时内容为空，序列化时就不应带上这个字段。

### 第 2 步：封装 LLM 客户端

先定义接口，主循环只依赖接口，不依赖具体厂商：

```go
// client.go
// LLM 抽象成接口：生产用真实客户端，测试用 mock
type LLM interface {
    Chat(ctx context.Context, msgs []Message, tools []ToolSpec) (Message, error)
}

type OpenAIClient struct {
    BaseURL, APIKey, Model string
    HTTP                   *http.Client
}

type chatReq struct {
    Model    string     `json:"model"`
    Messages []Message  `json:"messages"`
    Tools    []ToolSpec `json:"tools,omitempty"`
}
```

`Chat` 负责重试策略：

```go
// client.go
func (c *OpenAIClient) Chat(ctx context.Context, msgs []Message, tools []ToolSpec) (Message, error) {
    body, err := json.Marshal(chatReq{Model: c.Model, Messages: msgs, Tools: tools})
    if err != nil {
        return Message{}, err
    }
    var lastErr error
    for attempt := 0; attempt < 3; attempt++ {
        if attempt > 0 { // 退避重试：1s、2s
            select {
            case <-time.After(time.Duration(attempt) * time.Second):
            case <-ctx.Done():
                return Message{}, ctx.Err()
            }
        }
        msg, retry, err := c.once(ctx, body)
        if err == nil {
            return msg, nil
        }
        lastErr = err
        if !retry {
            break
        }
    }
    return Message{}, lastErr
}
```

`once` 发出一次请求，并告诉调用方这个错误值不值得重试：

```go
// client.go
// once 发一次请求；retry 表示这个错误值得重试（429 / 5xx）
func (c *OpenAIClient) once(ctx context.Context, body []byte) (Message, bool, error) {
    req, err := http.NewRequestWithContext(ctx, http.MethodPost,
        c.BaseURL+"/chat/completions", bytes.NewReader(body))
    if err != nil {
        return Message{}, false, err
    }
    req.Header.Set("Content-Type", "application/json")
    req.Header.Set("Authorization", "Bearer "+c.APIKey)
    resp, err := c.HTTP.Do(req)
    if err != nil {
        return Message{}, true, err
    }
    defer resp.Body.Close()
    data, _ := io.ReadAll(resp.Body)
    if resp.StatusCode != http.StatusOK {
        retry := resp.StatusCode == 429 || resp.StatusCode >= 500
        return Message{}, retry, fmt.Errorf("llm status %d: %s", resp.StatusCode, data)
    }
    var out struct {
        Choices []struct {
            Message Message `json:"message"`
        } `json:"choices"`
    }
    if err := json.Unmarshal(data, &out); err != nil || len(out.Choices) == 0 {
        return Message{}, false, fmt.Errorf("bad llm response: %s", data)
    }
    return out.Choices[0].Message, false, nil
}
```

设计说明：

1. 用 `NewRequestWithContext`，请求能被取消和超时。
2. 只重试**网络错误、429（限流）和 5xx**；其他 4xx（参数错误、鉴权失败）重试没有意义。
3. 退避等待时用 `select` 同时监听 `ctx.Done()`，上游一取消就立刻退出，不会傻等。
4. `defer resp.Body.Close()` 防止连接泄漏。`http.Client` 的 `Timeout` 在 `main` 中设置，默认无限等待是个隐患。

### 第 3 步：定义工具

每个工具只需要说明"我是谁"和"怎么调用我"：

```go
// tool.go
type Tool interface {
    Spec() ToolSpec
    Call(ctx context.Context, args json.RawMessage) (string, error)
}

// FuncTool 用一个函数快速实现 Tool
type FuncTool struct {
    Def FuncDef
    Fn  func(ctx context.Context, args json.RawMessage) (string, error)
}

func (t FuncTool) Spec() ToolSpec { return ToolSpec{Type: "function", Function: t.Def} }

func (t FuncTool) Call(ctx context.Context, a json.RawMessage) (string, error) {
    return t.Fn(ctx, a)
}
```

示例工具查天气，这里返回的是固定内容，实际项目替换成真实 API 调用即可：

```go
// tool.go
func weatherTool() Tool {
    return FuncTool{
        Def: FuncDef{
            Name:        "get_weather",
            Description: "查询指定城市的当前天气",
            Parameters: json.RawMessage(`{"type":"object",
                "properties":{"city":{"type":"string","description":"城市名"}},
                "required":["city"]}`),
        },
        Fn: func(ctx context.Context, raw json.RawMessage) (string, error) {
            var a struct {
                City string `json:"city"`
            }
            if err := json.Unmarshal(raw, &a); err != nil {
                return "", fmt.Errorf("参数解析失败: %w", err)
            }
            return a.City + "：晴，22 摄氏度", nil // 这里换成真实的天气 API 调用
        },
    }
}
```

新增一个工具，只需要再写一个返回 `Tool` 的函数并传给 Agent，主循环完全不用改。这就是接口带来的好处。

### 第 4 步：实现 Agent 主循环

先看结构与构造函数：

```go
// agent.go
type Agent struct {
    llm      LLM
    tools    map[string]Tool
    specs    []ToolSpec
    history  []Message
    MaxSteps int
}

func NewAgent(llm LLM, system string, tools ...Tool) *Agent {
    a := &Agent{llm: llm, tools: map[string]Tool{}, MaxSteps: 8}
    for _, t := range tools {
        a.tools[t.Spec().Function.Name] = t
        a.specs = append(a.specs, t.Spec())
    }
    a.history = []Message{{Role: "system", Content: system}}
    return a
}
```


主循环 `Run` 就是前面画的那个循环：

```go
// agent.go
// Run 是 Agent 的核心循环：问模型 -> 执行工具 -> 把结果喂回去 -> 直到模型给出最终答案
func (a *Agent) Run(ctx context.Context, input string) (string, error) {
    a.history = append(a.history, Message{Role: "user", Content: input})
    for step := 0; step < a.MaxSteps; step++ {
        msg, err := a.llm.Chat(ctx, a.history, a.specs)
        if err != nil {
            return "", fmt.Errorf("step %d: %w", step, err)
        }
        a.history = append(a.history, msg)
        if len(msg.ToolCalls) == 0 {
            return msg.Content, nil // 没有工具调用，就是最终答案
        }
        a.history = append(a.history, a.runTools(ctx, msg.ToolCalls)...)
    }
    return "", errors.New("超过最大步数，Agent 未收敛")
}
```

并行执行工具，并把错误转成文本交给模型：

```go
// agent.go
// runTools 并行执行同一轮里的多个工具调用，结果顺序与调用顺序一致
func (a *Agent) runTools(ctx context.Context, calls []ToolCall) []Message {
    out := make([]Message, len(calls))
    var wg sync.WaitGroup
    for i, c := range calls {
        wg.Add(1)
        go func() {
            defer wg.Done()
            out[i] = Message{Role: "tool", ToolCallID: c.ID, Content: a.callOne(ctx, c)}
        }()
    }
    wg.Wait()
    return out
}

// callOne 的错误不向上抛，而是变成文本交给模型，让它自己决定重试或换方案
func (a *Agent) callOne(ctx context.Context, c ToolCall) string {
    t, ok := a.tools[c.Function.Name]
    if !ok {
        return "error: 未知工具 " + c.Function.Name
    }
    slog.Info("tool call", "name", c.Function.Name, "args", c.Function.Arguments)
    res, err := t.Call(ctx, []byte(c.Function.Arguments))
    if err != nil {
        return "error: " + err.Error()
    }
    return res
}
```

几个关键设计：

| 设计                         | 原因                                     |
| -------------------------- | -------------------------------------- |
| `MaxSteps` 上限              | 防止模型反复调用工具陷入死循环，也控制成本                  |
| 工具错误转成 `error: ...` 文本     | 让模型自行修正参数或换方案，而不是中断整个流程                |
| 未知工具名也返回文本                 | 模型有时会"幻觉"出不存在的工具                       |
| `tools` 用 map、`specs` 用切片  | map 方便按名查找，切片保证发给模型的工具顺序稳定（map 遍历顺序随机） |
| 每个 goroutine 只写 `out[i]`   | 各写各的下标，无需加锁，结果顺序与调用顺序一致                |
| 每条 `tool` 消息带 `ToolCallID` | 协议要求，缺失会导致接口报错                         |

这里用到了第 4 章的并发模式：`WaitGroup` 等待一组 goroutine，Go 1.22 起循环变量每轮迭代独立，闭包里可以直接使用 `i` 和 `c`。

### 补充：限制并发度

`runTools` 会为同一轮的每个工具调用各开一个 goroutine。如果模型一次要求调用几十个工具，或者工具内部会访问有限流的下游，就需要限制同时执行的数量。惯用法是用带缓冲的 channel 当信号量，容量就是最大并发数：

```go
var wg sync.WaitGroup
sem := make(chan struct{}, 4) // 最多同时 4 个
for _, c := range calls {
    sem <- struct{}{}         // 拿令牌，满了就阻塞
    wg.Add(1)
    go func() {
        defer wg.Done()
        defer func() { <-sem }() // 归还令牌
        run(c)                   // 执行工具
    }()
}
wg.Wait()
```

### 第 5 步：组装入口并运行

```go
// main.go
func main() {
    llm := &OpenAIClient{
        BaseURL: os.Getenv("LLM_BASE_URL"), // 例如 https://api.openai.com/v1
        APIKey:  os.Getenv("LLM_API_KEY"),
        Model:   os.Getenv("LLM_MODEL"),
        HTTP:    &http.Client{Timeout: 60 * time.Second},
    }
    agent := NewAgent(llm, "你是一个乐于助人的助手，需要时调用工具。", weatherTool())

    ctx, cancel := context.WithTimeout(context.Background(), 2*time.Minute)
    defer cancel()
    ans, err := agent.Run(ctx, "深圳今天天气怎么样？")
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(ans)
}
```

运行方式：

```bash
export LLM_BASE_URL=https://你的厂商/v1
export LLM_API_KEY=你的key
export LLM_MODEL=模型名
cd agent && go run .
```

真实输出取决于你接入的模型。以天气为例，终端会先打印一行 `tool call name=get_weather ...` 的日志，随后输出模型根据工具结果组织的回答。

### 第 6 步：不调用真实模型的测试

Agent 的行为如果只靠手工试，回归全凭运气。利用第 5.2 节的 `httptest`，起一个本地假服务：第一次请求返回"请调用 `get_weather`"，第二次返回最终答案，并检查第二次请求里带上了工具结果：

```go
// agent_test.go
// 用 httptest 伪造一个 OpenAI 兼容服务：第一次要求调工具，第二次给最终答案
func TestAgentToolLoop(t *testing.T) {
    calls := 0
    var secondReq string
    srv := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        b, _ := io.ReadAll(r.Body)
        calls++
        w.Header().Set("Content-Type", "application/json")
        if calls == 1 {
            io.WriteString(w, `{"choices":[{"message":{"role":"assistant","tool_calls":[
                {"id":"c1","type":"function","function":{"name":"get_weather","arguments":"{\"city\":\"深圳\"}"}}]}}]}`)
            return
        }
        secondReq = string(b)
        io.WriteString(w, `{"choices":[{"message":{"role":"assistant","content":"深圳晴，22 度"}}]}`)
    }))
    defer srv.Close()

    llm := &OpenAIClient{BaseURL: srv.URL, APIKey: "k", Model: "m", HTTP: srv.Client()}
    ans, err := NewAgent(llm, "sys", weatherTool()).Run(context.Background(), "深圳天气？")
    if err != nil || ans != "深圳晴，22 度" {
        t.Fatalf("ans=%q err=%v", ans, err)
    }
    if !strings.Contains(secondReq, `"role":"tool"`) || !strings.Contains(secondReq, "tool_call_id") {
        t.Fatalf("第二次请求没有带上工具结果: %s", secondReq)
    }
    var probe map[string]any
    if json.Unmarshal([]byte(secondReq), &probe) != nil {
        t.Fatal("请求体不是合法 JSON")
    }
}
```

执行 `go test -race -v ./...`，预期看到 `--- PASS: TestAgentToolLoop`。由于 `Agent` 依赖的是 `LLM` 接口，也可以直接写一个实现该接口的 mock 来测试主循环，完全不走 HTTP。

### 第 7 步：验证与改进

1. 用 `go vet ./...` 与 `go test -race ./...` 确认没有静态问题和数据竞争。
2. 新增一个 `calculator` 工具，参数为表达式字符串，让 Agent 能回答算术问题。
3. 给 `runTools` 增加并发度限制（参见上面的"补充：限制并发度"），并写测试验证最大并发数不超过限制。
4. 实现对话历史截断：保留 `system` 消息和最近 N 条，注意不能把一条带 `tool_calls` 的 `assistant` 消息与它对应的 `tool` 消息拆开。
5. 进阶挑战：流式输出（解析 SSE，用 channel 逐段推送）；接入 MCP，把外部工具适配成 `Tool`；用 trpc-go 把 Agent 封装成 RPC 服务（参照第 7 章）。

### 常见坑

- 把 `arguments` 当成对象解析：它是字符串，要二次 `Unmarshal`。
- 工具出错就直接中断：应把错误文本回传给模型，让它自行修正。
- 没有 `MaxSteps`：模型陷入循环会无限消耗调用额度。
- 历史无限增长：超过上下文窗口后接口会直接报错，需要截断或摘要策略。
- 没设 `http.Client.Timeout` 和 `context` 超时：上游一卡，整个服务跟着卡死。
- `tool` 消息缺 `tool_call_id`，或没有紧跟在对应的 `assistant` 消息之后：接口返回 400。
- 多个请求共用同一个 `Agent`：`history` 被并发追加，数据错乱。一个会话对应一个 `Agent`。
- 日志里打印请求头：API key 泄露。日志只记录工具名、耗时与状态码。

### 本章小结

Agent 看起来高大上，落到代码上就是"一个接口抽象、一个循环、一组并发的工具调用"。用 interface 隔离变化，用 `context` 管住超时，用 `-race` 与 `httptest` 守住正确性，这些都是前面章节反复强调的 Go 工程习惯，在这里集中用了一遍。

---

## 附录 A 速查表

### A.1 语法速查

| 主题 | 写法 |
| --- | --- |
| 声明变量 | `var x int`、`x := 1` |
| 切片预分配 | `make([]T, 0, n)` |
| map 判存在 | `v, ok := m[k]` |
| 多返回值 | `func f() (int, error)` |
| 延迟执行 | `defer f.Close()` |
| 类型分支 | `switch v := x.(type)` |
| 启动协程 | `go f()` |
| 超时 | `ctx, cancel := context.WithTimeout(parent, d)` |
| 包装错误 | `fmt.Errorf("...: %w", err)` |
| 判断错误 | `errors.Is(err, target)`、`errors.As(err, &t)` |

### A.2 并发安全检查清单

- 每个 goroutine 是否有明确的退出路径？
- channel 是否只由发送方关闭，且只关闭一次？
- 共享变量是否都被锁或原子操作保护？
- 所有 `WithCancel`、`WithTimeout` 是否都 `defer cancel()`？
- 是否已用 `-race` 跑过测试？

### A.3 版本特性一览

| 版本 | 重要特性 |
| --- | --- |
| 1.13 | `errors.Is/As`、`%w` |
| 1.14 | 异步抢占 |
| 1.16 | `embed` |
| 1.18 | 泛型 |
| 1.19 | `GOMEMLIMIT` |
| 1.20 | `errors.Join` |
| 1.21 | `slices`、`maps`、`log/slog`、内置 `min`/`max`/`clear` |
| 1.22 | 循环变量每次迭代独立、整数 range、增强的 `ServeMux` 路由 |
| 1.23 | range over func（迭代器） |

### A.4 学习路线与资料

1. 先过一遍官方 A Tour of Go（go.dev/tour），约 1 到 2 天。
2. 阅读 Effective Go 与 Go Code Review Comments，建立惯用法意识。
3. 精读《The Go Programming Language》（中文版《Go 程序设计语言》）的并发章节。
4. 想理解运行时：读《Go 语言设计与实现》（draveness，在线）。
5. 并发进阶：阅读 Go 官方博客 "Go Concurrency Patterns" 与 "Pipelines and cancellation" 两篇。
6. 做项目：先完成第 8 章，再改造成 HTTP 与 RPC 服务。

## 附录 B 各章练习题

1. 写一个函数 `Dedup[T comparable](xs []T) []T`，去重并保持原有顺序。（第 3 章）
2. 实现一个线程安全的 LRU 缓存，要求 `Get`、`Put` 均为 O(1)。（第 2、4 章）
3. 用 channel 实现 Pipeline：生成数字，平方，求和，三个阶段分别在独立 goroutine 中。（第 4 章）
4. 写一个会泄漏 goroutine 的程序，用 pprof 的 goroutine profile 找到泄漏点，再修复。（第 4、5 章）
5. 对比 `append` 不预分配与预分配 10 万个元素的 `Benchmark`，用 `-benchmem` 观察分配次数。（第 2、5 章）
6. 用 `go build -gcflags=-m` 分析一段代码，找出哪些变量逃逸，尝试优化其中一个。（第 6 章）
7. 为第 8 章的 `checkAll` 编写使用 `httptest` 的表驱动测试。（第 5、8 章）

<p align="center">—— End ——</p>
