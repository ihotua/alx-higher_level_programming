#!/usr/bin/python3
"""0x0B. Python - Input/Output, task 2. Append to a file """


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF-8 text file"""
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
