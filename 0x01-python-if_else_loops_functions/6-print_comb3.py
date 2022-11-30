#!/usr/bin/python3.8
for num in range(1, 100):
    if (num / 10) > (num % 10):
        continue
    if num == 89:
        print("{:02d}".format(num))
    else:
        print("{:02d}".format(num), end=', ')
