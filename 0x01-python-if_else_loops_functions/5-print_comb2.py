#!/usr/bin/python3.8
for num in range(0, 100):
    if num == 99:
        print("{:02d}".format(num))
        continue
    print("{:02d}".format(num), end=", ")
