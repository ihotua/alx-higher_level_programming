#!/usr/bin/python3
def uppercase(str):
    for c in str:
        upper_c = chr(ord(c) - 32) if 97 <= ord(c) <= 122 else c
        print("{}".format(upper_c), end="")
    print()
