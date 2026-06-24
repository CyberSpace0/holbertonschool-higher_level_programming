#!/usr/bin/python3
"""Module containing lookup function."""


class MyList(list):
    """list class"""
    def print_sorted(self):
        """Return the list of available attributes and methods."""
        print(sorted(self))
