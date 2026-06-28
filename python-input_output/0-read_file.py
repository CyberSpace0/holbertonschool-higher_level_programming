#!/usr/bin/python3
"""Module containing lookup function."""

def read_file(filename=""):
    """read function"""
    with open(filename,"r") as file:
        print(file.read().strip())
