#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """This class represents a square."""

    def __init__(self, size=0):
        """Initialize a square with a validated size."""
        def size(self, value): 
            if type(value) is not int:
                raise TypeError("size must be an integer")

            if value < 0:
                raise ValueError("size must be >= 0")

            self.__size = value
            return self.__size

    def area(self):
        """returns the current square area"""
        return self.__size * self.__size

print(Square().area())