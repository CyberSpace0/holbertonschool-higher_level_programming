#!/usr/bin/python3
"""Module containing read_file function."""
import json


def from_json_string(my_str):
    """Json to Object"""
    return json.loads(my_str)
