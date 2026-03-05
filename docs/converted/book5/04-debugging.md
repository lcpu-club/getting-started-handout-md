---
icon: material/bug-outline
---
# 调试、测试和部署

我们在前面的章节中已经知道，代码中出现错误是难免的事情。无论是语法错误、语义错误，还是不能称得上错误但是不符合预期的行为，我们都需要进行调试和测试来找出问题所在。

一些大公司专门有“测试工程师”这类岗位来负责代码正式上线之前的测试工作，以检查代码的正确性和可靠性；但是对于大多数小型项目而言，这些工作往往是由开发人员自己完成的。在本章节中，我们会介绍一些常用的调试和测试方法，帮助同学们更好地理解和解决代码中的问题。

总得说来，调试和测试就像诊治一个危重病人（值得庆幸的是，这个病人能够复活）一样。此时，我们需要四步走：先救命、再治病、再调养，最后购买医疗保险，然后让他去工作。顺序不要乱，一步都不能少。

## 先救命

最常见的情况是：代码崩溃了，程序完全无法执行。对于 Python 而言，它的报错信息非常详细，通常可以直接定位到出错的行数和错误类型，因此往往只需要根据报错信息进行修复即可；但堆栈深层或异步、多线程场景中依然需要调试器来辅助定位问题。

而对于 C/C++ 这类语言而言，它们是静态的，运行时错误能过编译，而且它们的报错信息通常非常简洁，仅凭报错信息很难定位到具体的错误地点。因此，我们需要使用一些调试工具来帮助我们定位错误。

什么，你问我怎么确定编译错误？我认为编译错误应该由编译器来判断，而不是我们来判断；编译过一次以后，你的代码编辑器应该也能够显示哪里有编译错误！

### 使用调试器

我们在开发的过程中可以使用 VS Code 调试器，但是有时候我们无法获取程序源码。在这种情况下，我建议同学们使用那个最经典的调试工具 `gdb`。它是 GNU 项目的一部分，支持多种编程语言，包括 C、C++、Fortran 等。当然对于一些会读汇编的同学们而言，我觉得可以用 objdump 这类反汇编器来反汇编程序，并对这些汇编代码进行阅读；常见的反汇编器还有著名的 IDA Pro，它是一个商业软件，价格很贵，但是功能绝对对得起它的价格：它甚至能够对反汇编出来的东西进行自动分析！

```bash
objdump -d ./your_program > asm.s
```

当然大多数人是没这个能力也没这个毅力去读汇编的，因此 GDB 最终还是我们最常用的动态调试工具。例如，以下命令可以启动 GDB 并加载程序：

```bash
gdb ./your_program
```

在 GDB 中，我们可以使用以下命令来设置断点、运行程序、查看变量等：

- `break`：设置断点，可以简写为 `b`，例如 `break main` 在 `main` 函数处设置断点。也可以在特定的某一行设置断点，例如 `break 42` 在第 42 行设置断点；也可以利用偏移量来设置断点，例如 `break +10` 在当前行的往后继续数 10 行，在那里设置断点。
- `run`：运行程序。可以简写为 `r`。
- `next`：执行下一行代码，可以简写为 `n`。如果当前行是函数调用，则不会进入函数内部，而是把这个函数视为一个整体往下执行一行。该命令有一个变体 `ni`，它是汇编级别的断点定位，也就是执行下一条汇编指令。
- `step`：也是执行下一行代码，可以简写为 `s`。如果当前行是函数调用，则会进入函数内部，逐行执行函数内部的代码。`si` 是它的变体，表示汇编级别的单步执行。
- `continue`：继续运行直到下一个断点，可以简写为 `c`。
- `print`：打印变量的值，例如 `print variable`，可以简写为 `p variable`。如果变量是一个结构体或类的实例，可以使用 `print variable.field` 来打印某个字段的值。
- `backtrace`：查看函数调用栈，可以简写为 `bt`。这对于定位程序崩溃时的调用路径非常有用。
- `layout`：切换到图形界面模式，可以使用 `layout src` 来显示源代码，使用 `layout asm` 来显示汇编代码。
- `info`：查看程序的状态，例如 `info breakpoints` 查看断点信息，`info registers` 查看寄存器状态，`info locals` 查看局部变量等。
- `watch`：设置观察点，当某个变量的值发生变化时暂停执行，例如 `watch variable`。这对于调试复杂的逻辑错误非常有用。
- `set`：强制设置变量的值，例如 `set variable = value`。这对于调试时修改变量的值非常有用。
- `list`：查看源代码（带行号），可以简写为 `l`。
- `quit`：退出 GDB。

