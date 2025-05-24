import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
)
# prepare a cursor object
cursor = database.cursor()
# create a database
cursor.execute("CREATE DATABASE IF NOT EXISTS shop")

print("Database created successfully")
