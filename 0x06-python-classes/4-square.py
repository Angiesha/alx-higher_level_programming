#!/usr/bin/python3

"""Define a class Square (based on 3-square.py)."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.
            Args:
                size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Getter/Accessor function: Retrieves square size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter/Mutator function: Sets square size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return (self.__size ** 2)
