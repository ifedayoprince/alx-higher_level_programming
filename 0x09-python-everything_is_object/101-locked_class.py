#!/usr/bin/python3

"""Module containing code for:
    class LockedClass
"""


class LockedClass:
    """
    LockedClass: Prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name.
    """

    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
        super().__setattr__(name, value)
