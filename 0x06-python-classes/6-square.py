#!/usr/bin/python3
"""Square module."""


class Square:
    """Represents a square."""

    def __str__(self):
        self.my_print()

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size: Length of a side of the square.
            position: Position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Property of a size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Property of position of the square.

        Raises:
            TypeError: If value is not tuple of 2 positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
         len([x for x in value if isinstance(x, int) and x >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Area of the square.

        Returns:
            The size squared.
        """
        return self.__size ** 2

    def my_sprint(self):
        """Returns string rep of square."""
        res = ""
        if not self.size:
            return "\n"

        for a in range(self.position[1]):
                res += "\n"
        for a in range(self.size):
            for b in range(self.position[0]):
                res += " "
            for b in range(self.size):
                res += "#"
            res += "\n"
        return res

    def my_print(self):
        """Prints square."""
        print(self.my_sprint(), end="")
