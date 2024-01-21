#!/usr/bin/python3
"""
The module containing code for:
    magic_string
"""


magic_called = 1

def magic_string():
    """
    Prints a string the number of times the function was called.

    Return:
        str: the line of "Best School" to print.
    """
    
    if not hasattr(magic_string, "count"):
        magic_string.count = 0
    else:
        magic_string.count += 1
    return "BestSchool" + ", BestSchool" * magic_string.count



for i in range(10):
    print(magic_string())
