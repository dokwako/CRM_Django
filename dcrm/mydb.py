# install mysql
# pip install mysql
# pip install mysql-connector
#pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Password@123'
)

 # preparing cursor object
cursorObject = dataBase.cursor()

# creating the database 
cursorObject.execute(" CREATE DATABASE elderco")

print("All done")
