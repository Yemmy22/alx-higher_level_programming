#!/usr/bin/python3

'''
A mysqldb module that lists all
states from the database hbtn_0e_0_usa
'''

import MySQLdb
from sys import argv

if __name__ == "__main__":

    if len(argv) == 4:
        db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
        cur = db.cursor()
        cur.execute("SELECT * FROM states ORDER BY id;")
        rows = cur.fetchall()
        for row in rows:
            print(row)
