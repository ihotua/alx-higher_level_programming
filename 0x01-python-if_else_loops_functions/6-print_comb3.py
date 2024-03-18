#!/usr/bin/python3
for f in range(10):
    for g in range(f+1, 10):
        if f != 9 or g != 8:
            print("{:02d}, ".format(num), end='')
        else:
            print("{:02d}".format(num))
