#!/usr/bin/python3
"""A Module that DEFINES a Square Class"""


class Square:
    """A Class that REPRESENTS a Square"""

    def __init__(self, size=0):
        """Initialize a Square instance with
        a size that has a positive int value
        Args:
            size: a private instance attribure
            that holds the size of the square
        Raises:
            TypeError: if size isn't int
            ValueError: if size is negative"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """A Method that returns the size i.e
        getter
        Returns:
            size of square
        """

        return self.__size

    @size.setter
    def size(self, value):
        """A Method that sets the size i.e
        setter
        Args:
            value: to set for size
        Raises:
            TypeError: if size isn't int
            ValueError: if size is negative"""

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """A Method that returns the area
        of the square
        Returns:
            area of the square
        """

        return self.__size ** 2

    def my_print(self):
        """A Method that prints a square with #"""

        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)
