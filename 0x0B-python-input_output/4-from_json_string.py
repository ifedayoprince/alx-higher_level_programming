#!/usr/bin/python3
"""
The module containing code for:
    from_json_string
"""


import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string
    """

    return json.loads(my_str)
