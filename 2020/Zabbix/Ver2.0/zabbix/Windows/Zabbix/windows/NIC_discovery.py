import os
import re
import json

def discover_ethernet_adapter():
	conent=os.popen("ipconfig /all").readlines()
	NIC_name=[]
	for index in range(len(conent)):
		if "Ethernet adapter" in conent[index]:
			NIC_name.append(re.split(r'[:]',conent[index])[0].strip())	
	return(NIC_name)

if __name__ == '__main__':
	adapter={}
	adapter_list=[]
	NIC_name=discover_ethernet_adapter()
	
	for adapter_index in range(len(NIC_name)):
		adapter_list.append({"{#ADAPTER}":NIC_name[adapter_index]})
	adapter={"data":adapter_list}
	adapter_json=json.dumps(adapter)
	print(adapter_json)
