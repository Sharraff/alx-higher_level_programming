#!/usr/bin/python3
# gets all states via python yee boi with your own state
import MySQLdb
from sys import argv


if __name__ == "__main__":
    # gets all state stuff by N
    if len(args) != 5:
        raise Exception("need 4 arguments!")
    db = MySQLdb.connect(host='localhost',
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM WHERE name LIKE '{:s}' ORDER BY id ASC"
        .format(args[4]))
    states = cur.fetchall()
    for state in states:
        if state[1] == argv4]:
            print(state)
    cur.close()
    db.close()
