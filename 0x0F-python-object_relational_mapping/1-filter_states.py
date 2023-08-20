#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N) from
the database hbtn_0e_0_usa
This script should take 3 arguments:
mysql username, mysql password and database name
"""
from sys import argv
import MySQLdb


def main():
    db = MySQLdb.connect("localhost", *argv[1:4], 3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()