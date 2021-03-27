#!/usr/bin/python3
import MySQLdb
import sys


if __name__ == "__main__":
    MY_HOST = "localhost"
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    test = sys.argv[4]
    db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states WHERE name = '{}' \
    ORDER BY id ASC".format(test))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
