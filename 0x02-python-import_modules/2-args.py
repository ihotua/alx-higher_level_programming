#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    arg = sys.argv
    i = len(arg) - 1
    
    if i == 0:
        print("No arguments.")
    elif i == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(i))
    for j in range(1, i):
        print("{:d}: {:s}".format(j, arg[j]))
