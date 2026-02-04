#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Represents a rectangle.

    Attributes:
        __width (int): width of rectangle
        __height (int): heightrectangle
    """

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """

        self.width = width
        self.height = height

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
