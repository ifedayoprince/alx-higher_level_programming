#!/usr/bin/python3
"""
The module containing code for:
    to_json_string
"""


import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string)

    Args:
        my_obj (Any): the dictionary object
    """

    return json.dumps(my_obj)
