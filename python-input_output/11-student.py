#!/usr/bin/python3
"""Module containing Student class."""


class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the instance.

        If attrs is a list of strings, only those attributes
        are returned. Otherwise, all attributes are returned.
        """
        if type(attrs) is list and all(type(attr) is str for attr in attrs):
            return {
                key: value
                for key, value in self.__dict__.items()
                if key in attrs
            }
        return self.__dict__
    
    def reload_from_json(self, json):
        """Replace all attributes using a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
