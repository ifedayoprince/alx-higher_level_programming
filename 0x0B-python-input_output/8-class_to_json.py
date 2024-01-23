#!/usr/bin/python3
"""
The module containing code for:
    class_to_json
"""


def class_to_json(obj):
    """
    Returns the dictionary description with
    simple data structure (list, dictionary,
    string, integer and boolean) for JSON
    serialization of an object.

    Args:
        obj: The class to be converted to JSON.

    Return:
        dict: The dictionary description of a data structure.
    """

    return obj.__dict__
