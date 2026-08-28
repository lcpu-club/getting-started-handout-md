---
icon: fontawesome/solid/code
---
# Linux 高级知识

!!! note "作者"
    本文作者列表：

    - [wheatfox](https://github.com/enkerewpo) (wheatfox17@icloud.com)

## 进阶使用 Linux

### 终端管理

#### screen

screen 是一个终端复用器（Terminal Multiplexer），它允许你在一个终端内运行多个窗口（window），每个窗口的程序执行都是相互独立的。每当我们运行一次 screen 命令，都会启动一个 screen 会话（session）：

```bash
screen # 什么窗口都不开，显示一个欢迎界面
screen -S <sname> # 创建一个新的名字为 <sname> 的 session
```

接下来我们介绍 screen 的核心功能——窗口管理，首先要介绍其核心快捷键 `Ctrl+A`，在启动 screen 后（无论是否启动了窗口进入终端）：

1. `Ctrl+A d`： 分离当前会话，回到调用 screen 的终端
2. `Ctrl+A ?`： 显示帮助信息，这可以让你快速查阅所有快捷键
3. `Ctrl+A c`： 创建一个新的窗口
4. `Ctrl+A n`： 切换到下一个窗口
5. `Ctrl+A p`： 切换到上一个窗口
6. `Ctrl+A <number>`： 切换到指定编号的窗口
7. `Ctrl+A w`： 显示窗口列表
8. `Ctrl+A k`： 关闭当前窗口
9. `Ctrl+A :`： 进入命令模式
10. `Ctrl+A "`： 显示所有窗口的列表，并可以选择窗口
11. `Ctrl+A \`： 退出并杀死所有窗口
12. `Ctrl+A [` 或 `Ctrl+A ESC`： 进入**复制模式（copy mode）**，如果需要滚动屏幕或选择文本，则必须先进入复制模式。之后可以按 `ESC` 或 `q` 退出复制模式。进入复制模式之后可以通过 vi 风格的导航或方向键导航，到对应位置后，按下 `SPACE`，然后选择区域，再按下 `SPACE` 复制选中的文本，并**自动退出复制模式**。

当我们 detach 一个 screen 会话时，会显示一行（假设会话名为 `test`）：

```bash
[detached from 11647.test]
```

然后回到调用 screen 的终端，此时会话仍然在后台运行，可以通过 `screen -ls` 列出所有会话，然后通过 `screen -r <pid>/<session name>` 重新连接到该会话（根据 -ls 查到的 `pid.session_name` 来确定）。

```bash
screen -ls
screen -r 11647
screen -r 11647.test # pid.session_name 也可以
screen -r test # 如果会话名唯一，可以只用会话名
```

类似 vim 等软件，screen 本身也存在**命令模式（command line mode）**，通过按下 `Ctrl+A :` 进入命令模式，此时界面下面会显示一个冒号，然后可以通过输入命令来管理 screen：

1. `collapse`： 重新排序窗口，并保证新的编号连续
2. `detach`： 分离当前会话，回到调用 screen 的终端（此时 screen 会话仍然在后台运行）
3. `dinfo`： 显示当前会话的信息
4. `help`： 显示帮助信息

更多命令请参考 screen 的 manpage（`man screen`）。

!!! tip "提示"
    1. screen 最常用的一个场景是通过 ssh 连接远程服务器后，通过 screen 创建一个会话，然后在这个会话中运行编译或者机器学习任务，然后通过 screen 的 detach 功能将当前会话分离出来，这样退出 ssh 不会导致任务中断。
    2. screen 有时候也可以作为串口交互软件使用，例如通过 `screen /dev/ttyUSB0 115200` 打开一个波特率为 115200 的串口设备。Linux 下还可以使用 `minicom` 、`picocom` 以及图形化的 `gtkterm` 等软件来作为串口交互软件。

screen 的在线 manpage：[screen(1) — Linux manual page](https://man7.org/linux/man-pages/man1/screen.1.html)

#### tmux

### 系统初始化

#### sysvinit

#### busybox

#### systemd

#### openrc

### 远程连接

#### SSH

#### VNC

#### RDP

### 系统监控

#### ps

#### top

#### htop

#### btop

### tracing

#### strace

#### perf

#### ftrace

#### bpftrace

## Linux 内核初探

### 内核开发流程

### 内核源码树结构与内核编译

### KBUILD 系统

### 内核子系统简介

#### 进程管理

#### 内存管理

#### 文件系统

#### 网络管理

#### 驱动框架

#### 安全机制

### Rust For Linux

!!! note "注意"
    1. Rust-for-Linux 官方网站： <https://rust-for-linux.com>
    2. Rust-for-Linux 内核文档： <https://docs.kernel.org/rust/index.html>

### eBPF

1993 年 McCanne 和 Van Jacobson 在 USENIX 论文[^1]中提出 BSD Packet Filter，使用一套轻量可验证的虚拟机来高效过滤网络包。经典 BPF（cBPF）随后在 Linux 2.6 内核中被引入，用作 tcpdump 与 libpcap 的底层过滤引擎。2014 年，Linux 内核 3.18 替换了旧的 BPF 解释器，引入扩展 BPF（extended BPF，eBPF）虚拟机：增加 64 位寄存器、改进指令集、支持函数调用、提供独立栈空间并具备严格的安全验证。

[^1]: McCanne, Steven and Van Jacobson. “The BSD Packet Filter: A New Architecture for User-level Packet Capture.” USENIX Winter (1993)


!!! note "注意"
    1. eBPF 官方网站： <https://ebpf.io>
    2. eBPF 内核文档： <https://docs.kernel.org/bpf/index.html>

!!! note "注意"
    如果你想知道更多关于 Linux 内核的知识，可以参考 [Linux内核官方文档](https://docs.kernel.org/)。
