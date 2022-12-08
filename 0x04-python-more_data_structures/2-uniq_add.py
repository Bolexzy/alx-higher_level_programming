#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    if len(my_list) == 0:
        return sum
    for l in set(my_list):
        sum += l
    return sum
