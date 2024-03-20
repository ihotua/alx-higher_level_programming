#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    arg = sys.argv
    i = len(arg)

    if i == 1:
        print("No arguments.")
    else:
        print("{:d} argument".format(i - 1), end="")
        if i > 2:
            print("s", end="")
        print(":")
        for j in range(1,i)):
            print("{:d}: {:s}".format(i, arg[j]))
