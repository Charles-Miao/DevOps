import pymysql

db=pymysql.connect("192.168.80.129","root","XXX","server_information")

cursor=db.cursor()

sql="""INSERT INTO SYSTEM_SUMMARY (IP, MODEL, HOST_NAME, 
       MEMORY, CPU, OS_NAME, OS_VERSION, BOOTUP_TIME) 
	   VALUES ('192.168.123.56', 'Poweredge 2950', 
	   'molly-web01', 8, 'Intel(R) Xeon(R) CPU E5430@2.66GHz', 
	   'Microsoft Windows Server 2003 R2 Standard Edition', 
	   'Version 5.2 (Build 3790 : Service Pack 2) (x86)', 
	   '2018-2-19 14:42:50')"""

	   
cursor.execute(sql)
db.commit()

db.close()
