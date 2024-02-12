#!/usr/bin/python3
<<<<<<< HEAD
"""
Define an empty class
"""


class Square:
    """
    square class
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
=======
"""Define a square class"""


class Square:
    """Define a square"""
    def __init__(self, size=0):
        """
        Initialize a new Square instance

        Args:
            size (int): The size of the square
         """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    @property
    def size(self):
        """Retrives the size of the square"""
>>>>>>> 0e95aceeb45e5e3639bc262a4ec821c6e9fc177b
        return self.__size

    @size.setter
    def size(self, value):
<<<<<<< HEAD
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2
=======
        """
        Sets the size

        Args:
            value (int): The value of the size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
>>>>>>> 0e95aceeb45e5e3639bc262a4ec821c6e9fc177b
