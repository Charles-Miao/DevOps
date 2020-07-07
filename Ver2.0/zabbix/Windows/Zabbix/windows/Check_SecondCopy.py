import os
import re
import time
import configparser


def check_second_copy():
	#Initialization
	second_copy_log=r"C:\Program Files (x86)\SecCopy\log.rtf"
	check_SecCopy_result=1
	#read log file
	read_log=open(second_copy_log,mode='r',encoding='UTF-8')
	conent=read_log.readlines()
	for index in range(len(conent)):
		if "errors" in conent[index]:
			check_SecCopy_result=0	
	read_log.close()
	return(check_SecCopy_result)	
	
	
if __name__ == '__main__':
	print(check_second_copy())