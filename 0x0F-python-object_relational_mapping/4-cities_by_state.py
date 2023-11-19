#!/usr/bin/python3
""" Write a script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb as obj
import sys

if __name__ == "__main__":
    
    conn = obj.connect(user=sys.argv[1], passwd=sys.argv[2],
                   db=sys.argv[3], port=3306)
    result = conn.cursor()
    result.execute("""SELECT c.id, c.name, s.name FROM states s, cities c
            WHERE c.state_id = s.id ORDER BY c.id ASC""")

    query_rows = result.fetchall()
    
    for row in query_rows:
        print(row)
    result.close()
    conn.close()
