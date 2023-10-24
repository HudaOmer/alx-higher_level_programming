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
