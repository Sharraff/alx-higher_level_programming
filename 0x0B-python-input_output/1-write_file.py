#!/usr/bin/python3
# -*- coding: utf-8 -*-


def write_file(filename="", text=""):
    """
    writes inputed text to a utf-8encoded file

    Args:
        filename (str): The name of the file to open
        text (str): The text to write in
    Returns:
        A file with text writen in
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
