#! /usr/bin/python
import mysql.connector

# You Need To Change Credentials OF Connection According
# To Your MYSQL DataBase At 4 Places In This Script
# Must Use Quotation Marks ""
def createdb():
    try:
        connector = mysql.connector.connect(host="localhost",
                                            user="enter-your-mysql-username-here",
                                            password="enter-your-mysql-password-here")
        cur = connector.cursor()
        q = "CREATE DATABASE passlist"
        cur.execute(q)
        connector.commit()
        print("database created successfully...")
        cur.close()
        connector.close()

    except:
        print("Connection Error Occured In Database Connection")
        exit()

def createtb():
    try:
        connector = mysql.connector.connect(host="localhost",
                                            user="enter-your-mysql-username-here",
                                            password="enter-your-mysql-password-here",
                                            database="passlist")
        cur = connector.cursor()
        q = "CREATE TABLE password(id INT PRIMARY KEY AUTO_INCREMENT,username VARCHAR(50),pass VARCHAR(150))"
        cur.execute(q)
        connector.commit()
        print("tables created successfully...")
        cur.close()
        connector.close()

    except:
        print("Connection Error Occured In Database Connection")
        exit()


createdb()
createtb()

