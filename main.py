"""
ETL-Query script
"""
from mylib.create import create
from mylib.query import query

# Create
print("Creating database...")
create()
print("Querying database...")
print(query())