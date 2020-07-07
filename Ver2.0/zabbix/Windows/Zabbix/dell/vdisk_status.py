import os
import re
import sys

def vdisk_status(controller,ID):
	command="omreport storage vdisk controller="+controller
	conent=os.popen(command).readlines()
	for index in range(len(conent)):
		if "ID                                :" in conent[index]:
			read_ID=int(re.split(r'[:]',conent[index])[1].strip())
			if read_ID==ID:
				each_status=re.split(r'[:]',conent[index+1])[1].strip()
				each_state=re.split(r'[:]',conent[index+3])[1].strip()
				if each_status=="Ok" and each_state=="Ready":
					return(1)
				else:
					return(0)
			
if __name__ == '__main__':
	print(vdisk_status(sys.argv[1],int(sys.argv[2])))