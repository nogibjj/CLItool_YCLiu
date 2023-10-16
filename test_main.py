import sqlite3

def testMain(name):
    conn = sqlite3.connect(name)
    cursor = conn.cursor()   
    cursor.execute("SELECT name FROM sqlite_master\
                   WHERE type='table'\
                   ORDER BY name;")    
    output = cursor.fetchall()
    conn.close()
    assert len(output) == 2
    assert output[0][0] == "Customer"
    assert output[1][0] == "TXR"
    return "Success"

if __name__ == '__main__':
    testMain('Transactions.db')
    pass