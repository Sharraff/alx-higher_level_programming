#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
Author: Musharaff Ibrahim
"""


def pascal_triangle(n):
    """
    Creates a pascal triangle

    Attributes:
        n (n): The n exponent for triangle
    return:
        A matrix with values for the triangle
    """
    pascal = []
    triangle = []

    for i in range(int(n)):
        new = pascal[:]
        new.append(1)
        pos = len(pascal)
        for i in range(1, pos):
            new[i] = pascal[i - 1] + pascal[i]
        pascal = new[:]
        triangle.append(pascal)
    return triangle
