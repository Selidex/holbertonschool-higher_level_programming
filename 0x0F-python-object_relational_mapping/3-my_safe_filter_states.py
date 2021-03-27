#!/usr/bin/python3
"""Arizona is the only thing printed here"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    safe = sys.argv[4]
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states WHERE BINARY name = %s\
    ORDER BY id ASC", (safe, ))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
