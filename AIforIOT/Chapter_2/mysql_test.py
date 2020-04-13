import mysql.connector
connection = mysql.connector.connect(host="127.0.0.1", user="root", password="root", database='mysql')

mycursor = connection.cursor()
mycursor.execute("SHOW TABLES")
for x  in mycursor:
  print(x)

