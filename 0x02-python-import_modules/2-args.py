#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    ac = len(argv) - 1
    if (ac == 1):
        print("{} argument:".format(ac))
    elif ac == 0:
        print("{} arguments.".format(ac))
    else:
        print("{} arguments:".format(ac))

    for i in range(1, ac + 1):
        print("{}: {}".format(i, argv[i]))
