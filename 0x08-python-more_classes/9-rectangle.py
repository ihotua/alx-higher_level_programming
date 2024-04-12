#!/usr/bin/python3
"""Empty class Rectangle that defines a Rectangle"""


class Rectangle:
    """Class representing a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Set the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieve the height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Set the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Retrieve area"""
        return (self.width * self.height)

    def perimeter(self):
        """Retrieve perimeter"""
        return ((2 * (self.width + self.height)
                if self.width != 0 and self.height != 0 else 0))

    def __str__(self):
        """Return the rectangle with the character specified in print_symbol"""
        if self.width == 0 or self.height == 0:
            return ("")
        else:
            return ('\n'.join([str(self.print_symbol)
                    * self.width] * self.height))

    def __repr__(self):
        """Return string representation of the rectangle"""
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """Deletes an instance of a class"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Computes and compares the area of two rectangles"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
    """Creates a square instance of Rectangle"""
        return (Rectangle(size, size))
