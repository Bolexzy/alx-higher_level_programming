#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for item in range(x):
        try:
            print(my_list[item], end='')
            count += 1
        except IndexError:
            break
    print()
    return count
