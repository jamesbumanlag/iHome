
import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '0911'
    )


# prepare a cursor object
cursorObject = dataBase.cursor()


# Create a database
cursorObject.execute("CREATE DATABASE ihomedb")


print('All Done')