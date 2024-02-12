#!/usr/bin/python3
<<<<<<< HEAD
"""
Define an empty class
"""
=======
"""Define a square"""
>>>>>>> 0e95aceeb45e5e3639bc262a4ec821c6e9fc177b


class Square:
    """
<<<<<<< HEAD
    square class
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
=======
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
>>>>>>> 0e95aceeb45e5e3639bc262a4ec821c6e9fc177b
        return self.__size ** 2