当然，如果想要显示行号的话，我们编译代码的时候需要加上 `-g` 选项，例如：

```bash
gcc -g -o your_program your_program.c
```

也只有加上了 `-g` 选项，GDB 才能够显示源代码和行号，`s` 和 `n` 命令才能够逐行执行源代码，但是 `si` 和 `ni` 命令仍然能够正常执行。

以上命令其实很复杂，需要同学们多加练习才能熟练掌握。这里我推荐一个 GDB 的小练习：CMU ICS Lab2：BombLab。这个练习的目的是让同学们通过 GDB 来调试一个被加密的程序，找到正确的输入来“拆弹”。这个练习非常有趣，而且可以帮助同学们熟悉 GDB 的使用。

当然，GDB 的 TUI 界面还是太老了，我推荐装个插件 `pwndbg`，它可以让 GDB 的 TUI 现代化得多。

### 尸检

有时候程序确实崩了，救不活了，这时候我们需要“死后验尸”，确定程序真正的“死因”。当然，我们在解剖尸体之前，至少得对死因了解个大概，例如是段错误、内存泄漏、未定义行为，还是什么奇奇怪怪的东西。

#### 段错误

段错误可以使用 core dump 来分析。core dump 是程序崩溃时操作系统生成的一个文件，包含了程序的内存状态和寄存器状态等信息。我们可以使用 GDB 来分析 core dump 文件。

`ulimit -c unlimited` 命令可以设置 core dump 文件的大小限制为无限制。然后运行崩溃的程序，等着程序再崩溃一次。然后运行 `gdb ./your_program core`。这会加载 core dump 文件，并且可以使用 `bt` 命令查看函数调用栈，使用 `info locals` 查看局部变量等。

#### 内存泄漏

内存泄漏可以使用 Valgrind 来分析。Valgrind 是一个开源的内存调试工具，可以检测内存泄漏、未初始化内存读取等问题。使用 Valgrind 非常简单，只需要在运行程序时加上 `valgrind` 命令即可，例如：

```bash
valgrind --leak-check=full ./your_program
```

Valgrind 会输出内存泄漏的详细信息，包括泄漏的内存地址、大小、调用栈等信息。我们可以根据这些信息来定位内存泄漏的代码。

Valgrind 跑完以后别急着关，如果是开源项目或者协作项目，把 definitely lost 那行抄下来贴到 issue 上面，省得以后再犯同样的错误。当然，你也需要附上 suppressions 过滤后的结果，避免误报。

#### 未定义行为

越界和未定义行为可以使用 ASan 和 UBSan 来分析。ASan（AddressSanitizer）是一个内存错误检测工具，可以检测越界访问、使用后释放等问题。UBSan（UndefinedBehaviorSanitizer）是一个未定义行为检测工具，可以检测整数溢出、空指针解引用等问题。

我们在编译文件的时候，可以加上 `-fsanitize=address` 和 `-fsanitize=undefined` 选项来启用 ASan 和 UBSan。

## 再治病

有些时候，程序没有崩溃的风险，但它的执行不符合预期且占用了过多的资源。这时候，我们需要进行性能调优和资源使用分析。以下是一些常见的性能问题和资源使用问题，以及相应的分析工具。

### CPU占用过高

这种情况可以使用 perf 来分析问题，由 Linux 内核提供。只需要在运行程序时加上 `perf` 命令即可，例如：

```bash
perf record -g -o perf.data ./your_program && perf report -i perf.data
```

### 内存占用过高

这种情况可以使用 massif 来分析问题，该工具由 Valgrind 提供。例如：

```bash
valgrind --tool=massif --massif-out-file=ms.out ./your_program
```

运行完毕后，可以使用 `ms_print` 命令来查看内存使用情况，例如：

```bash
ms_print massif.out.<pid>
```

### IO卡死

IO 卡死通常是因为程序在等待某个 IO 操作完成，例如网络请求、文件读写等。我们可以使用 iotop 来分析 IO 卡死问题，只需要：

```bash
sudo iotop -o
```

然后盯着它看，找谁疯狂 IO 就可以了。

