#!/usr/bin/python3
"""class that defines a square """


class Square:
    """
     a class Square that defines a square by: (based on 2-square.py)
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

    def area(self):
        """
        Calculates the area of square.

        Returns: the current square area.
        """
        return self.__size ** 2
