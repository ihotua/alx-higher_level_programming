#!/usr/bin/python3
for num in range(100):
    if num < 99:
        print("{:02d}".format(num), else "{:02d}".format(num), end="")
    if (num+1) % 10 == 0:
        print()
