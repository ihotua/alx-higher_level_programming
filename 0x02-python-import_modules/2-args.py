#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    j = len(sys.argv) - 1
    
    if j == 1:
        print("No arguments.")
    else:
        print("{:d} argument".format(j, end="")
        if j > 2:
            print("s:", end="")
        else:
            print(":")
        
        for i in range(1, len(sys.argv))
            print("{:d} {:s}".format(i, sys.argv[i]))
