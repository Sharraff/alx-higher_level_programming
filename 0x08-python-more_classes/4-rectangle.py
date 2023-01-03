#!/usr/bin/python3

"""Area and perimeter

Task:
    calculate and print the area and perimeter of the rectangle
    """

class Rectangle:
    """
    class Rectangle that defines a rectangle figure

    Attributes:
        empty
    """
    def __inti__(self, width=0, height=0):
        """
        Init method for rectangle

        Attributes:
            width (int, optional): The width of the rectangle
            heght (int, optional): The height of the rectangle
        self.width = width
        self.height = height
        """
        self.width = width
        self.height = height

    def __str__(self):
        """
        str method to print rectangle

        Returns:
            The string with # rectangle
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string

        for i in range(self.__height):
            for j in range(self.__width):
                string += '#'
            if i < self.__height - 1:
                string += '\n'
        return string

    def __repr__(self):
        """
        provides __repr__ method for object rectangle

        Returns:
            string (str): string to get
        """
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height) +\
            ")"

    @property
    def height(self):
        """
        Property height to retrieve it

        Returns:
            height (int): The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter height of the rectangle

        Attributes:
            height (int): The height of the rectangle

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must an integer")
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
            width (int): The width of the rectangle

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
        calculate The area of the rectangle

        Returns:
            The area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        calculate the perimeter of the rectangle

        Returns:
            the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
