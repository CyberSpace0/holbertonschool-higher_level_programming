#!/usr/bin/python3
"""Module containing read_file function."""


def write_file(filename="", text=""):
    """Read a UTF-8 text file."""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
