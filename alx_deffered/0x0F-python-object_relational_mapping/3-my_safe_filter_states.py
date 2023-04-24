#!/usr/bin/python3

"""
Script displays states in a table in a database
with search filter
argv[1] should be user to access db
argv[2] should be password to access db
argv[3] should be the database
argv[4] is  search term
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    curs = db.cursor()
    curs.execute("SELECT * FROM states WHERE name='{}' ORDER BY id ASC"
                  .format(argv[4]))

    for row in curs.fetchall():
        if row[1] == argv[4]:
            print(row)
    curs.close()
    db.close()
