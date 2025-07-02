import os
import re

def check_chassis_temps_status():
	conent=os.popen("omreport chassis").readlines()
	for index in range(len(conent)):
		if ": Temperatures" in conent[index]:
			temps_status=re.split(r'[:]',conent[index])[0].strip()	
	return(temps_status)
			
def check_temps_status():
	conent=os.popen("omreport chassis temps").readlines()
	for index in range(len(conent)):
		if "Main System Chassis Temperatures:" in conent[index]:
			temps_status=re.split(r'[:]',conent[index])[1].strip()	
	return(temps_status)
			

if __name__ == '__main__':
	if check_chassis_temps_status()=="Ok":
		print(1)
	else:
		print(0)
