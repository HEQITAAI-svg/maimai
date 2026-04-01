# Linux 命令 - 学习路径

> 生成时间: 2026-04-01 17:24

## 📖 学习概览

Linux 是当今最广泛使用的服务器操作系统，掌握 Linux 命令行是每位开发者、运维工程师和系统管理员的必备技能。Linux 命令行提供了强大而灵活的方式来管理文件系统、控制进程、配置网络、处理文本数据等。与图形界面相比，命令行操作效率更高、可脚本化、可远程执行，是自动化运维和 DevOps 实践的基础。从简单的文件操作到复杂的 Shell 脚本编程，Linux 命令体系庞大而系统，通过循序渐进的学习可以逐步掌握这一强大工具。

## 🗺️ 路径总览

| 阶段 | 主题 | 知识点数 |
|------|------|---------|
| 🟢 入门 | 基础操作与文件系统 | 5 |
| 🟡 进阶 | 文本处理与系统管理 | 5 |
| 🔴 高级 | Shell 脚本与网络运维 | 5 |
| 🚀 实战 | 自动化运维与生产实践 | 5 |

## 🟢 阶段1：入门 - 基础操作与文件系统

了解 Linux 基本概念，掌握日常最常用的文件与目录操作命令，能够在终端中完成基本的导航和文件管理任务。

### 1.1 Linux 目录结构与导航

理解 Linux 文件系统层级结构（FHS），掌握 pwd、cd、ls 等导航命令。了解根目录 /、家目录 ~、绝对路径与相对路径的概念，能够在终端中自由切换目录并查看文件列表。

**推荐资源：**

**📄 文章：**

