#!/usr/bin/python3
"""
Module that defines a custom list class with a sorted print method.
"""

class MyList(list):
    """
    MyList class that inherits from the built-in list.
    """


    def print_sorted(self):
        """
        Print the list in ascending sorted order without modifying
        the original list.
        """
        print(sorted(self))
