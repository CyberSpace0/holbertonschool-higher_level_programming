#!/usr/bin/python3
"""Module containing read_file function."""
import json


def to_json_string(my_obj):
    """Read a UTF-8 text file."""
    return json.dumps(my_obj)
