#!/usr/bin/python3
"""
The module containing code for:
    save_to_json_file
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj (Any): The Python object.
        filename (str): The file name.
    """

    with open(filename, mode="w") as file:
        json.dump(my_obj, file)
