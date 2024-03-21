#!/usr/bin/python3
if __name__ == "__main__":
    import sys
        i = len(sys.argv)
    if i == 1:
        print("0 arguments.")
    else:
        print("{:d} argument".format(i - 1), end="")
        if i > 2:
            print("s", end="")
        print(":")
        for j in range(1, i)):
            print("{:d}: {:s}".format(j, sys.argv[j]))
