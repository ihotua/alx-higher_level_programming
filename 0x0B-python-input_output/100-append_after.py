#!/usr/bin/python3
"""0x0B. Python - Input/Output, task 13. Search and update"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after each line containing a
    specific string in a file.
    """
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        file.truncate()
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + '\n')
