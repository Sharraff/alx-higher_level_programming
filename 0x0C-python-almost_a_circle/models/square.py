#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
Author: Musharraff Ibrahim
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class square inherits from rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        class constructor for square

        Attribute:
            size (int): The size of the square
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        str method for class square

        Return:
            The string: [class_name] (id) x/y - size
        """
        string = "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
            self.id, self.x, self.y, self.size)
        return string

    @property
    def size(self):
        """
        getter method for size value

        Return:
            private value size value
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter method for size value

        Attribute:
            value (int): value to set
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value

    def update(self, *args, **kwargs):
        """
        Updates square class

        Attribute:
            args (list): inputted arguments to updating rectangle class
            kwargs (dict): inputted arguments to updating rectangle class
        """
        if args is not None and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        elif kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Returns a dictionary representation of Square class
        """
        return {"id": self.id, "x": self.x, "size": self.size,
            "y": self.y}
