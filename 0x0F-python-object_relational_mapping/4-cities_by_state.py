#!/usr/bin/python3

'''
A mysqldb module that lists all cities with their respective
states in the hbtn_0e_4_usa database.
'''

import MySQLdb
from sys import argv

if __name__ == "__main__":

    if len(argv) == 4:
        db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
        cur = db.cursor()
        cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities JOIN states ON\
                states.id = state_id ORDER BY cities.id ASC")
        rows = cur.fetchall()
        for row in rows:
            print(row)
