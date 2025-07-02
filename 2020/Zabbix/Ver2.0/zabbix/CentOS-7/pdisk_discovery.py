import os
import re
import json

def discovery_physicaldrive_id():
	conent=os.popen("sudo hpacucli ctrl all show config").readlines()
	physicaldrive_id=[]
	for index in range(len(conent)):
		if "physicaldrive" in conent[index]:
			physicaldrive_id.append(re.split(r'[ ]',conent[index])[7].strip())
	return physicaldrive_id

if __name__=='__main__':
	physicaldrive={}
	physicaldrive_list=[]
	physicaldrive_id=discovery_physicaldrive_id()

	for index in range(len(physicaldrive_id)):
		physicaldrive_list.append({"{#PHYSICALDRIVE}":physicaldrive_id[index]})
	physicaldrive={"data":physicaldrive_list}
	physicaldrive_json=json.dumps(physicaldrive)
	print physicaldrive_json
