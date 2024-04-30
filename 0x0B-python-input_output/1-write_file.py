#!/usr/bin/python3
"""0x0B-python-input_output Task 1: Append to a file"""


def write_file(filename="", text=""):
    """Writes a string to a UTF-8 and returns the number of xters"""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
        return len(text)
