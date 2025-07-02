import os
import re
import json

def discovery_logicaldrive_id():
	conent=os.popen("sudo hpacucli ctrl all show config").readlines()
	logicaldrive_id=[]
	for index in range(len(conent)):
		if "logicaldrive" in conent[index]:
			logicaldrive_id.append(re.split(r'[ ]',conent[index])[7].strip())
	return logicaldrive_id

if __name__=='__main__':
	logicaldrive={}
	logicaldrive_list=[]
	logicaldrive_id=discovery_logicaldrive_id()

	for index in range(len(logicaldrive_id)):
		logicaldrive_list.append({"{#LOGICALDRIVE}":logicaldrive_id[index]})
	logicaldrive={"data":logicaldrive_list}
	logicaldrive_json=json.dumps(logicaldrive)
	print logicaldrive_json
