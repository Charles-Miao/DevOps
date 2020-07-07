import os
import re
import sys

def get_IP_address(adapter):
	conent=os.popen("ifconfig -a").readlines()
	for index in range(len(conent)):
		if adapter=="lo" or adapter=="sit0":
			break
		if re.split(r'[ ]',conent[index])[0].strip()==adapter:
			return re.split(r'[: ]',conent[index+1].strip())[2].strip()

if __name__ == '__main__':
	print get_IP_address(sys.argv[1])
