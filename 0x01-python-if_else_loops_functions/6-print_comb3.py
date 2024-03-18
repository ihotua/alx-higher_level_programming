#!/usr/bin/python3
for f in range(10):
    for g in range(f+1, 10):
        if f != g:
            print("{}{}, ".format(f, g), end="")
print()
