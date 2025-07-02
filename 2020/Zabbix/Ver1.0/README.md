V1.0
---

**工具包**

- HP服务器：hpacucli，hpasmcli（Google和HP官网无法找到这个tool）

- DELL服务器：OMSA管理工具

**实践方式**

- 读取硬体信息写入MySQL DB，再从DB中读取信息，并用Web展示
- Dell服务器使用omreport指令
- HP服务器可以登录HP System Mamagement Homepage进行查看，并可以通过网络爬虫技术进行抓取，磁盘和raid等信息可以通过hpacucli指令进行读取

**语言**

- Client端：python
- Web后端：python
- Web前端：HTML，CSS，JS
- Web框架：vue，elementUI，JQuery
