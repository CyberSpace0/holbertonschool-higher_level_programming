#!/usr/bin/python3
""" Module is empty """


class Square:
    """class has private attribuate called size"""

    def __init__(self, size=0):
        """ class has specifc variable """
        if (type(size) != int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
