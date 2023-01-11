#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Authored: Musharraff Ibrahim
"""


def append_write(filename="", text=""):
    """
    appends a text to a file

    Args:
        filename (str): the name of the ile to write to
        text (str): text writen to file
    Returns:
        number of characters writen
    """
    with open(filename, mode="a+", encoding='utf-8') as f:
        return f.write(text)
