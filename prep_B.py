import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database= "Animali"
)

mycursor = mydb.cursor()
sql = "INSERT INTO Mammiferi (Nome_proprio, Razza, Peso, Età) VALUES (%s, %s, %s, %s)"
val= [
    ('Capi','Capibara', 40, 20),
    ('Nicoletta', 'Giraffa', 1600, 30),
    ('Ignacio', 'Petauro dello zucchero', 1, 3),
    ('Manolo', 'Alpaca', 60, 15)
]
mycursor.executemany(sql, val)

mydb.commit()
