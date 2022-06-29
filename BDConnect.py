import mysql.connector
from mysql.connector import errorcode, utils

try:
	db_connection = mysql.connector.connect(host='aesc-sqldevhm',port='1433', user='hmd\leonardo.duarte', password='lesodu@2022', database='Qualitor')
	print("Database connection made!")

except mysql.connector.Error as error:
	if error.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database doesn't exist")
	elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("User name or password is wrong")
	else:
		print(error)
else:
	db_connection.close()