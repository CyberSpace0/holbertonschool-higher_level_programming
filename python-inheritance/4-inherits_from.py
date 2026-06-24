#!/usr/bin/python3
"""Module containing lookup function."""


def inherits_from(obj, a_class):
    """check status"""
    return isinstance(obj, a_class) and type(obj) is not a_class
