#!/usr/bin/python3

'''
A mysqldb module that lists all states begining with
capital 'N' from the database hbtn_0e_0_usa
'''

import MySQLdb
from sys import argv

if __name__ == "__main__":

    if len(argv) == 4:
        db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
        cur = db.cursor()
        # cur.execute("SELECT * FROM states\
        # WHERE BINARY name LIKE 'N%' ORDER BY id ASC")
        cur.execute("SELECT * FROM states WHERE\
                ASCII(left(name, 1)) = ASCII('N') ORDER BY id ASC")
        rows = cur.fetchall()
        for row in rows:
            print(row)
