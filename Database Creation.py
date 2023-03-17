import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="2510triblaz")
db_cursor = mydb.cursor()
db_cursor.execute("CREATE database Car_Rental_Service")
mydb.close()