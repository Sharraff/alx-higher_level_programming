#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
Author: Musharraff Ibrahim
"""
import json


class Base:
    """
    class constructor

    Args:
        __nb_objects (int): private class attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor

        Attributes:
            id (int): An integer input for id
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return a json string representation

        Args:
            list_dictionarie (json): An inputed jason list of dictionaries
        Return:
            A json representation
        """
        if list_dictionaries is None or list_dictionaries:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of
        list_objs to a file

        Args:
            list_objs(): a list of instances who inherits of base
        """
        filename = cls.__name__ + "json"
        list_instance = []
        if list_objs is None:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(list_instance)
        else:
            for i in list_objs:
                list_instance.append(cls.to_dictionary(i))
            with open(filename, "w", encoding="utf-8") as f:
                f.write(cls.to_json_string(list_instance))

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list of the JSON string
        representation json_string

        Args:
            json_string (str): a string representing a list of dictionaries
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        A class method that that serialisese and
        deserializes in CSV
        """
        if list_objs is None or not isinstance(list_objs, list) or not +\
                all(isinstance(j, Base) for j in list_objs):
            with open(cls.__name__ + ".csv", "w", encoding="utf-8") as file:
                file.write("[]")
        if list_objs and any(isinstance(j, Base) for j in list_objs):
            dict_data = [i.to_dictionary() for i in list_objs]
            if cls.__name__ == "Rectangle":
                csv_columns = ["id", "width", "height", "x", "y"]
            else:
                csv_columns = ["id", "size", "x", "y"]
            with open(cls.__name__ + ".csv", "w", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=csv_columns)
                writer.writeheader()
                for data in dict_data:
                    writer.writerow(data)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns a instance with all attributes already set

        Args:
            **dictionary (pointer): can be thought of as a double
            pointer to a dictionary
        """
        if cls.__name__ == "Rectabgle":
            result = cls(32, 3)
            result.update(**dictionary)
            return result
        if cls.__name__ == "Square":
            result = cls(32)
            result.update(**dictionary)
            return result

    @classmethod
    def load_from_file_csv(cls):
        """
        loads from csv file
        """
        list_instance = []
        name = cls._name_ + ".csv"
        if os.path.isfile(name):
            with open(name, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    d = {key: int(value) for key, value in row.items()}
                    list_instance.append(cls.create(**d))
            return list_instance
        return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Draws square and rectangle"""
        for i in list_rectangles + list_squares:
            tt = turtle.Turtle()
            tt.shape("turtle")
            turtle.bgcolor("black")
            tt.fillcolor("white")
            tt.begin_fill()
            tt.pen(fillcolor="white", pencolor="red", pensize=2)
            for _ in range(2):
                tt.forward(i.width)
                tt.right(90)
                tt.forward(i.height)
                tt.right(90)
            tt.end_fill()
            turtle.done()
            turtle.done()
