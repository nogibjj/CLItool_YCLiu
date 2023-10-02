"""Query the database"""

import sqlite3


def query():
    """Query the database for the top 1 row of the listingDB table"""
    conn = sqlite3.connect("listingDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT bedrooms FROM listingDB LIMIT 2")
    
    print(cursor.fetchall())
    conn.close()
    return "Success"


