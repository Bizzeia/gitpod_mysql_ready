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



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",                          
  database="animali"                    #ti connette al server inserito
)



mycursor.execute("CREATE TABLE customers (id INT primary key auto_increment, name VARCHAR(324), address VARCHAR(234))")  

                ("ALTER TABLE customers ADD COLUMN surname VARCHAR(213)")