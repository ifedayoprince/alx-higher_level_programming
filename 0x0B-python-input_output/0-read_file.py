#!/usr/bin/python3
"""
the module containing code for:
    read_file
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its content to stdout.

    Args:
        filename (str): The name of the file to read.

    Returns:
        None
    """

    with open(filename, mode='r', encoding='utf-8') as file:
        print(file.read(), end='')
