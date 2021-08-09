import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nirajkumar28@",
    database="FoodUser_Record"
)
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE Foodtable(name VARCHAR(20),password VARCHAR(20),e_mail VARCHAR(50))")


