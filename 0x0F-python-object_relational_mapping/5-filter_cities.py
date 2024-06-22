#!/usr/bin/python3

'''
A mysqldb module that displays a sequence of all cities
associated with the third command line argument in the
hbtn_0e_4_usa database.
'''

import MySQLdb
from sys import argv

if __name__ == "__main__":

    if len(argv) == 5:
        db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
        cur = db.cursor()
        cur.execute("SELECT cities.name FROM cities WHERE\
                cities.state_id = (SELECT states.id FROM states\
                WHERE BINARY name = %s) ORDER BY cities.id ASC", (argv[4],))
        rows = cur.fetchall()

        count = 0
        for row in rows:
            count += 1
            for element in row:
                print(element, end="")
                if count < len(rows):
                    print(', ', end="")
        print()
