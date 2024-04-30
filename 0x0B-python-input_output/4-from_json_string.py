#!/usr/bin/python3
"""0x0B. Python -Input/Output, task 4.From JSON string to Object"""


import json


def from_json_string(my_str):
    """Converts a JSON string to a Python object."""
    return json.loads(my_str)
