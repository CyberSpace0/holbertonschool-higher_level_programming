#!/usr/bin/python3
"""Module containing read_file function."""


def read_file(filename=""):
    """Read a UTF-8 text file."""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
