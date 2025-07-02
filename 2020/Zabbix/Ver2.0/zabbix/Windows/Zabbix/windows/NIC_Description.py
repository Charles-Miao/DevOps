import os
import re
import sys

def get_Physical_address(adapter):
	conent=os.popen("ipconfig /all").readlines()
	for index in range(len(conent)):
		if re.split(r'[:]',conent[index])[0].strip()==adapter:
			if re.split(r'[:]',conent[index+2])[1].strip()== "Media disconnected":
				return(re.split(r'[:]',conent[index+4])[1].strip())
			else:
				return(re.split(r'[:]',conent[index+3])[1].strip())
			
if __name__ == '__main__':
	print(get_Physical_address(sys.argv[1]))