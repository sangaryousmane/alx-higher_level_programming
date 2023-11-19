#!/usr/bin/python3
""" Yes, it’s an SQL injection to delete all records of a table…"""

import MySQLdb as obj
import sys

if __name__ == "__main__":

    conn = obj.connect(user=sys.argv[1], passwd=sys.argv[2],
                       db=sys.argv[3], port=3306)
    result = conn.cursor()
    result.execute("""SELECT *FROM states AS s WHERE
            s.name = %s""", (sys.argv[4]),)
    query_rows = result.fetchall()

    for row in query_rows:
        print(row)
    result.close()
    conn.close()
