#!/usr/bin/python3
import pickle
""" Module Containing Student class"""


def serialize_and_save_to_file(data, filename):
    """serialize"""
    return pickle.dump(data,filename)

def load_and_deserialize(filename):
    """desirialize"""
    return pickle.load(filename)
