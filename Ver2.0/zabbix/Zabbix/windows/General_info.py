import os
import re
import time
import configparser

def get_cpu_name():
	conent=os.popen("wmic cpu get name").readlines()
	CPU_name=""
	for index in range(len(conent)):
		if conent[index].strip()=="":
			continue
		elif conent[index].strip()=="Name":
			continue
		else:
			CPU_name=CPU_name+conent[index].strip()+';	'
	return(CPU_name)
	
def get_cpu_QTY():
	conent=os.popen("wmic cpu get DeviceID").readlines()
	CPU_QTY=0
	for index in range(len(conent)):
		if conent[index].strip()=="":
			continue
		elif conent[index].strip()=="DeviceID":
			continue
		else:
			CPU_QTY=CPU_QTY+1
	return(str(CPU_QTY))
	
def get_CPU_NumberOfCores():
	conent=os.popen("wmic cpu get NumberOfCores").readlines()
	CPU_NumberOfCores=0
	for index in range(len(conent)):
		if conent[index].strip()=="":
			continue
		elif conent[index].strip()=="NumberOfCores":
			continue
		else:
			CPU_NumberOfCores=CPU_NumberOfCores+int(conent[index].strip())
	return(str(CPU_NumberOfCores))
		
def get_systeminfo():
	#Initialization
	systeminfo_log="C:\Zabbix\windows\systeminfo.log"
	if os.path.exists(systeminfo_log):
		os.remove(systeminfo_log)

	#get systeminfo
	os.system(r'C:\Zabbix\windows\get_systeminfo.bat')

def get_systeminfo_detail(query):
	#Initialization
	systeminfo_log="C:\Zabbix\windows\systeminfo.log"
	systeminfo_detail=""
	#read log file
	read_log=open(systeminfo_log,mode='r',encoding='UTF-8')
	conent=read_log.readlines()
	for index in range(len(conent)):
		if query in conent[index]:
			systeminfo_detail=re.split(r'[:]',conent[index])[1].strip()	
	read_log.close()
	return(systeminfo_detail)	
	
def get_OS_Version():
	#Initialization
	systeminfo_log="C:\Zabbix\windows\systeminfo.log"
	OS_Version=""
	#read log file
	read_log=open(systeminfo_log,mode='r',encoding='UTF-8')
	conent=read_log.readlines()
	for index in range(len(conent)):
		if "OS Version"==re.split(r'[:]',conent[index])[0].strip():
			OS_Version=re.split(r'[:]',conent[index])[1].strip()	
	read_log.close()
	return(OS_Version)	

def get_Install_Date():
	#Initialization
	systeminfo_log="C:\Zabbix\windows\systeminfo.log"
	Install_Date=""
	#read log file
	read_log=open(systeminfo_log,mode='r',encoding='UTF-8')
	conent=read_log.readlines()
	for index in range(len(conent)):
		if "Original Install Date" in conent[index]:
			Install_Date=re.split(r'[:,]',conent[index])[1].strip()	
			H=re.split(r'[:,]',conent[index])[2].strip()	
			T=re.split(r'[:,]',conent[index])[3].strip()
			S=re.split(r'[:,]',conent[index])[4].strip().split()[0]
			P=re.split(r'[:,]',conent[index])[4].strip().split()[1]	
	read_log.close()
	date_time=Install_Date+" "+H+":"+T+":"+S+" "+P
	timeArray=time.strptime(date_time, "%m/%d/%Y %H:%M:%S %p")
	timeStamp=int(time.mktime(timeArray))
	return(str(timeStamp))	
	
def get_Install_Date_cn():
	#Initialization
	systeminfo_log="C:\Zabbix\windows\systeminfo.log"
	Install_Date=""
	#read log file
	read_log=open(systeminfo_log,mode='r',encoding='UTF-8')
	conent=read_log.readlines()
	for index in range(len(conent)):
		if "Original Install Date" in conent[index]:
			Install_Date=re.split(r'[:,]',conent[index])[1].strip()	
			H=re.split(r'[:,]',conent[index])[2].strip()	
			T=re.split(r'[:,]',conent[index])[3].strip()
			S=re.split(r'[:,]',conent[index])[4].strip()
	read_log.close()
	date_time=Install_Date+" "+H+":"+T+":"+S
	timeArray=time.strptime(date_time, "%Y/%m/%d %H:%M:%S")
	timeStamp=int(time.mktime(timeArray))
	return(str(timeStamp))	

def get_Hotfix():
	#Initialization
	systeminfo_log="C:\Zabbix\windows\systeminfo.log"
	Hotfix=""
	#read log file
	read_log=open(systeminfo_log,mode='r',encoding='UTF-8')
	conent=read_log.readlines()
	for index in range(len(conent)):
		if "Hotfix(s):" in conent[index]:
			installed_quantity=int(re.split(r'[:]',conent[index])[1].strip().split()[0])
			for num in range(1,installed_quantity+1):
				Hotfix=Hotfix+re.split(r'[:]',conent[index+num])[1].strip()+","
	read_log.close()
	return(Hotfix)	
	
