#!/usr/bin/python3
"""0X0B. Python - Input/Output, task 14. Log parsing"""


import sys


def print_metrics(total_size, status_counts):
    """Print metrics to the console"""
    print("File size:", total_size)
    for status_code, count in sorted(status_counts.items()):
        print(f"{status_code}: {count}")


def parse_line(line):
    """Parse a log line and return file size and status code"""
    try:
        parts = line.split()
        if len(parts) < 9:
            return None, None
        return int(parts[-1]), parts[-2]
    except Exception as e:
        print(f"Error parsing line: {line}. Error: {e}")
        return None, None


def main():
    """Main entry point"""
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0,
            403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            file_size, status_code = parse_line(line)
            if file_size is not None and status_code is not None:
                total_size += file_size
                status_counts[int(status_code)] += 1
            line_count += 1
            if line_count % 10 == 0:
                print_metrics(total_size, status_counts)
    except KeyboardInterrupt:
        print_metrics(total_size, status_counts)


if __name__ == "__main__":
    main()
