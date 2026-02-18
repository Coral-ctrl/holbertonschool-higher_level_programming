#!/usr/bin/python3
"""Module that contains a class Student."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance with first name,
        last name, and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns dictionary representation of a Student instance.
        If attrs is a list of strings, only attribute names contained
        in this list must be retrieved.
        Otherwise, all attributes must be retrieved
        """
        obj_dict = self.__dict__.copy()

        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            filtered_dict = {key: value for key, value in obj_dict.items() if key in attrs}
            return filtered_dict
        return obj_dict

