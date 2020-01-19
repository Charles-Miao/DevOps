import os
import re

def check_chassis_batteries_status():
	conent=os.popen("omreport chassis").readlines()
	for index in range(len(conent)):
		if ": Batteries" in conent[index]:
			batteries_status=re.split(r'[:]',conent[index])[0].strip()	
	return(batteries_status)
			
if __name__ == '__main__':
	if check_chassis_batteries_status()=="Ok":
		print(1)
	else:
		print(0)
