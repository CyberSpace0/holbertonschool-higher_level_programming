#!/usr/bin/python3
"""Module containing Rectangle class."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        self.integer_validator(f"{size}", size)
        
        self.__size = size
