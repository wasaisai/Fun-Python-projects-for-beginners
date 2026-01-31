# 🧮 简易计算器项目（Python）

这是一个**从零开始、逐步演进**的 Python 学习项目。项目目标不是只做出一个“能算”的计算器，而是通过它**系统性地学习 Python 程序设计、命令行工具、GUI 以及程序结构设计**。

本 README 总结了：

* 项目做了什么
* 为什么要这样设计
* 每一步你学到了哪些核心知识点

---

## 📌 项目目标

实现一个支持 **命令行（CLI）和图形界面（GUI）** 的简易计算器，并具备：

* CLI / GUI 两种运行模式
* 程序启动时可选择模式
* 支持命令行参数（如 `--cli 4 + 5`）
* GUI 内部可切换界面（不销毁窗口）
* 清晰、可扩展的程序结构


---

## 🗂 项目整体结构（推荐）

```text
calculator/
│
├── main.py              # 程序入口，负责模式选择与调度
├── calc.py              # 计算逻辑（与界面无关）
├── gui.py               # GUI 相关代码（tkinter）
├── mode.py              # gui、cli模式相关代码
├── cli.py               # CLI 运行相关
├── utilies.py           # 解析命令行参数等函数
├── mode.txt             # 记录上次运行模式（自动生成）
└── README.md            # 项目说明文档
```

> 计算逻辑、界面、入口 **彼此解耦**，这是非常重要的设计原则。

---

## 🧠 核心设计思想

### 1️⃣ 程序入口只做“选择”，不做“具体实现”

```python
if __name__ == "__main__":
    main()
```

* `main()` 决定 **运行哪种模式**
* CLI / GUI 的具体逻辑放在独立函数中

👉 这是所有专业程序的基本结构。

---

### 2️⃣ CLI 与 GUI 共用同一套计算逻辑

```text
用户输入
   ↓
calculate_expression(expr)
   ↓
返回结果
```

* **计算逻辑不依赖 input / tkinter**
* CLI 和 GUI 都只是“调用者”

👉 这让代码更好测、更好改。

---

## ⌨️ 命令行（CLI）模式设计

### 基本交互模型

```text
while True:
    获取输入
    判断是否退出
    计算并输出结果
```

### 学到的知识点

* `while True` 循环
* `break` 退出循环
* `input()` 获取用户输入
* 字符串处理（`strip()`）
* 函数封装（`run_cli()`）

---

## 🪟 GUI（tkinter）模式设计

### tkinter 的基本结构

```python
root = tk.Tk()        # 创建主窗口
...
root.mainloop()       # 进入事件循环
```

### 核心认知

* `root` 是一个 **窗口对象**，不是系统关键字
* tkinter 是 **事件驱动模型**
* `mainloop()` 会阻塞程序，直到窗口关闭

---

## 🔄 GUI 内部切换（Frame 视图切换）

### 设计思路

```text
root（窗口）
 ├── gui_frame
 └── cli_frame
```

* 窗口始终不变
* 通过 `Frame.tkraise()` 切换界面

### 学到的知识点

* `Frame` 的作用
* 视图切换（View Switching）
* 不使用 `destroy()` 的界面切换方式

---

## 🚀 启动参数设计（sys.argv）

### 支持的用法

```bash
python main.py --cli 4 + 5
python main.py --gui
```

### 关键认知

```python
sys.argv == [
    'main.py', '--cli', '4', '+', '5'
]
```

* 命令行参数按**空格拆分**
* 表达式需要用：

```python
expr = " ".join(sys.argv[2:])
```

### 学到的知识点

* `sys.argv`
* 参数解析
* 一次性 CLI vs 交互式 CLI
* `return` 控制程序流程

---

## 💾 记住上次运行模式（文件持久化）

### 思路

* 使用一个简单文本文件：`mode.txt`
* 内容只保存：`cli` 或 `gui`

### 学到的知识点

* 文件读写（`open`）
* `try / except FileNotFoundError`
* 程序状态持久化

---

## 🧩 关键 Python 语法总结

### 条件表达式（三元表达式）

```python
mode = "cli" if choice == "1" else "gui"
```

等价于：

```python
if choice == "1":
    mode = "cli"
else:
    mode = "gui"
```

---

### 程序流程控制

* `break`：退出循环
* `return`：退出函数（非常重要）
* GUI 中避免 `while` 阻塞

---

## 🎯 这个项目真正训练的能力

✔ 把“想法”拆成函数
✔ 设计清晰的程序入口
✔ 理解 GUI 与 CLI 的本质差异
✔ 学会**控制程序生命周期**
✔ 为后续大型项目打基础

> 这已经不是“练语法”，而是**在学如何写程序**。

---

## 🔜 可以继续扩展的方向

* 使用 `argparse` 做专业命令行工具
* 给 GUI 增加布局和样式
* 打包成 `.exe`
* 加历史记录 / 错误提示
* 抽象成插件式计算器

---

## 🧠 最后一句话

> **这个简易计算器不是终点，
> 它是你从“写代码”走向“设计程序”的起点。**

