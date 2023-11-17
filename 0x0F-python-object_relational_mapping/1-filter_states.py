#!/usr/bin/python3
""" Write a script that lists all states with a name starting with N (upper N)"""

import sys
import MySQLdb as obj

if __name__ == "__main__":
    conn = obj.connect(user = sys.argv[1], passwd= sys.argv[2], db= sys.argv[3], 
            host='localhost', port=3306)

    result = conn.cursor()
    result.execute("SELECT *FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    query_rows = result.fetchall()

    for row in query_rows:
        print(row)
        result.close()
        conn.close()
