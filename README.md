## 2025

### [Keepalived for SWDL & Burn-in](https://github.com/Charles-Miao/DevOps/tree/master/2025/Keepalived_for_SWDL&Burn-in)

#### 背景：
- 22个老化架，每个老化架88个老化位，总共1936个老化位，1936个老化位都需要透过PXE服务下载和安装Windows系统
- 因为网络带宽的问题，有将这22个老化架分为3个子网，每个子网使用1台服务器，3台用，1台备，总共4台服务器
- 每台服务器安装各自的DHCP服务，WDS服务，当某个服务器故障时，需要手动切换备用服务器，并设定相关服务

#### 高可用解决建议：
- Copilot & Kimi：虚拟化+负载均衡器（HAProxy、Nginx等）；故障监控脚本+自动切换脚本
- ChartGPT & Doubao：[方案1.md](https://github.com/Charles-Miao/DevOps/tree/master/2025/Keepalived_for_SWDL&Burn-in/方案1.md)
- Gemini：[方案2.md](https://github.com/Charles-Miao/DevOps/tree/master/2025/Keepalived_for_SWDL&Burn-in/方案2.md)
- Claude：[方案3.md](https://github.com/Charles-Miao/DevOps/tree/master/2025/Keepalived_for_SWDL&Burn-in/方案3.md)

#### SWDL高可用测试：

- DHCP负载均衡，测试OK
- WDS两台都有配置，测试OK
- DFS同步log文件夹，测试FAIL，文件权限没有同步（在测试环境中，将文件夹设定为Everyone群组可写可读，可以解决此问题）
- 其他文件5分钟同步一次，测试OK

#### 监控 DFS 复制：

- 可以通过 DFS 管理控制台 来监控复制组的健康状态，查看复制是否正常进行。
- 使用 事件查看器 检查与 DFS 相关的日志，诊断复制问题。

#### 常见故障排除：

- 复制延迟：检查网络带宽、文件大小、复制调度设置，确保网络连接畅通。
- 冲突和数据不一致：检查是否有文件冲突，使用 冲突和删除文件夹 功能来处理文件冲突。
- 复制错误：通过事件查看器查看 DFS 复制相关的错误事件，根据错误代码进行问题诊断。

### [Gitea+LFS](https://github.com/Charles-Miao/DevOps/tree/master/2025/Gitea+LFS)

- 项目由来：使用SVN管理测试程式变更，无法处理2GB以上的文件。故而引入自建Git服务器+LFS（Large File Storage）
- 详细参见：[Gitea+LFS.md](https://github.com/Charles-Miao/DevOps/tree/master/2025/Gitea+LFS/Gitea+LFS.md)

### [Zabbix_Agent](https://github.com/Charles-Miao/DevOps/tree/master/2025/Zabbix_Agent)

- 流程图：[Flowchart](https://github.com/Charles-Miao/DevOps/blob/master/2025/Zabbix_Agent/flowchart.md)
- 使用[syncFileServer](https://github.com/Charles-Miao/Batch-in-Action/tree/master/2025/SyncFileServer)中的批处理脚本，同步文件服务器上的文件到备份服务器
- 使用[Zabbix_Agent](https://github.com/Charles-Miao/DevOps/tree/master/2025/Zabbix_Agent)中的python脚本和Zabbix工具，监控同步结果
- IT监控平台Zabbix添加Sync Files模板，此模板添加了一个Sync Files监控项，以及一个触发器（同步失败则触发）
- 主机添加Sync Files模板
- IT维护Email媒介：SMTP服务器和发送邮件的电子邮件
- IT添加SWDL群组和用户，并添加Email报警媒介
- 添加一个触发器动作，当文件同步异常时透过Email发送给SWDL群组

## 2020

### [Zabbix](https://github.com/Charles-Miao/DevOps/tree/master/2020/Zabbix/Ver2.0)

- [Zabbix in Action](https://charles-miao.github.io/tags/Zabbix/)
- 使用Zabbix采集数据，并异常报警
- 维护界面使用Zabbix自带web界面进行维护
- 使用Grafana实现监视仪表板
- 使用Windows NLB实现2层服务器自动切换
- 透过ILO、IPMI等接口实现服务器远端控制