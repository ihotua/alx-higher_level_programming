#!/usr/bin/python3
"""0x0B. Python - Input/Output,Task O. Read file"""


def read_file(filename=""):
    """ function that reads a text file and prints it to stdout """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
