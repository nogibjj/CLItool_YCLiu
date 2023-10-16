"""
Create local SQLite3 databases
"""
import sqlite3

def create():
    """"Create databse"""
    conn = sqlite3.connect('Transactions.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS Customer")
    c.execute("CREATE TABLE Customer (cust_id, name, sex)")
    c.execute("INSERT INTO Customer VALUES ('001','John','Male')")
    c.execute("INSERT INTO Customer VALUES ('002','Devin','Female')")
    c.execute("INSERT INTO Customer VALUES ('003','Sharon','Female')")
    c.execute("INSERT INTO Customer VALUES ('004','Tim','Male')")
    c.execute("INSERT INTO Customer VALUES ('005','Tina','Female')")
    #TXR
    c.execute("DROP TABLE IF EXISTS TXR")
    c.execute("CREATE TABLE TXR (cust_id, item, amount)")
    
    #insert
    c.execute("INSERT INTO TXR VALUES ('001','Hot Dog',100)")
    c.execute("INSERT INTO TXR VALUES ('001','Hot Dog',20)")
    c.execute("INSERT INTO TXR VALUES ('002','Hamburger',80)")
    c.execute("INSERT INTO TXR VALUES ('002','Hot Dog',120)")
    c.execute("INSERT INTO TXR VALUES ('003','Hamburger',60)")
    c.execute("INSERT INTO TXR VALUES ('003','Hot Dog',200)")
    c.execute("INSERT INTO TXR VALUES ('004','Hot Dog',40)")
    c.execute("INSERT INTO TXR VALUES ('004','Hamburger',140)")
    c.execute("INSERT INTO TXR VALUES ('005','Hamburger',150)")
    c.execute("INSERT INTO TXR VALUES ('005','Hamburger',80)")
    conn.commit()
    conn.close()
    return "Success"

