"""
Transforms and Loads data into the local SQLite3 database
"""
import sqlite3

#load the csv file and insert into a new sqlite3 database
def create():
    """"Create databse"""
    conn = sqlite3.connect('Customer.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS Customer")
    c.execute("CREATE TABLE Customer (id, name, sex)")
    #insert
    c.execute("INSERT INTO Customer VALUES ('001','John','Female')")
    conn.commit()
    conn.close()
    return "Customer.db"
