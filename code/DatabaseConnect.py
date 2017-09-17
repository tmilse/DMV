"""
Created on Sun Sep 17 11:15:45 2017

@author: NKallfa

Description: Example code to connect and interact with remote PostgreSQL database
"""

# Import package to connect to PostgreSQL database
# Might need to do "pip install psycopg2" OR "conda install psycopg2" to download the package
import psycopg2

# Connect to an existing database
conn = psycopg2.connect(dbname="postgres", user="nick", password="nick", host="104.131.45.55", port=5432)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute("CREATE TABLE nicktest (id serial PRIMARY KEY, num integer, data varchar);")

# Execute another command. This inserts a row in the table we just created
cur.execute("INSERT INTO nicktest (num, data) VALUES (%s, %s)", (100, "Text"))

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()