#!/usr/bin/python3
""" class BaseGeometry """

class BaseGeometry:
    """Reprsent base geometry."""

    def area(self):
        """Not implemented yet."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Constutor.

        Args:
            name (str): parameter name.
            value (int): parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
