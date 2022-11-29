#!/usr/bin/python3


def uppercase(str):
    for c in str:
        stg = ord(c)
        if stg >= 97 and stg <= 122:
            stg -= 32
        else:
            print("{:c}".format(stg), end="")
    print()
