# TypeScript 精简教程：以搭建 Agent 为目的

<!-- > 8 章 + 附录。代码均经 tsc --strict 编译校验，第 8 章完整 Agent 已实际运行。 -->

## 目录

- [**前言：学什么、怎么学**](#ch00)
  - [目标](#ch00-s01)
  - [知识点与 Agent 的对应关系](#ch00-s02)
  - [学习路线](#ch00-s03)
  - [一个心智模型](#ch00-s04)
  - [代码约定](#ch00-s05)
- [**第 1 章　环境与最小配置**](#ch01)
  - [1.1 TS 是什么](#ch01-s01)
  - [1.2 搭一个项目](#ch01-s02)
  - [1.3 三种运行方式](#ch01-s03)
  - [1.4 tsconfig 最小配置](#ch01-s04)
  - [1.5 JS 必备速览（Python 视角）](#ch01-s05)
  - [小结](#ch01-s06)
- [**第 2 章　类型基础、联合类型与收窄**](#ch02)
  - [2.1 标注与推断](#ch02-s01)
  - [2.2 常用类型](#ch02-s02)
  - [2.3 null 与 undefined](#ch02-s03)
  - [2.4 对象类型：interface 与 type](#ch02-s04)
  - [2.5 字面量类型与 as const](#ch02-s05)
  - [2.6 联合类型与收窄](#ch02-s06)
  - [2.7 可辨识联合（最重要）](#ch02-s07)
  - [小结](#ch02-s08)
- [**第 3 章　函数、泛型与类**](#ch03)
  - [3.1 函数](#ch03-s01)
  - [3.2 泛型](#ch03-s02)
  - [3.3 类](#ch03-s03)
  - [小结](#ch03-s04)
- [**第 4 章　类型运算最小集**](#ch04)
  - [4.1 typeof、keyof、索引访问](#ch04-s01)
  - [4.2 内置工具类型](#ch04-s02)
  - [4.3 satisfies：检查，但保留精确类型](#ch04-s03)
  - [4.4 读懂两种语法就够了](#ch04-s04)
  - [4.5 z.infer：Agent 里最常用的"类型运算"](#ch04-s05)
  - [小结](#ch04-s06)
- [**第 5 章　异步编程**](#ch05)
  - [5.1 Promise 与 async/await](#ch05-s01)
  - [5.2 并行：Promise.all](#ch05-s02)
  - [5.3 四个常见陷阱](#ch05-s03)
  - [5.4 取消与超时：AbortSignal](#ch05-s04)
  - [5.5 流式输出：async generator](#ch05-s05)
  - [5.6 重试与指数退避](#ch05-s06)
  - [小结](#ch05-s07)
- [**第 6 章　错误处理与运行时校验**](#ch06)
  - [6.1 错误处理基础](#ch06-s01)
  - [6.2 throw 还是 Result](#ch06-s02)
  - [6.3 为什么需要运行时校验](#ch06-s03)
  - [6.4 zod：schema 即类型](#ch06-s04)
  - [6.5 校验 LLM 输出](#ch06-s05)
  - [6.6 schema 转 JSON Schema，给模型当工具定义](#ch06-s06)
  - [6.7 原则](#ch06-s07)
  - [小结](#ch06-s08)
- [**第 7 章　模块与工程**](#ch07)
  - [7.1 模块（ESM）](#ch07-s01)
  - [7.2 没有类型的 JS 库](#ch07-s02)
  - [7.3 项目结构](#ch07-s03)
  - [7.4 测试：Vitest](#ch07-s04)
  - [7.5 Lint](#ch07-s05)
  - [7.6 常见编译报错速查](#ch07-s06)
  - [小结](#ch07-s07)
- [**第 8 章　实战：从零写一个 Tool-calling Agent**](#ch08)
  - [8.1 Agent 的本质：一个循环](#ch08-s01)
  - [8.2 数据模型](#ch08-s02)
  - [8.3 工具：一份 schema，三种用途](#ch08-s03)
  - [8.4 安全地执行工具](#ch08-s04)
  - [8.5 主循环](#ch08-s05)
  - [8.6 用假模型跑起来](#ch08-s06)
  - [8.7 测试](#ch08-s07)
  - [8.8 接入真实模型](#ch08-s08)
  - [8.9 事件流式输出](#ch08-s09)
  - [8.10 护栏清单](#ch08-s10)
  - [8.11 还能往哪扩展](#ch08-s11)
  - [练习](#ch08-s12)
- [**附录**](#ch09)
  - [附录 A　Python → TypeScript 对照](#ch09-s01)
  - [附录 B　速查](#ch09-s02)
  - [附录 C　检查清单](#ch09-s03)
  - [附录 D　延伸阅读](#ch09-s04)

---

<a id="ch00"></a>

# 前言：学什么、怎么学

<a id="ch00-s01"></a>

## 目标

读完能做到：**读懂并写出一个带工具调用的 TypeScript Agent**（含校验、并发、取消、流式、测试）。

不追求语言全貌，只保留搭 Agent 会用到的部分。类型体操、装饰器、命名空间、`.d.ts` 编写等一律略过。

<a id="ch00-s02"></a>

## 知识点与 Agent 的对应关系

| 章 | 内容           | 在 Agent 里用在哪                     |
| - | ------------ | -------------------------------- |
| 1 | 环境与 tsconfig | 项目起步                             |
| 2 | 类型基础、联合类型、收窄 | 消息、模型响应、状态的建模                    |
| 3 | 函数、泛型、类      | Tool 定义、LLM 接口、ToolRegistry      |
| 4 | 类型运算最小集      | `z.infer`、`Parameters`、`Extract` |
| 5 | 异步           | 调模型、并行工具、取消、流式、重试                |
| 6 | 错误处理与 zod    | 校验 LLM 输出、工具参数、环境变量              |
| 7 | 模块与工程        | ESM、脚本、测试                        |
| 8 | 实战           | 完整 Agent，约 250 行                 |

<a id="ch00-s03"></a>

## 学习路线

- **有 JS 基础**：1 → 2 → 3 → 5 → 6 → 8，4 和 7 查阅即可
- **Python 背景**：先看附录 A 的对照表，再按顺序读
- **赶时间**：直接读第 8 章，遇到不懂的类型回查对应章节

<a id="ch00-s04"></a>

## 一个心智模型

> TypeScript = JavaScript + 一层**编译期**的类型检查。类型在运行时不存在。

推论：**外部数据（HTTP、文件、LLM 输出）进入程序时，类型不会保护你，必须运行时校验。** 这是 Agent 开发里最重要的一条。

<a id="ch00-s05"></a>

## 代码约定

- 代码块里带 `// ❌` 的行会报编译错误，是故意写的反例
- 其余代码均在 `strict` 模式下编译通过

---

<a id="ch01"></a>

# 第 1 章　环境与最小配置

<a id="ch01-s01"></a>

## 1.1 TS 是什么

TS 是 JS 的**超集**：合法的 JS 都是合法的 TS，多出来的是类型标注。

```
.ts 源码 ──(检查类型 + 擦除类型)──▶ .js ──▶ Node / 浏览器运行
```

两个事实：

1. 类型**只存在于编译期**，运行时全部消失
2. TS **不改变运行时行为**，性能与 JS 完全一致

<a id="ch01-s02"></a>

## 1.2 搭一个项目

需要 Node.js 22+。

```bash
mkdir my-agent && cd my-agent
npm init -y
npm i -D typescript tsx @types/node vitest
npm i zod
npx tsc --init
```

<a id="ch01-s03"></a>

## 1.3 三种运行方式

| 方式        | 命令                              | 检查类型？ |
| --------- | ------------------------------- | ----- |
| tsx（开发首选） | `npx tsx src/index.ts`          | 否     |
| Node 直接跑  | `node src/index.ts`（22.18+）     | 否     |
| 编译后跑      | `npx tsc && node dist/index.js` | 是     |

**tsx、Node、esbuild 都只擦除类型，不会报类型错误。** 检查类型只能靠 `npx tsc --noEmit`，所以工程里两个都要有。

`package.json`：

```json
{
  "type": "module",
  "scripts": {
    "dev": "tsx watch src/index.ts",
    "typecheck": "tsc --noEmit",
    "test": "vitest run",
    "check": "npm run typecheck && npm run test"
  }
}
```

<a id="ch01-s04"></a>

## 1.4 tsconfig 最小配置

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "verbatimModuleSyntax": true,
    "skipLibCheck": true,
    "outDir": "dist"
  },
  "include": ["src", "tests"]
}
```

| 选项                         | 作用                                                                        |
| -------------------------- | ------------------------------------------------------------------------- |
| `strict`                   | 一键开启全部严格检查，**必开**。最关键的是 `strictNullChecks`（`null`/`undefined` 不能随便赋给别的类型） |
| `noUncheckedIndexedAccess` | `arr[0]` 的类型带上 `undefined`，强制处理越界                                         |
| `verbatimModuleSyntax`     | 仅作类型的导入必须写 `import type`，导入行为一目了然                                         |
| `module: NodeNext`         | Node ESM 的解析规则（见第 7 章：相对导入要写 `.js`）                                       |

<a id="ch01-s05"></a>

## 1.5 JS 必备速览（Python 视角）

```ts
const a = 1;                       // 不可重新赋值，默认用它
let b = 2;                         // 可变；不要用 var

const user = { id: 1, name: "April" };           // 对象，类似 dict，但用 user.name 访问
const { id, name } = user;                        // 解构
const user2 = { ...user, name: "Bob" };           // 展开：复制并覆盖
const [first, ...rest] = [1, 2, 3];               // 数组解构

const double = (x: number) => x * 2;              // 箭头函数
const msg = `hi ${name}`;                         // 模板字符串（f-string）

const maybe: { city?: string } = {};
const city = maybe.city?.toUpperCase() ?? "unknown";   // ?. 可选链；?? 仅在 null/undefined 时取默认值

console.log(1 === 1);              // 永远用 === 和 !==，不要用 ==
```

几个要记住的差异：

|   |   |   |
| - | - | - |

- `0 || 5` 得 `5`，`0 ?? 5` 得 `0`：**取默认值用 `??`**
- 对象、数组按引用比较：`[] === []` 为 `false`
- 数字只有 `number`，没有 int/float 之分
- 遍历键值：`for (const [k, v] of Object.entries(obj))`

<a id="ch01-s06"></a>

## 小结

- 开发用 `tsx` 跑，提交前跑 `tsc --noEmit`
- `strict` + `noUncheckedIndexedAccess` 必开
- 悬停鼠标看推断出的类型，是学 TS 最快的办法

---

<a id="ch02"></a>

# 第 2 章　类型基础、联合类型与收窄

这一章是全书的地基。**可辨识联合 + 收窄**会在 Agent 里反复出现：消息、模型响应、工具结果、事件，全靠它。

<a id="ch02-s01"></a>

## 2.1 标注与推断

```ts
const title: string = "TS";
let pages = 300;          // 推断为 number，不用写
pages = "三百";           // ❌ string 不能赋给 number
```

什么时候写类型：

| 场景        | 做法                           |
| --------- | ---------------------------- |
| 局部变量，有初始值 | 省略，让 TS 推断                   |
| 函数参数      | **必须写**                      |
| 导出函数的返回值  | 建议写                          |
| 初始为空的容器   | 要写：`const xs: string[] = []` |

<a id="ch02-s02"></a>

## 2.2 常用类型

```ts
let s: string, n: number, ok: boolean;
const xs: number[] = [1, 2, 3];                 // 数组
const pair: [string, number] = ["age", 18];     // 元组：定长、各位置类型固定
const m: Record<string, number> = { a: 1 };     // 字典
const ro: readonly number[] = [1, 2];           // 只读数组
```

类型名一律小写：`string`、`number`，不要写 `String`、`Number`。

### unknown：不知道类型时用它，不要用 any

| 类型        | 含义                           |
| --------- | ---------------------------- |
| `any`     | 关闭检查，且会"传染"。满屏 `any` 等于没用 TS |
| `unknown` | 能接收任何值，**用之前必须先收窄**          |
| `never`   | 不可能有值：永远抛错的函数、穷尽检查           |
| `void`    | 函数无返回值                       |

```ts
function toNumber(input: unknown): number {
  input.toFixed();                  // ❌ unknown 不能直接用
  if (typeof input === "number") return input;       // 收窄后可用
  if (typeof input === "string") return Number(input);
  throw new Error("unsupported");
}
```

**规则：外部输入（JSON、HTTP、`catch` 的错误、LLM 输出）一律先当 `unknown`。**

<a id="ch02-s03"></a>

## 2.3 null 与 undefined

开启 `strictNullChecks` 后，它们不能赋给其他类型，"可能为空"必须写进类型：

```ts
let a: string = null;               // ❌
let b: string | null = null;        // ✅

function len(s: string | null): number {
  return s.length;                  // ❌ s 可能是 null
}
function len2(s: string | null): number {
  return s === null ? 0 : s.length; // ✅
}

const timeout: number | undefined = undefined;
const t = timeout ?? 3000;          // 取默认值
```

非空断言 `x!` 等于"我保证不空"，错了运行时照样炸，**少用**。

<a id="ch02-s04"></a>

## 2.4 对象类型：interface 与 type

```ts
interface User {
  id: number;
  name: string;
  email?: string;               // 可选：读出来是 string | undefined
  readonly createdAt: Date;     // 只读：只在编译期，且是浅层的
}

type Role = "admin" | "user";   // type 还能表示联合、元组、函数
type Handler = (msg: string) => void;
```

|                | `interface` | `type`   |
| -------------- | ----------- | -------- |
| 描述对象           | ✅           | ✅        |
| 联合 / 元组 / 函数别名 | ❌           | ✅        |
| 扩展             | `extends`   | 交叉类型 `&` |
| 同名声明合并         | ✅           | ❌        |

**选择**：对象用哪个都行，团队统一即可；联合、元组、工具类型只能用 `type`。

TS 是**结构化类型**：只看"形状"，不看名字。

```ts
interface Named { name: string }
class Person { constructor(public name: string, public age: number) {} }
const n: Named = new Person("A", 1);      // ✅ 有 name: string 就够了
```

对象字面量直接赋值时，多余属性会被拦下：

```ts
interface Point { x: number; y: number }
const p: Point = { x: 1, y: 2, z: 3 };    // ❌ 多余属性 z
```

<a id="ch02-s05"></a>

## 2.5 字面量类型与 as const

类型可以是**某一个具体的值**：

```ts
let dir: "left" | "right" = "left";
dir = "up";                                // ❌
```

`as const` 把值冻结成最窄的只读类型，常用来**由值反推类型**，保证值与类型同源：

```ts
const ROLES = ["system", "user", "assistant", "tool"] as const;
type Role = (typeof ROLES)[number];        // "system" | "user" | "assistant" | "tool"
```

**不要用 `enum`**：它会生成运行时代码，且与"只擦类型"的运行方式冲突。用字面量联合代替。

<a id="ch02-s06"></a>

## 2.6 联合类型与收窄

|          |                                       |
| -------- | ------------------------------------- |
| 联合类型 \`A | B\`：只能使用**所有成员共有**的操作，要用特有的必须先**收窄**。 |

```ts
function show(x: string | number) {
  if (typeof x === "string") return x.toUpperCase();   // 这里 x 是 string
  return x.toFixed(2);                                  // 这里 x 是 number
}
```

常用收窄手段：

| 手段           | 例子                            |
| ------------ | ----------------------------- |
| `typeof`     | `typeof x === "string"`       |
| `instanceof` | `err instanceof Error`        |
| `in`         | `"swim" in animal`            |
| 相等 / 真值      | `x === null`、`if (x)`         |
| 可辨识字段        | `msg.role === "tool"`（见 2.7）  |
| 自定义守卫        | `function isCat(a): a is Cat` |

自定义守卫：

```ts
function isDefined<T>(x: T | null | undefined): x is T {
  return x !== null && x !== undefined;
}
const clean: string[] = ["a", undefined, "b"].filter(isDefined);   // string[]
```

> `x is T` 是你对编译器的承诺，TS 不会验证函数体。写错了类型就是谎言。

<a id="ch02-s07"></a>

## 2.7 可辨识联合（最重要）

给联合的每个成员加一个**同名的字面量字段**（常叫 `role`、`type`、`kind`、`status`），TS 就能按它精确收窄。

```ts
type Message =
  | { role: "system"; content: string }
  | { role: "user"; content: string }
  | { role: "assistant"; content: string; toolCalls?: { id: string; name: string }[] }
  | { role: "tool"; toolCallId: string; content: string };

function describe(m: Message): string {
  switch (m.role) {
    case "tool": return `结果 ${m.toolCallId}`;                       // m 被收窄为 tool 成员
    case "assistant": return `助手，工具调用 ${m.toolCalls?.length ?? 0} 个`;
    default: return `${m.role}: ${m.content}`;
  }
}
```


### 穷尽检查

用 `never` 保证"以后给联合加了成员，却忘了处理"时**编译报错**：

```ts
function assertNever(x: never): never {
  throw new Error(`未处理的分支: ${JSON.stringify(x)}`);
}

type Shape = { kind: "circle"; r: number } | { kind: "rect"; w: number; h: number };

function area(s: Shape): number {
  switch (s.kind) {
    case "circle": return Math.PI * s.r ** 2;
    case "rect": return s.w * s.h;
    default: return assertNever(s);     // 新增 Shape 成员后，这里会报错
  }
}
```

### 用它消灭非法状态

```ts
// 坏设计：loading 和 error 可能同时为 true，data 和 error 可能同时有值
interface BadState { loading: boolean; data?: string; error?: Error }

// 好设计：每个状态只带自己需要的数据，非法组合根本写不出来
type RequestState =
  | { status: "idle" }
  | { status: "loading" }
  | { status: "success"; data: string }
  | { status: "error"; error: Error };
```

<a id="ch02-s08"></a>

## 小结

- 参数必写类型，局部变量靠推断；不知道类型用 `unknown`
- `null` / `undefined` 要显式写进类型，用 `?.` 和 `??` 处理
- 字面量联合 + `as const` 代替 `enum`
- **可辨识联合 + `never` 穷尽检查**：建模 Agent 里所有"多种形态"的数据

---

<a id="ch03"></a>

# 第 3 章　函数、泛型与类

<a id="ch03-s01"></a>

## 3.1 函数

```ts
function add(a: number, b: number): number {
  return a + b;
}
const sub = (a: number, b: number) => a - b;       // 返回值可推断

function greet(name: string, title?: string) {}    // 可选参数
function repeat(s: string, times = 2) {}            // 默认值
function sum(...nums: number[]) {}                  // 剩余参数
```

### 参数超过 3 个，改用对象参数

```ts
interface CreateUserOptions {
  name: string;
  age?: number;
  admin?: boolean;
}

function createUser({ name, age = 18, admin = false }: CreateUserOptions) {
  return { name, age, admin };
}
createUser({ name: "April", admin: true });        // 一眼看懂每个参数
```

### 函数类型与回调

```ts
type Handler = (msg: string) => void;

const nums = [1, 2, 3];
const doubled = nums.map((n) => n * 2);            // 回调参数自动推断，不用再写类型
```

`async` 函数的返回值是 `Promise<T>`，详见第 5 章。

<a id="ch03-s02"></a>

## 3.2 泛型

**泛型 = 类型层面的参数**，用来让输入与输出的类型保持关联。

```ts
function first<T>(arr: T[]): T | undefined {
  return arr[0];
}
const a = first([1, 2, 3]);        // number | undefined
const b = first(["x"]);            // string | undefined
```

### 约束：`extends`

泛型默认可以是任何类型，所以不能访问它的属性。用 `extends` 设上限：

```ts
function longest<T extends { length: number }>(a: T, b: T): T {
  return a.length >= b.length ? a : b;
}
```

最经典的组合 `K extends keyof T`：

```ts
function getProp<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}
const user = { id: 1, name: "April" };
const n = getProp(user, "name");        // string
getProp(user, "age");                   // ❌ "age" 不是 user 的键
```

### 泛型接口与别名

```ts
type Result<T, E = Error> =
  | { ok: true; value: T }
  | { ok: false; error: E };

function divide(a: number, b: number): Result<number, string> {
  return b === 0 ? { ok: false, error: "除数为 0" } : { ok: true, value: a / b };
}

const r = divide(1, 0);
if (r.ok) console.log(r.value);    // number
else console.log(r.error);         // string
```

### Agent 里的泛型：Tool

```ts
interface Tool<TArgs, TResult> {
  name: string;
  description: string;
  run(args: TArgs): Promise<TResult>;
}

const weather: Tool<{ city: string }, { temp: number }> = {
  name: "get_weather",
  description: "查询天气",
  async run({ city }) {
    return { temp: city.length };
  },
};

async function callTool<A, R>(tool: Tool<A, R>, args: A): Promise<R> {
  return tool.run(args);
}
await callTool(weather, { town: "深圳" });     // ❌ 参数名错了，编译期就拦住
```

### 使用原则

- 类型参数在签名里**至少出现两次**才有意义；只出现一次通常是多余的
- 泛型函数体里不能 `new T()`：类型运行时不存在，要把构造函数当参数传进来
- 业务代码用简单泛型就够，别炫技

<a id="ch03-s03"></a>

## 3.3 类

Agent 里类适合封装**有状态的对象**：客户端、注册表、会话。

```ts
class ToolRegistry {
  private readonly tools = new Map<string, { name: string }>();

  register(tool: { name: string }): this {
    this.tools.set(tool.name, tool);
    return this;                                 // 返回 this 支持链式调用
  }

  get(name: string): { name: string } | undefined {
    return this.tools.get(name);
  }

  get size(): number {
    return this.tools.size;
  }
}
```

要点：

| 点 | 说明 |
|---|---|
| 访问修饰符 | `public`（默认）、`protected`、`private`；`private` 只在编译期限制，运行时真私有用 `#field` |
| `readonly` | 初始化后不可重新赋值 |
| 属性必须初始化 | `strictPropertyInitialization`：声明时赋值或在构造器里赋值 |
| 参数属性 | `constructor(private name: string) {}` 同时声明并赋值。但开启 `erasableSyntaxOnly`（Node 直接跑 TS）时不允许 |
| `implements` | 检查类是否满足接口，不继承实现 |
| `override` | 子类覆盖方法时标注，父类改名会立刻报错 |
| 抽象类 | `abstract class`：不能实例化，定义骨架 |

### 接口 + 实现：依赖倒置

```ts
interface Clock { now(): number }

class SystemClock implements Clock {
  now() { return Date.now(); }
}
class FakeClock implements Clock {
  constructor(private t: number) {}
  now() { return this.t; }
}

function isExpired(clock: Clock, deadline: number) {
  return clock.now() > deadline;
}
```

**业务代码只依赖接口，不依赖具体实现**。第 8 章的 `LLM` 接口就是这个思路：测试时换成假模型，上线换成真模型。

### 异步初始化：静态工厂

构造器不能 `await`：

```ts
class Client {
  private constructor(private readonly conn: string) {}

  static async create(url: string): Promise<Client> {
    const conn = await Promise.resolve(`connected:${url}`);
    return new Client(conn);
  }
}
const client = await Client.create("http://x");
```

### this 的坑

把方法当回调传，`this` 会丢。用箭头函数包一层：

```ts
class Counter {
  count = 0;
  inc = () => { this.count++; };          // 箭头函数属性，this 永远指向实例
}
const { inc } = new Counter();
inc();                                     // ✅
```

**组合优于继承**：能用"传入依赖"解决的，就不要写多层继承。

<a id="ch03-s04"></a>

## 小结

- 参数多了用对象参数；回调参数靠上下文推断
- 泛型 = 类型参数；`T extends ...` 加约束，`K extends keyof T` 取键
- 类封装状态；对外依赖接口，方便替换与测试
- 异步初始化用 `static async create()`

---

<a id="ch04"></a>

# 第 4 章　类型运算最小集

只讲搭 Agent 会反复遇到的几个，读懂即可，不要求自己写复杂类型。

<a id="ch04-s01"></a>

## 4.1 typeof、keyof、索引访问

```ts
const config = { host: "localhost", port: 3000 };
type Config = typeof config;                 // { host: string; port: number }
type ConfigKey = keyof Config;               // "host" | "port"
type Port = Config["port"];                  // number

const TOOLS = ["search", "calc"] as const;
type ToolName = (typeof TOOLS)[number];      // "search" | "calc"
```

- `typeof x`（类型位置）：从**值**得到类型，让值成为唯一真相来源
- `keyof T`：对象类型的键的联合
- `T[K]`：取属性类型；`T[number]` 取数组元素类型

<a id="ch04-s02"></a>

## 4.2 内置工具类型

| 工具类型 | 作用 |
|---|---|
| `Partial<T>` / `Required<T>` | 全部可选 / 全部必选 |
| `Readonly<T>` | 全部只读 |
| `Pick<T, K>` / `Omit<T, K>` | 保留 / 去掉指定键 |
| `Record<K, V>` | 键为 K、值为 V 的对象 |
| `Exclude<U, X>` / `Extract<U, X>` | 从联合中剔除 / 保留 |
| `NonNullable<T>` | 去掉 `null` 和 `undefined` |
| `ReturnType<F>` / `Parameters<F>` | 函数的返回类型 / 参数元组 |
| `Awaited<T>` | 解包 Promise |

```ts
interface User { id: number; name: string; password: string }

type PublicUser = Omit<User, "password">;
type UserPatch = Partial<Omit<User, "id">>;      // 更新接口：除 id 外都可选

async function fetchUser(id: number) { return { id, name: "A" }; }
type FetchResult = Awaited<ReturnType<typeof fetchUser>>;     // { id: number; name: string }
type FetchArgs = Parameters<typeof fetchUser>;                // [id: number]
```

`ReturnType` 对 async 函数得到的是 `Promise<...>`，要再包一层 `Awaited`。

### 从可辨识联合里取出某个成员

```ts
type Event =
  | { type: "tool_start"; name: string }
  | { type: "tool_end"; name: string; output: string }
  | { type: "done" };

type ToolEnd = Extract<Event, { type: "tool_end" }>;      // { type: "tool_end"; ... }
```

<a id="ch04-s03"></a>

## 4.3 satisfies：检查，但保留精确类型

```ts
type Palette = Record<string, string | [number, number, number]>;

const p = { red: [255, 0, 0], green: "#0f0" } satisfies Palette;
p.red.map((x) => x * 2);          // ✅ red 仍是元组
p.green.toUpperCase();             // ✅ green 仍是 string
```

用类型标注 `const p: Palette = ...` 则每个属性都被拓宽成联合，上面两行都会报错。**工具注册表、路由表、配置对象**适合用 `satisfies`。

<a id="ch04-s04"></a>

## 4.4 读懂两种语法就够了

**映射类型**：遍历键，生成新类型（`Partial`、`Pick` 就是这么写的）：

```ts
type MyPartial<T> = { [K in keyof T]?: T[K] };
```

**条件类型 + infer**：类型层面的 if 和模式匹配：

```ts
type MyReturn<F> = F extends (...args: any[]) => infer R ? R : never;
type R1 = MyReturn<() => string>;        // string
```

遇到复杂类型的做法：**悬停看结果，拆成有名字的中间类型**，别硬读。

<a id="ch04-s05"></a>

## 4.5 z.infer：Agent 里最常用的"类型运算"

zod schema 自带类型推导，一份 schema 同时给出类型和运行时校验（第 6 章详解）：

```ts
import { z } from "zod";

const Args = z.object({ city: z.string(), days: z.number().default(1) });
type Args = z.infer<typeof Args>;        // { city: string; days: number }
```

<a id="ch04-s06"></a>

## 小结

- `typeof` / `keyof` / `T[K]`：值与类型之间互相推
- 工具类型先用内置的，别自己造
- `satisfies` 用于"既要检查又要精确"
- 读不懂的类型：悬停、拆开

---

<a id="ch05"></a>

# 第 5 章　异步编程

Agent 的本质就是大量网络 I/O：调模型、调工具、读文件。异步是必修课。

<a id="ch05-s01"></a>

## 5.1 Promise 与 async/await

JS 单线程，靠事件循环处理异步。`Promise<T>` 表示"将来会得到一个 T"。

```ts
const delay = (ms: number) => new Promise<void>((resolve) => setTimeout(resolve, ms));

async function getUser(id: number): Promise<{ id: number; name: string }> {
  await delay(10);
  return { id, name: "April" };            // 自动包装成 Promise
}

const user = await getUser(1);             // ESM 里可以顶层 await
```

规则：`async` 函数一定返回 `Promise`；`await` 只能在 `async` 函数或 ESM 顶层使用。

<a id="ch05-s02"></a>

## 5.2 并行：Promise.all

```ts
async function serial(ids: number[]) {
  const out = [];
  for (const id of ids) out.push(await getUser(id));      // 逐个等，慢
  return out;
}

async function parallel(ids: number[]) {
  return Promise.all(ids.map((id) => getUser(id)));        // 同时发，等全部完成
}
```

| 组合器 | 行为 |
|---|---|
| `Promise.all` | 全成功才成功；**任一失败则整体失败** |
| `Promise.allSettled` | 等全部结束，逐个返回 `fulfilled` / `rejected` |
| `Promise.race` | 第一个**结束**的（无论成败）决定结果 |
| `Promise.any` | 第一个**成功**的 |

Agent 里的用法：模型一轮返回多个工具调用，用 `Promise.all` 并行执行；想让某个失败不影响其他，用 `allSettled`。

### 限制并发

一次发几百个请求会被限流。简单的并发池：

```ts
async function mapLimit<T, R>(
  items: readonly T[],
  limit: number,
  fn: (item: T, index: number) => Promise<R>,
): Promise<R[]> {
  const results = new Array<R>(items.length);
  let next = 0;

  async function worker() {
    while (true) {
      const i = next++;
      if (i >= items.length) return;
      results[i] = await fn(items[i]!, i);
    }
  }

  await Promise.all(Array.from({ length: Math.min(limit, items.length) }, worker));
  return results;
}

const users = await mapLimit([1, 2, 3, 4, 5, 6], 3, (id) => getUser(id));   // 最多 3 个并发
```

<a id="ch05-s03"></a>

## 5.3 四个常见陷阱

```ts
const ids = [1, 2, 3];

// 1. forEach 不会等 async 回调
ids.forEach(async (id) => { await getUser(id); });        // 返回时请求还没完成
for (const id of ids) await getUser(id);                  // ✅ 串行
await Promise.all(ids.map((id) => getUser(id)));          // ✅ 并行

// 2. 忘记 await：错误变成"未处理的 rejection"
async function save() {
  getUser(1);                                              // ❌ 逻辑错误：没有 await
  await getUser(1);                                        // ✅
}

// 3. try 里 return promise 要加 await，否则 catch 抓不到
async function safe() {
  try { return await getUser(1); } catch { return null; }
}
```


4. 外部调用没有超时，请求挂起，Agent 卡死。见 5.4。

用 ESLint 的 `@typescript-eslint/no-floating-promises` 可自动抓出第 2 类问题。

<a id="ch05-s04"></a>

## 5.4 取消与超时：AbortSignal

用户中途停止、请求超时，都靠它。

```ts
const ctrl = new AbortController();
setTimeout(() => ctrl.abort(), 1000);

try {
  const res = await fetch("https://example.com", { signal: ctrl.signal });
  await res.text();
} catch (e) {
  if (e instanceof DOMException && e.name === "AbortError") console.log("已取消");
  else throw e;
}

// 内置超时与合并
const timeoutSignal = AbortSignal.timeout(5000);
const both = AbortSignal.any([ctrl.signal, timeoutSignal]);     // 任一触发即取消
```

**约定：任何耗时的异步函数都接收可选的 `signal?: AbortSignal`，并向下透传。** 循环里用 `signal?.throwIfAborted()` 检查。

<a id="ch05-s05"></a>

## 5.5 流式输出：async generator

LLM 的流式响应是异步迭代。核心语法：`async function*` 产出，`for await` 消费。

```ts
async function* countdown(n: number): AsyncGenerator<number> {
  for (let i = n; i > 0; i--) {
    await delay(10);
    yield i;
  }
}

for await (const x of countdown(3)) console.log(x);     // 3 2 1
```

### 解析 SSE（OpenAI 兼容接口的流式格式）

服务端按行推送 `data: {...}`，以 `data: [DONE]` 结束：

```ts
async function* sseData(res: Response): AsyncGenerator<string> {
  if (!res.body) throw new Error("响应没有 body");
  const reader = res.body.getReader();
  const decoder = new TextDecoder();
  let buf = "";
  try {
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      buf += decoder.decode(value, { stream: true });
      let idx: number;
      while ((idx = buf.indexOf("\n")) >= 0) {
        const line = buf.slice(0, idx).trimEnd();
        buf = buf.slice(idx + 1);
        if (line.startsWith("data: ")) {
          const data = line.slice(6);
          if (data === "[DONE]") return;
          yield data;                      // 每条 data 再 JSON.parse 并用 zod 校验
        }
      }
    }
  } finally {
    reader.releaseLock();
  }
}
```

流可以像管道一样组合：

```ts
async function* mapStream<T, R>(src: AsyncIterable<T>, fn: (x: T) => R): AsyncGenerator<R> {
  for await (const x of src) yield fn(x);
}
async function collect(src: AsyncIterable<string>): Promise<string> {
  let s = "";
  for await (const x of src) s += x;
  return s;
}
```

<a id="ch05-s06"></a>

## 5.6 重试与指数退避

调外部 API 失败是常态：

```ts
interface RetryOptions {
  retries?: number;
  baseDelayMs?: number;
  shouldRetry?: (err: unknown) => boolean;
  signal?: AbortSignal;
}

async function retry<T>(fn: () => Promise<T>, opts: RetryOptions = {}): Promise<T> {
  const { retries = 3, baseDelayMs = 200, shouldRetry = () => true, signal } = opts;
  let lastErr: unknown;
  for (let attempt = 0; attempt <= retries; attempt++) {
    signal?.throwIfAborted();
    try {
      return await fn();
    } catch (err) {
      lastErr = err;
      if (attempt === retries || !shouldRetry(err)) break;
      await delay(baseDelayMs * 2 ** attempt + Math.random() * 100);    // 指数退避 + 抖动
    }
  }
  throw lastErr;
}
```

只重试**可恢复**的错误（网络错误、429、5xx），4xx 参数错误重试没有意义。

<a id="ch05-s07"></a>

## 小结

- 并行用 `Promise.all`，大批量用并发池
- 所有耗时函数接收 `signal`，对外部调用设超时
- 流式用 `async function*` + `for await`
- 外部调用加重试 + 退避；别忘了 `await`

---

<a id="ch06"></a>

# 第 6 章　错误处理与运行时校验

**类型在运行时不存在。** 从系统边界进来的数据（HTTP、文件、环境变量、**LLM 输出**）不会因为你写了类型就变得可信，必须运行时校验。这是 Agent 开发里最容易出事故的地方。

<a id="ch06-s01"></a>

## 6.1 错误处理基础

JS 里可以 `throw` 任何东西，所以 `catch` 到的是 `unknown`，必须收窄：

```ts
function toMessage(e: unknown): string {
  if (e instanceof Error) return e.message;
  if (typeof e === "string") return e;
  try { return JSON.stringify(e); } catch { return String(e); }
}
```

自定义错误，用 `cause` 保留原始错误链：

```ts
class AppError extends Error {
  constructor(message: string, public readonly code: string, options?: { cause?: unknown }) {
    super(message, options);
    this.name = "AppError";
  }
}

try {
  JSON.parse("{bad");
} catch (e) {
  throw new AppError("配置解析失败", "CONFIG_INVALID", { cause: e });
}
```

不认识的错误**继续向上抛**，不要 `catch {}` 吞掉。

<a id="ch06-s02"></a>

## 6.2 throw 还是 Result

| 场景 | 用法 |
|---|---|
| 预期内的失败（校验不过、查不到、工具失败） | `Result` 类型，调用方被编译器强制处理 |
| 不该发生的错误（bug、基础设施崩溃） | `throw` |
| Agent 的工具执行失败 | 捕获后**转成文本返回给模型**，让它自己决定重试或换办法 |

```ts
type Result<T, E = Error> = { ok: true; value: T } | { ok: false; error: E };
const ok = <T>(value: T): Result<T, never> => ({ ok: true, value });
const err = <E>(error: E): Result<never, E> => ({ ok: false, error });

function parseJson(text: string): Result<unknown, string> {
  try { return ok(JSON.parse(text)); } catch { return err("invalid json"); }
}
```

<a id="ch06-s03"></a>

## 6.3 为什么需要运行时校验

```ts
interface User { id: number; name: string }

const res = await fetch("https://example.com/user");
const user = (await res.json()) as User;     // ⚠️ as 只是让编译器闭嘴，没有任何运行时保护
```

如果后端返回 `{ id: 1 }`，`user.name.toUpperCase()` 在运行时炸。**`as` 不是类型转换，只是撒谎。**

<a id="ch06-s04"></a>

## 6.4 zod：schema 即类型

`npm i zod`。写一份 schema，同时得到**运行时校验**和 **TS 类型**：

```ts
import { z } from "zod";

const UserSchema = z.object({
  id: z.number().int().positive(),
  name: z.string().min(1),
  email: z.string().email().optional(),
  role: z.enum(["admin", "user"]).default("user"),
});

type User = z.infer<typeof UserSchema>;
// { id: number; name: string; email?: string; role: "admin" | "user" }

const ok1 = UserSchema.parse({ id: 1, name: "A" });          // 失败直接 throw
const r = UserSchema.safeParse({ id: "x" });                  // 失败返回 { success: false, error }
if (r.success) console.log(r.data.name);
else console.log(r.error.issues);                             // 路径 + 原因
```

常用 schema：

```ts
z.string().min(1).max(100);
z.number().int().min(0);
z.enum(["a", "b"]);
z.array(z.string());
z.record(z.string(), z.number());
z.string().nullable();
z.string().optional();
z.string().describe("给模型看的字段说明");

// 可辨识联合：按 kind 分流
const Action = z.discriminatedUnion("kind", [
  z.object({ kind: z.literal("search"), query: z.string() }),
  z.object({ kind: z.literal("calc"), expr: z.string() }),
]);

// 字符串转数字（环境变量常用）
z.coerce.number().default(3000);
```

### 环境变量：启动时就校验

```ts
const Env = z.object({
  NODE_ENV: z.enum(["development", "production", "test"]).default("development"),
  PORT: z.coerce.number().default(3000),
  API_KEY: z.string().min(1),
});
export const env = Env.parse(process.env);       // 缺了就在启动时失败，而不是跑到一半
```

<a id="ch06-s05"></a>

## 6.5 校验 LLM 输出

**LLM 的输出（尤其是 JSON 与工具调用参数）永远不可信。** 流程：解析 → 校验 → 失败则把错误喂回模型让它修正。

```ts
const ToolCallSchema = z.object({
  name: z.string(),
  arguments: z.record(z.string(), z.unknown()),
});

function parseToolCall(raw: string): Result<z.infer<typeof ToolCallSchema>, string> {
  let json: unknown;
  try {
    json = JSON.parse(raw);
  } catch {
    return err("不是合法 JSON");
  }
  const r = ToolCallSchema.safeParse(json);
  if (r.success) return ok(r.data);
  return err(r.error.issues.map((i) => `${i.path.join(".") || "(root)"}: ${i.message}`).join("; "));
}
```

失败信息会作为工具结果回传给模型，它通常能据此自我修正。第 8 章就是这么做的。

<a id="ch06-s06"></a>

## 6.6 schema 转 JSON Schema，给模型当工具定义

模型 API 的工具定义要的是 JSON Schema。**一份 zod schema 同时服务三件事：给模型的描述、运行时校验、TS 类型。**

```ts
const WeatherArgs = z.object({
  city: z.string().describe("城市名，如 深圳"),
  unit: z.enum(["c", "f"]).default("c"),
});

const parameters = z.toJSONSchema(WeatherArgs);      // zod v4 内置
```

zod v3 需要第三方包 `zod-to-json-schema`。

<a id="ch06-s07"></a>

## 6.7 原则

| 原则 | 说明 |
|---|---|
| 只在**系统边界**校验 | HTTP、文件、环境变量、LLM 输出。内部函数之间信任类型，别处处校验 |
| 只维护 schema，不手写类型 | 类型用 `z.infer` 推出来，避免两份定义不一致 |
| 失败信息要可读 | 带上字段路径，既方便日志也方便喂回模型 |
| 服务端必须校验 | 不能信任客户端 |

<a id="ch06-s08"></a>

## 小结

- `catch` 到的是 `unknown`，先收窄；不认识的错误继续抛
- 预期内失败用 `Result`，工具失败转文本给模型
- `as` 不校验；边界数据用 zod `safeParse`
- schema 一份三用：类型、校验、工具定义

---

<a id="ch07"></a>

# 第 7 章　模块与工程

<a id="ch07-s01"></a>

## 7.1 模块（ESM）

含顶层 `import` / `export` 的文件就是模块。新项目一律 ESM：`package.json` 设 `"type": "module"`，`tsconfig` 用 `NodeNext`。

```ts
// math.ts
export const PI = 3.14;
export function add(a: number, b: number): number { return a + b; }
export interface Point { x: number; y: number }

// app.ts
import { add, PI } from "./math.js";           // 注意是 .js
import type { Point } from "./math.js";        // 仅类型，编译后擦除
import { type Point as P2, add as plus } from "./math.js";
```

三条规则：

| 规则 | 原因 |
|---|---|
| Node ESM 下**相对路径要写 `.js`**，即使源文件是 `.ts` | TS 不改写路径，运行时加载的是编译后的 `.js` |
| 优先**具名导出**，少用 `export default` | 重命名、重构更安全 |
| 仅类型的导入写 `import type` | 配合 `verbatimModuleSyntax`，导入行为清晰，避免循环依赖副作用 |

路径别名（`paths`）只影响类型检查，**不改写运行时路径**，运行时需要打包器或 `tsx` 支持。没有必要就别用。

<a id="ch07-s02"></a>

## 7.2 没有类型的 JS 库

三种情况：

| 情况 | 做法 |
|---|---|
| 库自带类型（zod、openai） | 直接用 |
| 有社区类型包 | `npm i -D @types/xxx` |
| 完全没类型 | 临时 `declare module "xxx";`（变成 `any`），再逐步补声明 |

<a id="ch07-s03"></a>

## 7.3 项目结构

```
my-agent/
├── src/
│   ├── index.ts          # 入口
│   ├── config.ts         # 环境变量（zod 校验）
│   ├── agent/            # 主循环、消息类型
│   ├── llm/              # LLM 接口与各厂商适配
│   └── tools/            # 工具，每个工具一个文件
├── tests/
├── package.json
└── tsconfig.json
```

原则：按功能分目录，一个文件一个主要职责，每个工具独立成文件、统一从 `tools/index.ts` 导出。

<a id="ch07-s04"></a>

## 7.4 测试：Vitest

```ts
// tests/retry.test.ts
import { describe, it, expect, vi } from "vitest";

describe("retry", () => {
  it("失败后重试成功", async () => {
    const fn = vi.fn()
      .mockRejectedValueOnce(new Error("boom"))
      .mockResolvedValue("ok");
    const run = async () => { try { return await fn(); } catch { return await fn(); } };
    expect(await run()).toBe("ok");
    expect(fn).toHaveBeenCalledTimes(2);
  });

  it("异步抛错", async () => {
    await expect(Promise.reject(new Error("x"))).rejects.toThrow("x");
  });
});
```

Agent 项目的测试分层：

| 层 | 做法 |
|---|---|
| 工具函数 | 纯函数直接单测 |
| Agent 循环 | 用**假 LLM**（脚本化返回固定的工具调用），验证流程（第 8 章） |
| 提示词效果 | 用评测集（eval），不是单测 |
| 真实 API | 单独的集成测试，默认不跑 |

<a id="ch07-s05"></a>

## 7.5 Lint

`npm i -D eslint typescript-eslint`。Agent 项目最值得开的几条规则：

| 规则 | 防什么 |
|---|---|
| `no-floating-promises` | 忘记 `await` |
| `no-misused-promises` | 把 async 函数传给不处理 Promise 的地方 |
| `switch-exhaustiveness-check` | 联合类型的 `switch` 漏分支 |
| `no-explicit-any` | 滥用 `any` |

<a id="ch07-s06"></a>

## 7.6 常见编译报错速查

| 报错 | 原因与对策 |
|---|---|
| TS2322 / TS2345：类型不能赋给… | 看两边类型；多半缺少收窄 |
| TS2339：属性不存在 | 拼写错、联合类型没收窄 |
| TS18048：可能为 `undefined` | 用 `?.`、`??` 或先判断 |
| TS7006：参数隐式 `any` | 给参数加类型 |
| TS2307：找不到模块 | 缺类型包；NodeNext 下相对路径漏写 `.js` |
| TS2353：对象字面量有多余属性 | 拼写错，或确实多写了 |


读长报错：**从最后一行往上读**，最后一行通常是根因。实在无法解决，用 `// @ts-expect-error 原因` 标注并留 TODO，**别随手 `as any`**。

<a id="ch07-s07"></a>

## 小结

- 全 ESM；相对导入写 `.js`；类型导入写 `import type`
- 项目按功能分目录，工具独立成文件
- 测试 Agent：假 LLM + 脚本化响应
- CI 里必须有 `tsc --noEmit`，因为打包器和 tsx 都不查类型

---

<a id="ch08"></a>

# 第 8 章　实战：从零写一个 Tool-calling Agent

把前面所有知识串起来：可辨识联合、泛型、接口、zod、async、错误处理。代码**无需 API Key 即可运行**（用假模型），最后接入真实模型。

建议把本章代码按顺序放进同一个文件 `agent.ts` 里跑通。

<a id="ch08-s01"></a>

## 8.1 Agent 的本质：一个循环

```
 1. 把「对话历史 + 工具列表」发给模型            
 2. 模型返回：最终文本  或  工具调用请求          
 3. 若是工具调用 → 本地执行 → 结果追加到历史      
 4. 回到 1，直到得到最终文本 或 达到最大步数       
```

所有 Agent 框架（LangGraph、OpenAI Agents SDK、Claude Agent SDK）都是在这个循环上叠加记忆、规划、多 Agent、护栏、可观测性。

**设计顺序：类型先行 → 工具 → 执行 → 循环 → 测试 → 接真实模型。**

<a id="ch08-s02"></a>

## 8.2 数据模型

```ts
import { z } from "zod";

type ToolCall = { id: string; name: string; arguments: unknown };

type Message =
  | { role: "system"; content: string }
  | { role: "user"; content: string }
  | { role: "assistant"; content: string; toolCalls?: ToolCall[] }
  | { role: "tool"; toolCallId: string; name: string; content: string };

type ModelResponse =
  | { type: "text"; content: string }
  | { type: "tool_calls"; calls: ToolCall[] };

interface ToolDescriptor {
  name: string;
  description: string;
  parameters: unknown;        // JSON Schema
}

// 只依赖接口：测试用假模型，上线换真模型
interface LLM {
  complete(
    messages: readonly Message[],
    tools: readonly ToolDescriptor[],
    opts?: { signal?: AbortSignal },
  ): Promise<ModelResponse>;
}
```

要点：消息和模型响应都是**可辨识联合**，`switch` 就能精确收窄；`ToolCall.arguments` 是 `unknown`，因为它来自模型，不可信。

<a id="ch08-s03"></a>

## 8.3 工具：一份 schema，三种用途

`defineTool` 让 TS 从 `schema` 自动推断 `run` 的参数类型：

```ts
interface Tool<TArgs extends z.ZodType = z.ZodType> {
  name: string;
  description: string;
  schema: TArgs;
  dangerous?: boolean;                       // 需要人工确认的工具
  run(args: z.infer<TArgs>, ctx: { signal?: AbortSignal }): Promise<string>;
}

function defineTool<TArgs extends z.ZodType>(tool: Tool<TArgs>): Tool<TArgs> {
  return tool;
}

const calculator = defineTool({
  name: "calculator",
  description: "计算两个数的四则运算",
  schema: z.object({
    a: z.number(),
    b: z.number(),
    op: z.enum(["add", "sub", "mul", "div"]),
  }),
  async run({ a, b, op }) {                  // 参数类型自动推断
    switch (op) {
      case "add": return String(a + b);
      case "sub": return String(a - b);
      case "mul": return String(a * b);
      case "div":
        if (b === 0) throw new Error("除数不能为 0");
        return String(a / b);
    }
  },
});

const getWeather = defineTool({
  name: "get_weather",
  description: "查询城市天气",
  schema: z.object({ city: z.string().describe("城市名，如 深圳") }),
  async run({ city }) {
    return JSON.stringify({ city, temp: 26, desc: "晴" });
  },
});
```

注册表：把各种具体类型的工具统一存放，并导出给模型看的描述：

```ts
class ToolRegistry {
  private readonly tools = new Map<string, Tool>();

  register(...tools: Tool<any>[]): this {
    for (const t of tools) this.tools.set(t.name, t);
    return this;
  }

  get(name: string): Tool | undefined {
    return this.tools.get(name);
  }

  descriptors(): ToolDescriptor[] {
    return [...this.tools.values()].map((t) => ({
      name: t.name,
      description: t.description,
      parameters: z.toJSONSchema(t.schema),
    }));
  }
}
```

<a id="ch08-s04"></a>

## 8.4 安全地执行工具

原则：**工具调用来自不可信的模型，必须校验；失败要变成"给模型看的文本"，不能让整个 Agent 崩溃。**

```ts
interface ExecOptions {
  signal?: AbortSignal;
  approve?: (call: ToolCall) => Promise<boolean>;     // 危险工具的人工确认
}

async function executeTool(registry: ToolRegistry, call: ToolCall, opts: ExecOptions = {}): Promise<string> {
  const tool = registry.get(call.name);
  if (!tool) return `错误：不存在名为 ${call.name} 的工具`;

  const parsed = tool.schema.safeParse(call.arguments);
  if (!parsed.success) {
    const detail = parsed.error.issues
      .map((i) => `${i.path.join(".") || "(root)"}: ${i.message}`)
      .join("; ");
    return `错误：参数不合法 —— ${detail}`;                // 反馈给模型，让它自行修正
  }

  if (tool.dangerous && !(await opts.approve?.(call))) {
    return "错误：用户拒绝了该操作";
  }

  try {
    return await tool.run(parsed.data, { signal: opts.signal });
  } catch (e) {
    if (opts.signal?.aborted) throw e;                    // 用户取消：向上传播
    return `错误：工具执行失败 —— ${e instanceof Error ? e.message : String(e)}`;
  }
}
```

<a id="ch08-s05"></a>

## 8.5 主循环

```ts
interface AgentOptions {
  llm: LLM;
  registry: ToolRegistry;
  systemPrompt?: string;
  maxSteps?: number;
  approve?: ExecOptions["approve"];
  onEvent?: (e: AgentEvent) => void;
}

type AgentEvent =
  | { type: "model_response"; step: number; response: ModelResponse }
  | { type: "tool_start"; call: ToolCall }
  | { type: "tool_end"; call: ToolCall; output: string };

type AgentResult =
  | { status: "done"; answer: string; messages: Message[] }
  | { status: "max_steps"; messages: Message[] };

async function runAgent(userInput: string, opts: AgentOptions, signal?: AbortSignal): Promise<AgentResult> {
  const { llm, registry, maxSteps = 8, onEvent } = opts;
  const messages: Message[] = [
    { role: "system", content: opts.systemPrompt ?? "你是一个乐于助人的助手，必要时调用工具。" },
    { role: "user", content: userInput },
  ];

  for (let step = 1; step <= maxSteps; step++) {
    signal?.throwIfAborted();

    const response = await llm.complete(messages, registry.descriptors(), { signal });
    onEvent?.({ type: "model_response", step, response });

    switch (response.type) {
      case "text":
        messages.push({ role: "assistant", content: response.content });
        return { status: "done", answer: response.content, messages };

      case "tool_calls": {
        messages.push({ role: "assistant", content: "", toolCalls: response.calls });

        const outputs = await Promise.all(            // 同一轮的多个调用并行执行
          response.calls.map(async (call) => {
            onEvent?.({ type: "tool_start", call });
            const output = await executeTool(registry, call, { signal, approve: opts.approve });
            onEvent?.({ type: "tool_end", call, output });
            return { call, output };
          }),
        );
        for (const { call, output } of outputs) {
          messages.push({ role: "tool", toolCallId: call.id, name: call.name, content: output });
        }
        break;
      }
    }
  }
  return { status: "max_steps", messages };           // 防止模型死循环烧钱
}
```

设计细节：

| 设计 | 作用 |
|---|---|
| `maxSteps` | 兜底，防死循环 |
| `signal` 贯穿 | 随时可取消 |
| 工具错误转文本 | 模型可自我修正，流程不崩 |
| `Promise.all` | 同轮多个工具调用并行 |
| `onEvent` | 解耦"过程"与"展示"，便于做 UI、日志、测试 |
| 返回完整 `messages` | 可持久化会话、继续对话 |
| `switch` 不写 `default` | 配合 lint 的穷尽检查，新增响应类型时编译器会提醒 |

<a id="ch08-s06"></a>

## 8.6 用假模型跑起来

```ts
class ScriptedLLM implements LLM {
  private i = 0;
  constructor(private readonly script: ((messages: readonly Message[]) => ModelResponse)[]) {}

  async complete(messages: readonly Message[]): Promise<ModelResponse> {
    const next = this.script[this.i++];
    if (!next) throw new Error("脚本已耗尽");
    return next(messages);
  }
}

const scripted = new ScriptedLLM([
  () => ({                                         // 第 1 轮：同时调用两个工具
    type: "tool_calls",
    calls: [
      { id: "c1", name: "get_weather", arguments: { city: "深圳" } },
      { id: "c2", name: "calculator", arguments: { a: 6, b: 7, op: "mul" } },
    ],
  }),
  (messages) => ({                                 // 第 2 轮：读到工具结果，给出最终回答
    type: "text",
    content: "汇总：" + messages.filter((m) => m.role === "tool").map((m) => m.content).join(" | "),
  }),
]);

const registry = new ToolRegistry().register(calculator, getWeather);
const result = await runAgent("深圳天气如何？顺便算 6×7", {
  llm: scripted,
  registry,
  onEvent: (e) => console.log(e.type),
});
if (result.status === "done") console.log(result.answer);
```

<a id="ch08-s07"></a>

## 8.7 测试

```ts
import { it, expect } from "vitest";

it("参数不合法时，错误反馈给模型而不是崩溃", async () => {
  const llm = new ScriptedLLM([
    () => ({ type: "tool_calls", calls: [{ id: "c1", name: "calculator", arguments: { a: "x" } }] }),
    (messages) => {
      const last = messages.at(-1);
      return { type: "text", content: last?.role === "tool" ? last.content : "没有工具消息" };
    },
  ]);
  const r = await runAgent("算一下", { llm, registry: new ToolRegistry().register(calculator) });
  expect(r.status).toBe("done");
  if (r.status === "done") expect(r.answer).toContain("参数不合法");
});

it("超过最大步数应当终止", async () => {
  const endless = new ScriptedLLM(
    Array.from({ length: 10 }, () => () => ({
      type: "tool_calls" as const,
      calls: [{ id: "x", name: "get_weather", arguments: { city: "A" } }],
    })),
  );
  const r = await runAgent("loop", { llm: endless, registry: new ToolRegistry().register(getWeather), maxSteps: 3 });
  expect(r.status).toBe("max_steps");
});
```

<a id="ch08-s08"></a>

## 8.8 接入真实模型

只需实现 `LLM` 接口，业务代码一行不改。下面是兼容 OpenAI Chat Completions 的实现（国内多数厂商同一格式，改 `baseUrl` 和 `model` 即可）：

```ts
const WireResponse = z.object({
  choices: z.array(z.object({
    message: z.object({
      content: z.string().nullable().optional(),
      tool_calls: z.array(z.object({
        id: z.string(),
        function: z.object({ name: z.string(), arguments: z.string() }),
      })).optional(),
    }),
  })).min(1),
});

function toWire(m: Message) {
  switch (m.role) {
    case "assistant":
      return {
        role: "assistant",
        content: m.content,
        tool_calls: m.toolCalls?.map((c) => ({
          id: c.id,
          type: "function",
          function: { name: c.name, arguments: JSON.stringify(c.arguments) },
        })),
      };
    case "tool":
      return { role: "tool", tool_call_id: m.toolCallId, content: m.content };
    default:
      return { role: m.role, content: m.content };
  }
}

function safeJson(s: string): unknown {
  try { return JSON.parse(s); } catch { return s; }     // 解析失败就原样传下去，让 schema 校验报错并反馈给模型
}

class OpenAICompatibleLLM implements LLM {
  constructor(
    private readonly baseUrl: string,
    private readonly apiKey: string,
    private readonly model: string,
  ) {}

  async complete(
    messages: readonly Message[],
    tools: readonly ToolDescriptor[],
    opts?: { signal?: AbortSignal },
  ): Promise<ModelResponse> {
    const signal = AbortSignal.any([opts?.signal, AbortSignal.timeout(60_000)].filter((s): s is AbortSignal => !!s));
    const res = await fetch(`${this.baseUrl}/chat/completions`, {
      method: "POST",
      headers: { "Content-Type": "application/json", Authorization: `Bearer ${this.apiKey}` },
      signal,
      body: JSON.stringify({
        model: this.model,
        messages: messages.map(toWire),
        tools: tools.length ? tools.map((t) => ({ type: "function", function: t })) : undefined,
      }),
    });
    if (!res.ok) throw new Error(`LLM HTTP ${res.status}: ${await res.text()}`);

    const msg = WireResponse.parse(await res.json()).choices[0]!.message;     // 边界处校验
    if (msg.tool_calls?.length) {
      return {
        type: "tool_calls",
        calls: msg.tool_calls.map((c) => ({
          id: c.id,
          name: c.function.name,
          arguments: safeJson(c.function.arguments),
        })),
      };
    }
    return { type: "text", content: msg.content ?? "" };
  }
}

// const llm = new OpenAICompatibleLLM("https://api.openai.com/v1", process.env.API_KEY!, "gpt-4o");
```


这里体现了前面几章的几乎所有要点：边界处用 zod 校验、`unknown` 承载不可信数据、超时与取消合并、`switch` 按角色收窄。外部调用建议再套一层第 5 章的 `retry`。

<a id="ch08-s09"></a>

## 8.9 事件流式输出

把 `onEvent` 回调改成 `async function*`，调用方用 `for await` 消费，更适合接 UI 或 SSE：

```ts
async function* runAgentStream(
  userInput: string,
  opts: Omit<AgentOptions, "onEvent">,
  signal?: AbortSignal,
): AsyncGenerator<AgentEvent, AgentResult> {
  const { llm, registry, maxSteps = 8 } = opts;
  const messages: Message[] = [
    { role: "system", content: opts.systemPrompt ?? "你是一个乐于助人的助手。" },
    { role: "user", content: userInput },
  ];

  for (let step = 1; step <= maxSteps; step++) {
    signal?.throwIfAborted();
    const response = await llm.complete(messages, registry.descriptors(), { signal });
    yield { type: "model_response", step, response };

    if (response.type === "text") {
      messages.push({ role: "assistant", content: response.content });
      return { status: "done", answer: response.content, messages };
    }

    messages.push({ role: "assistant", content: "", toolCalls: response.calls });
    for (const call of response.calls) {
      yield { type: "tool_start", call };
      const output = await executeTool(registry, call, { signal, approve: opts.approve });
      yield { type: "tool_end", call, output };
      messages.push({ role: "tool", toolCallId: call.id, name: call.name, content: output });
    }
  }
  return { status: "max_steps", messages };
}

// 消费：for await 拿不到最终返回值，需要手动调用 next()
const gen = runAgentStream("深圳天气？", {
  llm: new ScriptedLLM([
    () => ({ type: "tool_calls", calls: [{ id: "c1", name: "get_weather", arguments: { city: "深圳" } }] }),
    () => ({ type: "text", content: "晴，26 度" }),
  ]),
  registry,
});
let step = await gen.next();
while (!step.done) {
  console.log("事件:", step.value.type);
  step = await gen.next();
}
console.log("最终:", step.value.status);
```

这里是**事件级**流式。**token 级**流式是给 `LLM` 加一个 `stream()` 方法，返回 `AsyncIterable<文本增量>`，解析方式见 5.5 的 SSE 示例。

<a id="ch08-s10"></a>

## 8.10 护栏清单

上线前逐项检查：

| 风险 | 对策 |
|---|---|
| 模型死循环、烧钱 | `maxSteps`；累计 token / 成本上限 |
| 参数乱填 | zod 校验，错误回传给模型 |
| 危险操作（删文件、发消息、花钱） | `dangerous: true` + `approve` 回调人工确认 |
| 请求挂起 | 每次模型与工具调用都设超时 |
| 用户想中止 | `AbortSignal` 全程透传 |
| 提示注入（工具返回的内容里夹带指令） | 工具输出视为**数据而非指令**；限制工具权限；敏感操作必须人工确认 |
| 密钥泄露 | 密钥只放环境变量；日志脱敏；不进提示词 |
| 上下文过长 | 截断或摘要旧消息；限制单个工具输出长度 |

<a id="ch08-s11"></a>

## 8.11 还能往哪扩展

| 方向 | 要点 |
|---|---|
| MCP | 用标准协议接入现成工具：官方 SDK `@modelcontextprotocol/sdk`，把 MCP 工具适配成本章的 `Tool` 即可 |
| 记忆 | 对话压缩、向量检索，抽象成 `Memory` 接口 |
| 多 Agent | 把子 Agent 包装成一个 `Tool` |
| 可观测性 | 事件流接日志 / tracing，记录每步耗时与 token |
| 持久化 | `messages` 本身可序列化，存起来即可断点续跑 |
| 现成框架 | Vercel AI SDK、Mastra、LangGraph.js、OpenAI Agents SDK、Claude Agent SDK |

**先手写一遍本章的循环，再看框架，你会更清楚框架替你做了什么。**

<a id="ch08-s12"></a>

## 练习

1. 给 `executeTool` 加超时：用 `AbortSignal.timeout` 与用户的 `signal` 合并
2. 实现一个真实的 `search` 工具：调用某个 HTTP API，并用 zod 校验返回值
3. 给 `LLM` 加 `stream()` 方法，用 5.5 的 `sseData` 实现 token 级流式
4. 让工具并行改为可配置：`parallel: boolean`，串行时按顺序执行并 yield 事件

---

<a id="ch09"></a>

# 附录

<a id="ch09-s01"></a>

## 附录 A　Python → TypeScript → Go 对照

| Python | TypeScript | Go |
|---|---|---|
| `x: int = 1` | `const x: number = 1` | `x := 1`（或 `var x int = 1`） |
| `list[int]` / `dict[str, int]` | `number[]` / `Record<string, number>`（或 `Map`） | `[]int` / `map[string]int` |
| `tuple[str, int]` | `[string, number]` | 无元组，用多返回值 `(string, int)` 或 `struct` |
| `Optional[str]` | `string \| undefined` | `*string`（指针，`nil` 表无值） |
| `Union[int, str]` | `number \| string` | 无原生联合，用 `any` 或 sealed interface |
| `Literal["a", "b"]` | `"a" \| "b"` | `type Mode string` + 常量 |
| `Any` | `any`（尽量用 `unknown`） | `any`（即 `interface{}`） |
| `TypeVar("T")` | `<T>` | `[T any]`（泛型，Go 1.18+） |
| `Protocol` / `TypedDict` | `interface`（结构化类型天然支持） | `interface`（方法集，**隐式实现**） |
| `Enum` | 字面量联合 + `as const` | `iota` 常量组 + 自定义类型 |
| `pydantic.BaseModel` | `zod` schema + `z.infer` | `struct` + tag + `encoding/json`（校验用 validator 库） |
| `f"hi {name}"` | `` `hi ${name}` `` | `fmt.Sprintf("hi %s", name)` |
| `[x*2 for x in xs]` | `xs.map(x => x * 2)` | `for` 循环（1.21+ 可用 `slices`） |
| `[x for x in xs if x > 0]` | `xs.filter(x => x > 0)` | `for` + `append` |
| `{**a, **b}` | `{ ...a, ...b }` | `maps.Copy(dst, src)`（1.21+） |
| `d.get(k, default)` | `obj[k] ?? default` | `v, ok := m[k]; if !ok { v = default }` |
| `for k, v in d.items()` | `for (const [k, v] of Object.entries(obj))` | `for k, v := range m` |
| `async def` / `await` | `async function` / `await` | goroutine + channel（无 async/await） |
| `asyncio.gather(*ts)` | `Promise.all(ts)` | `sync.WaitGroup` 或 `errgroup.Group` |
| `raise ValueError("x")` | `throw new Error("x")` | `return fmt.Errorf("x")`（错误是值） |
| `try/except E as e` | `try/catch (e)`，`e` 是 `unknown` | `if err != nil { ... }`（panic 仅用于不可恢复） |
| `json.loads(s)` | `JSON.parse(s)`（返回 `any`，务必校验） | `json.Unmarshal([]byte(s), &v)` |
| `pytest` | `vitest` | `go test`（标准库 `testing`） |
| `pip` / venv | `npm` / `pnpm` + `node_modules` | `go mod` / `go get` |

思维差异（TypeScript 相对 Python）：

1. Python 类型提示不强制，TS 类型检查在编译期**强制**，但同样运行时不存在
2. TS 是**结构化类型**，只看形状，不看名字
3. JS 有 `null` 和 `undefined` 两个空值，有 `==` 隐式转换、`this` 丢失这类坑
4. 数字只有 `number`；对象既是实例也是字典，严格的键值表用 `Map`
5. `[] === []` 为 `false`，比较的是引用

思维差异（Go 相对前两者）：

1. **错误是值，不是异常**：没有 `try/catch`，函数用多返回值 `(T, error)` 显式传播错误，`if err != nil` 是主旋律；`panic`/`recover` 只留给真正不可恢复的情形
2. **并发是 goroutine + channel**（CSP 模型），不是 async/await：信条是"不要通过共享内存来通信，而要通过通信来共享内存"
3. **接口隐式实现**：类型只要拥有对应方法集就自动满足接口，无需 `implements` 声明——和 TS 的结构化类型异曲同工，但作用于方法而非字段
4. **零值可用**：变量声明即带确定零值（`0`/`""`/`nil`/`false`），不像 JS 有 `undefined`/`null` 两套空值
5. **没有继承，只有组合**：通过 struct 嵌入复用，没有类层级
6. **类型系统刻意精简**：无联合类型、无三元运算符、无默认参数；泛型直到 1.18 才加入，枚举要靠 `iota` 模拟

<a id="ch09-s02"></a>

## 附录 B　速查

### 类型语法

```ts
type A = string | number;                       // 联合
type B = { a: number } & { b: string };        // 交叉
type C = "get" | "post";                        // 字面量联合
type D = (x: number) => string;                 // 函数
type E = [string, number];                      // 元组
type F = Record<string, number>;                // 字典
function f<T extends object, K extends keyof T>(x: T, k: K): T[K] { return x[k]; }
```

### 选择指南

| 需求 | 用什么 |
|---|---|
| 描述对象形状 | `interface` 或 `type` |
| 外部数据（不知道类型） | `unknown` + zod 校验 |
| 状态机 / 消息 / 事件 | 可辨识联合 + `never` 穷尽检查 |
| 固定的几个取值 | 字面量联合 + `as const`（不用 `enum`） |
| 输入输出类型关联 | 泛型 |
| 既检查又保留精确类型 | `satisfies` |
| 并行 / 限流 / 取消 / 超时 | `Promise.all` / 并发池 / `AbortSignal` |
| 预期内的失败 | `Result` |
| 依赖外部服务 | 定义接口，注入实现，测试用假实现 |

<a id="ch09-s03"></a>

<!-- ## 附录 C　检查清单

读完后对照：

- [ ] 能解释为什么类型在运行时不存在，以及这意味着要校验外部数据
- [ ] 能用可辨识联合 + `never` 设计消息与状态类型
- [ ] 能写带约束的泛型函数，如 `K extends keyof T`
- [ ] 能用 zod 定义 schema，并 `z.infer` 出类型、转成 JSON Schema
- [ ] 能正确处理并发、取消、超时、重试
- [ ] 能手写第 8 章的 Agent 循环，并用假模型测试
- [ ] 能把假模型换成真实模型，说清楚每一步的校验在哪
- [ ] 能说出 Agent 上线前至少 5 项护栏 -->

<a id="ch09-s04"></a>

## 附录 C　延伸阅读

| 资源 | 说明 |
|---|---|
| TypeScript 官方 Handbook | 语言细节的权威来源 |
| TypeScript Playground | 在线写代码并查看推断结果 |
| 《Effective TypeScript》 | 进阶：62 条具体建议 |
| type-challenges | 想练类型体操时再看 |
| Anthropic《Building Effective Agents》 | Agent 设计模式 |
| MCP 官方文档 | 工具接入的标准协议 |
