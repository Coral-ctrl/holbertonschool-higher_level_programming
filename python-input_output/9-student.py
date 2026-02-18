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

    def to_json(self):
        """Returns dictionary representation of a Student instance."""
        return self.__dict__.copy()
