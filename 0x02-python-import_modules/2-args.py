#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    j = len(sys.argv) - 1
    
    if j == 1:
        print("No arguments.")
    else:
        print("{:d} argument".format(j + 1), end="")
        if j > 2:
            print("s:", end="")
        else:
            print(":")
        
        for i in range(1, j + 1)):
            print("{:d}: {:s}".format(i, sys.argv[i]))
