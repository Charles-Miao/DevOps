#!/usr/bin/python
import os
import re
import time
import ConfigParser

def get_NIC_controller():
    conent=os.popen("lspci | grep Ethernet | cut -f3 -d':' | cut -f1 -d'(' | uniq").readlines()
    return conent[0]

def get_cpu_name():
    conent=os.popen("cat /proc/cpuinfo | grep name | cut -f2 -d: | uniq").readlines()
    return conent[0]

def get_cpu_qty():
    conent=os.popen("cat /proc/cpuinfo | grep 'physical id' | sort | uniq | wc -l").readlines()
    return conent[0]

def get_cpu_core():
    conent=os.popen("cat /proc/cpuinfo | grep 'cpu cores' | cut -f2 -d: | uniq").readlines()
    return conent[0]

def get_os_version():
    conent=os.popen("cat /etc/redhat-release").readlines()
    return conent[0]

def get_os_version_detail():
    conent=os.popen("uname -a").readlines()
    return conent[0]

def sync_time():
    conent=os.popen("ntpdate -u 172.30.30.7").readlines()
    time.sleep(5)
    conent=os.popen("ntpdate -u 172.30.30.7").readlines()
    if len(conent)==0:
        result=0
    for index in range(len(conent)):
        if "adjust time server 172.30.30.7 offset" in conent[index]:
            result=1
        else:
            result=0
    return result 

def get_Install_Date():
    conent=os.popen("passwd -S root").readlines()
    install_date=re.split(r'[ ]',conent[0])	
    date_time=install_date[2]+" 0:0:0 AM"
    timeArray=time.strptime(date_time, "%Y-%m-%d %H:%M:%S %p")
    timeStamp=int(time.mktime(timeArray))
    return(str(timeStamp))

if __name__=='__main__':
    config=ConfigParser.ConfigParser()
    config.read('/etc/zabbix/server_info.ini')
    agentd_hostname=config.get('Server_Info','Agent_Hostname')
    asset_number=config.get('Server_Info','Asset_Number')
    Location=config.get('Server_Info','Location')

    
    os_version=get_os_version()
    os_version_detail=get_os_version_detail()

    cpu_name=get_cpu_name()
    cpu_qty=str(int(get_cpu_qty()))
    cpu_core=get_cpu_core()
    cpu_cores=str(int(cpu_qty)*int(cpu_core))
    
    sync_time_result=str(sync_time())
    Original_Install_Date=get_Install_Date()
    
    NIC_controller=get_NIC_controller()

    asset_number_command='zabbix_sender -z 192.168.123.211 -p 10051 -s "'+agentd_hostname+'" -k asset -o '+'"'+asset_number+'"'
    Location_command='zabbix_sender -z 192.168.123.211 -p 10051 -s "'+agentd_hostname+'" -k location -o '+'"'+Location+'"'
    os_version_command='zabbix_sender -z 192.168.123.211 -p 10051 -s "'+agentd_hostname+'" -k OS.name -o '+'"'+os_version+'"'
    os_version_detail_command='zabbix_sender -z 192.168.123.211 -p 10051 -s "'+agentd_hostname+'" -k OS.version -o '+'"'+os_version_detail+'"'
    cpu_name_command='zabbix_sender -z 192.168.123.211 -p 10051 -s "'+agentd_hostname+'" -k CPU.name -o '+'"'+cpu_name+'"'
    cpu_qty_command='zabbix_sender -z 192.168.123.211 -p 10051 -s "'+agentd_hostname+'" -k CPU.QTY -o '+'"'+cpu_qty+'"'
    cpu_cores_command='zabbix_sender -z 192.168.123.211 -p 10051 -s "'+agentd_hostname+'" -k CPU.cores -o '+'"'+cpu_cores+'"'
    sync_time_command='zabbix_sender -z 192.168.123.211 -p 10051 -s "'+agentd_hostname+'" -k system.sync_time -o '+'"'+sync_time_result+'"'
    Original_Install_Date_command='zabbix_sender -z 192.168.123.211 -p 10051 -s "'+agentd_hostname+'" -k install.time -o '+'"'+Original_Install_Date+'"'
    NIC_controller_command='zabbix_sender -z 192.168.123.211 -p 10051 -s "'+agentd_hostname+'" -k NIC.Name -o '+'"'+NIC_controller+'"'

    os.system(asset_number_command)
    os.system(Location_command)
    os.system(os_version_command)
    os.system(os_version_detail_command)
    os.system(cpu_name_command)
    os.system(cpu_qty_command)
    os.system(cpu_cores_command)
    os.system(sync_time_command)
    os.system(Original_Install_Date_command)
    os.system(NIC_controller_command)
