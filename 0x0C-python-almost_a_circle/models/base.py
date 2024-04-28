#!/usr/bin/python3

"""Base Class Module"""


class Base:
    """Base class for other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class Constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
