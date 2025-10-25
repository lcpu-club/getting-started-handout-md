---
icon: fontawesome/brands/linux
---
# Linux 基础知识

很多人是因为迫不得已而使用 Linux :fontawesome-brands-linux:（最常见的是上ICS）。更深入的想一想，还有没有其他使用Linux的原因呢？

对于 Windows 等带图形化界面操作系统，我们所访问的其实是设计者抽象出的交互逻辑。但对于高效的系统，自底向上的彻底理解和掌握是高效使用系统的必备途径。我们得以更深入洞悉文件和文件之间的联系，获得系统更高的主动权。同时，以最小化的人机接口访问能把足够多的资源投入至计算，获得最高的资源利用率。Linux 正是带着这样的思想而诞生的。

因此，学习 Linux，我们需要掌握：

1. 对这一套思想有充分理解、能顺利玩一些玩具
2. 使用现有的工具操作命令行、把他人准备好的软件运行起来
3. 创造新的工具

让我们开始吧！

## Linux 的历史和发展

在20世纪80年代，主要的几个计算机系统有UNIX、DOS和Mac OS。当时，UNIX系统昂贵且无法用于个人计算机，DOS太简陋了且闭源，Mac OS则只用于苹果电脑，计算机科学教育严重受限。为了解决这个问题，Andrew S. Tanenbaum教授设计了MINIX系统，并将其用于教学。然而该系统功能有限且不实用。

当时在芬兰赫尔辛基大学读大二的Linus Torvald在用过MINIX之后，受到了启发。在1991年，他利用UNIX的核心，吸收了MINIX的精华，剔除了不必要的部分，编写了一个新的操作系统内核，并将其命名为Linux 0.01，该内核能够运行在x86架构的个人计算机上。这就是后来各种Linux的雏形。1994年，Linux 1.0版本发布，标志着Linux的正式诞生。

Linux内核采用了GPL协议，这使得任何人都可以自由地使用、修改和分发它。这种开放的理念吸引了大量的开发者和用户，形成了一个庞大的社区。如今，Linux已经与Windows、macOS成三足鼎立之势，成为全球最流行的操作系统之一，更成为了开源技术的象征。

然而，不管怎么讲故事，Linux最终还是一个操作系统，我们还是先要获取一个基于Linux的系统当玩具：不摸一摸，知道用起来舒不舒服，又了解它干啥呢？

## Linux 的发行版

虽然我们经常说"Linux系统"，但是实际上Linux并不是一个操作系统，它仅仅是一个内核（Kernel）。一个完整的操作系统还需要很多其他的组件，例如文件系统、图形界面、应用程序等。为了方便用户使用，很多组织和公司将Linux内核和其他组件打包在一起，形成了一个完整的操作系统，这就是我们常说的Linux发行版（Distribution）。Linux发行版种类繁多，每个发行版都有其独特的特点和适用场景。

| 发行版 | 特点 | 更新频率 | 适用情况 |
|--------|------|----------|----------|
| <img src="../images/ubuntu.svg" alt="Ubuntu" style="height: 20px; vertical-align: middle; margin-right: 8px;"> Ubuntu | 用户友好，社区活跃 | 两年 | Linux新手，桌面用户 |
| <img src="../images/debian.svg" alt="Debian" style="height: 20px; vertical-align: middle; margin-right: 8px;"> Debian | 稳定，软件包丰富 | 两年 | 服务器等生产环境 |
| <img src="../images/fedora.svg" alt="Fedora" style="height: 20px; vertical-align: middle; margin-right: 8px;"> Fedora | 最新技术，社区驱动 | 半年 | 开发者，技术爱好者 |
| <img src="../images/redhat.svg" alt="RHEL" style="height: 20px; vertical-align: middle; margin-right: 8px;"> RHEL | 商业支持，稳定 | 三年 | 企业用户，服务器 |
| <img src="../images/centos.svg" alt="CentOS" style="height: 20px; vertical-align: middle; margin-right: 8px;"> CentOS | RHEL的免费版本 | 死了 | 企业用户，服务器 |
| <img src="../images/archlinux.svg" alt="Arch" style="height: 20px; vertical-align: middle; margin-right: 8px;"> Arch | 滚动更新，极简 | 以天计 | 高级用户，DIY爱好者 |
| <img src="../images/nixos.svg" alt="NixOS" style="height: 20px; vertical-align: middle; margin-right: 8px;"> NixOS | 声明式配置，原子升级 | 以天计 | 高级用户，系统管理员 |
| <img src="../images/rockylinux.svg" alt="Rocky" style="height: 20px; vertical-align: middle; margin-right: 8px;"> Rocky | Cent的复活版本 | 三年 | 企业用户，服务器 |
| <img src="../images/almalinux.png" alt="Alma" style="height: 20px; vertical-align: middle; margin-right: 8px;"> Alma | Cent的复活版本 | 三年 | 企业用户，服务器 |
| <img src="../images/linuxmint.svg" alt="Mint" style="height: 20px; vertical-align: middle; margin-right: 8px;"> Mint | 基于Ubuntu，用户友好 | 两年 | Linux新手，桌面用户 |
| <img src="../images/manjaro.svg" alt="Manjaro" style="height: 20px; vertical-align: middle; margin-right: 8px;"> Manjaro | 基于Arch，用户友好 | 以月计 | Linux新手，桌面用户 |
| <img src="../images/opensuse.svg" alt="openSUSE" style="height: 20px; vertical-align: middle; margin-right: 8px;"> openSUSE | 稳定，企业支持 | 八个月 | 企业用户，服务器 |
| <img src="../images/gentoo.svg" alt="Gentoo" style="height: 20px; vertical-align: middle; margin-right: 8px;"> Gentoo | 源码编译，极致定制 | 以月计 | 高级用户，DIY爱好者 |
| <img src="../images/kalilinux.svg" alt="Kali" style="height: 20px; vertical-align: middle; margin-right: 8px;"> Kali | 安全测试，渗透测试 | 半年 | 网络安全专业人员 |
| <img src="../images/alpinelinux.svg" alt="Alpine" style="height: 20px; vertical-align: middle; margin-right: 8px;"> Alpine | 轻量级，安全 | 以月计 | 容器，嵌入式系统 |
| <img src="../images/linux.svg" alt="统信UOS" style="height: 20px; vertical-align: middle; margin-right: 8px;"> 统信UOS | 中国本土，兼容Windows | 两年 | 政府，企业用户 |

