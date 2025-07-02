import os
import re
import json

def discovery_processor_id():
	conent=os.popen("sudo hpasmcli -s 'show server'").readlines()
	processor_id=[]
	for index in range(len(conent)):
		if "Processor:" in conent[index]:
			processor_id.append(re.split(r'[: ]',conent[index])[2].strip())
	return processor_id

if __name__=='__main__':
	processor={}
	processor_list=[]
	processor_id=discovery_processor_id()

	for index in range(len(processor_id)):
		processor_list.append({"{#PROCESSOR}":processor_id[index]})
	processor={"data":processor_list}
	processor_json=json.dumps(processor)
	print processor_json
