#!/usr/bin/python3
"""Defines a Rectangle Class."""


class Rectangle:
    """
    Class defines a rectangle by: (based on 8-rectangle.py)

    Args:
        width: integer indicating the width.
        height: integer indicating the height.
        number_of_instances: Public class attribute
        print_symbol: Public class attribute
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle object.

        With width and height.

        Args:
            width: An integer to object width.

            height: An integer to object height.

        """
        Rectangle.number_of_instances += 1
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns a string  filled with the '#' character."""
        if self.__height == 0 or self.__width == 0:
            return ""
        rec_str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += str(self.print_symbol)
            rec_str += "\n"
        return rec_str[:-1]

    def __repr__(self):
        """Return a string representation of the Rectangle
        to be able to recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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

    def area(self):
        """
        Public instance method.

        Returns:
            The rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        public instance method.

        Returns:
            The rectangle perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest Rectangle based on the area.

        Args:
            rect_1: Rectangle instance
            rect_2: Rectangle instance

        Returns: rect_1 if both rectangles have the same area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        """a new Rectangle instance with width == height == size

        Args:
            size: The size

        Returns:
            new Rectangle instance with width == height == size
        """
        return cls(size, size)
