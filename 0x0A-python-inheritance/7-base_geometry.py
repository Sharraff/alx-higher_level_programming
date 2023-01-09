#!/usr/bin/python3
"""
Authored by Musharraff Ibrahim
"""


class BaseGeometry:
    """
    An empty class
    """
    pass

    def area(self):
        """
        public instance method that calculates the area

        Raises:
            Exception if area is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        public instance method that validates integer input
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
