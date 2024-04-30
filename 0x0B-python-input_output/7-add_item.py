#!/usr/bin/python3
"""0x0B. Python - Input/Output, task 7. Load, add, save"""


import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

try:
    data = load_from_json_file("add_item.json")
except FileNotFoundError:
    data = []
