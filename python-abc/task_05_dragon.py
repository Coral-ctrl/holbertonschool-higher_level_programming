#!usr/bin/python3
"""
Module for representing mixins in Python.
Contains SwimMixin and FlyMixin classes that provide
specific behaviours, and a Dragon class that combines both.
"""


class SwimMixin:
    """A mixin class that provides swimming capability."""

    def swim(self):
        """print a message"""
        print("The creature swims!")


class FlyMixin:
    """A mixin class that provides flying capability."""

    def fly(self):
        """print a message"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A Dragon class that inherits from both SwimMixin and FlyMixin."""

    def roar(self):
        """print a message"""
        print("The dragon roars!")
