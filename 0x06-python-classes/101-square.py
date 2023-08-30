#!/usr/bin/python3
"""Module class Square."""
class Square:
    """Represent a square."""
    def __str__(self):
        """Define the print() representation of a Square."""

        return self.my_sprint()[:-1]

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): size of the new square.
            position (int, int): The position of the new square.
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set the current size of the square."""

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
        """Get/set the current position of the square."""

        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
         len([x for x in value if isinstance(x, int) and x >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Return the current area of the square."""

        return self.__size ** 2

    def my_sprint(self):
        """Print the square with the # character."""

        res = ""
        if not self.size:
            return "\n"

        for i in range(self.position[1]):
                res += "\n"
        for i in range(self.size):
            for j in range(self.position[0]):
                res += " "
            for j in range(self.size):
                res += "#"
            res += "\n"
        return res

    def my_print(self):

        print(self.my_sprint(), end="")
