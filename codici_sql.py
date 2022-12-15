import mysql.connector

mydb = mysql.connector.connect(              
  host="localhost",                     #le tre righe sotto sono insrite dal prof
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE bizzeria")        #con questo inserisco il nome del database




import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")      #ti mostra tutti i database nel sistema

for x in mycursor:
  print(x)