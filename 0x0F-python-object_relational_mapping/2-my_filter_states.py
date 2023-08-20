#!/usr/bin/python3
"""
script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa
where name matches the argument.
This script should take 3 arguments:
mysql username, mysql password,
database name and state name searched
"""

from sys import argv
import MySQLdb


if __name__ == "__main__":
    st_name = argv[4]
    db = MySQLdb.connect("localhost", *argv[1:4], 3306)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE\
        BINARY '{:s}' ORDER BY states.id".format(st_name)
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
