#!/usr/bin/python3
"""Empty class Rectangle that defines a Rectangle"""


class Rectangle:
    """
    Class representing a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Instantiation with optional width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieve the width
        """
        return (self.__width)

    @property
    def height(self):
        """
        Retrieve the height
        """
        return (self.__height)

    @width.setter
    def width(self, value):
        """
        Set the width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """
        Set the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