当然，对于 Node.js 和 Python 服务，可以使用 `--inspect` 模式；然后打开 Chrome 浏览器，输入 `chrome://inspect`，火焰图和前端一样香。

## 再调养

经过以上的两步骤，我们总算是把程序的主要问题解决了个差不多。但是，为了保证程序的稳定性和可靠性，我们还需要进行一些额外的调养工作: 测试。

我们最好是找个地方把需要测试的代码隔离开来，放到一个单独的地方，防止其他代码或者文件影响测试结果；对于服务类型的项目，则更是如此。我们可以使用 tmux、screen 或者 Docker 来隔离测试环境。

### 轻量级隔离：tmux和screen

tmux 和 screen 是两个常用的终端复用工具，可以在一个终端中创建多个会话，方便我们进行隔离测试。使用方法非常简单，只需要在终端中输入 `tmux` 或 `screen` 即可进入一个新的会话。

在 tmux 中，我们可以使用以下命令来创建新的窗口、分割窗口等：

```bash
tmux new-session -s session_name # 创建一个新的会话
tmux ls # 列出所有会话
tmux attach -t session_name # 连接到指定的会话
```

会这三个就行。在 screen 中的相同功能命令是：

```bash
screen -S session_name # 创建一个新的会话
screen -ls # 列出所有会话
screen -r session_name # 连接到指定的会话
```

### 重量级隔离：Docker

docker 和上述两个东西不太一样。上述两个东西只能做到“守护终端”，但是对于环境的变化无能为力。使用 docker 可以做到隔离环境，甚至可以做到“守护进程”，但也复杂得多。

docker 有四个比较重要的概念需要了解：

- **镜像**：镜像是一个只读的模板，包含了运行某个应用程序所需的所有文件和依赖。我们可以从 Docker Hub 等公共仓库中拉取镜像，或者自己构建镜像。
- **容器**：容器是镜像的一个运行实例，它是一个轻量级、可移植且可写的运行环境。我们可以在容器中运行应用程序，并且容器之间相互隔离。
- **仓库**：仓库是镜像的存储位置，可以是公共的也可以是私有的。我们可以将镜像推送到仓库中，或者从仓库中拉取镜像。
- **注册中心**：注册中心是一个集中管理仓库的服务。Docker Hub 是一个公共的注册中心，我们也可以搭建自己的私有注册中心。公司内部一般也有自己的私有注册中心，用来存储公司内部的镜像，如 Harbor 等。

所以实际上，每一个 docker 中都是运行了一个轻量级的小系统，这个系统和宿主机是隔离的，互不影响。这个系统里面可以安装各种各样的软件包和依赖，完全按照我们的需求来配置环境。

#### 简单使用

我们可以使用 Docker 来创建一个隔离的测试环境，例如：

```bash
docker run -it --rm --name <your-container> -v $(pwd):/app -w /app python:3.9 bash
```

以上代码的含义是创建一个 Python 3.9 的 Docker 容器，并将当前目录挂载到容器的 `/app` 目录下，然后进入容器的 bash 终端，其名称为 `<your-container>`。这样，我们就可以在隔离的环境中进行测试了。上述命令中：

- `-i` 表示交互式终端，该参数会保持标准输入流打开，否则 cat 等交互命令无法使用；
- `-t` 表示分配一个伪终端，这样我们就可以在容器中使用终端命令了；
- `--rm` 表示容器退出后自动删除（但不会删除挂载在外面的文件）；
- `--name <your-container>` 表示容器的名称，可以自定义；
- `-v $(pwd):/app` 表示将当前目录挂载到容器的 `/app` 目录下，在 Windows Powershell 中需要使用 `-v ${PWD}:/app`；
- `-w /app` 表示设置容器的工作目录为 `/app`，实际上是设置容器内的 `PWD` 环境变量为 `/app`；若目录不存在会报错。
- `python:3.9` 表示使用 Python 3.9 的官方镜像作为基础镜像，不写默认最新版，**生产环境必须显式指明版本**；
- `bash` 表示进入容器后执行的命令，这里是进入 bash 终端。

当然，上述命令还是太长了，我们往往写成一个脚本来执行，或者利用 `alias` 命令等来充分简化命令。

上述命令中我们创建了一个临时容器，容器退出后会自动删除，适用于临时调试使用。如果我们想要创建一个持久化的容器，可以去掉 `--rm` 参数，适宜长期服务或长期调试使用。

