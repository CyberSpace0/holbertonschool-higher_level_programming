#!/usr/bin/python3
"""List all states from the database in ascending order by their IDs."""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    row = cur.fetchall()
    for i in row:
        print(i)

    cur.close()
    db.close()
