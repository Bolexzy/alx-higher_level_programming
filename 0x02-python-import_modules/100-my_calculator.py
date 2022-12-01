#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    opr = argv[2]
    if opr in ('+', '-', '*', '/'):
        if opr == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif opr == '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif opr == '*':
            print("{} - {} = {}".format(a, b, mul(a, b)))
        elif opr == '/':
            print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
