---
icon: fontawesome/solid/download
---
# Linux 安装和配置

## 安装 Linux 发行版

### CLab

我们在这一讲推荐大家直接去 [CLab](https://clab.pku.edu.cn/) 注册一个账号，根据上面的指南连接到虚拟机。这样，你就可以在不破坏自己的系统的情况下，体验 Linux 的魅力了。

当然，这种情况下，我们还可以顺带着复习一下密钥的相关用法。

### 实机安装

如果我们有一台不怎么重要的机器和一个U盘，可以利用U盘在这台机器上面安装Linux。你可以选择任意的发行版进行安装。

#### Ubuntu

Ubuntu安装过程非常简单，其自动化程度非常高。以下是一个简要步骤：

1. 获取Linux发行版的ISO镜像文件。可以从（[Ubuntu官网](https://ubuntu.com/download)）下载最新版本的Ubuntu ISO镜像。
2. 准备一个U盘，至少8GB容量。将这个镜像文件写入U盘。可以使用工具如Ultra ISO、Rufus（Windows）或Etcher（跨平台）来完成这个操作。
3. 将U盘插入目标机器，重启电脑并进入BIOS设置，将U盘设置为首选启动设备。
4. 保存设置并重启，系统将从U盘启动，进入Ubuntu安装界面，并按照提示进行安装。我们建议选择"安装Ubuntu"选项，并在安装过程中选择"擦除磁盘并安装Ubuntu"选项（注意，这将删除磁盘上的所有数据，请确保备份重要数据）。
5. 安装完成后，重启电脑，拔出U盘，系统将进入Ubuntu桌面环境。

对于硬盘容量较大且熟悉分区的同学，可以使用磁盘分区工具自己划出一个分区，并将Ubuntu安装在这个分区上。这样可以保留原有的操作系统，并在需要时切换到Ubuntu。在这种情况下我们一般使用grub引导程序来管理多系统启动。

#### 其他发行版

如果你对Linux有一定了解，或者想尝试其他发行版，可以选择其他发行版进行安装。对于此类学生，我们非常推荐使用Arch Linux，因为它提供了一个非常灵活和可定制的环境，适合有一定Linux基础的用户。

同时，安装Arch Linux也是一个很好的学习Linux的机会，因为它的安装过程需要用户从头手动配置系统，这样可以更深入地了解Linux的工作原理。

### 使用虚拟机

使用虚拟机也是一个很好的选择。通过虚拟机，我们可以在现有的操作系统上运行Linux或者其它系统，而不需要重新安装或配置硬件。

一般我们使用的虚拟机软件有VirtualBox、VMware等。不同的虚拟机有着不同的特点和使用方法，但是总体而言在虚拟机中安装一个Linux发行版的步骤与在实机上安装类似（只是不需要设置BIOS和U盘启动等了）。

### WSL

WSL是在Windows上使用Linux的最佳方式之一。它允许用户在Windows上运行Linux发行版，并提供了与Linux相似的命令行环境。WSL的安装和配置非常简单，只需要在命令行中运行以下命令即可：

```bash
wsl --install
```

WSL提供了与Linux相似的命令行环境，并且可以直接访问Windows文件系统。例如：

```bash
cd /mnt/c/Users/YourUsername/Documents
```

上述命令会在Linux环境中查看Windows的文档目录。这种跨系统的文件访问方式非常方便，可以让用户在Windows和Linux之间无缝切换。这样，我们就可以在Windows上使用Linux的命令行工具和开发环境了。

## 分区和文件系统

### 分区基础


### 文件系统类型


### 挂载点


## 用户和权限管理

### root权限的配置

root 用户是超级用户，拥有着 Linux 系统内最高的权限，在终端内使用su命令即可以超级用户开启终端，root 用户的权限最高，而其他账户则可能会有以能以超级用户身份执行命令的授权（可以类比 Windows 中的管理员权限），但即使是拥有授权的账户在终端输入的命令也不会以超级用户身份执行，如果需要以超级用户的身份运行则需要在此命令前加 sudo。

第一种情况，如果你所选择的发行版在安装过程中没有设置 root 密码的环节（如 Ubuntu），则新创建的用户会拥有管理员权限，一般不需要使用 root 账户，直接使用 sudo 命令即可。

第二种情况，如果你所选择的发行版在安装过程中已经设置了 root 密码，但是自己的账户并没有管理员权限（如 Debian），为了用起来方便一般会用 root 账户给自己的账户添加管理员权限，具体操作如下（$号后的为输入的命令）：

```bash
yourusername@yourcomputer$ su
root@yourcomputer$ /usr/sbin/usermod -aG sudo yourusername
```

前者表示切换至 root 账户，后者表示为你指定的账户添加管理员权限。有些发行版中 wheel 组表示有 sudo 权限的用户组（例如Arch），也可以用 visudo 编辑 sudo 配置。

### 用户管理命令

- `useradd`：创建新用户
- `usermod`：修改用户属性
- `userdel`：删除用户
- `passwd`：修改密码
- `groups`：查看用户所属组
- `id`：显示用户ID和组ID

### 权限管理

Linux使用数字权限系统：
- 4：读权限
- 2：写权限
- 1：执行权限

权限分为三组：所有者、组、其他用户。例如755表示所有者有读、写、执行权限，组和其他用户有读和执行权限。

## 软件包管理

### APT（Debian/Ubuntu）

APT是Debian及其衍生发行版（如Ubuntu）中用于管理软件包的工具。

#### 更新软件包列表
```bash
sudo apt update
```

#### 升级软件包
```bash
sudo apt upgrade
```

#### 安装软件包
```bash
sudo apt install package-name
```

#### 卸载软件包
```bash
sudo apt remove package-name
```

#### 搜索软件包
```bash
apt search keyword
```

### YUM/DNF（Red Hat系列）

YUM和DNF是Red Hat系列发行版的包管理器。

#### 更新软件包
```bash
sudo yum update
# 或
sudo dnf update
```

#### 安装软件包
```bash
sudo yum install package-name
# 或
sudo dnf install package-name
```

### Pacman（Arch Linux）

Pacman是Arch Linux的包管理器。

#### 更新系统
```bash
sudo pacman -Syu
```

#### 安装软件包
```bash
sudo pacman -S package-name
```

#### 搜索软件包
```bash
pacman -Ss keyword
```

### 软件源配置

如果你的系统在安装的时候已经选择过了国内源则忽略，否则默认源来自于国外。从国外的服务器更新软件包会很慢，可以根据自己系统的版本自行搜索匹配的源并更换。具体参考[北大开源镜像站的帮助文档](https://mirrors.pku.edu.cn/Help)。

!!! note "特别注意"
    我们请尽可能地使用包管理器来安装软件，而不是直接下载二进制文件或源码编译安装。包管理器可以自动处理依赖关系，并且可以方便地进行软件的更新和卸载。如果一定要手动安装软件，请确保你了解该软件的安装过程和依赖关系，并尽可能在虚拟环境或容器中进行测试，以避免对系统造成不必要的影响。

## 进阶：安装 Arch Linux

!!! tip "提示"
    这一部分内容是进阶内容，对于初次接触Linux的同学，我们推荐你先掌握基础知识，之后再尝试从零开始安装 Arch Linux。

熟练掌握Linux的基本操作以后，我们可以自己开一个虚拟机或者实体机器等，逐步地安装Arch Linux，进一步练习Linux的使用，并深化理解Linux系统的相关知识。

### 前置操作

在安装archlinux之前，我们首先要做一些前置的工作。我们需要一个U盘和一个archlinux的iso映像，并使用Rufus等工具将iso映像烧录到U盘中；另一方面，我们在安装整个系统的时候需要保证机器一直联网。

之后，在关机状态下，插上U盘，进入你计算机的BIOS环境，并选择你的启动方式为"从U盘启动"、关闭安全启动、调整启动模式为 UEFI。此三者缺一不可。另外，请确保你的计算机一直有网络连接；如果使用无线网络，务必保证你的无线网络名称和密码均不含特殊字符（如汉字）。

!!! note "注意"
    有少数奇葩的主板里面，安全启动[^1]被设置为开启，却不存在关闭它的选项，但系统主板内置有 Windows 系统的公钥证书签名，使其只能加载 Windows，其它系统（包括 archlinux）一律不予加载。用户不能关闭它，还没法换系统，实在让人无语。如果你正好是这样的电脑，不妨在虚拟机里尝试下 archlinux 吧！

[^1]: 安全启动指的是主板在这种情况下只信任微软签名的bootloader。Arch自带的bootloader没有微软签名，因此会被拒绝执行。

### 开始安装

#### 进入安装环境

在跳出的选项框中，选择第一项，进入安装环境。之后，该安装环境就会自动给你加载一些内容。不需要管这些内容具体是什么，一路确认到命令行界面，此时你的用户是`root@ archiso`，终端是zsh。从这一步开始，到安装完成为止，你的这个U盘就一定要一直插在电脑上。

#### 禁用reflector服务

这个服务主要是用于自行更新mirrorlist的。mirrorlist是软件包管理器 pacman 的软件下载渠道；也许它是一个很好的工具，但是在国内的特殊网络环境下，这个东西反而成了累赘，不妨禁用之。因此，这个东西一定要在联网之前搞。

```bash
systemctl stop reflector.service # 禁用reflector服务
```

#### 联网

我们使用`iwctl`来联网：

```bash
iwctl # 进入交互式命令行
device list # 列出无线网卡设备名，比如无线网卡看到叫 wlan0
station wlan0 scan # 扫描网络
station wlan0 get-networks # 列出所有 wifi 网络
station wlan0 connect wifi-name # 进行连接，注意这里无法输入中文。回车后输入密码即可
exit # 连接成功后退出
```

可以使用`ping`等工具来检查是否联网了。在Linux下`ping`必须按下`Ctrl+C`终止输出。

#### 同步时间

我们使用`timedatectl`来同步系统的时间。这一步是必要的，这是因为 Linux 很多加密校验（HTTPS、GPG）依赖正确时间。如果时间差太多，证书会被判定过期。

```bash
timedatectl set-ntp true
```

#### 检查是不是国内源

```bash
vim /etc/pacman.d/mirrorlist
```

检查有没有熟悉的pku.edu.cn和隔壁镜像。如果没有，说明你的reflector服务禁用晚了，不过并非不能解决，只需要在开头加上相关镜像就行了。不要在这一步添加社区源（例如archlinuxcn）。

#### 分区与格式化

!!! warning "警告"
    这两个操作对数据很危险！不要把含有重要数据的盘当作目标盘。

`lsblk`命令可以帮助我们确定我们要把archlinux安装在哪里。一般有两种硬盘编号，要么是走SATA协议的sdx，其中x是字母；要么是走NVME协议的nvmexn1，其中x是数字。我们可以通过观察磁盘的大小、已存在的分区情况等判断。下文统一使用sda作为磁盘编号，请根据你自己的实际情况更改磁盘编号。

```bash
cfdisk /dev/sda
```

我们要分出三个区：EFI用来启动（如果做双系统时已有一个EFI分区，则无需）；Swap用于临时存储（至少给到你物理内存的60%以上）、不活跃页交换和休眠；文件分区（使用Btrfs文件系统，不需要多个文件分区了）。

先创建Swap分区：选中FreeSpace，再选中操作New，再按回车，这样就能创建一个新的分区了。在按下回车后会提示输入分区大小，我们正常输入就可以了；单位可以自行输入。之后在新创建的分区上选中操作Type并按下回车，选择Linux Swap项目，按下回车以修改分区为swap格式。

再创建一个分区，操作类似之前的，只不过这次需要的分区格式是Linux File System。

最后，应用分区表的修改。选中操作Write，并回车，输入yes,再回车，确认分区操作。

分区完成后，可以再使用`lsblk`命令复查分区情况。

现在，我们需要格式化各种分区。我们假设EFI分区是sda1，Swap分区是sda2，Btrfs分区是sda3。

```bash
mkfs.fat -F32 /dev/sda1
mkswap /dev/sda2
mkfs.btrfs -L myArch /dev/sda3 # -L操作是指定盘符用的
mount -t btrfs -o compress=zstd /dev/sda3 /mnt # 挂载分区
btrfs subvolume create /mnt/@ # 创建 / 目录子卷
btrfs subvolume create /mnt/@home # 创建 /home 目录子卷
umount /mnt # 卸载分区以便于之后的挂载操作
```

#### 挂载分区

挂载分区有顺序性，需要从根目录开始挂载：

```bash
mount -t btrfs -o subvol=/@,compress=zstd /dev/sda3 /mnt # 挂载 / 目录
mkdir /mnt/home # 创建 /home 目录
mount -t btrfs -o subvol=/@home,compress=zstd /dev/sda3 /mnt/home # 挂载 /home 目录
mkdir -p /mnt/boot # 创建 /boot 目录
mount /dev/sda1 /mnt/boot # 挂载 /boot 目录
swapon /dev/sda2 # 挂载交换分区
```

用`df -h`命令和`free -h`来复查挂载情况。

#### 安装系统

现在终于到了最重要的一步：安装系统了。我们使用`pacstrap`来安装最基础的包和功能性软件。

```bash
pacstrap /mnt base base-devel linux linux-firmware btrfs-progs
pacstrap /mnt networkmanager vim sudo zsh zsh-completions # zsh也可以换成bash，但是不建议新手换这个。
```

倘若提示GPG证书错误，用以下命令更新一下密钥环：

```bash
pacman -S archlinux-keyring
```

然后经过一系列安装时信息的刷屏，就安装好了。之后，我们利用`genfstab`命令来根据当前挂载情况生成并写入fstab文件[^2]即可。

```bash
genfstab
```

[^2]: 该文件用来定义磁盘分区。它是 Linux 系统中重要的文件之一。

#### 换根，以及一些基础设置

接下来，我们需要从安装介质中切出，进入新系统的目录下。

```bash
arch-chroot /mnt
```

现在可以发现命令行的提示符颜色和样式发生了改变。我们现在可以设置主机名和时区了：
```bash
vim /etc/hostname
```
输入你喜欢的主机名称，当然这里也不要包含特殊字符以及空格。

下一步，设置`/etc/hosts`：
```bash
vim /etc/hosts
```
保证里面有以下内容：
```bash
127.0.0.1   localhost
::1         localhost
127.0.1.1   myarch.localdomain myarch
```

再下一步，设置时区和硬件时间：
```bash
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
hwclock --systohc
```
这里没有北京，只有上海，所以不要傻傻的找北京了！

使用vim或者nano编辑/etc/locale.gen，去掉 en_US.UTF-8 UTF-8 以及 zh_CN.UTF-8 UTF-8 行前的注释符号，并保存。之后用`locale-gen`命令来生成locale[^3]。

```bash
locale-gen
```

[^3]: 这个文件决定了软件使用的语言、书写习惯、字符集等

下一步运行以下命令来设置默认locale：
```bash
echo 'LANG=en_US.UTF-8'  > /etc/locale.conf
```
我们不建议在这一步设置任何中文的locale，会导致tty乱码。

现在为root用户设置密码：
```bash
passwd root
```
根据提示操作即可。注意输入密码时不会显示，不要以为键盘坏了。

最后，安装CPU微码：
```bash
pacman -S intel-ucode # Intel
pacman -S amd-ucode # AMD
```
CPU微码是厂商发布的CPU补丁，它们在启动早期加载，使用软件来修复硬件缺陷。

#### 作引导

引导是让主板和系统内核沟通的桥梁，系统的启动依赖于引导。

第一步，装包：
```bash
pacman -S grub efibootmgr os-prober
```
os-prober是为了能够引导Windows系列系统而不得不装的一个东西。如果不需要Windows系统，完全可以不安装之。但是，前两个还是要装的。

下一步，把grub安装到EFI分区：
```bash
grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=ARCH
```

然后，对开机指令进行一些微调，以加快速度：
```bash
vim /etc/default/grub
```
主要是对GRUB_CMDLINE_LINUX_DEFAULT进行修改：去掉最后的 quiet 参数（这样可以在启动的时候就把内核日志打出来，便于排错）；把 loglevel 的数值从 3 改成 5，方便排错；加入 nowatchdog 参数，这可以显著提高开关机速度。

如果需要引导Windows系列系统，则不得不添加新的一行：
```bash
GRUB_DISABLE_OS_PROBER=false
```

最后，生成配置文件：
```bash
grub-mkconfig -o /boot/grub/grub.cfg
```

#### 完成基础安装

输入以下命令以完成安装：
```bash
exit # 退回安装环境
umount -R /mnt # 卸载新分区
reboot # 重启
```
计算机关闭后，立刻拔掉U盘，进入引导界面，然后选择archlinux。

登录系统需要输入用户名和密码。在这时，我们还没有创建任何账户，因此只有一个root。输入用户名root，以及你的密码，即可进入系统。

为了保证这玩意能够自动联网，可以使用
```bash
systemctl enable --now NetworkManager # 设置开机自启并立即启动 NetworkManager 服务
nmcli dev wifi list # 显示附近的 Wi-Fi 网络
nmcli dev wifi connect "<Your_Wifi>" password "<your_password>" # 连接指定的无线网络
ping 8.8.8.8 # 测试网络连接
```

最后，安装并运行fastfetch：
```bash
pacman -S fastfetch
fastfetch
```
看着显示出的Arch徽标，我们终于可以长舒一口气：安装Arch Linux的过程终于结束了。当然，这个系统肯定很难日常使用，还需要一些后续配置，例如安装视窗等。之后的各种配置实际上都是在已经有的内容上继续开枝散叶，和现代Windows有显著的不同：现代Windows的视窗实际上已经紧紧地和系统内核绑定在一起了，而Linux的视窗只是个软件罢了！

#### 创建非根用户

根用户的权限太高了，甚至高于系统本身。这导致其自由度太高、安全度太低，几乎毫无容错。因此，有必要创建一个非根用户。

先做一点准备工作：使用vim或者nano编辑一下`~/.bash_profile`文件：
```bash
vim ~/.bash_profile
```
向其中加入以下内容：
```bash
export EDITOR='vim'
```
这样就会显式地制定编辑器为vim，保证部分情况下不会出错。

然后就可以添加用户了：
```bash
useradd -m -G wheel -s /bin/bash myusername
```
你可以把myusername改为你喜欢的名字，但是同样不能包含空格和特殊字符。这个wheel是一个特殊的用户组，可以使用sudo提权。你可以使用以下命令设置新用户的密码：
```bash
passwd myusername
```
再下一步，编辑sudoers文件：
```bash
EDITOR=vim visudo # 这里需要显式的指定编辑器，因为上面的环境变量还未生效
```
找到这一行，把前面的注释符号#去掉：
```bash
#%wheel ALL=(ALL:ALL) ALL
```
保存并退出就可以了。现在你就有了一个非根用户。

#### 开启多个库的支持

编辑这个文件：
```bash
vim /etc/pacman.conf
```
然后去掉`[multilib]`一节中所有内容的注释即可。这样可以开启32位库的支持。

然后在文档结尾处加入下面的文字来添加中国社区源：
```bash
[archlinuxcn]
Server = https://mirrors.ustc.edu.cn/archlinuxcn/$arch # 中国科学技术大学开源镜像站
Server = https://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/$arch # 清华大学开源软件镜像站
Server = https://mirrors.hit.edu.cn/archlinuxcn/$arch # 哈尔滨工业大学开源镜像站
Server = https://repo.huaweicloud.com/archlinuxcn/$arch # 华为开源镜像站
```

保存并退出上述文件，然后使用以下命令刷新数据库并更新系统：
```bash
pacman -Syyu
```

### 配置视窗，以及后续内容

通过以下的命令安装视窗相关的软件包：
```bash
pacman -S plasma-meta konsole dolphin
```
安装完成之后，运行以下命令：
```bash
systemctl enable sddm
```
之后重启电脑就行。输入你新创建的非根用户的密码，然后回车，就可以登录桌面了。

值得注意的是，这时尚未安装任何显卡驱动。如果你在进入桌面环境时遭遇闪退、花屏等异常情况，建议尝试安装相应的显卡驱动。这里我就不提了，感兴趣的同学可以自行查找相关资料进行了解。

之后，可以做一些很好的操作，例如使用`Ctrl+Alt+T`打开Konsole（不是Console，这个是一个终端模拟器）。连接一下网络，然后安装一些基础功能包：
```bash
sudo pacman -S sof-firmware alsa-firmware alsa-ucm-conf # 声音固件
sudo pacman -S ntfs-3g # 使系统可以识别 NTFS 格式的硬盘
sudo pacman -S adobe-source-han-serif-cn-fonts wqy-zenhei # 安装几个开源中文字体。一般装上文泉驿就能解决大多 wine 应用中文方块的问题
sudo pacman -S noto-fonts noto-fonts-cjk noto-fonts-emoji noto-fonts-extra # 安装谷歌开源字体及表情
sudo pacman -S firefox chromium # 安装常用的火狐、chromium 浏览器
sudo pacman -S ark # 压缩软件。在 dolphin 中可用右键解压压缩包
sudo pacman -S packagekit-qt6 packagekit appstream-qt appstream # 确保 Discover（软件中心）可用，需重启
sudo pacman -S gwenview # 图片查看器
sudo pacman -S archlinuxcn-keyring # cn 源中的签名（archlinuxcn-keyring 在 archlinuxcn）
sudo pacman -S yay # yay 命令可以让用户安装 AUR 中的软件（yay 在 archlinuxcn）
```

之后，如同root账户一样，配置其默认编辑器即可。

#### 配置中文环境

首先应当配置系统为中文。打开`System Settings > Language and Regional Settings > Language > Add languages`，找到并加入简体中文，然后拖拽到最上面一位，保存并退出设置。重启电脑就可以生效了。

现在该配置汉语输入法了：
```bash
sudo pacman -S fcitx5-im # 输入法基础包组
sudo pacman -S fcitx5-chinese-addons # 官方中文输入引擎
sudo pacman -S fcitx5-anthy # 日文输入引擎
sudo pacman -S fcitx5-pinyin-moegirl # 萌娘百科词库。二刺猿必备（archlinuxcn）
sudo pacman -S fcitx5-material-color # 输入法主题
```
下一步，创建以下文件，然后编辑这个文件：
```bash
vim ~/.config/environment.d/im.conf
```
向文件中加入这些内容并保存退出，以修正输入法的一些错误：
```bash
# fix fcitx problem
GTK_IM_MODULE=fcitx
QT_IM_MODULE=fcitx
XMODIFIERS=@im=fcitx
SDL_IM_MODULE=fcitx
GLFW_IM_MODULE=ibus
```
之后，打开系统设置-区域和语言，找到输入法一项，运行fcitx。之后，点击添加输入法，找到拼音输入（或者你喜欢的输入），将其添加为拼音输入法。

现在重启电脑就可以输入中文了。

### 总结

上面的过程就是从头安装ArchLinux的全过程了。实际上我们可以看到，上述过程总体上大概可以分为四部分：

1. 准备工作：准备好安装介质（这里是U盘）、改BIOS设置、联网等。
2. U盘根阶段：从U盘启动，进入Linux的安装环境；准备硬盘（分区、格式化、挂载等）；安装基础系统。
3. 机器根阶段：从U盘`chroot`到新的系统，安装剩余的软件包，配置系统（主机名、时区、locale等）；做启动引导。
4. 后续的各种配置。

实际上几乎所有的系统安装过程都可以大致分为这四个部分。只不过不同的系统在细节上有不同，而且许多系统会把这些步骤都封装好，用户只需要简单地点击几下就可以完成安装。