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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
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
>>>>>>> 0e95aceeb45e5e3639bc262a4ec821c6e9fc177b
