#!/usr/bin/python3
"""Module containing read_file function."""
import json


def save_to_json_file(my_obj, filename):
    """Json to Object"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
