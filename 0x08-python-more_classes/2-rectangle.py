#!/usr/python3


class Rectangle:
    """
    makes rectangle object

    Attributes:
        None
    """

    def __init__(self, width=0, height=0):
        """
        initializes a Rectangle object or instance

        Attributes:
            width (int, optional): The width of the rectangle
            height (int, optional): The height of the rectangle
        self.height = width
        self.width = width
        """
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """
        property height to retrieve

        Returns:
            height (int): The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter of the height of the rectangle

        Attributes:
            height (int): The height of the rectangle

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is not less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """
        Property width to retrieve it

        Returns:
            width (int): The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter width of the rectangle

        Attributes:
            width (int): The width of the Rectangle

        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """
        calculates the area of the rectangle

        Returns:
            The area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        calculates the perimeter of the rectangle

        Returns:
            The perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
