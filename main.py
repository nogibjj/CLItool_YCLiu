"""
ETL-Query script
"""
from mylib.delete import delete
from mylib.extract import extract
from mylib.query import query
from mylib.transform_load import load
from mylib.update import update

# Extract
print("Extracting data...")
extract()

# Transform and load
print("Transforming data...")
load()

# Query
print("Querying data...")
print(query())

# Update
print("Updating data...")
update()

# Query
print("Querying data...")
print(query())

# Delete
print("Deleting data...")
delete()

# Query
print("Querying data...")
print(query())
