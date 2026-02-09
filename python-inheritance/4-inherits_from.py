#!/usr/bin/python3
"""
Module that provides a function to check if the object is an instance of a
class that inherited from, the specified class.
"""


def inherits_from(obj, a_class):
    """
    Function that check if the object is an instance of, or if the
    object is an instance of a class that inherited from, the specified class.
    """

    if isinstance(obj, a_class):
        if type(obj) is not a_class:
            return True
    else:
        return False
