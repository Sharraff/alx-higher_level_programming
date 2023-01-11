#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Authored: Musharraff Ibrahim
"""
import json


def from_json_string(my_str):
    """
    Deserializes a JSON string to a python object

    Args:
        my_str (str): a json string to deserialize

    Returns:
        a python object
    """
    return json.loads(my_str)
