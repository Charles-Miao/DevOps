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
	
def discover_vdisk_ID(controller):
	command="omreport storage vdisk controller="+controller
	conent=os.popen(command).readlines()
	vdisk_ID=[]
	for index in range(len(conent)):
		if "ID                                :" in conent[index]:
			vdisk_ID.append(re.split(r'[:]',conent[index])[1].strip())	
	return(vdisk_ID)

if __name__ == '__main__':
	controller_ID=discover_controller_ID()
	vdisk={}
	vdisk_list=[]
	for controller_index in range(len(controller_ID)):
		vdisk_ID=discover_vdisk_ID(controller_ID[controller_index])
		for vdisk_index in range(len(vdisk_ID)):
			vdisk_list.append({"{#CONTROLLER}":controller_ID[controller_index],"{#VDISK}":vdisk_ID[vdisk_index]})
	vdisk={"data":vdisk_list}
	vdisk_json=json.dumps(vdisk)
	print(vdisk_json)
