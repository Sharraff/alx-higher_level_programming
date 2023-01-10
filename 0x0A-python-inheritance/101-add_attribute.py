#!/usr/bin/python3
"""
Authored by Musharraff Ibrahim
"""


def add_attribute(obj, name, value):
    """
    Add attributes into the class if its possible

    Arguments:
        obj (object): the object to set as atrribute
        name (str): Name for the new attribute
        value (int): Value to new attribute
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
