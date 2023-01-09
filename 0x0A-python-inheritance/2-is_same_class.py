#!/usr/bin/python3
"""
Authored by Musharraff Ibrahim
"""


def is_same_class(obj, a_class):
    """
    A function that returns True if the object is
    an instance of the specified class

    Args:
        obj: object of the class
        a_class: the class
    """
    if isinstance(type(obj), a_class):
        return True
    return False
