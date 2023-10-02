import sqlite3

def delete():
    """Update a row of database"""
    conn = sqlite3.connect("listingDB.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM listingDB WHERE id = '108061' ")    
    conn.commit()
    conn.close()
    return "Success"
