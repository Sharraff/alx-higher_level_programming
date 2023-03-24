#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
created on 19 march 2023
@author: Musharraff Ibrahim
"""


def main(args):
    # gets state stuff by N
    if len(args) != 4:
        raise Exception("need 3 arguments!")
    db = MySQLdb.connect(host='localhost',
                         user=args[1],
                         passwd=args[2],
                         db=args[3])
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name like binary 'N%' ORDER BY id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)

if __name__ == "__main__":
    import sys
    import MySQLdb
    main(sys.argv)
