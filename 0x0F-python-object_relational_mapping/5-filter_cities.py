#!/usr/bin/python3
"""Arizona is the only thing printed here"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    state = sys.argv[4]
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
    INNER JOIN states ON cities.state_id = states.id WHERE states.name = %s",
                (state, ))
    query_rows = cur.fetchall()
    st = ""
    for row in query_rows:
        if st != "":
            st += ", "
        st += row[0]
    print(st)
    cur.close()
    db.close()
