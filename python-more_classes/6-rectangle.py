#!/usr/bin/python3
"""Module For Recentangle"""


class Rectangle:
    """Rectangle class"""
    number_of_instances = 0
    
    def __init__(self, width=0, height=0):
        """Initialization"""
        self.width = width
        self.height = height
        number_of_instances += 1

    

    @property
    def width(self):
        """Getter for Width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for Width"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")

        elif (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for width"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for Width"""
        if (type(value) is not int):
            raise TypeError("height must be an integer")

        elif (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Recentangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """perimeter of recenangle"""
        if (self.__height == 0 or self.__width == 0):
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """Return the rectangle with # characters."""
        if (self.__width == 0 or self.__height == 0):
            return ""

        rect = ""

        for i in range(self.__height):
            rect += "#" * self.__width

            if i != self.__height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        """Documentaion for repr"""
        return "Rectangle(2, 4)"

    def __del__(self):
        """Delete function"""
        self.number_of_instances -= 1
        print("Bye rectangle...")
