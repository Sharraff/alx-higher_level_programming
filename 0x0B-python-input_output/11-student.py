#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
Authored: Musharraff Ibrahim
"""


class Student:
    """
    public class that defines a student class
    """

    def __init__(self, first_name, last_name, age):
        """
        initialises a new student

        Args:
            first_name (str): The first name of the student
            last_name (str): the last ne of the student
            age (int): The age of the student
        Return:
            returns the dictionary representation of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        represents students in to json format

        Attributes:
            attrs (dict): A python object to convert

        Returns:
            student class as a json format
        """
        if attrs is None:
            return self.__dict__
        return {key: value for key, value in self.__dict__.items()
                if key in attrs}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the student instance

        Attributes:
            attrs (dict): A python object to format

        Return:
            Student class as a json format
        """
        for key, value in json.items():
            setattr(self, key, value)
