#!/usr/bin/python3
"""Module containing read_file function."""


def append_write(filename="", text=""):
    """Read a UTF-8 text file."""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
