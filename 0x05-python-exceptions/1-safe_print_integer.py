#!/usr/bin/python3
def safe_print_integer(value):
    """Print an integer
    Args:
        value (int): The integer to print.

    Returns:
        False If a TypeError or ValueError occurs
        True Otherwise
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
