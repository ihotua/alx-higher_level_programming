#!/usr/bin/python3
"""
0x0B. Python - Input/Output, task 10. Student to JSON with filter
"""


class Student:
    """Simple class containing student data."""
    def __init__(self, first_name, last_name, age):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Public method Retrieves a dictionary representation of a
        Student instance
        """
        if (isinstance(attrs, list) and
                all(isinstance(x, str) for x in attrs)):
            return {x: getattr(self, x) for x in attrs 
                    if hasattr(self, x)}
        return (self.__dict__)
