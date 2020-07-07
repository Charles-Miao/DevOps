import os
import re
import sys

def get_Physical_address(adapter):
	conent=os.popen("ifconfig -a").readlines()
	for index in range(len(conent)):
		if adapter=="lo" or adapter=="sit0":
			break
		elif re.split(r'[ ]',conent[index].strip())[0].strip()==adapter:
			return re.split(r'[ ]',conent[index])[8].strip()
			
if __name__ == '__main__':
	print get_Physical_address(sys.argv[1])
