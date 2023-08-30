#!/usr/bin/python3
"""Square module."""
class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: Length of a side of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        try:
            self.__size = size
            if size < 0:
                raise ValueError
            if type(size) is not int:
                raise TypeError
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")

    def area(self):
        """Area of this square.

        Returns:
            The size squared.
        """
        return self.__size * self.__size
