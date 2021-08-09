import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Nirajkumar28@"
)

mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE library")
