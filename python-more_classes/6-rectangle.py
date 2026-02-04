#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Represents a rectangle.

    Class Attributes:
        number_of_instances (int): Counts current Rectangle instances.

    Attributes:
        __width (int): width of rectangle
        __height (int): heightrectangle
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance and increment instance counter.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
            Retrieves the width of the rectangle.

        Returns:
            int: The width of the resctangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle with validation.

        Args:
            value (int): New width of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.

        Returns:
            int: The height of the resctangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the width of the rectangle with validation.

        Args:
            value (int): New height of the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Computes and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Computes and returns the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return the string representation of the rectangle using '#'.

        Returns:
            str: Rectangle drawn with '#', or empty string if width
                 or height id 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        lines = []
        for i in range(self.__height):
            lines.append("#" * self.__width)
        return "\n".join(lines)

    def __repr__(self):
        """
        Return a string representation of the rectangle that can
        recreate a new instance using eval().

        Returns:
            str: String representation of the rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Print a message when a Rectangle instance is deleted
        and decrement the instance counter.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
