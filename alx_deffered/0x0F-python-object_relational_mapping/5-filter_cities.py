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
    if len(args) < 4:
        print("Usage: {} username password database_name".format(args[0]))
        exit(1)
    username = args[1]
    password = args[2]
    data = args[3]
    db = MySQLdb.connect(host='localhost', user=username,
            passwd=password, db=data, port=3306)
    cur = db.cursor()
    num_rows = cur.execute("SELECT cities.names FROM cities WHERE state_id =\
            (SELECT id FROM states WHERE name LIKE BINARY %s)\
            ORDER BY cities.id;", (state_name, ))
    rows = cur.fetchall()
    i = 1
    for row in rows:
        print(row[0], end='')
        if i < num_rows:
            print(end=', ')
        i += 1
    print()
    cur.close()
    db.close()
