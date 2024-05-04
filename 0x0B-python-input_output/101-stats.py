#!/usr/bin/python3
"""0X0B. Python - Input/Output, task 14. Log parsing"""


from collections import defaultdict
import sys

def print_statistics(total_file_size, status_counts):
    """Prints the total file size and status code counts."""
    print("Total file size:", total_file_size)
    for status_code, count in sorted(status_counts.items()):
        if count > 0:
            print(f"Number of lines with status code {status_code}: {count}")

def parse_log_line(line):
    """
    Parses a log line and extracts the file size and status code.
    """
    parts = line.split()
    if len(parts) < 9:
        return None, None
    return int(parts[-1]), int(parts[-2])

def main():
    """
    Main function to read stdin, parse log lines, and calculate statistics.
    """
    total_file_size = 0
    status_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            file_size, status_code = parse_log_line(line)
            if file_size is not None and status_code is not None:
                total_file_size += file_size
                status_counts[status_code] += 1
            line_count += 1
            if line_count % 10 == 0:
                # Print statistics every 10 lines
                print_statistics(total_file_size, status_counts)
    except KeyboardInterrupt:
        # If interrupted, print final statistics
        print_statistics(total_file_size, status_counts)

if __name__ == "__main__":
    main()
