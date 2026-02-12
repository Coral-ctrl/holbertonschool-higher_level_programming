#!/usr/bin/python3
"""
Module for demonstrating Abstract Base Classes in Python.
This module contains an abstract Animal class and two concrete
implementations: Dog and Cat.
"""


from abc import ABC, abstractmethod



class Animal(ABC):
    """
    Abstract base class representing an animal.
    This class cannot be instantiated directly. Subclasses must
    implement the sound method.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that should return the sound the animal makes.
        This method must be implemented by all subclasses.
        """
        pass


class Dog(Animal):
    """
    Dog class that inherits from Animal.
    Represents a dog and implements the sound method.
    """

    def sound(self):
        """Return the sound a dog makes."""
        return "Bark"


class Cat(Animal):
    """
    Cat class that inherits from Animal.
    Represents a cat and implements the sound method.
    """

    def sound(self):
        """Return the sound a cat makes."""
        return "Meow"
