#!/usr/bin/python3

"""
Create a square from Rectangle class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Create a square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Init the square
        Args:
            size (int): Size of the square
            x (int): The x postion
            y (int): the y position
            id (all): Id of the square
        """
        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self):
        """
        Describe the created square.
        Returns: The infos about it
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """
        Getter function for size
        Returns: The size var
        """
        return self.witdh

    @size.setter
    def size(self, value):
        """
        Setter for size
        Args:
            self (class)
            value (int): The new value
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update a square components
        Args:
            args (List of arg): The new components sorted
                as: (id, size, x, y)
            kwargs (Dict): Dict of new components
        Returns: Anything
        """
        i = 0
        for arg in args:
            if i == 0:
                self.id = arg
            if i == 1:
                self.size = arg
            if i == 2:
                self.x = arg
            if i == 3:
                self.y = arg
            i += 1
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        Create a dict representation of the class
        Returns: The dict
        """
        dict = {}
        dict["x"] = self.x
        dict["y"] = self.y
        dict["id"] = self.id
        dict["size"] = self.size
        return dict
