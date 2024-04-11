#!/usr/bin/python3
"""Empty class Rectangle that defines a Rectangle"""


class Rectangle:
    """
    Class representing a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"
    
    def __init__(self, width=0, height=0):
        """
        Instantiation with optional width and height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        Retrieve area
        """
        return (self.width * self.height)

    def perimeter(self):
        """
        Retrieve perimeter
        """
        return (2 * (self.width + self.height)
                if self.width != 0 and self.height != 0 else 0)

    def __str__(self):
        """
        return the rectangle with the character #
        """
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return ('\n'.join(['#' * self.width] * self.height))

    def __repr__(self):
        """
        Return string representation of the rectangle
        """
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """
        Deletes an instance of a class
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
