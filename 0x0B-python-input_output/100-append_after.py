#!/usr/bin/python3
"""0x0B. Python - Input/Output, task 13. Search and update"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after each line containing a
    specific string in a file.
    """
    read = []
    with open(filename, "r", encoding="utf-8") as f:
        read = f.readlines()
        index = 0

        while index < len(read):
            if search_string in read[index]:
                read.insert(index + 1, new_string)
                index += 1
            index += 1

    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(read)

