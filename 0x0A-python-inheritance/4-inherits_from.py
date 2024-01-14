#!/usr/bin/python3
"""
the module containig the function:
    - inherits_from
"""


def inherits_from(obj, a_class):
    """
    checks if the object is an instance of a class
    that inherited (directly or indirectly)
    from the specified class.

    Params:
        - obj: the object to check
        - a_class: the class to check against

    Returns:
        - True
        - False
    """

    return issubclass(type(obj), a_class)


a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))
