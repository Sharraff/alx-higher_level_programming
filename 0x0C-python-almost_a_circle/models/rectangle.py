#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
Author: Musharraff Ibrahim
"""
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle

    inheritance:
        Base (super class): defines the base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        class constructor for rectangle

        Attributes:
            width (int): Private attribute for the width of the Rectangle
            height (int): Private attribute for the height of the Rectangle
            x (int): Private attribute for x value of the Rectangle
            y (int): Private attribute for y value of the Rectangle
            id (int): Private attribute id inherits form Base
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        width getter for Rectangle class

        Returns:
            returns the rectangle width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter for Rectangle class

        Attribute:
            value (int): value to be set
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        width getter for Rectangle class

        Returns:
            value (int): the Rectangle height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter for Rectangle

        Attribute:
            value (int): value to be set
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        x getter method for rectangle

        Return:
            Private value of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter method for x value

        Attribute:
            value (int): value to set
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be an integer")
        self.__x = value

    @property
    def y(self):
        """
        getter method for y value

        Attribute:
            value (int): value to get
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter method for y value

        Attribute:
            value (int): value to set
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        area method for Rectangle class

        Returns:
            area of the Rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        display function that prints the
        rectangle
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.x):
                print(' ', end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """
        string representation of the rectangle class
        """
        str_rep = "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.__width, self.__height)
        return str_rep

    def update(self, *args, **kwargs):
        """
        Updates rectangle class

        Atrribute:
            args (list): inputted arguments to updating Rectangle class
            kwargs (dict): key, value pairs for updating Rectangle class
        """
        if args is not None and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
        elif kwargs is not None and len(kwargs) != 0:
            for (key, value) in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        returns the dictionary representation of the rectangle class
        """
        return {"x": self.x, "y": self.y, "id": self.id,
            "height": self.height, "width": self.width}
