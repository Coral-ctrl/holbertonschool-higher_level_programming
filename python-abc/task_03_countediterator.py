#!usr/bin/python3
"""
Module for demonstrating iterator in Python.
This module contains a CountedIterator class that extends the functionality
of built-in iterators by tracking the number of items iterated.
"""


class CountedIterator:
    """An iterator wrapper that counts the number of items iterated."""

    def __init__(self, iterable):
        """Initialize the CountedIterator with an iterable."""
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Return the iterator object itself."""
        return self

    def __next__(self):
        """Fetch the next item from the iterator and increment the counter."""
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except Exception:
            raise StopIteration("no items left to iterate")

    def get_count(self):
        """Return the current count of items iterated."""
        return self.count
