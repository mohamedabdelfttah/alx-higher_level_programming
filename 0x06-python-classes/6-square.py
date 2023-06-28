#!/usr/bin/python3
"""class that defines a square """


class Square:
    """
     a class Square that defines a square by: (based on 5-square.py)
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

    @property
    def position(self):
        """
        Return The position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Property setter for position.

        Args:
            value (tuple): position of the square.

        Raises:
            TypeError: position must be a tuple of 2 positive integers
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        print in stdout the square with  #
        """

        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ",  end="")
                print("#" * (self.__size))
