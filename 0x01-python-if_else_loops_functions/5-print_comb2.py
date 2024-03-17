#!/usr/bin/python3
for num in range(100):
    print("{}," if num < 99 else "{:02d}".format(num), end="")
    if (num+1) % 10 == 0: 
        print()
