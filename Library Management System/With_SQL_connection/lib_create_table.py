import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Nirajkumar28@",
    database="library"
)

mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE stdetails(id INT NOT NULL,name VARCHAR(255) NOT NULL,rollno INT,year INT NOT NULL)")
