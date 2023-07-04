#!/usr/bin/python3
"""Defines a Rectangle Class."""


class Rectangle:
    """
    Class defines a rectangle by: (based on 0-rectangle.py)

    Args:
        width: integer indicating the width.
        height: integer indicating the height.
    """
    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle object.

        With width and height.

        Args:
            width: An integer to object width.

            height: An integer to object height.

        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Get the width attribute value.

        Returns:
            The width  attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width private attribute value.

        Validates the assignment of the width private attribute.

        Arg:
            value: the value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height attribute value.

        Returns:
            The height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height attribute value.

        Validates the assignment of the height private attribute.

        Arg:
            value: the value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
