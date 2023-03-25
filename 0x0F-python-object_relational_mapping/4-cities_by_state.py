#!/usr/bin/python3
"""
Script displays cities in cities table
in a database.
argv[1] -> user
argv[2] -> password
argv[3] -> the database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
         passwd=argv[2], db=argv[3])

    curs = db.cursor()
    curs.execute("SELECT cities.id, cities.name, states.name FROM states\
                  INNER JOIN cties ON states.id = cities.states_id
                  ORDER BY cities.id ASC")
    for row in curs.fetchall():
        print(row)

    curs.close()
    db.close()
