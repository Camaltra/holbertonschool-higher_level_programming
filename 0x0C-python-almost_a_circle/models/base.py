#!/usr/bin/python3
"""
Create the fundement of geometric stuff
"""

import json
import csv
from turtle import *


class Base:
    """
    Create a base class for geometry purpose
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Init the class
        Args:
            self (class)
            id (int): The id of the created form
        Returns: Anything
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dict into a str (as json format)
        Args:
            list_dictionaries (list): A list of all dict
        Returns: A str format
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of object from a class, (covert it into list of dict,
        then into json str) into a file named ClassName.json
        Args:
            cls (class)
            list_objs (list): A list of object
        Returns: Anything
        """
        filename = cls.__name__ + ".json"
        list_dictionary = []
        if list_objs is not None:
            for obj in list_objs:
                list_dictionary.append(cls.to_dictionary(obj))

        with open(filename, "w+", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dictionary))

    @staticmethod
    def from_json_string(json_string):
        """
        Take a json str format, and put it into list of dict
        Args:
            json_string (str): The input
        Returns: A list of dict of these objects
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance from a dict
        Args:
            dictionary (dict): The data
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(23, 31)
        else:
            dummy = cls(7)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Load geometry data from a file, then create the figure
        Args:
            cls (class)
        Returns: The list of the created figure
        """
        filename = cls.__name__ + ".json"
        listOfInstance = []
        try:
            with open(filename, "r") as f:
                buf = f.read()
                listOfInstance = cls.from_json_string(buf)
                for i in range(len(listOfInstance)):
                    listOfInstance[i] = cls.create(**listOfInstance[i])
        except FileExistsError:
            pass
        return listOfInstance

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Save instances into cvs file
        Args:
            list_objs (list): List of obj to save into csv
        Returns: Anything
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w+", encoding="utf-8") as f:
            writer = csv.writer(f)
            for elem in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow(
                        [elem.id, elem.width, elem.height, elem.x, elem.y]
                        )
                else:
                    writer.writerow([elem.id, elem.size, elem.x, elem.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Load instance from csv file
        Args:
        Returns: A list of all instances
        """
        filename = cls.__name__ + ".csv"
        listOfObjs = []
        try:
            with open(filename, "r") as f:
                reader = csv.reader(f)
                for elem in reader:
                    if cls.__name__ == "Rectangle":
                        newObj = {
                            "id": int(elem[0]),
                            "width": int(elem[1]),
                            "height": int(elem[2]),
                            "x": int(elem[3]),
                            "y": int(elem[4]),
                        }
                    else:
                        newObj = {
                            "id": int(elem[0]),
                            "size": int(elem[1]),
                            "x": int(elem[2]),
                            "y": int(elem[3]),
                        }
                    newObj = cls.create(**newObj)
                    listOfObjs.append(newObj)
            return listOfObjs
        except FileExistsError:
            return []

    def draw(list_rectangles, list_squares):
        """
        Draw the given rectangle, or square
        Args:
            list_rectangles (list): List of all instances of rectangle to draw
            list_squares (list): list of all instances of square to draw
        Returns: Anything
        """
        wn = turtle.Screen()
        turtle.bgcolor("#61657F")
        myLittleTurtle = turtle.Turtle()
        myLittleTurtle.shape("circle")

        for elem in list_rectangles:
            myLittleTurtle.up()
            myLittleTurtle.goto(elem.x, elem.y)
            myLittleTurtle.down()
            for i in range(2):
                myLittleTurtle.fd(elem.width)
                myLittleTurtle.lt(90)
                myLittleTurtle.fd(elem.height)
                myLittleTurtle.lt(90)

        for elem in list_squares:
            myLittleTurtle.up()
            myLittleTurtle.goto(elem.x, elem.y)
            myLittleTurtle.down()
            for i in range(4):
                myLittleTurtle.fd(elem.size)
                myLittleTurtle.lt(90)

        myLittleTurtle.hideturtle()
        turtle.exitonclick()
