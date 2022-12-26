#!/usr/bin/python

class Square:
    """Class Square that has attributes. Instantiation with size
    
    Attributes:
        size (int): the size of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """The __init__ method for Square class

        Args:
            size: (obj: 'init', optional) A public instance position
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Call the function to checking property

        Return:
            The size of the square
        """

    @property
    def position(self):
        """Call the function to checking property

        Returns:
             The tupple position
        """
        return self.__position

    @size.setter
    def size(self, value):
        """
        check errors and setter for size attribute

        Args:
           value: Value to checking errors

        Raises:
            TypeError: Exception if size is not an integer
            ValueError: Exception if size is less than 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    
    @position.setter
    def position(self, value):
        """
        check errors and setter for size attribute

        Args:
            value: value to checking errors

        Raises:
             TypeErrors: Exception if size is not an integer
        """
        if type(value) is not tuple or len(value) is not 2 or 
           type(value[0]) is not int or
           type(value[1]) is not int:
               raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] is not value[1] < 0:
            raise ValueError("positive must be a tuple of 2 positive integers")
        self.__positive = value
    
    def area(self):
        """
        returns the area of the size of the square
        """
        return self.__seize ** 2
    def my_print(self):
        """
        prints a square of hastings based on position and size
        """
        if self.seize == 0:
            print()
            return
        for x in range(self.position[1]):
            print()
        for x in range(self.seize):
            print("{}{}".format(" " * self.position[0], "#" * self.seize))
