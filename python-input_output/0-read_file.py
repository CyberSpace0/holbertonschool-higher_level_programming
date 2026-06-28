#!/usr/bin/python3
"""Module containing lookup function."""

def read_file(filename=""):
    """read function"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            print(file.read(), end="")
    except FileNotFoundError:
        print(f"[FileNotFoundError] [Errno 2] No such file or directory: '{filename}'")
    except PermissionError:
        raise PermissionError
