#! /usr/bin/python
import mysql.connector
from cryptography.fernet import Fernet

################################
###-Change-the-Password-Here-###
code = "pass499"    ##########
###-Quotation-Marks-Are-Must-###
################################

# You Need To Change Credentials OF Connection According
# To Your MYSQL DataBase At 2 Places In This Script
# Must Use Quotation Marks ""
try:
    connector = mysql.connector.connect(host="localhost",
                                    user="enter-your-mysql-username-here",
                                    password="enter-your-mysql-password-here",
                                    database="passlist")
    cur=connector.cursor()

except:
    print("Connection Error Occured In Database Connection")
    exit()

key = b'_RjZ3gPnVUAuA2Ve-7R4ON12ZIfhHwHJ1RFQ_3UMLQ4='

# This Is The Main Function For Program
def main():
    print("\nWelcome to the PassWord Manager :created by DeadDroid")
    while True:
        print("""
    Type a Number For Your Choice
    1) Add a New Password 
    2) Delete Password
    3) List All Password
    4) Update Password
    5) List One Password
    0) For Exit
        """)
        inp = input("Enter Your Choice Here:- ")

        if inp == "1":
            user = input("Enter the username here:- ")
            pas = input("Enter the Password here:- ")
            addpass(user, pas)
            ask()
        elif inp == "2":
            user = input("Enter the username here:- ")
            delpass(user)
            ask()
        elif inp == "3":
            listpass()
            ask()
        elif inp == "4":
            user = input("Enter the username here:- ")
            pas = input("Enter the new Pass here:- ")
            updpass(user, pas)
            ask()
        elif inp == "5":
            user = input("Enter the username here:- ")
            getpass(user)
            ask()
        elif inp == "0":
            print("Bye-Bye ^_^ ")
            exit()
        else:
            print("invalid choice...")
            ask()

def addpass(u,p):
    ins = "INSERT INTO password(username,pass) VALUES (%s,%s)"
    en = encryptedpass(p,key)
    t = (u, en)
    cur.execute(ins, t)
    connector.commit()
    print(f"Password added successfully for : {u}")
def listpass():
    sel = "SELECT * FROM password"
    cur.execute(sel)
    data = cur.fetchall()
    if data:
        print("{:<10}{:<20}{:<30}".format("id", "username", "password"))
        print()
        for s in data:
            dp = decryptedpass(s[2],key)
            print("{:<10}{:<20}{:<30}".format(s[0], s[1], dp))
    else:
        print("List is Empty...")
def getpass(u):
    get = f"SELECT * FROM password WHERE username = %s"
    cur.execute(get, (u,))
    data = cur.fetchone()
    if data:
        print("{:<10}{:<20}{:<30}".format("id", "username", "password"))
        print()
        dp = decryptedpass(data[2],key)
        print("{:<10}{:<20}{:<30}".format(data[0], data[1],dp))
    else:
        print("Username Not Found...")
def delpass(u):
    de = "DELETE FROM password WHERE username = %s"
    cur.execute(de, (u,))
    connector.commit()
    print(f"password deleted successfully for : {u}")
def updpass(u, p):
    ud = "UPDATE password SET pass=%s WHERE username=%s"
    en = encryptedpass(p,key)
    value = (en,u)
    cur.execute(ud, value)
    connector.commit()
    print("password updated succesfully")
def ask():
    ask = input("\nEnter 'y' To Continue or 'q' To Quit:::-- ")
    if ask == "y":
        pass
    else:
        exit()

def encryptedpass(m,key):
    cipher_suite = Fernet(key)
    x = cipher_suite.encrypt(m.encode())
    x = str(x)
    x = x.removeprefix("b'")
    x = x.removesuffix("=='")
    x = x.swapcase()
    x = x[::-1]
    return x

def decryptedpass(em,key):
    x = em
    x = x[::-1]
    x = x.swapcase()
    x = x + "=="
    x = x.encode()
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(x).decode()
    return decrypted_message

# Verification Method For Security
def verify():
    ask = input("\n Enter The Verification PassWord Here:-- ")
    if ask == code:
        pass
    else:
        print("Unlucky ! Pass is Incorrect: Try Next Time")
        exit()

if __name__ == "__main__":
    verify()
    main()
