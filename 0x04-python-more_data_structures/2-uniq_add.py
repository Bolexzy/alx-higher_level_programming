#!/usr/bin/python3
def uniq_add(my_list=[]):
    num = 0
    for l in set(my_list):
        num += l
    return num
