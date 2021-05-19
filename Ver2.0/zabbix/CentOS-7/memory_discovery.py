import os
import re
import json

def discovery_memory_id():
	conent=os.popen("sudo hpasmcli -s 'show dimm'").readlines()
	memory_id=[]
	for index in range(len(conent)):
		if "Processor #:" in conent[index]:
			memory_id.append(re.split(r'[\t\n: ]',conent[index])[3].strip()+":"+re.split(r'[\t\n: ]',conent[index+1])[9].strip())
	return memory_id

if __name__=='__main__':
	memory={}
	memory_list=[]
	memory_id=discovery_memory_id()

	for index in range(len(memory_id)):
		memory_list.append({"{#MEMORY}":memory_id[index]})
	memory={"data":memory_list}
	memory_json=json.dumps(memory)
	print memory_json
