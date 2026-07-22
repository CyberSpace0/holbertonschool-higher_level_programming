#!/usr/bin/python3
""" select state """

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3])
    cur = db.cursor()
    cur.execute("select * from states order by id asc")
    row = cur.fetchall()
    for i in row:
        print(i)

    cur.close()
    db.close()
