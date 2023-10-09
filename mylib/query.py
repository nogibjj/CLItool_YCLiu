"""Query the database"""

import sqlite3


# Now you can run queries like this:

def query():    
    conn = sqlite3.connect("Transactions.db")
    cursor = conn.cursor()   
    cursor.execute("SELECT t1.cust_id, t1.name, t1.sex,\
                           SUM(t2.amount) AS total_amount \
                   FROM Customer t1\
                   INNER JOIN TXR t2\
                   ON t1.cust_id = t2.cust_id\
                   WHERE t1.sex ='Female'\
                   GROUP BY t1.cust_id\
                   ORDER BY total_amount DESC")    

    output = cursor.fetchall()
    conn.close()
    return output
print(query())