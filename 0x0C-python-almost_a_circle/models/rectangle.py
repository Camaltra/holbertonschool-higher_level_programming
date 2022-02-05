#!/usr/bin/python3

from models.base import Base


class Rectangle(Base):
    """
    Create a rectangle
    """

    def __init__(self, witdh, height, x=0, y=0, id=None):
        """
        Init the class
        Agrs:
            self (class)
            width (int): The width
            height (int): The height
            x (int): The x position of the rectangle
            y (int): The y position of the rectangle
            id (int): The id of the rectangle, based on the Base class
        Raises:
            Check these setter and getter funtion
        Returns: Anything
        """
        self.width = witdh
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Get the width value
        Returns: The width value
        """
        return self.__width

    @property
    def height(self):
        """
        Get the height value
        Returns: The height value
        """
        return self.__height

    @property
    def x(self):
        """
        Get the x value
        Returns: The x value
        """
        return self.__x

    @property
    def y(self):
        """
        Get the y value
        Returns: The y value
        """
        return self.__y

    @width.setter
    def width(self, value):
        """
        Set the width value
        Args:
            value (int): The value to fill
        Returns: Anything
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Set the height value
        Args:
            value (int): The value to fill
        Returns: Anything
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """
        Set the x value
        Args:
            value (int): The value to fill
        Returns: Anything
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """
        Set the y value
        Args:
            value (int): The value to fill
        Returns: Anything
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculated the area of a rectangle
        Returns: The area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """
        Create the rectangle with # char
        Returns: Anything
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.x):
                print(" ", end="")
            for k in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """
        Describe the created rectangle.
        Returns: The infos about it
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """
        Update a rectangle components
        Args:
            args (List of arg): The new components sorted
                as: (id, width, height, x, y)
            kwargs (Dict): Dict of new components
        Returns: Anything
        """
        if len(args):
            i = 0
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.height = arg
                if i == 3:
                    self.x = arg
                if i == 4:
                    self.y = arg
                i += 1
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
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
        dict["height"] = self.height
        dict["width"] = self.width
        return dict
