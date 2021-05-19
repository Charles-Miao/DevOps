import os
import re
import sys

def get_pdisk_status(memory):
	conent=os.popen("sudo hpasmcli -s 'show dimm'").readlines()
	memory_id=[]
	memory_id.append(re.split(r'[:]',memory)[0].strip())
	memory_id.append(re.split(r'[:]',memory)[1].strip())
	for index in range(len(conent)):
		if "Processor #:" in conent[index] and re.split(r'[\t\n: ]',conent[index])[3].strip()==memory_id[0] and re.split(r'[\t\n: ]',conent[index+1])[9].strip()==memory_id[1]:
			return re.split(r'[\t\n: ]',conent[index+2])[9].strip()

if __name__=='__main__':
	if get_pdisk_status(sys.argv[1])=="Yes":
		print 1
	else:
		print 0
