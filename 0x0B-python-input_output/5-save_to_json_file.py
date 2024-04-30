#!/usr/bin/python3
"""0x0B. Python - Input/Output, task 5. Save Object to a file  """


import json


def save_to_json_file(my_obj, filename):
    """Writes a Python object to a text file in JSON format."""
    with open(filename, 'w', encoding= 'utf-8') as file:
        json.dump(my_obj, file)
