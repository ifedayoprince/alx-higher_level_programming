#!/usr/bin/python3
"""
module containing definiton for:
    - class Rectangle
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """a rectangle class that inherits from class BaseGeometry
    """

    def __init__(self, width, height):
        """
        initalization function

        Params:
            - self: this instance
            - width: width of rectangle
            - height: height of rectangle
        """

        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
        calculate the area of the rectangle
        """

        return self.__width * self.__height

    def __str__(self):
        """
        the string representation
        """

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
