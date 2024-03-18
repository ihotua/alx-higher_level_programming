#!/usr/bin/python3
for f in range(10):
    for g in range(f+1, 10):
        if f == 8 and g == 9:
            print("{}{}".format(f, g))
        else:
            print("{}{}".format(f, g), end=", ")
