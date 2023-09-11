#!/usr/bin/python3
"""Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square."""

    def __init__(self, size):
        """Constutor.

        Args:
            size (int): The size of the new square.
        """
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