#### 增删改查、启动停止、进入退出

在上述命令创建容器后，会直接进入容器的 bash 终端。希望从容器中离开，可以使用 `Ctrl + P + Q` 组合键，这样可以让容器继续在后台运行。如果直接使用 `exit` 命令或者 `Ctrl + D` 组合键退出容器，则会停止容器的运行。如果在容器中输入 `Ctrl + C`，则会中断当前运行的命令，并向容器发送 SIGINT 信号，**可能**导致容器停止运行，这实际上取决于 PID1 进程对 SIGINT 信号的处理方式。

如想重新进入容器，可以使用 `docker attach <your-container>` 命令，但只能进入正在运行的容器。也可以使用 `docker exec <your-container> <command>` 命令来在容器中执行命令（这也是我们更推荐的方式，而不是每次都 attach），例如：

```bash
docker exec -it <your-container> bash
```

上述命令会在容器中启动一个新的 bash 终端。

在容器外，我们可以用 `docker ps` 命令来查看正在运行的容器，如果在上述命令末尾加上 `-a` 参数，则可以查看所有容器，包括未运行的容器。

可以利用 `docker start` 命令来启动一个已经存在的容器，例如：

```bash
docker start -i <your-container>
```

上述命令中的 `-i` 参数表示进入容器的交互式终端。

这个 start 还可以替代为：

- `docker restart <your-container>`：重启容器；
- `docker stop <your-container>`：停止容器（发送 SIGTERM 信号，优雅关闭进程，10 秒后若进程仍未退出则发送 SIGKILL 信号强制关闭进程）；
- `docker kill <your-container>`：强制终止容器（发送 SIGKILL 信号，强制关闭进程）；
- `docker pause <your-container>`：暂停容器（冻结 cgroup，阻止进程调度）；
- `docker unpause <your-container>`：恢复容器。

如果确实不想要这个容器了，可以使用 `docker rm <your-container>` 命令来删除容器。也可以用 `docker container prune` 命令来删除所有未运行的容器。

### 端口映射

我们也可以让测试代码在 docker 容器里面跑起来以后，再退出来，使用其他代码（例如测试代码）来访问这个容器。此时我们需要再 docker 容器中预留端口，也就是：

```bash
docker run -it --rm -p 8000:8000 -v $(pwd):/app -w /app python:3.9 bash
```

上述命令是做了一个端口映射，我们可以在本地的 8000 端口访问容器中的 8000 端口。解释其参数：

- `-p 8000:8000` 表示将本地的 8000 端口映射到容器的 8000 端口。前面的 8000 是本地端口，后面的 8000 是容器端口。这两个顺序**不可逆**，因为实际操作中映射的端口可能并不相同，例如 `-p 8080:80` 表示将本地的 8080 端口映射到容器的 80 端口，写反了不会报错但会导致无法访问。该操作默认使用 TCP 协议，也可以指定使用 UDP 协议，例如 `-p 8000:8000/udp`。
- 如需一次性映射多个端口，可以多次使用 `-p` 参数，例如 `-p 8000:8000 -p 9000:9000`。

容器间的通信建议自己建立一个 bridge 网络而不是走默认 bridge 网络，具体可以参考 Docker 官方文档。

### 单元测试

单元测试是对代码的最小可测试单元进行验证的过程。它通常是自动化的，可以帮助我们快速发现代码中的问题。Python 和 C/C++ 都有很好的单元测试框架。

对于 Python，我们可以使用 unittest 框架来编写单元测试。以下是一个简单的示例：

```python
import unittest
class TestMyFunction(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(my_function(1, 2), 3)

    def test_case_2(self):
        self.assertRaises(ValueError, my_function, -1, 2)

if __name__ == '__main__':
    unittest.main()
```

在这个示例中，我们定义了一个测试类 `TestMyFunction`，它继承自 `unittest.TestCase`。我们在这个类中定义了两个测试用例，分别测试了 `my_function` 函数的正确性和异常处理。最后，我们使用 `unittest.main()` 来运行所有的测试用例。这是一个非常简单的单元测试示例，实际的单元测试可能会更加复杂，要涉及几乎所有的代码逻辑。因此测试工程师这个职业也不是什么轻松的工作。

