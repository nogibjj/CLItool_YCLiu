"""Query the database"""

import sqlite3


def query():
    
    conn = sqlite3.connect("Customer.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Customer")    
    output = cursor.fetchall()
    conn.close()
    return output
