import os
import re
import sys

def Is_IP_reachable(adapter):
	conent=os.popen("ifconfig -a").readlines()
	for index in range(len(conent)):
		if adapter=="lo" or adapter=="sit0":
			break
		elif re.split(r'[ ]',conent[index])[0].strip()==adapter:
			reachable=0
			IP=re.split(r'[: ]',conent[index+1].strip())[2].strip()
			ping_command="ping "+IP+" -c 1"
			ping_result=os.popen(ping_command).readlines()
			for ping_index in range(len(ping_result)):
				if "1 packets transmitted, 1 received, 0% packet loss, time 0ms" in ping_result[ping_index].strip():
					reachable=1
			if reachable==1:
				return 1
			else:
				return 0
						
if __name__ == '__main__':
	print Is_IP_reachable(sys.argv[1])
