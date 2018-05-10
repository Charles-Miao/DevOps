import pymysql

db=pymysql.connect("192.168.80.129","root","241668Miao","server_information")

cursor=db.cursor()

sql="""CREATE TABLE SYSTEM
		"""

cursor.execute(sql)

db.close()