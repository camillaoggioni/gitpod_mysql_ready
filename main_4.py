import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT name, address FROM customers")
#Fatchall estrae tutte le righe della tabella
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

mycursor.execute("SELECT * FROM customers")
#Fatchone estrae una sola riga della tabella
myresult = mycursor.fetchone()

print(myresult)


