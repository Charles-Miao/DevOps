import os
import re
import sys

def fans_reading(num):
	conent=os.popen("omreport chassis fans").readlines()
	#read each fan rpm 
	fans={}
	for index in range(len(conent)):
		if "Index                     :" in conent[index]:
			each_fan_index=int(re.split(r'[:]',conent[index])[1].strip())
			each_fan_rpm=int(re.split(r'[:]',conent[index+3])[1].strip()[0:-3])
			fans[each_fan_index]=each_fan_rpm
	return(fans[num])
	
	
if __name__ == '__main__':
	print(fans_reading(int(sys.argv[1])))
