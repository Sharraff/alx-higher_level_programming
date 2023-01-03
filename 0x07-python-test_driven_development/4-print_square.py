#!/usr/bin/python3


def print_square(size):
    """
    print a square of char #

    Args:
        size (int): size of the square
    Raises:
        TypeError: Exception if size is not integer
        ValueError: Exception if size is less than 0
    """
    if size is 0:
        return
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    print('\n'.join('#' * size for x in range(size)))