- [Download Linux | Linux.org](https://www.linux.org/pages/download/) - Download Linux Links to popular distribution download pages 24 Popular Linux Distributions Explore different Linux distributions and find the one that fits your needs. Try distrowatch.com for more options.
- [Linux.org](https://www.linux.org/) - Mar 15, 2026 · Friendly Linux Forum The Banana Pi R4 is an open-source smart router. You can use it for networking jobs, as you will tell from the specs on the hardware. Keep in mind that this Single …
- [Forum list - Linux.org](https://www.linux.org/forums/) - Feb 20, 2026 · Server Linux Linux server section HomeLab Self-hosted services, virtualization, NAS, networking, monitoring, and home server infrastructure.
- [What's new - Linux.org](https://www.linux.org/whats-new/) - What's new - Linux.org - Friendly Linux Forum On 03/30/2026, Linux.org was briefly defaced due to a XenForo vulnerability that is also known to have affected other XenForo-based forums. More info here.
- [Linux Beginner Tutorials](https://www.linux.org/forums/linux-beginner-tutorials.123/) - Jul 9, 2013 · On 03/30/2026, Linux.org was briefly defaced due to a XenForo vulnerability that is also known to have affected other XenForo-based forums. More info here.

### 1.2 文件与目录操作

掌握创建、复制、移动、删除文件和目录的核心命令：touch、mkdir、cp、mv、rm、rmdir。理解递归操作（-r）和强制操作（-f）等常用选项，能够安全地进行文件管理操作。

### 1.3 文件内容查看

学习查看文件内容的多种方式：cat 用于输出全部内容，less/more 用于分页查看，head/tail 用于查看文件头尾部分。掌握 tail -f 实时跟踪日志文件的技巧，这是日常运维中非常实用的操作。

### 1.4 获取帮助：man 与 --help

学会使用 man 命令查阅任意命令的官方手册，使用 --help 选项快速获取命令用法摘要。掌握 man 手册的章节结构和搜索技巧，养成查阅文档的好习惯，这是自学 Linux 最重要的能力之一。

**推荐资源：**

**📄 文章：**

- [Download Linux | Linux.org](https://www.linux.org/pages/download/) - Download Linux Links to popular distribution download pages 24 Popular Linux Distributions Explore different Linux distributions and find …
- [Linux.org](https://www.linux.org/) - Mar 15, 2026 · Friendly Linux Forum The Banana Pi R4 is an open-source smart router. You can use it for networking jobs, as you will tell from …
- [Forum list - Linux.org](https://www.linux.org/forums/) - Feb 20, 2026 · Server Linux Linux server section HomeLab Self-hosted services, virtualization, NAS, networking, monitoring, and home server …
- [What's new - Linux.org](https://www.linux.org/whats-new/) - What's new - Linux.org - Friendly Linux Forum On 03/30/2026, Linux.org was briefly defaced due to a XenForo vulnerability that is also known …
- [Linux Beginner Tutorials](https://www.linux.org/forums/linux-beginner-tutorials.123/) - Jul 9, 2013 · On 03/30/2026, Linux.org was briefly defaced due to a XenForo vulnerability that is also known to have affected other XenForo …

### 1.5 用户与权限基础

理解 Linux 用户、用户组和文件权限的基本概念。掌握 chmod 修改权限、chown 修改归属、sudo 提权等命令。理解 rwx 权限位的含义以及数字表示法（如 755、644），为后续系统管理打下基础。

---

## 🟡 阶段2：进阶 - 文本处理与系统管理

掌握强大的文本处理工具和系统管理命令，能够高效地搜索、过滤、分析文本数据，并对进程、磁盘、网络进行基本管理。

### 2.1 文本搜索与过滤：grep 与 find

深入掌握 grep 命令进行文本模式匹配，支持正则表达式、递归搜索、忽略大小写等选项。掌握 find 命令按名称、类型、时间、大小等条件查找文件。这两个命令是 Linux 文本处理和文件定位的核心工具。

### 2.2 文本处理三剑客：sed、awk、cut

学习流编辑器 sed 进行文本替换和删除操作，掌握 awk 进行结构化文本的列提取和统计分析，使用 cut 按分隔符截取字段。这三个工具组合使用可以完成绝大多数文本数据处理任务，是运维和数据处理的利器。

### 2.3 管道与重定向

理解 Linux 哲学中「一切皆文件」和「组合小工具」的思想。掌握管道符 | 将命令串联，使用 >、>>、< 进行输出重定向和输入重定向，以及 2> 重定向错误输出。管道与重定向是发挥 Linux 命令组合威力的关键机制。

### 2.4 进程管理

掌握 ps、top、htop 查看系统进程状态，使用 kill、killall 终止进程，理解前台与后台进程（&、jobs、fg、bg）。了解进程优先级 nice/renice，能够监控系统资源占用情况并对异常进程进行处理。

**推荐资源：**

**💻 GitHub 项目：**

- [ayandavellem/alx-system_engineering-develops ⭐4](https://github.com/ayandavellem/alx-system_engineering-develops) - awk # pattern scanning and processing language basename # strip directory and suffix from filenames bg # resumes suspended jobs without bringing them to the foreground cat # print files cd # change the shell working directory. chmod # change file mode chown # change file owner and group crontab # maintain crontab files curl # transfer a URL cut # remove sections from each line of files date # display or set date and time dig # DNS lookup utility df # report file system disk space usage diff # compare files line by line du # estimate file space usage echo # display a line of text find # search for files in a directory hierarchy fg # resumes suspended jobs and bring them to the foreground grep # print lines matching a pattern kill # send a signal to a process less # read file with pagination ln # create links ls # list directory contents lsb_release # print distribution-specific information lsof # list open files mkdir # create mv # move files nc # arbitrary TCP and UDP connections and listens netstat # print network connections, routing tables, interface statistics... nice # execute a utility with an altered scheduling priority nproc # print the number of processing units available passwd # change user password pgrep # look up processes based on name and other attributes pkill # send signal to processes based on name and other attributes printenv # print all or part of environment pwd # print name of current/working directory top # display Linux processes tr # translate or delete characters ps # report a snapshot of the current processes rm # remove files or directories rmdir # remove directories rsync # remote file copy scp # secure copy (remote file copy program) sed # stream editor for filtering and transforming text sleep # suspend execution for an interval of time sort # sort lines of text file ssh # OpenSSH SSH client (remote login program) ssh-keygen # SSH key generation, management and conversion su # substitute user identity sudo # execute a command as another user tail # output the last part of files tar # manipulate archives files tr # translate or delete characters uname # Print operating system name uniq # report or omit repeated lines uptime # show how long system has been running w # Show who is logged on and what they are doing whereis # locate the binary, source, and manual page files for a command which # locate a command wc # print newline, word, and byte counts for each file xargs # build and execute command lines from standard input | # redirect standard output to another command > # redirect standard output < # redirect standard input & # send process to background

### 2.5 磁盘与存储管理

学习使用 df 查看磁盘空间使用情况，du 统计目录大小，mount/umount 挂载和卸载文件系统。了解 fdisk、lsblk 查看磁盘分区信息。掌握这些命令有助于及时发现磁盘空间不足等常见运维问题。

---

## 🔴 阶段3：高级 - Shell 脚本与网络运维

学习 Shell 脚本编程实现任务自动化，深入掌握网络诊断与远程管理工具，能够编写实用脚本解决复杂的系统管理问题。

### 3.1 Shell 脚本编程基础

学习 Bash 脚本的编写规范，掌握变量、条件判断（if/case）、循环（for/while）、函数等编程结构。理解脚本的执行权限与 shebang 行，学会接收命令行参数（$1、$@）和处理退出状态码，能够编写可复用的自动化脚本。

### 3.2 正则表达式进阶

系统学习正则表达式语法，包括元字符、量词、字符类、分组与捕获、前瞻断言等。区分基础正则（BRE）与扩展正则（ERE）的差异，结合 grep -E、sed、awk 等工具进行复杂模式匹配，大幅提升文本处理能力。

**推荐资源：**

**📄 文章：**

- [Download Linux | Linux.org](https://www.linux.org/pages/download/) - Download Linux Links to popular distribution download pages 24 Popular Linux Distributions Explore different Linux distributions and find the one that fits your needs. Try distrowatch.com for more options.
- [Linux.org](https://www.linux.org/) - Mar 15, 2026 · Friendly Linux Forum The Banana Pi R4 is an open-source smart router. You can use it for networking jobs, as you will tell from the specs on the hardware. Keep in mind that this Single …
- [Forum list - Linux.org](https://www.linux.org/forums/) - Feb 20, 2026 · Server Linux Linux server section HomeLab Self-hosted services, virtualization, NAS, networking, monitoring, and home server infrastructure.
- [What's new - Linux.org](https://www.linux.org/whats-new/) - What's new - Linux.org - Friendly Linux Forum On 03/30/2026, Linux.org was briefly defaced due to a XenForo vulnerability that is also known to have affected other XenForo-based forums. More info here.
- [Linux Beginner Tutorials](https://www.linux.org/forums/linux-beginner-tutorials.123/) - Jul 9, 2013 · On 03/30/2026, Linux.org was briefly defaced due to a XenForo vulnerability that is also known to have affected other XenForo-based forums. More info here.

### 3.3 网络诊断与管理

掌握 ping、traceroute 进行网络连通性测试，使用 netstat/ss 查看网络连接和端口监听状态，curl/wget 进行 HTTP 请求测试，nmap 进行端口扫描。了解 ip、ifconfig 配置网络接口，能够独立诊断和排查常见网络问题。

### 3.4 SSH 远程管理与安全

深入掌握 SSH 远程登录、密钥对认证配置（ssh-keygen、ssh-copy-id）、SSH 配置文件优化。学习 scp、rsync 进行远程文件传输和增量同步，掌握 SSH 隧道与端口转发技术，是远程运维和安全访问的核心技能。

### 3.5 系统日志与监控

了解 Linux 日志体系，掌握 journalctl 查询 systemd 日志，分析 /var/log 下的系统日志文件。学习 vmstat、iostat、sar 等性能监控工具，能够通过日志分析定位系统故障，建立基本的系统健康监控意识。

**推荐资源：**

**📄 文章：**

- [Download Linux | Linux.org](https://www.linux.org/pages/download/) - Download Linux Links to popular distribution download pages 24 Popular Linux Distributions Explore different Linux …
- [Linux.org](https://www.linux.org/) - Mar 15, 2026 · Friendly Linux Forum The Banana Pi R4 is an open-source smart router. You can use it for networking …
- [Forum list - Linux.org](https://www.linux.org/forums/) - Feb 20, 2026 · Server Linux Linux server section HomeLab Self-hosted services, virtualization, NAS, networking, …
- [What's new - Linux.org](https://www.linux.org/whats-new/) - What's new - Linux.org - Friendly Linux Forum On 03/30/2026, Linux.org was briefly defaced due to a XenForo vulnerability …
- [Linux Beginner Tutorials](https://www.linux.org/forums/linux-beginner-tutorials.123/) - Jul 9, 2013 · On 03/30/2026, Linux.org was briefly defaced due to a XenForo vulnerability that is also known to have …

---

## 🚀 阶段4：实战 - 自动化运维与生产实践

将所学命令和脚本知识应用于真实生产场景，掌握服务管理、定时任务、性能调优等实战技能，具备独立处理复杂运维任务的能力。

### 4.1 Systemd 服务管理

掌握使用 systemctl 管理系统服务的启动、停止、重启、开机自启等操作。学习编写自定义 Unit 文件将应用注册为系统服务，理解服务依赖关系和目标（target）概念，能够在生产环境中可靠地管理长期运行的服务进程。

### 4.2 定时任务：Cron 与自动化

掌握 crontab 定时任务的语法规则，学会配置各种周期性任务（每分钟、每天、每周等）。了解 anacron 处理系统关机期间错过的任务，结合 Shell 脚本实现日志轮转、数据备份、报告生成等常见自动化运维场景。

### 4.3 性能分析与调优实战

综合运用 top、perf、strace、lsof 等工具进行系统性能瓶颈分析。掌握 ulimit 配置系统资源限制，使用 tcpdump 抓包分析网络问题，通过 /proc 文件系统深入了解内核运行状态，具备在生产环境排查性能问题的实战能力。

**推荐资源：**

**📄 文章：**

- [Download Linux | Linux.org](https://www.linux.org/pages/download/) - Download Linux Links to popular distribution download pages 24 Popular Linux Distributions Explore different Linux distributions and find the one that fits your needs. Try distrowatch.com for more options.
- [Linux.org](https://www.linux.org/) - Mar 15, 2026 · Friendly Linux Forum The Banana Pi R4 is an open-source smart router. You can use it for networking jobs, as you will tell from the specs on the hardware. Keep in mind that this Single …
- [Forum list - Linux.org](https://www.linux.org/forums/) - Feb 20, 2026 · Server Linux Linux server section HomeLab Self-hosted services, virtualization, NAS, networking, monitoring, and home server infrastructure.
- [What's new - Linux.org](https://www.linux.org/whats-new/) - What's new - Linux.org - Friendly Linux Forum On 03/30/2026, Linux.org was briefly defaced due to a XenForo vulnerability that is also known to have affected other XenForo-based forums. More info here.
- [Linux Beginner Tutorials](https://www.linux.org/forums/linux-beginner-tutorials.123/) - Jul 9, 2013 · On 03/30/2026, Linux.org was briefly defaced due to a XenForo vulnerability that is also known to have affected other XenForo-based forums. More info here.

### 4.4 Shell 脚本实战项目

通过完整项目巩固脚本技能：编写系统巡检脚本（CPU、内存、磁盘告警）、日志分析脚本（统计错误频率、提取关键信息）、自动化部署脚本（代码拉取、服务重启、健康检查）。注重脚本的健壮性、错误处理和可维护性。

**推荐资源：**

**📄 文章：**

- [bash - What are the special dollar sign shell variables ... - Stack ...](https://stackoverflow.com/questions/5163144/what-are-the-special-dollar-sign-shell-variables) - Sep 14, 2012 · In Bash, there appear to be several variables which hold special, consistently-meaning values. For instance, ./myprogram &; echo $! will return the PID of the process which …
- [bash - What is the purpose of "&&" in a shell command? - Stack Overflow](https://stackoverflow.com/questions/4510640/what-is-the-purpose-of-in-a-shell-command) - Oct 27, 2021 · Furthermore, you also have which is the logical or, and also which is just a separator which doesn't care what happend to the command before.
- [How do AND and OR operators work in Bash? - Stack Overflow](https://stackoverflow.com/questions/14836768/how-do-and-and-or-operators-work-in-bash) - How do AND and OR operators work in Bash? Ask Question Asked 13 years, 1 month ago Modified 2 years, 10 months ago
- [What's the difference between <<, <<< and < < in bash?](https://askubuntu.com/questions/678915/whats-the-difference-between-and-in-bash) - Sep 27, 2015 · What's the difference between <<, <<< and < < in bash? Here document << is known as here-document structure. You let the program know what will be the ending text, and whenever that …
- [What does $# mean in bash? - Ask Ubuntu](https://askubuntu.com/questions/939620/what-does-mean-in-bash) - Jul 25, 2017 · Furthermore, when you use bash -c, behavior is different than if you run an executable shell script, because in the latter case the argument with index 0 is the shell command used to invoke it.

### 4.5 容器与云环境中的 Linux 命令

了解在 Docker 容器和 Kubernetes Pod 中使用 Linux 命令的场景与差异，掌握 docker exec 进入容器调试、kubectl exec 进入 Pod 排障的技巧。理解云服务器（AWS/阿里云）环境下的 Linux 运维特点，将命令技能延伸到现代云原生运维场景。

---

> 本学习路径由 AI 自动生成，资源链接来自互联网搜索，请注意甄别内容质量。
