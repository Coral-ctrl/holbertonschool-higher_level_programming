#!usr/bin/python3
"""
Module for demonstrating multiple inheritance in Python.
Contains Fish and Bird classes, and a FlyingFish class
that inherits from both.
"""


class Fish:
    """A class representing a fish."""

    def swim():
        """print a message"""
        print("The fish is swimming")

    def habitat():
        """print a message"""
        print("The fish lives in water")


class Bird:
    """A class representing a bird."""

    def fly():
        """print a message"""
        print("The bird is flying")

    def habitat():
        """print a message"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A class representing a flying fish that inherits from both."""

    def fly(self):
        """print a new message"""
        print("The flying fish is soaring!")

    def swim(self):
        """print a new message"""
        print("The flying fish is swimming!")

    def habitat(self):
        """print a new message"""
        print("The flying fish lives both in water and the sky!")
