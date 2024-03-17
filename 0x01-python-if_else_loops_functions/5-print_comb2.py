#!/usr/bin/python3
for num in range(100):
    print("{}," if num < 99 else "{}".format(num), end="")
    if (num+1) % 10 == 0: print()
