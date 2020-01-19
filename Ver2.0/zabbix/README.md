Server端安装配置
---

[Ubuntu Zabbix服务端配置](https://my.oschina.net/zhangyangyang/blog/841043)

[安装异常: The frontend does not match Zabbix database ](https://blog.csdn.net/purplegalaxy/article/details/37819899)

```shell
# 时间同步
# crontab -l
00 00 * * * /usr/sbin/ntpdate -u 195.13.1.153
```

```shell
#agent安装和配置
sudo apt-get install zabbix-agent
sudo apt-get install zabbix-get
#安装时间同步工具
sudo apt-get install ntpdate
#安装发送mail工具
sudo apt-get install bsd-mailx
sudo apt-get install mailx
sudo apt-get install s-nail
sudo apt-get install mailutils
#配置发送mail工具
sudo vim /etc/s-nail.rc
#配置Zabbix发送mail脚本：/usr/lib/zabbix/alertscripts/send_mail.sh
echo "$3" | mail -s "$2" "$1"
```

[监控模板](https://github.com/Charles-Miao/Server-Monitoring/tree/master/Ver2.0/zabbix/template)
---

HP服务器透过iLO口snmp协议进行硬件监控

- 系统需要开启SNMP服务，并在security选项卡中开放public只读功能
- 需要安装iLO 3/4 Channel Interface Driver
- 需要安装iLO 3/4 Management Controller Driver Package
- 需要安装HPE Insight Management Agents
- 需要安装Smart Array SAS/SATA Controller Driver，用于读取硬盘信息

Client配置
---

[Windows客户端配置](https://www.jianshu.com/p/9befd0bc7188)

```sheel
#无法抓取Client端数据，需要设定server端端口，并重启zabbix
#手动设定端口:10051
vim /etc/zabbix/zabbix_server.conf
sudo /etc/init.d/zabbix-server restart
```

[Client端脚本](https://github.com/Charles-Miao/Server-Monitoring/tree/master/Ver2.0/zabbix/Zabbix)
---

- zabbix client端程序
- sender采集脚本（抓取Windows一些基本信息）
- agent自定义key（DELL服务器硬件监控）