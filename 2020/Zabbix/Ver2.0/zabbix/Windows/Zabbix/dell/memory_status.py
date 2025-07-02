import os
import re

def check_chassis_memory_status():
	conent=os.popen("omreport chassis").readlines()
	for index in range(len(conent)):
		if ": Memory" in conent[index]:
			memory_status=re.split(r'[:]',conent[index])[0].strip()	
	return(memory_status)

if __name__ == '__main__':
	if check_chassis_memory_status()=="Ok":
		print(1)
	else:
		print(0)
