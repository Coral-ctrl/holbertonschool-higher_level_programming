#!/usr/bin/python3
"""
Module for demonstrating Abstract Base Classes in Python.
This module contains an abstract Shape class and two concrete
implementations: Circle and Rectangle.
"""


from abc import ABC, abstractmethod
import math


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
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate the perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Concrete implementation of a Rectangle shape."""

    def __init__(self, width, height):
        """Initialize a Rectangle with given width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print information about a shape using duck typing.

    This function doesn't check the type of the shape. It simply calls
    the area() and perimeter() methods, trusting that the object has them.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
