#!/usr/bin/python3
"""Module containing lookup function."""

def read_file(filename=""):
    """read function"""
    try:
        with open(filename, "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Permission denied")
