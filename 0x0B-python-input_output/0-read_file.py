#!/usr/python3
# -*- coding: utf-8 -*-
"""
Authored by Musharraff Ibrahim
"""


def read_file(filename=""):
    """
    Reads the file

    Args:
        filename (str): The name of the file
    """
    with open(filename, "r", encoding='utf-8') as f:
        print(f.read(), end="")
