技术实践
===

**工具包**

HP服务器：hpacucli，hpasmcli（Google和HP官网无法找到这个tool）

DELL服务器：OMSA管理工具

**实践方式**

读取硬体信息写入MySQL DB，再从DB中读取信息，并用Web展示

1. Dell服务器使用omreport指令
2. HP服务器可以登录HP System Mamagement Homepage进行查看，并可以通过网络爬虫技术进行抓取，磁盘和raid等信息可以通过hpacucli指令进行读取

**语言**

Client端：

- python

Web端：

- 后端：python
- 前端：HTML，CSS，JS
- 框架：vue，elementUI，JQuery

**Zabbix相关知识**

[Zabbix官方手册](https://www.zabbix.com/documentation/3.4/zh/manual)

[Ubuntu Zabbix服务端配置](https://my.oschina.net/zhangyangyang/blog/841043)

[安装异常: The frontend does not match Zabbix database ](https://blog.csdn.net/purplegalaxy/article/details/37819899)

```sheel
#手动设定端口:10051
vim /etc/zabbix/zabbix_server.conf
sudo /etc/init.d/zabbix-server restart
```

[Windows客户端配置](https://www.jianshu.com/p/9befd0bc7188)

[Zabbix 3.0从入门到精通(Zabbix使用详解)](http://www.cnblogs.com/clsn/p/7885990.html)

**其他知识**

- Ubuntu Xmark工具：**Remarkable**
- [ubuntu下使用git和github](https://blog.csdn.net/qq_31456593/article/details/79248706)
- [如何在ubuntu下使用Github？](https://blog.csdn.net/tina_ttl/article/details/51326684)