if __name__ == '__main__':
	config=configparser.ConfigParser()
	config.read(r"C:\Zabbix\windows\server_info.ini")
	agentd_hostname=config.get("Server_Info","Agentd_Hostname")
	asset_number=config.get("Server_Info","Asset_Number")
	Location=config.get("Server_Info","Location")

	#initialization
	sender="C:\Zabbix\zabbix_sender.exe"
#	agentd_hostname="Mainstore Server 237"
#	asset_number="21F01259"
#	Location="B6-3F,A6-R1-5,U21-U29"
	
	#get system info
	get_systeminfo()
	
	#get CPU name
	CPU_name=get_cpu_name()
	#get CPU QTY
	CPU_QTY=get_cpu_QTY()
	#get CPU NumberOfCores
	CPU_NumberOfCores=get_CPU_NumberOfCores()
	#get OS Name
	OS_Name=get_systeminfo_detail("OS Name:")
	#get OS version
	OS_Version=get_OS_Version()
	#get Original Insatll Date
	if get_systeminfo_detail("System Locale:")=="en-us;English (United States)":
		Original_Install_Date=get_Install_Date()
	elif get_systeminfo_detail("System Locale:")=="zh-cn;Chinese (China)":
		Original_Install_Date=get_Install_Date_cn()
	else:
		Original_Install_Date=str(0)
	#get Manufacturer
	System_Manufacturer=get_systeminfo_detail("System Manufacturer:")
	#get Model
	System_Model=get_systeminfo_detail("System Model:")
	#get Type
	System_Type=get_systeminfo_detail("System Type:")
	#get Locale
	System_Locale=get_systeminfo_detail("System Locale:")
	#get Hotfix
	Hotfixs=get_Hotfix()

	#set sending command
	asset_number_command=sender+' -z 192.168.123.211 -p 10051 -s "'+agentd_hostname+'" -k windows.asset -o '+'"'+asset_number+'"'
	Location_command=sender+' -z 192.168.123.211 -p 10051 -s "'+agentd_hostname+'" -k windows.location -o '+'"'+Location+'"'
	
	CPU_name_command=sender+' -z 192.168.123.211 -p 10051 -s "'+agentd_hostname+'" -k CPU.name -o '+'"'+CPU_name+'"'
	CPU_QTY_command=sender+' -z 192.168.123.211 -p 10051 -s "'+agentd_hostname+'" -k CPU.QTY -o '+'"'+CPU_QTY+'"'
	CPU_NumberOfCores_command=sender+' -z 192.168.123.211 -p 10051 -s "'+agentd_hostname+'" -k CPU.cores -o '+'"'+CPU_NumberOfCores+'"'
	
	OS_Name_command=sender+' -z 192.168.123.211 -p 10051 -s "'+agentd_hostname+'" -k windows.OS.name -o '+'"'+OS_Name+'"'
	OS_Version_command=sender+' -z 192.168.123.211 -p 10051 -s "'+agentd_hostname+'" -k windows.OS.version -o '+'"'+OS_Version+'"'
	Original_Install_Date_command=sender+' -z 192.168.123.211 -p 10051 -s "'+agentd_hostname+'" -k windows.install.time -o '+'"'+Original_Install_Date+'"'
	System_Manufacturer_command=sender+' -z 192.168.123.211 -p 10051 -s "'+agentd_hostname+'" -k hardware.manufacturer -o '+'"'+System_Manufacturer+'"'
	System_Model_command=sender+' -z 192.168.123.211 -p 10051 -s "'+agentd_hostname+'" -k hardware.model -o '+'"'+System_Model+'"'
	System_Type_command=sender+' -z 192.168.123.211 -p 10051 -s "'+agentd_hostname+'" -k system.type -o '+'"'+System_Type+'"'
	System_Locale_command=sender+' -z 192.168.123.211 -p 10051 -s "'+agentd_hostname+'" -k system.locale -o '+'"'+System_Locale+'"'
	Hotfixs_command=sender+' -z 192.168.123.211 -p 10051 -s "'+agentd_hostname+'" -k system.hotfixs -o '+'"'+Hotfixs+'"'

	#sending
	os.system(asset_number_command)
	os.system(Location_command)
	os.system(CPU_name_command)
	os.system(CPU_QTY_command)
	os.system(CPU_NumberOfCores_command)
	os.system(OS_Name_command)
	os.system(OS_Version_command)
	os.system(Original_Install_Date_command)
	os.system(System_Manufacturer_command)
	os.system(System_Model_command)
	os.system(System_Type_command)
	os.system(System_Locale_command)
	os.system(Hotfixs_command)
