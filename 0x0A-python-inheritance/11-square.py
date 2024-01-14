#!/usr/bin/python3
"""
the module containing code for:
    - class Square
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """the square class
    """

    def __init__(self, size):
        """
        the class initialization

        Params:
            - self: this instance
            - size: the size of the rectangle
        """

        super().integer_validator("size", size)

        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """string representation
        """

        return "[Square] {}/{}".format(self.__size, self.__size)
