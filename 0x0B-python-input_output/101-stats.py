#!/usr/bin/python3
"""
Log Parsing and Statistics Computation Script
"""


from sys import stdin
from collections import defaultdict


def print_statistics(file_size, status_codes):
    """
    Print stats plus total file size & no of lines by status code
    """

    print("File size:", file_size)
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def main():
    line_num = 0
    file_size = 0
    status_codes = defaultdict(int)

    try:
        for line in stdin:
            line_num += 1
            split_line = line.split()

            if len(split_line) > 1:
                file_size += int(split_line[-1])

            if len(split_line) > 2 and split_line[-2].isnumeric():
                status_code = split_line[-2]
                status_codes[status_code] += 1

            if line_num % 10 == 0:
                print_statistics(file_size, status_codes)

        print_statistics(file_size, status_codes)

    except KeyboardInterrupt:
        print_statistics(file_size, status_codes)
        raise


if __name__ == '__main__':
    main()
