[Demo笔记](https://www.notion.so/Zabbix-Introduction-89242b87d7b5400ba580971cb6c0f8d0)
===

使用手册
---

[Zabbix官方手册](https://www.zabbix.com/documentation/3.4/zh/manual)

[Zabbix 3.0从入门到精通(Zabbix使用详解)](http://www.cnblogs.com/clsn/p/7885990.html)

Server端安装配置
---

[Ubuntu Zabbix服务端配置](https://my.oschina.net/zhangyangyang/blog/841043)

[安装异常: The frontend does not match Zabbix database ](https://blog.csdn.net/purplegalaxy/article/details/37819899)

```shell
# 时间同步
# crontab -l
00 00 * * * /usr/sbin/ntpdate -u 195.13.1.153
```

Client配置
---

[Windows客户端配置](https://www.jianshu.com/p/9befd0bc7188)

```sheel
#无法抓取Client端数据，需要设定server端端口，并重启zabbix
#手动设定端口:10051
vim /etc/zabbix/zabbix_server.conf
sudo /etc/init.d/zabbix-server restart
```
