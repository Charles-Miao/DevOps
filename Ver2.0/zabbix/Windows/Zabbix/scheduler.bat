call C:\Zabbix\windows\General_info.py
call C:\Zabbix\windows\SoftwareList.py
call C:\Zabbix\windows\Sync_time.py
call C:\Zabbix\windows\activation.py
::get officescan server virus pattern
net use w: /d /y
net use w: \\172.168.168.100\ofcscan /user:admin btco
call C:\Zabbix\windows\OfficeScan_server_ptn.py
net use w: /d /y