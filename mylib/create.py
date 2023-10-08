"""
Transforms and Loads data into the local SQLite3 database
"""
import sqlite3
import csv


#load the csv file and insert into a new sqlite3 database
def create(dataset="data/listing.csv"):
    """"Transforms and Loads data into the local SQLite3 database"""

    payload = csv.reader(open(dataset, newline=''), delimiter=',')
    conn = sqlite3.connect('Customer.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS Customer")
    c.execute("CREATE TABLE Customer (id, name, sex)")
    #insert
    c.execute("INSERT INTO listingDB VALUES ('001','John','Female)")
    conn.commit()
    conn.close()
    return "Customer.db"

