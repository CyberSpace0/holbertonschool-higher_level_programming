#!/usr/bin/python3
""" Module Containing Student class"""
import pickle


def serialize_and_save_to_file(data, filename):
    """serialize"""
    with open(filename,"wb", encoding='utf-8') as f:
        pickle.dump(data, f)

def load_and_deserialize(filename):
    """desirialize"""
    with open(filename, "rb", encoding='utf-8') as rd:
        load = pickle.load(rd)
    return load
