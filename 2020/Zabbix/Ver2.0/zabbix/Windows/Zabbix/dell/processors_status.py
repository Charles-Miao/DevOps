import os
import re

def check_chassis_processors_status():
	conent=os.popen("omreport chassis").readlines()
	for index in range(len(conent)):
		if ": Processors" in conent[index]:
			processors_status=re.split(r'[:]',conent[index])[0].strip()	
	return(processors_status)

if __name__ == '__main__':
	if check_chassis_processors_status()=="Ok":
		print(1)
	else:
		print(0)
