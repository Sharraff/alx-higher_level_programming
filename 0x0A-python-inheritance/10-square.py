#!/usr/bin/python3
"""
Authored by Musharraff Ibrahim
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class that instanciates a new class square
    """
    def __init__(self, size):
        """
        initializes a square

        Attributes:
            size: size of square
        """
        self.__size = size
        self.__integer_validator = ("size", size)
        super().__init__(size, size)
        self.__size = size
