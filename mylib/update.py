import sqlite3

def update():
    """Update content of database"""
    conn = sqlite3.connect("listingDB.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE listingDB SET bedrooms = 'one'\
                    WHERE bedrooms = '1' ")    
    conn.commit()
    conn.close()
    return "Success"
