#!/usr/bin/python3
"""
Authored by Musharraff Ibrahim
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A Rectangle class shape, inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        init function for rectangle

        Attributes:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
