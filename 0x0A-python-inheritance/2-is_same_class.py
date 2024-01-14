#!/usr/bin/python3
"""
module containing definition for the functions:
    - is_same_class
"""


def is_same_class(obj, a_class):
    """
    checks if the ``obj`` is of the type ``a_class``.

    Params:
        - obj: the object to check.
        - a_class: the class to check against.
    """

    return issubclass(type(obj), a_class) and type(obj) != a_class
