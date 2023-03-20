#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import MySQLdb
import sys

"""
created on 19 march 2023
@author: Musharraff Ibrahim
"""


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 4:
        print("Usage: {} username password database_name".format(args[0]))
        exit(1)
    username = args[1]
    password = args[2]
    data = args[3]
    db = MySQLdb.connect(host='localhost', user=username,
            passwd=password, db=data, port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE states.name LIKE BINARY\
            '%N' ORDER BY states.id;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
