import os
import re
import sys

def pdisk_status(controller,ID):
	command="omreport storage pdisk controller="+controller
	conent=os.popen(command).readlines()
	for index in range(len(conent)):
		if "ID                              :" in conent[index]:
			read_ID=re.split(r'[:]',conent[index])[1].strip()+":"+re.split(r'[:]',conent[index])[2].strip()+":"+re.split(r'[:]',conent[index])[3].strip()
			if read_ID==ID:
				each_status=re.split(r'[:]',conent[index+1])[1].strip()
				each_state=re.split(r'[:]',conent[index+3])[1].strip()
				if each_status=="Ok" and each_state=="Online":
					return(1)
				else:
					return(0)
			
if __name__ == '__main__':
	print(pdisk_status(sys.argv[1],sys.argv[2]))
