#!/usr/bin/python3

'''
A mysqldb module that lists all states in the hbtn_0e_0_usa
database, that matches the fourth command line argument.
'''

import MySQLdb
from sys import argv

if __name__ == "__main__":

    if len(argv) == 5:
        db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
        cur = db.cursor()
        cur.execute("SELECT * FROM states\
                WHERE BINARY name = '{}' ORDER BY id ASC".format(argv[4]))
        rows = cur.fetchall()
        for row in rows:
            print(row)
