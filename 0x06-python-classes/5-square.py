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

    @property
    def size(self):
        """Returns the size of the square.

        Returns:
            int: The size of the square.
        """

        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The size of the square.
        """

        if not type(value) is int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints the square using '#' characters.
        """

        rows = []

        for _ in range(self.__size):
            rows.append("#" * self.__size)

        print("\n".join(rows))
