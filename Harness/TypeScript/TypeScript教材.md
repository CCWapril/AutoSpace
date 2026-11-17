# TypeScript 从入门到 Agent 实战

> 前言 + 13 章 + 附录，代码均经 tsc --strict 校验。

## 目录

- [**前言与学习路线**](#ch00)
  - [0.1 这本教材适合谁](#ch00-s01)
  - [0.2 怎么用这本教材](#ch00-s02)
  - [0.3 知识地图](#ch00-s03)
  - [0.4 建议学习节奏](#ch00-s04)
  - [0.5 一个先导例子：TS 到底帮你做了什么](#ch00-s05)
- [**第 1 章　TypeScript 是什么与环境搭建**](#ch01)
  - [1.1 TypeScript 是什么](#ch01-s01)
  - [1.2 为什么需要 TS](#ch01-s02)
  - [1.3 先补 JS 必备知识（10 分钟速通）](#ch01-s03)
  - [1.4 安装与创建项目](#ch01-s04)
  - [1.5 tsconfig.json 详解](#ch01-s05)
  - [1.6 类型检查的"工作流"](#ch01-s06)
  - [1.7 常见坑](#ch01-s07)
  - [本章小结](#ch01-s08)
  - [练习](#ch01-s09)
- [**第 2 章　基础类型与类型推断**](#ch02)
  - [2.1 类型标注的基本语法](#ch02-s01)
  - [2.2 原始类型（Primitive Types）](#ch02-s02)
  - [2.3 类型推断（Type Inference）](#ch02-s03)
  - [2.4 数组与元组](#ch02-s04)
  - [2.5 对象类型（初识）](#ch02-s05)
  - [2.6 any、unknown、never、void —— 四个特殊类型](#ch02-s06)
  - [2.7 null 与 undefined（strictNullChecks 的威力）](#ch02-s07)
  - [2.8 字面量类型与 `as const`](#ch02-s08)
  - [2.9 类型别名 `type`（初识）](#ch02-s09)
  - [2.10 类型断言（as）与它的风险](#ch02-s10)
  - [2.11 常见坑](#ch02-s11)
  - [本章小结](#ch02-s12)
  - [练习](#ch02-s13)
- [**第 3 章　函数**](#ch03)
  - [3.1 参数与返回值类型](#ch03-s01)
  - [3.2 可选参数、默认参数、剩余参数](#ch03-s02)
  - [3.3 函数类型的表示方法](#ch03-s03)
  - [3.4 `void` 返回类型的特殊性](#ch03-s04)
  - [3.5 函数重载（Overloads）](#ch03-s05)
  - [3.6 `this` 的类型](#ch03-s06)
  - [3.7 回调函数的类型](#ch03-s07)
  - [3.8 泛型函数初识](#ch03-s08)
  - [3.9 参数的变体（进阶：协变与逆变）](#ch03-s09)
  - [3.10 常见坑](#ch03-s10)
  - [本章小结](#ch03-s11)
  - [练习](#ch03-s12)
- [**第 4 章　对象类型：interface 与 type**](#ch04)
  - [4.1 内联对象类型](#ch04-s01)
  - [4.2 interface](#ch04-s02)
  - [4.3 type（类型别名）](#ch04-s03)
  - [4.4 interface 与 type 的区别（面试高频）](#ch04-s04)
  - [4.5 扩展与组合](#ch04-s05)
  - [4.6 索引签名（Index Signature）](#ch04-s06)
  - [4.7 多余属性检查（Excess Property Check）](#ch04-s07)
  - [4.8 结构化类型系统（Structural Typing）](#ch04-s08)
  - [4.9 进阶：品牌类型（Branded Type）](#ch04-s09)
  - [4.10 常用的内置对象类型](#ch04-s10)
  - [4.11 嵌套与复杂对象的建模例子](#ch04-s11)
  - [4.12 常见坑](#ch04-s12)
  - [本章小结](#ch04-s13)
  - [练习](#ch04-s14)
- [**第 5 章　联合类型、交叉类型与类型收窄**](#ch05)  
  <!-- |  |  |  
  | --- | --- | -->
  - [5.1 联合类型 `|`（A 或 B）](#ch05-s01)
  - [5.2 类型收窄（Narrowing）](#ch05-s02)
  - [5.3 可辨识联合（Discriminated Union）⭐](#ch05-s03)
  - [5.4 交叉类型 `&`（A 且 B）](#ch05-s04)
  - [5.5 字面量类型联合：替代 enum 的首选方式](#ch05-s05)
  - [5.6 联合类型的"分配"行为](#ch05-s06)
  - [5.7 常见坑](#ch05-s07)
  - [本章小结](#ch05-s08)
  - [练习](#ch05-s09)
- [**第 6 章　泛型（Generics）**](#ch06)
  - [6.1 为什么需要泛型](#ch06-s01)
  - [6.2 泛型函数](#ch06-s02)
  - [6.3 泛型约束 `extends`](#ch06-s03)
  - [6.4 泛型接口与类型别名](#ch06-s04)
  - [6.5 泛型类](#ch06-s05)
  - [6.6 泛型的推断规则与常见技巧](#ch06-s06)
  - [6.7 泛型实战：给"工具（Tool）"建模](#ch06-s07)
  - [6.8 泛型与"类型体操"的边界](#ch06-s08)
  - [6.9 常见坑](#ch06-s09)
  - [本章小结](#ch06-s10)
  - [练习](#ch06-s11)
- [**第 7 章　类（Class）与面向对象**](#ch07)
  - [7.1 基本写法](#ch07-s01)
  - [7.2 参数属性（Parameter Properties）：最常用的简写](#ch07-s02)
  - [7.3 访问修饰符](#ch07-s03)
  - [7.4 继承与 `override`](#ch07-s04)
  - [7.5 抽象类（Abstract Class）](#ch07-s05)
  - [7.6 实现接口：`implements`](#ch07-s06)
  - [7.7 静态成员与 getter/setter](#ch07-s07)
  - [7.8 类即类型](#ch07-s08)
  - [7.9 `this` 类型与链式调用](#ch07-s09)
  - [7.10 Mixin（了解）](#ch07-s10)
  - [7.11 类 vs 函数式：什么时候用类](#ch07-s11)
  - [7.12 装饰器（简述）](#ch07-s12)
  - [7.13 常见坑](#ch07-s13)
  - [本章小结](#ch07-s14)
  - [练习](#ch07-s15)
- [**第 8 章　类型运算：keyof、条件类型、映射类型与工具类型**](#ch08)
  - [8.1 `typeof`（类型位置）：从值得到类型](#ch08-s01)
  - [8.2 `keyof`：取对象类型的所有键](#ch08-s02)
  - [8.3 索引访问类型 `T[K]`](#ch08-s03)
  - [8.4 映射类型（Mapped Types）](#ch08-s04)
  - [8.5 条件类型（Conditional Types）](#ch08-s05)
  - [8.6 模板字面量类型](#ch08-s06)
  - [8.7 内置工具类型（Utility Types）速查](#ch08-s07)
  - [8.8 `satisfies` 运算符（TS 4.9+）](#ch08-s08)
  - [8.9 递归类型](#ch08-s09)
  - [8.10 综合实战：做几个实用的类型工具](#ch08-s10)
  - [8.11 类型体操的"自我保护"准则](#ch08-s11)
  - [8.12 常见坑](#ch08-s12)
  - [本章小结](#ch08-s13)
  - [练习](#ch08-s14)
- [**第 9 章　枚举、模块系统与声明文件**](#ch09)
  - [9.1 枚举（enum）](#ch09-s01)
  - [9.2 模块系统](#ch09-s02)
  - [9.3 命名空间（namespace）](#ch09-s03)
  - [9.4 声明文件（`.d.ts`）](#ch09-s04)
  - [9.5 三斜线指令（了解）](#ch09-s05)
  - [9.6 JSON 导入](#ch09-s06)
  - [9.7 常见坑](#ch09-s07)
  - [本章小结](#ch09-s08)
  - [练习](#ch09-s09)
- [**第 10 章　异步编程：Promise、async/await 与流**](#ch10)
  - [10.1 JS 的并发模型（一分钟版）](#ch10-s01)
  - [10.2 Promise](#ch10-s02)
  - [10.3 async / await](#ch10-s03)
  - [10.4 并发控制：串行 vs 并行](#ch10-s04)
  - [10.5 常见异步陷阱](#ch10-s05)
  - [10.6 取消：AbortController](#ch10-s06)
  - [10.7 异步迭代器与流式输出](#ch10-s07)
  - [10.8 重试与退避（Agent 必备）](#ch10-s08)
  - [10.9 事件循环里的"微任务饥饿"（了解）](#ch10-s09)
  - [10.10 常见坑速查](#ch10-s10)
  - [本章小结](#ch10-s11)
  - [练习](#ch10-s12)
- [**第 11 章　错误处理与运行时校验**](#ch11)
  - [11.1 JS 的错误机制](#ch11-s01)
  - [11.2 自定义错误类](#ch11-s02)
  - [11.3 两种错误处理风格](#ch11-s03)
  - [11.4 为什么需要运行时校验](#ch11-s04)
  - [11.5 手写校验的痛点](#ch11-s05)
  - [11.6 zod：最流行的运行时校验库](#ch11-s06)
  - [11.7 Agent 场景：校验 LLM 输出](#ch11-s07)
  - [11.8 类型层面防止"忘记处理错误"](#ch11-s08)
  - [11.9 常见坑](#ch11-s09)
  - [本章小结](#ch11-s10)
  - [练习](#ch11-s11)
- [**第 12 章　工程实践：项目结构、Lint、测试与构建**](#ch12)
  - [12.1 推荐的项目结构](#ch12-s01)
  - [12.2 package.json 与脚本](#ch12-s02)
  - [12.3 tsconfig 进阶配置](#ch12-s03)
  - [12.4 ESLint：代码质量守门员](#ch12-s04)
  - [12.5 测试](#ch12-s05)
  - [12.6 构建与打包](#ch12-s06)
  - [12.7 依赖管理](#ch12-s07)
  - [12.8 Git 与 CI 示例](#ch12-s08)
  - [12.9 日志与配置](#ch12-s09)
  - [12.10 性能与类型检查速度](#ch12-s10)
  - [12.11 渐进迁移：JS 项目 → TS](#ch12-s11)
  - [12.12 编码规范精要](#ch12-s12)
  - [本章小结](#ch12-s13)
  - [练习](#ch12-s14)
- [**第 13 章　综合实战：用 TypeScript 写一个 Tool-calling Agent**](#ch13)
  - [13.1 Agent 是什么（极简模型）](#ch13-s01)
  - [13.2 第一步：设计数据模型（类型先行）](#ch13-s02)
  - [13.3 第二步：定义"工具"（泛型 + zod）](#ch13-s03)
  - [13.4 第三步：安全地执行工具](#ch13-s04)
  - [13.5 第四步：Agent 主循环](#ch13-s05)
  - [13.6 第五步：写一个 Mock LLM，让它跑起来](#ch13-s06)
  - [13.7 第六步：写测试验证行为](#ch13-s07)
  - [13.8 接入真实模型](#ch13-s08)
  - [13.9 还能怎么扩展（学习路线）](#ch13-s09)
  - [13.10 本章回顾：每个知识点用在了哪](#ch13-s10)
  - [练习](#ch13-s11)
- [**附录**](#ch14)
  - [附录 A　Python → TypeScript 对照速查](#ch14-s01)
  - [附录 B　TypeScript 速查表](#ch14-s02)
  - [附录 C　常见编译错误速查](#ch14-s03)
  - [附录 D　部分练习参考思路](#ch14-s04)
  - [附录 E　推荐学习资源](#ch14-s05)
  - [学习检查清单](#ch14-s06)

---

<a id="ch00"></a>

# 前言与学习路线

<a id="ch00-s01"></a>

## 0.1 这本教材适合谁

- 会一点 JavaScript，或者**只会 Python / 其他语言**，想系统学 TypeScript 的人
- 想用 TypeScript 写 **Agent、MCP Server、CLI、Web 应用** 的工程师
- 看得懂 TS 代码，但遇到 `Partial<Pick<T, K>>`、条件类型就发怵的人

不需要提前精通 JS，但需要知道变量、函数、对象、数组、`if/for` 这些最基本概念。JS 里必须知道的部分，第 1 章会补。

<a id="ch00-s02"></a>

## 0.2 怎么用这本教材

每章结构统一：

1. **是什么**：一句话讲清概念
2. **为什么需要**：它解决什么问题
3. **怎么用**：带可运行代码的详细讲解
4. **常见坑**：新手最容易踩的地方
5. **本章小结 + 练习**：巩固用

> 代码块中，带 `// ❌` 注释的行表示**会报编译错误**，这是故意写的反例。其余代码均已用 `tsc --strict` 编译通过。

<a id="ch00-s03"></a>

## 0.3 知识地图

```
第一阶段：入门（第 1-3 章）
  环境与编译 → 基础类型 → 函数
第二阶段：核心（第 4-7 章）
  对象类型 → 联合/交叉/收窄 → 泛型 → 类
第三阶段：进阶（第 8-9 章）
  类型运算（keyof / 条件类型 / 映射类型 / 工具类型）→ 模块与声明文件
第四阶段：工程（第 10-13 章）
  异步 → 错误处理与运行时校验 → 工程配置 → Agent 实战
附录
  速查表 / 常见报错 / 练习答案思路
```

<a id="ch00-s04"></a>

## 0.4 建议学习节奏

| 阶段 | 内容        | 建议时间  | 目标                           |
| -- | --------- | ----- | ---------------------------- |
| 入门 | 第 1-3 章   | 2-3 天 | 能写带类型的函数和脚本                  |
| 核心 | 第 4-7 章   | 1 周   | 能给真实项目的数据建模                  |
| 进阶 | 第 8-9 章   | 1 周   | 能读懂并写出常见泛型工具类型               |
| 工程 | 第 10-13 章 | 1 周   | 能搭完整项目，写出 tool-calling Agent |

**核心心法**：TypeScript 不是"另一门语言"，而是 **给 JS 加上一层"类型说明书 + 检查器"**。学习重点不在语法有多少，而在**如何用类型描述你的数据和行为**。

<a id="ch00-s05"></a>

## 0.5 一个先导例子：TS 到底帮你做了什么

```ts
interface User {
  id: number;
  name: string;
  email?: string;
}

function greet(user: User): string {
  return `Hello, ${user.name}`;
}

greet({ id: 1, name: "April" });          // ✅
greet({ id: "1", name: "April" });        // ❌ id 应是 number
greet({ id: 1 });                         // ❌ 缺少 name
greet({ id: 1, name: "April", age: 18 }); // ❌ 多余属性 age
```

没有 TS 时，这三种错误都要等到运行时（甚至上线后）才暴露。TS 的价值就是：**把一大类运行时错误提前到编码阶段**。

---

<a id="ch01"></a>

# 第 1 章　TypeScript 是什么与环境搭建

<a id="ch01-s01"></a>

## 1.1 TypeScript 是什么

**TypeScript（TS）是 JavaScript 的超集**：

- 所有合法的 JS 代码，都是合法的 TS 代码
- TS 在 JS 之上增加了**静态类型系统**
- TS 代码**不能直接被浏览器/Node 执行**（新版 Node 可直接跑，见 1.5），需要先"擦除类型"变成 JS

```
  .ts 源码 ──(类型检查 + 擦除类型)──▶ .js 产物 ──▶ 浏览器 / Node 运行
```

### 两个关键事实（务必记住）

1. **类型只存在于编译期**。编译后类型全部消失，运行时没有任何类型检查。
2. **TS 不改变运行时行为**。性能、语义都和 JS 一致；TS 只负责"提前发现错误"。

<a id="ch01-s02"></a>

## 1.2 为什么需要 TS

JS 是动态类型语言，变量类型在运行时才确定，问题在项目变大后集中爆发：

| JS 的痛点                                                              | TS 的解法                      |
| ------------------------------------------------------------------- | --------------------------- |
| `undefined is not a function`、`Cannot read properties of undefined` | 编译期报错，强制处理 `null/undefined` |
| 函数参数传错类型、少传参数                                                       | 参数类型检查                      |
| 改一个字段名，不知道哪些地方受影响                                                   | 重命名/重构时 IDE 精准定位所有引用        |
| 看不懂别人的函数该传什么                                                        | 类型即文档，鼠标悬停即见                |
| 接口返回的 JSON 结构靠口头约定                                                  | 用类型显式建模                     |

<a id="ch01-s03"></a>

## 1.3 先补 JS 必备知识（10 分钟速通）

如果你来自 Python，下面是 JS 与 Python 的核心差异，TS 也继承它们。

```ts
// 变量声明：const（不可重新赋值，首选） / let（可变） / 不要用 var
const name = "April";
let count = 0;
count += 1;

// 数组与对象
const nums = [1, 2, 3];                       // 类似 Python list
const user = { id: 1, name: "April" };         // 类似 Python dict，但用点访问：user.name

// 箭头函数
const double = (x: number) => x * 2;

// 解构
const { id, name: userName } = user;           // 取出字段，可重命名
const [first, ...rest] = nums;                 // 数组解构 + 剩余元素

// 展开运算符
const user2 = { ...user, name: "Bob" };        // 复制并覆盖字段
const nums2 = [...nums, 4, 5];

// 模板字符串（类似 Python f-string）
const msg = `Hi ${userName}, you are #${id}`;

// 相等判断：永远用 === 和 !==，不要用 == 和 !=
const input: unknown = "1";
console.log(1 === 1, input === 1); // true false（== 会做隐式转换，=== 不会）

// 可选链与空值合并
const city = (user as { address?: { city?: string } }).address?.city ?? "unknown";
```

### JS 值得警惕的"特性"

| 现象                                                 | 说明                                      |   |    |
| -------------------------------------------------- | --------------------------------------- | - | -- |
| `typeof null === "object"`                         | 历史遗留 bug                                |   |    |
| `[] + {}`、`"1" + 1 === "11"`                       | 隐式类型转换，TS 会帮你拦住大部分                      |   |    |
| `0`、`""`、`NaN`、`null`、`undefined`、`false` 都是 falsy | 判断存在性时用 `=== undefined` 或 `??`，别滥用 \`   |   | \` |
| 数组、对象是引用类型                                         | `const a = [1]; const b = a;` 两者指向同一个数组 |   |    |
| 数字只有 `number`（64 位浮点），大整数用 `bigint`                | `0.1 + 0.2 !== 0.3`                     |   |    |

<a id="ch01-s04"></a>

## 1.4 安装与创建项目

### 1.4.1 前置条件

安装 **Node.js**（建议 LTS 22+）。验证：

```bash
node -v
npm -v
```

### 1.4.2 创建第一个项目

```bash
mkdir ts-demo && cd ts-demo
npm init -y                       # 生成 package.json
npm i -D typescript @types/node   # 本地安装 TS 与 Node 类型
npx tsc --init                    # 生成 tsconfig.json
```

新建 `src/hello.ts`：

```ts
const greet = (name: string): string => `Hello, ${name}!`;
console.log(greet("TypeScript"));
```

### 1.4.3 三种运行方式

| 方式                | 命令                                | 适用场景                                             |
| ----------------- | --------------------------------- | ------------------------------------------------ |
| **编译后运行**         | `npx tsc` 然后 `node dist/hello.js` | 生产构建，库发布                                         |
| **直接运行（Node 内置）** | `node src/hello.ts`               | Node 22.18+ / 23.6+ 默认支持"类型擦除"运行；只擦类型，**不做类型检查** |
| **第三方运行器**        | `npx tsx src/hello.ts`            | 开发调试，支持更多语法，也不做类型检查                              |


> **重点**：`tsx`、`node xxx.ts`、esbuild、swc 都只是**擦除类型**，**不会报类型错误**。要检查类型必须运行 `tsc --noEmit`。工程里通常两个都跑：开发用 tsx 快速运行，CI 里跑 `tsc --noEmit` 把关。

在 `package.json` 里配置脚本：

```json
{
  "scripts": {
    "dev": "tsx watch src/index.ts",
    "typecheck": "tsc --noEmit",
    "build": "tsc",
    "start": "node dist/index.js"
  }
}
```

<a id="ch01-s05"></a>

## 1.5 tsconfig.json 详解

`tsconfig.json` 是 TS 项目的"总开关"。下面是一份**现代 Node 项目的推荐配置**：

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "lib": ["ES2023"],
    "outDir": "dist",
    "rootDir": "src",

    "strict": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true,
    "exactOptionalPropertyTypes": false,

    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,

    "declaration": true,
    "sourceMap": true
  },
  "include": ["src"]
}
```

### 逐项解释

| 选项 | 含义 | 建议 |
|---|---|---|
| `target` | 编译产物的 JS 版本 | Node 项目 `ES2022` 及以上；浏览器看兼容目标 |
| `module` / `moduleResolution` | 模块系统与解析规则 | Node 项目用 `NodeNext`；前端打包器（Vite 等）用 `ESNext` + `Bundler` |
| `lib` | 可用的内置 API 类型（Promise、Map 等） | 与运行环境匹配；写前端要加 `"DOM"` |
| `outDir` / `rootDir` | 产物目录 / 源码目录 | 常规设置 |
| **`strict`** | **一键开启所有严格检查** | **必须开**，下面详述 |
| `noUncheckedIndexedAccess` | 数组/索引访问结果自动带 `undefined` | 强烈建议开，能拦住大量越界 bug |
| `noImplicitOverride` | 子类覆盖方法必须写 `override` | 建议开 |
| `esModuleInterop` | 兼容 CommonJS 默认导入 | 开 |
| `skipLibCheck` | 跳过 `.d.ts` 库文件检查 | 开，加速编译、避免依赖冲突 |
| `declaration` | 生成 `.d.ts` 类型声明 | 写库时开 |
| `sourceMap` | 生成 sourcemap，便于调试 | 开 |
| `include` / `exclude` | 哪些文件参与编译 | 常见 `"include": ["src"]` |

### `strict` 到底开了什么

`"strict": true` 等价于同时开启下面这些：

| 子选项 | 作用 |
|---|---|
| `strictNullChecks` | `null`/`undefined` 不再能赋给其他类型（**最重要**） |
| `noImplicitAny` | 推断不出类型时不允许悄悄变成 `any` |
| `strictFunctionTypes` | 函数参数类型严格逆变检查 |
| `strictBindCallApply` | `bind/call/apply` 参数检查 |
| `strictPropertyInitialization` | 类属性必须在构造器里初始化 |
| `noImplicitThis` | `this` 类型不明时报错 |
| `useUnknownInCatchVariables` | `catch (e)` 里的 `e` 是 `unknown` 而非 `any` |
| `alwaysStrict` | 产物里加 `"use strict"` |

**不开 strict 的 TS，等于只有一半的保护**。新项目永远开；老项目迁移可以逐项开。

<a id="ch01-s06"></a>

## 1.6 类型检查的"工作流"

写 TS 时的典型循环：

1. 在编辑器里写代码，红色波浪线即时提示
2. 鼠标悬停看推断的类型（学习阶段**经常这样做**，是理解 TS 最快的方式）
3. 提交前 `npm run typecheck` 全量检查
4. 构建/部署

### 善用编辑器

- 推荐 **VS Code**（TS 语言服务就是它内置的）
- 常用快捷键：`F12` 跳转定义、`Shift+F12` 查找引用、`F2` 重命名（会改所有引用）、`Ctrl+.` 快速修复/自动导入
- 看到不懂的类型，**悬停 + 按住 Ctrl 点击** 能展开完整类型

<a id="ch01-s07"></a>

## 1.7 常见坑

1. **以为 tsx / node 直接跑能发现类型错误**：不能，必须 `tsc --noEmit`。
2. **用全局 `tsc`**：不同项目版本不一致，请 `npm i -D typescript` 并用 `npx tsc`。
3. **忘记 `@types/node`**：用到 `process`、`fs`、`Buffer` 时会提示找不到名称。
4. **`tsconfig` 的 `include` 没包含文件**：文件没被检查，编辑器里也会失去类型支持。
5. **老项目 `strict: false`**：很多"TS 不好用"的感受来自这里。

<a id="ch01-s08"></a>

## 本章小结

- TS = JS + 静态类型，类型编译后消失，不影响运行时
- 开发推荐：`tsx` 快速运行 + `tsc --noEmit` 做类型检查
- `tsconfig.json` 必开 `strict`；加上 `noUncheckedIndexedAccess` 更稳
- 学习时多用"鼠标悬停"观察推断出来的类型

<a id="ch01-s09"></a>

## 练习

1. 按 1.4 创建项目，写一个函数 `add(a: number, b: number)`，故意传入字符串，观察错误信息。
2. 把 `tsconfig` 里的 `strict` 改成 `false`，再写 `let s: string = null;`，对比开关前后的区别。
3. 分别用 `npx tsx`、`npx tsc` 运行/编译一个含类型错误的文件，说明两者的区别。

---

<a id="ch02"></a>

# 第 2 章　基础类型与类型推断

<a id="ch02-s01"></a>

## 2.1 类型标注的基本语法

在变量名后面加 `: 类型` 即可：

```ts
const title: string = "TypeScript 教材";
let pages: number = 300;
let published: boolean = false;

pages = "三百";   // ❌ 不能把 string 赋给 number
```

TS 的类型系统有一个核心原则：**一个值只能被赋给"类型兼容"的变量**。

<a id="ch02-s02"></a>

## 2.2 原始类型（Primitive Types）

| 类型 | 含义 | 示例 |
|---|---|---|
| `string` | 字符串 | `"hi"`, `` `a${1}` `` |
| `number` | 所有数字（整数、浮点、`NaN`、`Infinity`） | `1`, `3.14`, `0xff` |
| `boolean` | 布尔 | `true`, `false` |
| `bigint` | 任意精度整数 | `100n` |
| `symbol` | 唯一标识符 | `Symbol("id")` |
| `null` | 空 | `null` |
| `undefined` | 未定义 | `undefined` |

```ts
const big: bigint = 9007199254740993n;
const id: symbol = Symbol("id");
const nothing: null = null;
const notYet: undefined = undefined;
```

> **注意小写**：用 `string`、`number`，**不要**写 `String`、`Number`（那是包装对象类型，几乎永远不是你想要的）。

<a id="ch02-s03"></a>

## 2.3 类型推断（Type Inference）

**TS 不需要你处处写类型**，能推断出来的就让它推断：

```ts
let age = 18;            // 推断为 number
let city = "Shenzhen";   // 推断为 string
age = "eighteen";        // ❌ number 不能赋 string

const PI = 3.14;         // const 推断为字面量类型 3.14（见 2.8）
```

### 什么时候写类型，什么时候省略

| 场景 | 建议 |
|---|---|
| 局部变量，初始化时有值 | **省略**，让 TS 推断 |
| 函数参数 | **必须写**（推断不出来） |
| 函数返回值 | 公共 API 建议写；内部小函数可省略 |
| 初始化为空的变量 | 要写，如 `let list: string[] = []` |
| 对象/配置的结构 | 用 `interface` / `type` 命名 |

```ts
// 初始值是空数组时，不写类型会推断为 never[]（或 any[]），之后无法 push
const bad = [];             // 推断为 any[]（演化数组类型）
const good: string[] = [];
good.push("ok");
```

<a id="ch02-s04"></a>

## 2.4 数组与元组

### 数组

两种写法等价，**推荐 `T[]`**；复杂类型用 `Array<T>` 更易读：

```ts
const a: number[] = [1, 2, 3];
const b: Array<string> = ["x", "y"];
const matrix: number[][] = [[1, 2], [3, 4]];

a.push("4");   // ❌ 只能放 number
```

只读数组：

```ts
const ro: readonly number[] = [1, 2, 3];
ro.push(4);    // ❌ readonly 数组没有 push
const copy = [...ro, 4]; // ✅ 通过创建新数组来"修改"
```

### 元组（Tuple）：固定长度、每个位置类型固定的数组

```ts
let pair: [string, number] = ["age", 18];
pair = [18, "age"];            // ❌ 位置类型不对
const [k, v] = pair;           // 解构得到 k: string, v: number

// 可选元素、剩余元素、命名元素
type Point = [x: number, y: number, z?: number];
type Row = [id: number, ...tags: string[]];

const p: Point = [1, 2];
const r: Row = [1, "a", "b"];
```

元组常用于函数返回多个值（类似 Python 的返回 tuple）：

```ts
function minMax(nums: number[]): [min: number, max: number] {
  return [Math.min(...nums), Math.max(...nums)];
}
const [lo, hi] = minMax([3, 1, 4]);
```

### `noUncheckedIndexedAccess` 的影响

开启后，按下标取值会带上 `undefined`，强制你处理越界：

```ts
const xs: number[] = [1, 2, 3];
const first = xs[0];       // 开启 noUncheckedIndexedAccess 时类型是 number | undefined
first.toFixed(2);          // ❌ 可能为 undefined
if (first !== undefined) {
  first.toFixed(2);        // ✅
}
```

<a id="ch02-s05"></a>

## 2.5 对象类型（初识）

先看最简单的写法，详细内容放到第 4 章：

```ts
const user: { id: number; name: string; email?: string } = {
  id: 1,
  name: "April",
};
console.log(user.email);   // string | undefined，可选属性可能没有
```

<a id="ch02-s06"></a>

## 2.6 any、unknown、never、void —— 四个特殊类型

这四个是新手最容易混淆的，务必搞清楚。

### `any`：放弃类型检查（逃生舱）

```ts
let x: any = 1;
x = "hello";
x.foo.bar.baz();   // 编译不报错，运行时才炸
```

`any` 会**传染**：从 `any` 取出的东西也是 `any`。满屏 `any` 的 TS 等于没用 TS。

### `unknown`：类型安全的 `any`（"我还不知道是什么"）

`unknown` 可以接收任何值，但**使用前必须先收窄**：

```ts
function parse(input: unknown): number {
  input.toFixed();             // ❌ unknown 不能直接用
  if (typeof input === "number") {
    return input;                // ✅ 收窄后，input 的类型就是 number
  }
  if (typeof input === "string") {
    return Number(input);
  }
  throw new Error("unsupported");
}
```

**规则：当你不知道类型时（外部输入、JSON、`catch` 的错误），用 `unknown`，不要用 `any`。**

### `never`：永远不会有值

三种典型场景：

```ts
// 1. 永远抛错的函数
function fail(msg: string): never {
  throw new Error(msg);
}

// 2. 死循环
function forever(): never {
  while (true) {}
}

// 3. 类型收窄后"不可能存在"的分支 —— 用来做"穷尽检查"（第 5 章详解）
type Shape = "circle" | "square";
function area(s: Shape): number {
  switch (s) {
    case "circle": return 3.14;
    case "square": return 1;
    default: {
      const _exhaustive: never = s; // 如果以后给 Shape 加了新成员却忘了处理，这里会报错
      return _exhaustive;
    }
  }
}
```

### `void`：函数没有返回值

```ts
function log(msg: string): void {
  console.log(msg);
}
```

### 四者对比

| 类型 | 能赋什么值进去 | 能当什么用 | 典型用途 |
|---|---|---|---|
| `any` | 任何值 | 任何用法（无检查） | 迁移老代码的临时手段 |
| `unknown` | 任何值 | 收窄后才能用 | 外部输入、`catch` 的错误 |
| `never` | 没有任何值 | 可赋给任何类型 | 穷尽检查、永不返回的函数 |
| `void` | `undefined` | 仅表示"无返回值" | 无返回值的函数 |

<a id="ch02-s07"></a>

## 2.7 null 与 undefined（strictNullChecks 的威力）

`strictNullChecks` 开启后，`null` 和 `undefined` **不再能赋给其他类型**：

```ts
let s: string = null;           // ❌
let t: string | null = null;    // ✅ 用联合类型显式声明"可能为空"

function len(s: string | null): number {
  return s.length;              // ❌ s 可能是 null
}
function len2(s: string | null): number {
  return s === null ? 0 : s.length;   // ✅
}
```

处理"可能为空"的常用工具：

```ts
interface Config { timeout?: number; name?: string }
const cfg: Config = {};

// 1. 可选链 ?.：中间有 null/undefined 就整体返回 undefined
const len3 = cfg.name?.length;                 // number | undefined

// 2. 空值合并 ??：仅当左边是 null/undefined 时取右边
const timeout = cfg.timeout ?? 3000;           // 注意：0 会被保留，用 || 的话 0 会被替换！

// 3. 非空断言 !：我保证它不是空（危险，慎用）
const forced = cfg.name!.length;               // 错了会运行时报错
```

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
> `??` 和 `||` 的区别：`0 || 3000` 得到 `3000`（0 是 falsy），`0 ?? 3000` 得到 `0`。**取默认值优先用 `??`**。

<a id="ch02-s08"></a>

## 2.8 字面量类型与 `as const`

类型不仅可以是 `string`，还可以是**某一个具体的值**：

```ts
let dir: "left" | "right" = "left";
dir = "up";                    // ❌ 只能是 "left" 或 "right"

const one = 1;                 // 类型是字面量 1，而不是 number
let two = 2;                   // 类型是 number（let 可变，所以拓宽了）
```

### `as const`：把值冻结为最窄的只读字面量类型

```ts
const config = {
  env: "prod",
  retries: 3,
  hosts: ["a.com", "b.com"],
};
// 推断：{ env: string; retries: number; hosts: string[] }

const config2 = {
  env: "prod",
  retries: 3,
  hosts: ["a.com", "b.com"],
} as const;
// 推断：{ readonly env: "prod"; readonly retries: 3; readonly hosts: readonly ["a.com", "b.com"] }
```

`as const` 最常见的用途：**从值反推联合类型**（后面章节会反复用到）：

```ts
const ROLES = ["admin", "user", "guest"] as const;
type Role = (typeof ROLES)[number];   // "admin" | "user" | "guest"

function isRole(x: string): x is Role {
  return (ROLES as readonly string[]).includes(x);
}
```

<a id="ch02-s09"></a>

## 2.9 类型别名 `type`（初识）

给类型起名字：

```ts
type ID = string | number;
type Callback = (err: Error | null, data?: string) => void;

let uid: ID = 1;
uid = "u-001";
```

<a id="ch02-s10"></a>

## 2.10 类型断言（as）与它的风险

当你比编译器更清楚类型时，可用 `as` 告诉它：

```ts
const el = { value: "42" } as { value: string };
const n = Number((el as { value: string }).value);

const raw: unknown = "hello";
const s = raw as string;      // 编译通过，但如果 raw 其实不是 string，运行时就错了
```

**`as` 不会做任何运行时检查，只是"闭嘴吧编译器"**。几条规则：

- 能用类型收窄（`typeof`、`in`、自定义守卫）就不用 `as`
- 双重断言 `x as unknown as T` 是最后的手段，说明设计可能有问题
- `as const` 是安全的，不属于上面的"风险断言"


<a id="ch02-s11"></a>

## 2.11 常见坑

| 坑 | 说明 | 正确做法 |
|---|---|---|
| 用 `String`/`Number`/`Object` 类型 | 这是包装对象类型 | 用小写 `string`/`number`/`object` |
| 到处写 `any` | 类型检查被关闭 | 用 `unknown` + 收窄 |
| `const x = []` 后无法 push | 推断为 `never[]`/演化 any | 显式写 `const x: T[] = []` |
| 滥用 `!` 非空断言 | 把错误推迟到运行时 | 先判断，或用 `??`/`?.` |
| `let` 声明字面量被拓宽 | `let d = "left"` 是 `string` | 显式标注或用 `as const` |
| 以为 `as` 会转换类型 | 它只改变编译器视角 | 真正转换要用 `Number()` 等 |

<a id="ch02-s12"></a>

## 本章小结

- 优先依赖**类型推断**，只在必要处标注（参数、公共返回值、空初始化）
- `unknown` 替代 `any`；`never` 做穷尽检查；`void` 表示无返回值
- `strictNullChecks` 让"可能为空"成为类型的一部分，用 `?.`、`??` 优雅处理
- 字面量类型 + `as const` 能把"值"变成"类型"

<a id="ch02-s13"></a>

## 练习

|  |  |
| --- | --- |
1. 写一个函数 `safeParseInt(input: unknown): number | null`，只有当 `input` 是数字字符串时才返回数字，否则 `null`。
2. 定义 `const STATUS = ["idle", "loading", "done"] as const`，推导出 `type Status`，再写一个函数接收 `Status` 并返回对应中文文案。
3. 解释为什么 `const a = [1, 2, 3]; a.push(4)` 可以，但 `const b = [1, 2, 3] as const; b.push(4)` 不行。

---

<a id="ch03"></a>

# 第 3 章　函数

函数是 TS 里最常写的东西。本章讲清：如何给函数标注类型、各种参数形式、重载、`this`，以及回调的类型陷阱。

<a id="ch03-s01"></a>

## 3.1 参数与返回值类型

```ts
function add(a: number, b: number): number {
  return a + b;
}

const sub = (a: number, b: number): number => a - b;
```

- **参数必须标注类型**（否则隐式 `any`，`strict` 下报错）
- **返回值类型可以省略**（TS 会推断），但对外暴露的函数建议显式写，因为这样"实现和契约分离"，改实现时若返回类型变了会立刻报错

```ts
function f(x: number) {
  if (x > 0) return "positive";
  return 0;
}
// 推断返回类型："positive" | 0
```

<a id="ch03-s02"></a>

## 3.2 可选参数、默认参数、剩余参数

```ts
// 可选参数：加 ?，类型自动变为 T | undefined，且必须放在必选参数后面
function greet(name: string, title?: string): string {
  return title ? `${title} ${name}` : name;
}
greet("April");
greet("April", "Dr.");

// 默认参数：自动变为可选，类型由默认值推断
function repeat(s: string, times = 2): string {
  return s.repeat(times);
}

// 剩余参数：收集成数组
function sum(...nums: number[]): number {
  return nums.reduce((a, b) => a + b, 0);
}
sum(1, 2, 3);
```

<a id="ch03-s03"></a>

## 3.3 函数类型的表示方法

函数本身也有类型，常见三种写法：

```ts
// 1. 函数类型表达式（最常用）
type BinaryOp = (a: number, b: number) => number;
const mul: BinaryOp = (a, b) => a * b;      // 参数类型由上下文推断，无需再写

// 2. 调用签名（对象 + 属性 + 可调用）
interface Counter {
  (step?: number): number;   // 可被调用
  count: number;             // 同时带有属性
}

// 3. 构造签名（能被 new）
interface Ctor<T> {
  new (...args: any[]): T;
}
```

### 上下文类型推断（Contextual Typing）

当函数作为回调传入时，**参数类型会自动推断**，不用重复标注：

```ts
const nums = [1, 2, 3];
const doubled = nums.map((n) => n * 2);   // n 推断为 number
const evens = nums.filter((n) => n % 2 === 0);
```

<a id="ch03-s04"></a>

## 3.4 `void` 返回类型的特殊性

一个声明返回 `void` 的**函数类型**，实际可以被赋值为"有返回值的函数"，调用方只是忽略返回值：

```ts
type Handler = (msg: string) => void;
const h: Handler = (msg) => msg.length;   // ✅ 返回了 number，但被允许
const result = h("hi");                    // result 的类型是 void，不能使用它
```

这是因为 `forEach` 这类 API 的回调通常会随手返回点什么，不应该被报错。但**直接声明返回 void 的函数声明**不能返回值：

```ts
function bad(): void {
  return 1;   // ❌
}
```

<a id="ch03-s05"></a>

## 3.5 函数重载（Overloads）

一个函数根据**参数类型不同**返回不同类型时使用。写法：若干"重载签名" + 一个"实现签名"：

```ts
function toArray(x: string): string[];
function toArray(x: number): number[];
function toArray(x: string | number): (string | number)[] {
  return [x];
}

const a = toArray("a");   // string[]
const b = toArray(1);     // number[]
toArray(true);            // ❌ 没有匹配的重载
```

要点：

- **实现签名对外不可见**，调用者只能看到上面的重载签名
- 重载按**从上到下**匹配，把更具体的写在前面
- 如果只是参数类型不同、返回类型一致，用**联合类型**即可，不要滥用重载
- 更现代的替代方案：**泛型 + 条件类型**（第 8 章）

<a id="ch03-s06"></a>

## 3.6 `this` 的类型

JS 里 `this` 取决于**调用方式**，是经典坑。TS 允许在函数第一个"伪参数"里声明 `this` 类型（编译后会被擦除）：

```ts
interface Button {
  label: string;
  onClick(this: Button): void;
}

const btn: Button = {
  label: "OK",
  onClick() {
    console.log(this.label);
  },
};

btn.onClick();           // ✅
const fn = btn.onClick;
fn();                    // ❌ this 丢失，TS 会报错
```

**实践建议**：回调里需要 `this` 时，用**箭头函数**（箭头函数不绑定自己的 `this`，沿用外层的），或者干脆不依赖 `this`。

<a id="ch03-s07"></a>

## 3.7 回调函数的类型

```ts
function fetchData(url: string, cb: (err: Error | null, data?: string) => void): void {
  setTimeout(() => cb(null, `data from ${url}`), 10);
}

fetchData("/api", (err, data) => {
  if (err) return console.error(err);
  console.log(data);
});
```

回调参数的"双向性"（协变/逆变）会在 3.9 简单提及。更推荐的写法是 **Promise / async-await**（第 10 章）。

<a id="ch03-s08"></a>

## 3.8 泛型函数初识

当参数与返回值类型之间存在"关联"时，需要泛型。先看一个直观的例子：

```ts
// 不用泛型：丢失类型信息
function firstAny(arr: any[]): any {
  return arr[0];
}

// 用泛型：输入什么类型，输出就是对应元素类型
function first<T>(arr: T[]): T | undefined {
  return arr[0];
}

const a = first([1, 2, 3]);       // number | undefined
const b = first(["x", "y"]);      // string | undefined
```

`<T>` 是"类型参数"，类似普通参数，但它接收的是**类型**。泛型是第 6 章的主角，这里只需知道：**泛型函数让"类型"也能像值一样被传递**。

<a id="ch03-s09"></a>

## 3.9 参数的变体（进阶：协变与逆变）

这是理解"为什么某些回调赋值会报错"的关键，了解即可。

```ts
class Animal { name = "" }
class Dog extends Animal { bark() {} }

type Feed = (a: Animal) => void;
type FeedDog = (d: Dog) => void;

declare let feedAnimal: Feed;
declare let feedDog: FeedDog;

feedDog = feedAnimal;   // ✅ 能喂所有动物的函数，当然能喂狗（参数逆变）
feedAnimal = feedDog;   // ❌ 只会喂狗的函数，不能保证喂任意动物
```

记忆口诀：

- **返回值是协变**：返回更具体的类型是安全的
- **参数是逆变**：接受更宽泛的参数类型是安全的
- 需要 `strictFunctionTypes`（`strict` 包含）才会严格检查

<a id="ch03-s10"></a>

## 3.10 常见坑

| 坑 | 说明 | 正确做法 |
|---|---|---|
| 可选参数放在必选参数前 | 语法不允许 | 调整顺序，或用默认值/对象参数 |
| 参数过多（>3 个） | 调用时容易传错位置 | 改成**一个对象参数** + 解构 |
| 滥用重载 | 维护成本高 | 优先联合类型/泛型 |
| 回调中 `this` 丢失 | JS 运行时特性 | 用箭头函数 |
| 忘记 `async` 函数返回 `Promise<T>` | 返回值标注成 `T` 会报错 | 标注 `Promise<T>` 或省略 |

### 推荐实践：对象参数

```ts
interface CreateUserOptions {
  name: string;
  age?: number;
  admin?: boolean;
}

function createUser({ name, age = 18, admin = false }: CreateUserOptions) {
  return { name, age, admin };
}

createUser({ name: "April", admin: true });   // 参数含义一目了然
```

<a id="ch03-s11"></a>

## 本章小结

- 参数必写类型，返回值可推断但建议公共函数显式写
- 可选/默认/剩余参数；回调里靠上下文推断参数类型
- `void` 函数类型允许被赋值为有返回值的函数
- 重载：多个签名 + 一个实现；能用联合类型/泛型就别重载
- `this` 参数可声明类型；回调里优先箭头函数
- 参数逆变、返回值协变

<a id="ch03-s12"></a>

## 练习

1. 写 `function pick<T, K extends keyof T>(obj: T, key: K): T[K]`，并解释每个类型参数的作用（提示：见第 6、8 章）。
2. 为一个 `sleep(ms)` 函数标注类型，返回 `Promise<void>`。
3. 写一个重载函数 `parse(input: string): number` 与 `parse(input: string[]): number[]`，再改写成泛型+联合类型的版本，比较优缺点。

---

<a id="ch04"></a>

# 第 4 章　对象类型：interface 与 type

真实项目里 90% 的类型工作，都是在**给对象建模**：用户、订单、API 响应、工具参数、配置……本章是日常使用频率最高的一章。

<a id="ch04-s01"></a>

## 4.1 内联对象类型

```ts
function printUser(user: { id: number; name: string }) {
  console.log(user.id, user.name);
}
```

内联写法适合一次性使用。复用就要**命名**，有两种方式：`interface` 和 `type`。

<a id="ch04-s02"></a>

## 4.2 interface

```ts
interface User {
  id: number;
  name: string;
  email?: string;            // 可选属性
  readonly createdAt: Date;  // 只读属性
}

const u: User = { id: 1, name: "April", createdAt: new Date() };
u.name = "Bob";              // ✅
u.createdAt = new Date();    // ❌ 只读属性不能被重新赋值
```

### 属性修饰符

| 修饰符 | 写法 | 含义 |
|---|---|---|
| 可选 | `email?: string` | 可以没有；读取时类型是 `string \| undefined` |
| 只读 | `readonly id: number` | 初始化后不能再赋值（仅编译期，不是真正冻结） |

> `readonly` 是**浅层**的：`readonly list: string[]` 只是不能给 `list` 重新赋值，但 `list.push()` 仍然可以。要深度只读，用 `readonly string[]` 或 `Readonly<T>` 配合递归类型。

|  |  |
| --- | --- |
### 可选属性 vs `T | undefined`

```ts
interface A { x?: number }         // x 可以不存在，也可以显式是 undefined
interface B { x: number | undefined }  // x 必须存在，只是值可以是 undefined

const a: A = {};            // ✅
const b: B = {};            // ❌ 缺少 x
const b2: B = { x: undefined }; // ✅
```

<a id="ch04-s03"></a>

## 4.3 type（类型别名）

```ts
type User2 = {
  id: number;
  name: string;
};

type ID = string | number;                 // type 可以表示联合类型
type Pair<T> = [T, T];                     // 元组
type Handler = (e: Event) => void;         // 函数
```

<a id="ch04-s04"></a>

## 4.4 interface 与 type 的区别（面试高频）

| 能力 | `interface` | `type` |
|---|---|---|
| 描述对象 | ✅ | ✅ |
| 描述联合 / 交叉 / 元组 / 基本类型别名 | ❌ | ✅ |
| 继承 / 扩展 | `extends` | 交叉类型 `&` |
| **同名自动合并（声明合并）** | ✅ | ❌（重复声明报错） |
| 实现于 `class ... implements` | ✅ | ✅（对象形态时） |
| 映射类型、条件类型 | ❌ | ✅ |
| 报错信息可读性 | 一般更友好 | 展开后可能很长 |

```ts
// interface 声明合并：同名自动合并，常用于扩展第三方库类型
interface Window2 { appName: string }
interface Window2 { version: number }
const w: Window2 = { appName: "x", version: 1 };   // 两个声明合并成一个

// type 重复声明会报错
type T1 = { a: number };
type T1 = { b: string };   // ❌ 重复标识符
```

### 选择建议

- **描述对象/类的形状（尤其是对外 API）**：优先 `interface`
- **联合类型、元组、工具类型、条件/映射类型的结果**：只能用 `type`
- 团队保持**一致性**比选哪个更重要
- 不确定就用 `type`，需要声明合并或 `extends` 的层级结构再用 `interface`

<a id="ch04-s05"></a>

## 4.5 扩展与组合

### interface 继承

```ts
interface Animal {
  name: string;
}
interface Dog extends Animal {
  breed: string;
}
interface Pet extends Animal, Dog2 {}   // 可以同时继承多个
interface Dog2 { owner: string }

const d: Dog = { name: "Rex", breed: "Husky" };
```

子接口可以**收窄**父接口属性的类型，但不能不兼容：

```ts
interface Base { id: string | number }
interface Child extends Base { id: number }     // ✅ number 是 string|number 的子类型
interface Bad extends Base { id: boolean }      // ❌ 不兼容
```

### 交叉类型 `&`

```ts
type WithTimestamp = { createdAt: Date; updatedAt: Date };
type Post = { title: string; body: string } & WithTimestamp;

const p: Post = {
  title: "t", body: "b",
  createdAt: new Date(), updatedAt: new Date(),
};
```

<a id="ch04-s06"></a>

## 4.6 索引签名（Index Signature）

当对象的**键是动态的**（比如 map、字典）时：

```ts
interface StringMap {
  [key: string]: string;
}
const headers: StringMap = { "Content-Type": "application/json" };
headers["X-Id"] = "1";

// 更推荐的现代写法：Record
type Headers = Record<string, string>;
```

注意与固定属性共存时，**固定属性类型必须兼容索引签名**：

```ts
interface Bad {
  [key: string]: string;
  count: number;        // ❌ number 不兼容 string
}
interface Ok {
  [key: string]: string | number;
  count: number;        // ✅
}
```

### 开启 `noUncheckedIndexedAccess` 后

```ts
const m: Record<string, number> = { a: 1 };
const v = m["b"];         // number | undefined（开启该选项后）
```

### 键为有限集合时用 `Record<K, V>`

```ts
type Level = "debug" | "info" | "error";
const colors: Record<Level, string> = {
  debug: "gray",
  info: "blue",
  error: "red",
};   // 少写一个 key 就会报错 —— 这是用 Record 做"穷尽映射"的好处
```

<a id="ch04-s07"></a>

## 4.7 多余属性检查（Excess Property Check）

**对象字面量**直接赋值时，TS 会检查多余属性：

```ts
interface Point { x: number; y: number }

const p1: Point = { x: 1, y: 2, z: 3 };   // ❌ 对象字面量不能有多余的 z

const raw = { x: 1, y: 2, z: 3 };
const p2: Point = raw;                     // ✅ 通过变量传入，不触发多余属性检查
```


这体现了 TS 的**结构化类型系统**（4.8）：只要"满足所需结构"就兼容；多余属性检查只是对字面量的额外防呆（防止拼写错误）。

<a id="ch04-s08"></a>

## 4.8 结构化类型系统（Structural Typing）

TS 不看你"叫什么名字"（名义类型），而看你"长什么样"（结构）：

```ts
interface Named { name: string }
class Person { constructor(public name: string, public age: number) {} }

const n: Named = new Person("April", 18);   // ✅ Person 有 name: string，就满足 Named
```

对比 Java/C#：它们要求显式 `implements`。TS 的**鸭子类型**让代码非常灵活，但也意味着：**两个无关的类型只要结构相同就互相兼容**。

```ts
type UserId = string;
type OrderId = string;
const uid: UserId = "u1";
const oid: OrderId = uid;   // ✅ 结构相同，不会报错 —— 想区分需要"品牌类型"（见 4.9）
```

<a id="ch04-s09"></a>

## 4.9 进阶：品牌类型（Branded Type）

当你想在类型层面区分"同样是 string 的不同含义"时：

```ts
type Brand<T, B extends string> = T & { readonly __brand: B };

type UserId = Brand<string, "UserId">;
type OrderId = Brand<string, "OrderId">;

const asUserId = (s: string) => s as UserId;
const asOrderId = (s: string) => s as OrderId;

function getUser(id: UserId) {}

const uid = asUserId("u1");
const oid = asOrderId("o1");
getUser(uid);   // ✅
getUser(oid);   // ❌ OrderId 不能赋给 UserId
```

这在金融、ID 众多、单位容易混淆（米/英尺）的项目里很有用。

<a id="ch04-s10"></a>

## 4.10 常用的内置对象类型

| 类型 | 含义 | 说明 |
|---|---|---|
| `object` | 非原始类型（对象、数组、函数） | 不能访问属性 |
| `{}` | 任何非 `null/undefined` 的值 | 很宽，包含 `string`、`number`；**一般不要用** |
| `Record<K, V>` | 键为 K、值为 V 的对象 | 字典首选 |
| `Object` | JS 原型 Object | 不要用 |
| `Function` | 任意函数 | 不要用，写具体函数类型 |

<a id="ch04-s11"></a>

## 4.11 嵌套与复杂对象的建模例子

```ts
interface Address {
  city: string;
  street?: string;
}

interface Order {
  id: string;
  items: { sku: string; qty: number; price: number }[];
  shipping: Address;
  status: "pending" | "paid" | "shipped";
  meta?: Record<string, unknown>;
}

function total(order: Order): number {
  return order.items.reduce((sum, it) => sum + it.qty * it.price, 0);
}
```

从已有类型提取子类型：

```ts
type OrderItem = Order["items"][number];   // 索引访问类型（第 8 章详解）
type OrderStatus = Order["status"];        // "pending" | "paid" | "shipped"
```

<a id="ch04-s12"></a>

## 4.12 常见坑

| 坑 | 说明 | 正确做法 |
|---|---|---|
| 把 `readonly` 当"深冻结" | 它只在编译期，且浅层 | 需要运行时不可变用 `Object.freeze` |
| `{}` 当"任意对象" | 实际表示"非空值"，字符串也能赋给它 | 用 `object` 或 `Record<string, unknown>` |
| 索引签名对象取值认为一定存在 | 缺 key 时运行时是 `undefined` | 开 `noUncheckedIndexedAccess` |
| 多余属性检查"失灵" | 通过变量传递不检查 | 理解它只对字面量生效 |
| 同名 `type` 重复声明 | 报错 | 改名，或用 `interface` 合并 |

<a id="ch04-s13"></a>

## 本章小结

- 对象建模首选 `interface`/`type`；`type` 能力更全，`interface` 支持声明合并
- 修饰符：`?` 可选、`readonly` 只读；字典用 `Record` 或索引签名
- TS 是**结构化类型**：看"形状"不看"名字"，品牌类型可补足区分
- 多余属性检查只对对象字面量生效

<a id="ch04-s14"></a>

## 练习

|  |  |  |
| --- | --- | --- |
1. 为一个 "聊天消息" 建模：包含 `id`、`role`（`"user" | "assistant" | "system"`）、`content`、可选 `toolCalls`（数组，每项含 `id`、`name`、`arguments`）。
2. 用 `Brand` 类型区分 `Meter` 和 `Feet`，写一个只接受 `Meter` 的函数。
3. 解释为什么 `const p2: Point = raw`（变量传入）不报多余属性错误，而字面量会。

---

<a id="ch05"></a>

# 第 5 章　联合类型、交叉类型与类型收窄

如果说泛型是 TS 的"灵魂"，那**联合类型 + 类型收窄**就是 TS 的"日常"。这一章决定你写 TS 是否顺手。

<a id="ch05-s01"></a>

|  |  |
| --- | --- |
## 5.1 联合类型 `|`（A 或 B）

```ts
type ID = string | number;

function printId(id: ID) {
  console.log(id.toUpperCase());   // ❌ number 没有 toUpperCase
}
```

**联合类型的核心规则：对联合类型的值，只能使用所有成员"共有"的操作，除非先收窄。**

```ts
function printId2(id: string | number) {
  if (typeof id === "string") {
    console.log(id.toUpperCase());   // ✅ 这里 id 被收窄为 string
  } else {
    console.log(id.toFixed(2));      // ✅ 这里 id 被收窄为 number
  }
}
```

<a id="ch05-s02"></a>

## 5.2 类型收窄（Narrowing）

**收窄 = TS 通过代码流分析，在某个位置把"宽类型"缩小为"窄类型"。** 下面是所有常用手段。

### 5.2.1 `typeof` 守卫

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
适用于原始类型：`"string" | "number" | "boolean" | "bigint" | "symbol" | "undefined" | "function" | "object"`

```ts
function pad(x: string | number): string {
  return typeof x === "number" ? x.toFixed(0) : x;
}
```

> `typeof null === "object"`！判断对象前要先排除 `null`。

### 5.2.2 真值收窄

```ts
function len(s?: string): number {
  if (s) return s.length;   // 排除了 undefined 和 ""
  return 0;
}
```

注意：`0`、`""`、`NaN` 也是 falsy，会被一并排除。如果 `0` 是合法值，请用 `=== undefined`。

### 5.2.3 相等收窄

```ts
function f(a: string | number, b: string | boolean) {
  if (a === b) {
    // 只有 string 是两者共有，所以这里 a、b 都是 string
    a.toUpperCase();
    b.toUpperCase();
  }
}
```

### 5.2.4 `in` 操作符

```ts
interface Fish { swim(): void }
interface Bird { fly(): void }

function move(a: Fish | Bird) {
  if ("swim" in a) {
    a.swim();     // Fish
  } else {
    a.fly();      // Bird
  }
}
```

### 5.2.5 `instanceof`

```ts
function show(x: Date | string) {
  if (x instanceof Date) {
    return x.toISOString();
  }
  return x.toUpperCase();
}

function handle(err: unknown) {
  if (err instanceof Error) {
    console.error(err.message);   // ✅ Error 类型
  }
}
```

### 5.2.6 赋值收窄与控制流

```ts
let x: string | number = "hello";
x.toUpperCase();      // ✅ 赋值后 TS 知道此刻是 string
x = 10;
x.toFixed();          // ✅ 现在是 number
```

TS 的"控制流分析"会跟踪 `if`、`return`、`throw`、`switch` 等：

```ts
function f(x: string | null): number {
  if (x === null) {
    throw new Error("null");
  }
  return x.length;      // 前面的 throw 之后，x 一定是 string
}
```

### 5.2.7 自定义类型守卫（Type Predicate）

当内置手段不够用时，自己写判断函数，返回类型写 `参数 is 类型`：

```ts
interface Cat { meow(): void }
interface Dog { bark(): void }

function isCat(a: Cat | Dog): a is Cat {
  return (a as Cat).meow !== undefined;
}

function talk(a: Cat | Dog) {
  if (isCat(a)) a.meow();
  else a.bark();
}
```

> **风险提醒**：`a is Cat` 是你对编译器的"承诺"，TS 不会验证函数体是否真的正确。写错了，类型就是谎言。

常见的实用守卫：

```ts
// 过滤掉 null/undefined，并让数组类型也跟着变
function isDefined<T>(x: T | null | undefined): x is T {
  return x !== null && x !== undefined;
}

const raw: (string | undefined)[] = ["a", undefined, "b"];
const clean: string[] = raw.filter(isDefined);   // ✅ 类型正确变成 string[]
```

### 5.2.8 断言函数（Assertion Function）

不返回布尔，而是"通过则继续，不通过则抛错"：

```ts
function assertString(x: unknown): asserts x is string {
  if (typeof x !== "string") throw new Error("not string");
}

function use(v: unknown) {
  assertString(v);
  v.toUpperCase();   // ✅ 之后 v 被视为 string
}
```

<a id="ch05-s03"></a>

## 5.3 可辨识联合（Discriminated Union）⭐

**这是 TS 中最重要的设计模式之一。**

做法：给联合的每个成员加一个**同名的字面量属性**（"判别字段"，常叫 `kind`、`type`、`status`），TS 就能根据它精确收窄。

```ts
type Shape =
  | { kind: "circle"; radius: number }
  | { kind: "rect"; width: number; height: number }
  | { kind: "triangle"; base: number; height: number };

function area(s: Shape): number {
  switch (s.kind) {
    case "circle":
      return Math.PI * s.radius ** 2;       // s 被收窄为 circle 成员
    case "rect":
      return s.width * s.height;
    case "triangle":
      return (s.base * s.height) / 2;
  }
}
```

### 穷尽检查（Exhaustiveness Checking）

用 `never` 保证"以后新增成员时，忘记处理会编译报错"：

```ts
function assertNever(x: never): never {
  throw new Error(`Unexpected: ${JSON.stringify(x)}`);
}

function area2(s: Shape): number {
  switch (s.kind) {
    case "circle": return Math.PI * s.radius ** 2;
    case "rect": return s.width * s.height;
    case "triangle": return (s.base * s.height) / 2;
    default: return assertNever(s);   // 如果 Shape 新增 "polygon"，这里立刻报错
  }
}
```

### 用可辨识联合建模"状态"

这是消灭"非法状态"的利器。对比两种建模：

```ts
// 坏设计（不推荐）：字段组合可能出现矛盾状态（loading 和 error 同时为真？data 与 error 同时有值？）
interface BadState {
  loading: boolean;
  data?: string;
  error?: Error;
}

// ✅ 好设计：每个状态只携带自己需要的数据，非法组合根本无法表达
type RequestState =
  | { status: "idle" }
  | { status: "loading" }
  | { status: "success"; data: string }
  | { status: "error"; error: Error };

function render(s: RequestState): string {
  switch (s.status) {
    case "idle": return "点击加载";
    case "loading": return "加载中...";
    case "success": return s.data;
    case "error": return s.error.message;
  }
}
```

> **设计原则：Make illegal states unrepresentable（让非法状态无法被表达）。**

### Agent 中的典型应用：消息与工具调用

```ts
type Message =
  | { role: "system"; content: string }
  | { role: "user"; content: string }
  | { role: "assistant"; content: string; toolCalls?: { id: string; name: string; args: unknown }[] }
  | { role: "tool"; toolCallId: string; content: string };

function describe(m: Message): string {
  switch (m.role) {
    case "tool": return `tool result for ${m.toolCallId}`;
    case "assistant": return `assistant (${m.toolCalls?.length ?? 0} tool calls)`;
    default: return `${m.role}: ${m.content}`;
  }
}
```

<a id="ch05-s04"></a>

## 5.4 交叉类型 `&`（A 且 B）

```ts
type A = { a: number };
type B = { b: string };
type AB = A & B;
const ab: AB = { a: 1, b: "x" };   // 必须同时满足
```

### 交叉的陷阱

1. **同名属性类型冲突，会变成 `never`**

```ts
type X = { id: string } & { id: number };
// X["id"] 的类型是 string & number = never，这个对象根本无法被构造
```

2. **对联合类型取交叉，会"分配"出组合**

```ts
type U = (A | B) & { c: boolean };
// 等价于 (A & {c}) | (B & {c})
```

### 交叉 vs 联合的直觉

| | 值的集合 | 可访问的属性 |
|---|---|---|
| `A \| B` | A 的值 ∪ B 的值（**更大**） | 只有**共有**属性 |
| `A & B` | A 的值 ∩ B 的值（**更小**） | **所有**属性 |

> 初学者常觉得反直觉：**属性越多的类型，值的范围越小**。

<a id="ch05-s05"></a>

## 5.5 字面量类型联合：替代 enum 的首选方式

```ts
type Method = "GET" | "POST" | "PUT" | "DELETE";

function request(url: string, method: Method = "GET") {}
request("/a", "PATCH");   // ❌
```

配合 `as const` 实现"值 + 类型"同源：

```ts
const METHODS = ["GET", "POST", "PUT", "DELETE"] as const;
type Method2 = (typeof METHODS)[number];
```

<a id="ch05-s06"></a>

## 5.6 联合类型的"分配"行为

对联合类型调用某些操作，会**逐个成员分配**。最典型的就是条件类型（第 8 章）：

```ts
type ToArray<T> = T extends unknown ? T[] : never;
type R = ToArray<string | number>;   // string[] | number[]（而不是 (string | number)[]）
```

<a id="ch05-s07"></a>

## 5.7 常见坑

| 坑 | 说明 | 正确做法 |
|---|---|---|
| 用 `boolean` 字段组合表达状态 | 出现矛盾组合 | 用可辨识联合 |
| 判别字段不是字面量 | `kind: string` 无法收窄 | 用字面量类型 |
| 自定义守卫写错 | 类型变成谎言 | 守卫实现要严谨，必要时配合 zod |
| `switch` 没有 default 穷尽检查 | 新增成员时静默漏处理 | 加 `assertNever` |
| 回调里收窄失效 | 变量在回调中可能被改 | 用 `const` 保存收窄后的值 |
| `typeof x === "object"` 忘记排除 null | `null` 也是 object | 先判断 `x !== null` |

回调里收窄失效的例子：

```ts
function f(obj: { name?: string }) {
  if (obj.name) {
    setTimeout(() => {
      // 在回调内，属性可能被其他代码修改，TS 对"属性"的收窄较保守
      console.log(obj.name?.length);
    }, 0);
    const n = obj.name;        // 提前保存到 const，收窄结果稳定
    setTimeout(() => console.log(n.length), 0);   // ✅
  }
}
```

<a id="ch05-s08"></a>

## 本章小结

- 联合类型只能使用共有成员，必须先**收窄**才能使用特有成员
- 收窄手段：`typeof`、真值、`===`、`in`、`instanceof`、赋值、自定义守卫、断言函数
- **可辨识联合 + `never` 穷尽检查**是 TS 设计模式的核心
- 交叉类型取"并且"，属性冲突会得到 `never`


<a id="ch05-s09"></a>

## 练习

1. 用可辨识联合为 "支付方式" 建模：`card`（含卡号、有效期）、`alipay`（含账号）、`cash`（无额外字段），写 `describePayment` 并加穷尽检查。
2. 写一个 `isNonEmptyArray<T>(x: T[]): x is [T, ...T[]]` 守卫。
3. 把下面的坏设计改成可辨识联合：`{ isLoading: boolean; isError: boolean; data?: User; errorMsg?: string }`。

---

<a id="ch06"></a>

# 第 6 章　泛型（Generics）

泛型是 TS 最重要、也最让新手困惑的特性。本章会从"为什么"出发，一步步建立直觉。

<a id="ch06-s01"></a>

## 6.1 为什么需要泛型

假设要写一个"返回数组第一个元素"的函数。

**方案 A：用 `any`** —— 丢失类型信息

```ts
function firstAny(arr: any[]): any {
  return arr[0];
}
const x = firstAny([1, 2, 3]);   // x 是 any，后续再也没有类型保护
```

**方案 B：为每种类型写一个函数** —— 重复

```ts
function firstNumber(arr: number[]): number | undefined { return arr[0]; }
function firstString(arr: string[]): string | undefined { return arr[0]; }
```

**方案 C：泛型** —— 把"类型"也作为参数

```ts
function first<T>(arr: T[]): T | undefined {
  return arr[0];
}

const a = first([1, 2, 3]);       // T 推断为 number，a: number | undefined
const b = first(["x", "y"]);      // T 推断为 string，b: string | undefined
const c = first<boolean>([true]); // 也可以手动指定 T
```

**一句话理解：泛型 = 类型层面的函数参数。** `<T>` 声明一个类型变量，调用时由 TS 推断或你手动指定。

<a id="ch06-s02"></a>

## 6.2 泛型函数

```ts
function identity<T>(x: T): T {
  return x;
}

// 多个类型参数
function pair<A, B>(a: A, b: B): [A, B] {
  return [a, b];
}
const p = pair("age", 18);   // [string, number]

// 箭头函数写法（.ts 文件里直接写，.tsx 文件里需要 <T,> 避免和 JSX 混淆）
const wrap = <T>(x: T): { value: T } => ({ value: x });
```

### 命名惯例

| 名称 | 含义 |
|---|---|
| `T` | Type，最通用 |
| `K` / `V` | Key / Value |
| `E` | Element |
| `R` | Return / Result |
| `TInput`、`TOutput` | 多个类型参数时，用有语义的名字更清晰 |

<a id="ch06-s03"></a>

## 6.3 泛型约束 `extends`

泛型默认可以是任何类型，所以你**不能访问它的任何属性**：

```ts
function len<T>(x: T): number {
  return x.length;   // ❌ T 可能没有 length
}
```

用 `extends` 给类型参数设"上限"：

```ts
function len2<T extends { length: number }>(x: T): number {
  return x.length;
}

len2("hello");        // ✅ string 有 length
len2([1, 2, 3]);      // ✅
len2({ length: 5 });  // ✅
len2(123);            // ❌ number 没有 length
```

约束的另一个好处：**保留具体类型**，而不是退化成约束类型：

```ts
function longest<T extends { length: number }>(a: T, b: T): T {
  return a.length >= b.length ? a : b;
}
const s = longest("abc", "de");           // 返回类型是 "abc" | "de" 的拓宽结果：string
const arr = longest([1, 2], [1, 2, 3]);   // number[]
```

### 经典用法：`K extends keyof T`

约束一个类型参数是另一个类型的键：

```ts
function getProp<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}

const user = { id: 1, name: "April" };
const n = getProp(user, "name");   // string
const i = getProp(user, "id");     // number
getProp(user, "age");              // ❌ "age" 不是 user 的键
```

这个函数把"key 必须存在于 obj"和"返回值类型随 key 变化"同时保证了，是理解泛型的绝佳样例。

<a id="ch06-s04"></a>

## 6.4 泛型接口与类型别名

```ts
interface Box<T> {
  value: T;
}
const b1: Box<number> = { value: 1 };
const b2: Box<string[]> = { value: ["a"] };

type Result<T, E = Error> =
  | { ok: true; value: T }
  | { ok: false; error: E };

function divide(a: number, b: number): Result<number, string> {
  return b === 0 ? { ok: false, error: "divide by zero" } : { ok: true, value: a / b };
}

const r = divide(1, 0);
if (r.ok) {
  console.log(r.value);    // number
} else {
  console.log(r.error);    // string
}
```

上面 `E = Error` 是**默认类型参数**：不传就用默认。

### 实战：API 响应的泛型封装

```ts
interface ApiResponse<T> {
  code: number;
  message: string;
  data: T;
}

interface Page<T> {
  items: T[];
  total: number;
}

type UserListResp = ApiResponse<Page<{ id: number; name: string }>>;
```

<a id="ch06-s05"></a>

## 6.5 泛型类

```ts
class Stack<T> {
  private items: T[] = [];

  push(item: T): void {
    this.items.push(item);
  }
  pop(): T | undefined {
    return this.items.pop();
  }
  peek(): T | undefined {
    return this.items[this.items.length - 1];
  }
  get size(): number {
    return this.items.length;
  }
}

const s = new Stack<number>();
s.push(1);
s.push("2");   // ❌
```

<a id="ch06-s06"></a>

## 6.6 泛型的推断规则与常见技巧

### 6.6.1 从参数推断

```ts
function map<T, U>(arr: T[], fn: (x: T) => U): U[] {
  return arr.map(fn);
}
const lens = map(["a", "bb"], (s) => s.length);   // T=string, U=number，lens: number[]
```

### 6.6.2 不要让类型参数只出现一次

**经验法则：如果一个类型参数在签名里只出现一次，它大概率是多余的。**

```ts
// 不推荐：T 只出现一次，没有建立任何关联
function printAll<T extends string[]>(arr: T): void {}
// ✅ 直接写类型更清晰
function printAll2(arr: string[]): void {}
```

### 6.6.3 `const` 类型参数（TS 5.0+）

让推断保留字面量，而不用调用方写 `as const`：

```ts
function tuple<const T extends readonly unknown[]>(x: T): T {
  return x;
}
const t = tuple([1, "a"]);   // readonly [1, "a"]，而不是 (string | number)[]
```

### 6.6.4 默认类型参数

```ts
interface Event2<TPayload = unknown> {
  type: string;
  payload: TPayload;
}
const e1: Event2 = { type: "x", payload: 123 };               // payload: unknown
const e2: Event2<{ id: number }> = { type: "y", payload: { id: 1 } };
```

### 6.6.5 多个泛型之间的依赖

```ts
// U 依赖 T：从对象里取出多个键
function pick<T, K extends keyof T>(obj: T, keys: K[]): Pick<T, K> {
  const out = {} as Pick<T, K>;
  for (const k of keys) out[k] = obj[k];
  return out;
}

const u = { id: 1, name: "A", age: 18 };
const part = pick(u, ["id", "name"]);   // { id: number; name: string }
```

<a id="ch06-s07"></a>

## 6.7 泛型实战：给"工具（Tool）"建模

Agent 框架里，每个工具有参数类型和返回类型，泛型可以把它们关联起来：

```ts
interface Tool<TArgs, TResult> {
  name: string;
  description: string;
  run(args: TArgs): Promise<TResult>;
}

const weatherTool: Tool<{ city: string }, { temp: number; desc: string }> = {
  name: "get_weather",
  description: "查询城市天气",
  async run({ city }) {
    return { temp: 26, desc: `${city} 晴` };
  },
};

// 通用调用器：根据 tool 的类型，自动约束入参、推断出参
async function callTool<A, R>(tool: Tool<A, R>, args: A): Promise<R> {
  return tool.run(args);
}

const res = await callTool(weatherTool, { city: "深圳" });   // res: { temp: number; desc: string }
await callTool(weatherTool, { town: "深圳" });               // ❌ 参数名错误
```

<a id="ch06-s08"></a>

## 6.8 泛型与"类型体操"的边界

泛型最强大的用法是配合 `keyof`、条件类型、映射类型（第 8 章）。但要克制：

- **业务代码**：简单泛型（容器、响应封装、工具函数）就够
- **库/框架代码**：才需要复杂类型运算，且要写足测试和注释
- 判断标准：**同事能在 30 秒内看懂吗？** 看不懂就简化，或者拆成多个有名字的中间类型

<a id="ch06-s09"></a>

## 6.9 常见坑

| 坑 | 说明 | 正确做法 |
|---|---|---|
| 泛型函数体内对 `T` 做具体操作 | `T` 是未知类型，不能随意访问 | 加 `extends` 约束 |
| 类型参数只出现一次 | 多余的泛型 | 直接用具体类型 |
| 用 `any` 代替泛型 | 丢失类型联动 | 用泛型保持关联 |
| `.tsx` 里写 `<T>(x) => ...` 报错 | 与 JSX 标签冲突 | 写成 `<T,>(x: T) => ...` 或用 `function` |
| 返回 `{} as T` | 绕过检查 | 用 `Partial<T>` 过渡，或重新设计 |
| 把类型参数当值用 | 类型运行时不存在 | 想要运行时信息，需要显式传值（如 class 构造器） |

最后一条的例子：

```ts
function create<T>(): T {
  return new T();   // ❌ T 在运行时不存在
}
// 正确：把构造器作为值传进来
function create2<T>(Ctor: new () => T): T {
  return new Ctor();
}
class Foo { x = 1 }
const foo = create2(Foo);   // Foo
```

<a id="ch06-s10"></a>

## 本章小结

- 泛型 = 类型层面的参数，用来"保持类型之间的关联"
- `extends` 给泛型设上限；`K extends keyof T` 是最经典的组合
- 可以用在函数、接口、类型别名、类上；支持默认类型参数
- 保持克制：类型参数至少出现两次才有意义；业务代码别炫技

<a id="ch06-s11"></a>

## 练习

1. 实现 `function groupBy<T, K extends string>(arr: T[], key: (x: T) => K): Record<K, T[]>`。
|  |  |
| --- | --- |
2. 实现泛型类 `Cache<K, V>`，支持 `set`、`get`（返回 `V | undefined`）、`has`。
3. 给 `Result<T, E>` 写两个辅助函数 `ok(value)` 与 `err(error)`，并写一个 `map` 函数对成功值做转换。

---

<a id="ch07"></a>

# 第 7 章　类（Class）与面向对象

TS 的类 = ES6 的类 + 类型标注 + 访问修饰符等扩展。在 Agent / 后端项目里，类常用于封装"有状态的对象"：客户端、会话、插件、仓储等。

<a id="ch07-s01"></a>

## 7.1 基本写法

```ts
class User {
  id: number;
  name: string;

  constructor(id: number, name: string) {
    this.id = id;
    this.name = name;
  }

  greet(): string {
    return `Hi, I'm ${this.name}`;
  }
}

const u = new User(1, "April");
console.log(u.greet());
```

**`strictPropertyInitialization`**（`strict` 包含）要求：每个属性必须在声明处或构造器里初始化，否则报错：

```ts
class Bad {
  name: string;          // ❌ 没有初始化
}
class Ok1 { name = ""; }                                   // 声明时初始化
class Ok2 { name: string; constructor() { this.name = ""; } }  // 构造器初始化
class Ok3 { name!: string; }                               // 用 ! 明确声明"我保证稍后赋值"（慎用）
class Ok4 { name?: string; }                               // 或者声明为可选
```

<a id="ch07-s02"></a>

## 7.2 参数属性（Parameter Properties）：最常用的简写

在构造器参数前加修饰符，就同时**声明属性并赋值**：

```ts
class User2 {
  constructor(
    public id: number,
    public name: string,
    private password: string,
    readonly createdAt: Date = new Date(),
  ) {}
}

const u2 = new User2(1, "April", "secret");
u2.name;         // ✅
u2.password;     // ❌ private
```

> 注意：开启 `erasableSyntaxOnly`（TS 5.8+，用于 Node 直接运行 TS）时，参数属性**不被允许**，因为它不是纯类型语法。如果你的项目用 Node 的"类型擦除"运行，就回到 7.1 的显式写法。

<a id="ch07-s03"></a>

## 7.3 访问修饰符

| 修饰符 | 类内部 | 子类 | 类外部 |
|---|---|---|---|
| `public`（默认） | ✅ | ✅ | ✅ |
| `protected` | ✅ | ✅ | ❌ |
| `private` | ✅ | ❌ | ❌ |

```ts
class Account {
  public owner: string;
  protected balance = 0;
  private pin = "0000";

  constructor(owner: string) {
    this.owner = owner;
  }
}

class Savings extends Account {
  addInterest() {
    this.balance *= 1.01;    // ✅ protected 子类可访问
    this.pin;                // ❌ private 子类不可访问
  }
}
```

### TS `private` vs JS `#private`

```ts
class A {
  private x = 1;    // 仅编译期限制；运行时用 (a as any).x 仍能读到
  #y = 2;           // JS 原生私有字段，运行时真正私有
}
```

**需要真正的运行时私有，用 `#`；只需要编译期约束，用 `private`。**

<a id="ch07-s04"></a>

## 7.4 继承与 `override`

```ts
class Animal {
  constructor(public name: string) {}
  speak(): string {
    return `${this.name} makes a sound`;
  }
}

class Dog extends Animal {
  constructor(name: string, public breed: string) {
    super(name);           // 子类构造器必须先调用 super，才能使用 this
  }

  override speak(): string {     // noImplicitOverride 开启后，覆盖必须写 override
    return `${this.name} barks`;
  }
}

const d: Animal = new Dog("Rex", "Husky");   // 多态：子类可以赋给父类类型
d.speak();
```

`override` 的价值：父类方法改名后，子类的 `override` 会立刻报错，避免"以为在覆盖，其实是新增了一个方法"。

<a id="ch07-s05"></a>

## 7.5 抽象类（Abstract Class）

不能被直接实例化，用于定义"骨架 + 约定"：

```ts
abstract class Agent {
  constructor(protected name: string) {}

  abstract think(input: string): Promise<string>;   // 子类必须实现

  async run(input: string): Promise<string> {       // 通用流程由父类提供（模板方法模式）
    console.log(`[${this.name}] start`);
    const out = await this.think(input);
    console.log(`[${this.name}] done`);
    return out;
  }
}

class EchoAgent extends Agent {
  async think(input: string): Promise<string> {
    return `echo: ${input}`;
  }
}

const a = new Agent("x");        // ❌ 抽象类不能实例化
const e = new EchoAgent("echo");
```


<a id="ch07-s06"></a>

## 7.6 实现接口：`implements`

```ts
interface Disposable {
  dispose(): void;
}

class Connection implements Disposable {
  dispose() {
    console.log("closed");
  }
}
```

- `implements` 只**检查**类是否满足接口，不会"继承"任何实现
- 类可以实现多个接口：`class A implements I1, I2`
- **接口 vs 抽象类**：接口只有类型，编译后消失；抽象类有运行时存在，可带默认实现

<a id="ch07-s07"></a>

## 7.7 静态成员与 getter/setter

```ts
class Counter {
  static instances = 0;
  private _count = 0;

  constructor() {
    Counter.instances++;
  }

  get count(): number {
    return this._count;
  }
  set count(v: number) {
    if (v < 0) throw new Error("negative");
    this._count = v;
  }

  static create(): Counter {
    return new Counter();
  }
}

const c = Counter.create();
c.count = 5;
console.log(c.count, Counter.instances);
```

<a id="ch07-s08"></a>

## 7.8 类即类型

声明一个类，**同时得到一个值（构造函数）和一个类型（实例类型）**：

```ts
class Point {
  constructor(public x: number, public y: number) {}
}

const p: Point = new Point(1, 2);                    // Point 作类型
function make(ctor: typeof Point): Point {           // typeof Point 是"构造函数本身"的类型
  return new ctor(0, 0);
}
```

因为 TS 是结构化类型，**即使不是 `new Point` 创建的对象，只要形状一致也能赋给 `Point`**：

```ts
const p2: Point = { x: 1, y: 2 };   // ✅ 结构兼容（若 Point 有 private 成员则不再兼容）
```

> 带 `private/protected` 成员的类，会变成"半名义类型"：只有该类（及子类）的实例才兼容。

<a id="ch07-s09"></a>

## 7.9 `this` 类型与链式调用

```ts
class QueryBuilder {
  private parts: string[] = [];

  select(fields: string): this {       // 返回 this 类型，子类继承后链式调用仍保持子类类型
    this.parts.push(`SELECT ${fields}`);
    return this;
  }
  from(table: string): this {
    this.parts.push(`FROM ${table}`);
    return this;
  }
  build(): string {
    return this.parts.join(" ");
  }
}

const sql = new QueryBuilder().select("*").from("users").build();
```

<a id="ch07-s10"></a>

## 7.10 Mixin（了解）

TS 里实现"多继承"的方式——用函数返回类：

```ts
type Constructor<T = {}> = new (...args: any[]) => T;

function Timestamped<TBase extends Constructor>(Base: TBase) {
  return class extends Base {
    createdAt = new Date();
  };
}

class Doc {
  title = "";
}
const TimestampedDoc = Timestamped(Doc);
const d = new TimestampedDoc();
d.createdAt;
d.title;
```

<a id="ch07-s11"></a>

## 7.11 类 vs 函数式：什么时候用类

| 场景 | 建议 |
|---|---|
| 有状态 + 多个方法共享状态（客户端、连接、会话） | **类** |
| 需要继承、多态、抽象基类（插件体系） | **类** |
| 纯数据变换、工具函数 | **函数 + 对象类型** |
| 需要极好的可测试性/可组合 | 函数 + 依赖注入（把依赖作为参数） |

前端 React/Vue3、Node 工具类库倾向**函数式**；企业后端（NestJS 等）倾向**类 + 装饰器**。TS 两种都支持，可以混用。

<a id="ch07-s12"></a>

## 7.12 装饰器（简述）

TS 5.0+ 支持符合 ECMAScript 标准的装饰器（无需 `experimentalDecorators`）：

```ts
function logged<This, Args extends unknown[], Return>(
  target: (this: This, ...args: Args) => Return,
  context: ClassMethodDecoratorContext<This, (this: This, ...args: Args) => Return>,
) {
  return function (this: This, ...args: Args): Return {
    console.log(`call ${String(context.name)}`, args);
    return target.call(this, ...args);
  };
}

class Service {
  @logged
  run(x: number) {
    return x * 2;
  }
}
new Service().run(3);
```

NestJS、TypeORM 等老框架依赖的是**旧版实验性装饰器**（`experimentalDecorators: true`），两者不兼容，新项目注意区分。

<a id="ch07-s13"></a>

## 7.13 常见坑

| 坑 | 说明 | 正确做法 |
|---|---|---|
| 把方法当回调传，`this` 丢失 | `setTimeout(obj.method)` | 用箭头函数包一层，或在类里用箭头函数属性 |
| 构造器里使用 `this` 前未调用 `super` | 运行时报错 | 子类构造器第一行 `super(...)` |
| 过度继承 | 层级深、耦合高 | **组合优于继承** |
| 在构造器里做异步初始化 | 构造器不能 `await` | 用静态工厂方法 `static async create()` |
| `private` 当作安全机制 | 运行时可绕过 | 敏感数据别放客户端，或用 `#` |

构造器不能异步的解决方案：

```ts
class Client {
  private constructor(private conn: string) {}

  static async create(url: string): Promise<Client> {
    const conn = await Promise.resolve(`connected:${url}`);
    return new Client(conn);
  }
}
const client = await Client.create("http://x");
```

<a id="ch07-s14"></a>

## 本章小结

- 参数属性是最常用的简写；`strictPropertyInitialization` 要求属性必须初始化
- 修饰符：`public/protected/private/readonly`；运行时真私有用 `#`
- 继承用 `extends` + `override`，抽象类用 `abstract`，接口用 `implements`
- 类同时是值和类型；TS 仍是结构化类型
- 优先"组合优于继承"，函数式和类可混用

<a id="ch07-s15"></a>

## 练习

1. 设计抽象类 `Tool`，包含 `abstract name`、`abstract run(args)`，并实现两个子类 `SearchTool`、`CalcTool`。
2. 实现一个 `EventEmitter<Events>` 泛型类，`on(event, handler)` 与 `emit(event, payload)` 的参数类型根据 `Events` 映射自动推断。
3. 把一个使用 `private` 参数属性的类改写为兼容 `erasableSyntaxOnly` 的写法。

---

<a id="ch08"></a>

# 第 8 章　类型运算：keyof、条件类型、映射类型与工具类型

这一章是 TS 的"进阶核心"，也是别人口中的"类型体操"。别被吓到：**类型运算本质上就是"对类型做函数式变换"**。掌握下面这套积木，就能读懂 99% 的库类型。

> 学习方法：每个例子都在编辑器里**鼠标悬停**查看结果类型。

<a id="ch08-s01"></a>

## 8.1 `typeof`（类型位置）：从值得到类型

JS 里 `typeof` 返回字符串；**TS 在类型位置用 `typeof`，是取一个值的类型**。

```ts
const config = { host: "localhost", port: 3000, tls: false };
type Config = typeof config;   // { host: string; port: number; tls: boolean }

function connect(c: Config) {}

function add(a: number, b: number) { return a + b; }
type AddFn = typeof add;       // (a: number, b: number) => number
```

好处：**值是唯一的真相来源，类型自动跟随**，避免两处手写不同步。

<a id="ch08-s02"></a>

## 8.2 `keyof`：取对象类型的所有键

```ts
interface User { id: number; name: string; email: string }

type UserKey = keyof User;        // "id" | "name" | "email"

function getField(u: User, k: UserKey) {
  return u[k];                    // string | number
}
```

常与 `typeof` 配合：

```ts
const COLORS = { red: "#f00", green: "#0f0", blue: "#00f" };
type ColorName = keyof typeof COLORS;   // "red" | "green" | "blue"
```

<a id="ch08-s03"></a>

## 8.3 索引访问类型 `T[K]`

```ts
interface Order {
  id: string;
  items: { sku: string; qty: number }[];
  status: "pending" | "paid";
}

type Status = Order["status"];              // "pending" | "paid"
type Items = Order["items"];                // { sku: string; qty: number }[]
type Item = Order["items"][number];         // { sku: string; qty: number }  —— 取数组元素类型
type IdOrStatus = Order["id" | "status"];   // string | "pending" | "paid" => string

const ROLES = ["admin", "user"] as const;
type Role = (typeof ROLES)[number];         // "admin" | "user"
```

`T[number]` 是"取数组/元组所有元素类型联合"的惯用法。

<a id="ch08-s04"></a>

## 8.4 映射类型（Mapped Types）

**对一个类型的每个键做变换，生成新类型**，语法 `{ [K in Keys]: ... }`：

```ts
type Flags<T> = { [K in keyof T]: boolean };

interface Features { dark: string; beta: number }
type F = Flags<Features>;   // { dark: boolean; beta: boolean }
```

### 修饰符：`readonly`、`?` 以及用 `-` / `+` 去掉或添加

```ts
type MyPartial<T> = { [K in keyof T]?: T[K] };          // 全部可选
type MyRequired<T> = { [K in keyof T]-?: T[K] };        // 去掉 ?，全部必选
type MyReadonly<T> = { readonly [K in keyof T]: T[K] }; // 全部只读
type Mutable<T> = { -readonly [K in keyof T]: T[K] };   // 去掉 readonly
```

### 键重映射 `as`：改名、过滤

```ts
// 把所有键改成 getXxx 形式
type Getters<T> = {
  [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K];
};

interface Person { name: string; age: number }
type PersonGetters = Getters<Person>;
// { getName: () => string; getAge: () => number }

// 过滤：只保留函数类型的属性
type OnlyFunctions<T> = {
  [K in keyof T as T[K] extends (...args: any[]) => any ? K : never]: T[K];
};
```

> `as never` 的键会被**过滤掉**，这是映射类型里做"筛选"的标准技巧。

<a id="ch08-s05"></a>

## 8.5 条件类型（Conditional Types）

形如 `T extends U ? X : Y`，相当于类型层面的三元表达式：

```ts
type IsString<T> = T extends string ? true : false;

type A = IsString<"hi">;    // true
type B = IsString<123>;     // false
```

### 8.5.1 分配式条件类型（Distributive）

当 `T` 是**裸类型参数**且传入联合类型时，条件类型会**对联合的每个成员分别计算**，再合并：

```ts
type ToArray<T> = T extends unknown ? T[] : never;
type R = ToArray<string | number>;   // string[] | number[]

// 想禁用分配：用方括号包裹
type ToArray2<T> = [T] extends [unknown] ? T[] : never;
type R2 = ToArray2<string | number>; // (string | number)[]
```

分配的经典应用：`Exclude`、`Extract`（见 8.7）。

### 8.5.2 `infer`：在条件类型中"捕获"类型

`infer X` 声明一个待推断的类型变量，只能用在 `extends` 子句里：

```ts
// 取函数返回类型
type MyReturnType<T> = T extends (...args: any[]) => infer R ? R : never;
type R1 = MyReturnType<() => string>;                 // string

// 取函数参数元组
type MyParameters<T> = T extends (...args: infer P) => any ? P : never;
type P1 = MyParameters<(a: number, b: string) => void>;   // [a: number, b: string]

// 取数组元素类型
type ElementOf<T> = T extends (infer E)[] ? E : never;
type E1 = ElementOf<string[]>;                        // string

// 取 Promise 的结果类型（递归解包）
type Awaited2<T> = T extends Promise<infer U> ? Awaited2<U> : T;
type A2 = Awaited2<Promise<Promise<number>>>;         // number
```

**理解方式**：`infer` 就是"模式匹配"——给 `T` 套一个模板，模板里 `infer` 的位置就是你要取出来的部分。

### 8.5.3 条件类型的实战：根据入参决定返回类型

```ts
type Input = string | string[];
type Output<T extends Input> = T extends string ? number : number[];

declare function parse<T extends Input>(x: T): Output<T>;

const a = parse("1");          // number
const b = parse(["1", "2"]);   // number[]
```

<a id="ch08-s06"></a>

## 8.6 模板字面量类型

在类型层面做字符串拼接，甚至模式匹配：

```ts
type Greeting = `Hello, ${string}`;
const g: Greeting = "Hello, April";   // ✅
const g2: Greeting = "Hi, April";     // ❌

type Event = "click" | "focus";
type Handler = `on${Capitalize<Event>}`;   // "onClick" | "onFocus"

// 交叉组合：笛卡尔积
type Size = "sm" | "lg";
type Color = "red" | "blue";
type ClassName = `${Size}-${Color}`;       // "sm-red" | "sm-blue" | "lg-red" | "lg-blue"

// 配合 infer 解析
type ExtractId<S> = S extends `user:${infer Id}` ? Id : never;
type Id1 = ExtractId<"user:42">;           // "42"
```

内置的字符串工具类型：`Uppercase<S>`、`Lowercase<S>`、`Capitalize<S>`、`Uncapitalize<S>`。

<a id="ch08-s07"></a>

## 8.7 内置工具类型（Utility Types）速查

这些都是用上面的积木实现的，**建议先直接使用，再回头看实现**。

### 对象变换类

| 工具类型 | 作用 | 示例 |
|---|---|---|
| `Partial<T>` | 所有属性变可选 | `Partial<User>` |
| `Required<T>` | 所有属性变必选 | `Required<Config>` |
| `Readonly<T>` | 所有属性只读 | `Readonly<State>` |
| `Pick<T, K>` | 只保留指定的键 | `Pick<User, "id" \| "name">` |
| `Omit<T, K>` | 去掉指定的键 | `Omit<User, "password">` |
| `Record<K, V>` | 构造键值对象 | `Record<string, number>` |

```ts
interface User {
  id: number;
  name: string;
  password: string;
  email?: string;
}

type PublicUser = Omit<User, "password">;
type UserPreview = Pick<User, "id" | "name">;
type UserPatch = Partial<Omit<User, "id">>;      // 更新接口：除 id 外都可选
type UserDraft = Required<Pick<User, "name" | "email">>;
```

### 联合类型操作类

| 工具类型 | 作用 | 示例 |
|---|---|---|
| `Exclude<T, U>` | 从联合 T 中剔除可赋给 U 的成员 | `Exclude<"a"\|"b", "a">` → `"b"` |
| `Extract<T, U>` | 从联合 T 中保留可赋给 U 的成员 | `Extract<string\|number, number>` → `number` |
| `NonNullable<T>` | 去掉 `null` 和 `undefined` | `NonNullable<string \| null>` → `string` |


```ts
type Events = { type: "click"; x: number } | { type: "key"; code: string } | { type: "scroll" };
type ClickEvent = Extract<Events, { type: "click" }>;    // { type: "click"; x: number }
type NonScroll = Exclude<Events, { type: "scroll" }>;
```

实现（体会分配式条件类型）：

```ts
type MyExclude<T, U> = T extends U ? never : T;
type MyExtract<T, U> = T extends U ? T : never;
type MyNonNullable<T> = T extends null | undefined ? never : T;
```

### 函数相关类

| 工具类型 | 作用 |
|---|---|
| `ReturnType<F>` | 函数返回类型 |
| `Parameters<F>` | 函数参数元组 |
| `ConstructorParameters<C>` | 构造器参数元组 |
| `InstanceType<C>` | 构造器的实例类型 |
| `ThisParameterType<F>` / `OmitThisParameter<F>` | 与 `this` 参数相关 |
| `Awaited<T>` | 递归解包 Promise |

```ts
async function fetchUser(id: number) {
  return { id, name: "April" };
}

type FetchResult = Awaited<ReturnType<typeof fetchUser>>;   // { id: number; name: string }
type FetchArgs = Parameters<typeof fetchUser>;              // [id: number]
```

> `ReturnType<typeof asyncFn>` 得到的是 `Promise<...>`，需要再包一层 `Awaited<>`。

### 其他

| 工具类型 | 作用 |
|---|---|
| `NoInfer<T>`（TS 5.4+） | 阻止在该位置参与类型推断 |
| `Uppercase` 等 | 字符串类型转换 |

<a id="ch08-s08"></a>

## 8.8 `satisfies` 运算符（TS 4.9+）

场景：既想**检查**一个值符合某类型，又想**保留它更精确的推断类型**。

```ts
type Palette = Record<string, string | [number, number, number]>;

// 用类型标注：丢失精确信息
const p1: Palette = { red: [255, 0, 0], green: "#0f0" };
p1.red.map((x) => x);    // ❌ red 被拓宽为 string | [number, number, number]

// 用 satisfies：检查通过，同时保留各属性的精确类型
const p2 = { red: [255, 0, 0], green: "#0f0" } satisfies Palette;
p2.red.map((x) => x * 2);     // ✅ red 仍是 number[]（元组位置）
p2.green.toUpperCase();       // ✅ green 仍是 string
```

经验：**配置对象、路由表、工具注册表** 这类"既要检查又要精确"的场景，`satisfies` 非常好用。

<a id="ch08-s09"></a>

## 8.9 递归类型

类型可以引用自身，描述树、JSON 等：

```ts
type Json =
  | string
  | number
  | boolean
  | null
  | Json[]
  | { [key: string]: Json };

const data: Json = { a: [1, 2, { b: null }] };

// 深层 Partial
type DeepPartial<T> = T extends object
  ? { [K in keyof T]?: DeepPartial<T[K]> }
  : T;

// 树节点
interface TreeNode<T> {
  value: T;
  children: TreeNode<T>[];
}
```

<a id="ch08-s10"></a>

## 8.10 综合实战：做几个实用的类型工具

### 8.10.1 取对象里值类型为某种类型的键

```ts
type KeysOfType<T, V> = {
  [K in keyof T]: T[K] extends V ? K : never;
}[keyof T];

interface Form { name: string; age: number; email: string; active: boolean }
type StringKeys = KeysOfType<Form, string>;   // "name" | "email"
```

### 8.10.2 让某些键必选，其余保持原样

```ts
type RequireKeys<T, K extends keyof T> = T & Required<Pick<T, K>>;

interface Options { host?: string; port?: number; debug?: boolean }
type WithHost = RequireKeys<Options, "host">;
const o: WithHost = { host: "x" };    // host 必填
```

### 8.10.3 优美展开：`Prettify`

交叉类型在悬停时显示得很乱，用这个"展平"一下：

```ts
type Prettify<T> = { [K in keyof T]: T[K] } & {};
type Merged = Prettify<{ a: number } & { b: string }>;   // 悬停显示 { a: number; b: string }
```

### 8.10.4 事件系统：由映射推导出强类型的 on/emit

```ts
type EventMap = {
  login: { userId: string };
  logout: undefined;
  message: { from: string; text: string };
};

class Emitter<E extends Record<string, unknown>> {
  private handlers: { [K in keyof E]?: ((payload: E[K]) => void)[] } = {};

  on<K extends keyof E>(event: K, fn: (payload: E[K]) => void): void {
    (this.handlers[event] ??= []).push(fn);
  }
  emit<K extends keyof E>(event: K, payload: E[K]): void {
    this.handlers[event]?.forEach((fn) => fn(payload));
  }
}

const bus = new Emitter<EventMap>();
bus.on("message", (p) => console.log(p.from, p.text));   // p 自动推断
bus.emit("message", { from: "a", text: "hi" });
bus.emit("message", { from: "a" });                      // ❌ 缺少 text
```


<a id="ch08-s11"></a>

## 8.11 类型体操的"自我保护"准则

1. **优先用内置工具类型**，别重复造轮子
2. 复杂类型拆成**有名字的中间类型**，逐步组合
3. 给复杂类型写**类型测试**（用 `Equal` 断言，或 `expectTypeOf`）：

```ts
type Equal<A, B> =
  (<T>() => T extends A ? 1 : 2) extends (<T>() => T extends B ? 1 : 2) ? true : false;

type Expect<T extends true> = T;

type _t1 = Expect<Equal<Exclude<"a" | "b", "a">, "b">>;      // ✅ 通过
type _t2 = Expect<Equal<Exclude<"a" | "b", "a">, "a">>;      // ❌ 类型不相等，编译报错
```

4. 类型太复杂导致编辑器卡顿 / 报"类型实例化过深" → 简化
5. **业务代码里：能让运行时代码更简单，就别用类型体操**

<a id="ch08-s12"></a>

## 8.12 常见坑

| 坑 | 说明 | 正确做法 |
|---|---|---|
| 条件类型在联合类型上"意外分配" | 裸类型参数会触发分配 | 用 `[T] extends [U]` 包裹禁用 |
| `keyof` 对象含索引签名 | `keyof Record<string, X>` 是 `string \| number` | 注意 `number` 也会出现 |
| `Omit` 在联合类型上表现异常 | `Omit` 不分配，会破坏联合 | 自定义分配版 `DistributiveOmit` |
| `infer` 只能在 `extends` 子句用 | 否则语法错误 | 重新组织为条件类型 |
| 类型过深报错 `Type instantiation is excessively deep` | 递归太深 | 减少递归层数，或收尾递归优化 |

`Omit` 联合问题的例子：

```ts
type Shape = { kind: "a"; x: number } | { kind: "b"; y: number };
type Bad = Omit<Shape, "x">;       // 联合被"压扁"，kind 变成 "a" | "b"，y 也丢了
type DistributiveOmit<T, K extends PropertyKey> = T extends unknown ? Omit<T, K> : never;
type Good = DistributiveOmit<Shape, "x">;   // { kind: "a" } | { kind: "b"; y: number }
```

<a id="ch08-s13"></a>

## 本章小结

积木清单（建议背下来）：

| 积木 | 作用 |
|---|---|
| `typeof x` | 值 → 类型 |
| `keyof T` | 类型 → 键的联合 |
| `T[K]` | 取属性类型 |
| `{ [K in ...]: ... }` | 映射类型，遍历键 |
| `T extends U ? X : Y` | 条件类型，分配式 |
| `infer` | 模式匹配捕获类型 |
| `` `${A}-${B}` `` | 模板字面量类型 |
| `satisfies` | 检查但不拓宽 |
| 内置工具类型 | `Partial/Pick/Omit/Record/ReturnType/Awaited...` |

<a id="ch08-s14"></a>

## 练习

1. 手写 `MyPick<T, K extends keyof T>` 与 `MyOmit`（提示：`Exclude<keyof T, K>`）。
2. 实现 `DeepReadonly<T>`。
3. 实现 `Last<T extends unknown[]>`：取元组最后一个元素类型；`Last<[1, 2, 3]>` → `3`。
4. 实现 `CamelCase<S>`：把 `"user_name"` 转成 `"userName"`（提示：模板字面量 + `infer` + `Capitalize`）。

---

<a id="ch09"></a>

# 第 9 章　枚举、模块系统与声明文件

本章解决三个工程化问题：**枚举要不要用**、**代码怎么拆文件**、**没有类型的 JS 库怎么办**。

<a id="ch09-s01"></a>

## 9.1 枚举（enum）

### 9.1.1 数字枚举

```ts
enum Direction {
  Up,      // 0
  Down,    // 1
  Left,    // 2
  Right,   // 3
}

const d: Direction = Direction.Up;
console.log(Direction[0]);       // "Up"（数字枚举有反向映射）
```

可以指定起始值，之后自动递增：

```ts
enum HttpCode { Ok = 200, Created, Accepted }   // 200, 201, 202
```

### 9.1.2 字符串枚举

```ts
enum LogLevel {
  Debug = "DEBUG",
  Info = "INFO",
  Error = "ERROR",
}
const lv: LogLevel = LogLevel.Info;
```

### 9.1.3 `const enum`

编译时直接内联为常量，不生成对象。**但与 `isolatedModules`、Babel/esbuild 等工具链兼容性差，现代项目不推荐。**

### 9.1.4 枚举的编译产物

```ts
enum Color { Red, Green }
```

会编译成一个**运行时对象**：

```js
var Color;
(function (Color) {
  Color[Color["Red"] = 0] = "Red";
  Color[Color["Green"] = 1] = "Green";
})(Color || (Color = {}));
```

这意味着：**枚举不是纯类型语法**，它在运行时有代码。因此在"只擦除类型"的运行方式（Node 直接运行 TS、`erasableSyntaxOnly`）下，**枚举不被支持**。

### 9.1.5 枚举的已知问题

1. 数字枚举**不够安全**（早期版本任意数字都能赋给它）
2. 增加运行时代码、影响 tree-shaking
3. 与类型擦除运行方式冲突
4. 联合字面量类型能做到同样的事，更轻、更灵活

### 9.1.6 推荐替代：联合字面量 + `as const` 对象

```ts
// 方案 1：纯联合类型（最轻量）
type LogLevel = "debug" | "info" | "error";

// 方案 2：const 对象 + 类型（需要运行时可遍历、可取值时）
const LogLevels = {
  Debug: "debug",
  Info: "info",
  Error: "error",
} as const;
type LogLevel2 = (typeof LogLevels)[keyof typeof LogLevels];   // "debug" | "info" | "error"

function log(level: LogLevel2, msg: string) {}
log(LogLevels.Info, "ok");   // ✅
log("info", "ok");           // ✅ 直接写字面量也行
log("warn", "ok");           // ❌
```

**结论：新项目默认不用 enum。遇到老项目/框架（如 Angular）里的 enum，认识即可。**

<a id="ch09-s02"></a>

## 9.2 模块系统

### 9.2.1 什么是模块

TS 把"含有顶层 `import` 或 `export` 的文件"视为**模块**，拥有独立作用域；否则视为**全局脚本**，变量会污染全局。所以：**每个源文件都应该是模块**（需要时用 `export {}` 强制）。

### 9.2.2 导出与导入

```ts
// math.ts
export const PI = 3.14159;
export function add(a: number, b: number): number {
  return a + b;
}
export interface Point { x: number; y: number }
export default function main() {}      // 默认导出（每个文件最多一个）

// app.ts
import main, { PI, add } from "./math.js";       // 默认导入 + 具名导入
import { add as plus } from "./math.js";          // 重命名
import * as M from "./math.js";                   // 命名空间导入
import type { Point } from "./math.js";           // 只导入类型（编译后擦除）
import { type Point as P2, add as add2 } from "./math.js";   // 混合，行内 type

export { add } from "./math.js";                  // 再导出
export * from "./math.js";                        // 全部再导出
```

> **Node ESM 注意**：`module: NodeNext` 下，相对路径导入**必须带扩展名**，并且写 `.js`（即使源文件是 `.ts`）。这是因为 TS 不改写路径，运行时要加载的是编译后的 `.js`。

### 9.2.3 具名导出 vs 默认导出

| | 具名导出 | 默认导出 |
|---|---|---|
| 重命名 | 导入时必须一致（可用 `as`） | 导入方可随意命名（易造成混乱） |
| 重构 | IDE 重命名能同步 | 较难 |
| tree-shaking | 友好 | 一般 |
| 建议 | **默认优先使用** | 仅用于框架约定（如 Next.js 页面） |

### 9.2.4 `import type` 与 `verbatimModuleSyntax`

```ts
import type { User } from "./types.js";   // 一定会被擦除，不留运行时代码
import { type User2, createUser } from "./user.js";
```

开启 `"verbatimModuleSyntax": true`（推荐）后，TS 要求**仅作类型使用的导入必须写 `type`**，让"导入是否保留"完全可见，避免因循环依赖或副作用产生意外。

### 9.2.5 CommonJS 与 ESM

| | CommonJS (CJS) | ES Modules (ESM) |
|---|---|---|
| 语法 | `require` / `module.exports` | `import` / `export` |
| 加载 | 同步 | 异步，支持顶层 `await` |
| Node 中的标记 | `.cjs` 或 `package.json` 无 `"type": "module"` | `.mjs` 或 `"type": "module"` |
| 现状 | 老项目、部分工具仍在用 | **新项目首选** |

**新项目建议：`package.json` 设 `"type": "module"`，`tsconfig` 用 `"module": "NodeNext"`，全部用 ESM。**

### 9.2.6 路径别名

```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": { "@/*": ["src/*"] }
  }
}
```

```ts
import { add } from "@/utils/math";
```

> **注意**：`paths` 只影响类型检查，**不会改写运行时路径**。运行时需要打包器（Vite/webpack/esbuild）、`tsx`、或 `tsc-alias` 等工具处理。Node 原生运行建议改用 `package.json` 的 `imports` 字段（`"#utils/*"`）。

<a id="ch09-s03"></a>

## 9.3 命名空间（namespace）

```ts
namespace Utils {
  export function log(msg: string) { console.log(msg); }
}
Utils.log("hi");
```

历史产物，**现代项目不推荐**，用 ES 模块代替。同样不被类型擦除运行方式支持。仅在写 `.d.ts` 描述老式全局库时会见到。

<a id="ch09-s04"></a>

## 9.4 声明文件（`.d.ts`）

### 9.4.1 它是什么

`.d.ts` 文件**只含类型声明，不含实现**，用来"给已存在的 JS 代码补上类型"。

### 9.4.2 使用第三方库的类型

三种情况：

| 情况 | 例子 | 做法 |
|---|---|---|
| 库自带类型 | `zod`、`axios`、`openai` | 直接用，无需额外操作 |
| 社区类型包 `@types/xxx` | `@types/node`、`@types/express`、`@types/lodash` | `npm i -D @types/xxx` |
| 完全没有类型 | 某些老库 | 自己写声明（见下） |

### 9.4.3 为无类型库写声明

在项目里新建 `src/types/legacy-lib.d.ts`：

```ts
// 最简：整个模块当 any（快速解决，但无类型保护）
declare module "legacy-lib";

// 更好：描述你实际用到的部分
declare module "legacy-lib" {
  export function parse(input: string): { ok: boolean; value: unknown };
  export const version: string;
}
```

### 9.4.4 全局声明与扩展

```ts
// 声明全局变量（如构建工具注入的）
declare const __APP_VERSION__: string;

// 扩展已有的全局接口
declare global {
  interface Window {
    analytics: { track(event: string): void };
  }
  namespace NodeJS {
    interface ProcessEnv {
      NODE_ENV: "development" | "production";
      API_KEY: string;
    }
  }
}
export {};   // 让文件成为模块，declare global 才能生效
```

### 9.4.5 模块扩充（Module Augmentation）

给第三方库的类型"打补丁"：

```ts
import "express";
declare module "express" {
  interface Request {
    userId?: string;      // 给 req 增加自定义字段
  }
}
```

### 9.4.6 发布自己的库时

`tsconfig` 设 `"declaration": true`，`tsc` 会为每个 `.ts` 生成 `.d.ts`，并在 `package.json` 中指明：

```json
{
  "type": "module",
  "main": "./dist/index.js",
  "types": "./dist/index.d.ts",
  "exports": {
    ".": { "types": "./dist/index.d.ts", "default": "./dist/index.js" }
  }
}
```

<a id="ch09-s05"></a>

## 9.5 三斜线指令（了解）

```ts
/// <reference types="node" />
```

老式写法，现代项目多用 `tsconfig` 的 `types` 字段或直接 `import`。

<a id="ch09-s06"></a>

## 9.6 JSON 导入

```json
// tsconfig：开启 "resolveJsonModule": true
```

```ts
import pkg from "./package.json" with { type: "json" };
console.log(pkg.version);   // 类型自动推断为 string
```

<a id="ch09-s07"></a>

## 9.7 常见坑

| 坑 | 说明 | 正确做法 |
|---|---|---|
| Node ESM 下导入不写扩展名 | 运行时报 `ERR_MODULE_NOT_FOUND` | 相对路径写 `.js` |
| `paths` 别名运行时找不到 | `paths` 只给类型检查用 | 打包器/`tsx`/`imports` 字段 |
| 循环依赖 | A 导入 B，B 又导入 A | 抽取公共模块；类型循环用 `import type` |
| 忘记 `export {}` | 文件被当成全局脚本，变量冲突 | 加上 `export {}` |
| `declare global` 不生效 | 文件不是模块 | 文件里加至少一个 `import/export` |
| 滥用 `declare module "x";` | 变成 any | 逐步补全声明 |
| 滥用 `enum` | 与类型擦除运行冲突 | 联合字面量 + `as const` |

<a id="ch09-s08"></a>

## 本章小结

- 枚举会产生运行时代码，新项目优先 **联合字面量 / `as const` 对象**
- 项目全面使用 ESM，`NodeNext` 下相对路径带 `.js`
- `import type` + `verbatimModuleSyntax` 让导入行为清晰
- `.d.ts` 为无类型 JS 库提供类型；`declare global` / 模块扩充用于补丁式扩展
- `paths` 只作用于类型检查

<a id="ch09-s09"></a>

## 练习

1. 把一个 `enum Status { Pending, Done }` 改写为 `as const` 对象 + 联合类型，保持调用方式不变。
2. 写一个 `env.d.ts`，让 `process.env.API_KEY` 的类型变为 `string`。
3. 建两个文件 `a.ts`、`b.ts`，故意制造循环依赖，然后用 `import type` 解决类型层面的循环。

---

<a id="ch10"></a>

# 第 10 章　异步编程：Promise、async/await 与流

Agent 的本质就是大量的网络 I/O：调模型、调工具、读文件。**异步是 TS 写 Agent 的必修课**。

<a id="ch10-s01"></a>

## 10.1 JS 的并发模型（一分钟版）

- JS 是**单线程**，靠**事件循环（Event Loop）**处理异步
- 耗时操作（网络、文件、定时器）交给系统，完成后把回调放入队列，等主线程空闲时执行
- 所以**不会阻塞**，但也意味着**不要在主线程里写长时间同步计算**

```ts
console.log("1");
setTimeout(() => console.log("2"), 0);
Promise.resolve().then(() => console.log("3"));
console.log("4");
// 输出顺序：1 4 3 2
// 同步代码先执行 → 微任务（Promise）→ 宏任务（setTimeout）
```

<a id="ch10-s02"></a>

## 10.2 Promise

`Promise<T>` 代表"**将来会得到一个 T**"，有三种状态：`pending`（进行中）、`fulfilled`（成功）、`rejected`（失败）。

```ts
function delay(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function fetchNumber(): Promise<number> {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      Math.random() > 0.5 ? resolve(42) : reject(new Error("failed"));
    }, 10);
  });
}

fetchNumber()
  .then((n) => n * 2)                // n: number，返回新的 Promise<number>
  .then((n) => console.log(n))
  .catch((err) => console.error(err))
  .finally(() => console.log("done"));
```

<a id="ch10-s03"></a>

## 10.3 async / await

`async/await` 是 Promise 的语法糖，让异步代码"看起来像同步"。

```ts
async function getUser(id: number): Promise<{ id: number; name: string }> {
  await delay(10);
  return { id, name: "April" };      // 自动包装为 Promise
}

async function main() {
  const user = await getUser(1);     // 等待并取出 Promise 的值
  console.log(user.name);
}
```

规则：

1. `async` 函数**一定返回 Promise**（返回值类型写 `Promise<T>`）
2. `await` 只能在 `async` 函数里使用（或 ESM 顶层）
3. **顶层 await**：在 ESM 模块（`module: NodeNext/ES2022+`）里可以直接写 `await`

### 错误处理：`try/catch`

```ts
async function safeFetch(url: string): Promise<string | null> {
  try {
    const res = await fetch(url);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return await res.text();
  } catch (err) {
    // strict 下 err 是 unknown，必须收窄
    const msg = err instanceof Error ? err.message : String(err);
    console.error(msg);
    return null;
  }
}
```

<a id="ch10-s04"></a>

## 10.4 并发控制：串行 vs 并行

这是最常见的性能问题。

### 串行（慢）

```ts
async function serial(ids: number[]) {
  const results = [];
  for (const id of ids) {
    results.push(await getUser(id));   // 每个都要等上一个完成
  }
  return results;
}
```

### 并行：`Promise.all`

```ts
async function parallel(ids: number[]) {
  return Promise.all(ids.map((id) => getUser(id)));   // 同时发起，等全部完成
}
```

### 四个组合器对比

| 方法 | 行为 | 失败时 |
|---|---|---|
| `Promise.all([...])` | 全部成功才成功，返回结果数组 | **任一失败即整体失败**（快速失败） |
| `Promise.allSettled([...])` | 等所有结束，返回每个的状态 | 不会失败，自己看结果 |
| `Promise.race([...])` | 第一个**结束**的（成功或失败）决定结果 | 取决于最快那个 |
| `Promise.any([...])` | 第一个**成功**的 | 全部失败才失败（`AggregateError`） |

```ts
const settled = await Promise.allSettled([getUser(1), getUser(2)]);
for (const r of settled) {
  if (r.status === "fulfilled") console.log(r.value.name);
  else console.error(r.reason);
}

// 典型用法：超时控制
function withTimeout<T>(p: Promise<T>, ms: number): Promise<T> {
  const timeout = new Promise<never>((_, reject) =>
    setTimeout(() => reject(new Error("timeout")), ms),
  );
  return Promise.race([p, timeout]);
}
```

`Promise.all` 的元组类型推断很强：

```ts
const [u, n] = await Promise.all([getUser(1), fetchNumber().catch(() => 0)]);
// u: { id: number; name: string }, n: number
```

### 限制并发数

一次性发 1000 个请求会被限流或压垮服务。简单的并发池：

```ts
async function mapLimit<T, R>(
  items: T[],
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

// 同时最多 3 个并发
const users = await mapLimit([1, 2, 3, 4, 5, 6], 3, (id) => getUser(id));
```

<a id="ch10-s05"></a>

## 10.5 常见异步陷阱

### 陷阱 1：`forEach` 里用 `await` 不会等待

```ts
const ids = [1, 2, 3];
ids.forEach(async (id) => {
  await getUser(id);          // forEach 不会等这些 Promise
});
console.log("forEach 返回时，上面的请求还没完成");

// ✅ 正确：for...of 串行，或 Promise.all 并行
for (const id of ids) await getUser(id);
await Promise.all(ids.map((id) => getUser(id)));
```

### 陷阱 2：忘记 `await`（浮动 Promise）

```ts
async function save() {
  getUser(1);        // ❌ 没有 await，错误会变成"未处理的 rejection"，且顺序不可控
  await getUser(1);  // ✅
}
```

开启 ESLint 规则 `@typescript-eslint/no-floating-promises` 能自动抓出这类问题（见第 12 章）。

### 陷阱 3：`async` 函数里 `return` 与 `return await` 的区别

```ts
async function a() {
  try {
    return getUser(1);          // 异常不会被本函数的 catch 捕获
  } catch { return null; }
}
async function b() {
  try {
    return await getUser(1);    // ✅ 异常会被捕获
  } catch { return null; }
}
```

### 陷阱 4：在循环里创建 Promise 却不收集

```ts
const tasks = ids.map((id) => getUser(id));   // 此时请求已经发出了
// 之后记得 await Promise.all(tasks)，否则错误无人处理
```

<a id="ch10-s06"></a>

## 10.6 取消：AbortController

给请求、工具调用提供**可取消**能力（Agent 里"用户中途停止"非常常见）：

```ts
async function fetchWithCancel(url: string, signal: AbortSignal) {
  const res = await fetch(url, { signal });
  return res.text();
}

const ctrl = new AbortController();
setTimeout(() => ctrl.abort(), 1000);     // 1 秒后取消

try {
  await fetchWithCancel("https://example.com", ctrl.signal);
} catch (e) {
  if (e instanceof DOMException && e.name === "AbortError") {
    console.log("已取消");
  } else {
    throw e;
  }
}

// 内置的超时信号
await fetch("https://example.com", { signal: AbortSignal.timeout(5000) });
```

**设计建议：任何会耗时的自定义异步函数，都应该接收一个可选的 `signal?: AbortSignal` 参数，并向下透传。**

<a id="ch10-s07"></a>

## 10.7 异步迭代器与流式输出

LLM 的流式响应（SSE/stream）是 Agent 的日常。核心语法是 `for await...of` 与 `async function*`：

```ts
// 异步生成器：每次 yield 一个值
async function* streamTokens(text: string): AsyncGenerator<string, void, void> {
  for (const ch of text) {
    await delay(5);
    yield ch;
  }
}

// 消费
let out = "";
for await (const token of streamTokens("Hello")) {
  out += token;
  process.stdout.write(token);
}
```

类型要点：

- `AsyncGenerator<T, TReturn, TNext>` 或更简洁的 `AsyncIterable<T>` / `AsyncIterableIterator<T>`
- 对外暴露流式 API 时，返回 `AsyncIterable<T>` 即可

### 实用：把流式输出收集为完整文本

```ts
async function collect(stream: AsyncIterable<string>): Promise<string> {
  let s = "";
  for await (const chunk of stream) s += chunk;
  return s;
}
```

### 变换流：管道式处理

```ts
async function* mapStream<T, R>(src: AsyncIterable<T>, fn: (x: T) => R): AsyncGenerator<R> {
  for await (const x of src) yield fn(x);
}

const upper = mapStream(streamTokens("abc"), (c) => c.toUpperCase());
console.log(await collect(upper));   // "ABC"
```

<a id="ch10-s08"></a>

## 10.8 重试与退避（Agent 必备）

调用外部 API 失败是常态，需要**指数退避重试**：

```ts
interface RetryOptions {
  retries?: number;
  baseDelayMs?: number;
  shouldRetry?: (err: unknown, attempt: number) => boolean;
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
      if (attempt === retries || !shouldRetry(err, attempt)) break;
      const wait = baseDelayMs * 2 ** attempt + Math.random() * 100;   // 指数退避 + 抖动
      await delay(wait);
    }
  }
  throw lastErr;
}

const n = await retry(() => fetchNumber(), { retries: 5 });
```

<a id="ch10-s09"></a>

## 10.9 事件循环里的"微任务饥饿"（了解）

```ts
// 无限的微任务会让宏任务（定时器、I/O）永远得不到执行
function loop() { Promise.resolve().then(loop); }
```

写递归 Promise 链时留意；长时间 CPU 计算可以拆分，或交给 `worker_threads`。

<a id="ch10-s10"></a>

## 10.10 常见坑速查

| 坑 | 说明 | 正确做法 |
|---|---|---|
| `forEach(async ...)` | 不会等待 | `for...of` 或 `Promise.all(map)` |
| 浮动 Promise | 错误无人捕获 | 总是 `await`/`.catch`，开 lint 规则 |
| 无限制并发 | 限流/内存爆 | 并发池、`p-limit` |
| 串行写成了 `await` 在循环里，但其实可并行 | 性能差 | `Promise.all` |
| 捕获了错误却不处理 | 吞掉异常 | 记录日志并重新抛出或返回 `Result` |
| 忘记超时 | 请求挂起，Agent 卡死 | `AbortSignal.timeout` |
| 在 `async` 回调里抛错 | 外层 `try/catch` 抓不到 | 在回调内部处理 |

<a id="ch10-s11"></a>

## 本章小结

- `Promise<T>` + `async/await` 是异步基础；await 只能在 async/顶层模块里用
- `Promise.all/allSettled/race/any` 的差异要牢记
- 并行用 `Promise.all`，大批量用并发池限流
- 用 `AbortController` 支持取消与超时；耗时函数都应接受 `signal`
- 流式输出用 `async function*` + `for await`
- 外部调用要配**重试 + 退避 + 超时**

<a id="ch10-s12"></a>

## 练习

1. 实现 `timeout<T>(p: Promise<T>, ms: number): Promise<T>`，超时抛错。
2. 写一个 `async function* chunk<T>(src: AsyncIterable<T>, size: number)`，把流按固定大小打包成数组再输出。
3. 用 `mapLimit` 并发抓取 20 个 URL（可用模拟函数），限制并发为 4，并验证实际最大并发数不超过 4。

---

<a id="ch11"></a>

# 第 11 章　错误处理与运行时校验

**TS 的类型在运行时不存在。** 这意味着：来自外部的数据（HTTP、文件、用户输入、**LLM 输出**）仍然需要运行时校验。本章讲两件事：怎么优雅地处理错误，怎么把"类型"和"运行时校验"统一起来。

<a id="ch11-s01"></a>

## 11.1 JS 的错误机制

```ts
try {
  throw new Error("boom");
} catch (e) {
  // strict 下 e 是 unknown（useUnknownInCatchVariables）
  if (e instanceof Error) console.log(e.message, e.stack);
}
```

注意：**JS 里可以 `throw` 任何东西**（字符串、对象……），所以 `catch` 到的永远是 `unknown`，必须收窄。

```ts
function toMessage(e: unknown): string {
  if (e instanceof Error) return e.message;
  if (typeof e === "string") return e;
  try { return JSON.stringify(e); } catch { return String(e); }
}
```

<a id="ch11-s02"></a>

## 11.2 自定义错误类

```ts
class AppError extends Error {
  constructor(
    message: string,
    public readonly code: string,
    options?: { cause?: unknown },
  ) {
    super(message, options);       // ES2022 的 cause 支持，保留错误链
    this.name = "AppError";
  }
}

class NotFoundError extends AppError {
  constructor(resource: string, id: string) {
    super(`${resource} ${id} not found`, "NOT_FOUND");
    this.name = "NotFoundError";
  }
}

try {
  throw new NotFoundError("User", "42");
} catch (e) {
  if (e instanceof NotFoundError) console.log(e.code);
  else if (e instanceof AppError) console.log("app error");
  else throw e;       // 不认识的错误，继续向上抛，不要吞掉！
}
```

### 用 `cause` 保留原始错误

```ts
async function loadConfig(path: string) {
  try {
    return JSON.parse(path);
  } catch (e) {
    throw new AppError("配置解析失败", "CONFIG_INVALID", { cause: e });
  }
}
```

<a id="ch11-s03"></a>

## 11.3 两种错误处理风格

### 风格 A：异常（throw/catch）

- 优点：写起来简单，错误自动向上冒泡
- 缺点：**函数签名看不出会抛什么**，调用者容易漏处理

### 风格 B：Result 类型（把错误作为返回值）

```ts
type Result<T, E = Error> =
  | { ok: true; value: T }
  | { ok: false; error: E };

const ok = <T>(value: T): Result<T, never> => ({ ok: true, value });
const err = <E>(error: E): Result<never, E> => ({ ok: false, error });

function parseJson(text: string): Result<unknown, string> {
  try {
    return ok(JSON.parse(text));
  } catch {
    return err("invalid json");
  }
}

const r = parseJson("{}");
if (!r.ok) {
  console.error(r.error);     // string
} else {
  console.log(r.value);       // unknown
}
```

优点：**错误成为类型的一部分，调用方被编译器强制处理**。缺点：写法稍繁琐，需要团队统一约定。

### 怎么选

| 场景 | 建议 |
|---|---|
| "预期内"的失败（校验不通过、查不到、工具调用失败） | **Result 类型** |
| "不应该发生"的错误（程序 bug、基础设施崩溃） | `throw` |
| 库/SDK 的公共 API | 通常用 `throw`（符合 JS 生态习惯），并在文档里写明 |
| Agent 的工具调用 | 工具内部捕获错误并**返回给模型**，让模型自己决定重试 |

<a id="ch11-s04"></a>

## 11.4 为什么需要运行时校验

```ts
interface User { id: number; name: string }

const res = await fetch("/api/user");
const user = (await res.json()) as User;   // ⚠️ 只是对编译器撒谎
user.name.toUpperCase();                   // 如果后端返回 { id: 1 }，这里在运行时炸
```

`res.json()` 返回 `any`/`unknown`，用 `as` 断言**没有任何保护**。**所有边界处的数据都要校验**：

- HTTP 响应、请求体
- 读取的文件、环境变量
- 数据库查询结果（部分 ORM 已帮你做了）
- **LLM 的输出（尤其是 JSON / tool call 的参数）**——这点在 Agent 中最关键

<a id="ch11-s05"></a>

## 11.5 手写校验的痛点

```ts
function isUser(x: unknown): x is User {
  return (
    typeof x === "object" && x !== null &&
    typeof (x as any).id === "number" &&
    typeof (x as any).name === "string"
  );
}
```

问题：类型定义和校验逻辑**要写两遍**，且容易不同步。解决办法：**从校验器推导类型**——"schema 即类型"。

<a id="ch11-s06"></a>

## 11.6 zod：最流行的运行时校验库

```bash
npm i zod
```

### 基本使用

```ts
import { z } from "zod";

const UserSchema = z.object({
  id: z.number().int().positive(),
  name: z.string().min(1),
  email: z.string().email().optional(),
  role: z.enum(["admin", "user"]).default("user"),
  tags: z.array(z.string()).default([]),
});

// ⭐ 从 schema 自动推导 TS 类型
type User = z.infer<typeof UserSchema>;
// { id: number; name: string; email?: string; role: "admin" | "user"; tags: string[] }

// 两种解析方式
const parsed = UserSchema.parse({ id: 1, name: "April" });        // 失败直接 throw ZodError
const result = UserSchema.safeParse({ id: "x" });                  // 失败返回 { success: false, error }
if (result.success) {
  console.log(result.data.name);         // 类型已是 User
} else {
  console.log(result.error.issues);      // 详细的错误列表（路径 + 原因）
}
```

### 常用 schema 速查

```ts
z.string().min(1).max(100).regex(/^[a-z]+$/);
z.number().int().min(0).max(100);
z.boolean();
z.literal("admin");
z.enum(["a", "b"]);
z.union([z.string(), z.number()]);
z.array(z.string()).nonempty();
z.record(z.string(), z.number());              // Record<string, number>
z.tuple([z.string(), z.number()]);
z.string().nullable();                          // string | null
z.string().optional();                          // string | undefined

// 可辨识联合
const Shape = z.discriminatedUnion("kind", [
  z.object({ kind: z.literal("circle"), radius: z.number() }),
  z.object({ kind: z.literal("rect"), w: z.number(), h: z.number() }),
]);

// 转换与自定义校验
const NumFromString = z.string().transform((s) => Number(s));
const Even = z.number().refine((n) => n % 2 === 0, "必须是偶数");

// 对象操作
const Patch = UserSchema.partial().omit({ id: true });
const Strict = UserSchema.strict();            // 不允许多余字段
```

### 在边界处使用

```ts
async function getUser(id: number): Promise<User> {
  const res = await fetch(`/api/users/${id}`);
  const json: unknown = await res.json();
  return UserSchema.parse(json);       // 运行时校验 + 得到有类型保障的值
}
```

### 环境变量校验（强烈推荐）

```ts
const EnvSchema = z.object({
  NODE_ENV: z.enum(["development", "production", "test"]).default("development"),
  PORT: z.coerce.number().default(3000),           // coerce：字符串自动转数字
  API_KEY: z.string().min(1),
});

export const env = EnvSchema.parse(process.env);   // 启动时就失败，而不是运行到一半才炸
```

### 同类库对比

| 库 | 特点 |
|---|---|
| **zod** | 生态最大，API 友好，Agent/LLM SDK 广泛采用 |
| valibot | 体积小，tree-shaking 友好 |
| ArkType | 语法接近 TS 类型本身，性能高 |
| typebox | 基于 JSON Schema，性能好 |

<a id="ch11-s07"></a>

## 11.7 Agent 场景：校验 LLM 输出

LLM 输出不可信。**任何要让程序使用的 LLM 输出，都必须过一遍 schema。**

```ts
import { z } from "zod";

const ToolCallSchema = z.object({
  name: z.string(),
  arguments: z.record(z.string(), z.unknown()),
});

function parseToolCall(raw: string) {
  let json: unknown;
  try {
    json = JSON.parse(raw);
  } catch {
    return { ok: false as const, error: "不是合法 JSON" };
  }
  const r = ToolCallSchema.safeParse(json);
  return r.success
    ? { ok: true as const, value: r.data }
    : { ok: false as const, error: r.error.issues.map((i) => `${i.path.join(".")}: ${i.message}`).join("; ") };
}

// 校验失败时，把错误信息喂回给模型，让它自我修正（经典的"重试修复"循环）
```

### 把 zod schema 变成 JSON Schema 给模型

模型 API 里的"工具定义"要的是 JSON Schema，可以由 zod 生成，**一份 schema 同时服务于：给模型的描述、运行时校验、TS 类型**：

```ts
// zod v4 内置：z.toJSONSchema(schema)
// zod v3 可用第三方包 zod-to-json-schema
const WeatherArgs = z.object({
  city: z.string().describe("城市名，如 深圳"),
  unit: z.enum(["c", "f"]).default("c"),
});
const jsonSchema = z.toJSONSchema(WeatherArgs);   // 可直接放进工具定义的 parameters
```

<a id="ch11-s08"></a>

## 11.8 类型层面防止"忘记处理错误"

配合第 5 章的可辨识联合与穷尽检查：

```ts
type ToolResult =
  | { status: "ok"; output: string }
  | { status: "error"; message: string; retryable: boolean }
  | { status: "timeout" };

function handle(r: ToolResult): string {
  switch (r.status) {
    case "ok": return r.output;
    case "error": return r.retryable ? "will retry" : r.message;
    case "timeout": return "timed out";
  }
}
```

<a id="ch11-s09"></a>

## 11.9 常见坑

| 坑 | 说明 | 正确做法 |
|---|---|---|
| `JSON.parse(x) as T` | 对编译器撒谎 | 先解析为 `unknown`，再用 schema 校验 |
| 吞掉错误 `catch {}` | 排查噩梦 | 至少记录日志，或重新抛出 |
| 把业务失败也 `throw` | 控制流混乱、性能差 | 预期内失败用 `Result` |
| `catch (e)` 直接用 `e.message` | e 是 unknown | 先 `instanceof Error` |
| 校验只在前端 | 后端不能信任客户端 | 服务端必须校验 |
| 自己定义的类型和 schema 两份 | 容易不一致 | 只维护 schema，`z.infer` 出类型 |
| 过度校验内部数据 | 浪费性能、代码噪音 | **只在系统边界校验**，内部信任类型 |

<a id="ch11-s10"></a>

## 本章小结

- `catch` 到的是 `unknown`；自定义 Error 类 + `cause` 保留错误链
- 预期内的失败用 `Result`，意外用 `throw`
- 类型 ≠ 运行时保障：**系统边界必须运行时校验**
- 用 zod 做"schema 即类型"：`z.infer`；环境变量、HTTP 响应、LLM 输出统统校验
- schema 还能生成 JSON Schema 给模型使用

<a id="ch11-s11"></a>

## 练习

|  |  |
| --- | --- |
1. 用 zod 定义一个"聊天工具调用"的 schema：`{ id, name, arguments }`，其中 `name` 限定在 `"search" | "calc"`，并按 `name` 使用不同的 `arguments` 结构（提示：`discriminatedUnion`）。
2. 实现 `parseOrThrow<T>(schema: z.ZodType<T>, data: unknown): T`，错误信息里带上出错字段路径。
3. 设计一个 `Result` 版本的 `fetchJson(url, schema)`，让调用方无法忽略失败分支。

---

<a id="ch12"></a>

# 第 12 章　工程实践：项目结构、Lint、测试与构建

前面讲的都是"语言"，这一章讲"如何把 TS 项目真正跑起来并长期维护"。

<a id="ch12-s01"></a>

## 12.1 推荐的项目结构

```
my-project/
├── src/
│   ├── index.ts              # 入口
│   ├── config.ts             # 环境变量与配置（zod 校验）
│   ├── domain/               # 领域类型与纯逻辑
│   ├── services/             # 业务服务
│   ├── tools/                # （Agent 项目）工具实现
│   └── utils/
├── tests/                    # 测试
├── package.json
├── tsconfig.json
├── eslint.config.js
└── .gitignore                # 忽略 node_modules、dist
```

原则：

- **按功能（领域）分，而不是按技术类型分**：`user/`（含类型、服务、路由）比到处是 `types/`、`services/` 更易维护
- 一个文件一个主要职责；文件超过几百行就考虑拆分
- 对外暴露的 API 统一从 `index.ts` 导出

<a id="ch12-s02"></a>

## 12.2 package.json 与脚本

```json
{
  "name": "my-project",
  "version": "0.1.0",
  "type": "module",
  "engines": { "node": ">=22" },
  "scripts": {
    "dev": "tsx watch src/index.ts",
    "build": "tsc -p tsconfig.build.json",
    "start": "node dist/index.js",
    "typecheck": "tsc --noEmit",
    "lint": "eslint .",
    "test": "vitest run",
    "check": "npm run typecheck && npm run lint && npm run test"
  }
}
```

`npm run check` 作为**本地提交前 / CI 的统一入口**。

<a id="ch12-s03"></a>

## 12.3 tsconfig 进阶配置

### 12.3.1 严格度进阶选项

| 选项 | 作用 | 建议 |
|---|---|---|
| `noUncheckedIndexedAccess` | 索引访问带 `undefined` | 开 |
| `exactOptionalPropertyTypes` | 区分"属性缺失"与"值为 undefined" | 视团队而定，较严格 |
| `noImplicitReturns` | 所有分支都要有返回 | 开 |
| `noFallthroughCasesInSwitch` | switch 不允许意外穿透 | 开 |
| `noUnusedLocals` / `noUnusedParameters` | 未使用的变量/参数报错 | 交给 ESLint 更灵活 |
| `verbatimModuleSyntax` | 强制 `import type` 规范 | 开 |
| `isolatedModules` | 保证每个文件可独立转译（与 esbuild/swc 兼容） | 开 |
| `erasableSyntaxOnly` | 禁止 enum/namespace/参数属性等非纯类型语法 | 想用 Node 直接跑 TS 时开 |

### 12.3.2 拆分配置：开发与构建

`tsconfig.json`（编辑器与类型检查，包含测试）：

```json
{
  "compilerOptions": { "strict": true, "module": "NodeNext", "target": "ES2022", "noEmit": true },
  "include": ["src", "tests"]
}
```

`tsconfig.build.json`（构建产物，排除测试）：

```json
{
  "extends": "./tsconfig.json",
  "compilerOptions": { "noEmit": false, "outDir": "dist", "rootDir": "src", "declaration": true },
  "include": ["src"]
}
```

### 12.3.3 项目引用（Monorepo，了解）

多包仓库用 `references` + `composite: true` 做增量构建；配合 pnpm workspace / turborepo。

<a id="ch12-s04"></a>

## 12.4 ESLint：代码质量守门员

TS 官方生态用 **typescript-eslint**：

```bash
npm i -D eslint typescript-eslint
```

`eslint.config.js`（flat config）：

```js
import eslint from "@eslint/js";
import tseslint from "typescript-eslint";

export default tseslint.config(
  eslint.configs.recommended,
  ...tseslint.configs.recommendedTypeChecked,      // 带类型信息的规则
  {
    languageOptions: {
      parserOptions: { projectService: true, tsconfigRootDir: import.meta.dirname },
    },
    rules: {
      "@typescript-eslint/no-floating-promises": "error",     // 抓"忘记 await"
      "@typescript-eslint/no-misused-promises": "error",
      "@typescript-eslint/consistent-type-imports": "error",  // 强制 import type
      "@typescript-eslint/no-explicit-any": "warn",
      "@typescript-eslint/switch-exhaustiveness-check": "error", // switch 穷尽检查
    },
  },
  { ignores: ["dist", "node_modules"] },
);
```

最值得开的几条规则：

| 规则 | 防止的问题 |
|---|---|
| `no-floating-promises` | 忘记 `await` 导致的错误吞没 |
| `no-misused-promises` | 把 async 函数传给不处理 Promise 的地方 |
| `switch-exhaustiveness-check` | 联合类型 switch 漏分支 |
| `no-unnecessary-type-assertion` | 无用的 `as` |
| `no-explicit-any` | 滥用 any |

**格式化交给 Prettier（或 Biome）**，不要用 ESLint 管格式。Biome 是一体化的 lint + format 替代方案，速度非常快。

<a id="ch12-s05"></a>

## 12.5 测试

### Vitest（推荐，API 类似 Jest，原生支持 TS/ESM）

```bash
npm i -D vitest
```

```ts
// src/math.ts
export const add = (a: number, b: number) => a + b;

// tests/math.test.ts
import { describe, it, expect, vi } from "vitest";
import { add } from "../src/math.js";

describe("add", () => {
  it("adds numbers", () => {
    expect(add(1, 2)).toBe(3);
  });

  it("works with mocks", () => {
    const fn = vi.fn((x: number) => x * 2);
    expect(fn(2)).toBe(4);
    expect(fn).toHaveBeenCalledWith(2);
  });
});
```

### 测试类型本身

```ts
import { expectTypeOf } from "vitest";

expectTypeOf<ReturnType<typeof add>>().toEqualTypeOf<number>();
expectTypeOf(add).parameter(0).toBeNumber();
```

### 测试异步与错误

```ts
it("rejects on error", async () => {
  await expect(Promise.reject(new Error("x"))).rejects.toThrow("x");
});
```

### Agent 项目的测试策略

- **工具函数**：纯函数，直接单测
- **Agent 循环**：用**假的 LLM（mock）**脚本化返回固定的 tool call，验证流程
- **提示词与效果**：用评测集（eval）而不是单测
- 真实调用 API 的测试放进单独的"集成测试"，默认不跑

<a id="ch12-s06"></a>

## 12.6 构建与打包

| 场景 | 方案 |
|---|---|
| Node 服务/CLI，直接发布 | `tsc` 输出 JS 即可 |
| 需要单文件、更快启动 | `esbuild` / `tsup` / `tsdown` 打包 |
| 前端 Web | Vite（内部用 esbuild/Rollup） |
| 发布 npm 库 | `tsup`：同时输出 ESM/CJS + `.d.ts` |
| 极简开发运行 | `tsx` / `node xxx.ts` |

**注意：多数打包器只擦除类型、不做类型检查**，所以 CI 一定要有 `tsc --noEmit`。

<a id="ch12-s07"></a>

## 12.7 依赖管理

- 包管理器：`pnpm`（快、省空间、严格）> `npm` > `yarn`
- 区分 `dependencies`（运行时需要）与 `devDependencies`（开发/类型/测试）
- 类型包 `@types/*` 放 `devDependencies`
- 提交 `package-lock.json` / `pnpm-lock.yaml`，保证可复现
- 定期升级依赖，尤其是 `typescript`、`typescript-eslint`（大版本要读迁移说明）

<a id="ch12-s08"></a>

## 12.8 Git 与 CI 示例

`.gitignore`：

```
node_modules
dist
.env
*.tsbuildinfo
```

GitHub Actions 示例（其他 CI 同理）：

```yaml
name: ci
on: [push, pull_request]
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 22, cache: npm }
      - run: npm ci
      - run: npm run check
```

<a id="ch12-s09"></a>

## 12.9 日志与配置

```ts
// config.ts：集中、校验、只读
import { z } from "zod";

const Schema = z.object({
  LOG_LEVEL: z.enum(["debug", "info", "warn", "error"]).default("info"),
  MODEL: z.string().default("gpt-4o"),
  API_KEY: z.string().min(1),
});

export const config = Object.freeze(Schema.parse(process.env));
```

生产日志推荐 `pino`（结构化 JSON 日志）。**绝不要把密钥、用户隐私写进日志。**

<a id="ch12-s10"></a>

## 12.10 性能与类型检查速度

- 大项目 `tsc` 慢：开 `incremental`、`skipLibCheck`，用项目引用拆分
- 编辑器卡：检查是否有**过度复杂的类型**、巨大的联合类型（>几百成员）
- 用 `tsc --extendedDiagnostics` 或 `--generateTrace` 分析慢点
- TS 7 起编译器用原生语言重写（官方称 native port），速度显著提升，升级可以重点关注

<a id="ch12-s11"></a>

## 12.11 渐进迁移：JS 项目 → TS

1. 加 `tsconfig.json`，`allowJs: true`、`checkJs: false`
2. 按目录/文件逐步把 `.js` 改成 `.ts`
3. 先接受大量 `any`，用 `// @ts-expect-error` 标记暂时无法修复处（优于 `@ts-ignore`，因为问题修复后会提示删除）
4. 逐步开启 `strict` 子选项：`noImplicitAny` → `strictNullChecks` → 其余
5. 最终全部 `strict`

```ts
// @ts-expect-error —— 已知问题，TODO: 迁移后移除
const x: number = "1";
```

<a id="ch12-s12"></a>

## 12.12 编码规范精要

| 建议 | 原因 |
|---|---|
| 不用 `any`，用 `unknown` | 保持类型安全 |
| 优先 `interface`/`type` 命名，复用 | 可读 |
| 函数参数 >3 个，改用对象参数 | 可读、可扩展 |
| 用 `readonly`/`as const` 表达不变性 | 减少意外修改 |
| 联合类型 + 可辨识字段建模状态 | 消灭非法状态 |
| `switch` 做穷尽检查 | 新增成员不遗漏 |
| 系统边界做运行时校验 | 类型不是运行时保障 |
| 命名：类型 `PascalCase`，变量/函数 `camelCase`，常量 `UPPER_SNAKE` | 统一风格 |
| 不用 `I` 前缀（`IUser`）、不用 `Enum` 后缀 | TS 社区习惯 |
| 避免过度抽象与类型体操 | 可维护优先 |

<a id="ch12-s13"></a>

## 本章小结

- 脚本标准化：`dev / build / typecheck / lint / test / check`
- ESLint（typescript-eslint）+ Prettier/Biome；务必开启 `no-floating-promises`
- Vitest 测试，Agent 用假 LLM 脚本化测试
- 打包器多不做类型检查，CI 里必须有 `tsc --noEmit`
- 老项目渐进迁移，用 `@ts-expect-error` 管理遗留问题

<a id="ch12-s14"></a>

## 练习

1. 创建一个新项目，配好 `tsconfig`、ESLint、Vitest 与 `npm run check`。
2. 故意写一个"浮动 Promise"，看 ESLint 如何报错。
3. 为一个 `retry()` 函数写 3 个 Vitest 用例（成功、重试后成功、最终失败），用 `vi.fn` 模拟失败。

---

<a id="ch13"></a>

# 第 13 章　综合实战：用 TypeScript 写一个 Tool-calling Agent

把前面所有知识串起来：**可辨识联合、泛型、zod、async、错误处理、可测试性**，从零实现一个最小但结构完整的 Agent。

> 为了让代码**无需 API Key 就能运行**，我们会用一个"假 LLM"（脚本化的 mock）。最后一节说明如何替换成真实模型。

<a id="ch13-s01"></a>

## 13.1 Agent 是什么（极简模型）

Agent 的核心循环只有四步：

```
┌─────────────────────────────────────────────┐
│ 1. 把对话历史 + 工具列表发给模型               │
│ 2. 模型返回：文本回答  OR  工具调用请求          │
│ 3. 若是工具调用 → 本地执行工具 → 把结果加入历史  │
│ 4. 回到 1，直到模型给出最终回答 或 达到最大步数   │
└─────────────────────────────────────────────┘
```

这就是 **ReAct / tool-calling loop**。所有 Agent 框架（LangGraph、OpenAI Agents SDK、Claude Agent SDK……）都是在这个循环上叠加：记忆、规划、多 Agent、护栏、可观测性。

<a id="ch13-s02"></a>

## 13.2 第一步：设计数据模型（类型先行）

```ts
import { z } from "zod";

// ---------- 消息 ----------
type ToolCall = { id: string; name: string; arguments: unknown };

type Message =
  | { role: "system"; content: string }
  | { role: "user"; content: string }
  | { role: "assistant"; content: string; toolCalls?: ToolCall[] }
  | { role: "tool"; toolCallId: string; name: string; content: string };

// ---------- 模型的一次返回 ----------
type ModelResponse =
  | { type: "text"; content: string }
  | { type: "tool_calls"; calls: ToolCall[] };

// ---------- LLM 抽象：只依赖接口，方便替换与测试 ----------
interface LLM {
  complete(
    messages: readonly Message[],
    tools: readonly ToolDescriptor[],
    opts?: { signal?: AbortSignal },
  ): Promise<ModelResponse>;
}

// 给模型看的工具描述（JSON Schema）
interface ToolDescriptor {
  name: string;
  description: string;
  parameters: unknown;
}
```

要点：

- 消息是**可辨识联合**，`switch (m.role)` 就能精确收窄
- 模型返回也是可辨识联合，强迫我们处理"文本"和"工具调用"两种情况
- `LLM` 是接口：**依赖倒置**，业务代码不绑定具体厂商

<a id="ch13-s03"></a>

## 13.3 第二步：定义"工具"（泛型 + zod）

目标：**一份 zod schema 同时产出 TS 类型、运行时校验、给模型的 JSON Schema**。

```ts
interface Tool<TArgs extends z.ZodType = z.ZodType> {
  name: string;
  description: string;
  schema: TArgs;
  run(args: z.infer<TArgs>, ctx: { signal?: AbortSignal }): Promise<string>;
}

// 辅助函数：让 TS 从 schema 自动推断 run 的参数类型
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
  async run({ a, b, op }) {            // 参数自动推断为 { a: number; b: number; op: "add" | ... }
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
  schema: z.object({ city: z.string().describe("城市名") }),
  async run({ city }) {
    return JSON.stringify({ city, temp: 26, desc: "晴" });
  },
});
```

**工具注册表**：用 `Map` 存放，把"带具体类型的工具"统一当作 `Tool` 存储：

```ts
class ToolRegistry {
  private tools = new Map<string, Tool>();

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

<a id="ch13-s04"></a>

## 13.4 第三步：安全地执行工具

核心原则：**工具调用来自不可信的 LLM，必须校验；工具失败要变成"给模型看的文本"，而不是让整个 Agent 崩溃。**

```ts
async function executeTool(
  registry: ToolRegistry,
  call: ToolCall,
  signal?: AbortSignal,
): Promise<string> {
  const tool = registry.get(call.name);
  if (!tool) return `错误：不存在名为 ${call.name} 的工具`;

  const parsed = tool.schema.safeParse(call.arguments);
  if (!parsed.success) {
    const detail = parsed.error.issues.map((i) => `${i.path.join(".") || "(root)"}: ${i.message}`).join("; ");
    return `错误：参数不合法 —— ${detail}`;      // 反馈给模型，让它自行修正
  }

  try {
    return await tool.run(parsed.data, { signal });
  } catch (e) {
    if (signal?.aborted) throw e;                // 用户取消：向上传播，不当作工具错误
    return `错误：工具执行失败 —— ${e instanceof Error ? e.message : String(e)}`;
  }
}
```

<a id="ch13-s05"></a>

## 13.5 第四步：Agent 主循环

```ts
interface AgentOptions {
  llm: LLM;
  registry: ToolRegistry;
  systemPrompt?: string;
  maxSteps?: number;
  onEvent?: (e: AgentEvent) => void;
}

// 事件流：用可辨识联合描述 Agent 过程中的各类事件，方便 UI/日志/测试订阅
type AgentEvent =
  | { type: "model_response"; step: number; response: ModelResponse }
  | { type: "tool_start"; call: ToolCall }
  | { type: "tool_end"; call: ToolCall; output: string };

type AgentResult =
  | { status: "done"; answer: string; messages: Message[] }
  | { status: "max_steps"; messages: Message[] };

async function runAgent(
  userInput: string,
  opts: AgentOptions,
  signal?: AbortSignal,
): Promise<AgentResult> {
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
      case "text": {
        messages.push({ role: "assistant", content: response.content });
        return { status: "done", answer: response.content, messages };
      }
      case "tool_calls": {
        messages.push({ role: "assistant", content: "", toolCalls: response.calls });

        // 同一轮的多个工具调用并行执行
        const outputs = await Promise.all(
          response.calls.map(async (call) => {
            onEvent?.({ type: "tool_start", call });
            const output = await executeTool(registry, call, signal);
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

  return { status: "max_steps", messages };    // 防止无限循环烧钱
}
```

几个值得学习的细节：

| 设计 | 作用 |
|---|---|
| `maxSteps` 上限 | 防止模型陷入死循环 |
| `signal` 贯穿始终 | 支持用户随时取消 |
| 工具错误转成文本返回 | 模型可以自我修正，而不是整个流程崩溃 |
| `Promise.all` 并行工具 | 模型一次请求多个调用时提速 |
| `onEvent` 回调 | 解耦"过程"与"展示"，便于做流式 UI、日志、测试 |
| 完整返回 `messages` | 便于持久化会话、继续对话 |
| `switch` 无 `default` | 配合 `switch-exhaustiveness-check`，新增响应类型会被编译器提醒 |

<a id="ch13-s06"></a>

## 13.6 第五步：写一个 Mock LLM，让它跑起来

```ts
// 脚本化的假模型：按顺序返回预设响应
class ScriptedLLM implements LLM {
  private i = 0;
  constructor(private script: ((messages: readonly Message[]) => ModelResponse)[]) {}

  async complete(messages: readonly Message[]): Promise<ModelResponse> {
    const next = this.script[this.i++];
    if (!next) throw new Error("脚本已耗尽");
    return next(messages);
  }
}

const llm = new ScriptedLLM([
  // 第 1 轮：模型决定调用两个工具
  () => ({
    type: "tool_calls",
    calls: [
      { id: "c1", name: "get_weather", arguments: { city: "深圳" } },
      { id: "c2", name: "calculator", arguments: { a: 6, b: 7, op: "mul" } },
    ],
  }),
  // 第 2 轮：看到工具结果后给出最终回答
  (messages) => {
    const toolOutputs = messages.filter((m) => m.role === "tool").map((m) => m.content);
    return { type: "text", content: `汇总：${toolOutputs.join(" | ")}` };
  },
]);

const registry = new ToolRegistry().register(calculator, getWeather);

const result = await runAgent("深圳天气如何？顺便算 6×7", {
  llm,
  registry,
  onEvent: (e) => console.log(e.type),
});

if (result.status === "done") console.log(result.answer);
```

<a id="ch13-s07"></a>

## 13.7 第六步：写测试验证行为

```ts
import { it, expect } from "vitest";

it("参数不合法时，错误应该反馈给模型而不是崩溃", async () => {
  const llm = new ScriptedLLM([
    () => ({ type: "tool_calls", calls: [{ id: "c1", name: "calculator", arguments: { a: "x" } }] }),
    (messages) => {
      const last = messages.at(-1);
      return { type: "text", content: last?.role === "tool" ? last.content : "no tool msg" };
    },
  ]);
  const r = await runAgent("算一下", { llm, registry: new ToolRegistry().register(calculator) });
  expect(r.status).toBe("done");
  if (r.status === "done") expect(r.answer).toContain("参数不合法");
});

it("超过最大步数应当终止", async () => {
  const forever = new ScriptedLLM(
    Array.from({ length: 10 }, () => () => ({
      type: "tool_calls" as const,
      calls: [{ id: "x", name: "get_weather", arguments: { city: "A" } }],
    })),
  );
  const r = await runAgent("loop", { llm: forever, registry: new ToolRegistry().register(getWeather), maxSteps: 3 });
  expect(r.status).toBe("max_steps");
});
```

<a id="ch13-s08"></a>

## 13.8 接入真实模型

只需实现 `LLM` 接口，业务代码一行不用改。以兼容 OpenAI 风格接口为例（示意，非完整）：

```ts
class OpenAICompatibleLLM implements LLM {
  constructor(
    private baseUrl: string,
    private apiKey: string,
    private model: string,
  ) {}

  async complete(messages: readonly Message[], tools: readonly ToolDescriptor[], opts?: { signal?: AbortSignal }): Promise<ModelResponse> {
    const res = await fetch(`${this.baseUrl}/chat/completions`, {
      method: "POST",
      headers: { "Content-Type": "application/json", Authorization: `Bearer ${this.apiKey}` },
      signal: opts?.signal,
      body: JSON.stringify({
        model: this.model,
        messages: messages.map(toWireMessage),
        tools: tools.map((t) => ({ type: "function", function: t })),
      }),
    });
    if (!res.ok) throw new Error(`LLM HTTP ${res.status}`);
    const data: unknown = await res.json();
    return parseWireResponse(data);    // 用 zod 校验并转换为 ModelResponse
  }
}
declare function toWireMessage(m: Message): unknown;
declare function parseWireResponse(data: unknown): ModelResponse;
```

不同厂商的消息格式、工具调用字段略有差异，适配逻辑都集中在这一个类里，这正是"面向接口编程"的收益。

<a id="ch13-s09"></a>

## 13.9 还能怎么扩展（学习路线）

| 方向 | 要点 | 涉及的 TS 知识 |
|---|---|---|
| **流式输出** | 模型 token 边生成边展示 | `AsyncIterable`、`async function*`（第 10 章） |
| **记忆** | 对话压缩、向量检索 | 泛型仓储接口 |
| **多 Agent** | Agent 之间传消息、子 Agent 当作工具 | 递归类型、泛型 |
| **MCP Server/Client** | 用标准协议暴露/接入工具 | 官方 `@modelcontextprotocol/sdk` + zod |
| **护栏与权限** | 工具调用前需用户确认 | 可辨识联合描述审批状态 |
| **可观测性** | 记录每步耗时、token、成本 | 事件流 + 中间件模式 |
| **持久化与恢复** | 会话存储、断点续跑 | 序列化友好的数据类型 |

<a id="ch13-s10"></a>

## 13.10 本章回顾：每个知识点用在了哪

| 知识点 | 用在 |
|---|---|
| 可辨识联合 | `Message`、`ModelResponse`、`AgentEvent`、`AgentResult` |
| 泛型 + 约束 | `Tool<TArgs>`、`defineTool` |
| `z.infer` | 工具参数类型自动推断 |
| 接口与依赖倒置 | `LLM` 接口，便于 mock 与替换 |
| 类 | `ToolRegistry`、`ScriptedLLM` |
| async / Promise.all | 并行执行工具 |
| AbortSignal | 取消与超时 |
| 错误处理 | 工具错误转文本返回，不崩溃 |
| 运行时校验 | 校验 LLM 给出的工具参数 |

<a id="ch13-s11"></a>

## 练习

1. 给 `runAgent` 增加**工具调用审批**：对标记 `dangerous: true` 的工具，需要调用方提供 `approve(call)` 回调返回 `true` 才执行。
2. 给 `executeTool` 加**超时**（用 `AbortSignal.timeout` 合并用户的 signal）。
3. 把 `runAgent` 改造成 `async function*`，每个 `AgentEvent` 通过 `yield` 流式输出。
4. 实现一个 `search` 工具，真实调用某个 HTTP API，并用 zod 校验其返回值。

---

<a id="ch14"></a>

# 附录

<a id="ch14-s01"></a>

## 附录 A　Python → TypeScript 对照速查

给有 Python 背景的读者。

### A.1 基础语法

| Python | TypeScript |
|---|---|
| `x: int = 1` | `const x: number = 1` |
| `list[int]` | `number[]` |
| `dict[str, int]` | `Record<string, number>` 或 `Map<string, number>` |
| `tuple[str, int]` | `[string, number]` |
| `set[int]` | `Set<number>` |
| `Optional[str]` / `str \| None` | `string \| undefined`（或 `string \| null`） |
| `Union[int, str]` | `number \| string` |
| `Literal["a", "b"]` | `"a" \| "b"` |
| `Any` | `any`（尽量用 `unknown`） |
| `Callable[[int], str]` | `(x: int) => string` 写作 `(x: number) => string` |
| `TypeVar("T")` | `<T>` |
| `Protocol` | `interface`（结构化类型天然支持） |
| `TypedDict` | `interface` / `type` |
| `@dataclass` | `interface` + 对象字面量，或 `class` + 参数属性 |
| `Enum` | 联合字面量 + `as const` |
| `None` | `null` / `undefined` |
| `NoReturn` | `never` |

### A.2 常用操作

| Python | TypeScript |
|---|---|
| `f"hi {name}"` | `` `hi ${name}` `` |
| `len(xs)` | `xs.length` |
| `xs.append(1)` | `xs.push(1)` |
| `[x*2 for x in xs]` | `xs.map(x => x * 2)` |
| `[x for x in xs if x > 0]` | `xs.filter(x => x > 0)` |
| `sum(xs)` | `xs.reduce((a, b) => a + b, 0)` |
| `x in d`（字典） | `"key" in obj` 或 `map.has(key)` |
| `d.get(k, default)` | `obj[k] ?? default` |
| `{**a, **b}` | `{ ...a, ...b }` |
| `a, b = b, a` | `[a, b] = [b, a]` |
| `for k, v in d.items()` | `for (const [k, v] of Object.entries(obj))` |
| `enumerate(xs)` | `xs.entries()` / `xs.map((x, i) => ...)` |
| `zip(a, b)` | `a.map((x, i) => [x, b[i]])` |
| `x if cond else y` | `cond ? x : y` |
| `is None` | `=== undefined` / `=== null` |
| `with open(...)` | `try/finally`，或 `using`（TS 5.2+ 显式资源管理） |
| `async def` / `await` | `async function` / `await` |
| `asyncio.gather(*tasks)` | `Promise.all(tasks)` |
| `raise ValueError("x")` | `throw new Error("x")` |
| `try/except E as e` | `try/catch (e)`，e 为 `unknown` |
| `import json; json.loads(s)` | `JSON.parse(s)`（返回 any，务必校验） |
| `pydantic.BaseModel` | `zod` schema + `z.infer` |
| `pytest` | `vitest` |
| `pip` / `venv` | `npm`/`pnpm` + `node_modules` |
| `__init__.py` 包 | `index.ts` 再导出 |

### A.3 思维差异

1. **Python 的类型提示不强制，TS 的类型检查是编译期强制的**（但同样运行时不存在）
2. **TS 是结构化类型**，Python 的 `Protocol` 才有类似效果
3. **JS 的 `==`、`this`、`undefined/null` 双空值、隐式转换**是 Python 里没有的坑
4. **TS 的数字只有 `number`**，没有 `int/float` 之分
5. **对象即字典**：JS 对象既是"实例"也是"字典"，`Map` 才是严格的键值表
6. **字符串、数组、对象的比较**：`[] === []` 为 `false`（引用比较），没有 Python 那样的结构相等

<a id="ch14-s02"></a>

## 附录 B　TypeScript 速查表

### B.1 类型语法

```ts
// 原始
let a: string, b: number, c: boolean, d: bigint, e: symbol, f: null, g: undefined;

// 数组、元组
let xs: number[];  let ys: Array<string>;  let t: [string, number];  let ro: readonly number[];

// 对象
let o: { a: number; b?: string; readonly c: boolean };
let dict: Record<string, number>;   let idx: { [k: string]: number };

// 函数
let fn: (a: number, b?: string, ...rest: boolean[]) => void;

// 联合 / 交叉 / 字面量
let u: string | number;  let i: A & B;  let lit: "x" | 1 | true;

// 泛型
function f<T extends object, K extends keyof T = keyof T>(x: T, k: K): T[K] { return x[k]; }

// 类型运算
type A1 = keyof T;   type A2 = typeof value;   type A3 = T[K];
type A4 = T extends U ? X : Y;   type A5 = { [K in keyof T]: T[K] };
type A6 = `prefix-${string}`;     type A7 = T extends (infer R)[] ? R : never;
```

### B.2 常用内置工具类型

| 类型 | 说明 |
|---|---|
| `Partial<T>` / `Required<T>` / `Readonly<T>` | 全部可选 / 必选 / 只读 |
| `Pick<T, K>` / `Omit<T, K>` | 选取 / 排除键 |
| `Record<K, V>` | 键值对象 |
| `Exclude<U, X>` / `Extract<U, X>` / `NonNullable<T>` | 联合类型过滤 |
| `ReturnType<F>` / `Parameters<F>` | 函数返回值 / 参数 |
| `Awaited<T>` | 解包 Promise |
| `InstanceType<C>` / `ConstructorParameters<C>` | 类相关 |
| `NoInfer<T>` | 阻止推断 |

### B.3 收窄手段

`typeof` · `instanceof` · `in` · `===` · 真值 · 可辨识字段 · `x is T` · `asserts x is T` · `Array.isArray`

### B.4 选择指南

| 需求 | 用什么 |
|---|---|
| 描述对象形状 | `interface` 或 `type` |
| 联合、元组、条件类型 | `type` |
| 外部数据（不知道类型） | `unknown` + zod 校验 |
| 状态机 / 消息类型 | 可辨识联合 |
| 固定的几个取值 | 字面量联合 + `as const` |
| 保持输入输出类型关联 | 泛型 |
| 区分相同底层类型的 ID | 品牌类型 |
| 既检查又保留精确类型 | `satisfies` |
| 异步 | `async/await` + `Promise.all` |
| 取消、超时 | `AbortSignal` |

<a id="ch14-s03"></a>

## 附录 C　常见编译错误速查

| 错误码 | 信息（简化） | 原因与对策 |
|---|---|---|
| TS2322 | Type 'X' is not assignable to type 'Y' | 类型不匹配。检查赋值两边；看是否缺少收窄 |
| TS2345 | Argument of type 'X' is not assignable to parameter of type 'Y' | 传参类型不对 |
| TS2339 | Property 'p' does not exist on type 'T' | 属性不存在：拼写错、联合类型未收窄、类型定义缺失 |
| TS2532 / TS18048 | Object is possibly 'undefined' | 对可能为空的值直接访问；用 `?.`、`??` 或先判断 |
| TS2531 / TS18047 | Object is possibly 'null' | 同上 |
| TS7006 | Parameter 'x' implicitly has an 'any' type | 参数缺类型标注 |
| TS7053 | Element implicitly has an 'any' type because expression of type 'string' can't be used to index type | 用 `string` 索引了没有索引签名的对象；用 `keyof T` 或 `Record` |
| TS2304 | Cannot find name 'X' | 没导入、没声明；缺少 `@types/node` 或 `lib` 配置 |
| TS2307 | Cannot find module 'x' | 路径错误；缺少类型包；NodeNext 下相对路径缺 `.js` |
| TS2554 | Expected N arguments, but got M | 参数个数不对 |
| TS2741 | Property 'p' is missing in type | 对象缺少必填属性 |
| TS2353 | Object literal may only specify known properties | 对象字面量里多余的属性（拼写错？） |
| TS2564 | Property has no initializer and is not definitely assigned | 类属性未初始化 |
| TS2367 | This comparison appears to be unintentional | 比较的两个类型没有交集，通常是逻辑错误 |
| TS2488 / TS2495 | Type must have a '[Symbol.iterator]()' | 对非可迭代类型用了展开或 for-of |
| TS2589 | Type instantiation is excessively deep | 类型递归太深，需简化 |
| TS1259 / TS1192 | can only be default-imported using 'esModuleInterop' | 开启 `esModuleInterop` |
| TS5097 / TS2835 | An import path can only end with a '.ts' extension / need explicit file extensions | ESM 下相对导入需写 `.js` |

### 读报错的技巧

1. **从最后一行往上读**：TS 的长错误信息，最后一行通常是根因
2. 看到 `Type 'X' is not assignable to type 'Y'`，在编辑器里悬停两边的类型，对比差异
3. 复杂泛型报错，先把类型提取成有名字的中间类型，逐步缩小范围
4. 实在无法解决：用 `// @ts-expect-error 原因` 临时标注，并记下 TODO，**不要随手 `as any`**

<a id="ch14-s04"></a>

## 附录 D　部分练习参考思路

> 先自己做，再对照。思路比代码重要。

### 第 2 章练习 1

```ts
function safeParseInt(input: unknown): number | null {
  if (typeof input !== "string") return null;
  if (!/^-?\d+$/.test(input.trim())) return null;
  return Number.parseInt(input, 10);
}
```

### 第 5 章练习 2

```ts
function isNonEmptyArray<T>(x: T[]): x is [T, ...T[]] {
  return x.length > 0;
}
```

### 第 6 章练习 1

```ts
function groupBy<T, K extends string>(arr: T[], key: (x: T) => K): Record<K, T[]> {
  const out = {} as Record<K, T[]>;
  for (const item of arr) {
    const k = key(item);
    (out[k] ??= []).push(item);
  }
  return out;
}
```

### 第 8 章练习

```ts
type MyPick<T, K extends keyof T> = { [P in K]: T[P] };
type MyOmit<T, K extends keyof T> = MyPick<T, Exclude<keyof T, K>>;

type DeepReadonly<T> = T extends (...args: any[]) => any
  ? T
  : T extends object
    ? { readonly [K in keyof T]: DeepReadonly<T[K]> }
    : T;

type Last<T extends unknown[]> = T extends [...unknown[], infer L] ? L : never;

type CamelCase<S extends string> = S extends `${infer H}_${infer T}`
  ? `${H}${Capitalize<CamelCase<T>>}`
  : S;
```

### 第 10 章练习 1

```ts
function timeout<T>(p: Promise<T>, ms: number): Promise<T> {
  return new Promise<T>((resolve, reject) => {
    const timer = setTimeout(() => reject(new Error(`timeout after ${ms}ms`)), ms);
    p.then(resolve, reject).finally(() => clearTimeout(timer));   // 别忘了清理定时器
  });
}
```

### 第 10 章练习 2

```ts
async function* chunk<T>(src: AsyncIterable<T>, size: number): AsyncGenerator<T[]> {
  let buf: T[] = [];
  for await (const x of src) {
    buf.push(x);
    if (buf.length >= size) {
      yield buf;
      buf = [];
    }
  }
  if (buf.length > 0) yield buf;   // 不要丢掉最后不足一批的数据
}
```

<a id="ch14-s05"></a>

## 附录 E　推荐学习资源

| 资源 | 说明 |
|---|---|
| TypeScript 官方文档（typescriptlang.org/docs） | 权威，Handbook 一定要通读 |
| TypeScript Playground（typescriptlang.org/play） | 在线编写 + 查看编译结果 + 分享链接 |
| 《Effective TypeScript》（Dan Vanderkam） | 62 条具体建议，进阶必读 |
| type-challenges（GitHub） | 类型体操题库，由易到难 |
| Total TypeScript（Matt Pocock） | 系统的进阶教程，免费部分质量很高 |
| TypeScript 源码 `lib.*.d.ts` | 看内置类型如何实现，是最好的类型学习材料 |

<a id="ch14-s06"></a>

## 学习检查清单

读完全书后，对照看自己能否做到：

- [ ] 能解释 TS 类型为什么在运行时不存在，以及这意味着什么
- [ ] 能为一个真实 API 的请求/响应建模，并用 zod 校验
- [ ] 能用可辨识联合 + `never` 穷尽检查设计状态机
- [ ] 能写出带约束的泛型函数，并解释每个类型参数
- [ ] 能读懂 `Partial<Pick<T, K>>`、`ReturnType<typeof fn>`、简单的条件类型
- [ ] 能配置 strict 的 `tsconfig`，并说明各选项含义
- [ ] 能正确处理并发、取消、超时、重试
- [ ] 能独立搭建一个带测试与 lint 的 TS 项目
- [ ] 能写出一个结构完整的 tool-calling Agent
