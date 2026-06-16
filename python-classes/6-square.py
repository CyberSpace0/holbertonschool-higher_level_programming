#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """This class represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with a validated size."""
        self.size = size
        self.position = position

    @property
    def position(self):
        """Retrive teh position"""
        return self.__position
    
    @position.setter
    def position(self, value):
        """Set the position of the square."""
        if (
            type(value) is not tuple
            or len(value) != 2
            or type(value[0]) is not int
            or type(value[1]) is not int
            or value[0] < 0
            or value[1] < 0
        ):
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )
    
        self.__position = value


    @property
    def size(self):
        """Retrive"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the value of size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """returns the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """print # as squares"""
        for i in range(self.size):
            for x in range(self.size):
                print("#", end="")
            print("")
        if (self.size == 0):
            print("")
            return
