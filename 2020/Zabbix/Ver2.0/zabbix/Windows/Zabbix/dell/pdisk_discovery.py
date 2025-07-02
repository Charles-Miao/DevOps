import os
import re
import json

def discover_controller_ID():
	conent=os.popen("omreport storage controller").readlines()
	controller_ID=[]
	for index in range(len(conent)):
		if "ID                                            :" in conent[index]:
			controller_ID.append(re.split(r'[:]',conent[index])[1].strip())	
	return(controller_ID)
	
def discover_pdisk_ID(controller):
	command="omreport storage pdisk controller="+controller
	conent=os.popen(command).readlines()
	pdisk_ID=[]
	for index in range(len(conent)):
		if "ID                              :" in conent[index]:
			ID=re.split(r'[:]',conent[index])[1].strip()+":"+re.split(r'[:]',conent[index])[2].strip()+":"+re.split(r'[:]',conent[index])[3].strip()
			pdisk_ID.append(ID)
	return(pdisk_ID)

if __name__ == '__main__':
	controller_ID=discover_controller_ID()
	pdisk={}
	pdisk_list=[]
	for controller_index in range(len(controller_ID)):
		pdisk_ID=discover_pdisk_ID(controller_ID[controller_index])
		for pdisk_index in range(len(pdisk_ID)):
			pdisk_list.append({"{#CONTROLLER}":controller_ID[controller_index],"{#PDISK}":pdisk_ID[pdisk_index]})
	pdisk={"data":pdisk_list}
	pdisk_json=json.dumps(pdisk)
	print(pdisk_json)
