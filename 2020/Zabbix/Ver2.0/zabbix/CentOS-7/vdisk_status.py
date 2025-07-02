import os
import re
import sys

def get_pdisk_status(logicaldrive):
	conent=os.popen("sudo hpacucli ctrl all show config").readlines()
	for index in range(len(conent)):
		if logicaldrive in conent[index] and re.split(r'[ ]',conent[index])[7].strip()==logicaldrive:
			return re.split(r'[) ]',conent[index])[12].strip()

if __name__=='__main__':
	if get_pdisk_status(sys.argv[1])=="OK":
		print 1
	else:
		print 0
