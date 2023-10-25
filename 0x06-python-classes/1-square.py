#!/usr/bin/python
"""
Module: square
This module defines a Square class.
"""

class Square:
    """
    Class to represent a square.

    Attributes:
        size (int): The size of the square.

    Methods:
        __init__(self, size): Initializes a new Square instance.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
