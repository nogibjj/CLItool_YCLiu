"""
Transforms and Loads data into the local SQLite3 database
"""
import sqlite3

#load the csv file and insert into a new sqlite3 database
def createCustomer():
    """"Create databse"""
    conn = sqlite3.connect('Customer.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS Customer")
    c.execute("CREATE TABLE Customer (id, name, sex)")
    #insert
    c.execute("INSERT INTO Customer VALUES ('001','John','Male')")
    c.execute("INSERT INTO Customer VALUES ('002','Devin','Female')")
    c.execute("INSERT INTO Customer VALUES ('003','Sharon','Female')")
    c.execute("INSERT INTO Customer VALUES ('004','Tim','Male')")
    c.execute("INSERT INTO Customer VALUES ('005','Tina','Female')")
    conn.commit()
    conn.close()
    return "Customer.db"
