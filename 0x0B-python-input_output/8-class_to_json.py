#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
Authored: Musharraff Ibrahim
"""


def class_to_json(obj):
    """Return the dictionary representation
    of a simple data structure.
    """
    return obj.__dict__
