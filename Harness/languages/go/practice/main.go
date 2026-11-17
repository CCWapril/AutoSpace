// main.go
package main

import (
	"fmt"
	"strconv"
	"os"
	"errors"
	"sync"
	"time"
	"context"
)

var a int
var s string
var s0 = "hello"
const pi = 3.141592

const (
	Read = iota // 枚举值，从0开始
	Write
	Execute
)

func divmod(a, b int) (q, r int, err error) {
	if b == 0 {
		return 0, 0, fmt.Errorf("division by zero")
	}
	return a / b, a % b, nil
}

func inc(p *int) { *p++ }

type Rect struct { W, H float64 } // 数据定义,字段首字母大写表示对包外可见
func (r Rect) Area() float64 { return r.W * r.H } // 值接收
type Counter struct { n int }
func (c *Counter) Inc() { c.n++ } // 指针接收
func (c Counter) IncBad() { c.n++ }

type Animal struct { Name string }
func (a Animal) Speak() string { return a.Name + " makes a sound" }
type Dog struct { 
	Animal // 嵌入字段，Dog 自动获得 Animal 的字段与方法
	Bread string
}

type Shape interface { Area() float64 } // 接口定义，隐式，不用声明

type MyErr struct{}
func (*MyErr) Error() string { return "x" }
func mayFail() error {
    var p *MyErr // 值为 nil 的指针
	if p == nil {
          return nil     // 返回真正的 nil 接口
      }
    return p     // 接口的类型部分是 *MyErr，不为空
}

var ErrNotFound = errors.New("not found") // 创建哨兵错误

type QueryError struct {
    Key string
    Err error
}

func (e *QueryError) Error() string {
    return "query " + e.Key + ": " + e.Err.Error()
}
func (e *QueryError) Unwrap() error { return e.Err }

// 模拟耗时任务：返回一个 channel，500ms 后送出结果；ctx 被取消则提前退出
func doWork(ctx context.Context) <-chan string {
	out := make(chan string, 1) // 带缓冲，避免调用方放弃接收时 goroutine 卡住泄漏
	go func() {
		select {
		case <-time.After(500 * time.Millisecond):
			out <- "work finished"
		case <-ctx.Done():
		}
	}()
	return out
}

