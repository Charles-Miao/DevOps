import os
import time
import configparser

def get_sync_time_result():

#	net_use=os.popen(r'net use \\192.168.123.71 /user:administrator TBUITEMEZ900!!').readlines()
#	print(net_use)
#	net_time=os.popen(r'net time \\192.168.123.71 /set /y').readlines()
#	print(net_time)
#	sync_result=0
#	for index in range(len(net_time)):
#		if net_time[index].strip()=="The command completed successfully.":
#			sync_result=1
#	
#	if sync_result==1:
#		return(1)
#	else:
#		return(0)

	#set log path
	sync_time_log="C:\Zabbix\windows\Sync_time.log"
	
	#delete log file
	if os.path.exists(sync_time_log):
		os.remove(sync_time_log)
	
	#call sync time batch file
	os.system(r"C:\Zabbix\windows\PSTools\psexec -u administrator -p password C:\Zabbix\windows\Sync_time.bat")
	
	time.sleep(30)
	
	#read log file
	read_log=open(sync_time_log,mode='r',encoding='UTF-8')
	conent=read_log.readlines()
	read_log.close()
	
	#get sync time result
	sync_result=0
	for index in range(len(conent)):
		if conent[index].strip()=="The command completed successfully.":
			sync_result=1
	
	if sync_result==1:
		return(1)
	else:
		return(0)
	
if __name__ == '__main__':
	config=configparser.ConfigParser()
	config.read(r"C:\Zabbix\windows\server_info.ini")
	agentd_hostname=config.get("Server_Info","Agentd_Hostname")
	#initialization
	sender="C:\Zabbix\zabbix_sender.exe"
	#agentd_hostname="Mainstore Server 237"
	synctime_result=str(get_sync_time_result())
	print(synctime_result)
	command=sender+' -z 192.168.123.211 -p 10051 -s "'+agentd_hostname+'" -k system.sync_time -o '+'"'+synctime_result+'"'
	os.system(command)