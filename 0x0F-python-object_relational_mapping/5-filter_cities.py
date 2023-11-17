#!/usr/bin/python3
""" Yes, it’s an SQL injection to delete all records of a table…"""

import sys
import MySQLdb as obj


if __name__ == "__main__":
    conn = obj.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], host='localhost', port=3306)

    result = conn.cursor()
    sql_statement = ("""
    SELECT c.name FROM cities AS c, states s WHERE s.name %s AND c.state_id==s.id
    ORDER BY c.id ASC""", (sys.argv[4],)

    query_rows = result.execute(sql_statement).fetchall()

    for row in query_rows:
        print(','.join(row[0]))
    result.close()
    conn.close()
