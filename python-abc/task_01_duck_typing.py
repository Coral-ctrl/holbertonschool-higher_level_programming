#!/usr/bin/python3
"""
Module for demonstrating Abstract Base Classes in Python.
This module contains an abstract Shape class and two concrete
implementations: Circle and Rectangle.
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract base class representing a shape."""

    @abstractmethod
    def area(self):
        """Abstract method that should return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method that should return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Concrete implementation of a Circle shape."""

    def __init__(self, radius):
        """Initialize a Circle with a given radius."""
        self.__radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return pi * (abs(self.__radius) ** 2)

    def perimeter(self):
        """Calculate the perimeter of the circle."""
        return 2 * pi * abs(self.__radius)


class Rectangle(Shape):
    """Concrete implementation of a Rectangle shape."""

    def __init__(self, width, height):
        """Initialize a Rectangle with given width and height."""
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.__width + self.__height)


def shape_info(obj):
    """
    Print information about a shape using duck typing.

    This function doesn't check the type of the shape. It simply calls
    the area() and perimeter() methods, trusting that the object has them.
    """
    try:
        print("Area: {}".format(obj.area()))
        print("Perimeter: {}".format(obj.perimeter()))
    except Exception:
        print("Shape information error")
