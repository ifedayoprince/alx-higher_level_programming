#!/usr/bin/python3
"""
the module containing the functions:
    - is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    if the object is an instance of, or if
    the object is an instance of a class that
    inherited from the specified class.

    Params:
        - obj: the object to check
        - a_class: the class to check against

    Returns:
        - True
        - False
    """

    return isinstance(obj, a_class)
