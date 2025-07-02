import os
import re
import configparser

def get_InstalledSoftwareList():
	InstalledSoftwareList=""

	conent_32=os.popen("powershell -executionPolicy bypass -file C:\Zabbix\windows\InstalledSoftwareList_32.ps1").readlines()
	for index in range(len(conent_32)):
		if conent_32[index].strip()=="":
			continue
		elif conent_32[index].strip().split()[0]=="Name":
			continue
		elif conent_32[index].strip().split()[0]=="----":
			continue
		elif conent_32[index].strip().split()[0]=="DisplayName":
			continue
		elif conent_32[index].strip().split()[0]=="-----------":
			continue
		elif conent_32[index].strip() in InstalledSoftwareList:
			continue
		else:
			InstalledSoftwareList=InstalledSoftwareList+conent_32[index].strip()+','
			
	conent_64=os.popen("powershell -executionPolicy bypass -file C:\Zabbix\windows\InstalledSoftwareList_64.ps1").readlines()
	for index in range(len(conent_64)):
		if conent_64[index].strip()=="":
			continue
		elif conent_64[index].strip().split()[0]=="Name":
			continue
		elif conent_64[index].strip().split()[0]=="----":
			continue
		elif conent_64[index].strip().split()[0]=="DisplayName":
			continue
		elif conent_64[index].strip().split()[0]=="-----------":
			continue
		elif conent_64[index].strip() in InstalledSoftwareList:
			continue
		else:
			InstalledSoftwareList=InstalledSoftwareList+conent_64[index].strip()+','
	
	return(InstalledSoftwareList)

def get_tasklist():
	conent=os.popen("tasklist /fo list").readlines()
	tasklist=""
	for index in range(len(conent)):
		if "Image Name:" in conent[index]:
			tasklist=tasklist+re.split(r'[:]',conent[index])[1].strip()	+','
	return(tasklist)
	
if __name__ == '__main__':
	config=configparser.ConfigParser()
	config.read(r"C:\Zabbix\windows\server_info.ini")
	agentd_hostname=config.get("Server_Info","Agentd_Hostname")
	#initialization
	sender="C:\Zabbix\zabbix_sender.exe"
	#agentd_hostname="Mainstore Server 237"
	
	#get info
	InstalledSoftwareList=get_InstalledSoftwareList()
	tasklist=get_tasklist()

	#set sending command
	InstalledSoftwareList_command=sender+' -z 192.168.123.211 -p 10051 -s "'+agentd_hostname+'" -k system.installedsoftwarelist -o '+'"'+InstalledSoftwareList+'"'
	tasklist_command=sender+' -z 192.168.123.211 -p 10051 -s "'+agentd_hostname+'" -k system.tasklist -o '+'"'+tasklist+'"'

	#sending
	os.system(InstalledSoftwareList_command)
	os.system(tasklist_command)