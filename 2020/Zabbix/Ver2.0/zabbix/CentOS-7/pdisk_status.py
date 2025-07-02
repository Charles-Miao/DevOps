import os
import re
import sys

def get_pdisk_status(physicaldrive):
	conent=os.popen("sudo hpacucli ctrl all show config").readlines()
	for index in range(len(conent)):
		if physicaldrive in conent[index] and re.split(r'[ ]',conent[index])[7].strip()==physicaldrive:
			return re.split(r'[) ]',conent[index])[15].strip()


if __name__=='__main__':
	if get_pdisk_status(sys.argv[1])=="OK":
		print 1
	else:
		print 0
