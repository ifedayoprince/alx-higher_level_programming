#!/usr/bin/python3
"""the module containing 'Rectangle' class

    Raises:
        TypeError: width and height should be integers
        ValueError: width and height should be greater than 0
        TypeError: rect_1 and rect_2 must be instances of `Rectange`
"""


class Rectange:
    """the rectange class with methods used:
        - Creating a rectangle
        - Setting its size
        - Printing it
     """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        out_rect = ""
        for y in range(self.__height):
            for x in range(self.__width):
                out_rect += "#"
            if not y == (self.__height - 1):
                out_rect += "\n"
        return out_rect

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
