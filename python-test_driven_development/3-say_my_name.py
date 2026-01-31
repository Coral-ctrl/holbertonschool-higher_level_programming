#!/usr/bin/python3
"""Module for say_my_name function."""

def say_my_name(first_name, last_name=""):
    """Print a name in the format 'My name is <first name> <last name>'.
    
    Args:
        first_name: First name (must be a string)
        last_name: Last name (must be a string), default is empty string
    
    Raises:
        TypeError: If first_name is not a string
        TypeError: If last_name is not a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
