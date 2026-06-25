#!/usr/bin/python3
"""Module containing VerboseList class."""


class VerboseList(list):
    """List that prints notifications when modified."""

    def append(self, item):
        """Append item and print notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        """Extend list and print notification."""
        super().extend(items)
        print(f"Extended the list with {len(items)} items.")

    def remove(self, item):
        """Remove item and print notification."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop item and print notification."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
