## 2025

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