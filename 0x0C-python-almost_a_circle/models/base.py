#!/usr/bin/python3
""" Defines a base class model."""
import json
import csv


class Base:
    """Represents the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.
        Args:
            id (int): The identity of the new Base.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.
        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if (list_dictionaries is None or list_dictionaries == []):
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON serialization of list_objs to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                json_file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string.
        Args:
            json_string (str): A JSON str representation of a list of dicts.

        Returns:
            If json string is empty or None: an empty list.
            else - The Python list represented by json_string.
        """
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set from dictionary.
        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances initialized from a file of JSON strings.
        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instances.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as json_file:
                list_dict = Base.from_json_string(json_file.read())
                return [cls.create(**d) for d in list_dict]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the CSV serialization of list_objs to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline='') as csv_file:
            if list_objs is None:
                csv_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writerows([obj.to_dictionary() for obj in list_objs])

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances instantiated frfom a CSV file.
         Reads from `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as csv_file:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                reader = csv.DictReader(csv_file, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in reader]
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []
