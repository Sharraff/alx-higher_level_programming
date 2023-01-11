#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
Authored: Musharraff Ibrahim
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes a serialized object to a file

    Args:
        my_obj (str): obect to serialize
        filename (str): name of file to save object to
    Returns:
        json representation of python object
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
