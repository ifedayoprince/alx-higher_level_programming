#!/usr/bin/python3
"""
the module containing the method:
    - lookup
"""


def lookup(obj):
    """
    function that returns the list of available
    attributes and methods of an object.

    Params:
        - obj: the object to be scanned
    """

    return dir(obj)
