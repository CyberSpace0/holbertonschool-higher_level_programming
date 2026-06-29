#!/usr/bin/python3
"""Module containing read_file function."""
import json


def class_to_json(obj):
    """Json to Object"""
    return obj.__dict__
