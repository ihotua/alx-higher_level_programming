#!/usr/bin/python3
"""
0x0B. Python - Input/Output, task 11. Student to disk and reload
"""


class Student:
    """Simple class containing student data."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return (self.__dict__)
        else:
            attributes = {}
            for attr_name in attrs:
                if hasattr(self, attr_name):
                    attributes[attr_name] = getattr(self, attr_name)
            return attributes

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
