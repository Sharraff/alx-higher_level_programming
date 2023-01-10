#!/usr/bin/python3
"""
Authored by Musharraff Ibrahim
"""


class MyInt(int):
    """
    A class that inherits from int
    """
    def __eq__(self, num):
        """
        equal function for MyInt class

        Attributes:
            num (int):an inputed integer

        Returns:
            the oppositive boolean of the input
        """
        return (int(self) != num)

    def __ne__(self, num):
        """
        no equal function for MyInt class

        Attributes:
            num (int): an inputed integer

        Returns:
            the oppositive boolean of the input
        """
        return (int(self) == num)
