#!/usr/bin/python3
"""
The module containing code for:
    load_from_json_file
"""


import json


def load_from_json_file(filename):
    """
    Creates an Object from a “JSON file”

    Args:
        filename (str): The name of the file to load from.

    Returns:
        Any: The object deserialized from the JSON file.
    """

    with open(filename, "r") as file:
        return json.load(file)
