from flask import render_template
from flask import Flask


app = Flask(__name__)

import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
  database="CLASH_ROYALE"
)
mycursor = mydb.cursor()

@app.route('/units')
def unitList():
    mycursor.execute("SELECT * FROM Clash_Unit")
    myresult= mycursor.fetchall()
    return render_template(clash_units.html, units=myresult)