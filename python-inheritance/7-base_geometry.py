#!/usr/bin/python3
"""Module containing BaseGeometry function."""


class BaseGeometry:
    """BaseGeometry"""
    def area(self):
        """raise exception message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validator"""
        if (isinstance(value, int) and type(value) is int ):
            raise TypeError(f"{name} must be an integer")
        elif (value <= 0):
            raise ValueError(f"{name} must be greater than 0")
