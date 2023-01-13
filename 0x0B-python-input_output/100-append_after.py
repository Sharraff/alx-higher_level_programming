#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
Author: Musharraff Ibrahim
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line after each line containing a specific string

    Args:
        filename (str): name of the file
        search_string (str): The string to match
        new_string (str): The string to insert after matching
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        lines = f.readlines()

    for i in range(len(lines)):
        if search_string in lines[i]:
            lines.inserti + 1, (new_string)

    with open(filename, mode="w", encoding="utf-8") as file:
        content = "".join(lines)
        file.write(content)
