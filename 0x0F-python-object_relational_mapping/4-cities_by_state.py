#!/usr/bin/python3
"""
script that list all cities from
the the database htbn_0e_0_usa
This script should take 3 arguments:
mysql username, mysql password,
database name and state name searched
"""

from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect("localhost", *argv[1:4], 3306)
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name\
, states.name FROM cities JOIN states ON cities.state_id = states.id\
 ORDER BY cities.id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