// 入口函数，在main包里运行main程序
func main() {
	fmt.Println("一、基本语法")
	fmt.Println("--------------------------------")
	// 1. 变量、常量
	fmt.Println("1.变量/常量")
	fmt.Println("Hello, Go!")
	b := 10 // 短声明，仅限函数内
	fmt.Println(a, s, s0, len(s0), b, pi, Read, Write, Execute)
	fmt.Println("--------------------------------")

	// 2. 控制流
	fmt.Println("2.控制流")
	for i := 0; i < 5; i++ {fmt.Println(i)}
	for i, v := range []int{7,8} {fmt.Println(i, v)}
	for i := range 3 {fmt.Println(i)}
	// strconv.Atoi 将字符串转为整数，分号后是判断条件，err为nil表示没有错误
	if v, err := strconv.Atoi("42"); err != nil {
		fmt.Println(err)
	} else {
		fmt.Println(v)
	}
	fmt.Println("--------------------------------")

	// 3. 函数
	fmt.Println("3.函数")
	fmt.Println(divmod(7, 2))
	fmt.Println("--------------------------------")

	// 4. defer 延迟执行
	fmt.Println("4.defer")
	f, err := os.Open("example.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer f.Close()
	fmt.Println("--------------------------------")

	// 5. 数组
	fmt.Println("5.数组")
	c := []int{1, 2, 3}
	fmt.Println(c)
	fmt.Println(c[1:])
	fmt.Println(append(c[:2], 4)) // append 修改了 c 的数据，但追加没触发扩容，容量不足时会分配新数组并拷贝旧数据
	// 已知大小时用 make([]T, 0, n) 预分配容量，避免重复扩容，可以用.Clone或者copy副本
	m := map[string]int{"a":1, "b":2}
	fmt.Println(m)
	m["c"] = 3
	fmt.Println(m)
	fmt.Println(m["d"])
	delete(m, "a")
	fmt.Println(m)
	fmt.Println("--------------------------------")

	// 6. 指针
	fmt.Println("6.指针")
	x := 10
	p := &x
	fmt.Println(p,*p)
	inc(p)
	fmt.Println(x, p, *p) // 11 11，inc 通过指针修改了 x
	fmt.Println("--------------------------------")

	fmt.Println("二、类型系统")
	fmt.Println("--------------------------------")
	fmt.Println("1.结构体struct")
	r := Rect{W: 3, H: 4}   // 或者 Rect{3, 4}
    fmt.Println(r.W, r.H)   // 3 4
	fmt.Println(r.Area())
	var cnt Counter
	cnt.IncBad()
	fmt.Println(cnt.n)
	cnt.Inc()
	fmt.Println(cnt.n)
	fmt.Println("--------------------------------")

	fmt.Println("2.组合代替继承")
	// 用embedding实现代码复用
	d := Dog{Animal{"Rex"}, "Lab"}
	fmt.Println(d, d.Speak(), d.Name)
	fmt.Println("--------------------------------")

	fmt.Println("3.interface")
	var shape Shape = Rect{3, 4}
	fmt.Println(shape, shape.Area())
	// 空接口any interface{} 可以保存任意值
	switch v := interface{}(x).(type) {
	case int:
		fmt.Println("int", v)
	case string:
		fmt.Println("string", v)
	default:
		fmt.Println("unknown type")
	}
	// 接口值为nil的陷阱:"动态类型 + 动态值"，都为空是接口才等于nil
	fmt.Println(mayFail() == nil)
	fmt.Println("--------------------------------")

	fmt.Println("4.错误处理")
	data, error := os.ReadFile("conf.json")
	if error != nil {
    	fmt.Errorf("read conf: %w", error) // %w 包装，保留错误链
		fmt.Println(data, error)
	}
	error0 := fmt.Errorf("handler: %w", &QueryError{Key: "k1", Err: ErrNotFound})
	var qe *QueryError
	fmt.Println(errors.Is(error0, ErrNotFound), errors.As(error0, &qe), qe.Key, qe.Err)
	fmt.Println("--------------------------------")

	fmt.Println("三、并发*")
	fmt.Println("--------------------------------")

	fmt.Println("1. goroutine")
	var wg sync.WaitGroup
	wg.Add(1)
	go func() { 
		defer wg.Done()
		fmt.Println("in goroutine") }() // 轻量级协程
	wg.Wait()
	fmt.Println("--------------------------------")

	fmt.Println("2. channel")
	// goroutine 类似python queue 往里放从里取
	ch := make(chan int)
	go func() { ch <- 42 }()
	go func() { ch <- 41 }()
	fmt.Println(<-ch)
	fmt.Println(<-ch)
	fmt.Println("--------------------------------")

	fmt.Println("3. select") // 多路复用，哪个就绪就执行哪个
	select {
	case v := <-ch:
    	fmt.Println("got", v)
	case <-time.After(50 * time.Millisecond):
    	fmt.Println("timeout")
	default: // 非阻塞操作
		fmt.Println("nothing ready")
	}
	fmt.Println("--------------------------------")

	fmt.Println("4.sync包")
	var mu sync.Mutex // 互斥锁，保护共享资源,RWMutex读写锁
	cnt0 := 0
	// var wg sync.WaitGroup // 等待一组 goroutine 结束
	for i := 0; i < 1000; i++ {
    	wg.Add(1)
    	go func() {
        	defer wg.Done()
        	mu.Lock()
        	cnt0++
        	mu.Unlock()
    	}()
	}
	wg.Wait()
	fmt.Println(cnt0) // 1000
	fmt.Println("--------------------------------")

	fmt.Println("5.context")
	ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)
	defer cancel() // 确保在函数退出时取消上下文,释放资源

	select {
		case <-ctx.Done():
			fmt.Println(ctx.Err()) // context deadline exceeded
		case <-time.After(1 * time.Second):
			fmt.Println("done")
		case res := <-doWork(ctx):
			fmt.Println("result:", res)
	}


}
