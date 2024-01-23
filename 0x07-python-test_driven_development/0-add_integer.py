#!/usr/bin/python3
"""
Module for methods:
    - add_integer

"""


def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a: first int.
        b: second int, default value is 98.

    Raises:
        TypeError: if a, b are neither int nor float.

    Returns:
        sum of a and b.
    """

    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
