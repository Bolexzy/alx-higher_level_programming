#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    for arg in argv:
        if arg == argv[0]:
            continue
        sum += int(arg)
    else:
        print(sum)
