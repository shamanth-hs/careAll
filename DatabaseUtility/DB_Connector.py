import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="admin",
    database="care_all"
)

cursor = con.cursor()
cursor.execute("Create table if not exists")