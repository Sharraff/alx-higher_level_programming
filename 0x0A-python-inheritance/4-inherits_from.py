#!/usr/bin/python3
"""
Authored by Musharraff Ibrahim
"""


def inherits_from(obj, a_class):
    """
    function returns true if the object is derived
    or inherited from the base class

    Args:
        obj: class object
        a_class: the object class
    """
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
