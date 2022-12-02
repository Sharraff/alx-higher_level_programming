#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div


if __name__ == "__main__":
    a = int(argv[1])
    b = int(argv[3])
    sign = argv[2]
    lenght = len(argv)
    if (lenght != 3):
        print("Usage:./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if sign == '+':
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif sign == '-':
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif sign == '*':
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    elif sign == '/':
        print("{:.0f} / {:.0f} = {:.0f}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and / ")
        exit(1)
