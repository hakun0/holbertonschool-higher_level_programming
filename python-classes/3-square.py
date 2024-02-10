#!/usr/bin/python3
"""Define a square"""


class Square:
    """
    Initialize a new Square instance

    Parameters:
        size (int): The size of the square
    """
    def __init__(self, size=0):
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance:
            raise TypeError("size must be an integer")
        self.__size = size

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2
