#!/usr/bin/python3

"""
A class that defines a square.
"""


class Square:
    """
    Class that defines properties of square by: (based on 1-square.py).
    """
    def __init__(self, size=0):
        """
        Initialize a Square object.

        Args:
            size : The size of the square.

        Raises:
            TypeError: If `size` is not an integer.
            ValueError: If `size` is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
