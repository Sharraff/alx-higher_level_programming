#!/usr/bin/python3
"""
Authored by Musharraff Ibrahim
"""


def is_kind_of_class(obj, a_class):
    """
    A function that returns true if the object is
    an instance of the class, or the object is
    specified to the class

    Args:
        obj: the class object
        a_class: the class
    """
    if isinstance(obj, a_class):
        return True
    return False
