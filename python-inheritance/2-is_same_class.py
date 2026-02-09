#!/usr/bin/python3
"""
Module that provides a function to check if the object is exactly
an instance of the specified class.
"""


def is_same_class(obj, a_class):
    """
    Function that checks whether the pbject is exactly an
    instance of the specified class.
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
