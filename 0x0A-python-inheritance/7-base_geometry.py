#!/usr/bin/python3

"""
Module: 6-base_geometry
"""


class BaseGeometry:
    """
    A base geometry class.
    """

    def area(self):
        """
        Calculates the area.
        Raises an exception indicating that the area() method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value as an integer.
        Raises a TypeError if the value is not an integer.
        Raises a ValueError if the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

