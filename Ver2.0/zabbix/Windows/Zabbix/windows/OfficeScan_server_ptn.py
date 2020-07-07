import configparser
import re
import os
import json
import configparser
import time

def get_officescan_server_ptn():
	config=configparser.ConfigParser(strict=False,allow_no_value=True)
	config.read(r'W:\ofcscan.ini')
	ptn=config.get('INI_PROGRAM_VERSION_SECTION','NonCrcPtnVersion')
	return(int(re.split(r'[.]',ptn)[0]+re.split(r'[.]',ptn)[1]+re.split(r'[.]',ptn)[2]))

	
if __name__ == '__main__':

#---discovery method
#	officescan={}
#	officescan_list=[]
#	server_pattern=get_officescan_server_ptn()
#	officescan_list.append({"{#SERVER_PATTERN}":server_pattern})
#	officescan={"data":officescan_list}
#	officescan_json=json.dumps(officescan)
#	print(officescan_json)

#---angent method
#	print(get_officescan_server_ptn())

#---collector method
	config=configparser.ConfigParser()
	config.read(r"C:\Zabbix\windows\server_info.ini")
	agentd_hostname=config.get("Server_Info","Agentd_Hostname")
	sender="C:\Zabbix\zabbix_sender.exe"
#	agentd_hostname="Mainstore Server 237"
	server_officescan_ptn=str(get_officescan_server_ptn())
#	print(server_officescan_ptn)
	command=sender+' -z 192.168.123.211 -p 10051 -s "'+agentd_hostname+'" -k officescan.server.ptn -o '+'"'+server_officescan_ptn+'"'
	os.system(command)