对于什么都不会的小白而言，我们推荐使用Ubuntu、Mint、Manjaro等用户友好的发行版。

## Linux的基本操作

得了，来了啥也别说，先跑个小火车：

```bash
sudo apt update
sudo apt install -y sl
sl
```

执行以上命令，我们就可以看到一个小火车在终端上跑了过去。

`sl`是一个玩具软件，它的全称是Steam Locomotive，是一个在终端上显示火车动画的程序。这不仅能够展示ASCII艺术的魅力，还能矫正打错的`ls`命令（列出目录内容）。

`apt`是Debian及其衍生发行版（如Ubuntu）中用于管理软件包的工具。它可以用来安装、更新和删除软件包。

于是我们就能看到，一个程序就这么跑起来了。

让我们看看上面内容是怎么发生的。我们刚刚输入的命令大概是这样的形式：
```bash
程序 子命令 [选项] [对象]
```

其中，除了子命令，选项和对象都是可选的。我们就用第二个命令来举例说说：apt是程序，install是子命令，-y是选项，sl是对象。

看起来很明确。

那么，我们怎么知道有什么程序，我们又怎么使用它们呢？对于第一个问题，我们可以通过搜索来解决；对于第二个问题，我们可以通过手册来解决。

- `<program> -h`：这是最简单的方式，直接查看程序的帮助信息。通常会列出所有可用的子命令和选项。
- `man <program>`：这是查看程序手册的方式。手册通常会提供更详细的信息，包括子命令的用法、选项的含义等。但是这个手册可能会比较长，需要耐心阅读。
- `tldr <program>`：这个命令会给出一些常用的命令示例和简要说明。当然，`tldr`需要自己安装，当然，安装方法和`sl`类似。

## Linux 的文件系统结构

好的，我们刚刚已经知道怎么使用Linux了。接下来，我们来看看Linux的文件系统。我们不会涉及到任何复杂的概念，只会介绍一些最基本的内容。

思考以下问题：我们刚刚确实输入了`sl`命令，但是我们并没有输入`sl`的路径。那这个`sl`到底在哪里呢？我们怎么知道它在哪里？（其实我们知不知道真无所谓）终端又怎么知道它在哪里？小火车又是怎么跑起来的？

为了解决这一问题，计算机前辈们发挥了聪明才智：只要把所有的东西都归纳为一个概念，那么不就可以方便的管理了吗？于是，文件系统就诞生了。

UNIX和Linux认为，所有的东西都是**文件**。文件系统就是用来管理这些文件的。这时候，我们就可以使用同样的方式来对所有的东西进行操作了。但是我们又出现了其他问题：

1. 文件怎么组织？
2. 文件是谁的？怎么反映不同类型的特性？
3. 文件怎么相互联系？

接下来我们将会逐个回答以上问题。

### 文件的组织

我们在上一章中提到，Windows系统下，物理先于文件存在，所以有盘符一说。但是Linux不这么认为：Linux认为什么都是文件。于是，Linux的根目录`/`就成了所有文件的起点。所有的文件都在这个根目录下。

于是，我们就能够通过目录来解决这一问题。目录是一个特殊的文件，它可以包含其他文件和子目录。我们可以使用`ls`命令来查看当前目录下的文件和子目录，也可以使用`cd`命令来切换目录。

