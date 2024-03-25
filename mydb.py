import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='New-Password-Here123415151!',
)

# prepare a cursor object using cursor() method
cursorObject = dataBase.cursor()

# create database
cursorObject.execute("CREATE DATABASE elderco")

print("Database created successfully........")