在编写测试用例的时候，除了涉及到大多数的常规数据以外，也要尽可能地考虑一些特殊值（例如边界情况等），也需要故意混入一些显然错误的数据来测试程序的健壮性和异常处理能力。

### 集成测试

集成测试则指的是对整个系统进行测试，验证各个模块之间的交互是否正常。集成测试通常是手动进行的，一般是编写一些集成测试代码，然后用这个代码来测试整个系统的功能是否正常。

对于 Python，我们可以使用 pytest 框架来编写集成测试。以下是一个简单的示例：

```python
import pytest
def test_my_function():
    assert my_function(1, 2) == 3
    assert my_function(-1, 2) == 1
    assert my_function(0, 0) == 0
    with pytest.raises(ValueError):
        my_function(-1, -2)
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, 2, 1),
    (0, 0, 0),
])
def test_my_function_parametrized(a, b, expected):
    assert my_function(a, b) == expected
```

对于服务类项目，我们的测试代码可以是自动调用这个服务来做一些事情，看看能不能产生符合预期的结果。比如说，我们可以使用 `requests` 库来发送 HTTP 请求，验证服务的响应是否正确。

## 买保险

大多数时候，我们的程序经过一大堆调试和测试后，已经可以正常运行，并得到了充分的优化。但是为了保证程序确实得到了优化，我们还需要进行一些额外的测试工作。比方说，我们使用 Python 的 pytest-benchmark 装饰器来进行性能测试：

```python
@pytest.mark.benchmark
def test_my_function(benchmark):
    result = benchmark(my_function, *args, **kwargs)
    assert result == expected_result
    return result
```

跑就完了。

对于所有程序，我们都可以使用 hyperfine 来进行性能测试：

```bash
hyperfine 'python old.py' 'python new.py' --warmup 5 --runs 50
```

加上这个选项把东西抄下来：

```text
--export-markdown results.md
```

然后 PR 里面贴出“优化完成”和这张表，老板登时点赞。

## 去工作

### 部署

代码调试完成了，现在该把代码部署到生产环境了。部署代码的方式有很多种，具体取决于项目的类型和规模。对于小型项目，我们可以直接将代码上传到服务器上运行；对于大型项目，我们可以使用 CI/CD 工具来自动化部署流程。

GitHub Actions 是一个常用的 CI/CD 工具，可以帮助我们自动化部署流程。我们可以编写一个 GitHub Actions 工作流文件，定义部署的步骤和条件。例如：

```yaml
name: Deploy
on:
    push:
        branches:
        - main
jobs:
    deploy:
        runs-on: ubuntu-latest
        steps:
        - name: Checkout code
          uses: actions/checkout@v2
        - name: Set up Python
          uses: actions/setup-python@v2
          with:
            python-version: '3.9'
        - name: Install dependencies
          run: |
            python -m pip install --upgrade pip
            pip install -r requirements.txt
        - name: Run tests
          run: pytest
        - name: Deploy to server
          run: |
            scp -r . user@server:/path/to/deploy
            ssh user@server 'cd /path/to/deploy && ./deploy.sh'
```

在这个示例中，我们定义了一个名为 `Deploy` 的工作流，当代码推送到 `main` 分支时触发。工作流包含了几个步骤：检出代码、设置 Python 环境、安装依赖、运行测试和部署到服务器。当然，具体的部署步骤需要根据项目的实际情况进行调整。

除了自动部署以外，CI/CD 工具还可以帮助我们进行代码质量检查、性能测试等工作。我们可以在工作流中添加相应的步骤来实现这些功能。

### 回滚

有时候，部署完成后我们会发现代码出现了问题，导致服务无法正常运行。这时候，我们需要进行回滚操作，将代码恢复到之前的稳定版本。

最简单的回滚方式是使用 Git 的版本控制功能。我们可以使用 `git revert` 命令来撤销最近的提交，或者使用 `git checkout` 命令来切换到之前的某个版本。

有些时候部署的代码并不是直接从 Git 仓库中拉取的，而是经过打包、编译等步骤生成的二进制文件或者 Docker 镜像等。这时候，我们需要使用相应的工具来进行回滚操作。例如，如果我们使用 Docker 来部署服务，我们可以使用 `docker rollback` 命令来回滚到之前的镜像版本，也就是：

```bash
docker service update --image your_image:previous_version your_service
```

这样就可以将服务回滚到之前的版本。
