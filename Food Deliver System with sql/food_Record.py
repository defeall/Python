import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nirajkumar28@"
)
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE FoodUser_Record")

