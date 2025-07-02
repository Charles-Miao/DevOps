import os
import re
import sys

def get_IP_address(adapter):
	conent=os.popen("ipconfig /all").readlines()
	for index in range(len(conent)):
		if re.split(r'[:]',conent[index])[0].strip()==adapter:
			if re.split(r'[:]',conent[index+2])[1].strip()== "Media disconnected":
				return("NA")
			else:
				while "IPv4 Address" not in re.split(r'[:.]',conent[index])[0].strip():
					#print(re.split(r'[:.]',conent[index])[0].strip())
					index=index+1
				return(re.split(r'[:()]',conent[index])[1].strip())

if __name__ == '__main__':
	print(get_IP_address(sys.argv[1]))