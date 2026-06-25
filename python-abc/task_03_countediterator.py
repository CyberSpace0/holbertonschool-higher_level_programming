#!/usr/bin/python3
"""Module containing CountedIterator."""


class CountedIterator:
    """Iterator that counts fetched items."""

    def __init__(self, iterable):
        """Initialize iterator and counter."""
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Return next item and increment counter."""
        item = next(self.iterator)
        self.count += 1
        return item

    def __iter__(self):
        """Return iterator object."""
        return self

    def get_count(self):
        """Return number of fetched items."""
        return self.count
