#!/usr/bin/python3
"""Module containing read_file function."""
import json


def load_from_json_file(filename):
    """Json to Object"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
