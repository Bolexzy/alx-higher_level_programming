#!/usr/bin/python3
def magic_string(l=[]):
    magic_string.count = getattr(magic_string, "count", 0) + 1
    return ("BestSchool, " * (magic_string.count - 1) + "BestSchool")
