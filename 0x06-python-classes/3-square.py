#!/usr/bin/python3
"""
The module containing code for the:
    class Square
"""


class Square:
    """
    The Square class.
    """

    def __init__(self, size=0):
        """The initialization method.

        Args:
            size (int): The size of the square.
        """

        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """

        return self.__size ** 2
