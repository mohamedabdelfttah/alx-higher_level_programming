#!/usr/bin/python3
"""class that defines a square """


class Square:
    """
     a class Square that defines a square by: (based on 3-square.py)
    """
    def __init__(self, size=0):
        """
        Initialize a Square object.

        Args:
            size : The size of the square.
        """
        self.__size = size

    def area(self):
        """
        Calculates the area of square.

        Returns: the current square area.
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Return the size of a square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Property setter for size.

        Args:
            value (int): size of a square.

        Raises:
            TypeError: If `size` is not an integer.
            ValueError: If `size` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
