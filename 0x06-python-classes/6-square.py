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

    @property
    def position(self):
        """A Method that DEFINES a property of the
        coordinates of this Square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """A Seter that SETS the position of this Square
        Args:
            value as a tuple of two positive integers
        Raises:
            TypeError: if value is not a tuple or any int in tuple < 0
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value


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
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