Linux的目录结构和Windows极其相似，只是没有盘符，并且使用`/`作为分隔符，而不是`\`。我们可以使用`/`来表示根目录，使用`..`来表示上一级目录，使用`./`来表示当前目录。需要注意的是，Linux的文件系统是区分大小写的，所以`/home`和`/Home`是两个不同的目录。

Linux还有一个重要的目录：用户的家目录，通常位于`/home/username`。在这个目录下，用户可以存放一些配置文件。我们可以使用`~`来表示当前用户的家目录。我们不推荐把自己的杂七杂八文件放在根目录或者家目录下，而是放在家目录的子目录下。这样可以更好地组织文件，并且避免与系统文件冲突。

我们在上一章提到，处于安全性考虑，对于可执行文件，如果没有提供路径，系统会在一些特定的目录下查找。因此假如有一个可执行文件`hello`，我们应当使用`./hello`来运行它，而不是直接使用`hello`。

如果我们想要在任何地方都能运行这个程序，我们可以把它加入PATH环境变量中去。PATH是一个环境变量，它包含了一些目录的路径，系统会在未提供路径时去这些目录下查找可执行文件。我们可以使用`echo $PATH`命令来查看当前的PATH变量。

### 文件权限和所有权

作为多机系统，Linux 中文件如果对每个访问者都相同，那就没有安全性可言了。Linux 的做法是，抽象出了"用户"这个实体（其实就是在 `/etc/passwd` 里面定义的一行 UID 和用户名的对应而已）。为了方便用户的文件共享，同时抽象出了组（Group）的概念，代表一组互相信任的用户。

对文件的基本操作有读、写、执行三种。我们使用权限位4、2、1来表示这三种操作。每个文件都有三个权限位，分别对应所有者、组和其他用户。我们可以使用`ls -l`命令来查看文件的权限。

举例：750，表示所有者有读、写、执行权限（7=4+2+1），组有读和执行权限（5=4+1），其他用户没有任何权限（0）。

我们可以使用`chmod`命令来修改文件的权限。例如，`chmod 777 file.txt`将会把指定文件的权限设置为777。

!!! tip "提示"
    修改文件权限需要有相应的权限，否则会报错。

!!! warning "警告"
    不要执行这类抽象的命令：`chmod 777 /`，这会导致系统无法正常工作。

所以可执行文件并不是因为这个文件本身有什么特别，而是这个文件被你赋予了可执行的性质。一个简单的文本文件也可以被加上可执行的权限，也可以发挥操作其他文件的作用。

例如，如果你会写 Python 的话，写一个从输入读取 2 个数字，输出他们和的程序，输出结果到控制台。在本地跑起来这个程序之后，把 `#!/usr/bin/env python3` 放在脚本的第一行（这个特殊的一行叫 Shebang）。给这个脚本加上可执行的属性，然后直接运行这个文本！

### 文件的联系

文件间的联系，主要是通过文件系统的链接来实现的。Linux 中有两种链接：硬链接和软链接。硬链接是指在文件系统中，一个文件可以有多个文件名，存在于多个位置，但是文件系统中只有一份文件副本，所有链接均指向这一副本。删除其中一个文件名并不会影响文件内容，只有所有位置下的文件链接均被删除时，此文件副本才会被最终移除。软链接是指一个文件名指向另一个文件名，删除原文件名会影响软链接的有效性。

硬链接和软链接的区别在于，硬链接是文件系统的一个特性，而软链接是文件系统的一个单独的文件。硬链接只能在同一个文件系统下，而软链接可以在不同文件系统下。硬链接不能链接目录，而软链接可以链接目录。

## 常用命令行工具

### 系统命令

- `sudo`命令用于提权。
- `poweroff`和`shutdown`两个命令用于关机。
- `reboot`命令用于重启电脑。
- `whoami`命令用于查看自己是哪个用户。
- `which`命令用于查找可执行文件的路径。
- `ps`命令用于显示当前运行的进程。
- `kill`命令用于终止进程。
- `fg`命令可以将后台运行的任务调回前台，这个命令可以恢复被`Ctrl+Z`挂起的任务。
- `bg`命令可以将任务放到后台运行。

### 文件和目录操作

- `pwd`命令用于显示当前工作目录的绝对路径。
- `ls`命令用于列出目录中的文件和子目录。
- `cd`命令用于切换当前工作目录。
- `mkdir`命令用于创建新目录。
- `touch`命令用于创建新文件或更新现有文件的修改时间。
- `rm`命令用于删除文件或目录。
- `cp`命令用于复制文件或目录。
- `mv`命令用于移动或重命名文件或目录。
- `ln`命令用于创建链接。
- `tar`命令用于打包和解包文件。

### 文本处理工具

- `head`命令用于显示文件的前几行。
- `tail`命令用于显示文件的后几行。
- `cat`命令用于连接文件并打印到标准输出。
- `echo`命令用于在终端输出文本。
- `grep`命令用于在文件中搜索文本模式。
- `sed`命令用于流式文本编辑。
- `awk`命令用于文本处理和数据分析。
- `sort`命令用于对文本行进行排序。
- `uniq`命令用于去除重复行。
- `wc`命令用于统计文件的行数、单词数和字符数。
