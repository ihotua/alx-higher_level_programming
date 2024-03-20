#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    num_args = len(sys.argv) - 1
    
    if num_args == 0:
        print("0 arguments.")
    else:
        print("{:d} argument".format(num_args), end="")
        if num_args > 1:
            print("s:", end="")
        else:
            print(":")
        
        for i in range(1, len(sys.argv)):
            print("{:d}: {:s}".format(i, sys.argv[i]))
