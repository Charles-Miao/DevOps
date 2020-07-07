import os
import re
import sys

def Is_IP_reachable(adapter):
	conent=os.popen("ipconfig /all").readlines()
	for index in range(len(conent)):
		if re.split(r'[:]',conent[index])[0].strip()==adapter:
			if re.split(r'[:]',conent[index+2])[1].strip()== "Media disconnected":
				return(-1)
			else:
				reachable=0
				while "IPv4 Address" not in re.split(r'[:.]',conent[index])[0].strip():
					index=index+1
				IP=re.split(r'[:()]',conent[index])[1].strip()
				#IP=re.split(r'[:()]',conent[index+8])[1].strip()
				ping_command="ping "+IP+" -n 1"
				ping_result=os.popen(ping_command).readlines()
				for ping_index in range(len(ping_result)):
					if "Packets: Sent = 1, Received = 1, Lost = 0 (0% loss)," in ping_result[ping_index].strip():
						reachable=1
				if reachable==1:
					return(1)
				else:
					return(0)
						
if __name__ == '__main__':
	print(Is_IP_reachable(sys.argv[1]))