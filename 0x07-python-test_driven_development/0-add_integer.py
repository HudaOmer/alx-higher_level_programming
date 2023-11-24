#!/usr/bin/python3
"""

a module for a function that adds two numbers

"""


def add_integer(a, b=98):
    """ a function that adds two integer and/or float numbers

    Args:
        a: first number
        b: second number

    Returns:
        the sum of given numbers

    Raises:
        TypeError: if a or b aren't integer / float

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
