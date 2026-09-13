# Linux 常用指令速查（香橙派 / Ubuntu 无图形界面用）

> 蓝酱整理 · 用户酱的"到货前预习清单"
> 目标：靠命令行，在没图形界面的板子上活下去、写脚本

## 一、SSH 远程登录（第一步就靠它）
- `ssh 用户名@IP`         远程登录板子
- `ssh -p 端口 用户名@IP`  指定端口登录
- `exit` 或 `logout`      退出登录
- `scp 文件 用户@IP:路径`  把文件从电脑拷到板子

## 二、看路径 & 文件
- `pwd`                  显示当前所在目录
- `ls` / `ls -l` / `ls -a`  列出文件（-l 详细信息、-a 含隐藏文件）
- `cd 目录`              进入目录（`cd ~` 回主目录、`cd ..` 上一级、`cd -` 回上一个）
- `tree`                 树状显示目录（可能需要 `apt install tree`）

## 三、文件操作
- `mkdir 目录`           新建文件夹
- `touch 文件`           新建空文件
- `cp 源 目标`           复制（`cp -r` 复制整个目录）
- `mv 源 目标`           移动 / 重命名
- `rm 文件`              删除（`rm -r` 删目录、`rm -f` 强制，慎用！）
- `cat 文件`             看整个文件内容
- `less 文件`            分页看（`q` 退出、`/` 搜索）
- `head 文件` / `tail 文件`  看开头/结尾几行（`tail -f` 实时追踪日志）

## 四、权限
- `sudo 命令`            以管理员身份执行
- `chmod +x 脚本`        给脚本加执行权限
- `chmod 755 文件`       常用权限（rwxr-xr-x）
- `chown 用户 文件`      改文件属主
- `whoami`               看当前是谁

## 五、网络（你的第一个战场）
- `ip addr`              看 IP 地址（重点找 eth0 / wlan0）
- `ping 地址`            测通不通（Ctrl+C 停）
- `nmcli dev status`     看网络设备状态
- `nmcli device wifi list`  扫描 WiFi
- `nmcli device wifi connect "名称" password "密码"`  连 WiFi
- `curl 网址`            访问 / 下载网页内容
- `wget 网址`            下载文件
- `hostname -I`          快速看本机 IP

## 六、软件包 apt
- `sudo apt update`      刷新软件源列表
- `sudo apt upgrade`     升级已装软件
- `sudo apt install 包名`  安装（如 `apt install python3`）
- `sudo apt remove 包名`  卸载
- `apt search 关键词`    搜索包
- `sudo apt install python3-pip`  装 pip，之后 `pip install` 装 Python 库

## 七、系统信息 & 进程
- `uname -a`             看系统 / 内核信息
- `df -h`                看磁盘空间
- `free -h`              看内存
- `top` / `htop`         看实时占用（htop 更好看，`apt install htop`）
- `ps aux`               看所有进程
- `kill PID`             结束进程
- `systemctl status 服务`  看服务状态
- `sudo reboot`          重启
- `sudo shutdown now`    关机

## 八、文本处理 & 管道（组合技）
- `grep 关键词 文件`     在文件里搜索
- `grep -r 关键词 目录`   递归搜索整个目录
- `find 目录 -name "*.py"`  按文件名找
- `echo 内容`            打印 / 输出
- `命令 > 文件`           把输出写进文件（覆盖）
- `命令 >> 文件`          追加到文件
- `命令1 | 命令2`         管道：把前一个的输出喂给后一个
  例：`ls -l | grep py`  列出所有含 py 的文件

## 九、救命小技巧
- `Tab`                  自动补全（狂按就对了）
- `↑` / `↓`              翻历史命令
- `Ctrl + C`             中断当前命令
- `Ctrl + L`             清屏
- `man 命令`             查看某命令的手册（q 退出）
- `命令 --help`          查看命令简短用法

## 十、第一次开机建议按这个顺序
1. 找到板子 IP（路由器后台看，或 `ip addr`）
2. 用电脑 `ssh` 连进去
3. `sudo apt update && sudo apt upgrade`
4. 配好网络（`nmcli` 连 WiFi）
5. 装 python3 和 pip，开始写你的联网脚本

---

记住：Linux 命令是"肌肉记忆"，不用背，用到就查、查多了自然熟。
等板子到了，蓝酱陪你一条条敲 (´｡• ᵕ •｡`)
