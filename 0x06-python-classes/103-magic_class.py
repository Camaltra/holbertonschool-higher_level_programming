#!/usr/bin/python3

import math

"""Create a Magic Class"""


class MagicClass:
    """Magic Class"""
    def __init__(self, radius=0):
        """
        Init the circle
        Args:
            radius (int or float): Radius of the circle
        Raises:
            TypeError: Not an int or float
        Returns: Nothing
        """
        self.__radius = 0
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calcul the area of the circle
        Returns: The area of the circle
        """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """
        Calcul the circumference of the circle
        Returns: The circumference of the circle
        """
        return (2 * math.pi * self.__radius)
