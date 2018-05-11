import pymysql

db=pymysql.connect("192.168.80.129","root","241668Miao","server_information")

cursor=db.cursor()

sql="""CREATE TABLE SYSTEM_SUMMARY (
	   IP CHAR(16) NOT NULL PRIMARY KEY,
	   MODEL CHAR(21),
	   HOST_NAME CHAR(33),
	   MEMORY INT,
	   CPU TEXT,
	   OS_NAME TEXT,
	   OS_VERSION TEXT,
	   BOOTUP_TIME DATETIME )"""


cursor.execute(sql)

sql="""CREATE TABLE CM0S_BATTERY (
	   IP CHAR(16) NOT NULL,
	   HEALTH CHAR,
	   STATUS CHAR,
	   READING CHAR,
	   COLLECTION_TIME DATETIME,
	   FOREIGN KEY (IP) REFERENCES SYSTEM_SUMMARY(IP))"""
	   
cursor.execute(sql)

db.close()