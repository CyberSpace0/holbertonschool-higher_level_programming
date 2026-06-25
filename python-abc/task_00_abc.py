#!/usr/bin/python3
"""Module containing Rectangle class."""
from abc import ABC, abstractmethod


class Animal:
    """Animal"""
    @abstractmethod
    def sound(self):
        """sound function"""
        pass
    
class Dog(Animal):
    """dog"""
    def sound(self):
        """sound function"""
        return "Bark"

class Cat(Animal):
    """cat"""
    def sound(self):
        """sound function"""
        return "Meow"
