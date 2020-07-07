chcp 437
echo off

set log_file=C:\Zabbix\windows\systeminfo.log

if exist %log_file% del %log_file%

systeminfo > %log_file%