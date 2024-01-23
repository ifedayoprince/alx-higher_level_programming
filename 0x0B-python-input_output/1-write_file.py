#!/usr/bin/python3
"""
the module containing code for:
    write_file
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and
    returns the number of characters written.

    Args:
        filename (str): The name of the file to write.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written.
    """

    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
