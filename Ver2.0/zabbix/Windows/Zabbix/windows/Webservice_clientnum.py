import os

def get_webservice_clientnum():
	conent=os.popen('netstat -n |findstr ":80 :808"').readlines()
	return(len(conent))
	
if __name__ == '__main__':
	print(get_webservice_clientnum())