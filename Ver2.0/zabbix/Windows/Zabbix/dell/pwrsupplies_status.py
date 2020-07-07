import os
import re

def check_chassis_pwrsupplies_status():
	conent=os.popen("omreport chassis").readlines()
	for index in range(len(conent)):
		if ": Power Supplies" in conent[index]:
			pwrsupplies_status=re.split(r'[:]',conent[index])[0].strip()	
	return(pwrsupplies_status)
			
if __name__ == '__main__':
	if check_chassis_pwrsupplies_status()=="Ok":
		print(1)
	else:
		print(0)
