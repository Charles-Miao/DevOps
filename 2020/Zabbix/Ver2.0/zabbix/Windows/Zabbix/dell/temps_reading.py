import os
import re

def temps_reading():
	conent=os.popen("omreport chassis temps").readlines()
	for index in range(len(conent)):
		if "Reading                   :" in conent[index]:
			temps_reading=float(re.split(r'[:]',conent[index])[1].strip()[0:-1])
	return(temps_reading)
			
if __name__ == '__main__':
	print(temps_reading())