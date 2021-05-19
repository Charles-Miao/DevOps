import os
import re
import sys

def get_pdisk_status(processor):
	conent=os.popen("sudo hpasmcli -s 'show server'").readlines()
	for index in range(len(conent)):
		if "Processor:" in conent[index] and re.split(r'[:]',conent[index])[1].strip()==processor:
			return re.split(r'[\n: ]',conent[index+11])[9].strip()

if __name__=='__main__':
	if get_pdisk_status(sys.argv[1])=="Ok":
		print 1
	else:
		print 0
