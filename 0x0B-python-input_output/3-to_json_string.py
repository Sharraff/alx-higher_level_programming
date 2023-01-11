#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Authored: Musharraff Ibrahim
"""

def to_json_string(my_obj):
    """
    serializes a python object string

    Args:
        my_obj (str): python object

    Returns:
        JSON representation of an object string
    """
    import json
    return json.dumps(my_obj)
