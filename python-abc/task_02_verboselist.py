#!usr/bin/python3
"""Module for demonstrating extending built-in classes in Python."""


class VerboseList(list):
    """A list subclass that prints notifications when modified."""

    def append(self, item):
        """Add an item to the end of the list and print notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, item):
        """Extend the list with items and print notification."""
        count = len(item)
        super().extend(item)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Remove an item from the list and print notification."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Remove and return an item at the given index and print notification."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
