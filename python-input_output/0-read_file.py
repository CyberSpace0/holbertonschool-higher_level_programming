#!/usr/bin/python3
"""Module containing lookup function."""

def read_file(filename=""):
    """read function"""
    try:
        with open(filename, "r") as file:
            print(file.read().strip())
    except FileNotFoundError:
        print(f"[FileNotFoundError] [Errno 2] No such file or directory: '{filename}'")
    except PermissionError:
        raise PermissionError
