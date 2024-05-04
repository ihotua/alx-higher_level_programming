#!/usr/bin/python3
"""
Log Parsing and Statistics Computation Script

This script reads HTTP GET request results from stdin and computes metrics such as total file size and the number of lines by status code.

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

Each 10 lines and after a keyboard interruption (CTRL + C), it prints statistics since the beginning:
- Total file size: File size: <total size>
- Number of lines by status code:
  - Status codes: 200, 301, 400, 401, 403, 404, 405, and 500
  - Format: <status code>: <number>
  - Status codes are printed in ascending order.

Usage:
$ cat log_file.txt | ./log_stats.py
"""


from sys import stdin
from collections import defaultdict

def print_statistics(file_size, status_codes):
    """
    Print statistics including total file size and number of lines by status code.

    Args:
        file_size (int): Cumulative total of bytes received through GET requests in log.
        status_codes (dict): Totals of status codes from responses.
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
