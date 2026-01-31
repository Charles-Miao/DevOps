## 2026
### Log服务器优化建议
#### 问题：
- 目前架构无法实现log服务器的高可用
- 单台服务器的磁盘读性能告警，磁盘的读请求响应时间持续偏高

#### [解决方案](https://www.doubao.com/thread/wda4f36da18105c87)：
- 两个ftp节点（配置相同）+DFS+Nginx

### Burn-in网络架构优化
#### 背景：
- 原规划Burn-in网络架构每条线3个子网，每个子网搭配1台服务器，并配1台备用服务器，3条线total需要12台服务器，每个子网设计最大agent 700台，相对于H客户1000台的agent有充分的冗余，但是online服务器故障，需要手动切换备份服务器
- 备份服务器*3是由收购W公司提供，已经使用5年以上，故障率高，同时这些机器都是W自产机器，无有效售后
- IT发现电源/内存/SSD故障，购买备品更换，只有1台可以正常开机，另外服务器存在电源持续故障，BIOS持续故障导致无法启动等问题，如果进一步分析，可能需要花费更多的备品费用，但是并不会解决故障率高的问题

#### 优化方案：
- L1保留原有方案，3个子网分别控制7，7，6个老化架，每个子网agent数量分别为616，616，528，唯一维修ok的服务器作为备份服务器
- L2使用2+1的方案，2台服务器做负载均衡，1台作为备份，total控制13个老化架，平均每台负责的agent为1144/2=572
- L3使用2+1的方案，2台服务器做负载均衡，1台作为备份，total控制56个老化架，平均每台负责的agent为1400/2=700

#### 实施细则：
- 网络中继（同一台服务器给不同子网分配DHCP），设定ok
- DHCP负载均衡，log DFS同步，设定ok
- 备份服务器设定，DFS设定ok，DHCP故障转移IT不建议2+1的架构，建议备份服务器DHCP配置但不启用，出现异常时IT手动启用备份服务器

#### 改善优点：
- L2和L3，online服务器故障，2台服务器可以自动故障转移，如果长期无法恢复，备份服务器的DHCP需要IT手动加入负载均衡
- L1是集中老化架上架机台，load会集中在某一台服务器上，但是L2和L3虽然集中老化架上架机台，但是服务器会交替使用，分担了服务器的load，有效提高了服务器的瞬时使用率，相对于L1即稳定，又高效

## 2025
### IMGit优化建议
#### 背景：
- IMGit每年需要发费900,000+RMB软件授权费用

#### 架构对比：
| A客户 |  B客户 |
| :---: |  :---: |
| 使用IMGit软件download image |  使用Windows自带服务，并使用DISM download image |
| 每条线只有2台Image服务器 |  每条线有5台Image服务器 |
| 所有服务器全部放主机房，汇聚交换机的带宽只有20Gib |  所有服务器全部放产线，每台服务器的带宽都是20Gib |
| Edge交换机的主干只有2Gib |  Edge交换机全部为光纤连接，带宽有10Gib |

#### 优化建议：
- 将A客户中的2台WDS服务器扩容至7TB，升级为Image服务器，这样每条线total有4台Image服务器，费用大约30000RMB/线
- 将Image服务器拿到产线机柜，可以突破汇聚交换机的20Gib带宽限制，费用0
- 升级Edge交换机为光纤传输，费用大约72000RMB/线

#### 预估费用：
- 30000RMB/线 + 72000RMB/线 = 102000RMB/线

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

### [本地化部署Gitea+LFS实现测试程序版本控制](https://github.com/Charles-Miao/DevOps/tree/master/2025/Gitea+LFS)

- 项目由来：使用SVN管理测试程式变更，无法处理2GB以上的文件。故而引入自建Git服务器+LFS（Large File Storage）
- 详细参见：[Gitea+LFS.md](https://github.com/Charles-Miao/DevOps/tree/master/2025/Gitea+LFS/Gitea+LFS.md)

### [Zabbix文件同步监控](https://github.com/Charles-Miao/DevOps/tree/master/2025/Zabbix_Agent)

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