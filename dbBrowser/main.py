import click
from dbBrowser import create
import sqlite3

@click.command()
@click.argument('name', type=click.Path(exists=True))

def findTables(name):
    conn = sqlite3.connect(name)
    cursor = conn.cursor()   
    cursor.execute("SELECT name FROM sqlite_master\
                   WHERE type='table'\
                   ORDER BY name;")    
    output = cursor.fetchall()
    conn.close()
    print("Below are the tables in {}:".format(name))
    for tableData in output:
        print(tableData[0])
    return output

if __name__ == "__main__":
    create()
    findTables()