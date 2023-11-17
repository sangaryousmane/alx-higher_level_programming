#!/usr/bin/python3
""" Write a script that lists all states with a name starting with N (upper N)"""

import MySQLdb as obj

conn = obj.connect(host="localhost", user="root", passwd="root", db="hbtn_0e_0_usa")

result = conn.cursor()
result.execute("SELECT *FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
query_rows = result.fetchall()
for row in query_rows:
    print(row)
result.close()
conn.close()
