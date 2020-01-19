@echo off
if exist C:\Zabbix\windows\ofcscan.ini del C:\Zabbix\windows\ofcscan.ini
copy \\172.168.168.100\ofcscan\ofcscan.ini C:\Zabbix\windows\ofcscan.ini /y
