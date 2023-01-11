#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
Authored: Muaharraff Ibrahim
"""
import json


def load_from_json_file(filename):
    """
    loads an object from json file

    Args:
        filename (str): The name of the output file

    Return:
        A file with a text in json format
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
