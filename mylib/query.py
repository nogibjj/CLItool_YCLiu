"""Query the database"""

import sqlite3


def query():
    """Query the database for the top 1 row of the listingDB table"""
    conn = sqlite3.connect("listingDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, bedrooms, price FROM listingDB LIMIT 10")
    
    print(cursor.fetchall())
    conn.close()
    return "Success"


